"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("absences")
def absences_group():
    """absences-Operationen."""
    pass

@absences_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of absences to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of absences to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort as JSON: {\"by\":\"<field>\",\"direction\":1} (1 asc, -1 desc). The spec's \"field:1\" form returns 400.")
@click.option("--status", "status", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--user", "user", default=None, help="")
@click.option("--userIds", "userIds", default=None, help="")
@click.option("--objectManagers", "objectManagers", default=None, help="")
@click.option("--notFinished", "notFinished", default=None, help="")
@click.option("--assigned", "assigned", default=None, help="")
@click.option("--object", "object", default=None, help="")
@click.option("--end", "end", default=None, help="")
@click.option("--dtEndFrom", "dtEndFrom", default=None, help="")
@click.option("--dtEndTo", "dtEndTo", default=None, help="")
@click.option("--dtStartTo", "dtStartTo", default=None, help="")
@click.option("--absencePayType", "absencePayType", default=None, help="")
@click.option("--userIdsByName", "userIdsByName", default=None, help="")
@click.option("--absenceType", "absenceType", default=None, help="")
@click.option("--affectedObjectIds", "affectedObjectIds", default=None, help="")
@click.option("--employmentUserIds", "employmentUserIds", default=None, help="")
@click.option("--userIdsByTag", "userIdsByTag", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_absences_list(ctx, limit, offset, sort, status, ids, user, userIds, objectManagers, notFinished, assigned, object, end, dtEndFrom, dtEndTo, dtStartTo, absencePayType, userIdsByName, absenceType, affectedObjectIds, employmentUserIds, userIdsByTag, generalField, fetch_all, extra_params):
    """List absences"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/absences/",
        query={"limit": limit, "offset": offset, "sort": sort, "status": status, "ids": ids, "user": user, "userIds": userIds, "objectManagers": objectManagers, "notFinished": notFinished, "assigned": assigned, "object": object, "end": end, "dtEndFrom": dtEndFrom, "dtEndTo": dtEndTo, "dtStartTo": dtStartTo, "absencePayType": absencePayType, "userIdsByName": userIdsByName, "absenceType": absenceType, "affectedObjectIds": affectedObjectIds, "employmentUserIds": employmentUserIds, "userIdsByTag": userIdsByTag, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@absences_group.command("create")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_absences_create(ctx, data, dry_run, assume_yes, extra_params):
    """Create new absence"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/absences/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@absences_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_absences_get(ctx, id, extra_params):
    """Get absence by ID"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/absences/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@absences_group.command("update-full", short_help="🟡 Update absence (full)")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_absences_update_full(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update absence (full)"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='put', path="/absences/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@absences_group.command("delete", short_help="🟡 Delete absence")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_absences_delete(ctx, id, dry_run, assume_yes, extra_params):
    """Delete absence"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/absences/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@absences_group.command("update", short_help="🟡 Update absence")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_absences_update(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update absence"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/absences/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@absences_group.command("list-personal")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of absences to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of absences to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort as JSON: {\"by\":\"<field>\",\"direction\":1} (1 asc, -1 desc). The spec's \"field:1\" form returns 400.")
@click.option("--status", "status", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--absencePayType", "absencePayType", default=None, help="")
@click.option("--absenceType", "absenceType", default=None, help="")
@click.option("--dtEndFrom", "dtEndFrom", default=None, help="")
@click.option("--dtEndTo", "dtEndTo", default=None, help="")
@click.option("--dtStartTo", "dtStartTo", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_absences_list_personal(ctx, limit, offset, sort, status, ids, absencePayType, absenceType, dtEndFrom, dtEndTo, dtStartTo, generalField, fetch_all, extra_params):
    """List personal absences"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/absences/self",
        query={"limit": limit, "offset": offset, "sort": sort, "status": status, "ids": ids, "absencePayType": absencePayType, "absenceType": absenceType, "dtEndFrom": dtEndFrom, "dtEndTo": dtEndTo, "dtStartTo": dtStartTo, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@absences_group.command("approve", short_help="🟡 Approve absence")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_absences_approve(ctx, id, dry_run, assume_yes, extra_params):
    """Approve absence"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/absences/" + id + "/approve",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@absences_group.command("approve-multiple", short_help="🟡 Approve multiple absences")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_absences_approve_multiple(ctx, data, dry_run, assume_yes, extra_params):
    """Approve multiple absences"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/absences/approve-multiple",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@absences_group.command("decline", short_help="🟡 Decline absence")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_absences_decline(ctx, id, data, dry_run, assume_yes, extra_params):
    """Decline absence"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/absences/" + id + "/decline",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@absences_group.command("cancel", short_help="🟡 Cancel absence")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_absences_cancel(ctx, id, data, dry_run, assume_yes, extra_params):
    """Cancel absence"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/absences/" + id + "/cancel",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@absences_group.command("assign-replacements", short_help="🟡 Assign absence replacements")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_absences_assign_replacements(ctx, id, data, dry_run, assume_yes, extra_params):
    """Assign absence replacements"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/absences/" + id + "/assign",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@absences_group.command("get-user-vacation-days")
@click.argument("USERID")
@click.option("--from", "from_", default=None, help="Start date for the calculation period (UTC timestamp)")
@click.option("--to", "to", default=None, help="End date for the calculation period (UTC timestamp)")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_absences_get_user_vacation_days(ctx, userid, from_, to, extra_params):
    """Get user vacation days"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/users/" + userid + "/vacationDays",
        query={"from": from_, "to": to}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@absences_group.command("get-user-days-absent")
@click.argument("USERID")
@click.option("--from", "from_", default=None, help="Start date for the absence period (UTC timestamp)")
@click.option("--to", "to", default=None, help="End date for the absence period (UTC timestamp)")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_absences_get_user_days_absent(ctx, userid, from_, to, extra_params):
    """Get user days absent"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/users/" + userid + "/daysAbsent",
        query={"from": from_, "to": to}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@absences_group.command("count")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_absences_count(ctx, fetch_all, extra_params):
    """Count absences"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/absences/count",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@absences_group.command("count-new")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_absences_count_new(ctx, fetch_all, extra_params):
    """Count new absences"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/absences/countNewEntities",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

def register(root):
    root.add_command(absences_group)
