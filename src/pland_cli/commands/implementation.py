"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("implementation")
def implementation_group():
    """implementation-Operationen."""
    pass

@implementation_group.command("get-progress")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of users to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of users to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort as JSON: {\"by\":\"<field>\",\"direction\":1} (1 asc, -1 desc). The spec's \"field:1\" form returns 400.")
@click.option("--userName", "userName", default=None, help="")
@click.option("--employment", "employment", default=None, help="")
@click.option("--department", "department", default=None, help="")
@click.option("--tags", "tags", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_implementation_get_progress(ctx, limit, offset, sort, userName, employment, department, tags, fetch_all, extra_params):
    """Get user implementation progress"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/implementation/",
        query={"limit": limit, "offset": offset, "sort": sort, "userName": userName, "employment": employment, "department": department, "tags": tags}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

def register(root):
    root.add_command(implementation_group)
