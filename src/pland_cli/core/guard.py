"""Runtime guard layer for write operations.

`enforce()` applies the risk tier (confirmation, fail-closed); `audit()`
writes an append-only trail. See spec 2026-06-01-...-destructive-guard.
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path
from typing import Any, Callable

import click


def _audit_path() -> Path:
    override = os.environ.get("PLAND_AUDIT_LOG")
    if override:
        return Path(override)
    if os.name == "nt":
        base = os.environ.get("LOCALAPPDATA") or str(Path.home())
        return Path(base) / "pland" / "audit.jsonl"
    base = os.environ.get("XDG_STATE_HOME") or str(Path.home() / ".local" / "state")
    return Path(base) / "pland" / "audit.jsonl"


def audit(entry: dict[str, Any]) -> None:
    """Append an entry to the audit log, best effort. Never raises."""
    try:
        rec = {"ts": int(time.time()), **entry}
        path = _audit_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    except Exception:
        pass


def _is_id_segment(seg: str) -> bool:
    """True when the segment looks like an object ID (placeholder, number, opaque ID)."""
    if seg.startswith("{"):
        return True
    if seg.isdigit():
        return True
    # Mongo/hex-like or long opaque IDs (>=12 chars, not actual words)
    if len(seg) >= 12 and all(c in "0123456789abcdefABCDEF-" for c in seg):
        return True
    return False


def _resource_token(path: str) -> str:
    """Confirmation token for 🔴: the resource name, i.e. the segment before the ID."""
    parts = [s for s in path.strip("/").split("/") if s]
    # Drop trailing ID segments -> the resource name remains.
    while parts and _is_id_segment(parts[-1]):
        parts.pop()
    return parts[-1] if parts else "confirm"


def _abort(method: str, path: str, risk: str, decision: str, msg: str) -> None:
    audit({"method": method.upper(), "path": path, "risk": risk, "decision": decision})
    click.echo(msg, err=True)
    raise SystemExit(2)


def enforce(
    *,
    method: str,
    path: str,
    risk: str,
    draftable: str | None = None,
    assume_yes: bool = False,
    lookup: Callable[[], dict] | None = None,
    isatty: Callable[[], bool] | None = None,
    confirmer: Callable[[str], bool] | None = None,
    tokener: Callable[[str], str] | None = None,
) -> None:
    """Enforce the risk tier. Returning means the call may proceed;
    raising SystemExit(2) means aborted or blocked."""
    isatty = isatty or sys.stdin.isatty
    # Prompts go to stderr: with --json, stdout carries the result object, and a
    # confirmation written there would make it unparseable for the caller.
    confirmer = confirmer or (lambda prompt: click.confirm(prompt, default=False, err=True))
    tokener = tokener or (
        lambda prompt: click.prompt(prompt, default="", show_default=False, err=True)
    )

    # Zustandsabhaengig: draftfaehige DELETE -> NUR bei einem echten Entwurf-Objekt
    # auf free herabstufen. Ein leeres/unerwartetes Lookup-Ergebnis ({}, Liste,
    # error) deliberately stays confirm (fail-safe) — the downgrade must not
    # hinge on an unverified API response shape.
    if draftable and lookup is not None:
        try:
            obj = lookup()
            if isinstance(obj, dict) and obj.get("_id") and not obj.get("fixDate"):
                risk = "free"
        except Exception:
            pass  # fail-safe: stays confirm

    if risk == "free":
        audit({"method": method.upper(), "path": path, "risk": "free", "decision": "auto"})
        return

    label = f"{method.upper()} {path}"

    if risk == "critical":
        if not isatty():
            _abort(method, path, risk, "blocked_no_tty",
                   f"🔴 Critical operation {label} needs confirmation at the terminal "
                   f"(no interactive TTY). No flag can bypass this.")
        token = _resource_token(path)
        entered = tokener(f"🔴 CRITICAL: {label}. Type '{token}' to confirm")
        if (entered or "").strip() != token:
            _abort(method, path, risk, "aborted", "Aborted (token did not match).")
        audit({"method": method.upper(), "path": path, "risk": "critical",
               "decision": "critical_confirmed"})
        return

    # confirm
    if assume_yes:
        audit({"method": method.upper(), "path": path, "risk": "confirm", "decision": "override"})
        return
    if not isatty():
        _abort(method, path, risk, "blocked_no_tty",
               f"🟡 {label} is protected and needs confirmation. No interactive "
               f"TTY — release it deliberately with --yes.")
    if confirmer(f"🟡 Run {label}?"):
        audit({"method": method.upper(), "path": path, "risk": "confirm", "decision": "confirmed"})
        return
    _abort(method, path, risk, "aborted", "Aborted.")
