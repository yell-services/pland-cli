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
    _run(monkeypatch, tmp_path, lookup=lambda: {"_id": "1"},  # no fixDate -> draft
         confirmer=lambda p: pytest.fail("a draft must not prompt"))


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
    # fail-safe: an empty dict ({}) has no fixDate but must NOT pass as a draft
    # (free) — that would fail open on an unexpected API response.
    called = {"n": 0}

    def conf(p):
        called["n"] += 1
        return True

    _run(monkeypatch, tmp_path, lookup=lambda: {}, confirmer=conf)
    assert called["n"] == 1


def test_object_without_id_stays_confirm(monkeypatch, tmp_path):
    # A dict without _id is not a recognised draft object -> fail-safe confirm.
    called = {"n": 0}

    def conf(p):
        called["n"] += 1
        return True

    _run(monkeypatch, tmp_path, lookup=lambda: {"foo": "bar"}, confirmer=conf)
    assert called["n"] == 1
