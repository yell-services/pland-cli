from __future__ import annotations

import calendar

import click

from pland_cli.enrichment._filters import filter_by_date_range
from pland_cli.enrichment.registry import enrich, get_client
from pland_cli.utils import output as out_mod
from pland_cli.utils.timestamps import parse_date, to_ms


@enrich("salary", "for-object", new=True)
@click.command()
@click.option("--object-id", required=True, help="Objekt-ID (Einsatzort).")
@click.option("--from", "frm", required=True, help="Startdatum YYYY-MM-DD (inklusive).")
@click.option("--to", "to", required=True, help="Enddatum YYYY-MM-DD (inklusive).")
@click.pass_context
def salaries_for_object(ctx: click.Context, object_id: str, frm: str, to: str) -> None:
    """Abgerechnete Zeiteinträge eines Objekts im Zeitraum (clientseitig gefiltert)."""
    out_mod.set_json(ctx.obj.get("as_json", False))
    client = get_client(ctx)
    from_ms = to_ms(parse_date(frm))
    to_ms_end = to_ms(parse_date(to)) + 86_400_000 - 1  # bis Tagesende
    rows = list(filter_by_date_range(
        client, "/salaries/", {"objectId": object_id},
        from_ms=from_ms, to_ms=to_ms_end, date_field="from",
    ))
    out_mod.out(rows)


@enrich("salary", "monthly-report", new=True)
@click.command()
@click.option("--object-id", required=True, help="Objekt-ID (Einsatzort).")
@click.option("--year", type=int, required=True, help="Jahr (z. B. 2024).")
@click.option("--month", type=int, required=True, help="Monat 1-12.")
@click.pass_context
def salaries_monthly_report(ctx: click.Context, object_id: str, year: int, month: int) -> None:
    """Aggregiert Arbeitsstunden eines Objekts für einen Monat."""
    out_mod.set_json(ctx.obj.get("as_json", False))
    client = get_client(ctx)
    last_day = calendar.monthrange(year, month)[1]
    from_ms = to_ms(parse_date(f"{year:04d}-{month:02d}-01"))
    to_ms_end = to_ms(parse_date(f"{year:04d}-{month:02d}-{last_day:02d}")) + 86_400_000 - 1
    rows = list(filter_by_date_range(
        client, "/salaries/", {"objectId": object_id},
        from_ms=from_ms, to_ms=to_ms_end, date_field="from",
    ))
    total_seconds = sum(int(r.get("workingTime", 0)) for r in rows)
    out_mod.out({
        "object_id": object_id,
        "year": year,
        "month": month,
        "entries": len(rows),
        "total_hours": round(total_seconds / 3600, 2),
    })
