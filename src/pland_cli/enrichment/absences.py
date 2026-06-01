from __future__ import annotations

import click

from pland_cli.enrichment._filters import filter_by_date_range
from pland_cli.enrichment.registry import enrich, get_client
from pland_cli.utils import output as out_mod
from pland_cli.utils.timestamps import parse_date, to_ms


@enrich("absences", "in-range", new=True)
@click.command()
@click.option("--from", "frm", required=True, help="Start YYYY-MM-DD.")
@click.option("--to", "to", required=True, help="Ende YYYY-MM-DD.")
@click.option("--approved-only", is_flag=True, help="Nur genehmigte (approvedBy gesetzt).")
@click.pass_context
def absences_in_range(ctx: click.Context, frm: str, to: str, approved_only: bool) -> None:
    """Abwesenheiten im Zeitraum (clientseitig nach dtStart gefiltert)."""
    out_mod.set_json(ctx.obj.get("as_json", False))
    client = get_client(ctx)
    from_ms = to_ms(parse_date(frm))
    to_ms_end = to_ms(parse_date(to)) + 86_400_000 - 1
    rows = list(filter_by_date_range(
        client, "/absences/", None,
        from_ms=from_ms, to_ms=to_ms_end, date_field="dtStart",
    ))
    if approved_only:
        rows = [r for r in rows if r.get("approvedBy")]
    out_mod.out(rows)
