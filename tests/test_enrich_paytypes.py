import json

import httpx
from click.testing import CliRunner

from pland_cli.cli import main


def test_paytype_wage_resolves_fields(monkeypatch):
    seen = {}

    def handler(request):
        seen["path"] = request.url.path
        return httpx.Response(200, json={
            "_id": "pt1", "name": "Standard", "wage": 18.5, "extra": "ignored"
        })

    import pland_cli.enrichment.pay_types as pt
    from pland_cli.core.client import PlandClient
    from pland_cli.core.config import Config
    monkeypatch.setattr(pt, "get_client", lambda ctx: PlandClient(
        Config(base_url="https://api.test/v2", api_key="k", profile="prod"),
        transport=httpx.MockTransport(handler)))

    result = CliRunner().invoke(main, ["--json", "pay-types", "wage", "pt1"])
    assert result.exit_code == 0
    assert seen["path"] == "/v2/payTypes/pt1"
    payload = json.loads(result.output)
    assert payload == {"id": "pt1", "name": "Standard", "wage": 18.5}
