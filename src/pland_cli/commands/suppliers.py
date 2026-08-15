"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("suppliers")
def suppliers_group():
    """suppliers-Operationen."""
    pass

@suppliers_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort as JSON: {\"by\":\"<field>\",\"direction\":1} (1 asc, -1 desc). The spec's \"field:1\" form returns 400.")
@click.option("--name", "name", default=None, help="")
@click.option("--status", "status", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_suppliers_list(ctx, limit, offset, sort, name, status, ids, generalField, fetch_all, extra_params):
    """List suppliers"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/suppliers/",
        query={"limit": limit, "offset": offset, "sort": sort, "name": name, "status": status, "ids": ids, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@suppliers_group.command("create")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_suppliers_create(ctx, data, dry_run, extra_params):
    """Create supplier"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/suppliers/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@suppliers_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_suppliers_get(ctx, id, extra_params):
    """Get supplier"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/suppliers/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@suppliers_group.command("delete", short_help="🟡 Delete supplier")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_suppliers_delete(ctx, id, dry_run, assume_yes, confirm_token, extra_params):
    """Delete supplier"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/suppliers/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@suppliers_group.command("update", short_help="🟡 Update supplier")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_suppliers_update(ctx, id, data, dry_run, assume_yes, confirm_token, extra_params):
    """Update supplier"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/suppliers/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@suppliers_group.command("get-last-number")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_suppliers_get_last_number(ctx, fetch_all, extra_params):
    """Get last supplier number"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/suppliers/lastNumber",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

def register(root):
    root.add_command(suppliers_group)
