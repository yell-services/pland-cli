"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("sms")
def sms_group():
    """sms-Operationen."""
    pass

@sms_group.command("callback")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_sms_callback(ctx, data, dry_run, extra_params):
    """SMS status callback"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/sms/callback",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@sms_group.command("track-clicked-link")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_sms_track_clicked_link(ctx, data, dry_run, extra_params):
    """Track clicked SMS link"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/sms/clickedLink",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

def register(root):
    root.add_command(sms_group)
