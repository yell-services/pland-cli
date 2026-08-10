import json
import re
from pathlib import Path

import click
import httpx
import pytest
from click.testing import CliRunner

import pland_cli.commands as commands_pkg
from pland_cli.cli import main
from pland_cli.core.client import PlandError
from pland_cli.enrichment.batch import (
    ResolvedEntry,
    _operation_index,
    execute,
    format_plan,
    max_risk,
    resolve_entries,
)


def test_max_risk_of_empty_list_is_free():
    assert max_risk([]) == "free"


def test_max_risk_picks_highest():
    assert max_risk(["free", "free"]) == "free"
    assert max_risk(["free", "confirm"]) == "confirm"
    assert max_risk(["confirm", "critical", "free"]) == "critical"


def test_max_risk_rejects_unknown_level():
    with pytest.raises(ValueError, match="unknown risk level"):
        max_risk(["free", "nonsense"])


def test_resolve_fills_method_path_and_risk():
    resolved = resolve_entries([
        {"group": "salary", "command": "release-using-time-tracking",
         "data": {"timeTrackingId": "t1"}},
    ])
    assert len(resolved) == 1
    entry = resolved[0]
    assert entry.index == 0
    assert entry.method == "post"
    assert entry.path == "/salaries/releaseWithTimeTracking"
    assert entry.risk == "critical"
    assert entry.data == {"timeTrackingId": "t1"}


def test_resolve_substitutes_path_params_in_order():
    resolved = resolve_entries([
        {"group": "jobs", "command": "view", "args": ["abc123"]},
    ])
    assert resolved[0].path == "/jobs/abc123"
    assert resolved[0].method == "get"
    assert resolved[0].risk == "free"


def test_resolve_rejects_unknown_command():
    with pytest.raises(click.ClickException, match="entry 0: unknown command 'salary nope'"):
        resolve_entries([{"group": "salary", "command": "nope"}])


def test_resolve_rejects_wrong_arg_count():
    with pytest.raises(click.ClickException, match="entry 1: expects 1 path argument, got 0"):
        resolve_entries([
            {"group": "jobs", "command": "view", "args": ["ok"]},
            {"group": "jobs", "command": "view"},
        ])


def test_resolve_rejects_non_object_entry():
    with pytest.raises(click.ClickException, match="entry 0: must be a JSON object"):
        resolve_entries(["oops"])


def test_resolve_rejects_non_list_args():
    with pytest.raises(click.ClickException, match="entry 0: 'args' must be a JSON array"):
        resolve_entries([{"group": "jobs", "command": "view", "args": 42}])


def test_resolve_rejects_dict_args():
    with pytest.raises(click.ClickException, match="entry 0: 'args' must be a JSON array"):
        resolve_entries([{"group": "jobs", "command": "view", "args": {"jobId": "abc"}}])


def test_runtime_risk_matches_generated_risk():
    """batch classifies at run time; the generator baked risk into the source.

    If these ever disagree, a single gate would understate what a batch does.
    """
    generated: dict[tuple[str, str], str] = {}
    for source in Path(commands_pkg.__path__[0]).glob("*.py"):
        text = source.read_text()
        for match in re.finditer(
            r'def _cmd_([a-z0-9_]+)\(.*?risk="([a-z]+)"', text, re.DOTALL
        ):
            generated["_cmd_" + match.group(1)] = match.group(2)

    checked = 0
    for (group, command), op in _operation_index().items():
        func = "_cmd_" + f"{group}_{command}".replace("-", "_")
        if func not in generated:
            continue
        entry = {"group": group, "command": command, "args": ["x"] * len(op.path_params)}
        expected = resolve_entries([entry])[0].risk
        assert generated[func] == expected, f"{group} {command}"
        checked += 1
    assert checked > 300, f"only {checked} commands compared, expected the full surface"


def _entry(i, group, command, method, path, risk):
    return ResolvedEntry(index=i, group=group, command=command, method=method,
                         path=path, risk=risk, data=None)


def test_plan_groups_and_counts():
    plan = format_plan([
        _entry(0, "salary", "release-using-time-tracking", "post", "/salaries/releaseWithTimeTracking", "critical"),
        _entry(1, "salary", "release-using-time-tracking", "post", "/salaries/releaseWithTimeTracking", "critical"),
        _entry(2, "jobs", "create", "post", "/jobs/v2", "free"),
    ])
    assert "Plan: 3 operations" in plan
    # Pin the exact rendered line: marker bound to its own operation
    assert "    2 x  salary release-using-time-tracking  🔴" in plan
    assert "    1 x  jobs create  🟢" in plan


def test_plan_lists_deletes_individually():
    plan = format_plan([
        _entry(0, "jobs", "delete", "delete", "/jobs/a1", "confirm"),
        _entry(1, "jobs", "delete", "delete", "/jobs/b2", "confirm"),
    ])
    # Pin the exact rendered lines: marker bound to each deletion
    assert "  [0] jobs delete  /jobs/a1  🟡" in plan
    assert "  [1] jobs delete  /jobs/b2  🟡" in plan
    # Ensure deletions are listed individually, not aggregated
    assert "2 x" not in plan


def test_plan_preserves_first_appearance_ordering():
    """Verify that groups appear in first-appearance order, not sorted."""
    plan = format_plan([
        _entry(0, "salary", "release-using-time-tracking", "post", "/salaries/releaseWithTimeTracking", "critical"),
        _entry(1, "jobs", "create", "post", "/jobs/v2", "free"),
        _entry(2, "salary", "release-using-time-tracking", "post", "/salaries/releaseWithTimeTracking", "critical"),
    ])
    # Pin the exact lines with their markers
    salary_line = "    2 x  salary release-using-time-tracking  🔴"
    jobs_line = "    1 x  jobs create  🟢"
    assert salary_line in plan
    assert jobs_line in plan
    # Verify salary appears before jobs (first-appearance order)
    assert plan.index(salary_line) < plan.index(jobs_line)


class _FakeClient:
    def __init__(self, fail_on: set[str] | None = None, timeout_on: set[str] | None = None):
        self.calls: list[tuple[str, str, dict | None]] = []
        self.fail_on = fail_on or set()
        self.timeout_on = timeout_on or set()

    def _maybe_fail(self, path):
        if path in self.timeout_on:
            raise httpx.ReadTimeout("timed out")
        if path in self.fail_on:
            raise PlandError(409, "Conflict", "already exists", {})

    def post(self, path, json=None, params=None, files=None, data=None):
        self.calls.append(("post", path, json))
        self._maybe_fail(path)
        return {"_id": "new"}

    def get(self, path, params=None):
        self.calls.append(("get", path, None))
        self._maybe_fail(path)
        return {}


def test_execute_calls_every_entry_in_order(monkeypatch, tmp_path):
    monkeypatch.setattr("pland_cli.core.guard._audit_path", lambda: tmp_path / "a.jsonl")
    client = _FakeClient()
    entries = [
        _entry(0, "jobs", "create", "post", "/jobs/v2", "free"),
        _entry(1, "jobs", "view", "get", "/jobs/x1", "free"),
    ]
    entries[0].data = {"a": 1}
    ok, failures = execute(client, entries)
    assert ok == 2 and failures == []
    assert client.calls == [("post", "/jobs/v2", {"a": 1}), ("get", "/jobs/x1", None)]


def test_execute_continues_past_a_failure(monkeypatch, tmp_path):
    monkeypatch.setattr("pland_cli.core.guard._audit_path", lambda: tmp_path / "a.jsonl")
    client = _FakeClient(fail_on={"/jobs/bad"})
    entries = [
        _entry(0, "jobs", "view", "get", "/jobs/ok1", "free"),
        _entry(1, "jobs", "view", "get", "/jobs/bad", "free"),
        _entry(2, "jobs", "view", "get", "/jobs/ok2", "free"),
    ]
    ok, failures = execute(client, entries)
    assert ok == 2
    assert [f["index"] for f in failures] == [1]
    assert failures[0]["status"] == 409
    assert [c[1] for c in client.calls] == ["/jobs/ok1", "/jobs/bad", "/jobs/ok2"]


def test_execute_audits_one_line_per_executed_entry(monkeypatch, tmp_path):
    log = tmp_path / "a.jsonl"
    monkeypatch.setattr("pland_cli.core.guard._audit_path", lambda: log)
    client = _FakeClient(fail_on={"/jobs/bad"})
    execute(client, [
        _entry(0, "jobs", "view", "get", "/jobs/ok1", "free"),
        _entry(1, "jobs", "view", "get", "/jobs/bad", "free"),
    ])
    lines = log.read_text().splitlines()
    assert len(lines) == 2
    assert json.loads(lines[0])["decision"] == "batch_ok"
    assert json.loads(lines[1])["decision"] == "batch_failed"


def test_execute_continues_past_a_transport_error(monkeypatch, tmp_path):
    log = tmp_path / "a.jsonl"
    monkeypatch.setattr("pland_cli.core.guard._audit_path", lambda: log)
    client = _FakeClient(timeout_on={"/jobs/bad"})
    entries = [
        _entry(0, "jobs", "view", "get", "/jobs/ok1", "free"),
        _entry(1, "jobs", "view", "get", "/jobs/bad", "free"),
        _entry(2, "jobs", "view", "get", "/jobs/ok2", "free"),
    ]
    ok, failures = execute(client, entries)
    assert ok == 2
    assert [f["index"] for f in failures] == [1]
    assert [c[1] for c in client.calls] == ["/jobs/ok1", "/jobs/bad", "/jobs/ok2"]
    lines = log.read_text().splitlines()
    assert len(lines) == 3
    assert json.loads(lines[1])["decision"] == "batch_failed"


def _write(tmp_path, entries):
    path = tmp_path / "ops.json"
    path.write_text(json.dumps(entries))
    return str(path)


def test_dry_run_prints_plan_and_never_prompts(tmp_path):
    file = _write(tmp_path, [
        {"group": "salary", "command": "release-using-time-tracking", "data": {"timeTrackingId": "t"}},
    ])
    result = CliRunner().invoke(main, ["batch", "run", "--file", file, "--dry-run"])
    assert result.exit_code == 0
    assert "1 operations" in result.output
    assert "salary release-using-time-tracking" in result.output


def test_json_dry_run_keeps_stdout_parseable(tmp_path):
    """--json must not have the human plan corrupt the machine-readable stream."""
    file = _write(tmp_path, [
        {"group": "salary", "command": "release-using-time-tracking", "data": {"timeTrackingId": "t"}},
    ])
    result = CliRunner().invoke(main, ["--json", "batch", "run", "--file", file, "--dry-run"])
    assert result.exit_code == 0
    assert json.loads(result.stdout) == {"operations": 1, "risk": "critical"}
    # The human still sees the plan before any gate — on stderr, out of the way.
    assert "salary release-using-time-tracking" in result.stderr


def test_free_only_batch_does_not_prompt(tmp_path, monkeypatch):
    monkeypatch.setattr("pland_cli.core.guard._audit_path", lambda: tmp_path / "a.jsonl")
    client = _FakeClient()
    import pland_cli.enrichment.batch as batch_mod
    monkeypatch.setattr(batch_mod, "get_client", lambda ctx: client)
    file = _write(tmp_path, [{"group": "jobs", "command": "view", "args": ["x1"]}])
    result = CliRunner().invoke(main, ["batch", "run", "--file", file])
    assert result.exit_code == 0
    assert client.calls == [("get", "/jobs/x1", None)]


def test_critical_batch_requires_the_token(tmp_path, monkeypatch):
    monkeypatch.setattr("pland_cli.core.guard._audit_path", lambda: tmp_path / "a.jsonl")
    client = _FakeClient()
    import pland_cli.enrichment.batch as batch_mod
    monkeypatch.setattr(batch_mod, "get_client", lambda ctx: client)
    file = _write(tmp_path, [
        {"group": "salary", "command": "release-using-time-tracking", "data": {"timeTrackingId": "t"}},
    ])
    # No TTY under CliRunner: fail-closed, and nothing is sent.
    result = CliRunner().invoke(main, ["batch", "run", "--file", file])
    assert result.exit_code == 2
    assert client.calls == []


def test_yes_flag_does_not_bypass_critical(tmp_path, monkeypatch):
    monkeypatch.setattr("pland_cli.core.guard._audit_path", lambda: tmp_path / "a.jsonl")
    client = _FakeClient()
    import pland_cli.enrichment.batch as batch_mod
    monkeypatch.setattr(batch_mod, "get_client", lambda ctx: client)
    file = _write(tmp_path, [
        {"group": "salary", "command": "release-using-time-tracking", "data": {"timeTrackingId": "t"}},
    ])
    result = CliRunner().invoke(main, ["batch", "run", "--file", file, "--yes"])
    assert result.exit_code == 2
    assert client.calls == []


def test_failure_makes_exit_code_nonzero(tmp_path, monkeypatch):
    monkeypatch.setattr("pland_cli.core.guard._audit_path", lambda: tmp_path / "a.jsonl")
    client = _FakeClient(fail_on={"/jobs/bad"})
    import pland_cli.enrichment.batch as batch_mod
    monkeypatch.setattr(batch_mod, "get_client", lambda ctx: client)
    file = _write(tmp_path, [
        {"group": "jobs", "command": "view", "args": ["ok"]},
        {"group": "jobs", "command": "view", "args": ["bad"]},
    ])
    result = CliRunner().invoke(main, ["batch", "run", "--file", file])
    assert result.exit_code == 1
    assert "1 failed" in result.output


def test_unknown_command_aborts_before_any_request(tmp_path, monkeypatch):
    client = _FakeClient()
    import pland_cli.enrichment.batch as batch_mod
    monkeypatch.setattr(batch_mod, "get_client", lambda ctx: client)
    file = _write(tmp_path, [
        {"group": "jobs", "command": "view", "args": ["ok"]},
        {"group": "salary", "command": "nope"},
    ])
    result = CliRunner().invoke(main, ["batch", "run", "--file", file])
    assert result.exit_code != 0
    assert client.calls == []
