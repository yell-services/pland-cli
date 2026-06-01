"""Nimmt echte (read-only) Responses auf und scrubbt PII.

Nutzung: PLAND_API_KEY=... uv run python tests/record_fixtures.py
Schreibt anonymisierte JSON-Fixtures nach tests/fixtures/.
"""
from __future__ import annotations

import json
from pathlib import Path

from pland_cli.core.client import PlandClient
from pland_cli.core.config import resolve_config

FIXTURE_DIR = Path(__file__).parent / "fixtures"
_PII_KEYS = {"firstName", "lastName", "email", "phone", "street", "city", "iban", "bic"}


def scrub(obj):
    if isinstance(obj, dict):
        return {k: ("***" if k in _PII_KEYS else scrub(v)) for k, v in obj.items()}
    if isinstance(obj, list):
        return [scrub(x) for x in obj]
    return obj


def record(client: PlandClient, name: str, path: str, params: dict | None = None) -> None:
    data = client.get(path, params=params)
    (FIXTURE_DIR / name).write_text(json.dumps(scrub(data), indent=2, ensure_ascii=False))
    print(f"→ {name} ({len(data) if isinstance(data, list) else 1} Einträge)")


def main() -> None:
    client = PlandClient(resolve_config())
    record(client, "users_page.json", "/users/", {"limit": 3})
    record(client, "absences_page.json", "/absences/", {"limit": 3})
    # Salary-Objekt-Fixture braucht eine echte objectId — manuell ergänzen.


if __name__ == "__main__":
    main()
