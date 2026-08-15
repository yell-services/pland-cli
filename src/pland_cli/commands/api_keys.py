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
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_api_keys_get_api_key(ctx, limit, offset, fetch_all, extra_params):
    """List API Keys"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/api_key/",
        query={"limit": limit, "offset": offset}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@api_keys_group.command("create-api-key")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_api_keys_create_api_key(ctx, data, dry_run, extra_params):
    """Create API Key"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/api_key/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@api_keys_group.command("delete-api-key", short_help="🔴 Expire API Key")
@click.argument("KEYID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_api_keys_delete_api_key(ctx, keyid, dry_run, assume_yes, confirm_token, extra_params):
    """Expire API Key"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/api_key/" + keyid + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@api_keys_group.command("update-api-key", short_help="🔴 Rotate API Key")
@click.argument("KEYID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_api_keys_update_api_key(ctx, keyid, dry_run, assume_yes, confirm_token, extra_params):
    """Rotate API Key"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/api_key/" + keyid + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

def register(root):
    root.add_command(api_keys_group)
