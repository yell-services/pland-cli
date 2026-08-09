"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("pay-type-templates")
def pay_type_templates_group():
    """pay-type-templates-Operationen."""
    pass

@pay_type_templates_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_pay_type_templates_list(ctx, limit, offset, fetch_all, extra_params):
    """List pay type templates"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/payTypeTemplates/",
        query={"limit": limit, "offset": offset}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

def register(root):
    root.add_command(pay_type_templates_group)
