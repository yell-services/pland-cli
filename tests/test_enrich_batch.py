import re
from pathlib import Path

import click
import pytest

import pland_cli.commands as commands_pkg
from pland_cli.enrichment.batch import (
    ResolvedEntry,
    _operation_index,
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
