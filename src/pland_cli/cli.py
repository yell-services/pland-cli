from __future__ import annotations

import importlib
import pkgutil

import click
from click_repl import repl as _click_repl

import pland_cli.commands as commands_pkg
from pland_cli import __version__
from pland_cli.core.client import PlandAuthError, PlandClient
from pland_cli.core.config import resolve_config


def _start_repl(ctx: click.Context) -> None:
    click.echo("◆ pland REPL — 'help' for commands, 'quit' to exit")
    _click_repl(ctx)


@click.command("repl")
@click.pass_context
def repl_cmd(ctx: click.Context) -> None:
    """Interaktiven REPL starten."""
    _start_repl(ctx.parent or ctx)


def _attach_client(ctx: click.Context) -> None:
    """Lazily place the PlandClient in ctx.obj; exit code 3 when no key is set.

    Called by run_operation (and by commands when needed), NOT by cli.py itself,
    so that key-free commands (schema/describe/auth status/--help) run without
    an API key.
    """
    if ctx.obj.get("client"):
        return
    try:
        cfg = resolve_config(profile=ctx.obj.get("profile"))
    except ValueError as e:
        click.echo(str(e), err=True)
        ctx.exit(2)
    try:
        ctx.obj["client"] = PlandClient(cfg)
    except PlandAuthError as e:
        click.echo(str(e), err=True)
        ctx.exit(3)


@click.group(invoke_without_command=True)
@click.option("--json", "as_json", is_flag=True, help="Maschinenlesbare JSON-Ausgabe.")
@click.option("--profile", default=None, help="API-Profil: prod | beta | local.")
@click.version_option(__version__, "--version")
@click.pass_context
def main(ctx: click.Context, as_json: bool, profile: str | None) -> None:
    """pland — CLI for the pland.app API."""
    ctx.ensure_object(dict)
    ctx.obj["as_json"] = as_json
    ctx.obj["profile"] = profile
    if ctx.invoked_subcommand is None:
        _start_repl(ctx)


def _register_generated() -> None:
    for m in pkgutil.iter_modules(commands_pkg.__path__):
        mod = importlib.import_module(f"pland_cli.commands.{m.name}")
        mod.register(main)


def _apply_enrichments() -> None:
    from pland_cli.enrichment.registry import (
        apply_enrichment,
        load_enrichments,
        validate_overrides,
    )

    load_enrichments()
    for name, cmd in main.commands.items():
        if isinstance(cmd, click.Group):
            apply_enrichment(name, cmd)
    validate_overrides(main)


_register_generated()
_apply_enrichments()

from pland_cli.meta import register_meta  # noqa: E402

register_meta(main)

from pland_cli.auth import register_auth  # noqa: E402

register_auth(main)

from pland_cli.skill_install import register_skill  # noqa: E402

register_skill(main)

main.add_command(repl_cmd)


if __name__ == "__main__":
    main()
