from pland_cli.core.pagination import collect_all


class FakeClient:
    """Liefert vorgegebene Seiten; simuliert den Overlap-Bug (doppelte _id)."""

    def __init__(self, pages):
        self.pages = pages
        self.calls = 0

    def get(self, path, params=None):
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
