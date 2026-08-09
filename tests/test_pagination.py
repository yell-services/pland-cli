import json

from pland_cli.core.client import PlandError
from pland_cli.core.pagination import collect_all


class FakeClient:
    """Serves predefined pages; reproduces the overlap bug (duplicate _id)."""

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
        [{"_id": "b"}, {"_id": "c"}],  # 'b' overlaps
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
    # Without a stable sort the API returns pages in random order →
    # duplicates and lost records (506 of 1705).
    client = FakeClient([[{"_id": "a"}, {"_id": "b"}], []])
    collect_all(client, "/invoices/", page_size=2)
    for params in client.params_log:
        assert json.loads(params["sort"]) == {"by": "_id", "direction": 1}


def test_collect_respects_caller_sort():
    client = FakeClient([[{"_id": "a"}], []])
    collect_all(client, "/invoices/", {"sort": "custom"}, page_size=2)
    assert all(p["sort"] == "custom" for p in client.params_log)


def test_collect_falls_back_when_sort_rejected():
    # Endpoints without sort support → 400; retry without it, dedup stays as backstop.
    client = FakeClient([[{"_id": "a"}, {"_id": "b"}], []], reject_sort=True)
    items = collect_all(client, "/legacy/", page_size=2)
    assert [i["_id"] for i in items] == ["a", "b"]
    assert "sort" in client.params_log[0]
    assert all("sort" not in p for p in client.params_log[1:])


def test_collect_does_not_drop_sort_on_server_error():
    # A 500 must not pass as "this endpoint does not know sort" — pagination
    # would otherwise carry on silently without a stable order.
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
        raise AssertionError("expected a PlandError")
    assert len(client.params_log) == 1  # no retry without sort


def test_collect_advances_by_delivered_rows():
    # /salaries/ caps server-side at 200 no matter what limit is requested. An
    # offset that jumps by the *requested* size skips the difference — measured
    # 9800 instead of 24483 rows.
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
    # The server caps the offset and keeps handing back fresh _ids: without a
    # ceiling this runs forever. An error beats a silent partial result.
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
        assert "in circles" in str(exc)
    else:
        raise AssertionError("expected a RuntimeError")
