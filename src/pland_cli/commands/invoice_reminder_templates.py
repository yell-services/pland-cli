"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("invoice-reminder-templates")
def invoice_reminder_templates_group():
    """invoice-reminder-templates-Operationen."""
    pass

@invoice_reminder_templates_group.command("create", short_help="🟡 Create invoice reminder template")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_invoice_reminder_templates_create(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Create invoice reminder template"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoiceReminders/templates",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@invoice_reminder_templates_group.command("get-distinct-values")
@click.option("--fieldKey", "fieldKey", default=None, help="Field name to get distinct values for")
@click.option("--status", "status", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_invoice_reminder_templates_get_distinct_values(ctx, fieldKey, status, fetch_all, extra_params):
    """Get distinct field values"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/invoiceReminders/templates/distinctValues",
        query={"fieldKey": fieldKey, "status": status}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@invoice_reminder_templates_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_invoice_reminder_templates_get(ctx, id, extra_params):
    """Get invoice reminder template"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/invoiceReminders/templates/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@invoice_reminder_templates_group.command("delete")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_invoice_reminder_templates_delete(ctx, id, dry_run, extra_params):
    """Delete invoice reminder template"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/invoiceReminders/templates/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@invoice_reminder_templates_group.command("update")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_invoice_reminder_templates_update(ctx, id, data, dry_run, extra_params):
    """Update invoice reminder template"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/invoiceReminders/templates/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

def register(root):
    root.add_command(invoice_reminder_templates_group)
