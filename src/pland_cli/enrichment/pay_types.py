from __future__ import annotations

import click

from pland_cli.enrichment.registry import enrich, get_client
from pland_cli.utils import output as out_mod


@enrich("pay-types", "wage", new=True)
@click.command()
@click.argument("PAY_TYPE_ID")
@click.pass_context
def pay_type_wage(ctx: click.Context, pay_type_id: str) -> None:
    """Stundenlohn (wage) einer Lohnart auflösen."""
    out_mod.set_json(ctx.obj.get("as_json", False))
    client = get_client(ctx)
    pt = client.get(f"/payTypes/{pay_type_id}")
    out_mod.out({"id": pay_type_id, "name": pt.get("name"), "wage": pt.get("wage")})
