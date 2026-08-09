"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("task-types")
def task_types_group():
    """task-types-Operationen."""
    pass

@task_types_group.command("list")
@click.option("--page", "page", default=None, type=int, help="Page number")
@click.option("--limit", "limit", default=None, type=int, help="Number of items per page")
@click.option("--status", "status", default=None, help="")
@click.option("--name", "name", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_task_types_list(ctx, page, limit, status, name, ids, fetch_all, extra_params):
    """List task types"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/taskTypes/",
        query={"page": page, "limit": limit, "status": status, "name": name, "ids": ids}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@task_types_group.command("create")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_task_types_create(ctx, data, dry_run, assume_yes, extra_params):
    """Create a new task type"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/taskTypes/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@task_types_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_task_types_get(ctx, id, extra_params):
    """Get task type"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/taskTypes/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@task_types_group.command("delete")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_task_types_delete(ctx, id, dry_run, assume_yes, extra_params):
    """Deletes a task type"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/taskTypes/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@task_types_group.command("update")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_task_types_update(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update task type"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/taskTypes/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

def register(root):
    root.add_command(task_types_group)
