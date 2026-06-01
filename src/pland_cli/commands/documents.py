"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click


@click.group("documents")
def documents_group():
    """documents-Operationen."""
    pass

@documents_group.command("get")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_documents_get(ctx, id, extra_params):
    """Get document by ID"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/documents/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@documents_group.command("delete", short_help="🔴 Delete document")
@click.argument("ID")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_documents_delete(ctx, id, dry_run, assume_yes, extra_params):
    """Delete document"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='delete', path="/documents/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
    )

@documents_group.command("update", short_help="🔴 Update document")
@click.argument("ID")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_documents_update(ctx, id, data, dry_run, assume_yes, extra_params):
    """Update document"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='patch', path="/documents/" + id + "",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="critical", draftable=None, assume_yes=assume_yes,
    )

@documents_group.command("exists")
@click.argument("ID")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_documents_exists(ctx, id, extra_params):
    """Check document existence"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/documents/" + id + "/exists",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@documents_group.command("get-for-entity")
@click.argument("ENTITY")
@click.argument("ID")
@click.option("--includeObjectDocuments", "includeObjectDocuments", default=None, type=bool, help="Only relevant for jobs: If true, also include documents from job's objects")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_documents_get_for_entity(ctx, entity, id, includeObjectDocuments, extra_params):
    """Get documents for an entity"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/" + entity + "/" + id + "/documents",
        query={"includeObjectDocuments": includeObjectDocuments}, extra_params=extra_params, fetch_all=False,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@documents_group.command("list-by-ids")
@click.option("--ids", "ids", default=None, help="")
@click.option("--all", "fetch_all", is_flag=True, help="Alle Seiten paginieren.")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_documents_list_by_ids(ctx, ids, fetch_all, extra_params):
    """List documents by IDs"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='get', path="/documents/",
        query={"ids": ids}, extra_params=extra_params, fetch_all=fetch_all,
        data=None, file_=None, output=None, dry_run=False,
        risk="free", draftable=None, assume_yes=False,
    )

@documents_group.command("create")
@click.option("--file", "file_", type=click.Path(exists=True), help="Datei (multipart).")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_documents_create(ctx, file_, dry_run, assume_yes, extra_params):
    """Upload document(s)"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/documents/",
        query={}, extra_params=extra_params, fetch_all=False,
        data=None, file_=file_, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

@documents_group.command("create-with-url")
@click.option("--data", default=None, help="Request-Body als JSON-String.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Request nur anzeigen, nicht senden.")
@click.option("--yes", "assume_yes", is_flag=True, help="Bestaetigung ueberspringen (nur 🟡; 🔴 verlangt Terminal-Eingabe).")
@click.option("--extra-params", default=None, help="Zusätzliche Query-Params als JSON.")
@click.pass_context
def _cmd_documents_create_with_url(ctx, data, dry_run, assume_yes, extra_params):
    """Create document from URL"""
    from pland_cli._codegen.runtime import run_operation
    run_operation(
        ctx, method='post', path="/documents/withUrl",
        query={}, extra_params=extra_params, fetch_all=False,
        data=data, file_=None, output=None, dry_run=dry_run,
        risk="free", draftable=None, assume_yes=assume_yes,
    )

def register(root):
    root.add_command(documents_group)
