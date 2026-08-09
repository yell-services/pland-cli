"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("invoice-storno")
def invoice_storno_group():
    """invoice-storno-Operationen."""
    pass

@invoice_storno_group.command("create-pdf")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--output", type=click.Path(), help="Write the response to a file.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_invoice_storno_create_pdf(ctx, data, output, dry_run, assume_yes, extra_params):
    """Generate combined PDF for multiple storno documents"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/stornos/pdf",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=output, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@invoice_storno_group.command("create-preview")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_invoice_storno_create_preview(ctx, data, dry_run, assume_yes, extra_params):
    """Create preview of storno document"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/stornos/preview",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@invoice_storno_group.command("create-send", short_help="🟡 Send storno documents via email")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_invoice_storno_create_send(ctx, data, dry_run, assume_yes, extra_params):
    """Send storno documents via email"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/stornos/send",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@invoice_storno_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_invoice_storno_get(ctx, id, extra_params):
    """Get storno document details"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/stornos/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@invoice_storno_group.command("delete", short_help="🟡 Delete storno document")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_invoice_storno_delete(ctx, id, dry_run, assume_yes, extra_params):
    """Delete storno document"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/stornos/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable="Invoice Storno", assume_yes=assume_yes,
    )

@invoice_storno_group.command("update", short_help="🟡 Update storno document")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_invoice_storno_update(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update storno document"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/stornos/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@invoice_storno_group.command("create-pdf-by-id")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--output", type=click.Path(), help="Write the response to a file.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_invoice_storno_create_pdf_by_id(ctx, id, data, output, dry_run, assume_yes, extra_params):
    """Generate PDF for specific storno document"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/stornos/" + id + "/pdf",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=output, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@invoice_storno_group.command("get-referenced-faktura-documents")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_invoice_storno_get_referenced_faktura_documents(ctx, id, extra_params):
    """Get referenced documents for storno"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/stornos/" + id + "/referencedFakturaDocuments",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@invoice_storno_group.command("create-attach-documents")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_invoice_storno_create_attach_documents(ctx, id, data, dry_run, assume_yes, extra_params):
    """Attach documents to storno"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/stornos/" + id + "/attachDocuments",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@invoice_storno_group.command("create-add-documents")
@click.argument("ID")
@click.option("--file", "file_", type=click.Path(exists=True), help="File (multipart).")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_invoice_storno_create_add_documents(ctx, id, file_, dry_run, assume_yes, extra_params):
    """Add new documents to storno"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/stornos/" + id + "/addDocuments",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=file_, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

def register(root):
    root.add_command(invoice_storno_group)
