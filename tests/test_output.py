import json

import pytest

from pland_cli.utils import output


def test_out_json_is_parseable(capsys):
    output.set_json(True)
    output.out({"a": 1, "b": [1, 2]})
    captured = capsys.readouterr()
    assert json.loads(captured.out) == {"a": 1, "b": [1, 2]}


def test_out_ok_json_envelope(capsys):
    output.set_json(True)
    output.out_ok("done", {"id": "x"})
    payload = json.loads(capsys.readouterr().out)
    assert payload == {"ok": True, "message": "done", "data": {"id": "x"}}


def test_out_err_exits_nonzero(capsys):
    output.set_json(True)
    with pytest.raises(SystemExit) as exc:
        output.out_err(404, "Not Found", "missing", {"errors": []})
    assert exc.value.code == 1
    payload = json.loads(capsys.readouterr().err)
    assert payload["ok"] is False
    assert payload["error"]["status"] == 404
