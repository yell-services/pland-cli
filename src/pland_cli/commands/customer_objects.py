"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("customer-objects")
def customer_objects_group():
    """customer-objects-Operationen."""
    pass

@customer_objects_group.command("list-by")
@click.argument("CUSTOMERID")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customer_objects_list_by(ctx, customerid, limit, offset, extra_params):
    """List objects by customer"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/customers/" + customerid + "/objects",
        query={"limit": limit, "offset": offset}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@customer_objects_group.command("list-by-location")
@click.argument("LAT")
@click.argument("LONG")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customer_objects_list_by_location(ctx, lat, long, extra_params):
    """List customer objects by location"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/objects/location/" + lat + "/" + long + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@customer_objects_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort as JSON: {\"by\":\"<field>\",\"direction\":1} (1 asc, -1 desc). The spec's \"field:1\" form returns 400.")
@click.option("--customerId", "customerId", default=None, help="")
@click.option("--objectManagers", "objectManagers", default=None, help="")
@click.option("--contactIds", "contactIds", default=None, help="")
@click.option("--nameAndAddress", "nameAndAddress", default=None, help="")
@click.option("--name", "name", default=None, help="")
@click.option("--tags", "tags", default=None, help="")
@click.option("--active", "active", default=None, type=bool, help="Filter by active status")
@click.option("--status", "status", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--customerIds", "customerIds", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customer_objects_list(ctx, limit, offset, sort, customerId, objectManagers, contactIds, nameAndAddress, name, tags, active, status, ids, customerIds, generalField, fetch_all, extra_params):
    """List customer objects"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/objects/",
        query={"limit": limit, "offset": offset, "sort": sort, "customerId": customerId, "objectManagers": objectManagers, "contactIds": contactIds, "nameAndAddress": nameAndAddress, "name": name, "tags": tags, "active": active, "status": status, "ids": ids, "customerIds": customerIds, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@customer_objects_group.command("create")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customer_objects_create(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Create customer object"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/objects/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@customer_objects_group.command("list-material")
@click.argument("OBJECTID")
@click.option("--allWhenEmpty", "allWhenEmpty", default=None, type=bool, help="Return all materials when closet is empty")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customer_objects_list_material(ctx, objectid, allWhenEmpty, extra_params):
    """List object material"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/objects/" + objectid + "/material",
        query={"allWhenEmpty": allWhenEmpty}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@customer_objects_group.command("add-material")
@click.argument("OBJECTID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customer_objects_add_material(ctx, objectid, data, dry_run, assume_yes, confirm_token, extra_params):
    """Add material to object"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/objects/" + objectid + "/material",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@customer_objects_group.command("list-active-users-on")
@click.argument("OBJECTID")
@click.option("--showAll", "showAll", default=None, type=bool, help="Show all users when no active users found")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customer_objects_list_active_users_on(ctx, objectid, showAll, extra_params):
    """List active users on object"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/objects/" + objectid + "/activeUsers",
        query={"showAll": showAll}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@customer_objects_group.command("remove-material", short_help="🟡 Remove material from object")
@click.argument("OBJECTID")
@click.argument("TYPE")
@click.argument("CLOSETID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customer_objects_remove_material(ctx, objectid, type, closetid, dry_run, assume_yes, confirm_token, extra_params):
    """Remove material from object"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/objects/" + objectid + "/material/" + type + "/" + closetid + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@customer_objects_group.command("change-material-budget", short_help="🟡 Change material budget")
@click.argument("OBJECTID")
@click.argument("ARTICLEID")
@click.argument("BUDGET")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customer_objects_change_material_budget(ctx, objectid, articleid, budget, dry_run, assume_yes, confirm_token, extra_params):
    """Change material budget"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/objects/" + objectid + "/material/" + articleid + "/" + budget + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@customer_objects_group.command("set-location")
@click.argument("OBJECTID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customer_objects_set_location(ctx, objectid, data, dry_run, assume_yes, confirm_token, extra_params):
    """Set object location"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/objects/" + objectid + "/location",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@customer_objects_group.command("get-assigned-managers")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customer_objects_get_assigned_managers(ctx, fetch_all, extra_params):
    """Get assigned object managers"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/objects/assignedObjectManagers",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@customer_objects_group.command("get-by-number")
@click.argument("OBJECTNUMBER")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customer_objects_get_by_number(ctx, objectnumber, extra_params):
    """Get customer object by number"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/objects/" + objectnumber + "/byNumber",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@customer_objects_group.command("set-end-date-for-and-assignments", short_help="🔴 Set end date for object and assignments")
@click.argument("OBJECTID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customer_objects_set_end_date_for_and_assignments(ctx, objectid, data, dry_run, assume_yes, confirm_token, extra_params):
    """Set end date for object and assignments"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/objects/" + objectid + "/setEndDateForObjectAndAllAssignmentsOnObject",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@customer_objects_group.command("get-available-tags")
@click.option("--name", "name", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customer_objects_get_available_tags(ctx, name, fetch_all, extra_params):
    """Get available object tags"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/objects/tags",
        query={"name": name}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@customer_objects_group.command("get-basic-assignments-of")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customer_objects_get_basic_assignments_of(ctx, id, extra_params):
    """Get object assignments for time tracking"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/objects/" + id + "/assignmentInfo",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@customer_objects_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customer_objects_get(ctx, id, extra_params):
    """Get customer object by ID"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/objects/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@customer_objects_group.command("delete", short_help="🟡 Delete customer object")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customer_objects_delete(ctx, id, dry_run, assume_yes, confirm_token, extra_params):
    """Delete customer object"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/objects/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@customer_objects_group.command("update", short_help="🟡 Update customer object")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customer_objects_update(ctx, id, data, dry_run, assume_yes, confirm_token, extra_params):
    """Update customer object"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/objects/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@customer_objects_group.command("count")
@click.option("--customerId", "customerId", default=None, help="")
@click.option("--objectManagers", "objectManagers", default=None, help="")
@click.option("--contactIds", "contactIds", default=None, help="")
@click.option("--nameAndAddress", "nameAndAddress", default=None, help="")
@click.option("--name", "name", default=None, help="")
@click.option("--tags", "tags", default=None, help="")
@click.option("--status", "status", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--customerIds", "customerIds", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customer_objects_count(ctx, customerId, objectManagers, contactIds, nameAndAddress, name, tags, status, ids, customerIds, generalField, fetch_all, extra_params):
    """Count customer objects"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/objects/count",
        query={"customerId": customerId, "objectManagers": objectManagers, "contactIds": contactIds, "nameAndAddress": nameAndAddress, "name": name, "tags": tags, "status": status, "ids": ids, "customerIds": customerIds, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@customer_objects_group.command("get-last-number")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customer_objects_get_last_number(ctx, fetch_all, extra_params):
    """Get last object number"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/objects/lastNumber",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@customer_objects_group.command("get-distinct-values")
@click.option("--fieldKey", "fieldKey", default=None, help="Field name to get distinct values for")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_customer_objects_get_distinct_values(ctx, fieldKey, fetch_all, extra_params):
    """Distinct values for a customer object field"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/objects/distinctValues",
        query={"fieldKey": fieldKey}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

def register(root):
    root.add_command(customer_objects_group)
