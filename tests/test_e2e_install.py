import subprocess
import sys

import pytest

pytestmark = pytest.mark.live


def test_module_help_runs():
    """Verifiziert, dass die CLI als Modul lauffähig ist (Smoke, kein Key nötig)."""
    out = subprocess.run([sys.executable, "-m", "pland_cli.cli", "--help"],
                         capture_output=True, text=True)
    assert out.returncode == 0
    assert "pland" in out.stdout.lower()
