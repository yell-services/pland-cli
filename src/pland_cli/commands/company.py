"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("company")
def company_group():
    """company-Operationen."""
    pass

@company_group.command("get-info")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_company_get_info(ctx, fetch_all, extra_params):
    """Get company information"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/company",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@company_group.command("set-info", short_help="🟡 Set company info")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_company_set_info(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Set company info"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/company/info",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@company_group.command("set-custom-email-settings", short_help="🟡 Set custom email settings")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_company_set_custom_email_settings(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Set custom email settings"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/company/emailSettings",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@company_group.command("disable-custom-email-settings", short_help="🟡 Disable custom email settings")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_company_disable_custom_email_settings(ctx, dry_run, assume_yes, confirm_token, extra_params):
    """Disable custom email settings"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/company/disableCustomEmailSettings",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@company_group.command("consent-to-bank-integration")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_company_consent_to_bank_integration(ctx, dry_run, extra_params):
    """Consent to bank integration"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/company/consentToBankIntegration",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@company_group.command("set-logo")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_company_set_logo(ctx, data, dry_run, extra_params):
    """Set company logo"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/company/companyLogo",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

def register(root):
    root.add_command(company_group)
