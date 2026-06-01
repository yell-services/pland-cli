"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("payment-terms")
def payment_terms_group():
    """payment-terms-Operationen."""
    pass

@payment_terms_group.command("list")
@click.option("--skip", "skip", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--sortKey", "sortKey", default=None, type=click.Choice(["paymentGoal", "description", "created", "updated"]), help="Field to sort by")
@click.option("--sortDirection", "sortDirection", default=None, type=click.Choice(["asc", "desc"]), help="Sort direction")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_payment_terms_list(ctx, skip, limit, sortKey, sortDirection, fetch_all, extra_params):
    """List payment terms"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/paymentTerms/",
        query={"skip": skip, "limit": limit, "sortKey": sortKey, "sortDirection": sortDirection}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@payment_terms_group.command("create")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_payment_terms_create(ctx, data, dry_run, assume_yes, extra_params):
    """Create payment term"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/paymentTerms/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@payment_terms_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_payment_terms_get(ctx, id, extra_params):
    """Get payment term"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/paymentTerms/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@payment_terms_group.command("delete")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_payment_terms_delete(ctx, id, dry_run, assume_yes, extra_params):
    """Delete payment term"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/paymentTerms/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@payment_terms_group.command("update")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_payment_terms_update(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update payment term"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/paymentTerms/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

def register(root):
    root.add_command(payment_terms_group)
