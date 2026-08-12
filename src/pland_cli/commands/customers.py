"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("customers")
def customers_group():
    """customers-Operationen."""
    pass

@customers_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort as JSON: {\"by\":\"<field>\",\"direction\":1} (1 asc, -1 desc). The spec's \"field:1\" form returns 400.")
@click.option("--number", "number", default=None, type=int, help="")
@click.option("--customerHasAssignedObjectManager", "customerHasAssignedObjectManager", default=None, help="")
@click.option("--objectIds", "objectIds", default=None, help="")
@click.option("--nameAndAddress", "nameAndAddress", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--status", "status", default=None, help="")
@click.option("--name", "name", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customers_list(ctx, limit, offset, sort, number, customerHasAssignedObjectManager, objectIds, nameAndAddress, generalField, status, name, ids, fetch_all, extra_params):
    """List customers"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/customers/",
        query={"limit": limit, "offset": offset, "sort": sort, "number": number, "customerHasAssignedObjectManager": customerHasAssignedObjectManager, "objectIds": objectIds, "nameAndAddress": nameAndAddress, "generalField": generalField, "status": status, "name": name, "ids": ids}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@customers_group.command("create")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customers_create(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Create customer"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/customers/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@customers_group.command("count")
@click.option("--number", "number", default=None, type=int, help="")
@click.option("--customerHasAssignedObjectManager", "customerHasAssignedObjectManager", default=None, help="")
@click.option("--objectIds", "objectIds", default=None, help="")
@click.option("--nameAndAddress", "nameAndAddress", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customers_count(ctx, number, customerHasAssignedObjectManager, objectIds, nameAndAddress, generalField, fetch_all, extra_params):
    """Count customers"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/customers/count",
        query={"number": number, "customerHasAssignedObjectManager": customerHasAssignedObjectManager, "objectIds": objectIds, "nameAndAddress": nameAndAddress, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@customers_group.command("get-last-number")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customers_get_last_number(ctx, fetch_all, extra_params):
    """Get last customer number"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/customers/lastNumber",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@customers_group.command("get-distinct-values")
@click.option("--fieldKey", "fieldKey", default=None, help="Field name to get distinct values for (e.g. contactPerson, vatNumber, address.city)")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customers_get_distinct_values(ctx, fieldKey, fetch_all, extra_params):
    """Get distinct values"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/customers/distinctValues",
        query={"fieldKey": fieldKey}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@customers_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customers_get(ctx, id, extra_params):
    """Get customer"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/customers/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@customers_group.command("delete", short_help="🟡 Delete customer")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customers_delete(ctx, id, dry_run, assume_yes, confirm_token, extra_params):
    """Delete customer"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/customers/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@customers_group.command("update", short_help="🟡 Update customer")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customers_update(ctx, id, data, dry_run, assume_yes, confirm_token, extra_params):
    """Update customer"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/customers/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@customers_group.command("update-many", short_help="🟡 Batch update customers")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customers_update_many(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Batch update customers"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/customers/many",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@customers_group.command("get-or-create-chat")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customers_get_or_create_chat(ctx, id, dry_run, assume_yes, confirm_token, extra_params):
    """Get/create customer chat"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/customers/" + id + "/chat",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@customers_group.command("get-documentation")
@click.argument("ID")
@click.option("--timeStart", "timeStart", default=None, type=int, help="Start timestamp for documentation period")
@click.option("--timeEnd", "timeEnd", default=None, type=int, help="End timestamp for documentation period")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customers_get_documentation(ctx, id, timeStart, timeEnd, extra_params):
    """Get customer documentation"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/customers/" + id + "/documentation",
        query={"timeStart": timeStart, "timeEnd": timeEnd}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@customers_group.command("set-end-date", short_help="🔴 Set customer end date")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customers_set_end_date(ctx, id, data, dry_run, assume_yes, confirm_token, extra_params):
    """Set customer end date"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/customers/" + id + "/setEndDateForCustomerAndAllObjectsOnCustomer",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

def register(root):
    root.add_command(customers_group)
