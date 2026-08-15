"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("push-notifications")
def push_notifications_group():
    """push-notifications-Operationen."""
    pass

@push_notifications_group.command("list")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_push_notifications_list(ctx, fetch_all, extra_params):
    """List notifications"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/notification/v2/",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@push_notifications_group.command("mark-as-read")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_push_notifications_mark_as_read(ctx, data, dry_run, extra_params):
    """Mark notifications as read"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/notification/v2/read",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@push_notifications_group.command("mark-as-unread")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_push_notifications_mark_as_unread(ctx, data, dry_run, extra_params):
    """Mark notifications as unread"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/notification/v2/unread",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@push_notifications_group.command("delete", short_help="🔴 Delete notifications")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_push_notifications_delete(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Delete notifications"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/notification/v2/delete",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@push_notifications_group.command("mark-all-as-read")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_push_notifications_mark_all_as_read(ctx, dry_run, extra_params):
    """Mark all notifications as read"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/notification/v2/readAll",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@push_notifications_group.command("delete-all-read", short_help="🔴 Delete all read notifications")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_push_notifications_delete_all_read(ctx, dry_run, assume_yes, confirm_token, extra_params):
    """Delete all read notifications"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/notification/v2/deleteAllRead",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@push_notifications_group.command("delete-all", short_help="🔴 Delete all notifications")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_push_notifications_delete_all(ctx, dry_run, assume_yes, confirm_token, extra_params):
    """Delete all notifications"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/notification/v2/deleteAll",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

def register(root):
    root.add_command(push_notifications_group)
