from __future__ import annotations

import shutil
from importlib import resources
from pathlib import Path

import click


def _skills_dir() -> Path:
    return Path(str(resources.files("pland_cli").joinpath("skills")))


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
        target.mkdir(parents=True, exist_ok=True)
        shutil.copy(src / "AGENTS.md", target / "AGENTS.md")
        refs = target / "references"
        refs.mkdir(exist_ok=True)
        for ref in (src / "references").glob("*.md"):
            shutil.copy(ref, refs / ref.name)
        click.echo(f"Codex-AGENTS.md installiert → {target / 'AGENTS.md'}")


def register_skill(root: click.Group) -> None:
    root.add_command(skill_group)
