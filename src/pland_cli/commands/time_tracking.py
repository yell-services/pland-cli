"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("time-tracking")
def time_tracking_group():
    """time-tracking-Operationen."""
    pass

@time_tracking_group.command("start-for-job")
@click.argument("JOBID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_time_tracking_start_for_job(ctx, jobid, data, dry_run, assume_yes, extra_params):
    """Start time tracking for a job"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/timetracking/start/" + jobid + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@time_tracking_group.command("start-simple")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_time_tracking_start_simple(ctx, data, dry_run, assume_yes, extra_params):
    """Start simple time tracking"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/timetracking/start",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@time_tracking_group.command("stop")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_time_tracking_stop(ctx, data, dry_run, assume_yes, extra_params):
    """Stop active time tracking"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/timetracking/stop",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@time_tracking_group.command("get-active")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_time_tracking_get_active(ctx, fetch_all, extra_params):
    """Get active time tracking status"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/timetracking/",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@time_tracking_group.command("filter")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of entries to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of entries to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort as JSON: {\"by\":\"<field>\",\"direction\":1} (1 asc, -1 desc). The spec's \"field:1\" form returns 400.")
@click.option("--userId", "userId", default=None, help="")
@click.option("--from", "from_", default=None, help="")
@click.option("--to", "to", default=None, help="")
@click.option("--objectId", "objectId", default=None, help="")
@click.option("--activityTypeId", "activityTypeId", default=None, help="")
@click.option("--status", "status", default=None, help="")
@click.option("--timeTrackingNotApproved", "timeTrackingNotApproved", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_time_tracking_filter(ctx, limit, offset, sort, userId, from_, to, objectId, activityTypeId, status, timeTrackingNotApproved, fetch_all, extra_params):
    """Filter time tracking entries"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/timetracking/list",
        query={"limit": limit, "offset": offset, "sort": sort, "userId": userId, "from": from_, "to": to, "objectId": objectId, "activityTypeId": activityTypeId, "status": status, "timeTrackingNotApproved": timeTrackingNotApproved}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@time_tracking_group.command("list-from-user")
@click.argument("USERID")
@click.option("--from", "from_", default=None, type=int, help="Start timestamp (UTC) for the time range to query")
@click.option("--to", "to", default=None, type=int, help="End timestamp (UTC) for the time range to query")
@click.option("--includeForTrackingDate", "includeForTrackingDate", default=None, type=bool, help="Whether to include entries filtered by tracking date instead of time start")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_time_tracking_list_from_user(ctx, userid, from_, to, includeForTrackingDate, extra_params):
    """Get time tracking entries for a user"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/users/" + userid + "/timeTrackings",
        query={"from": from_, "to": to, "includeForTrackingDate": includeForTrackingDate}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@time_tracking_group.command("sync-offline")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_time_tracking_sync_offline(ctx, data, dry_run, assume_yes, extra_params):
    """Sync single offline time tracking"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/timetracking/sync",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@time_tracking_group.command("sync-offline-batch")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_time_tracking_sync_offline_batch(ctx, data, dry_run, assume_yes, extra_params):
    """Sync multiple offline time tracking entries"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/timetracking/syncBatch",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@time_tracking_group.command("release-by-working", short_help="🔴 Release time tracking by working time (deprecated)")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_time_tracking_release_by_working(ctx, id, dry_run, assume_yes, extra_params):
    """Release time tracking by working time (deprecated)"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/timetracking/" + id + "/workingTime",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
    )

@time_tracking_group.command("release-by-target", short_help="🔴 Release time tracking by target time (deprecated)")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_time_tracking_release_by_target(ctx, id, dry_run, assume_yes, extra_params):
    """Release time tracking by target time (deprecated)"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/timetracking/" + id + "/targetTime",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
    )

@time_tracking_group.command("release-by-custom-by-admin", short_help="🔴 Release time tracking with custom time by admin (deprecated)")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_time_tracking_release_by_custom_by_admin(ctx, id, data, dry_run, assume_yes, extra_params):
    """Release time tracking with custom time by admin (deprecated)"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/timetracking/" + id + "/customTimeByAdmin",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
    )

@time_tracking_group.command("release-by-custom", short_help="🔴 Release time tracking with custom time (deprecated)")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_time_tracking_release_by_custom(ctx, id, data, dry_run, assume_yes, extra_params):
    """Release time tracking with custom time (deprecated)"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/timetracking/" + id + "/customTime",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
    )

@time_tracking_group.command("cancel", short_help="🔴 Cancel time tracking entry")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_time_tracking_cancel(ctx, id, dry_run, assume_yes, extra_params):
    """Cancel time tracking entry"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/timetracking/" + id + "/cancel",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
    )

@time_tracking_group.command("un-cancel", short_help="🔴 Restore cancelled time tracking entry")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_time_tracking_un_cancel(ctx, id, dry_run, assume_yes, extra_params):
    """Restore cancelled time tracking entry"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/timetracking/" + id + "/unCancel",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
    )

@time_tracking_group.command("add-manually")
@click.argument("JOBID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_time_tracking_add_manually(ctx, jobid, data, dry_run, assume_yes, extra_params):
    """Add time tracking manually (deprecated)"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/timetracking/add/" + jobid + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@time_tracking_group.command("get-not-approved-stamps")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of entries to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of entries to skip for pagination")
@click.option("--FilterUser", "FilterUser", default=None, help="Filter by user ID")
@click.option("--FilterFrom", "FilterFrom", default=None, type=int, help="Filter entries from this date (UTC timestamp)")
@click.option("--FilterTo", "FilterTo", default=None, type=int, help="Filter entries until this date (UTC timestamp)")
@click.option("--FilterObject", "FilterObject", default=None, help="Filter by object ID")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_time_tracking_get_not_approved_stamps(ctx, limit, offset, FilterUser, FilterFrom, FilterTo, FilterObject, fetch_all, extra_params):
    """Get not approved time tracking entries"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/timetracking/notApproved",
        query={"limit": limit, "offset": offset, "FilterUser": FilterUser, "FilterFrom": FilterFrom, "FilterTo": FilterTo, "FilterObject": FilterObject}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@time_tracking_group.command("can-be-approved-by-target")
@click.argument("ID")
@click.option("--timeToAdd", "timeToAdd", default=None, type=int, help="Additional time to add for approval check (in minutes)")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_time_tracking_can_be_approved_by_target(ctx, id, timeToAdd, extra_params):
    """Check if time tracking can be approved by target time"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/timetracking/" + id + "/canBeApprovedByTargetTime",
        query={"timeToAdd": timeToAdd}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@time_tracking_group.command("count-new")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_time_tracking_count_new(ctx, fetch_all, extra_params):
    """Count new time trackings"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/timetracking/countNewEntities",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

def register(root):
    root.add_command(time_tracking_group)
