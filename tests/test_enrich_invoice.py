import json

import httpx
from click.testing import CliRunner

from pland_cli.cli import main


def test_drafts_filtered_clientside_by_object(monkeypatch):
    rows = [
        {"_id": "i1", "objectId": "o1", "fixDate": None},
        {"_id": "i2", "objectId": "o2", "fixDate": None},
        {"_id": "i3", "objectId": "o1", "fixDate": 1712000000000},  # fixiert → kein Entwurf
    ]

    def handler(request):
        return httpx.Response(
            200, json=rows if int(request.url.params.get("offset", "0")) == 0 else []
        )

    import pland_cli.enrichment.invoice as inv
    from pland_cli.core.client import PlandClient
    from pland_cli.core.config import Config
    monkeypatch.setattr(inv, "get_client", lambda ctx: PlandClient(
        Config(base_url="https://api.test/v2", api_key="k", profile="prod"),
        transport=httpx.MockTransport(handler)))

    result = CliRunner().invoke(main, ["--json", "invoice", "drafts", "--object-id", "o1"])
    assert result.exit_code == 0
    assert [r["_id"] for r in json.loads(result.output)] == ["i1"]


def test_strip_readonly_fields():
    from pland_cli.enrichment.invoice import strip_readonly
    body = strip_readonly({
        "_id": "x",
        "object": {},
        "customer": {},
        "recipient": {},
        "assignments": [],
        "previousInvoices": [],
        "totals": {},
        "status": "draft",
        "companyId": "c1",
        "attachedDocumentIds": ["a"],
        "note": "keep",
    })
    for ro in ("_id", "object", "customer", "recipient", "assignments",
               "previousInvoices", "totals", "status", "companyId"):
        assert ro not in body
    assert body["attachedDocumentIds"] == ["a"]
    assert body["note"] == "keep"
