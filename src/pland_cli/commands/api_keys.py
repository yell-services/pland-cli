"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("api-keys")
def api_keys_group():
    """api-keys-Operationen."""
    pass

@api_keys_group.command("get-api-key")
@click.option("--limit", "limit", default=None, type=int, help="Number of results to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of results to skip")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_api_keys_get_api_key(ctx, limit, offset, fetch_all, extra_params):
    """List API Keys"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/api_key/",
        query={"limit": limit, "offset": offset}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@api_keys_group.command("create-api-key")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_api_keys_create_api_key(ctx, data, dry_run, assume_yes, extra_params):
    """Create API Key"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/api_key/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@api_keys_group.command("delete-api-key", short_help="🔴 Expire API Key")
@click.argument("KEYID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_api_keys_delete_api_key(ctx, keyId, dry_run, assume_yes, extra_params):
    """Expire API Key"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/api_key/" + keyId + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
    )

@api_keys_group.command("update-api-key", short_help="🔴 Rotate API Key")
@click.argument("KEYID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_api_keys_update_api_key(ctx, keyId, dry_run, assume_yes, extra_params):
    """Rotate API Key"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/api_key/" + keyId + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
    )

def register(root):
    root.add_command(api_keys_group)
