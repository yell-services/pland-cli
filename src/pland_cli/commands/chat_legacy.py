"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("chat-legacy")
def chat_legacy_group():
    """chat-legacy-Operationen."""
    pass

@chat_legacy_group.command("get-user-token")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_chat_legacy_get_user_token(ctx, fetch_all, extra_params):
    """Get chat user token"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/chat/token",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@chat_legacy_group.command("create-channel")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_chat_legacy_create_channel(ctx, data, dry_run, extra_params):
    """Create chat channel"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/chat/createChannel",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@chat_legacy_group.command("update-channel", short_help="🟡 Update chat channel")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_chat_legacy_update_channel(ctx, id, data, dry_run, assume_yes, confirm_token, extra_params):
    """Update chat channel"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/chat/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@chat_legacy_group.command("delete-channel", short_help="🟡 Delete chat channel")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_chat_legacy_delete_channel(ctx, id, dry_run, assume_yes, confirm_token, extra_params):
    """Delete chat channel"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/chat/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@chat_legacy_group.command("add-channel-members")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_chat_legacy_add_channel_members(ctx, id, data, dry_run, extra_params):
    """Add channel members"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/chat/" + id + "/members",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@chat_legacy_group.command("remove-channel-members")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_chat_legacy_remove_channel_members(ctx, id, data, dry_run, extra_params):
    """Remove channel members"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/chat/" + id + "/removeMembers",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@chat_legacy_group.command("send-invite-sms", short_help="🟡 Send chat invite SMS")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_chat_legacy_send_invite_sms(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Send chat invite SMS"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/chat/sendSMS",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

def register(root):
    root.add_command(chat_legacy_group)
