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


def test_in_range_filters_by_jobdate(monkeypatch):
    rows = [
        {"_id": "t1", "trackingJobDate": 1713175200000, "approved": False},  # 2024-04-15
        {"_id": "t2", "trackingJobDate": 1715767200000, "approved": False},  # 2024-05-15 (außerhalb)
    ]

    def handler(request: httpx.Request) -> httpx.Response:
        offset = int(request.url.params.get("offset", "0"))
        return httpx.Response(200, json=rows if offset == 0 else [])

    import pland_cli.enrichment.time_tracking as tt
    monkeypatch.setattr(tt, "get_client", lambda ctx: _mk(handler))

    result = CliRunner().invoke(
        main,
        ["--json", "time-tracking", "in-range",
         "--from", "2024-04-01", "--to", "2024-04-30"],
    )
    assert result.exit_code == 0
    assert [r["_id"] for r in json.loads(result.output)] == ["t1"]


def test_in_range_unapproved_flag_sets_param(monkeypatch):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["timeTrackingNotApproved"] = request.url.params.get("timeTrackingNotApproved")
        return httpx.Response(200, json=[])

    import pland_cli.enrichment.time_tracking as tt
    monkeypatch.setattr(tt, "get_client", lambda ctx: _mk(handler))

    result = CliRunner().invoke(
        main,
        ["--json", "time-tracking", "in-range",
         "--from", "2024-04-01", "--to", "2024-04-30", "--unapproved"],
    )
    assert result.exit_code == 0
    assert seen["timeTrackingNotApproved"] == "true"


def test_in_range_without_unapproved_omits_param(monkeypatch):
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["timeTrackingNotApproved"] = request.url.params.get("timeTrackingNotApproved")
        return httpx.Response(200, json=[])

    import pland_cli.enrichment.time_tracking as tt
    monkeypatch.setattr(tt, "get_client", lambda ctx: _mk(handler))

    result = CliRunner().invoke(
        main,
        ["--json", "time-tracking", "in-range",
         "--from", "2024-04-01", "--to", "2024-04-30"],
    )
    assert result.exit_code == 0
    assert seen["timeTrackingNotApproved"] is None
