"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("invoice-reminders")
def invoice_reminders_group():
    """invoice-reminders-Operationen."""
    pass

@invoice_reminders_group.command("create")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_reminders_create(ctx, data, dry_run, assume_yes, extra_params):
    """Create invoice reminder"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoiceReminders/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@invoice_reminders_group.command("get-distinct-values")
@click.option("--fieldKey", "fieldKey", default=None, help="Field name to get distinct values for")
@click.option("--status", "status", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_reminders_get_distinct_values(ctx, fieldKey, status, fetch_all, extra_params):
    """Get distinct field values for invoice reminders"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/invoiceReminders/distinctValues",
        query={"fieldKey": fieldKey, "status": status}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@invoice_reminders_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_reminders_get(ctx, id, extra_params):
    """Get invoice reminder"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/invoiceReminders/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@invoice_reminders_group.command("delete", short_help="🟡 Delete invoice reminder")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_reminders_delete(ctx, id, dry_run, assume_yes, extra_params):
    """Delete invoice reminder"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/invoiceReminders/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@invoice_reminders_group.command("update", short_help="🟡 Update invoice reminder")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_reminders_update(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update invoice reminder"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/invoiceReminders/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@invoice_reminders_group.command("generate-combined-pdf")
@click.option("--output", type=click.Path(), help="Antwort in Datei schreiben.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_reminders_generate_combined_pdf(ctx, output, dry_run, assume_yes, extra_params):
    """Generate combined PDF for reminders"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoiceReminders/pdf",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=output, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@invoice_reminders_group.command("create-preview")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_reminders_create_preview(ctx, dry_run, assume_yes, extra_params):
    """Create reminder preview"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoiceReminders/preview",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@invoice_reminders_group.command("send", short_help="🟡 Send reminders via email")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_reminders_send(ctx, dry_run, assume_yes, extra_params):
    """Send reminders via email"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoiceReminders/send",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@invoice_reminders_group.command("generate-pdf")
@click.argument("ID")
@click.option("--output", type=click.Path(), help="Antwort in Datei schreiben.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_reminders_generate_pdf(ctx, id, output, dry_run, assume_yes, extra_params):
    """Generate reminder PDF"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoiceReminders/" + id + "/pdf",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=output, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@invoice_reminders_group.command("list-referenced-faktura-documents-for")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_reminders_list_referenced_faktura_documents_for(ctx, id, extra_params):
    """List referenced documents"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/invoiceReminders/" + id + "/referencedFakturaDocuments",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@invoice_reminders_group.command("attach-documents-to")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_reminders_attach_documents_to(ctx, id, dry_run, assume_yes, extra_params):
    """Attach documents to reminder"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoiceReminders/" + id + "/attachDocuments",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@invoice_reminders_group.command("add-documents-to")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_reminders_add_documents_to(ctx, id, dry_run, assume_yes, extra_params):
    """Add documents to reminder"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoiceReminders/" + id + "/addDocuments",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@invoice_reminders_group.command("get-or-create-chat")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_reminders_get_or_create_chat(ctx, id, dry_run, assume_yes, extra_params):
    """Get or create reminder chat"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoiceReminders/" + id + "/chat",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@invoice_reminders_group.command("create-from", short_help="🟡 Create reminders from invoices")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_reminders_create_from(ctx, data, dry_run, assume_yes, extra_params):
    """Create reminders from invoices"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoiceReminders/createInvoiceReminders",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

def register(root):
    root.add_command(invoice_reminders_group)
