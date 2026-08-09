"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("logbuch")
def logbuch_group():
    """logbuch-Operationen."""
    pass

@logbuch_group.command("view-chat")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_logbuch_view_chat(ctx, id, extra_params):
    """View chat details"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/chat/v2/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@logbuch_group.command("subscribe-users-to-chat")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_logbuch_subscribe_users_to_chat(ctx, id, data, dry_run, assume_yes, extra_params):
    """Subscribe users to a chat"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/chat/v2/" + id + "/subscribe",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@logbuch_group.command("unsubscribe-users-from-chat")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_logbuch_unsubscribe_users_from_chat(ctx, id, data, dry_run, assume_yes, extra_params):
    """Unsubscribe users from a chat"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/chat/v2/" + id + "/unsubscribe",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@logbuch_group.command("get-users-with-access-to-chat")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_logbuch_get_users_with_access_to_chat(ctx, id, extra_params):
    """Get users with access to a chat"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/chat/v2/" + id + "/users",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@logbuch_group.command("send-chat-message")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_logbuch_send_chat_message(ctx, id, data, dry_run, assume_yes, extra_params):
    """Send a chat message"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/chat/v2/" + id + "/send",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@logbuch_group.command("send-note-message")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_logbuch_send_note_message(ctx, id, data, dry_run, assume_yes, extra_params):
    """Send a note message"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/chat/v2/" + id + "/sendNote",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@logbuch_group.command("send-thread-message")
@click.argument("ID")
@click.option("--parentMessageId", "parentMessageId", default=None, help="Parent message ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_logbuch_send_thread_message(ctx, id, parentMessageId, data, dry_run, assume_yes, extra_params):
    """Send a thread message"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/chat/v2/" + id + "/sendThread",
        query={"parentMessageId": parentMessageId}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@logbuch_group.command("list-for-chat")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_logbuch_list_for_chat(ctx, id, extra_params):
    """List messages for chat"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/chat/v2/" + id + "/messages",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@logbuch_group.command("mark-messages-as-read")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_logbuch_mark_messages_as_read(ctx, id, dry_run, assume_yes, extra_params):
    """Mark messages as read"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/chat/v2/" + id + "/markMessagesAsRead",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@logbuch_group.command("delete-message")
@click.argument("ID")
@click.argument("MESSAGEID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_logbuch_delete_message(ctx, id, messageId, dry_run, assume_yes, extra_params):
    """Delete a message"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/chat/v2/" + id + "/messages/" + messageId + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@logbuch_group.command("patch-message")
@click.argument("ID")
@click.argument("MESSAGEID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_logbuch_patch_message(ctx, id, messageId, data, dry_run, assume_yes, extra_params):
    """Update a message"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/chat/v2/" + id + "/messages/" + messageId + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@logbuch_group.command("pin-message")
@click.argument("ID")
@click.argument("MESSAGEID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_logbuch_pin_message(ctx, id, messageId, data, dry_run, assume_yes, extra_params):
    """Pin or unpin a message"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/chat/v2/" + id + "/messages/" + messageId + "/pin",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

def register(root):
    root.add_command(logbuch_group)
