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


def test_monthly_report_aggregates_hours(monkeypatch):
    rows = [
        {"_id": "s1", "from": 1713175200000, "workingTime": 28800},  # 2024-04-15, 8h
        {"_id": "s2", "from": 1713607200000, "workingTime": 14400},  # 2024-04-20, 4h
        {"_id": "s3", "from": 1715767200000, "workingTime": 36000},  # 2024-05-15 (out of range)
    ]

    def handler(request: httpx.Request) -> httpx.Response:
        offset = int(request.url.params.get("offset", "0"))
        return httpx.Response(200, json=rows if offset == 0 else [])

    import pland_cli.enrichment.salaries as sal
    monkeypatch.setattr(sal, "get_client", lambda ctx: _mk(handler))

    result = CliRunner().invoke(
        main,
        ["--json", "salary", "monthly-report",
         "--object-id", "o1", "--year", "2024", "--month", "4"],
    )
    assert result.exit_code == 0
    report = json.loads(result.output)
    assert report["total_hours"] == 12.0
    assert report["entries"] == 2
    assert report["object_id"] == "o1"
    assert report["year"] == 2024
    assert report["month"] == 4
