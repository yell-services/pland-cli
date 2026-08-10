from __future__ import annotations

import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Any

import click
import httpx

from pland_cli.core.config import Config

_TIMEOUT = 120.0
_MAX_RETRIES = 5
# A server may ask for any delay it likes; a CLI that sleeps for an hour looks hung.
_MAX_RETRY_WAIT = 60.0


class PlandAuthError(Exception):
    """No API key available."""


class PlandError(Exception):
    def __init__(self, status: int, title: str, detail: str, raw: dict):
        super().__init__(f"HTTP {status}: {title} — {detail}")
        self.status = status
        self.title = title
        self.detail = detail
        self.raw = raw


def _handle_response(resp: httpx.Response) -> Any:
    """Success → JSON (or bytes for binary); failure → PlandError in pland's format."""
    if resp.is_success:
        ctype = resp.headers.get("content-type", "")
        if "application/json" in ctype:
            return resp.json()
        return resp.content  # binary (PDF/ZIP/…)
    try:
        body = resp.json()
    except ValueError:
        raise PlandError(resp.status_code, resp.reason_phrase, resp.text[:200], {})
    errs = body.get("errors") or []
    detail = "; ".join(e.get("message", "") for e in errs) or body.get("message", "")
    raise PlandError(resp.status_code, body.get("message", resp.reason_phrase), detail, body)


def _retry_after(value: str | None, attempt: int) -> float:
    """Seconds to wait before retrying a 429, clamped to [0, _MAX_RETRY_WAIT].

    RFC 7231 allows either delta-seconds or an HTTP-date. Anything unparseable
    falls back to exponential backoff rather than raising in the middle of a
    retry, which used to turn a rate limit into a traceback.
    """
    wait = float(2 ** attempt)
    if value:
        try:
            wait = float(value)
        except ValueError:
            try:
                when: datetime | None = parsedate_to_datetime(value)
            except (TypeError, ValueError):
                when = None
            if when is not None:
                if when.tzinfo is None:
                    when = when.replace(tzinfo=timezone.utc)
                wait = (when - datetime.now(timezone.utc)).total_seconds()
    return min(max(wait, 0.0), _MAX_RETRY_WAIT)


def bootstrap_api_key(
    base_url: str,
    login_id: str,
    password: str,
    name: str = "pland-cli",
    *,
    transport: httpx.BaseTransport | None = None,
) -> str:
    """Log in with login ID and password, then create a new API key.

    Runs ``POST /auth/login`` (→ bearer token) and with it ``POST /api_key/``,
    returning the key as ``<id>:<secret>``. The login ID (a number) and the
    password are **used for the login only and never
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
            raise PlandError(500, "Login returned no token", "Response contained no 'token'.", {})
        auth = token if token.lower().startswith("bearer ") else f"Bearer {token}"
        created = _handle_response(
            c.post("/api_key/", json={"name": name}, headers={"Authorization": auth})
        )
        key = created.get("key") if isinstance(created, dict) else None
        if not key:
            raise PlandError(500, "Key creation failed", "Response contained no 'key'.", {})
        return key


class PlandClient:
    def __init__(self, config: Config, transport: httpx.BaseTransport | None = None):
        if not config.api_key:
            raise PlandAuthError(
                "No API key set. Set PLAND_API_KEY or run `pland auth set-key`."
            )
        self._client = httpx.Client(
            base_url=config.base_url,
            headers={"x-API-Key": config.api_key.strip()},
            timeout=_TIMEOUT,
            transport=transport,
        )

    def _request(self, method: str, path: str, **kwargs: Any) -> Any:
        # A command builds its path by substituting an argument into a template
        # ("/holidays/" + id). httpx resolves dot segments client-side, so an
        # argument like "../../users/ID" would retarget the request at a
        # different — and possibly higher-risk — endpoint than the one
        # guard.enforce classified. One check here covers every caller.
        if ".." in path.split("/"):
            raise click.ClickException(
                f"Request path must not contain '..' segments: {path!r}"
            )
        resp = self._client.request(method, path, **kwargs)
        for attempt in range(_MAX_RETRIES):
            if resp.status_code != 429:
                break
            time.sleep(_retry_after(resp.headers.get("Retry-After"), attempt))
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
