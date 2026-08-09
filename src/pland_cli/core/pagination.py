from __future__ import annotations

import json
from typing import Iterator

from pland_cli.core.client import PlandError

_PAGE_SIZE = 500
# Backstop against a server that caps the offset and keeps handing back the same
# page. An error beats a silently truncated result.
_MAX_PAGES = 500

# Without a stable, unique sort the API returns pages in non-deterministic
# order: pagination then produces duplicates and silently drops records
# (506 of 1705 were missing on /invoices/).
_STABLE_SORT = json.dumps({"by": "_id", "direction": 1})


def paginate(client, path: str, params: dict | None = None,
             page_size: int = _PAGE_SIZE) -> Iterator[dict]:
    """Every item of a paginated endpoint, in stable _id order.

    Injects sort={"by":"_id","direction":1} unless the caller supplies its own
    sort. If an endpoint rejects the sort parameter (400), the walk restarts
    once without it; _id deduplication then stays on as a backstop against the
    overlap bug.
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
            # Only a 400 means "this endpoint does not know sort". Continuing
            # without sort on 401/403/500 would silently abandon the stable
            # order — reintroducing the very bug the injection prevents.
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
        # When sorted, a page of nothing but known rows means the end. When
        # unsorted it can be genuine (rows shifted between pages), so only the
        # page ceiling applies there.
        if new == 0 and "sort" in base:
            break
        # Advance by the number of rows *delivered*, not the number requested:
        # some endpoints cap server-side regardless of limit (/salaries/ at 200).
        # With page_size 500 every round skipped 300 rows — measured 9800
        # instead of 24483 records, a 60 % loss.
        offset += len(batch)
    else:
        raise RuntimeError(
            f"{path}: no end after {_MAX_PAGES} pages — pagination is going in circles."
        )


def collect_all(client, path: str, params: dict | None = None,
                page_size: int = _PAGE_SIZE) -> list[dict]:
    return list(paginate(client, path, params, page_size))
