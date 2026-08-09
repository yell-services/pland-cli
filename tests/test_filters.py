from pland_cli.enrichment._filters import filter_by_date_range


class FakeClient:
    def __init__(self, pages):
        self.pages = pages
        self.calls = 0

    def get(self, path, params=None):
        page = self.pages[self.calls] if self.calls < len(self.pages) else []
        self.calls += 1
        return page


def test_filters_clientside_by_field_and_dedups():
    pages = [
        [{"_id": "a", "from": 100}, {"_id": "b", "from": 250}],
        [{"_id": "b", "from": 250}, {"_id": "c", "from": 500}],  # overlap + outside
        [],
    ]
    out = list(filter_by_date_range(FakeClient(pages), "/salaries/", {"objectId": "o"},
                                    from_ms=100, to_ms=300, date_field="from"))
    assert [i["_id"] for i in out] == ["a", "b"]  # c (500) falls outside
