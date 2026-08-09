"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("surcharges")
def surcharges_group():
    """surcharges-Operationen."""
    pass

@surcharges_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort as JSON: {\"by\":\"<field>\",\"direction\":1} (1 asc, -1 desc). The spec's \"field:1\" form returns 400.")
@click.option("--name", "name", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--status", "status", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_surcharges_list(ctx, limit, offset, sort, name, ids, status, generalField, fetch_all, extra_params):
    """List surcharges"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/surcharges/",
        query={"limit": limit, "offset": offset, "sort": sort, "name": name, "ids": ids, "status": status, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@surcharges_group.command("create")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_surcharges_create(ctx, data, dry_run, assume_yes, extra_params):
    """Create surcharge"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/surcharges/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@surcharges_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_surcharges_get(ctx, id, extra_params):
    """Get surcharge by ID"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/surcharges/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@surcharges_group.command("delete")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_surcharges_delete(ctx, id, dry_run, assume_yes, extra_params):
    """Delete surcharge"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/surcharges/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@surcharges_group.command("update")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_surcharges_update(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update surcharge"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/surcharges/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@surcharges_group.command("update-many", short_help="🟡 Batch update surcharges")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_surcharges_update_many(ctx, data, dry_run, assume_yes, extra_params):
    """Batch update surcharges"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/surcharges/many",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

def register(root):
    root.add_command(surcharges_group)
