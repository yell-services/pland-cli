"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("contacts")
def contacts_group():
    """contacts-Operationen."""
    pass

@contacts_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to offset for pagination")
@click.option("--sort", "sort", default=None, help="Sort as JSON: {\"by\":\"<field>\",\"direction\":1} (1 asc, -1 desc). The spec's \"field:1\" form returns 400.")
@click.option("--objectIds", "objectIds", default=None, help="")
@click.option("--customerId", "customerId", default=None, help="")
@click.option("--name", "name", default=None, help="")
@click.option("--showInApp", "showInApp", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_contacts_list(ctx, limit, offset, sort, objectIds, customerId, name, showInApp, generalField, fetch_all, extra_params):
    """List contacts"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/contacts/",
        query={"limit": limit, "offset": offset, "sort": sort, "objectIds": objectIds, "customerId": customerId, "name": name, "showInApp": showInApp, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@contacts_group.command("create")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_contacts_create(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Create contact"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/contacts/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@contacts_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_contacts_get(ctx, id, extra_params):
    """Get contact"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/contacts/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@contacts_group.command("delete", short_help="🟡 Delete contact")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_contacts_delete(ctx, id, dry_run, assume_yes, confirm_token, extra_params):
    """Delete contact"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/contacts/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@contacts_group.command("update", short_help="🟡 Update contact")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_contacts_update(ctx, id, data, dry_run, assume_yes, confirm_token, extra_params):
    """Update contact"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/contacts/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@contacts_group.command("get-distinct-values")
@click.option("--fieldKey", "fieldKey", default=None, help="Field name to get distinct values for (e.g. position, salutation, email)")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_contacts_get_distinct_values(ctx, fieldKey, fetch_all, extra_params):
    """Get distinct values"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/contacts/distinctValues",
        query={"fieldKey": fieldKey}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@contacts_group.command("update-many", short_help="🟡 Batch update contacts")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_contacts_update_many(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Batch update contacts"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/contacts/many",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@contacts_group.command("list-for-object")
@click.argument("OBJECTID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_contacts_list_for_object(ctx, objectid, extra_params):
    """List contacts for object"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/objects/" + objectid + "/contacts",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@contacts_group.command("list-job")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_contacts_list_job(ctx, id, extra_params):
    """List job contacts"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/jobs/" + id + "/contacts",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

def register(root):
    root.add_command(contacts_group)
