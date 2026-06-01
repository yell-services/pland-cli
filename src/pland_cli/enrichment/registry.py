from __future__ import annotations

import importlib
import pkgutil

import click

_REGISTRY: dict[str, dict[str, click.Command]] = {}
OVERRIDES: list[tuple[str, str, bool]] = []


def enrich(group: str, command: str, *, new: bool = False):
    """Registriert einen Click-Command als Overlay für (group, command).

    new=False ersetzt den gleichnamigen generierten Command, new=True ergänzt einen.
    """
    def deco(cmd: click.Command) -> click.Command:
        cmd.name = command
        _REGISTRY.setdefault(group, {})[command] = cmd
        OVERRIDES.append((group, command, new))
        return cmd
    return deco


def load_enrichments() -> None:
    import pland_cli.enrichment as pkg

    for m in pkgutil.iter_modules(pkg.__path__):
        if m.name not in ("registry", "_filters"):
            importlib.import_module(f"pland_cli.enrichment.{m.name}")


_MARKER = "(enriched)"


def _mark_enriched(cmd: click.Command) -> None:
    """Markiert die Kurz-Hilfe sichtbar mit '(enriched)' (idempotent).

    Der Marker steht vorne, damit er auch bei schmalen Terminals (Click kürzt
    short_help auf die Spaltenbreite) nicht abgeschnitten wird.
    """
    if cmd.short_help:
        base = cmd.short_help
    elif cmd.help:
        base = cmd.help.strip().splitlines()[0]
    else:
        base = ""
    if base.startswith(_MARKER):
        return
    cmd.short_help = f"{_MARKER} {base}" if base else _MARKER


def apply_enrichment(group_name: str, group_cmd: click.Group) -> None:
    for name, cmd in _REGISTRY.get(group_name, {}).items():
        _mark_enriched(cmd)
        group_cmd.add_command(cmd, name)  # ersetzt gleichnamigen oder ergänzt


def validate_overrides(root: click.Group) -> None:
    """Bricht ab, wenn ein @enrich auf eine nicht-existente Gruppe zeigt (Tippfehler)."""
    existing = set(root.commands)
    bad = sorted({g for (g, _c, _n) in OVERRIDES if g not in existing})
    if bad:
        raise RuntimeError(f"Enrichment für unbekannte Gruppe(n): {bad}")


def get_client(ctx: click.Context):
    """Holt den lazy Client (Exit 3 ohne Key) — für Enrichment-Commands."""
    from pland_cli.cli import _attach_client

    _attach_client(ctx)
    return ctx.obj["client"]
