"""Laufzeit-Schutzlayer fuer schreibende Operationen.

`enforce()` setzt die Risiko-Stufe durch (Bestaetigung/fail-closed); `audit()`
schreibt eine Append-only-Spur. Siehe Spec 2026-06-01-...-destructive-guard.
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
    """Haengt einen Eintrag (best effort) ans Audit-Log. Wirft nie."""
    try:
        rec = {"ts": int(time.time()), **entry}
        path = _audit_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
    except Exception:
        pass


def _is_id_segment(seg: str) -> bool:
    """True, wenn das Segment wie eine Objekt-ID aussieht (Platzhalter/Zahl/Opaque-ID)."""
    if seg.startswith("{"):
        return True
    if seg.isdigit():
        return True
    # Mongo-/Hex-aehnliche oder lange opake IDs (>=12 Zeichen, keine echten Worte)
    if len(seg) >= 12 and all(c in "0123456789abcdefABCDEF-" for c in seg):
        return True
    return False


def _resource_token(path: str) -> str:
    """Bestaetigungs-Token fuer 🔴: der Ressourcenname (Segment vor der ID)."""
    parts = [s for s in path.strip("/").split("/") if s]
    # Trailing ID-Segment(e) wegwerfen -> der Ressourcenname bleibt.
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
    """Setzt die Risiko-Stufe durch. Kehrt zurueck = darf ausgefuehrt werden;
    wirft SystemExit(2) = abgebrochen/blockiert."""
    isatty = isatty or sys.stdin.isatty
    confirmer = confirmer or (lambda prompt: click.confirm(prompt, default=False))
    tokener = tokener or (lambda prompt: click.prompt(prompt, default="", show_default=False))

    # Zustandsabhaengig: draftfaehige DELETE -> NUR bei einem echten Entwurf-Objekt
    # auf free herabstufen. Ein leeres/unerwartetes Lookup-Ergebnis ({}, Liste,
    # Fehler) bleibt bewusst confirm (fail-safe) — die Herabstufung darf nicht an
    # einer ungeprueften API-Antwortform haengen.
    if draftable and lookup is not None:
        try:
            obj = lookup()
            if isinstance(obj, dict) and obj.get("_id") and not obj.get("fixDate"):
                risk = "free"
        except Exception:
            pass  # fail-safe: bleibt confirm

    if risk == "free":
        audit({"method": method.upper(), "path": path, "risk": "free", "decision": "auto"})
        return

    label = f"{method.upper()} {path}"

    if risk == "critical":
        if not isatty():
            _abort(method, path, risk, "blocked_no_tty",
                   f"🔴 Kritische Operation {label} braucht eine Bestaetigung am Terminal "
                   f"(kein interaktives TTY). Kein Flag-Bypass moeglich.")
        token = _resource_token(path)
        entered = tokener(f"🔴 KRITISCH: {label}. Tippe '{token}' zur Bestaetigung")
        if (entered or "").strip() != token:
            _abort(method, path, risk, "aborted", "Abgebrochen (Token stimmt nicht).")
        audit({"method": method.upper(), "path": path, "risk": "critical",
               "decision": "critical_confirmed"})
        return

    # confirm
    if assume_yes:
        audit({"method": method.upper(), "path": path, "risk": "confirm", "decision": "override"})
        return
    if not isatty():
        _abort(method, path, risk, "blocked_no_tty",
               f"🟡 {label} ist geschuetzt und braucht eine Bestaetigung. Kein interaktives "
               f"TTY — mit --yes bewusst freigeben.")
    if confirmer(f"🟡 {label} ausfuehren?"):
        audit({"method": method.upper(), "path": path, "risk": "confirm", "decision": "confirmed"})
        return
    _abort(method, path, risk, "aborted", "Abgebrochen.")
