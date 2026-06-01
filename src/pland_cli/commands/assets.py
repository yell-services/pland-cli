"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("assets")
def assets_group():
    """assets-Operationen."""
    pass

@assets_group.command("redirect-to-secure")
@click.option("--url", "url", default=None, help="Original asset URL to be secured")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assets_redirect_to_secure(ctx, url, fetch_all, extra_params):
    """Get secure asset URL"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/assets/redirect",
        query={"url": url}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

def register(root):
    root.add_command(assets_group)
