"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("invoice")
def invoice_group():
    """invoice-Operationen."""
    pass

@invoice_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort field and direction (e.g. issuedOn:-1, documentNumber:1)")
@click.option("--invoiceTypeOf", "invoiceTypeOf", default=None, help="")
@click.option("--assignmentIds", "assignmentIds", default=None, help="")
@click.option("--activityTypeId", "activityTypeId", default=None, help="")
@click.option("--invoiceByReminderTemplate", "invoiceByReminderTemplate", default=None, help="")
@click.option("--status", "status", default=None, help="")
@click.option("--name", "name", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--customer", "customer", default=None, help="")
@click.option("--objectIds", "objectIds", default=None, help="")
@click.option("--objectIdsByTag", "objectIdsByTag", default=None, help="")
@click.option("--statusTags", "statusTags", default=None, help="")
@click.option("--referenceIds", "referenceIds", default=None, help="")
@click.option("--fakturaDocuments", "fakturaDocuments", default=None, help="")
@click.option("--issuedOnFrom", "issuedOnFrom", default=None, help="")
@click.option("--issuedOnTo", "issuedOnTo", default=None, help="")
@click.option("--documentNumber", "documentNumber", default=None, help="")
@click.option("--fakturaDocumentNames", "fakturaDocumentNames", default=None, help="")
@click.option("--documentPrefix", "documentPrefix", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_list(ctx, limit, offset, sort, invoiceTypeOf, assignmentIds, activityTypeId, invoiceByReminderTemplate, status, name, ids, customer, objectIds, objectIdsByTag, statusTags, referenceIds, fakturaDocuments, issuedOnFrom, issuedOnTo, documentNumber, fakturaDocumentNames, documentPrefix, generalField, fetch_all, extra_params):
    """List invoices"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/invoices/",
        query={"limit": limit, "offset": offset, "sort": sort, "invoiceTypeOf": invoiceTypeOf, "assignmentIds": assignmentIds, "activityTypeId": activityTypeId, "invoiceByReminderTemplate": invoiceByReminderTemplate, "status": status, "name": name, "ids": ids, "customer": customer, "objectIds": objectIds, "objectIdsByTag": objectIdsByTag, "statusTags": statusTags, "referenceIds": referenceIds, "fakturaDocuments": fakturaDocuments, "issuedOnFrom": issuedOnFrom, "issuedOnTo": issuedOnTo, "documentNumber": documentNumber, "fakturaDocumentNames": fakturaDocumentNames, "documentPrefix": documentPrefix, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@invoice_group.command("create")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_create(ctx, data, dry_run, assume_yes, extra_params):
    """Create invoice"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoices/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@invoice_group.command("get-last-number")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_get_last_number(ctx, fetch_all, extra_params):
    """Get last invoice number"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/invoices/lastNumber",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@invoice_group.command("count")
@click.option("--invoiceTypeOf", "invoiceTypeOf", default=None, help="")
@click.option("--assignmentIds", "assignmentIds", default=None, help="")
@click.option("--activityTypeId", "activityTypeId", default=None, help="")
@click.option("--invoiceByReminderTemplate", "invoiceByReminderTemplate", default=None, help="")
@click.option("--status", "status", default=None, help="")
@click.option("--name", "name", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--customer", "customer", default=None, help="")
@click.option("--objectIds", "objectIds", default=None, help="")
@click.option("--objectIdsByTag", "objectIdsByTag", default=None, help="")
@click.option("--statusTags", "statusTags", default=None, help="")
@click.option("--referenceIds", "referenceIds", default=None, help="")
@click.option("--fakturaDocuments", "fakturaDocuments", default=None, help="")
@click.option("--issuedOnFrom", "issuedOnFrom", default=None, help="")
@click.option("--issuedOnTo", "issuedOnTo", default=None, help="")
@click.option("--documentNumber", "documentNumber", default=None, help="")
@click.option("--fakturaDocumentNames", "fakturaDocumentNames", default=None, help="")
@click.option("--documentPrefix", "documentPrefix", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_count(ctx, invoiceTypeOf, assignmentIds, activityTypeId, invoiceByReminderTemplate, status, name, ids, customer, objectIds, objectIdsByTag, statusTags, referenceIds, fakturaDocuments, issuedOnFrom, issuedOnTo, documentNumber, fakturaDocumentNames, documentPrefix, generalField, fetch_all, extra_params):
    """Count invoices"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/invoices/count",
        query={"invoiceTypeOf": invoiceTypeOf, "assignmentIds": assignmentIds, "activityTypeId": activityTypeId, "invoiceByReminderTemplate": invoiceByReminderTemplate, "status": status, "name": name, "ids": ids, "customer": customer, "objectIds": objectIds, "objectIdsByTag": objectIdsByTag, "statusTags": statusTags, "referenceIds": referenceIds, "fakturaDocuments": fakturaDocuments, "issuedOnFrom": issuedOnFrom, "issuedOnTo": issuedOnTo, "documentNumber": documentNumber, "fakturaDocumentNames": fakturaDocumentNames, "documentPrefix": documentPrefix, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@invoice_group.command("get-distinct-values")
@click.option("--field", "field", default=None, help="Field name to get distinct values for")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_get_distinct_values(ctx, field, fetch_all, extra_params):
    """Get distinct field values"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/invoices/distinctValues",
        query={"field": field}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@invoice_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_get(ctx, id, extra_params):
    """Get invoice by ID"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/invoices/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@invoice_group.command("delete", short_help="🟡 Delete invoice")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_delete(ctx, id, dry_run, assume_yes, extra_params):
    """Delete invoice"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/invoices/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable="Invoice", assume_yes=assume_yes,
    )

@invoice_group.command("update", short_help="🟡 Update invoice")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_update(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update invoice"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/invoices/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@invoice_group.command("set-fixed", short_help="🟡 Set invoices to fixed status")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_set_fixed(ctx, data, dry_run, assume_yes, extra_params):
    """Set invoices to fixed status"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoices/setFixed",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@invoice_group.command("set-canceled", short_help="🔴 Cancel invoices")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_set_canceled(ctx, data, dry_run, assume_yes, extra_params):
    """Cancel invoices"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoices/setToCanceled",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
    )

@invoice_group.command("create-stripe-account-link")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_create_stripe_account_link(ctx, fetch_all, extra_params):
    """Create Stripe account connection link"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/invoices/settings/createLinkToConnectStripeAccount",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@invoice_group.command("create-payment-link")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_create_payment_link(ctx, id, extra_params):
    """Create payment link for invoice"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/invoices/" + id + "/createPaymentLink",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@invoice_group.command("link-to-credit", short_help="🟡 Link invoice to credit")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_link_to_credit(ctx, id, data, dry_run, assume_yes, extra_params):
    """Link invoice to credit"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoices/" + id + "/createCredit",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@invoice_group.command("link-to-reminder", short_help="🟡 Link invoice to reminder")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_link_to_reminder(ctx, id, data, dry_run, assume_yes, extra_params):
    """Link invoice to reminder"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoices/" + id + "/createInvoiceReminder",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@invoice_group.command("get-transactions")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_get_transactions(ctx, id, extra_params):
    """Get matching transactions for invoice"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/invoices/" + id + "/transactions",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@invoice_group.command("generate-multiple-zugferd-pdfs", short_help="🟡 Generate ZUGFeRD PDFs for multiple invoices")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--output", type=click.Path(), help="Antwort in Datei schreiben.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_generate_multiple_zugferd_pdfs(ctx, data, output, dry_run, assume_yes, extra_params):
    """Generate ZUGFeRD PDFs for multiple invoices"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoices/generateZugferdPdfs",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=output, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@invoice_group.command("generate-single-zugferd-pdf", short_help="🟡 Generate ZUGFeRD PDF for invoice")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--output", type=click.Path(), help="Antwort in Datei schreiben.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_generate_single_zugferd_pdf(ctx, data, output, dry_run, assume_yes, extra_params):
    """Generate ZUGFeRD PDF for invoice"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoices/generateZugferdPdf",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=output, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@invoice_group.command("export")
@click.option("--from", "from_", default=None, type=int, help="Start date for export (UTC timestamp in milliseconds)")
@click.option("--to", "to", default=None, type=int, help="End date for export (UTC timestamp in milliseconds)")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--output", type=click.Path(), help="Antwort in Datei schreiben.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_export(ctx, from_, to, data, output, dry_run, assume_yes, extra_params):
    """Export invoices"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoices/export",
        query={"from": from_, "to": to}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=output, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@invoice_group.command("send-with-zugferd", short_help="🟡 Send invoices with ZUGFeRD attachments")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_send_with_zugferd(ctx, data, dry_run, assume_yes, extra_params):
    """Send invoices with ZUGFeRD attachments"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoices/sendZugferd",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@invoice_group.command("send-with-xrechnung", short_help="🟡 Send invoices with XRechnung attachments")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_send_with_xrechnung(ctx, data, dry_run, assume_yes, extra_params):
    """Send invoices with XRechnung attachments"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoices/sendXRechnung",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@invoice_group.command("generate-xinvoice-xml", short_help="🟡 Generate XRechnung XML for invoice")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--output", type=click.Path(), help="Antwort in Datei schreiben.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_generate_xinvoice_xml(ctx, data, output, dry_run, assume_yes, extra_params):
    """Generate XRechnung XML for invoice"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoices/generateXInvoice",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=output, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@invoice_group.command("generate-remaining-payments", short_help="🟡 Generate remaining payments for invoices")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_generate_remaining_payments(ctx, data, dry_run, assume_yes, extra_params):
    """Generate remaining payments for invoices"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoices/generateRemainingPayments",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@invoice_group.command("get-dashboard-data")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_invoice_get_dashboard_data(ctx, data, dry_run, assume_yes, extra_params):
    """Get invoice dashboard data"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/invoices/dashboard",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

def register(root):
    root.add_command(invoice_group)
