"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("custom-fields")
def custom_fields_group():
    """custom-fields-Operationen."""
    pass

@custom_fields_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_custom_fields_list(ctx, limit, offset, fetch_all, extra_params):
    """List custom field definitions"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/customFields/",
        query={"limit": limit, "offset": offset}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@custom_fields_group.command("count")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_custom_fields_count(ctx, fetch_all, extra_params):
    """Count custom field definitions"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/customFields/count",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@custom_fields_group.command("get-distinct-values")
@click.option("--fieldKey", "fieldKey", default=None, help="Field name to get distinct values for")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_custom_fields_get_distinct_values(ctx, fieldKey, fetch_all, extra_params):
    """Distinct values for a custom field"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/customFields/distinctValues",
        query={"fieldKey": fieldKey}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

def register(root):
    root.add_command(custom_fields_group)
