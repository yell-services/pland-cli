# tests/test_guard.py
import json

import click
import pytest

from pland_cli.core import guard


def test_audit_appends_jsonl(tmp_path, monkeypatch):
    log = tmp_path / "audit.jsonl"
    monkeypatch.setattr(guard, "_audit_path", lambda: log)
    guard.audit({"method": "DELETE", "path": "/x/1", "risk": "confirm", "decision": "confirmed"})
    guard.audit({"method": "DELETE", "path": "/x/2", "risk": "critical", "decision": "aborted"})
    lines = log.read_text().splitlines()
    assert len(lines) == 2
    rec = json.loads(lines[0])
    assert rec["method"] == "DELETE" and rec["decision"] == "confirmed"
    assert "ts" in rec


def test_audit_never_raises(monkeypatch):
    # Selbst wenn der Pfad nicht schreibbar ist, darf audit() nie werfen.
    monkeypatch.setattr(guard, "_audit_path", lambda: (_ for _ in ()).throw(OSError("boom")))
    guard.audit({"x": 1})  # darf nicht werfen


def _enforce(monkeypatch, tmp_path, **kw):
    monkeypatch.setattr(guard, "_audit_path", lambda: tmp_path / "a.jsonl")
    defaults = dict(method="delete", path="/documents/1", risk="confirm",
                    draftable=None, assume_yes=False, lookup=None,
                    isatty=lambda: True, confirmer=lambda prompt: True,
                    tokener=lambda prompt: "")
    defaults.update(kw)
    return guard.enforce(**defaults)


def test_free_runs_through(monkeypatch, tmp_path):
    _enforce(monkeypatch, tmp_path, risk="free")  # kein Abbruch


def test_confirm_yes_flag_overrides(monkeypatch, tmp_path):
    _enforce(monkeypatch, tmp_path, risk="confirm", assume_yes=True,
             confirmer=lambda p: pytest.fail("darf nicht fragen"))


def test_confirm_tty_accepts(monkeypatch, tmp_path):
    _enforce(monkeypatch, tmp_path, risk="confirm", confirmer=lambda p: True)


def test_confirm_tty_declined_aborts(monkeypatch, tmp_path):
    with pytest.raises((click.Abort, SystemExit)):
        _enforce(monkeypatch, tmp_path, risk="confirm", confirmer=lambda p: False)


def test_confirm_no_tty_blocks(monkeypatch, tmp_path):
    with pytest.raises((click.Abort, SystemExit)):
        _enforce(monkeypatch, tmp_path, risk="confirm", isatty=lambda: False)


def test_critical_requires_correct_token(monkeypatch, tmp_path):
    # falscher Token -> Abbruch
    with pytest.raises((click.Abort, SystemExit)):
        _enforce(monkeypatch, tmp_path, risk="critical", method="delete",
                 path="/salaries/1", tokener=lambda p: "falsch")


def test_critical_yes_flag_does_not_bypass(monkeypatch, tmp_path):
    with pytest.raises((click.Abort, SystemExit)):
        _enforce(monkeypatch, tmp_path, risk="critical", assume_yes=True,
                 isatty=lambda: False)


def test_critical_correct_token_runs(monkeypatch, tmp_path):
    # Token = letztes Pfadsegment-Eltern ("salaries") — siehe Implementierung
    _enforce(monkeypatch, tmp_path, risk="critical", path="/salaries/1",
             tokener=lambda p: "salaries")
