import json

from pland_cli.core.client import PlandError
from pland_cli.core.pagination import collect_all


class FakeClient:
    """Liefert vorgegebene Seiten; simuliert den Overlap-Bug (doppelte _id)."""

    def __init__(self, pages, reject_sort=False):
        self.pages = pages
        self.calls = 0
        self.params_log = []
        self.reject_sort = reject_sort

    def get(self, path, params=None):
        self.params_log.append(dict(params or {}))
        if self.reject_sort and params and "sort" in params:
            raise PlandError(400, "Could not fetch list.",
                             "Sorting needs by and direction", {})
        page = self.pages[self.calls] if self.calls < len(self.pages) else []
        self.calls += 1
        return page


def test_collect_dedups_overlapping_ids():
    pages = [
        [{"_id": "a"}, {"_id": "b"}],
        [{"_id": "b"}, {"_id": "c"}],  # 'b' überlappt
        [],
    ]
    items = collect_all(FakeClient(pages), "/salaries/", page_size=2)
    assert [i["_id"] for i in items] == ["a", "b", "c"]


def test_collect_handles_items_envelope():
    pages = [{"items": [{"_id": "x"}]}, {"items": []}]
    items = collect_all(FakeClient(pages), "/x/", page_size=2)
    assert [i["_id"] for i in items] == ["x"]


def test_collect_stops_on_empty():
    items = collect_all(FakeClient([[]]), "/x/", page_size=2)
    assert items == []


def test_collect_sends_stable_sort():
    # Ohne stabile Sortierung liefert die API Seiten in zufaelliger
    # Reihenfolge → Duplikate + verlorene Datensaetze (506 von 1705).
    client = FakeClient([[{"_id": "a"}, {"_id": "b"}], []])
    collect_all(client, "/invoices/", page_size=2)
    for params in client.params_log:
        assert json.loads(params["sort"]) == {"by": "_id", "direction": 1}


def test_collect_respects_caller_sort():
    client = FakeClient([[{"_id": "a"}], []])
    collect_all(client, "/invoices/", {"sort": "custom"}, page_size=2)
    assert all(p["sort"] == "custom" for p in client.params_log)


def test_collect_falls_back_when_sort_rejected():
    # Endpoints ohne sort-Support → 400; Retry ohne sort, Dedup bleibt Backstop.
    client = FakeClient([[{"_id": "a"}, {"_id": "b"}], []], reject_sort=True)
    items = collect_all(client, "/legacy/", page_size=2)
    assert [i["_id"] for i in items] == ["a", "b"]
    assert "sort" in client.params_log[0]
    assert all("sort" not in p for p in client.params_log[1:])


def test_collect_does_not_drop_sort_on_server_error():
    # Ein 500 darf nicht als "Endpoint kennt sort nicht" durchgehen — sonst
    # liefe die Pagination still ohne stabile Sortierung weiter.
    class Failing(FakeClient):
        def get(self, path, params=None):
            self.params_log.append(dict(params or {}))
            raise PlandError(500, "Server", "boom", {})

    client = Failing([[]])
    try:
        collect_all(client, "/invoices/", page_size=2)
    except PlandError as exc:
        assert exc.status == 500
    else:
        raise AssertionError("PlandError erwartet")
    assert len(client.params_log) == 1  # kein Retry ohne sort


def test_collect_advances_by_delivered_rows():
    # /salaries/ deckelt serverseitig bei 200, egal welches limit angefragt
    # wird. Ein Offset, der um die *angeforderte* Groesse springt, ueberliest
    # die Differenz — gemessen 9800 statt 24483 Zeilen.
    class Capped(FakeClient):
        def get(self, path, params=None):
            self.params_log.append(dict(params or {}))
            offset = params["offset"]
            rows = [{"_id": f"r{i}"} for i in range(offset, min(offset + 2, 5))]
            return rows

    client = Capped([], )
    items = collect_all(client, "/salaries/", page_size=10)
    assert [i["_id"] for i in items] == [f"r{i}" for i in range(5)]
    assert [p["offset"] for p in client.params_log] == [0, 2, 4, 5]


def test_collect_raises_instead_of_truncating_on_endless_paging():
    # Server deckelt den Offset und reicht immer neue _ids nach: ohne
    # Obergrenze liefe das ewig. Ein Fehler ist besser als ein stilles Teilergebnis.
    class Endless(FakeClient):
        def __init__(self):
            super().__init__([])
            self.n = 0

        def get(self, path, params=None):
            self.n += 1
            return [{"_id": f"x{self.n}"}]

    try:
        collect_all(Endless(), "/x/", {"sort": "custom"}, page_size=1)
    except RuntimeError as exc:
        assert "im Kreis" in str(exc)
    else:
        raise AssertionError("RuntimeError erwartet")
