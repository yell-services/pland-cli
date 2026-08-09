"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("jobs")
def jobs_group():
    """jobs-Operationen."""
    pass

@jobs_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort as JSON: {\"by\":\"<field>\",\"direction\":1} (1 asc, -1 desc). The spec's \"field:1\" form returns 400.")
@click.option("--status", "status", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--jobTemplateId", "jobTemplateId", default=None, help="")
@click.option("--originalId", "originalId", default=None, help="")
@click.option("--absenceId", "absenceId", default=None, help="")
@click.option("--notAccepted", "notAccepted", default=None, help="")
@click.option("--objectId", "objectId", default=None, help="")
@click.option("--objectIds", "objectIds", default=None, help="")
@click.option("--teamId", "teamId", default=None, help="")
@click.option("--userIds", "userIds", default=None, help="")
@click.option("--activityTypeId", "activityTypeId", default=None, help="")
@click.option("--currentlyWorking", "currentlyWorking", default=None, help="")
@click.option("--liveJobs", "liveJobs", default=None, help="")
@click.option("--assignmentIds", "assignmentIds", default=None, help="")
@click.option("--tags", "tags", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_jobs_list(ctx, limit, offset, sort, status, ids, jobTemplateId, originalId, absenceId, notAccepted, objectId, objectIds, teamId, userIds, activityTypeId, currentlyWorking, liveJobs, assignmentIds, tags, fetch_all, extra_params):
    """List all jobs"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/jobs/",
        query={"limit": limit, "offset": offset, "sort": sort, "status": status, "ids": ids, "jobTemplateId": jobTemplateId, "originalId": originalId, "absenceId": absenceId, "notAccepted": notAccepted, "objectId": objectId, "objectIds": objectIds, "teamId": teamId, "userIds": userIds, "activityTypeId": activityTypeId, "currentlyWorking": currentlyWorking, "liveJobs": liveJobs, "assignmentIds": assignmentIds, "tags": tags}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@jobs_group.command("list-by-assignment")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_jobs_list_by_assignment(ctx, id, extra_params):
    """List jobs by assignment"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/assignments/" + id + "/jobs",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@jobs_group.command("list-for-user")
@click.argument("USERID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_jobs_list_for_user(ctx, userId, extra_params):
    """List jobs for user"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/users/" + userId + "/jobs",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@jobs_group.command("check-user-capacity")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_jobs_check_user_capacity(ctx, data, dry_run, assume_yes, extra_params):
    """Check user job capacity"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/jobs/checkCapacity",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@jobs_group.command("list-for-object")
@click.argument("OBJECTID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_jobs_list_for_object(ctx, objectId, extra_params):
    """List jobs for object"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/objects/" + objectId + "/jobs",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@jobs_group.command("create")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_jobs_create(ctx, data, dry_run, assume_yes, extra_params):
    """Create a job"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/jobs/v2",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@jobs_group.command("view")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_jobs_view(ctx, id, extra_params):
    """Get job by ID"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/jobs/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@jobs_group.command("delete", short_help="🟡 Delete a job")
@click.argument("ID")
@click.option("--splitDate", "splitDate", default=None, help="Split date for deletion")
@click.option("--type", "type", default=None, help="Delete type")
@click.option("--teamId", "teamId", default=None, help="Team ID (optional, for team job deletion)")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_jobs_delete(ctx, id, splitDate, type, teamId, dry_run, assume_yes, extra_params):
    """Delete a job"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/jobs/" + id + "",
        query={"splitDate": splitDate, "type": type, "teamId": teamId}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@jobs_group.command("patch-old", short_help="🟡 Update a job (legacy)")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_jobs_patch_old(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update a job (legacy)"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/jobs/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@jobs_group.command("patch", short_help="🟡 Update a job")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_jobs_patch(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update a job"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/jobs/" + id + "/v2",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@jobs_group.command("load-resources-and-calendar-data")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_jobs_load_resources_and_calendar_data(ctx, data, dry_run, assume_yes, extra_params):
    """Load resources and calendar data"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/jobs/loadResourcesAndCalendarData",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@jobs_group.command("load-calendar-data")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_jobs_load_calendar_data(ctx, data, dry_run, assume_yes, extra_params):
    """Load calendar data"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/jobs/loadCalendarData",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@jobs_group.command("in-time-frame")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_jobs_in_time_frame(ctx, data, dry_run, assume_yes, extra_params):
    """Get jobs in a specific time frame"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/jobs/jobsInTimeFrame",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@jobs_group.command("change-accepted-status", short_help="🟡 Change job accepted status")
@click.argument("ID")
@click.argument("TYPE")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_jobs_change_accepted_status(ctx, id, type, dry_run, assume_yes, extra_params):
    """Change job accepted status"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/jobs/" + id + "/status/" + type + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@jobs_group.command("mark-as-started")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_jobs_mark_as_started(ctx, id, dry_run, assume_yes, extra_params):
    """Mark job as started"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/jobs/" + id + "/started",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@jobs_group.command("get-open")
@click.option("--from", "from_", default=None, help="Start of the time frame")
@click.option("--to", "to", default=None, help="End of the time frame")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_jobs_get_open(ctx, from_, to, fetch_all, extra_params):
    """Get open jobs"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/jobs/notAssigned",
        query={"from": from_, "to": to}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@jobs_group.command("get-status-list-for")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_jobs_get_status_list_for(ctx, id, extra_params):
    """Get job status list"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/jobs/" + id + "/statusList",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@jobs_group.command("get-status-list-for-object")
@click.argument("OBJECTID")
@click.option("--from", "from_", default=None, help="Start of the time frame")
@click.option("--to", "to", default=None, help="End of the time frame")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_jobs_get_status_list_for_object(ctx, objectId, from_, to, extra_params):
    """Get job status list for object"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/objects/" + objectId + "/statusList",
        query={"from": from_, "to": to}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@jobs_group.command("calculate-target-times-and-allowed-times-for-user-ids")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_jobs_calculate_target_times_and_allowed_times_for_user_ids(ctx, data, dry_run, assume_yes, extra_params):
    """Calculate user target and allowed times"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/jobs/userCapacities",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@jobs_group.command("get-time-tracking-for")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_jobs_get_time_tracking_for(ctx, id, extra_params):
    """Get time tracking entries for a job"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/jobs/" + id + "/timeTrackings",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

def register(root):
    root.add_command(jobs_group)
