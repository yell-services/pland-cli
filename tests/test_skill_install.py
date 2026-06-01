from click.testing import CliRunner

from pland_cli.cli import main


def test_install_claude_copies_skill(tmp_path):
    result = CliRunner().invoke(main, ["skill", "install", "--agent", "claude",
                                       "--dest", str(tmp_path)])
    assert result.exit_code == 0
    assert (tmp_path / "pland" / "SKILL.md").exists()
    assert (tmp_path / "pland" / "references" / "commands.md").exists()


def test_install_codex_writes_agents_md(tmp_path):
    result = CliRunner().invoke(main, ["skill", "install", "--agent", "codex",
                                       "--dest", str(tmp_path)])
    assert result.exit_code == 0
    assert (tmp_path / "AGENTS.md").exists()
