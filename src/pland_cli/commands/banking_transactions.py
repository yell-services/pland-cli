"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("banking-transactions")
def banking_transactions_group():
    """banking-transactions-Operationen."""
    pass

@banking_transactions_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort field and direction (e.g. bankBookingDate:-1, amount:1)")
@click.option("--bookingDateFrom", "bookingDateFrom", default=None, help="")
@click.option("--bookingDateTo", "bookingDateTo", default=None, help="")
@click.option("--transactionTypeOf", "transactionTypeOf", default=None, help="")
@click.option("--transactions", "transactions", default=None, help="")
@click.option("--senderId", "senderId", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_banking_transactions_list(ctx, limit, offset, sort, bookingDateFrom, bookingDateTo, transactionTypeOf, transactions, senderId, generalField, fetch_all, extra_params):
    """List banking transactions"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/transactions/",
        query={"limit": limit, "offset": offset, "sort": sort, "bookingDateFrom": bookingDateFrom, "bookingDateTo": bookingDateTo, "transactionTypeOf": transactionTypeOf, "transactions": transactions, "senderId": senderId, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@banking_transactions_group.command("create")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_banking_transactions_create(ctx, data, dry_run, assume_yes, extra_params):
    """Create banking transaction"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/transactions/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@banking_transactions_group.command("get-distinct-values")
@click.option("--field", "field", default=None, help="Field name to get distinct values for")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_banking_transactions_get_distinct_values(ctx, field, fetch_all, extra_params):
    """Get distinct values"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/transactions/distinctValues",
        query={"field": field}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@banking_transactions_group.command("delete", short_help="🟡 Delete banking transaction")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_banking_transactions_delete(ctx, id, dry_run, assume_yes, extra_params):
    """Delete banking transaction"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/transactions/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@banking_transactions_group.command("list-senders")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort field and direction (e.g. name:1, iban:1)")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_banking_transactions_list_senders(ctx, limit, offset, sort, fetch_all, extra_params):
    """List transaction senders"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/senders/",
        query={"limit": limit, "offset": offset, "sort": sort}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@banking_transactions_group.command("match-to-invoices", short_help="🟡 Match transaction to invoices")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_banking_transactions_match_to_invoices(ctx, id, data, dry_run, assume_yes, extra_params):
    """Match transaction to invoices"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/transactions/" + id + "/match",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@banking_transactions_group.command("unmatch", short_help="🟡 Unmatch transaction from invoices")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_banking_transactions_unmatch(ctx, id, dry_run, assume_yes, extra_params):
    """Unmatch transaction from invoices"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/transactions/" + id + "/unmatch",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@banking_transactions_group.command("delete-many", short_help="🔴 Delete multiple transactions")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_banking_transactions_delete_many(ctx, data, dry_run, assume_yes, extra_params):
    """Delete multiple transactions"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/transactions/delete",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
    )

@banking_transactions_group.command("get-matching-invoices")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_banking_transactions_get_matching_invoices(ctx, id, extra_params):
    """Get matching invoices for transaction"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/transactions/" + id + "/matchingInvoices",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@banking_transactions_group.command("ignore", short_help="🟡 Ignore/unignore transactions")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_banking_transactions_ignore(ctx, data, dry_run, assume_yes, extra_params):
    """Ignore/unignore transactions"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/transactions/ignore",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

def register(root):
    root.add_command(banking_transactions_group)
