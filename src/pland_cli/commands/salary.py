"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("salary")
def salary_group():
    """salary-Operationen."""
    pass

@salary_group.command("list-salaries")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort as JSON: {\"by\":\"<field>\",\"direction\":1} (1 asc, -1 desc). The spec's \"field:1\" form returns 400.")
@click.option("--status", "status", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--user", "user", default=None, help="")
@click.option("--from", "from_", default=None, help="")
@click.option("--to", "to", default=None, help="")
@click.option("--object", "object", default=None, help="")
@click.option("--objectIds", "objectIds", default=None, help="")
@click.option("--objectsByName", "objectsByName", default=None, help="")
@click.option("--fromWithIncludedTrackingDate", "fromWithIncludedTrackingDate", default=None, help="")
@click.option("--activityTypeId", "activityTypeId", default=None, help="")
@click.option("--jobIds", "jobIds", default=None, help="")
@click.option("--trackingJobDate", "trackingJobDate", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_salary_list_salaries(ctx, limit, offset, sort, status, ids, user, from_, to, object, objectIds, objectsByName, fromWithIncludedTrackingDate, activityTypeId, jobIds, trackingJobDate, generalField, fetch_all, extra_params):
    """List salaries"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/salaries/",
        query={"limit": limit, "offset": offset, "sort": sort, "status": status, "ids": ids, "user": user, "from": from_, "to": to, "object": object, "objectIds": objectIds, "objectsByName": objectsByName, "fromWithIncludedTrackingDate": fromWithIncludedTrackingDate, "activityTypeId": activityTypeId, "jobIds": jobIds, "trackingJobDate": trackingJobDate, "generalField": generalField}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@salary_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_salary_get(ctx, id, extra_params):
    """Get salary by ID"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/salaries/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@salary_group.command("delete", short_help="🔴 Delete salary")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_salary_delete(ctx, id, dry_run, assume_yes, confirm_token, extra_params):
    """Delete salary"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/salaries/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@salary_group.command("update", short_help="🔴 Update salary")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_salary_update(ctx, id, data, dry_run, assume_yes, confirm_token, extra_params):
    """Update salary"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/salaries/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@salary_group.command("get-chat")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_salary_get_chat(ctx, id, dry_run, assume_yes, confirm_token, extra_params):
    """Get or create salary chat"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/salaries/" + id + "/chat",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@salary_group.command("release-using-time-tracking", short_help="🔴 Release salary using time tracking")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_salary_release_using_time_tracking(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Release salary using time tracking"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/salaries/releaseWithTimeTracking",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@salary_group.command("release-using-job", short_help="🔴 Release salary using job")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_salary_release_using_job(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Release salary using job"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/salaries/releaseWithJob",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@salary_group.command("get-groups")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_salary_get_groups(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Get salary groups"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/salaries/getSalaryGroups",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@salary_group.command("get-overview-for-users")
@click.option("--from", "from_", default=None, type=int, help="Start date for the salary period (UTC timestamp)")
@click.option("--to", "to", default=None, type=int, help="End date for the salary period (UTC timestamp)")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_salary_get_overview_for_users(ctx, from_, to, data, dry_run, assume_yes, confirm_token, extra_params):
    """Get salary overview for users"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/salaries/overview/users",
        query={"from": from_, "to": to}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@salary_group.command("get-overview-for-objects")
@click.option("--from", "from_", default=None, type=int, help="Start date for the salary period (UTC timestamp)")
@click.option("--to", "to", default=None, type=int, help="End date for the salary period (UTC timestamp)")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_salary_get_overview_for_objects(ctx, from_, to, data, dry_run, assume_yes, confirm_token, extra_params):
    """Get salary overview for objects"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/salaries/overview/objects",
        query={"from": from_, "to": to}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@salary_group.command("get-user-absence-salaries")
@click.argument("USERID")
@click.option("--from", "from_", default=None, type=int, help="Start date for the salary period (UTC timestamp)")
@click.option("--to", "to", default=None, type=int, help="End date for the salary period (UTC timestamp)")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_salary_get_user_absence_salaries(ctx, userid, from_, to, extra_params):
    """Get user absence salaries"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/users/" + userid + "/absenceSalaries",
        query={"from": from_, "to": to}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@salary_group.command("get-user-salaries")
@click.argument("USERID")
@click.option("--from", "from_", default=None, type=int, help="Start date for the salary period (UTC timestamp)")
@click.option("--to", "to", default=None, type=int, help="End date for the salary period (UTC timestamp)")
@click.option("--includeForTrackingDate", "includeForTrackingDate", default=None, type=bool, help="Include salaries based on tracking date instead of salary period")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_salary_get_user_salaries(ctx, userid, from_, to, includeForTrackingDate, extra_params):
    """Get user salaries"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/users/" + userid + "/salaries",
        query={"from": from_, "to": to, "includeForTrackingDate": includeForTrackingDate}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
        confirm_token=None,
    )

@salary_group.command("export-rows-in-background")
@click.option("--from", "from_", default=None, type=int, help="Start date for the salary period (UTC timestamp)")
@click.option("--to", "to", default=None, type=int, help="End date for the salary period (UTC timestamp)")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_salary_export_rows_in_background(ctx, from_, to, data, dry_run, assume_yes, confirm_token, extra_params):
    """Export salary rows in background"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/salaries/exportSalaryRowsInBackground",
        query={"from": from_, "to": to}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@salary_group.command("export-rows")
@click.option("--from", "from_", default=None, type=int, help="Start date for the salary period (UTC timestamp)")
@click.option("--to", "to", default=None, type=int, help="End date for the salary period (UTC timestamp)")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--output", type=click.Path(), help="Write the response to a file.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_salary_export_rows(ctx, from_, to, data, output, dry_run, assume_yes, confirm_token, extra_params):
    """Export salary rows"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/salaries/exportSalaryRows",
        query={"from": from_, "to": to}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=output, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@salary_group.command("export-for-objects")
@click.option("--exportType", "exportType", default=None, help="Type of export format (e.g., csv, excel, pdf)")
@click.option("--from", "from_", default=None, type=int, help="Start date for the salary period (UTC timestamp)")
@click.option("--to", "to", default=None, type=int, help="End date for the salary period (UTC timestamp)")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--output", type=click.Path(), help="Write the response to a file.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_salary_export_for_objects(ctx, exportType, from_, to, data, output, dry_run, assume_yes, confirm_token, extra_params):
    """Export salary data for objects"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/salaries/objectExport",
        query={"exportType": exportType, "from": from_, "to": to}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=output, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@salary_group.command("release-all-times-in-time-frame", short_help="🔴 Release all times in time frame")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_salary_release_all_times_in_time_frame(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Release all times in time frame"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/salaries/releaseInTimeFrame",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

@salary_group.command("release-job-occurrences", short_help="🔴 Release job occurrences")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user's explicit go; the token still has to match.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_salary_release_job_occurrences(ctx, data, dry_run, assume_yes, confirm_token, extra_params):
    """Release job occurrences"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/salaries/releaseJobOccurrences",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
        confirm_token=confirm_token,
    )

def register(root):
    root.add_command(salary_group)
