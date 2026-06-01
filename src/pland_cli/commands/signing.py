"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("signing")
def signing_group():
    """signing-Operationen."""
    pass

@signing_group.command("create")
@click.option("--file", "file_", type=click.Path(exists=True), help="Datei (multipart).")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_signing_create(ctx, file_, dry_run, assume_yes, extra_params):
    """Create a new signing"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/signing/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=file_, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@signing_group.command("list-for-assignment")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_signing_list_for_assignment(ctx, id, extra_params):
    """List signings for an assignment"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/assignments/" + id + "/signings",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@signing_group.command("list-for-job")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_signing_list_for_job(ctx, id, extra_params):
    """List signings for a job"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/jobs/" + id + "/signings",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

def register(root):
    root.add_command(signing_group)
