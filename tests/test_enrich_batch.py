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


@pytest.mark.parametrize("entry", [
    # Row 1: gate says free (DELETE /holidays/{id}), would send DELETE /users/USERID.
    {"group": "holiday", "command": "delete", "args": ["../../users/USERID"]},
    # Row 2: gate says confirm, would send the 🔴 mass-delete DELETE /notifications/delete.
    {"group": "jobs", "command": "delete", "args": ["../notifications/delete"]},
    # Row 3: gate says free, would send PATCH /api_key/KEYID.
    {"group": "articles", "command": "update", "args": ["../api_key/KEYID"]},
])
def test_resolve_rejects_path_arguments_that_escape_their_segment(entry):
    """A '/' in a path argument makes the gated path differ from the sent one."""
    with pytest.raises(click.ClickException, match="must not contain '/'"):
        resolve_entries([entry])


def test_resolve_refuses_a_write_with_required_query_parameters():
    """jobs delete needs splitDate and type, which no batch entry can carry."""
    with pytest.raises(click.ClickException, match="requires query parameters"):
        resolve_entries([{"group": "jobs", "command": "delete", "args": ["a1"]}])


def test_resolve_refuses_a_get_with_required_query_parameters():
    """The limitation is about the entry format, so it holds for reads too."""
    with pytest.raises(click.ClickException, match=r"requires query parameters \['fieldKey'\]"):
        resolve_entries([{"group": "assignments", "command": "get-distinct-field-values"}])


def test_resolve_rejects_non_object_data():
    with pytest.raises(click.ClickException, match="entry 0: 'data' must be a JSON object"):
        resolve_entries([{"group": "jobs", "command": "create", "data": 42}])


def test_resolve_treats_null_args_as_no_path_arguments():
    resolved = resolve_entries([{"group": "jobs", "command": "create", "args": None}])
    assert resolved[0].path == "/jobs/v2"


def test_resolve_rejects_empty_dict_args():
    """Falsy non-lists must not slip through as an implicit empty arg list."""
    with pytest.raises(click.ClickException, match="entry 0: 'args' must be a JSON array"):
        resolve_entries([{"group": "jobs", "command": "view", "args": {}}])


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
    refused = 0
    for (group, command), op in _operation_index().items():
        func = "_cmd_" + f"{group}_{command}".replace("-", "_")
        if func not in generated:
            continue
        entry = {"group": group, "command": command, "args": ["x"] * len(op.path_params)}
        if any(p.get("required") for p in op.query_params):
            # resolve_entries refuses these outright, so they have no runtime
            # risk to compare. Assert the refusal rather than merely skipping.
            with pytest.raises(click.ClickException, match="requires query parameters"):
                resolve_entries([entry])
            refused += 1
            continue
        expected = resolve_entries([entry])[0].risk
        assert generated[func] == expected, f"{group} {command}"
        checked += 1
    # Exact, not a floor: 522 generated commands map onto a spec operation and
    # 43 of them carry a required query parameter. If either number moves, the
    # comparison surface changed and this test must be re-read, not re-tuned.
    assert (checked, refused) == (479, 43), f"compared {checked}, refused {refused}"


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

    def delete(self, path, params=None):
        self.calls.append(("delete", path, None))
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
    client = _FakeClient(fail_on={"/absences/bad"})
    execute(client, [
        _entry(0, "jobs", "view", "get", "/jobs/ok1", "free"),
        _entry(1, "absences", "delete", "delete", "/absences/bad", "confirm"),
    ])
    lines = log.read_text().splitlines()
    assert len(lines) == 2
    assert json.loads(lines[0])["decision"] == "batch_ok"
    # The audit trail is the only forensic record a batch leaves, so pin every
    # field execute() writes, not just the decision.
    record = json.loads(lines[1])
    assert record["decision"] == "batch_failed"
    assert record["batch_index"] == 1
    assert record["method"] == "DELETE"
    assert record["path"] == "/absences/bad"
    assert record["risk"] == "confirm"


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
    payload = json.loads(result.stdout)
    assert payload["dry_run"] is True
    assert payload["count"] == 1
    assert payload["risk"] == "critical"
    assert payload["confirmToken"] == "releaseWithTimeTracking"
    # The human still sees the plan before any gate — on stderr, out of the way.
    assert "salary release-using-time-tracking" in result.stderr


def test_json_dry_run_lists_every_request(tmp_path, monkeypatch):
    """An agent has to read what each entry would send, not just how many."""
    monkeypatch.setenv("PLAND_BASE_URL", "https://api.test/v2")
    file = _write(tmp_path, [
        {"group": "salary", "command": "release-using-time-tracking",
         "data": {"timeTrackingId": "t"}},
        {"group": "holiday", "command": "delete", "args": ["h1"]},
    ])
    result = CliRunner().invoke(main, ["--json", "batch", "run", "--file", file, "--dry-run"])
    assert result.exit_code == 0
    ops = json.loads(result.stdout)["operations"]
    assert [o["index"] for o in ops] == [0, 1]
    assert ops[0] == {
        "index": 0, "group": "salary", "command": "release-using-time-tracking",
        "risk": "critical", "method": "POST",
        "url": "https://api.test/v2/salaries/releaseWithTimeTracking",
        "path": "/salaries/releaseWithTimeTracking", "params": None,
        "body": {"timeTrackingId": "t"},
    }
    # The path argument has to appear in the URL, or the preview names the wrong record.
    assert ops[1]["url"] == "https://api.test/v2/holidays/h1"
    assert ops[1]["method"] == "DELETE"


def test_json_dry_run_sends_no_request(tmp_path, monkeypatch):
    """A batch preview must not touch the API, whatever the file holds."""
    def _no_client(ctx):  # pragma: no cover - reaching this IS the failure
        raise AssertionError("batch dry run resolved a client")

    import pland_cli.enrichment.batch as batch_mod
    monkeypatch.setattr(batch_mod, "get_client", _no_client)
    file = _write(tmp_path, [
        {"group": "users", "command": "delete", "args": ["u1"]},
        {"group": "salary", "command": "release-using-time-tracking",
         "data": {"timeTrackingId": "t"}},
    ])
    result = CliRunner().invoke(main, ["--json", "batch", "run", "--file", file, "--dry-run"])
    assert result.exit_code == 0


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


def test_yes_flag_releases_a_confirm_batch(tmp_path, monkeypatch):
    """--yes must actually reach guard.enforce for the 🟡 tier."""
    monkeypatch.setattr("pland_cli.core.guard._audit_path", lambda: tmp_path / "a.jsonl")
    client = _FakeClient()
    import pland_cli.enrichment.batch as batch_mod
    monkeypatch.setattr(batch_mod, "get_client", lambda ctx: client)
    file = _write(tmp_path, [{"group": "absences", "command": "delete", "args": ["a1"]}])
    result = CliRunner().invoke(main, ["batch", "run", "--file", file, "--yes"])
    assert result.exit_code == 0
    assert client.calls == [("delete", "/absences/a1", None)]


def test_confirm_batch_without_yes_is_fail_closed(tmp_path, monkeypatch):
    """The same file without --yes: no TTY under CliRunner, so nothing is sent."""
    monkeypatch.setattr("pland_cli.core.guard._audit_path", lambda: tmp_path / "a.jsonl")
    client = _FakeClient()
    import pland_cli.enrichment.batch as batch_mod
    monkeypatch.setattr(batch_mod, "get_client", lambda ctx: client)
    file = _write(tmp_path, [{"group": "absences", "command": "delete", "args": ["a1"]}])
    result = CliRunner().invoke(main, ["batch", "run", "--file", file])
    assert result.exit_code == 2
    assert client.calls == []


def test_mixed_batch_gates_on_a_critical_entry_that_is_not_first(tmp_path, monkeypatch):
    """The gate is max() over the whole file, not the first entry's risk.

    A free read followed by a 🔴 release must still hit the 🔴 tier, which
    fail-closes without a TTY — so not even the free read is sent.
    """
    monkeypatch.setattr("pland_cli.core.guard._audit_path", lambda: tmp_path / "a.jsonl")
    client = _FakeClient()
    import pland_cli.enrichment.batch as batch_mod
    monkeypatch.setattr(batch_mod, "get_client", lambda ctx: client)
    file = _write(tmp_path, [
        {"group": "jobs", "command": "view", "args": ["x1"]},
        {"group": "salary", "command": "release-using-time-tracking",
         "data": {"timeTrackingId": "t"}},
    ])
    result = CliRunner().invoke(main, ["batch", "run", "--file", file])
    assert result.exit_code == 2
    assert client.calls == []


def test_mixed_batch_without_yes_is_fail_closed_when_confirm_is_not_first(tmp_path, monkeypatch):
    """free + confirm with the confirm last: one 🟡 gate, and it fail-closes."""
    monkeypatch.setattr("pland_cli.core.guard._audit_path", lambda: tmp_path / "a.jsonl")
    client = _FakeClient()
    import pland_cli.enrichment.batch as batch_mod
    monkeypatch.setattr(batch_mod, "get_client", lambda ctx: client)
    file = _write(tmp_path, [
        {"group": "jobs", "command": "view", "args": ["x1"]},
        {"group": "absences", "command": "delete", "args": ["a1"]},
    ])
    result = CliRunner().invoke(main, ["batch", "run", "--file", file])
    assert result.exit_code == 2
    assert client.calls == []


def test_mixed_batch_with_yes_runs_every_entry_when_confirm_is_not_first(tmp_path, monkeypatch):
    """The same file with --yes: one 🟡 gate released, both entries execute."""
    monkeypatch.setattr("pland_cli.core.guard._audit_path", lambda: tmp_path / "a.jsonl")
    client = _FakeClient()
    import pland_cli.enrichment.batch as batch_mod
    monkeypatch.setattr(batch_mod, "get_client", lambda ctx: client)
    file = _write(tmp_path, [
        {"group": "jobs", "command": "view", "args": ["x1"]},
        {"group": "absences", "command": "delete", "args": ["a1"]},
    ])
    result = CliRunner().invoke(main, ["batch", "run", "--file", file, "--yes"])
    assert result.exit_code == 0
    assert client.calls == [("get", "/jobs/x1", None), ("delete", "/absences/a1", None)]


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


def test_gate_names_the_first_entry_at_the_maximum_risk(tmp_path, monkeypatch):
    """The prompt label and the 🔴 token must name the operation being gated.

    Taking entries[0] instead would still gate at the right tier, but would ask
    the user to type a token for a benign resource while a critical entry rides
    along on that confirmation.
    """
    monkeypatch.setattr("pland_cli.core.guard._audit_path", lambda: tmp_path / "a.jsonl")
    seen: dict = {}
    monkeypatch.setattr("pland_cli.core.guard.enforce", lambda **kw: seen.update(kw))
    client = _FakeClient()
    import pland_cli.enrichment.batch as batch_mod
    monkeypatch.setattr(batch_mod, "get_client", lambda ctx: client)
    file = _write(tmp_path, [
        {"group": "jobs", "command": "view", "args": ["x1"]},
        {"group": "absences", "command": "delete", "args": ["a1"]},
        {"group": "salary", "command": "release-using-time-tracking",
         "data": {"timeTrackingId": "t1"}},
        {"group": "salary", "command": "release-using-time-tracking",
         "data": {"timeTrackingId": "t2"}},
    ])
    result = CliRunner().invoke(main, ["batch", "run", "--file", file])
    assert result.exit_code == 0
    assert seen["risk"] == "critical"
    assert seen["method"] == "post"
    assert seen["path"] == "/salaries/releaseWithTimeTracking"


def test_confirm_token_runs_the_critical_batch_without_a_tty(tmp_path, monkeypatch):
    """The user gave the go, so the token is passed instead of typed."""
    monkeypatch.setattr("pland_cli.core.guard._audit_path", lambda: tmp_path / "a.jsonl")
    client = _FakeClient()
    import pland_cli.enrichment.batch as batch_mod
    monkeypatch.setattr(batch_mod, "get_client", lambda ctx: client)
    file = _write(tmp_path, [
        {"group": "salary", "command": "release-using-time-tracking", "data": {"timeTrackingId": "t"}},
    ])
    result = CliRunner().invoke(
        main, ["batch", "run", "--file", file, "--confirm", "releaseWithTimeTracking"])
    assert result.exit_code == 0
    assert client.calls == [("post", "/salaries/releaseWithTimeTracking", {"timeTrackingId": "t"})]


def test_a_wrong_confirm_token_sends_nothing(tmp_path, monkeypatch):
    monkeypatch.setattr("pland_cli.core.guard._audit_path", lambda: tmp_path / "a.jsonl")
    client = _FakeClient()
    import pland_cli.enrichment.batch as batch_mod
    monkeypatch.setattr(batch_mod, "get_client", lambda ctx: client)
    file = _write(tmp_path, [
        {"group": "salary", "command": "release-using-time-tracking", "data": {"timeTrackingId": "t"}},
    ])
    result = CliRunner().invoke(main, ["batch", "run", "--file", file, "--confirm", "jobs"])
    assert result.exit_code == 2
    assert client.calls == []


def test_the_plan_names_the_token_to_pass(tmp_path, monkeypatch):
    """--dry-run has to tell the caller which token the real run expects."""
    monkeypatch.setattr("pland_cli.core.guard._audit_path", lambda: tmp_path / "a.jsonl")
    file = _write(tmp_path, [
        {"group": "salary", "command": "release-using-time-tracking", "data": {"timeTrackingId": "t"}},
    ])
    result = CliRunner().invoke(main, ["batch", "run", "--file", file, "--dry-run"])
    assert result.exit_code == 0
    assert "--confirm releaseWithTimeTracking" in result.output
