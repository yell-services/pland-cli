from click.testing import CliRunner

from pland_cli.cli import main


def test_repl_command_exists():
    result = CliRunner().invoke(main, ["repl", "--help"])
    assert result.exit_code == 0


def test_bare_invocation_starts_repl(monkeypatch):
    called = {}
    import pland_cli.cli as cli_mod
    monkeypatch.setattr(cli_mod, "_start_repl", lambda ctx: called.setdefault("yes", True))
    CliRunner().invoke(main, [])
    assert called.get("yes") is True
