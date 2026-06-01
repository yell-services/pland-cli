import httpx
import pytest

from pland_cli.core.client import PlandError, bootstrap_api_key


def _transport(handler):
    return httpx.MockTransport(handler)


def test_bootstrap_logs_in_then_creates_key():
    seen = {}

    def handler(request: httpx.Request) -> httpx.Response:
        # base_url enthält /v2 → Pfad endet auf den Endpunkt, beginnt nicht damit.
        if request.url.path.endswith("/auth/login"):
            seen["login"] = request.content.decode()
            return httpx.Response(200, json={"token": "Bearer jwt-xyz"})
        if request.url.path.endswith("/api_key/"):
            seen["auth"] = request.headers.get("Authorization")
            seen["keybody"] = request.content.decode()
            return httpx.Response(201, json={"key": "12345678:abcdef"})
        return httpx.Response(404, json={})

    key = bootstrap_api_key(
        "https://api.test/v2", "4711", "pw", name="pland-cli", transport=_transport(handler)
    )
    assert key == "12345678:abcdef"
    # Login geht mit ID/Nummer im username-Feld, nicht mit E-Mail.
    assert '"username":"4711"' in seen["login"]
    # Bearer-Token korrekt weitergereicht (Prefix nicht verdoppelt).
    assert seen["auth"] == "Bearer jwt-xyz"
    # Credentials gehen NUR an /auth/login, niemals an /api_key/.
    assert "pw" not in seen["keybody"]
    assert "4711" not in seen["keybody"]
    assert '"name"' in seen["keybody"]


def test_bootstrap_adds_bearer_prefix_when_missing():
    seen = {}

    def handler(request):
        if request.url.path.endswith("/auth/login"):
            return httpx.Response(200, json={"token": "rawjwt"})
        seen["auth"] = request.headers.get("Authorization")
        return httpx.Response(201, json={"key": "k:s"})

    bootstrap_api_key("https://api.test/v2", "4711", "b", transport=_transport(handler))
    assert seen["auth"] == "Bearer rawjwt"


def test_bootstrap_invalid_credentials_raises():
    def handler(request):
        return httpx.Response(401, json={"message": "Invalid credentials"})

    with pytest.raises(PlandError) as exc:
        bootstrap_api_key("https://api.test/v2", "4711", "b", transport=_transport(handler))
    assert exc.value.status == 401


def test_bootstrap_missing_token_raises():
    def handler(request):
        return httpx.Response(200, json={"somethingElse": True})

    with pytest.raises(PlandError):
        bootstrap_api_key("https://api.test/v2", "4711", "b", transport=_transport(handler))


def test_bootstrap_missing_key_in_response_raises():
    def handler(request):
        if request.url.path.endswith("/auth/login"):
            return httpx.Response(200, json={"token": "Bearer t"})
        return httpx.Response(201, json={"noKeyHere": True})

    with pytest.raises(PlandError):
        bootstrap_api_key("https://api.test/v2", "4711", "b", transport=_transport(handler))
