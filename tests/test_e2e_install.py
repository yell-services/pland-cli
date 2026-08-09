import subprocess
import sys

import pytest

pytestmark = pytest.mark.live


def test_module_help_runs():
    """Verify the CLI runs as a module (smoke test, no key required)."""
    out = subprocess.run([sys.executable, "-m", "pland_cli.cli", "--help"],
                         capture_output=True, text=True)
    assert out.returncode == 0
    assert "pland" in out.stdout.lower()
