# tests/test_guard_draft.py
import pytest

from pland_cli.core import guard


def _run(monkeypatch, tmp_path, lookup, confirmer):
    monkeypatch.setattr(guard, "_audit_path", lambda: tmp_path / "a.jsonl")
    guard.enforce(method="delete", path="/invoices/1", risk="confirm",
                  draftable="Invoice", assume_yes=False, lookup=lookup,
                  isatty=lambda: True, confirmer=confirmer,
                  tokener=lambda p: "")


def test_draft_invoice_runs_without_confirm(monkeypatch, tmp_path):
    _run(monkeypatch, tmp_path, lookup=lambda: {"_id": "1"},  # kein fixDate -> Entwurf
         confirmer=lambda p: pytest.fail("Entwurf darf nicht nachfragen"))


def test_fixed_invoice_requires_confirm(monkeypatch, tmp_path):
    called = {"n": 0}

    def conf(p):
        called["n"] += 1
        return True

    _run(monkeypatch, tmp_path, lookup=lambda: {"_id": "1", "fixDate": 123}, confirmer=conf)
    assert called["n"] == 1


def test_lookup_failure_falls_back_to_confirm(monkeypatch, tmp_path):
    called = {"n": 0}

    def conf(p):
        called["n"] += 1
        return True

    def boom():
        raise RuntimeError("net")

    _run(monkeypatch, tmp_path, lookup=boom, confirmer=conf)
    assert called["n"] == 1


def test_empty_lookup_result_stays_confirm(monkeypatch, tmp_path):
    # fail-safe: ein leeres dict ({}) hat kein fixDate, darf aber NICHT als
    # Entwurf (free) durchgehen — sonst fail-open bei unerwarteter API-Antwort.
    called = {"n": 0}

    def conf(p):
        called["n"] += 1
        return True

    _run(monkeypatch, tmp_path, lookup=lambda: {}, confirmer=conf)
    assert called["n"] == 1


def test_object_without_id_stays_confirm(monkeypatch, tmp_path):
    # Ein dict ohne _id ist kein erkanntes Entwurf-Objekt -> fail-safe confirm.
    called = {"n": 0}

    def conf(p):
        called["n"] += 1
        return True

    _run(monkeypatch, tmp_path, lookup=lambda: {"foo": "bar"}, confirmer=conf)
    assert called["n"] == 1
