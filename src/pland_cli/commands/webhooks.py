"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("webhooks")
def webhooks_group():
    """webhooks-Operationen."""
    pass

@webhooks_group.command("delete", short_help="🟡 Delete customer object")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_webhooks_delete(ctx, id, dry_run, assume_yes, extra_params):
    """Delete customer object"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/integrations/webhooks/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@webhooks_group.command("update", short_help="🟡 Update Webhook")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_webhooks_update(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update Webhook"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/integrations/webhooks/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@webhooks_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort field and direction (e.g. number:1, status.createdAt:-1)")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_webhooks_list(ctx, limit, offset, sort, fetch_all, extra_params):
    """List Webhooks"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/integrations/webhooks/",
        query={"limit": limit, "offset": offset, "sort": sort}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@webhooks_group.command("create")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_webhooks_create(ctx, data, dry_run, assume_yes, extra_params):
    """Create a new webhook"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/integrations/webhooks/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

def register(root):
    root.add_command(webhooks_group)
