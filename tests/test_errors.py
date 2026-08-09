"""Exit code 2 (usage/input errors) without a Python traceback.

Spec: input/usage errors produce a clean message and exit code 2, no traceback.
"""
from click.testing import CliRunner

from pland_cli.cli import main


def _no_traceback(result) -> bool:
    blob = result.output + (str(result.exception) if result.exception else "")
    return "Traceback (most recent call last)" not in blob


def test_bad_data_json_exits_2_without_traceback(monkeypatch):
    monkeypatch.setenv("PLAND_API_KEY", "k")  # auth must not fire first
    result = CliRunner().invoke(main, ["absences", "create", "--data", "{not json}"])
    assert result.exit_code == 2
    assert _no_traceback(result)
    assert "--data" in result.output


def test_bad_extra_params_json_exits_2_without_traceback(monkeypatch):
    monkeypatch.setenv("PLAND_API_KEY", "k")
    result = CliRunner().invoke(
        main, ["absences", "list", "--extra-params", "{nope}"]
    )
    assert result.exit_code == 2
    assert _no_traceback(result)
    assert "--extra-params" in result.output


def test_unknown_profile_exits_2_with_clear_message(monkeypatch, tmp_path):
    # Keep a real config file out of the way.
    monkeypatch.setattr(
        "pland_cli.core.config.CONFIG_PATH", tmp_path / "none.toml"
    )
    result = CliRunner().invoke(main, ["--profile", "bogus", "users", "list"])
    assert result.exit_code == 2
    assert _no_traceback(result)
    assert "bogus" in result.output


def test_unknown_profile_auth_status_json_exits_2(monkeypatch, tmp_path):
    monkeypatch.setattr(
        "pland_cli.core.config.CONFIG_PATH", tmp_path / "none.toml"
    )
    result = CliRunner().invoke(
        main, ["--json", "--profile", "bogus", "auth", "status"]
    )
    assert result.exit_code == 2
    assert _no_traceback(result)
    assert "bogus" in result.output
