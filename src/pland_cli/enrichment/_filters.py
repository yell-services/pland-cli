from __future__ import annotations

from typing import Iterator

from pland_cli.core.pagination import paginate


def filter_by_date_range(client, path: str, base_params: dict | None,
                         from_ms: int, to_ms: int, date_field: str) -> Iterator[dict]:
    """Holt alle Items (paginiert + _id-dedupt) und filtert clientseitig.

    pland's from/to-Query-Filter unterschlägt frisch synchronisierte Einträge;
    deshalb ziehen wir alles und filtern hier nach `date_field` in [from_ms, to_ms].
    """
    for item in paginate(client, path, base_params):
        ts = item.get(date_field)
        if ts is not None and from_ms <= int(ts) <= to_ms:
            yield item
