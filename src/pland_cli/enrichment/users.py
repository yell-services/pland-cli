from __future__ import annotations

import click

from pland_cli.core.pagination import paginate
from pland_cli.enrichment.registry import enrich, get_client
from pland_cli.utils import output as out_mod


@enrich("users", "active", new=True)
@click.command()
@click.pass_context
def users_active(ctx: click.Context) -> None:
    """Only active employees (status.status == '1')."""
    out_mod.set_json(ctx.obj.get("as_json", False))
    client = get_client(ctx)
    active = [
        u for u in paginate(client, "/users/", None)
        if (u.get("status") or {}).get("status") == "1"
    ]
    out_mod.out(active)
