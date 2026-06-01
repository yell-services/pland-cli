"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("equipment")
def equipment_group():
    """equipment-Operationen."""
    pass

@equipment_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="Maximum number of items to return")
@click.option("--offset", "offset", default=None, type=int, help="Number of items to skip for pagination")
@click.option("--sort", "sort", default=None, help="Sort field and direction (e.g. serialNumber:1, nextMaintenanceDate:-1)")
@click.option("--equipmentBySerialNumberOrName", "equipmentBySerialNumberOrName", default=None, help="")
@click.option("--objectIds", "objectIds", default=None, help="")
@click.option("--equipmentByCategory", "equipmentByCategory", default=None, help="")
@click.option("--tags", "tags", default=None, help="")
@click.option("--generalField", "generalField", default=None, help="")
@click.option("--status", "status", default=None, help="")
@click.option("--name", "name", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_equipment_list(ctx, limit, offset, sort, equipmentBySerialNumberOrName, objectIds, equipmentByCategory, tags, generalField, status, name, ids, fetch_all, extra_params):
    """List equipment"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/equipment/",
        query={"limit": limit, "offset": offset, "sort": sort, "equipmentBySerialNumberOrName": equipmentBySerialNumberOrName, "objectIds": objectIds, "equipmentByCategory": equipmentByCategory, "tags": tags, "generalField": generalField, "status": status, "name": name, "ids": ids}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@equipment_group.command("create")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_equipment_create(ctx, data, dry_run, assume_yes, extra_params):
    """Create equipment"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/equipment/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@equipment_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_equipment_get(ctx, id, extra_params):
    """Get equipment"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/equipment/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@equipment_group.command("delete", short_help="🟡 Delete equipment")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_equipment_delete(ctx, id, dry_run, assume_yes, extra_params):
    """Delete equipment"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/equipment/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@equipment_group.command("update", short_help="🟡 Update equipment")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_equipment_update(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update equipment"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/equipment/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@equipment_group.command("get-distinct-values")
@click.option("--field", "field", default=None, help="Field name to get distinct values for (e.g. serialNumber, category, tags)")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_equipment_get_distinct_values(ctx, field, fetch_all, extra_params):
    """Get distinct values"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/equipment/distinctValues",
        query={"field": field}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@equipment_group.command("update-many", short_help="🟡 Batch update equipment")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_equipment_update_many(ctx, data, dry_run, assume_yes, extra_params):
    """Batch update equipment"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/equipment/many",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@equipment_group.command("get-or-create-chat")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_equipment_get_or_create_chat(ctx, id, dry_run, assume_yes, extra_params):
    """Get/create equipment chat"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/equipment/" + id + "/chat",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

def register(root):
    root.add_command(equipment_group)
