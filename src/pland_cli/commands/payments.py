"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("payments")
def payments_group():
    """payments-Operationen."""
    pass

@payments_group.command("get-by-id")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_payments_get_by_id(ctx, id, extra_params):
    """Get payment details"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/payments/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@payments_group.command("delete", short_help="🟡 Delete payment")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_payments_delete(ctx, id, dry_run, assume_yes, extra_params):
    """Delete payment"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/payments/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@payments_group.command("update", short_help="🟡 Update payment")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_payments_update(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update payment"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/payments/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@payments_group.command("get")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort field and direction (e.g. paymentDate:1, amount:-1)")
@click.option("--invoiceIds", "invoiceIds", default=None, help="Filter by invoice IDs (comma-separated)")
@click.option("--paymentDateFrom", "paymentDateFrom", default=None, help="Filter payments from this date (YYYY-MM-DD)")
@click.option("--paymentDateTo", "paymentDateTo", default=None, help="Filter payments to this date (YYYY-MM-DD)")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_payments_get(ctx, limit, offset, sort, invoiceIds, paymentDateFrom, paymentDateTo, fetch_all, extra_params):
    """List payments"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/payments/",
        query={"limit": limit, "offset": offset, "sort": sort, "invoiceIds": invoiceIds, "paymentDateFrom": paymentDateFrom, "paymentDateTo": paymentDateTo}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@payments_group.command("create-invoice", short_help="🟡 Create payment for invoice")
@click.argument("INVOICEID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_payments_create_invoice(ctx, invoiceId, data, dry_run, assume_yes, extra_params):
    """Create payment for invoice"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/payments/invoice/" + invoiceId + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

def register(root):
    root.add_command(payments_group)
