"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("tasks")
def tasks_group():
    """tasks-Operationen."""
    pass

@tasks_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort as JSON: {\"by\":\"<field>\",\"direction\":1} (1 asc, -1 desc). The spec's \"field:1\" form returns 400.")
@click.option("--customer", "customer", default=None, help="")
@click.option("--userIds", "userIds", default=None, help="")
@click.option("--taskByTitleIdentifier", "taskByTitleIdentifier", default=None, help="")
@click.option("--taskAssignee", "taskAssignee", default=None, help="")
@click.option("--relatedContacts", "relatedContacts", default=None, help="")
@click.option("--relatedUsers", "relatedUsers", default=None, help="")
@click.option("--relatedObjects", "relatedObjects", default=None, help="")
@click.option("--relatedCustomers", "relatedCustomers", default=None, help="")
@click.option("--relatedAssignments", "relatedAssignments", default=None, help="")
@click.option("--relatedInvoices", "relatedInvoices", default=None, help="")
@click.option("--relatedEquipments", "relatedEquipments", default=None, help="")
@click.option("--taskStatus", "taskStatus", default=None, help="")
@click.option("--priority", "priority", default=None, help="")
@click.option("--callId", "callId", default=None, help="")
@click.option("--taskTabs", "taskTabs", default=None, help="")
@click.option("--taskType", "taskType", default=None, help="")
@click.option("--taskFromRecurringTemplate", "taskFromRecurringTemplate", default=None, help="")
@click.option("--status", "status", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_tasks_list(ctx, limit, offset, sort, customer, userIds, taskByTitleIdentifier, taskAssignee, relatedContacts, relatedUsers, relatedObjects, relatedCustomers, relatedAssignments, relatedInvoices, relatedEquipments, taskStatus, priority, callId, taskTabs, taskType, taskFromRecurringTemplate, status, fetch_all, extra_params):
    """List tasks"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/tasks/",
        query={"limit": limit, "offset": offset, "sort": sort, "customer": customer, "userIds": userIds, "taskByTitleIdentifier": taskByTitleIdentifier, "taskAssignee": taskAssignee, "relatedContacts": relatedContacts, "relatedUsers": relatedUsers, "relatedObjects": relatedObjects, "relatedCustomers": relatedCustomers, "relatedAssignments": relatedAssignments, "relatedInvoices": relatedInvoices, "relatedEquipments": relatedEquipments, "taskStatus": taskStatus, "priority": priority, "callId": callId, "taskTabs": taskTabs, "taskType": taskType, "taskFromRecurringTemplate": taskFromRecurringTemplate, "status": status}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@tasks_group.command("create")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_tasks_create(ctx, data, dry_run, extra_params):
    """Create task"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/tasks/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@tasks_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_tasks_get(ctx, id, extra_params):
    """Get task"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/tasks/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@tasks_group.command("update", short_help="🟡 Update task")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_tasks_update(ctx, id, data, dry_run, assume_yes, confirm_token, extra_params):
    """Update task"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/tasks/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@tasks_group.command("delete-multiple", short_help="🔴 Delete multiple tasks")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_tasks_delete_multiple(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Delete multiple tasks"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/tasks/delete",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@tasks_group.command("resolve", short_help="🟡 Resolve task")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_tasks_resolve(ctx, id, dry_run, assume_yes, confirm_token, extra_params):
    """Resolve task"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/tasks/" + id + "/resolve",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@tasks_group.command("complete", short_help="🟡 Complete task")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_tasks_complete(ctx, id, data, dry_run, assume_yes, confirm_token, extra_params):
    """Complete task"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/tasks/" + id + "/complete",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@tasks_group.command("count-new")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_tasks_count_new(ctx, fetch_all, extra_params):
    """Count new tasks"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/tasks/countNewEntities",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

def register(root):
    root.add_command(tasks_group)
