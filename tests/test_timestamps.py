from datetime import datetime
from zoneinfo import ZoneInfo

from pland_cli.utils.timestamps import to_ms, from_ms, parse_date

BERLIN = ZoneInfo("Europe/Berlin")


def test_roundtrip_ms():
    dt = datetime(2024, 4, 15, 8, 0, tzinfo=BERLIN)
    assert from_ms(to_ms(dt)) == dt


def test_to_ms_is_milliseconds():
    dt = datetime(1970, 1, 1, 0, 0, 1, tzinfo=ZoneInfo("UTC"))
    assert to_ms(dt) == 1000


def test_parse_date_returns_berlin_midnight():
    dt = parse_date("2024-04-15")
    assert (dt.year, dt.month, dt.day) == (2024, 4, 15)
    assert dt.tzinfo is not None
