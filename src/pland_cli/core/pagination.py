from __future__ import annotations

from typing import Iterator

_PAGE_SIZE = 500


def paginate(client, path: str, params: dict | None = None,
             page_size: int = _PAGE_SIZE) -> Iterator[dict]:
    """Alle Items eines paginierten Endpoints; dedupliziert per _id (Overlap-Bug)."""
    base = dict(params or {})
    offset = 0
    seen: set = set()
    while True:
        page_params = {**base, "limit": page_size, "offset": offset}
        batch = client.get(path, params=page_params)
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
        if new == 0:
            break
        offset += page_size


def collect_all(client, path: str, params: dict | None = None,
                page_size: int = _PAGE_SIZE) -> list[dict]:
    return list(paginate(client, path, params, page_size))
