from __future__ import annotations

import click

from pland_cli.core.pagination import paginate
from pland_cli.enrichment.registry import enrich, get_client
from pland_cli.utils import output as out_mod


@enrich("assignment-confirmations", "list", new=True)
@click.command()
@click.option("--offer-id", default=None,
              help="Nur die Bestätigungen dieses Angebots (spart den Rundgang).")
@click.pass_context
def assignment_confirmations_list(ctx: click.Context, offer_id: str | None) -> None:
    """Assignment confirmations, collected through the offers they came from.

    The API serves no /assignmentConfirmations/ collection, and the generator
    returns no ids — the only handle on a confirmation is the offer it was
    generated from, via that offer's referencedFakturaDocuments.
    """
    out_mod.set_json(ctx.obj.get("as_json", False))
    client = get_client(ctx)

    if offer_id:
        offer_ids = [offer_id]
    else:
        # ponytail: one request per offer, no bulk route exists. Fine at a few
        # hundred offers; if it gets slow, --offer-id skips the walk entirely.
        offer_ids = [o["_id"] for o in paginate(client, "/offers/", {})]

    found: list[dict] = []
    seen: set[str] = set()
    failed: list[str] = []
    for oid in offer_ids:
        try:
            related = client.get(f"/offers/{oid}/referencedFakturaDocuments")
        except Exception:
            # One unreadable offer must not sink the walk, but swallowing it
            # silently would report a short list as if it were complete.
            failed.append(oid)
            continue
        for doc in related if isinstance(related, list) else []:
            if doc.get("documentType") != "assignment_confirmation":
                continue
            if doc.get("_id") in seen:
                continue
            seen.add(doc["_id"])
            found.append({**doc, "offerId": oid})
    if failed:
        click.echo(
            f"Warning: {len(failed)} of {len(offer_ids)} offers could not be read; "
            f"the list may be incomplete. First: {', '.join(failed[:3])}",
            err=True,
        )
    out_mod.out(found)
