from click.testing import CliRunner

from pland_cli.cli import main


def test_version():
    """--version reports the packaged version.

    Compared against the installed metadata rather than a literal, so a
    release only has to touch __init__.py — hatch derives the package version
    from there, and a hardcoded literal here would be a third place to drift.
    """
    from importlib.metadata import version

    from pland_cli import __version__

    result = CliRunner().invoke(main, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.output
    assert version("pland-cli") == __version__


def test_help_lists_group():
    result = CliRunner().invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "pland" in result.output.lower()
