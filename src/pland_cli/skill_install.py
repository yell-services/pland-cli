from __future__ import annotations

import shutil
from importlib import resources
from pathlib import Path

import click

TITLE_MARKER = "# pland-cli — "


def _skills_dir() -> Path:
    return Path(str(resources.files("pland_cli").joinpath("skills")))


def _is_ours(path: Path) -> bool:
    """True for an AGENTS.md this installer wrote; anything else belongs to the project."""
    try:
        return path.read_text(encoding="utf-8", errors="replace").lstrip().startswith(TITLE_MARKER)
    except OSError:
        return False


@click.group("skill")
def skill_group() -> None:
    """Agent-Skill installieren."""


@skill_group.command("install")
@click.option("--agent", type=click.Choice(["claude", "codex"]), default="claude")
@click.option("--dest", default=None, help="Zielverzeichnis (Default: agent-typisch).")
def install(agent: str, dest: str | None) -> None:
    """Kopiert SKILL.md/AGENTS.md + references an den Agent-Ort."""
    src = _skills_dir()
    if agent == "claude":
        target = Path(dest) if dest else Path.cwd() / ".claude" / "skills"
        pland_dir = target / "pland"
        (pland_dir / "references").mkdir(parents=True, exist_ok=True)
        shutil.copy(src / "SKILL.md", pland_dir / "SKILL.md")
        for ref in (src / "references").glob("*.md"):
            shutil.copy(ref, pland_dir / "references" / ref.name)
        click.echo(f"Claude-Skill installiert → {pland_dir}")
    else:
        target = Path(dest) if dest else Path.cwd()
        agents_md = target / "AGENTS.md"
        if agents_md.exists() and not _is_ours(agents_md):
            # never clobber a project-owned AGENTS.md; replacing our own is an update
            raise click.ClickException(
                f"{agents_md} existiert und stammt nicht von diesem Installer — Inhalt von Hand "
                "zusammenführen oder mit --dest ein anderes Ziel wählen."
            )
        target.mkdir(parents=True, exist_ok=True)
        shutil.copy(src / "AGENTS.md", agents_md)
        refs = target / "references"
        refs.mkdir(exist_ok=True)
        for ref in (src / "references").glob("*.md"):
            shutil.copy(ref, refs / ref.name)
        click.echo(f"Codex-AGENTS.md installiert → {target / 'AGENTS.md'}")


def register_skill(root: click.Group) -> None:
    root.add_command(skill_group)
