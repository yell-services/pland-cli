"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("material-orders")
def material_orders_group():
    """material-orders-Operationen."""
    pass

@material_orders_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="")
@click.option("--offset", "offset", default=None, type=int, help="")
@click.option("--sort", "sort", default=None, help="Sort as JSON: {\"by\":\"<field>\",\"direction\":1} (1 asc, -1 desc). The spec's \"field:1\" form returns 400.")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_material_orders_list(ctx, limit, offset, sort, fetch_all, extra_params):
    """List all orders"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/orders/",
        query={"limit": limit, "offset": offset, "sort": sort}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@material_orders_group.command("count")
@click.option("--status", "status", default=None, help="")
@click.option("--ids", "ids", default=None, help="")
@click.option("--objectId", "objectId", default=None, help="")
@click.option("--objectIds", "objectIds", default=None, help="")
@click.option("--objectManagers", "objectManagers", default=None, help="")
@click.option("--objectName", "objectName", default=None, help="")
@click.option("--orderStatus", "orderStatus", default=None, help="")
@click.option("--from", "from_", default=None, help="")
@click.option("--to", "to", default=None, help="")
@click.option("--customerIds", "customerIds", default=None, help="")
@click.option("--searchOrders", "searchOrders", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_material_orders_count(ctx, status, ids, objectId, objectIds, objectManagers, objectName, orderStatus, from_, to, customerIds, searchOrders, fetch_all, extra_params):
    """Count orders"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/orders/count",
        query={"status": status, "ids": ids, "objectId": objectId, "objectIds": objectIds, "objectManagers": objectManagers, "objectName": objectName, "orderStatus": orderStatus, "from": from_, "to": to, "customerIds": customerIds, "searchOrders": searchOrders}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@material_orders_group.command("count-new")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_material_orders_count_new(ctx, fetch_all, extra_params):
    """Count new orders"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/orders/countNewEntities",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@material_orders_group.command("get-distinct-values")
@click.option("--fieldKey", "fieldKey", default=None, help="Field name to get distinct values for")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_material_orders_get_distinct_values(ctx, fieldKey, fetch_all, extra_params):
    """Get distinct values for orders"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/orders/distinctValues",
        query={"fieldKey": fieldKey}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@material_orders_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_material_orders_get(ctx, id, extra_params):
    """Get order by ID"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/orders/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@material_orders_group.command("delete", short_help="🟡 Delete order")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_material_orders_delete(ctx, id, dry_run, assume_yes, extra_params):
    """Delete order"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/orders/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@material_orders_group.command("update", short_help="🟡 Update order")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_material_orders_update(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update order"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/orders/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@material_orders_group.command("get-or-create-chat")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_material_orders_get_or_create_chat(ctx, id, dry_run, assume_yes, extra_params):
    """Get/create material order chat"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/orders/" + id + "/chat",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@material_orders_group.command("finish", short_help="🟡 Mark order as finished")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_material_orders_finish(ctx, id, dry_run, assume_yes, extra_params):
    """Mark order as finished"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/orders/" + id + "/finishOrder",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@material_orders_group.command("remove-item", short_help="🟡 Remove order item")
@click.argument("ID")
@click.argument("TYPE")
@click.argument("ORDERITEMID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_material_orders_remove_item(ctx, id, type, orderItemId, dry_run, assume_yes, extra_params):
    """Remove order item"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/orders/" + id + "/" + type + "/" + orderItemId + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@material_orders_group.command("change-budget", short_help="🟡 Change order items budget or adds article if missing")
@click.argument("ID")
@click.argument("ARTICLEID")
@click.argument("BUDGET")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_material_orders_change_budget(ctx, id, articleId, budget, dry_run, assume_yes, extra_params):
    """Change order items budget or adds article if missing"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/orders/" + id + "/" + articleId + "/" + budget + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@material_orders_group.command("get-pdf")
@click.argument("ID")
@click.option("--output", type=click.Path(), help="Antwort in Datei schreiben.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_material_orders_get_pdf(ctx, id, output, extra_params):
    """Generate order PDF"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/orders/" + id + "/pdf",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=output, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

def register(root):
    root.add_command(material_orders_group)
