"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("users")
def users_group():
    """users-Operationen."""
    pass

@users_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of users to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of users to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort as JSON: {\"by\":\"<field>\",\"direction\":1} (1 asc, -1 desc). The spec's \"field:1\" form returns 400.")
@click.option("--name", "name", default=None, help="")
@click.option("--username", "username", default=None, help="")
@click.option("--status", "status", default=None, help="")
@click.option("--employment", "employment", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--excludeIds", "excludeIds", default=None, help="")
@click.option("--tags", "tags", default=None, help="")
@click.option("--activityTypeId", "activityTypeId", default=None, help="")
@click.option("--workedOnObjects", "workedOnObjects", default=None, help="")
@click.option("--worksOnObject", "worksOnObject", default=None, help="")
@click.option("--currentlyWorking", "currentlyWorking", default=None, help="")
@click.option("--basedOnObjectManager", "basedOnObjectManager", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_list(ctx, limit, offset, sort, name, username, status, employment, ids, excludeIds, tags, activityTypeId, workedOnObjects, worksOnObject, currentlyWorking, basedOnObjectManager, fetch_all, extra_params):
    """List users"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/users/",
        query={"limit": limit, "offset": offset, "sort": sort, "name": name, "username": username, "status": status, "employment": employment, "ids": ids, "excludeIds": excludeIds, "tags": tags, "activityTypeId": activityTypeId, "workedOnObjects": workedOnObjects, "worksOnObject": worksOnObject, "currentlyWorking": currentlyWorking, "basedOnObjectManager": basedOnObjectManager}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@users_group.command("create")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_create(ctx, data, dry_run, assume_yes, extra_params):
    """Create a new user"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/users/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@users_group.command("get-last-number")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_get_last_number(ctx, fetch_all, extra_params):
    """Get last user number"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/users/lastNumber",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@users_group.command("get-distinct-values")
@click.option("--fieldKey", "fieldKey", default=None, help="Field name to get distinct values for (e.g., employment, tags, contact.city)")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_get_distinct_values(ctx, fieldKey, fetch_all, extra_params):
    """Get user distinct values"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/users/distinctValues",
        query={"fieldKey": fieldKey}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@users_group.command("count")
@click.option("--name", "name", default=None, help="")
@click.option("--username", "username", default=None, help="")
@click.option("--status", "status", default=None, help="")
@click.option("--employment", "employment", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--excludeIds", "excludeIds", default=None, help="")
@click.option("--tags", "tags", default=None, help="")
@click.option("--activityTypeId", "activityTypeId", default=None, help="")
@click.option("--workedOnObjects", "workedOnObjects", default=None, help="")
@click.option("--worksOnObject", "worksOnObject", default=None, help="")
@click.option("--currentlyWorking", "currentlyWorking", default=None, help="")
@click.option("--basedOnObjectManager", "basedOnObjectManager", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_count(ctx, name, username, status, employment, ids, excludeIds, tags, activityTypeId, workedOnObjects, worksOnObject, currentlyWorking, basedOnObjectManager, fetch_all, extra_params):
    """Count users"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/users/count",
        query={"name": name, "username": username, "status": status, "employment": employment, "ids": ids, "excludeIds": excludeIds, "tags": tags, "activityTypeId": activityTypeId, "workedOnObjects": workedOnObjects, "worksOnObject": worksOnObject, "currentlyWorking": currentlyWorking, "basedOnObjectManager": basedOnObjectManager}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@users_group.command("get-by-id")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_get_by_id(ctx, id, extra_params):
    """Get user by ID"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/users/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@users_group.command("delete", short_help="🔴 Delete user")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_delete(ctx, id, dry_run, assume_yes, extra_params):
    """Delete user"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/users/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
    )

@users_group.command("update", short_help="🟡 Update user")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_update(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update user"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/users/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@users_group.command("update-many", short_help="🟡 Update multiple users")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_update_many(ctx, data, dry_run, assume_yes, extra_params):
    """Update multiple users"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/users/many",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@users_group.command("get-chat")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_get_chat(ctx, id, dry_run, assume_yes, extra_params):
    """Get or create user chat"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/users/" + id + "/chat",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@users_group.command("generate-password", short_help="🔴 Generate new password for user")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_generate_password(ctx, id, dry_run, assume_yes, extra_params):
    """Generate new password for user"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/users/" + id + "/generatePassword",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
    )

@users_group.command("set-device-token")
@click.argument("TOKEN")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_set_device_token(ctx, token, dry_run, assume_yes, extra_params):
    """Set device token for push notifications"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/users/setDeviceToken/" + token + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@users_group.command("set-web-push-token")
@click.argument("TOKEN")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_set_web_push_token(ctx, token, dry_run, assume_yes, extra_params):
    """Set web push token for browser notifications"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/users/webPushToken/" + token + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@users_group.command("send-smsto-all", short_help="🔴 Send SMS credentials to all users")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_send_smsto_all(ctx, dry_run, assume_yes, extra_params):
    """Send SMS credentials to all users"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/users/sendSMSToAllUsers",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
    )

@users_group.command("set-home-location")
@click.argument("USERID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_set_home_location(ctx, userid, data, dry_run, assume_yes, extra_params):
    """Set user home location"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/users/" + userid + "/location",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@users_group.command("set-profile-image")
@click.argument("USERID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_set_profile_image(ctx, userid, data, dry_run, assume_yes, extra_params):
    """Set user profile image"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/users/" + userid + "/profileImage",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@users_group.command("get-all-employment-types")
@click.option("--filterPassiveUserGroups", "filterPassiveUserGroups", default=None, type=bool, help="Filter out passive user groups")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_get_all_employment_types(ctx, filterPassiveUserGroups, fetch_all, extra_params):
    """Get all employment types"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/users/allEmploymentTypes",
        query={"filterPassiveUserGroups": filterPassiveUserGroups}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@users_group.command("set-last-time-active")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_set_last_time_active(ctx, dry_run, assume_yes, extra_params):
    """Update user last active time"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/users/lastTimeActive",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@users_group.command("filter")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_filter(ctx, data, dry_run, assume_yes, extra_params):
    """Filter users with advanced criteria"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/users/filter",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@users_group.command("get-by-number")
@click.argument("USERNUMBER")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_get_by_number(ctx, usernumber, extra_params):
    """Get user by number"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/users/" + usernumber + "/byNumber",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@users_group.command("set-end-date-for-and-all-jobs", short_help="🔴 Set end date for user and their jobs")
@click.argument("ID")
@click.option("--data", default=None, help="Request body as a JSON string.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 always requires terminal input).")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_set_end_date_for_and_all_jobs(ctx, id, data, dry_run, assume_yes, extra_params):
    """Set end date for user and their jobs"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/users/" + id + "/setEndDateForUserAndAllJobsOfUser",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
    )

@users_group.command("get-available-tags")
@click.option("--name", "name", default=None, help="")
@click.option("--username", "username", default=None, help="")
@click.option("--status", "status", default=None, help="")
@click.option("--employment", "employment", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--excludeIds", "excludeIds", default=None, help="")
@click.option("--tags", "tags", default=None, help="")
@click.option("--activityTypeId", "activityTypeId", default=None, help="")
@click.option("--workedOnObjects", "workedOnObjects", default=None, help="")
@click.option("--worksOnObject", "worksOnObject", default=None, help="")
@click.option("--currentlyWorking", "currentlyWorking", default=None, help="")
@click.option("--basedOnObjectManager", "basedOnObjectManager", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_get_available_tags(ctx, name, username, status, employment, ids, excludeIds, tags, activityTypeId, workedOnObjects, worksOnObject, currentlyWorking, basedOnObjectManager, fetch_all, extra_params):
    """Get available user tags"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/users/tags",
        query={"name": name, "username": username, "status": status, "employment": employment, "ids": ids, "excludeIds": excludeIds, "tags": tags, "activityTypeId": activityTypeId, "workedOnObjects": workedOnObjects, "worksOnObject": worksOnObject, "currentlyWorking": currentlyWorking, "basedOnObjectManager": basedOnObjectManager}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@users_group.command("get-own")
@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")
@click.option("--extra-params", default=None, help="Additional query params as JSON.")
@click.pass_context
def _cmd_users_get_own(ctx, fetch_all, extra_params):
    """Get the user the API key belongs to"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/users/self",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

def register(root):
    root.add_command(users_group)
