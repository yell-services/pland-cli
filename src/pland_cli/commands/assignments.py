"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("assignments")
def assignments_group():
    """assignments-Operationen."""
    pass

@assignments_group.command("duplicate")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assignments_duplicate(ctx, data, dry_run, assume_yes, extra_params):
    """Duplicate assignments"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/assignments/duplicate",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@assignments_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort as JSON: {\"by\":\"<field>\",\"direction\":1} (1 asc, -1 desc). The spec's \"field:1\" form returns 400.")
@click.option("--status", "status", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--type", "type", default=None, help="")
@click.option("--objectIds", "objectIds", default=None, help="")
@click.option("--objectIdsByTag", "objectIdsByTag", default=None, help="")
@click.option("--name", "name", default=None, help="")
@click.option("--activityTypeId", "activityTypeId", default=None, help="")
@click.option("--assignmentBillingTypes", "assignmentBillingTypes", default=None, help="")
@click.option("--assignmentSearch", "assignmentSearch", default=None, help="")
@click.option("--assignmentBillingType", "assignmentBillingType", default=None, help="")
@click.option("--assignmentStatus", "assignmentStatus", default=None, help="")
@click.option("--assignmentsWithProductIds", "assignmentsWithProductIds", default=None, help="")
@click.option("--customer", "customer", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assignments_list(ctx, limit, offset, sort, status, ids, type, objectIds, objectIdsByTag, name, activityTypeId, assignmentBillingTypes, assignmentSearch, assignmentBillingType, assignmentStatus, assignmentsWithProductIds, customer, generalField, fetch_all, extra_params):
    """List assignments"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/assignments/",
        query={"limit": limit, "offset": offset, "sort": sort, "status": status, "ids": ids, "type": type, "objectIds": objectIds, "objectIdsByTag": objectIdsByTag, "name": name, "activityTypeId": activityTypeId, "assignmentBillingTypes": assignmentBillingTypes, "assignmentSearch": assignmentSearch, "assignmentBillingType": assignmentBillingType, "assignmentStatus": assignmentStatus, "assignmentsWithProductIds": assignmentsWithProductIds, "customer": customer, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@assignments_group.command("get-last-number")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assignments_get_last_number(ctx, fetch_all, extra_params):
    """Get last assignment number"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/assignments/lastNumber",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@assignments_group.command("get-distinct-field-values")
@click.option("--fieldKey", "fieldKey", default=None, help="Field name to get distinct values for")
@click.option("--status", "status", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--type", "type", default=None, help="")
@click.option("--objectIds", "objectIds", default=None, help="")
@click.option("--objectIdsByTag", "objectIdsByTag", default=None, help="")
@click.option("--name", "name", default=None, help="")
@click.option("--activityTypeId", "activityTypeId", default=None, help="")
@click.option("--assignmentBillingTypes", "assignmentBillingTypes", default=None, help="")
@click.option("--assignmentSearch", "assignmentSearch", default=None, help="")
@click.option("--assignmentBillingType", "assignmentBillingType", default=None, help="")
@click.option("--assignmentStatus", "assignmentStatus", default=None, help="")
@click.option("--assignmentsWithProductIds", "assignmentsWithProductIds", default=None, help="")
@click.option("--customer", "customer", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assignments_get_distinct_field_values(ctx, fieldKey, status, ids, type, objectIds, objectIdsByTag, name, activityTypeId, assignmentBillingTypes, assignmentSearch, assignmentBillingType, assignmentStatus, assignmentsWithProductIds, customer, generalField, fetch_all, extra_params):
    """Get distinct field values"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/assignments/distinctValues",
        query={"fieldKey": fieldKey, "status": status, "ids": ids, "type": type, "objectIds": objectIds, "objectIdsByTag": objectIdsByTag, "name": name, "activityTypeId": activityTypeId, "assignmentBillingTypes": assignmentBillingTypes, "assignmentSearch": assignmentSearch, "assignmentBillingType": assignmentBillingType, "assignmentStatus": assignmentStatus, "assignmentsWithProductIds": assignmentsWithProductIds, "customer": customer, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@assignments_group.command("count-with-filter")
@click.option("--status", "status", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--type", "type", default=None, help="")
@click.option("--objectIds", "objectIds", default=None, help="")
@click.option("--objectIdsByTag", "objectIdsByTag", default=None, help="")
@click.option("--name", "name", default=None, help="")
@click.option("--activityTypeId", "activityTypeId", default=None, help="")
@click.option("--assignmentBillingTypes", "assignmentBillingTypes", default=None, help="")
@click.option("--assignmentSearch", "assignmentSearch", default=None, help="")
@click.option("--assignmentBillingType", "assignmentBillingType", default=None, help="")
@click.option("--assignmentStatus", "assignmentStatus", default=None, help="")
@click.option("--assignmentsWithProductIds", "assignmentsWithProductIds", default=None, help="")
@click.option("--customer", "customer", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assignments_count_with_filter(ctx, status, ids, type, objectIds, objectIdsByTag, name, activityTypeId, assignmentBillingTypes, assignmentSearch, assignmentBillingType, assignmentStatus, assignmentsWithProductIds, customer, generalField, fetch_all, extra_params):
    """Count assignments with filter"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/assignments/count",
        query={"status": status, "ids": ids, "type": type, "objectIds": objectIds, "objectIdsByTag": objectIdsByTag, "name": name, "activityTypeId": activityTypeId, "assignmentBillingTypes": assignmentBillingTypes, "assignmentSearch": assignmentSearch, "assignmentBillingType": assignmentBillingType, "assignmentStatus": assignmentStatus, "assignmentsWithProductIds": assignmentsWithProductIds, "customer": customer, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@assignments_group.command("update-many", short_help="🟡 Update multiple assignments")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assignments_update_many(ctx, data, dry_run, assume_yes, extra_params):
    """Update multiple assignments"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/assignments/many",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@assignments_group.command("view")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assignments_view(ctx, id, extra_params):
    """Get assignment by ID"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/assignments/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@assignments_group.command("delete", short_help="🟡 Delete assignment")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assignments_delete(ctx, id, dry_run, assume_yes, extra_params):
    """Delete assignment"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/assignments/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@assignments_group.command("update", short_help="🟡 Update assignment")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assignments_update(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update assignment"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/assignments/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@assignments_group.command("get-or-create-chat")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assignments_get_or_create_chat(ctx, id, dry_run, assume_yes, extra_params):
    """Get or create assignment chat"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/assignments/" + id + "/chat",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@assignments_group.command("set-end-date", short_help="🔴 Set assignment and jobs end date")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assignments_set_end_date(ctx, id, data, dry_run, assume_yes, extra_params):
    """Set assignment and jobs end date"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/assignments/" + id + "/setEndDateForAssignmentAndAllJobsOnAssignment",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
    )

@assignments_group.command("get-user")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assignments_get_user(ctx, id, extra_params):
    """Get user assignments"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/users/" + id + "/assignments",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@assignments_group.command("generate-recurring-invoices", short_help="🟡 Generate recurring invoices (Debug)")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assignments_generate_recurring_invoices(ctx, dry_run, assume_yes, extra_params):
    """Generate recurring invoices (Debug)"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/assignments/generateRecurringInvoices",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@assignments_group.command("create-invoices-for", short_help="🟡 Create invoices for assignments")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assignments_create_invoices_for(ctx, data, dry_run, assume_yes, extra_params):
    """Create invoices for assignments"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/assignments/createInvoices",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@assignments_group.command("create-service-reports-for", short_help="🟡 Create service reports for assignments")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assignments_create_service_reports_for(ctx, data, dry_run, assume_yes, extra_params):
    """Create service reports for assignments"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/assignments/createServiceReports",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@assignments_group.command("realize-dynamic-positions", short_help="🟡 Realize dynamic positions")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assignments_realize_dynamic_positions(ctx, id, data, dry_run, assume_yes, extra_params):
    """Realize dynamic positions"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/assignments/" + id + "/realizeDynamicPositions",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@assignments_group.command("get-partial-invoices-for")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assignments_get_partial_invoices_for(ctx, id, extra_params):
    """Get partial invoices for assignment"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/assignments/" + id + "/partialInvoices",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@assignments_group.command("get-next-invoice-date-preview")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assignments_get_next_invoice_date_preview(ctx, data, dry_run, assume_yes, extra_params):
    """Preview next invoice dates"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/assignments/nextInvoiceDatePreview",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@assignments_group.command("calculate-capacities")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assignments_calculate_capacities(ctx, data, dry_run, assume_yes, extra_params):
    """Calculate assignment capacities"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/assignments/capacities",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@assignments_group.command("calculate-covers")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assignments_calculate_covers(ctx, data, dry_run, assume_yes, extra_params):
    """Calculate assignment coverage"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/assignments/calculateAssignmentCovers",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@assignments_group.command("update-product-prices", short_help="🟡 Update product prices")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_assignments_update_product_prices(ctx, data, dry_run, assume_yes, extra_params):
    """Update product prices"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/assignments/updateProductPrices",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

def register(root):
    root.add_command(assignments_group)
