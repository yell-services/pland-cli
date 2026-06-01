from click.testing import CliRunner

from pland_cli.cli import main


def test_schema_resolves_definition():
    result = CliRunner().invoke(main, ["--json", "schema", "Absence"])
    assert result.exit_code == 0
    assert "properties" in result.output or "Absence" in result.output


def test_describe_lists_params():
    result = CliRunner().invoke(main, ["--json", "describe", "absences", "list"])
    assert result.exit_code == 0
    assert "method" in result.output.lower()
