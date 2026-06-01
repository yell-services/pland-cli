import json

import httpx
from click.testing import CliRunner

from pland_cli.cli import main


def _mk(handler):
    from pland_cli.core.client import PlandClient
    from pland_cli.core.config import Config
    return PlandClient(
        Config(base_url="https://api.test/v2", api_key="k", profile="prod"),
        transport=httpx.MockTransport(handler),
    )


def test_for_object_filters_clientside(monkeypatch):
    rows = [
        {"_id": "s1", "from": 1713175200000, "workingTime": 28800},  # 2024-04-15
        {"_id": "s2", "from": 1715767200000, "workingTime": 14400},  # 2024-05-15 (außerhalb)
    ]

    def handler(request: httpx.Request) -> httpx.Response:
        offset = int(request.url.params.get("offset", "0"))
        return httpx.Response(200, json=rows if offset == 0 else [])

    import pland_cli.enrichment.salaries as sal
    monkeypatch.setattr(sal, "get_client", lambda ctx: _mk(handler))

    result = CliRunner().invoke(
        main,
        ["--json", "salary", "for-object", "--object-id", "o1",
         "--from", "2024-04-01", "--to", "2024-04-30"],
    )
    assert result.exit_code == 0
    ids = [r["_id"] for r in json.loads(result.output)]
    assert ids == ["s1"]


def test_for_object_passes_object_id_param(monkeypatch):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["objectId"] = request.url.params.get("objectId")
        return httpx.Response(200, json=[])

    import pland_cli.enrichment.salaries as sal
    monkeypatch.setattr(sal, "get_client", lambda ctx: _mk(handler))

    result = CliRunner().invoke(
        main,
        ["--json", "salary", "for-object", "--object-id", "obj-42",
         "--from", "2024-04-01", "--to", "2024-04-30"],
    )
    assert result.exit_code == 0
    assert seen["objectId"] == "obj-42"
