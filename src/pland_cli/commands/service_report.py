"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("service-report")
def service_report_group():
    """service-report-Operationen."""
    pass

@service_report_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--serviceReportTypeOf", "serviceReportTypeOf", default=None, help="")
@click.option("--assignmentIds", "assignmentIds", default=None, help="")
@click.option("--activityTypeId", "activityTypeId", default=None, help="")
@click.option("--customerId", "customerId", default=None, help="")
@click.option("--objectIds", "objectIds", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_list(ctx, limit, offset, serviceReportTypeOf, assignmentIds, activityTypeId, customerId, objectIds, generalField, fetch_all, extra_params):
    """List service reports"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/serviceReports/",
        query={"limit": limit, "offset": offset, "serviceReportTypeOf": serviceReportTypeOf, "assignmentIds": assignmentIds, "activityTypeId": activityTypeId, "customerId": customerId, "objectIds": objectIds, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@service_report_group.command("create")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_create(ctx, data, dry_run, assume_yes, extra_params):
    """Create service report"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/serviceReports/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@service_report_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_get(ctx, id, extra_params):
    """Get service report"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/serviceReports/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@service_report_group.command("delete", short_help="🟡 Delete service report")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_delete(ctx, id, dry_run, assume_yes, extra_params):
    """Delete service report"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/serviceReports/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@service_report_group.command("update", short_help="🟡 Update service report")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_update(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update service report"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/serviceReports/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@service_report_group.command("get-last-number")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_get_last_number(ctx, fetch_all, extra_params):
    """Get last service report number"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/serviceReports/lastNumber",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@service_report_group.command("get-count")
@click.option("--serviceReportTypeOf", "serviceReportTypeOf", default=None, help="")
@click.option("--assignmentIds", "assignmentIds", default=None, help="")
@click.option("--activityTypeId", "activityTypeId", default=None, help="")
@click.option("--customerId", "customerId", default=None, help="")
@click.option("--objectIds", "objectIds", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_get_count(ctx, serviceReportTypeOf, assignmentIds, activityTypeId, customerId, objectIds, generalField, fetch_all, extra_params):
    """Get service report count"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/serviceReports/count",
        query={"serviceReportTypeOf": serviceReportTypeOf, "assignmentIds": assignmentIds, "activityTypeId": activityTypeId, "customerId": customerId, "objectIds": objectIds, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@service_report_group.command("generate-pdf", short_help="🟡 Generate service report PDF")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_generate_pdf(ctx, id, data, dry_run, assume_yes, extra_params):
    """Generate service report PDF"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/serviceReports/" + id + "/generatePDF",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@service_report_group.command("list-referenced-faktura-documents")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_list_referenced_faktura_documents(ctx, id, extra_params):
    """List referenced faktura documents"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/serviceReports/" + id + "/referencedFakturaDocuments",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@service_report_group.command("attach-documents-to")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_attach_documents_to(ctx, id, data, dry_run, assume_yes, extra_params):
    """Attach documents to service report"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/serviceReports/" + id + "/attachDocuments",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@service_report_group.command("add-documents-to")
@click.argument("ID")
@click.option("--file", "file_", type=click.Path(exists=True), help="Datei (multipart).")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_add_documents_to(ctx, id, file_, dry_run, assume_yes, extra_params):
    """Add documents to service report"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/serviceReports/" + id + "/addDocuments",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=file_, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@service_report_group.command("get-or-create-chat")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_get_or_create_chat(ctx, id, extra_params):
    """Get or create service report chat"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/serviceReports/" + id + "/chat",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@service_report_group.command("create-preview", short_help="🟡 Create service report preview")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_create_preview(ctx, data, dry_run, assume_yes, extra_params):
    """Create service report preview"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/serviceReports/createPreview",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@service_report_group.command("duplicate")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_duplicate(ctx, id, dry_run, assume_yes, extra_params):
    """Duplicate service report"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/serviceReports/" + id + "/duplicate",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@service_report_group.command("generate-combined-pdf", short_help="🟡 Generate combined service report PDF")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--output", type=click.Path(), help="Antwort in Datei schreiben.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_generate_combined_pdf(ctx, data, output, dry_run, assume_yes, extra_params):
    """Generate combined service report PDF"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/serviceReports/generateCombinedPDF",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=output, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@service_report_group.command("generate-zip", short_help="🟡 Generate service report ZIP archive")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--output", type=click.Path(), help="Antwort in Datei schreiben.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_generate_zip(ctx, data, output, dry_run, assume_yes, extra_params):
    """Generate service report ZIP archive"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/serviceReports/generateZip",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=output, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@service_report_group.command("set-fixed", short_help="🟡 Set service reports to fixed")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_set_fixed(ctx, data, dry_run, assume_yes, extra_params):
    """Set service reports to fixed"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/serviceReports/setFixed",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@service_report_group.command("get-user")
@click.argument("USERID")
@click.option("--assignmentId", "assignmentId", default=None, help="Filter by specific assignment ID (optional)")
@click.option("--includeFaktured", "includeFaktured", default=None, type=bool, help="Include service reports that have been invoiced (default: false)")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_get_user(ctx, userId, assignmentId, includeFaktured, extra_params):
    """Get user service reports"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/users/" + userId + "/serviceReports",
        query={"assignmentId": assignmentId, "includeFaktured": includeFaktured}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@service_report_group.command("create-from-app", short_help="🟡 Create service report from app")
@click.argument("USERID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_create_from_app(ctx, userId, data, dry_run, assume_yes, extra_params):
    """Create service report from app"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/users/" + userId + "/serviceReports",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@service_report_group.command("sign", short_help="🟡 Sign service report")
@click.argument("USERID")
@click.argument("SERVICEREPORTID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_sign(ctx, userId, serviceReportId, data, dry_run, assume_yes, extra_params):
    """Sign service report"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/users/" + userId + "/serviceReports/" + serviceReportId + "/sign",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@service_report_group.command("set-to-finished", short_help="🟡 Set service reports to finished")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_set_to_finished(ctx, data, dry_run, assume_yes, extra_params):
    """Set service reports to finished"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/serviceReports/setToFinished",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@service_report_group.command("set-to-faktured", short_help="🟡 Set service report to faktured")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_set_to_faktured(ctx, id, data, dry_run, assume_yes, extra_params):
    """Set service report to faktured"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/serviceReports/" + id + "/setToFaktured",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@service_report_group.command("set-multiple-to-faktured", short_help="🟡 Set multiple service reports to faktured")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_service_report_set_multiple_to_faktured(ctx, data, dry_run, assume_yes, extra_params):
    """Set multiple service reports to faktured"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/serviceReports/setMultipleToFaktured",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

def register(root):
    root.add_command(service_report_group)
