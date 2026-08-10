"""Run many spec operations from one file behind a single risk gate."""
from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

import click

from pland_cli._codegen.extract import Operation, extract_operations
from pland_cli._codegen.security import classify
from pland_cli._codegen.spec import load_spec
from pland_cli.core import guard
from pland_cli.core.client import PlandError

RISK_ORDER = {"free": 0, "confirm": 1, "critical": 2}
MARKER = {"free": "🟢", "confirm": "🟡", "critical": "🔴"}


def max_risk(risks: list[str]) -> str:
    """Highest risk level in the list; "free" for an empty list."""
    highest = "free"
    for risk in risks:
        if risk not in RISK_ORDER:
            raise ValueError(f"unknown risk level: {risk!r}")
        if RISK_ORDER[risk] > RISK_ORDER[highest]:
            highest = risk
    return highest


@dataclass
class ResolvedEntry:
    index: int
    group: str
    command: str
    method: str
    path: str
    risk: str
    data: dict | None


@lru_cache(maxsize=1)
def _operation_index() -> dict[tuple[str, str], Operation]:
    return {(op.group, op.command): op for op in extract_operations(load_spec())}


def resolve_entries(entries: list) -> list[ResolvedEntry]:
    """Resolve raw entries against the spec. Raises on the first bad entry."""
    index = _operation_index()
    resolved: list[ResolvedEntry] = []
    for i, raw in enumerate(entries):
        if not isinstance(raw, dict):
            raise click.ClickException(f"entry {i}: must be a JSON object")
        group, command = str(raw.get("group")), str(raw.get("command"))
        op = index.get((group, command))
        if op is None:
            raise click.ClickException(f"entry {i}: unknown command '{group} {command}'")
        args = raw.get("args") or []
        if not isinstance(args, list):
            raise click.ClickException(f"entry {i}: 'args' must be a JSON array")
        if len(args) != len(op.path_params):
            raise click.ClickException(
                f"entry {i}: expects {len(op.path_params)} path argument"
                f"{'s' if len(op.path_params) != 1 else ''}, got {len(args)}"
            )
        path = op.path
        for param, value in zip(op.path_params, args):
            path = path.replace("{" + param["name"] + "}", str(value))
        # GET is always read-only -> free (classify() only reasons about write ops
        # and would fall through to its confirm fail-safe for reads). Mirrors
        # _codegen/render.py:39 exactly, so classification cannot drift between
        # generated commands and batch.
        risk = "free" if op.method == "get" else classify(op.method, op.path, op.tag)
        resolved.append(ResolvedEntry(
            index=i, group=op.group, command=op.command, method=op.method,
            path=path, risk=risk, data=raw.get("data"),
        ))
    return resolved


def format_plan(entries: list[ResolvedEntry]) -> str:
    """Human-readable summary shown before the risk gate."""
    lines = [f"Plan: {len(entries)} operations"]
    counts: dict[tuple[str, str], list[ResolvedEntry]] = {}
    for entry in entries:
        counts.setdefault((entry.group, entry.command), []).append(entry)
    for (group, command), group_entries in counts.items():
        risk = group_entries[0].risk
        if group_entries[0].method == "delete":
            for entry in group_entries:
                lines.append(f"  [{entry.index}] {group} {command}  {entry.path}  {MARKER[risk]}")
        else:
            lines.append(f"  {len(group_entries):>3} x  {group} {command}  {MARKER[risk]}")
    return "\n".join(lines)


def execute(client, entries: list[ResolvedEntry]) -> tuple[int, list[dict]]:
    """Run every entry, recording failures instead of aborting.

    Runs with no per-entry risk gate: the batch is gated once, up front.
    guard.audit() still records one line per executed operation.
    """
    succeeded = 0
    failures: list[dict] = []
    for entry in entries:
        try:
            if entry.method == "get":
                client.get(entry.path)
            elif entry.method == "delete":
                client.delete(entry.path)
            else:
                getattr(client, entry.method)(entry.path, json=entry.data)
        except PlandError as exc:
            failures.append({
                "index": entry.index, "group": entry.group, "command": entry.command,
                "status": exc.status, "detail": exc.detail or exc.title,
            })
            decision = "batch_failed"
        else:
            succeeded += 1
            decision = "batch_ok"
        guard.audit({
            "method": entry.method.upper(), "path": entry.path,
            "risk": entry.risk, "decision": decision, "batch_index": entry.index,
        })
    return succeeded, failures
