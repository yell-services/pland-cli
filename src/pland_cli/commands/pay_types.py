"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("pay-types")
def pay_types_group():
    """pay-types-Operationen."""
    pass

@pay_types_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_pay_types_get(ctx, id, extra_params):
    """Get pay type"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/payTypes/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@pay_types_group.command("delete", short_help="🟡 Delete pay type")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_pay_types_delete(ctx, id, dry_run, assume_yes, extra_params):
    """Delete pay type"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/payTypes/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@pay_types_group.command("update", short_help="🟡 Update pay type")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_pay_types_update(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update pay type"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/payTypes/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@pay_types_group.command("get-salaries")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort as JSON: {\"by\":\"<field>\",\"direction\":1} (1 asc, -1 desc). The spec's \"field:1\" form returns 400.")
@click.option("--status", "status", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--name", "name", default=None, help="")
@click.option("--requestable", "requestable", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_pay_types_get_salaries(ctx, limit, offset, sort, status, ids, name, requestable, fetch_all, extra_params):
    """List salary pay types"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/payTypes/salary",
        query={"limit": limit, "offset": offset, "sort": sort, "status": status, "ids": ids, "name": name, "requestable": requestable}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@pay_types_group.command("create-salary")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_pay_types_create_salary(ctx, data, dry_run, assume_yes, extra_params):
    """Create salary pay type"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/payTypes/salary",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@pay_types_group.command("get-absences")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort as JSON: {\"by\":\"<field>\",\"direction\":1} (1 asc, -1 desc). The spec's \"field:1\" form returns 400.")
@click.option("--status", "status", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--name", "name", default=None, help="")
@click.option("--requestable", "requestable", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_pay_types_get_absences(ctx, limit, offset, sort, status, ids, name, requestable, fetch_all, extra_params):
    """List absence pay types"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/payTypes/absence",
        query={"limit": limit, "offset": offset, "sort": sort, "status": status, "ids": ids, "name": name, "requestable": requestable}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@pay_types_group.command("create-absence")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_pay_types_create_absence(ctx, data, dry_run, assume_yes, extra_params):
    """Create absence pay type"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/payTypes/absence",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

def register(root):
    root.add_command(pay_types_group)
