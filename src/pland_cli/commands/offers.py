"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("offers")
def offers_group():
    """offers-Operationen."""
    pass

@offers_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort as JSON: {\"by\":\"<field>\",\"direction\":1} (1 asc, -1 desc). The spec's \"field:1\" form returns 400.")
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
@click.option("--offerTypeOf", "offerTypeOf", default=None, help="")
@click.option("--assignmentIds", "assignmentIds", default=None, help="")
@click.option("--activityTypeId", "activityTypeId", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_list(ctx, limit, offset, sort, status, name, ids, customer, objectIds, objectIdsByTag, statusTags, referenceIds, fakturaDocuments, issuedOnFrom, issuedOnTo, documentNumber, fakturaDocumentNames, documentPrefix, offerTypeOf, assignmentIds, activityTypeId, generalField, fetch_all, extra_params):
    """List offers"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/offers/",
        query={"limit": limit, "offset": offset, "sort": sort, "status": status, "name": name, "ids": ids, "customer": customer, "objectIds": objectIds, "objectIdsByTag": objectIdsByTag, "statusTags": statusTags, "referenceIds": referenceIds, "fakturaDocuments": fakturaDocuments, "issuedOnFrom": issuedOnFrom, "issuedOnTo": issuedOnTo, "documentNumber": documentNumber, "fakturaDocumentNames": fakturaDocumentNames, "documentPrefix": documentPrefix, "offerTypeOf": offerTypeOf, "assignmentIds": assignmentIds, "activityTypeId": activityTypeId, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@offers_group.command("create")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_create(ctx, data, dry_run, extra_params):
    """Create offer"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/offers/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@offers_group.command("attach-documents-to")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_attach_documents_to(ctx, id, data, dry_run, extra_params):
    """Attach documents"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/offers/" + id + "/attachDocuments",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@offers_group.command("add-documents-to")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_add_documents_to(ctx, id, data, dry_run, extra_params):
    """Add documents"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/offers/" + id + "/addDocuments",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@offers_group.command("get-last-number")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_get_last_number(ctx, fetch_all, extra_params):
    """Get last offer number"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/offers/lastNumber",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@offers_group.command("list-referenced-faktura-documents-for")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_list_referenced_faktura_documents_for(ctx, id, extra_params):
    """List related documents"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/offers/" + id + "/referencedFakturaDocuments",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@offers_group.command("count")
@click.option("--status", "status", default=None, help="")
@click.option("--offerTypeOf", "offerTypeOf", default=None, help="")
@click.option("--customerId", "customerId", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_count(ctx, status, offerTypeOf, customerId, fetch_all, extra_params):
    """Count offers"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/offers/count",
        query={"status": status, "offerTypeOf": offerTypeOf, "customerId": customerId}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@offers_group.command("get-distinct-values")
@click.option("--fieldKey", "fieldKey", default=None, help="Field name to get distinct values for")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_get_distinct_values(ctx, fieldKey, fetch_all, extra_params):
    """Get distinct field values"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/offers/distinctValues",
        query={"fieldKey": fieldKey}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@offers_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_get(ctx, id, extra_params):
    """Get offer by ID"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/offers/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@offers_group.command("delete", short_help="🟡 Delete offer")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_delete(ctx, id, dry_run, assume_yes, confirm_token, extra_params):
    """Delete offer"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/offers/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable="Offers", assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@offers_group.command("update", short_help="🟡 Update offer")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_update(ctx, id, data, dry_run, assume_yes, confirm_token, extra_params):
    """Update offer"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/offers/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@offers_group.command("get-or-create-chat")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_get_or_create_chat(ctx, id, dry_run, extra_params):
    """Get/create offer chat"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/offers/" + id + "/chat",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@offers_group.command("create-preview")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--output", type=click.Path(), help="Write the response to a file.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_create_preview(ctx, data, output, dry_run, extra_params):
    """Create offer preview"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/offers/preview",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=output, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@offers_group.command("duplicate")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_duplicate(ctx, data, dry_run, extra_params):
    """Duplicate offers"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/offers/duplicate",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@offers_group.command("generate-combined-pdf")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--output", type=click.Path(), help="Write the response to a file.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_generate_combined_pdf(ctx, data, output, dry_run, extra_params):
    """Generate combined offers PDF"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/offers/pdf",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=output, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@offers_group.command("generate-zip")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--output", type=click.Path(), help="Write the response to a file.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_generate_zip(ctx, data, output, dry_run, extra_params):
    """Generate offers ZIP"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/offers/zip",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=output, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@offers_group.command("send", short_help="🟡 Send offers")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_send(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Send offers"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/offers/send",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@offers_group.command("send-letters", short_help="🟡 Send offer letters")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_send_letters(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Send offer letters"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/offers/sendLetter",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@offers_group.command("calculate-letter-price")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_calculate_letter_price(ctx, data, dry_run, extra_params):
    """Calculate letter price"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/offers/letterPrice",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@offers_group.command("generate-pdf")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--output", type=click.Path(), help="Write the response to a file.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_generate_pdf(ctx, id, data, output, dry_run, extra_params):
    """Generate offer PDF"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/offers/" + id + "/pdf",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=output, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@offers_group.command("set-fixed", short_help="🟡 Set offers to fixed/open")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_set_fixed(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Set offers to fixed/open"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/offers/setFixed",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@offers_group.command("set-to-accepted", short_help="🟡 Set offers to accepted")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_set_to_accepted(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Set offers to accepted"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/offers/setToAccepted",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@offers_group.command("set-to-declined", short_help="🟡 Set offers to declined")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_set_to_declined(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Set offers to declined"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/offers/setToDeclined",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@offers_group.command("generate-assignment-confirmations", short_help="🟡 Generate assignment confirmations")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_generate_assignment_confirmations(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Generate assignment confirmations"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/offers/generateAssignmentConfirmations",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@offers_group.command("link-to-assignment", short_help="🟡 Link offer to assignment")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_link_to_assignment(ctx, id, data, dry_run, assume_yes, confirm_token, extra_params):
    """Link offer to assignment"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/offers/" + id + "/createdAssignmentFromOffer",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@offers_group.command("link-to-invoice", short_help="🟡 Link offer to invoice")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_link_to_invoice(ctx, id, data, dry_run, assume_yes, confirm_token, extra_params):
    """Link offer to invoice"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/offers/" + id + "/createdInvoiceFromOffer",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@offers_group.command("get-partial-invoices-for")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_offers_get_partial_invoices_for(ctx, id, extra_params):
    """Get partial invoices"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/offers/" + id + "/partialInvoices",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

def register(root):
    root.add_command(offers_group)
