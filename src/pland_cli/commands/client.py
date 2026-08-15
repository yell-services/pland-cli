"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("client")
def client_group():
    """client-Operationen."""
    pass

@client_group.command("create-unauthorized-complain", short_help="🟡 Create complaint")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_client_create_unauthorized_complain(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Create complaint"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/client/complain",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@client_group.command("upload-to-complaint")
@click.argument("OBJECTID")
@click.option("--file", "file_", type=click.Path(exists=True), help="File (multipart).")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_client_upload_to_complaint(ctx, objectid, file_, dry_run, extra_params):
    """Upload complaint image"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/client/" + objectid + "/upload",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=file_, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@client_group.command("upload-documents")
@click.argument("OBJECTID")
@click.option("--file", "file_", type=click.Path(exists=True), help="File (multipart).")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_client_upload_documents(ctx, objectid, file_, dry_run, extra_params):
    """Upload documents"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/client/" + objectid + "/uploadDocuments",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=file_, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@client_group.command("get-object-documentation")
@click.argument("OBJECTID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_client_get_object_documentation(ctx, objectid, extra_params):
    """Get object documentation"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/client/" + objectid + "/documentation",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@client_group.command("get-company-info-unauthorized")
@click.argument("OBJECTID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_client_get_company_info_unauthorized(ctx, objectid, extra_params):
    """Get company info"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/client/" + objectid + "/company",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@client_group.command("get-offer")
@click.argument("ID")
@click.option("--zipCode", "zipCode", default=None, help="ZIP code of the customer for verification")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_client_get_offer(ctx, id, zipCode, extra_params):
    """Get offer document"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/client/faktura/offers/" + id + "",
        query={"zipCode": zipCode}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@client_group.command("get-invoice")
@click.argument("ID")
@click.option("--zipCode", "zipCode", default=None, help="ZIP code of the customer for verification")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_client_get_invoice(ctx, id, zipCode, extra_params):
    """Get invoice document"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/client/faktura/invoices/" + id + "",
        query={"zipCode": zipCode}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@client_group.command("get-credit")
@click.argument("ID")
@click.option("--zipCode", "zipCode", default=None, help="ZIP code of the customer for verification")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_client_get_credit(ctx, id, zipCode, extra_params):
    """Get credit document"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/client/faktura/credits/" + id + "",
        query={"zipCode": zipCode}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@client_group.command("accept-offer")
@click.argument("ID")
@click.option("--zipCode", "zipCode", default=None, help="ZIP code of the customer for verification")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_client_accept_offer(ctx, id, zipCode, extra_params):
    """Accept offer"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/client/faktura/offers/" + id + "/accept",
        query={"zipCode": zipCode}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@client_group.command("decline-offer")
@click.argument("ID")
@click.option("--zipCode", "zipCode", default=None, help="ZIP code of the customer for verification")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_client_decline_offer(ctx, id, zipCode, extra_params):
    """Decline offer"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/client/faktura/offers/" + id + "/decline",
        query={"zipCode": zipCode}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@client_group.command("create-user-unauthorized")
@click.argument("COMPANYID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_client_create_user_unauthorized(ctx, companyid, data, dry_run, extra_params):
    """Create user (unauthorized)"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/client/" + companyid + "/users/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@client_group.command("update-user-unauthorized", short_help="🟡 Update user (unauthorized)")
@click.argument("COMPANYID")
@click.argument("USERID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_client_update_user_unauthorized(ctx, companyid, userid, data, dry_run, assume_yes, confirm_token, extra_params):
    """Update user (unauthorized)"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/client/" + companyid + "/users/" + userid + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@client_group.command("create-unauthorized-task", short_help="🟡 Create task")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_client_create_unauthorized_task(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Create task"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/client/task",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

def register(root):
    root.add_command(client_group)
