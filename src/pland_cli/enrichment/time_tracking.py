from __future__ import annotations

import click

from pland_cli.enrichment._filters import filter_by_date_range
from pland_cli.enrichment.registry import enrich, get_client
from pland_cli.utils import output as out_mod
from pland_cli.utils.timestamps import parse_date, to_ms


@enrich("time-tracking", "in-range", new=True)
@click.command()
@click.option("--from", "frm", required=True, help="Arbeitstag-Start YYYY-MM-DD.")
@click.option("--to", "to", required=True, help="Arbeitstag-Ende YYYY-MM-DD.")
@click.option("--unapproved", is_flag=True, help="Only entries that are not approved.")
@click.pass_context
def timetracking_in_range(ctx: click.Context, frm: str, to: str, unapproved: bool) -> None:
    """Time entries by working day, filtered client-side on trackingJobDate."""
    out_mod.set_json(ctx.obj.get("as_json", False))
    client = get_client(ctx)
    params = {"timeTrackingNotApproved": "true"} if unapproved else {}
    from_ms = to_ms(parse_date(frm))
    to_ms_end = to_ms(parse_date(to)) + 86_400_000 - 1
    rows = list(filter_by_date_range(
        client, "/timetracking/list", params,
        from_ms=from_ms, to_ms=to_ms_end, date_field="trackingJobDate",
    ))
    out_mod.out(rows)
