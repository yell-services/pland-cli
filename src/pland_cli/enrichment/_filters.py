from __future__ import annotations

from typing import Iterator

from pland_cli.core.pagination import paginate


def filter_by_date_range(client, path: str, base_params: dict | None,
                         from_ms: int, to_ms: int, date_field: str) -> Iterator[dict]:
    """Fetch every item (paginated, _id-deduplicated) and filter client-side.

    pland's from/to query filter omits freshly synchronised entries, so we pull
    everything and filter here on `date_field` within [from_ms, to_ms].
    """
    for item in paginate(client, path, base_params):
        ts = item.get(date_field)
        if ts is not None and from_ms <= int(ts) <= to_ms:
            yield item
