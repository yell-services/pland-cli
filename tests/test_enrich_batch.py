import click
import pytest

from pland_cli.enrichment.batch import max_risk, resolve_entries


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
