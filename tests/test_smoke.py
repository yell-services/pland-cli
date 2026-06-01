from click.testing import CliRunner

from pland_cli.cli import main


def test_version():
    result = CliRunner().invoke(main, ["--version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.output


def test_help_lists_group():
    result = CliRunner().invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "pland" in result.output.lower()
