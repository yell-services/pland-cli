"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("notifications")
def notifications_group():
    """notifications-Operationen."""
    pass

@notifications_group.command("get-all")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to offset for pagination")
@click.option("--sort", "sort", default=None, help="Sort as JSON: {\"by\":\"<field>\",\"direction\":1} (1 asc, -1 desc). The spec's \"field:1\" form returns 400.")
@click.option("--from", "from_", default=None, help="")
@click.option("--to", "to", default=None, help="")
@click.option("--wasRead", "wasRead", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_notifications_get_all(ctx, limit, offset, sort, from_, to, wasRead, fetch_all, extra_params):
    """Get all notifications"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/notifications/",
        query={"limit": limit, "offset": offset, "sort": sort, "from": from_, "to": to, "wasRead": wasRead}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@notifications_group.command("count-user")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_notifications_count_user(ctx, fetch_all, extra_params):
    """Count new notifications"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/notifications/countNewEntities",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@notifications_group.command("all-entities-count")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_notifications_all_entities_count(ctx, fetch_all, extra_params):
    """Count all entity types"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/notifications/allEntitiesCount",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@notifications_group.command("mark-as-checked")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_notifications_mark_as_checked(ctx, id, dry_run, assume_yes, confirm_token, extra_params):
    """Mark notification as checked"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/notifications/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@notifications_group.command("mark-as-read")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_notifications_mark_as_read(ctx, id, dry_run, assume_yes, confirm_token, extra_params):
    """Mark notification as read"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/notifications/" + id + "/read",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@notifications_group.command("mark-as-un-read")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_notifications_mark_as_un_read(ctx, id, dry_run, assume_yes, confirm_token, extra_params):
    """Mark notification as unread"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/notifications/" + id + "/unRead",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

def register(root):
    root.add_command(notifications_group)
