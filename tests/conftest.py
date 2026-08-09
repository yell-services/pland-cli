import json
from pathlib import Path

import httpx
import pytest

from pland_cli.core.client import PlandClient
from pland_cli.core.config import Config

FIXTURE_DIR = Path(__file__).parent / "fixtures"


def load_fixture(name: str) -> object:
    return json.loads((FIXTURE_DIR / name).read_text())


@pytest.fixture
def mock_client():
    """Build a PlandClient whose responses are driven by a handler."""

    def _make(handler) -> PlandClient:
        cfg = Config(base_url="https://api.test/v2", api_key="k", profile="prod")
        return PlandClient(cfg, transport=httpx.MockTransport(handler))

    return _make


def pytest_addoption(parser):
    parser.addoption(
        "--run-live",
        action="store_true",
        default=False,
        help="Run live tests against prod (GET only).",
    )


def pytest_collection_modifyitems(config, items):
    if config.getoption("--run-live"):
        return
    skip_live = pytest.mark.skip(reason="Live-Test (nutze --run-live)")
    for item in items:
        if "live" in item.keywords:
            item.add_marker(skip_live)
