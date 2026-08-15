"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("quality-control")
def quality_control_group():
    """quality-control-Operationen."""
    pass

@quality_control_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort as JSON: {\"by\":\"<field>\",\"direction\":1} (1 asc, -1 desc). The spec's \"field:1\" form returns 400.")
@click.option("--status", "status", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--name", "name", default=None, help="")
@click.option("--objectId", "objectId", default=None, help="")
@click.option("--userId", "userId", default=None, help="")
@click.option("--objectManagers", "objectManagers", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_quality_control_list(ctx, limit, offset, sort, status, ids, name, objectId, userId, objectManagers, fetch_all, extra_params):
    """List quality control entries"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/qualityControl/",
        query={"limit": limit, "offset": offset, "sort": sort, "status": status, "ids": ids, "name": name, "objectId": objectId, "userId": userId, "objectManagers": objectManagers}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@quality_control_group.command("create")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_quality_control_create(ctx, data, dry_run, extra_params):
    """Create quality control entry"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/qualityControl/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@quality_control_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_quality_control_get(ctx, id, extra_params):
    """Get quality control entry"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/qualityControl/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

def register(root):
    root.add_command(quality_control_group)
