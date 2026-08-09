from __future__ import annotations

import json
from typing import Iterator

from pland_cli.core.client import PlandError

_PAGE_SIZE = 500
# Backstop gegen einen Server, der den Offset deckelt und dieselbe Seite endlos
# weiterreicht. Lieber ein Abbruch mit Fehler als ein still gekuerztes Ergebnis.
_MAX_PAGES = 500

# Ohne stabile, eindeutige Sortierung liefert die API Seiten in
# nicht-deterministischer Reihenfolge: bei Pagination entstehen Duplikate
# und Datensaetze gehen still verloren (bei /invoices/ fehlten 506 von 1705).
_STABLE_SORT = json.dumps({"by": "_id", "direction": 1})


def paginate(client, path: str, params: dict | None = None,
             page_size: int = _PAGE_SIZE) -> Iterator[dict]:
    """Alle Items eines paginierten Endpoints, in stabiler _id-Sortierung.

    Injiziert sort={"by":"_id","direction":1}, sofern der Aufrufer keine
    eigene Sortierung mitgibt. Lehnt ein Endpoint den sort-Param ab (400),
    wird einmal ohne sort neu gestartet; die _id-Deduplizierung bleibt dann
    als Backstop gegen den Overlap-Bug aktiv.
    """
    base = dict(params or {})
    injected_sort = "sort" not in base
    if injected_sort:
        base["sort"] = _STABLE_SORT
    offset = 0
    seen: set = set()
    for _ in range(_MAX_PAGES):
        page_params = {**base, "limit": page_size, "offset": offset}
        try:
            batch = client.get(path, params=page_params)
        except PlandError as exc:
            # Nur 400 heisst "Endpoint kennt sort nicht". Bei 401/403/500 ohne
            # sort weiterzulaufen wuerde die stabile Sortierung still aufgeben —
            # also genau den Bug zurueckholen, den die Injektion verhindert.
            if exc.status == 400 and injected_sort and offset == 0:
                injected_sort = False
                base.pop("sort", None)
                continue
            raise
        if isinstance(batch, dict):
            batch = batch.get("items", [])
        if not batch:
            break
        new = 0
        for item in batch:
            _id = item.get("_id") if isinstance(item, dict) else None
            if _id is not None and _id in seen:
                continue
            if _id is not None:
                seen.add(_id)
            new += 1
            yield item
        # Sortiert heisst: eine Seite aus lauter Bekanntem ist das Ende.
        # Unsortiert kann sie echt sein (die Zeilen haben sich zwischen den
        # Seiten verschoben) — dort greift nur die Seitenobergrenze.
        if new == 0 and "sort" in base:
            break
        # Um die *gelieferte* Zeilenzahl weiter, nicht um die angeforderte:
        # manche Endpoints deckeln serverseitig unabhaengig vom limit
        # (/salaries/ bei 200). Mit page_size 500 uebersprang jede Runde 300
        # Zeilen — gemessen 9800 statt 24483 Datensaetzen, 60 % Verlust.
        offset += len(batch)
    else:
        raise RuntimeError(
            f"{path}: nach {_MAX_PAGES} Seiten kein Ende — die Paginierung dreht sich im Kreis."
        )


def collect_all(client, path: str, params: dict | None = None,
                page_size: int = _PAGE_SIZE) -> list[dict]:
    return list(paginate(client, path, params, page_size))
