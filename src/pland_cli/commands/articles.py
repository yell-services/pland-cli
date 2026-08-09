"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("articles")
def articles_group():
    """articles-Operationen."""
    pass

@articles_group.command("list")
@click.option("--limit", "limit", default=None, type=int, help="")
@click.option("--offset", "offset", default=None, type=int, help="")
@click.option("--sort", "sort", default=None, help="Sort as JSON: {\"by\":\"<field>\",\"direction\":1} (1 asc, -1 desc). The spec's \"field:1\" form returns 400.")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_articles_list(ctx, limit, offset, sort, fetch_all, extra_params):
    """List all articles"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/articles/",
        query={"limit": limit, "offset": offset, "sort": sort}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@articles_group.command("create-custom")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_articles_create_custom(ctx, data, dry_run, assume_yes, extra_params):
    """Create a new article (custom logic)"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/articles/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@articles_group.command("get-last-number")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_articles_get_last_number(ctx, fetch_all, extra_params):
    """Get last article number"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/articles/lastNumber",
        query={}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@articles_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_articles_get(ctx, id, extra_params):
    """Get article by ID"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/articles/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@articles_group.command("delete")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_articles_delete(ctx, id, dry_run, assume_yes, extra_params):
    """Delete article"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/articles/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@articles_group.command("update")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_articles_update(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update article"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/articles/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@articles_group.command("order-material", short_help="🟡 Order material for an object")
@click.argument("OBJECTID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_articles_order_material(ctx, objectId, data, dry_run, assume_yes, extra_params):
    """Order material for an object"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/objects/" + objectId + "/order",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@articles_group.command("become-default", short_help="🟡 Set article as default for a budget")
@click.argument("ID")
@click.argument("BUDGET")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_articles_become_default(ctx, id, budget, dry_run, assume_yes, extra_params):
    """Set article as default for a budget"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/articles/" + id + "/default/" + budget + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="confirm", draftable=None, assume_yes=assume_yes,
    )

@articles_group.command("is-default")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_articles_is_default(ctx, id, extra_params):
    """Check if article is default"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/articles/" + id + "/default",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@articles_group.command("remove-default")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_articles_remove_default(ctx, id, dry_run, assume_yes, extra_params):
    """Remove article as default"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/articles/" + id + "/default",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@articles_group.command("list-objects-for")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_articles_list_objects_for(ctx, id, extra_params):
    """List objects for an article"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/articles/" + id + "/objects",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@articles_group.command("get-distinct-values-custom")
@click.option("--fieldKey", "fieldKey", default=None, help="Field key to get distinct values for")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_articles_get_distinct_values_custom(ctx, fieldKey, fetch_all, extra_params):
    """Get distinct values for articles (custom)"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/articles/distinctValues",
        query={"fieldKey": fieldKey}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@articles_group.command("update-amount-in-stock")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_articles_update_amount_in_stock(ctx, data, dry_run, assume_yes, extra_params):
    """Update amount in stock for multiple articles"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/articles/updateAmountInStock",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

def register(root):
    root.add_command(articles_group)
