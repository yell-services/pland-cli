from __future__ import annotations

import click

from pland_cli.core.pagination import paginate
from pland_cli.enrichment.registry import enrich, get_client
from pland_cli.utils import output as out_mod

_READONLY = ("_id", "object", "customer", "recipient", "assignments",
             "previousInvoices", "totals", "status", "companyId")


def strip_readonly(invoice: dict) -> dict:
    """Entfernt Read-only-Felder vor einem PATCH."""
    return {k: v for k, v in invoice.items() if k not in _READONLY}


@enrich("invoice", "drafts", new=True)
@click.command()
@click.option("--object-id", required=True, help="Objekt-ID (clientseitig gefiltert).")
@click.pass_context
def invoice_drafts(ctx: click.Context, object_id: str) -> None:
    """Entwurfs-Rechnungen (ohne fixDate) eines Objekts.

    pland ignoriert den objectId-Query-Param → wir filtern clientseitig.
    """
    out_mod.set_json(ctx.obj.get("as_json", False))
    client = get_client(ctx)
    drafts = [
        inv for inv in paginate(client, "/invoices/", {"objectId": object_id})
        if inv.get("objectId") == object_id and not inv.get("fixDate")
    ]
    out_mod.out(drafts)
