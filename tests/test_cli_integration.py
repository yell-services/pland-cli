from click.testing import CliRunner

from pland_cli.cli import main


def test_groups_are_registered():
    result = CliRunner().invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "absences" in result.output
    assert "users" in result.output


def test_absences_list_help():
    result = CliRunner().invoke(main, ["absences", "list", "--help"])
    assert result.exit_code == 0
    assert "--limit" in result.output


def test_missing_key_gives_clear_error(monkeypatch, tmp_path):
    monkeypatch.delenv("PLAND_API_KEY", raising=False)
    monkeypatch.setattr("pland_cli.core.config.CONFIG_PATH", tmp_path / "none.toml")
    result = CliRunner().invoke(main, ["users", "list"])
    assert result.exit_code == 3
    assert "API key" in result.output
