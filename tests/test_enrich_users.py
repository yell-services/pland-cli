import json

import httpx
from click.testing import CliRunner

from pland_cli.cli import main


def test_users_active_filters_status(monkeypatch):
    rows = [
        {"_id": "u1", "status": {"status": "1"}, "general": {"firstName": "***"}},
        {"_id": "u2", "status": {"status": "2"}, "general": {"firstName": "***"}},
        {"_id": "u3", "status": None, "general": {"firstName": "***"}},
    ]

    def handler(request):
        return httpx.Response(
            200, json=rows if int(request.url.params.get("offset", "0")) == 0 else []
        )

    import pland_cli.enrichment.users as us
    from pland_cli.core.client import PlandClient
    from pland_cli.core.config import Config
    monkeypatch.setattr(us, "get_client", lambda ctx: PlandClient(
        Config(base_url="https://api.test/v2", api_key="k", profile="prod"),
        transport=httpx.MockTransport(handler)))

    result = CliRunner().invoke(main, ["--json", "users", "active"])
    assert result.exit_code == 0
    assert [r["_id"] for r in json.loads(result.output)] == ["u1"]
