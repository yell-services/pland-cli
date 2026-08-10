"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("upload")
def upload_group():
    """upload-Operationen."""
    pass

@upload_group.command("list")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_upload_list(ctx, fetch_all, extra_params):
    """List all uploads"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/upload/",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@upload_group.command("csv", short_help="🟡 CSV import for various entities")
@click.argument("TYPE")
@click.option("--file", "file_", type=click.Path(exists=True), help="File (multipart).")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_upload_csv(ctx, type, file_, dry_run, assume_yes, extra_params):
    """CSV import for various entities"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/upload/" + type + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=file_, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@upload_group.command("image", short_help="🟡 Image upload")
@click.argument("UPLOADPATH")
@click.option("--file", "file_", type=click.Path(exists=True), help="File (multipart).")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_upload_image(ctx, uploadpath, file_, dry_run, assume_yes, extra_params):
    """Image upload"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/upload/images/" + uploadpath + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=file_, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@upload_group.command("camt-transactions", short_help="🟡 camt v8 xml upload")
@click.option("--file", "file_", type=click.Path(exists=True), help="File (multipart).")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_upload_camt_transactions(ctx, file_, dry_run, assume_yes, extra_params):
    """camt v8 xml upload"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/upload/camtTransactions",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=file_, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@upload_group.command("get-image-safe")
@click.argument("UPLOADID")
@click.option("--output", type=click.Path(), help="Write the response to a file.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_upload_get_image_safe(ctx, uploadid, output, extra_params):
    """Get image by upload ID"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/upload/images/" + uploadid + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=output, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

def register(root):
    root.add_command(upload_group)
