"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("complaints")
def complaints_group():
    """complaints-Operationen."""
    pass

@complaints_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort field and direction (e.g. number:1, status.createdAt:-1)")
@click.option("--status", "status", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--objectIds", "objectIds", default=None, help="")
@click.option("--object", "object", default=None, help="")
@click.option("--customerIds", "customerIds", default=None, help="")
@click.option("--objectManager", "objectManager", default=None, help="")
@click.option("--objectManagers", "objectManagers", default=None, help="")
@click.option("--objectsByName", "objectsByName", default=None, help="")
@click.option("--userIds", "userIds", default=None, help="")
@click.option("--user", "user", default=None, help="")
@click.option("--complaintStatus", "complaintStatus", default=None, help="")
@click.option("--from", "from_", default=None, help="")
@click.option("--to", "to", default=None, help="")
@click.option("--searchComplaint", "searchComplaint", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_complaints_list(ctx, limit, offset, sort, status, ids, objectIds, object, customerIds, objectManager, objectManagers, objectsByName, userIds, user, complaintStatus, from_, to, searchComplaint, generalField, fetch_all, extra_params):
    """List complaints"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/complaints/",
        query={"limit": limit, "offset": offset, "sort": sort, "status": status, "ids": ids, "objectIds": objectIds, "object": object, "customerIds": customerIds, "objectManager": objectManager, "objectManagers": objectManagers, "objectsByName": objectsByName, "userIds": userIds, "user": user, "complaintStatus": complaintStatus, "from": from_, "to": to, "searchComplaint": searchComplaint, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@complaints_group.command("create")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_complaints_create(ctx, data, dry_run, assume_yes, extra_params):
    """Create complaint"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/complaints/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@complaints_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_complaints_get(ctx, id, extra_params):
    """Get complaint by ID"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/complaints/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@complaints_group.command("delete", short_help="🟡 Delete complaint")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_complaints_delete(ctx, id, dry_run, assume_yes, extra_params):
    """Delete complaint"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/complaints/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@complaints_group.command("update", short_help="🟡 Update complaint")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_complaints_update(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update complaint"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/complaints/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@complaints_group.command("count")
@click.option("--status", "status", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--objectIds", "objectIds", default=None, help="")
@click.option("--object", "object", default=None, help="")
@click.option("--customerIds", "customerIds", default=None, help="")
@click.option("--objectManager", "objectManager", default=None, help="")
@click.option("--objectManagers", "objectManagers", default=None, help="")
@click.option("--objectsByName", "objectsByName", default=None, help="")
@click.option("--userIds", "userIds", default=None, help="")
@click.option("--user", "user", default=None, help="")
@click.option("--complaintStatus", "complaintStatus", default=None, help="")
@click.option("--from", "from_", default=None, help="")
@click.option("--to", "to", default=None, help="")
@click.option("--searchComplaint", "searchComplaint", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_complaints_count(ctx, status, ids, objectIds, object, customerIds, objectManager, objectManagers, objectsByName, userIds, user, complaintStatus, from_, to, searchComplaint, generalField, fetch_all, extra_params):
    """Count complaints"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/complaints/count",
        query={"status": status, "ids": ids, "objectIds": objectIds, "object": object, "customerIds": customerIds, "objectManager": objectManager, "objectManagers": objectManagers, "objectsByName": objectsByName, "userIds": userIds, "user": user, "complaintStatus": complaintStatus, "from": from_, "to": to, "searchComplaint": searchComplaint, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@complaints_group.command("count-new")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_complaints_count_new(ctx, fetch_all, extra_params):
    """Count new complaints"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/complaints/countNewEntities",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@complaints_group.command("get-distinct-values")
@click.option("--field", "field", default=None, help="Field name to get distinct values for")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_complaints_get_distinct_values(ctx, field, fetch_all, extra_params):
    """Get complaint distinct values"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/complaints/distinctValues",
        query={"field": field}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@complaints_group.command("get-monitor")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_complaints_get_monitor(ctx, fetch_all, extra_params):
    """Get complaint monitor data"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/complaints/monitor",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@complaints_group.command("get-user")
@click.argument("USERID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_complaints_get_user(ctx, userId, extra_params):
    """Get user complaints"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/users/" + userId + "/complaints",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@complaints_group.command("assign", short_help="🟡 Assign complaint to user")
@click.argument("COMPLAINTID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_complaints_assign(ctx, complaintId, data, dry_run, assume_yes, extra_params):
    """Assign complaint to user"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/complaints/" + complaintId + "/assign",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@complaints_group.command("resolve", short_help="🟡 Resolve complaint")
@click.argument("COMPLAINTID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_complaints_resolve(ctx, complaintId, data, dry_run, assume_yes, extra_params):
    """Resolve complaint"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/complaints/" + complaintId + "/resolve",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@complaints_group.command("count-user")
@click.argument("USERID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_complaints_count_user(ctx, userId, extra_params):
    """Count user complaints"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/users/" + userId + "/countComplaints",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@complaints_group.command("generate-response")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_complaints_generate_response(ctx, id, extra_params):
    """Generate AI response for complaint"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/complaints/" + id + "/generateResponse",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@complaints_group.command("get-generations-left")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_complaints_get_generations_left(ctx, fetch_all, extra_params):
    """Get remaining AI generations"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/complaints/generationsLeft",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

def register(root):
    root.add_command(complaints_group)
