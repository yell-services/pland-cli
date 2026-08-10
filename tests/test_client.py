from datetime import datetime, timedelta, timezone
from email.utils import format_datetime

import click
import httpx
import pytest

from pland_cli.core.client import (
    _MAX_RETRY_WAIT,
    PlandAuthError,
    PlandClient,
    PlandError,
    _retry_after,
)
from pland_cli.core.config import Config


def _client(handler) -> PlandClient:
    cfg = Config(base_url="https://api.test/v2", api_key="id:secret", profile="prod")
    return PlandClient(cfg, transport=httpx.MockTransport(handler))


def test_missing_key_raises():
    with pytest.raises(PlandAuthError):
        PlandClient(Config(base_url="x", api_key="", profile="prod"))


def test_get_sets_api_key_header_and_returns_json():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        seen["key"] = request.headers.get("x-API-Key")
        return httpx.Response(200, json=[{"_id": "1"}])

    result = _client(handler).get("/users/")
    assert seen["key"] == "id:secret"
    assert result == [{"_id": "1"}]


def test_error_maps_pland_format():
    def handler(request):
        return httpx.Response(
            400, json={"message": "There was an error", "errors": [{"message": "Not found."}]}
        )

    with pytest.raises(PlandError) as exc:
        _client(handler).get("/nope")
    assert exc.value.status == 400
    assert "Not found." in exc.value.detail


def test_binary_response_returned_as_bytes():
    def handler(request):
        return httpx.Response(200, content=b"PK\x03\x04zip", headers={"content-type": "application/zip"})

    result = _client(handler).get("/salaries/export-rows")
    assert result == b"PK\x03\x04zip"


def test_post_forwards_data_form_fields():
    seen = {}

    def handler(request):
        seen["content_type"] = request.headers["content-type"]
        body = request.content.decode("latin-1")
        seen["has_field"] = 'name="userId"' in body
        seen["has_value"] = "u42" in body
        return httpx.Response(200, json={"_id": "doc1"})

    result = _client(handler).post(
        "/documents/",
        data={"userId": "u42"},
        files={"file": ("x.pdf", b"%PDF", "application/pdf")},
    )
    assert result == {"_id": "doc1"}
    assert seen["content_type"].startswith("multipart/")
    assert seen["has_field"] is True
    assert seen["has_value"] is True


def test_429_retries_then_succeeds(monkeypatch):
    monkeypatch.setattr("pland_cli.core.client.time.sleep", lambda s: None)
    calls = {"n": 0}

    def handler(request):
        calls["n"] += 1
        if calls["n"] == 1:
            return httpx.Response(429, headers={"Retry-After": "1"}, json={})
        return httpx.Response(200, json={"ok": True})

    result = _client(handler).get("/x")
    assert calls["n"] == 2
    assert result == {"ok": True}


def _recording_handler(seen):
    def handler(request: httpx.Request) -> httpx.Response:
        seen.append(request.url.raw_path.decode())
        return httpx.Response(200, json={})

    return handler


@pytest.mark.parametrize(
    "arg",
    ["../../users/USERID", "../notifications/delete", "..", "a/../../x"],
)
def test_dot_dot_segments_are_rejected_before_any_request(arg):
    """A path argument must not retarget the request at a different endpoint.

    Commands build their path by substituting an argument into a template, and
    httpx resolves dot segments client-side. Without this check, the free
    command `holiday delete ../../users/ID` was sent as DELETE /users/ID — an
    endpoint the guard classifies as critical.
    """
    seen: list[str] = []
    with pytest.raises(click.ClickException, match=r"must not contain '\.\.'"):
        _client(_recording_handler(seen)).delete("/holidays/" + arg)
    assert seen == []


def test_percent_encoded_dots_are_not_a_traversal():
    """%2f stays encoded on the wire, so it is one segment and must pass."""
    seen: list[str] = []
    _client(_recording_handler(seen)).delete("/holidays/..%2f..%2fusers%2fU1")
    assert seen == ["/v2/holidays/..%2f..%2fusers%2fU1"]


def test_a_dot_in_an_id_is_not_a_traversal():
    seen: list[str] = []
    _client(_recording_handler(seen)).get("/documents/report.v2.pdf")
    assert seen == ["/v2/documents/report.v2.pdf"]


def test_retry_after_accepts_delta_seconds():
    assert _retry_after("5", attempt=0) == 5.0


def test_retry_after_accepts_an_http_date():
    soon = datetime.now(timezone.utc) + timedelta(seconds=30)
    assert 25.0 <= _retry_after(format_datetime(soon, usegmt=True), attempt=0) <= 31.0


def test_retry_after_falls_back_to_backoff_when_unparseable():
    assert _retry_after("soon", attempt=3) == 8.0


def test_retry_after_without_a_header_is_exponential_backoff():
    assert _retry_after(None, attempt=2) == 4.0


def test_retry_after_is_clamped_to_a_sane_range():
    past = format_datetime(datetime.now(timezone.utc) - timedelta(hours=1), usegmt=True)
    assert _retry_after(past, attempt=0) == 0.0
    assert _retry_after("99999", attempt=0) == _MAX_RETRY_WAIT


def test_429_with_an_http_date_retry_after_still_retries(monkeypatch):
    """An HTTP-date Retry-After used to raise ValueError in the middle of a retry."""
    slept: list[float] = []
    monkeypatch.setattr("pland_cli.core.client.time.sleep", slept.append)
    calls = {"n": 0}

    def handler(request):
        calls["n"] += 1
        if calls["n"] == 1:
            return httpx.Response(
                429, headers={"Retry-After": "Wed, 21 Oct 2015 07:28:00 GMT"}, json={}
            )
        return httpx.Response(200, json={"ok": True})

    assert _client(handler).get("/x") == {"ok": True}
    assert calls["n"] == 2
    assert slept == [0.0]  # the date is in the past, so no wait
