"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("assignment-confirmations")
def assignment_confirmations_group():
    """assignment-confirmations-Operationen."""
    pass

@assignment_confirmations_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_assignment_confirmations_get(ctx, id, extra_params):
    """Get assignment confirmation by ID"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/assignmentConfirmations/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@assignment_confirmations_group.command("delete", short_help="🟡 Delete assignment confirmation")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_assignment_confirmations_delete(ctx, id, dry_run, assume_yes, confirm_token, extra_params):
    """Delete assignment confirmation"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/assignmentConfirmations/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@assignment_confirmations_group.command("generate-combined-pdf")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--output", type=click.Path(), help="Write the response to a file.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_assignment_confirmations_generate_combined_pdf(ctx, data, output, dry_run, extra_params):
    """Generate combined PDF"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/assignmentConfirmations/pdf",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=output, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@assignment_confirmations_group.command("create-preview")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_assignment_confirmations_create_preview(ctx, data, dry_run, extra_params):
    """Create assignment confirmation preview"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/assignmentConfirmations/preview",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@assignment_confirmations_group.command("send", short_help="🟡 Send assignment confirmations")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_assignment_confirmations_send(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Send assignment confirmations"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/assignmentConfirmations/send",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@assignment_confirmations_group.command("generate-single-pdf")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--output", type=click.Path(), help="Write the response to a file.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_assignment_confirmations_generate_single_pdf(ctx, id, data, output, dry_run, extra_params):
    """Generate PDF for assignment confirmation"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/assignmentConfirmations/" + id + "/pdf",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=output, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@assignment_confirmations_group.command("list-referenced-documents")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_assignment_confirmations_list_referenced_documents(ctx, id, extra_params):
    """List referenced documents"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/assignmentConfirmations/" + id + "/referencedFakturaDocuments",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@assignment_confirmations_group.command("attach-documents-to")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_assignment_confirmations_attach_documents_to(ctx, id, data, dry_run, extra_params):
    """Attach documents"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/assignmentConfirmations/" + id + "/attachDocuments",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@assignment_confirmations_group.command("add-documents-to")
@click.argument("ID")
@click.option("--file", "file_", type=click.Path(exists=True), help="File (multipart).")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_assignment_confirmations_add_documents_to(ctx, id, file_, dry_run, extra_params):
    """Add new documents"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/assignmentConfirmations/" + id + "/addDocuments",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=file_, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

def register(root):
    root.add_command(assignment_confirmations_group)
