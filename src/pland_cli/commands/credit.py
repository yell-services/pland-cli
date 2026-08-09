"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("credit")
def credit_group():
    """credit-Operationen."""
    pass

@credit_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--creditTypeOf", "creditTypeOf", default=None, help="")
@click.option("--assignmentIds", "assignmentIds", default=None, help="")
@click.option("--activityTypeId", "activityTypeId", default=None, help="")
@click.option("--customerId", "customerId", default=None, help="")
@click.option("--objectIds", "objectIds", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_credit_list(ctx, limit, offset, creditTypeOf, assignmentIds, activityTypeId, customerId, objectIds, generalField, fetch_all, extra_params):
    """List credit notes"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/credits/",
        query={"limit": limit, "offset": offset, "creditTypeOf": creditTypeOf, "assignmentIds": assignmentIds, "activityTypeId": activityTypeId, "customerId": customerId, "objectIds": objectIds, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@credit_group.command("create")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_credit_create(ctx, data, dry_run, assume_yes, extra_params):
    """Create credit note"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/credits/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@credit_group.command("get-last-number")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_credit_get_last_number(ctx, fetch_all, extra_params):
    """Get last credit number"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/credits/lastNumber",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@credit_group.command("get-count")
@click.option("--creditTypeOf", "creditTypeOf", default=None, help="")
@click.option("--assignmentIds", "assignmentIds", default=None, help="")
@click.option("--activityTypeId", "activityTypeId", default=None, help="")
@click.option("--customerId", "customerId", default=None, help="")
@click.option("--objectIds", "objectIds", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_credit_get_count(ctx, creditTypeOf, assignmentIds, activityTypeId, customerId, objectIds, generalField, fetch_all, extra_params):
    """Get credit count"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/credits/count",
        query={"creditTypeOf": creditTypeOf, "assignmentIds": assignmentIds, "activityTypeId": activityTypeId, "customerId": customerId, "objectIds": objectIds, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@credit_group.command("get-distinct-values")
@click.option("--fieldKey", "fieldKey", default=None, help="Field name to get distinct values for")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_credit_get_distinct_values(ctx, fieldKey, fetch_all, extra_params):
    """Get distinct field values"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/credits/distinctValues",
        query={"fieldKey": fieldKey}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@credit_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_credit_get(ctx, id, extra_params):
    """Get credit note"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/credits/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@credit_group.command("delete", short_help="🟡 Delete credit note")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_credit_delete(ctx, id, dry_run, assume_yes, extra_params):
    """Delete credit note"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/credits/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable="Credit", assume_yes=assume_yes,
    )

@credit_group.command("update", short_help="🟡 Update credit note")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_credit_update(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update credit note"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/credits/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@credit_group.command("generate-pdf")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_credit_generate_pdf(ctx, id, data, dry_run, assume_yes, extra_params):
    """Generate credit note PDF"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/credits/" + id + "/pdf",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@credit_group.command("list-referenced-faktura-documents-from")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_credit_list_referenced_faktura_documents_from(ctx, id, extra_params):
    """List referenced faktura documents"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/credits/" + id + "/referencedFakturaDocuments",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@credit_group.command("attach-documents-to")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_credit_attach_documents_to(ctx, id, data, dry_run, assume_yes, extra_params):
    """Attach documents to credit note"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/credits/" + id + "/attachDocuments",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@credit_group.command("add-documents-to")
@click.argument("ID")
@click.option("--file", "file_", type=click.Path(exists=True), help="Datei (multipart).")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_credit_add_documents_to(ctx, id, file_, dry_run, assume_yes, extra_params):
    """Add documents to credit note"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/credits/" + id + "/addDocuments",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=file_, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@credit_group.command("get-or-create-chat")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_credit_get_or_create_chat(ctx, id, dry_run, assume_yes, extra_params):
    """Get or create credit note chat"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/credits/" + id + "/chat",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@credit_group.command("create-preview")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_credit_create_preview(ctx, data, dry_run, assume_yes, extra_params):
    """Create credit note preview"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/credits/preview",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@credit_group.command("duplicate")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_credit_duplicate(ctx, data, dry_run, assume_yes, extra_params):
    """Duplicate credit note"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/credits/duplicate",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@credit_group.command("generate-combined-pdf")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--output", type=click.Path(), help="Antwort in Datei schreiben.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_credit_generate_combined_pdf(ctx, data, output, dry_run, assume_yes, extra_params):
    """Generate combined credit PDF"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/credits/pdf",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=output, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@credit_group.command("generate-zip")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--output", type=click.Path(), help="Antwort in Datei schreiben.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_credit_generate_zip(ctx, data, output, dry_run, assume_yes, extra_params):
    """Generate credit ZIP archive"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/credits/zip",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=output, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@credit_group.command("send", short_help="🟡 Send credit notes")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_credit_send(ctx, data, dry_run, assume_yes, extra_params):
    """Send credit notes"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/credits/send",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@credit_group.command("set-fixed", short_help="🟡 Set credit notes to fixed")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_credit_set_fixed(ctx, data, dry_run, assume_yes, extra_params):
    """Set credit notes to fixed"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/credits/setFixed",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

def register(root):
    root.add_command(credit_group)
