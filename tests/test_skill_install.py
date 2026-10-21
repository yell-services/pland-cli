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


def test_install_codex_keeps_a_project_agents_md(tmp_path):
    own = "# My project\n\nRules the project wrote.\n"
    (tmp_path / "AGENTS.md").write_text(own, encoding="utf-8")
    result = CliRunner().invoke(main, ["skill", "install", "--agent", "codex",
                                       "--dest", str(tmp_path)])
    assert result.exit_code != 0
    assert (tmp_path / "AGENTS.md").read_text(encoding="utf-8") == own


def test_install_codex_updates_its_own_agents_md(tmp_path):
    (tmp_path / "AGENTS.md").write_text("# pland-cli — old version\n", encoding="utf-8")
    result = CliRunner().invoke(main, ["skill", "install", "--agent", "codex",
                                       "--dest", str(tmp_path)])
    assert result.exit_code == 0
    assert "old version" not in (tmp_path / "AGENTS.md").read_text(encoding="utf-8")
