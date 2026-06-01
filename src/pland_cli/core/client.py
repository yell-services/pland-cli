from __future__ import annotations

import time
from typing import Any

import httpx

from pland_cli.core.config import Config

_TIMEOUT = 120.0
_MAX_RETRIES = 5


class PlandAuthError(Exception):
    """Kein API-Key verfügbar."""


class PlandError(Exception):
    def __init__(self, status: int, title: str, detail: str, raw: dict):
        super().__init__(f"HTTP {status}: {title} — {detail}")
        self.status = status
        self.title = title
        self.detail = detail
        self.raw = raw


def _handle_response(resp: httpx.Response) -> Any:
    """Erfolg → JSON (oder Bytes bei Binär); Fehler → PlandError im pland-Format."""
    if resp.is_success:
        ctype = resp.headers.get("content-type", "")
        if "application/json" in ctype:
            return resp.json()
        return resp.content  # binär (PDF/ZIP/…)
    try:
        body = resp.json()
    except ValueError:
        raise PlandError(resp.status_code, resp.reason_phrase, resp.text[:200], {})
    errs = body.get("errors") or []
    detail = "; ".join(e.get("message", "") for e in errs) or body.get("message", "")
    raise PlandError(resp.status_code, body.get("message", resp.reason_phrase), detail, body)


def bootstrap_api_key(
    base_url: str,
    login_id: str,
    password: str,
    name: str = "pland-cli",
    *,
    transport: httpx.BaseTransport | None = None,
) -> str:
    """Loggt sich mit Login-ID/Passwort ein und erzeugt einen neuen API-Key.

    Führt ``POST /auth/login`` (→ Bearer-Token) und damit ``POST /api_key/`` aus
    und gibt den Key (``<id>:<secret>``) zurück. Die Login-ID (Nummer) und das
    Passwort werden **ausschließlich für den Login verwendet und nirgends
    gespeichert** — nur der Aufrufer entscheidet, was mit dem Key geschieht.
    """
    with httpx.Client(base_url=base_url, timeout=_TIMEOUT, transport=transport) as c:
        login = _handle_response(
            c.post(
                "/auth/login",
                json={"username": login_id, "password": password, "type": "dashboard"},
            )
        )
        token = login.get("token") if isinstance(login, dict) else None
        if not token:
            raise PlandError(500, "Login ohne Token", "Antwort enthielt kein 'token'.", {})
        auth = token if token.lower().startswith("bearer ") else f"Bearer {token}"
        created = _handle_response(
            c.post("/api_key/", json={"name": name}, headers={"Authorization": auth})
        )
        key = created.get("key") if isinstance(created, dict) else None
        if not key:
            raise PlandError(500, "Key-Erstellung fehlgeschlagen", "Antwort enthielt kein 'key'.", {})
        return key


class PlandClient:
    def __init__(self, config: Config, transport: httpx.BaseTransport | None = None):
        if not config.api_key:
            raise PlandAuthError(
                "Kein API-Key gesetzt. Setze PLAND_API_KEY oder nutze `pland auth set-key`."
            )
        self._client = httpx.Client(
            base_url=config.base_url,
            headers={"x-API-Key": config.api_key.strip()},
            timeout=_TIMEOUT,
            transport=transport,
        )

    def _request(self, method: str, path: str, **kwargs: Any) -> Any:
        resp = self._client.request(method, path, **kwargs)
        for attempt in range(_MAX_RETRIES):
            if resp.status_code != 429:
                break
            wait = float(resp.headers.get("Retry-After", 2 ** attempt))
            time.sleep(wait)
            resp = self._client.request(method, path, **kwargs)
        return self._handle(resp)

    def _handle(self, resp: httpx.Response) -> Any:
        return _handle_response(resp)

    def get(self, path: str, params: dict | None = None) -> Any:
        return self._request("GET", path, params=params)

    def post(self, path: str, json: Any = None, params: dict | None = None,
             files: dict | None = None, data: dict | None = None) -> Any:
        return self._request("POST", path, json=json, params=params, files=files, data=data)

    def patch(self, path: str, json: Any = None, params: dict | None = None) -> Any:
        return self._request("PATCH", path, json=json, params=params)

    def put(self, path: str, json: Any = None, params: dict | None = None) -> Any:
        return self._request("PUT", path, json=json, params=params)

    def delete(self, path: str, params: dict | None = None) -> Any:
        return self._request("DELETE", path, params=params)
