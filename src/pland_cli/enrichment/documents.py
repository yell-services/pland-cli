from __future__ import annotations

from pathlib import Path

import click

from pland_cli._codegen.runtime import show_dry_run
from pland_cli.enrichment.registry import enrich, get_client
from pland_cli.utils import output as out_mod


def _doc_params(kind: str) -> dict:
    """kind='faktura' merges into the invoice; anything else stays a separate attachment."""
    return {"type": "faktura"} if kind == "faktura" else {}


@enrich("documents", "upload", new=True)
@click.command()
@click.argument("PDF", type=click.Path(exists=True))
@click.option("--kind", type=click.Choice(["regular", "faktura"]), default="regular",
              help="faktura = an Rechnung gemergt; regular = separater Anhang.")
@click.option("--user-id", default=None, help="Optionale User-Zuordnung.")
@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")
@click.pass_context
def documents_upload(ctx: click.Context, pdf: str, kind: str, user_id: str | None,
                     dry_run: bool) -> None:
    """PDF hochladen (multipart) mit korrektem faktura/regular-Typ."""
    out_mod.set_json(ctx.obj.get("as_json", False))
    path = Path(pdf)
    data = {"userId": user_id} if user_id else None
    if dry_run:
        show_dry_run(ctx, "post", "/documents/", _doc_params(kind) or None,
                     body=data, file_=pdf)
        return
    client = get_client(ctx)
    with path.open("rb") as fh:
        files = {"file": (path.name, fh, "application/pdf")}
        result = client.post("/documents/", params=_doc_params(kind), files=files, data=data)
    out_mod.out_ok("Dokument hochgeladen", result)
