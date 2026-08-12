"""Run many spec operations from one file behind a single risk gate."""
from __future__ import annotations

import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import click
import httpx

from pland_cli._codegen.extract import Operation, extract_operations
from pland_cli._codegen.security import classify
from pland_cli._codegen.spec import load_spec
from pland_cli.core import guard
from pland_cli.core.client import PlandError
from pland_cli.enrichment.registry import enrich, get_client
from pland_cli.utils import output as out_mod

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
        # A missing key and an explicit null both mean "no path arguments";
        # anything else that is not a list is an error, including falsy values.
        args = raw.get("args")
        if args is None:
            args = []
        if not isinstance(args, list):
            raise click.ClickException(f"entry {i}: 'args' must be a JSON array")
        if len(args) != len(op.path_params):
            raise click.ClickException(
                f"entry {i}: expects {len(op.path_params)} path argument"
                f"{'s' if len(op.path_params) != 1 else ''}, got {len(args)}"
            )
        path = op.path
        for param, value in zip(op.path_params, args):
            # A path argument is a single URL segment. Letting one carry '/'
            # would let it walk to another endpoint (httpx normalises '..'
            # client-side), so the gate would classify a request that is never
            # the one actually sent.
            if "/" in str(value):
                raise click.ClickException(
                    f"entry {i}: path argument {value!r} must not contain '/'")
            path = path.replace("{" + param["name"] + "}", str(value))
        # An entry carries only group/command/args/data, so an operation whose
        # query parameters are mandatory can never be expressed completely.
        # Sending it anyway would let the server decide what the missing half
        # meant, so refuse it for every method — GET included.
        required_qp = [p["name"] for p in op.query_params if p.get("required")]
        if required_qp:
            raise click.ClickException(
                f"entry {i}: '{op.group} {op.command}' requires query parameters {required_qp}, "
                f"which a batch entry cannot express — run it individually"
            )
        # GET is always read-only -> free (classify() only reasons about write ops
        # and would fall through to its confirm fail-safe for reads). Mirrors
        # _codegen/render.py:39 exactly, so classification cannot drift between
        # generated commands and batch.
        risk = "free" if op.method == "get" else classify(op.method, op.path, op.tag)
        data = raw.get("data")
        if data is not None and not isinstance(data, dict):
            raise click.ClickException(f"entry {i}: 'data' must be a JSON object")
        resolved.append(ResolvedEntry(
            index=i, group=op.group, command=op.command, method=op.method,
            path=path, risk=risk, data=data,
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
        except (PlandError, httpx.HTTPError) as exc:
            failures.append({
                "index": entry.index, "group": entry.group, "command": entry.command,
                "status": getattr(exc, "status", 0),
                "detail": getattr(exc, "detail", None) or str(exc),
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


def _gate_token(entries: list[ResolvedEntry], risk: str) -> str | None:
    """The token the real run will ask for, so --dry-run can name it."""
    if risk == "free":
        return None
    gate = next(e for e in entries if e.risk == risk)
    return guard._resource_token(gate.path)


@enrich("batch", "run", new=True)
@click.command()
@click.option("--file", "file_", required=True, type=click.Path(exists=True, dir_okay=False),
              help="JSON file holding an array of operations.")
@click.option("--dry-run", is_flag=True, help="Print the plan and exit without asking.")
@click.option("--yes", "assume_yes", is_flag=True,
              help="Skip a 🟡 confirmation. Has no effect on 🔴.")
@click.option("--confirm", "confirm_token", metavar="TOKEN",
              help="Pass the confirmation token instead of typing it at a terminal. "
                   "For a caller without a TTY that has the user's explicit go; the "
                   "token still has to match. --dry-run prints the one to use.")
@click.pass_context
def batch_run(ctx: click.Context, file_: str, dry_run: bool, assume_yes: bool,
              confirm_token: str | None) -> None:
    """Run many operations from a file behind a single risk gate."""
    out_mod.set_json(ctx.obj.get("as_json", False))
    try:
        raw = json.loads(Path(file_).read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise click.ClickException(f"{file_} is not valid JSON: {exc}") from exc
    if not isinstance(raw, list):
        raise click.ClickException(f"{file_} must hold a JSON array of operations")

    entries = resolve_entries(raw)
    risk = max_risk([e.risk for e in entries])
    # The plan is always shown before the gate, but it must not pollute the
    # machine-readable stream: under --json it goes to stderr.
    click.echo(format_plan(entries), err=out_mod.USE_JSON)
    if dry_run:
        if out_mod.USE_JSON:
            out_mod.out({"operations": len(entries), "risk": risk,
                         "confirmToken": _gate_token(entries, risk)})
        else:
            token = _gate_token(entries, risk)
            if token:
                click.echo(f"Run it with: --confirm {token}")
        return

    if risk != "free":
        # Gate on the actual riskiest operation, so prompt label and audit line
        # name a real request rather than a synthetic one.
        gate = next(e for e in entries if e.risk == risk)
        guard.enforce(method=gate.method, path=gate.path, risk=risk,
                      draftable=None, assume_yes=assume_yes,
                      confirm_token=confirm_token)

    succeeded, failures = execute(get_client(ctx), entries)
    if out_mod.USE_JSON:
        out_mod.out({"succeeded": succeeded, "failed": len(failures), "failures": failures})
    else:
        click.echo(f"Done: {succeeded} succeeded, {len(failures)} failed")
        for failure in failures:
            # status 0 is execute()'s sentinel for "never got an HTTP response".
            status = failure["status"] or "no response"
            click.echo(f"  [{failure['index']}] {failure['group']} {failure['command']}"
                       f"  {status}  {failure['detail']}")
    if failures:
        ctx.exit(1)
