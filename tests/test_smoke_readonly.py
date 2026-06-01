import os

import pytest
from click.testing import CliRunner

from pland_cli.cli import main

pytestmark = pytest.mark.live


@pytest.fixture(autouse=True)
def _require_key():
    if not os.environ.get("PLAND_API_KEY"):
        pytest.skip("PLAND_API_KEY nicht gesetzt — Live-Test übersprungen")


def test_users_list_live():
    result = CliRunner().invoke(main, ["--json", "users", "list", "--limit", "1"])
    assert result.exit_code == 0
    assert result.output.strip().startswith("[") or result.output.strip().startswith("{")
