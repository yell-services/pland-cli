from __future__ import annotations

from datetime import datetime
from zoneinfo import ZoneInfo

BERLIN = ZoneInfo("Europe/Berlin")


def to_ms(dt: datetime) -> int:
    """datetime → Unix-Millisekunden."""
    return int(dt.timestamp() * 1000)


def from_ms(ms: int, tz: ZoneInfo = BERLIN) -> datetime:
    """Unix-Millisekunden → datetime (Default Europe/Berlin)."""
    return datetime.fromtimestamp(ms / 1000, tz=tz)


def parse_date(value: str, tz: ZoneInfo = BERLIN) -> datetime:
    """ISO-Datum 'YYYY-MM-DD' → Mitternacht in der Ziel-Zeitzone."""
    d = datetime.strptime(value, "%Y-%m-%d")
    return d.replace(tzinfo=tz)
