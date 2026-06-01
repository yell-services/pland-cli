import httpx
import pytest

from pland_cli.core.client import PlandClient, PlandError, PlandAuthError
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
