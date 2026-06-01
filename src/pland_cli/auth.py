from __future__ import annotations

import click

from pland_cli.core import config as config_mod
from pland_cli.core.client import PlandError, bootstrap_api_key
from pland_cli.core.config import DEFAULT_PROFILE, resolve_config, save_api_key
from pland_cli.utils import output as out_mod


@click.group("auth")
def auth_group() -> None:
    """API-Key verwalten."""


@auth_group.command("set-key")
@click.option("--profile", default="prod")
@click.password_option("--key", prompt="API-Key", confirmation_prompt=False)
def set_key(profile: str, key: str) -> None:
    """Speichert den API-Key in ~/.config/pland/config.toml (chmod 600)."""
    path = save_api_key(key, profile=profile, path=config_mod.CONFIG_PATH)
    click.echo(f"Key für Profil '{profile}' gespeichert → {path}")


@auth_group.command("bootstrap")
@click.option("--profile", default=None, help="Ziel-Profil (Default: aktuelles bzw. prod).")
@click.option(
    "--login-id", "login_id", prompt="pland Login-ID (Nummer)",
    help="Login-ID/Nummer (wird NICHT gespeichert).",
)
@click.password_option(
    "--password", prompt="pland Passwort", confirmation_prompt=False,
    help="Login-Passwort (wird NICHT gespeichert).",
)
@click.option("--name", default="pland-cli", help="Name des neuen API-Keys.")
@click.pass_context
def bootstrap(ctx: click.Context, profile: str | None, login_id: str, password: str, name: str) -> None:
    """Erzeugt per Login einen neuen API-Key und speichert nur diesen.

    Login-ID (Nummer) und Passwort werden ausschließlich für den einmaligen
    Login verwendet und NIRGENDS gespeichert — nur der erzeugte API-Key landet
    in der Config. Tipp: Lass den Menschen die Eingabe machen (interaktiver
    Prompt), statt die Zugangsdaten als Flags über die Shell-History zu reichen.
    """
    out_mod.set_json(ctx.obj.get("as_json", False))
    profile = profile or ctx.obj.get("profile") or DEFAULT_PROFILE
    try:
        cfg = resolve_config(profile=profile)
    except ValueError as e:
        click.echo(str(e), err=True)
        ctx.exit(2)
    try:
        key = bootstrap_api_key(cfg.base_url, login_id, password, name=name)
    except PlandError as e:
        click.echo(f"Bootstrap fehlgeschlagen: {e}", err=True)
        ctx.exit(1)
    path = save_api_key(key, profile=profile, path=config_mod.CONFIG_PATH)
    # Den Key selbst NIE ausgeben — nur bestätigen.
    out_mod.out({"profile": profile, "saved_to": str(path), "key_created": True})


@auth_group.command("status")
@click.pass_context
def status(ctx: click.Context) -> None:
    """Zeigt Profil, Base-URL und ob ein Key vorliegt (ohne ihn auszugeben)."""
    out_mod.set_json(ctx.obj.get("as_json", False))
    try:
        cfg = resolve_config(profile=ctx.obj.get("profile"))
    except ValueError as e:
        click.echo(str(e), err=True)
        ctx.exit(2)
    out_mod.out({
        "profile": cfg.profile,
        "base_url": cfg.base_url,
        "has_key": bool(cfg.api_key),
    })


def register_auth(root: click.Group) -> None:
    root.add_command(auth_group)
