import click
from click.testing import CliRunner

from pland_cli.enrichment.assignment_confirmations import assignment_confirmations_list

CONFIRMATION = {"_id": "c1", "documentType": "assignment_confirmation", "documentNumber": 1005}
INVOICE = {"_id": "i1", "documentType": "invoice", "documentNumber": 3117}


class FakeClient:
    """Serves the two calls the command makes; `broken` offers raise."""

    def __init__(self, related: dict, broken: set[str] = frozenset()):
        self.related, self.broken = related, broken

    def get(self, path, params=None):
        if path == "/offers/":
            return [{"_id": o} for o in self.related]
        oid = path.split("/")[2]
        if oid in self.broken:
            raise RuntimeError("boom")
        return self.related[oid]


def run(client, args=()):
    import pland_cli.enrichment.assignment_confirmations as mod

    original = mod.get_client
    mod.get_client = lambda ctx: client
    # paginate() would re-page the fake; the command's own /offers/ call is enough.
    original_paginate = mod.paginate
    mod.paginate = lambda c, path, params: c.get(path)
    try:
        return CliRunner().invoke(assignment_confirmations_list, list(args), obj={"as_json": True})
    finally:
        mod.get_client, mod.paginate = original, original_paginate


def test_collects_only_confirmations_and_tags_the_offer():
    client = FakeClient({"o1": [INVOICE, CONFIRMATION], "o2": [INVOICE]})
    result = run(client)
    assert result.exit_code == 0, result.output
    assert '"_id": "c1"' in result.output
    assert '"offerId": "o1"' in result.output
    assert "i1" not in result.output


def test_partial_failure_is_reported_not_swallowed():
    """A short list must never read as a complete one."""
    client = FakeClient({"o1": [CONFIRMATION], "o2": [CONFIRMATION]}, broken={"o2"})
    result = run(client)
    assert result.exit_code == 0
    assert "may be incomplete" in result.output
    assert "1 of 2 offers" in result.output


def test_offer_id_skips_the_walk():
    client = FakeClient({"o1": [CONFIRMATION]})
    calls = []
    original_get = client.get
    client.get = lambda path, params=None: (calls.append(path), original_get(path, params))[1]
    result = run(client, ["--offer-id", "o1"])
    assert result.exit_code == 0
    assert "/offers/" not in calls, "listing every offer defeats --offer-id"
    assert '"_id": "c1"' in result.output
