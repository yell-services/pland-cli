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


def test_in_range_filters_by_dtstart_and_status(monkeypatch):
    rows = [
        {"_id": "a1", "dtStart": 1713175200000, "approvedBy": "mgr"},   # 2024-04-15, approved
        {"_id": "a2", "dtStart": 1713607200000, "approvedBy": None},    # 2024-04-20, not approved
        {"_id": "a3", "dtStart": 1715767200000, "approvedBy": "mgr"},   # 2024-05-15 (out of range)
    ]

    def handler(request: httpx.Request) -> httpx.Response:
        offset = int(request.url.params.get("offset", "0"))
        return httpx.Response(200, json=rows if offset == 0 else [])

    import pland_cli.enrichment.absences as ab
    monkeypatch.setattr(ab, "get_client", lambda ctx: _mk(handler))

    result = CliRunner().invoke(
        main,
        ["--json", "absences", "in-range",
         "--from", "2024-04-01", "--to", "2024-04-30", "--approved-only"],
    )
    assert result.exit_code == 0
    assert [r["_id"] for r in json.loads(result.output)] == ["a1"]


def test_in_range_without_approved_only_keeps_all_in_window(monkeypatch):
    rows = [
        {"_id": "a1", "dtStart": 1713175200000, "approvedBy": "mgr"},   # 2024-04-15
        {"_id": "a2", "dtStart": 1713607200000, "approvedBy": None},    # 2024-04-20
        {"_id": "a3", "dtStart": 1715767200000, "approvedBy": "mgr"},   # 2024-05-15 (out of range)
    ]

    def handler(request: httpx.Request) -> httpx.Response:
        offset = int(request.url.params.get("offset", "0"))
        return httpx.Response(200, json=rows if offset == 0 else [])

    import pland_cli.enrichment.absences as ab
    monkeypatch.setattr(ab, "get_client", lambda ctx: _mk(handler))

    result = CliRunner().invoke(
        main,
        ["--json", "absences", "in-range",
         "--from", "2024-04-01", "--to", "2024-04-30"],
    )
    assert result.exit_code == 0
    assert [r["_id"] for r in json.loads(result.output)] == ["a1", "a2"]
