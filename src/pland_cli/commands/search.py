"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("search")
def search_group():
    """search-Operationen."""
    pass

@search_group.command("perform-global")
@click.option("--searchTerm", "searchTerm", default=None, help="The term to search for")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_search_perform_global(ctx, searchTerm, fetch_all, extra_params):
    """Perform Global Search"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/search/",
        query={"searchTerm": searchTerm}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

def register(root):
    root.add_command(search_group)
