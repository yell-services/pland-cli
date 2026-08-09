import json

import click
import httpx

from pland_cli._codegen.runtime import run_operation
from pland_cli.core.client import PlandClient
from pland_cli.core.config import Config


def _ctx(handler, as_json=True):
    cfg = Config(base_url="https://api.test/v2", api_key="k", profile="prod")
    client = PlandClient(cfg, transport=httpx.MockTransport(handler))
    ctx = click.Context(click.Command("x"))
    ctx.obj = {"as_json": as_json, "client": client}
    return ctx


def test_get_builds_query_and_outputs(capsys):
    def handler(request):
        assert request.url.params.get("limit") == "5"
        return httpx.Response(200, json=[{"_id": "1"}])

    run_operation(_ctx(handler), method="get", path="/absences/",
                  query={"limit": 5, "offset": None}, extra_params=None,
                  data=None, file_=None, output=None)
    assert json.loads(capsys.readouterr().out) == [{"_id": "1"}]


def test_post_parses_data_json(capsys):
    def handler(request):
        assert json.loads(request.content) == {"x": 1}
        return httpx.Response(200, json={"_id": "n"})

    run_operation(_ctx(handler), method="post", path="/absences/",
                  query={}, extra_params=None, data='{"x": 1}', file_=None, output=None)
    assert json.loads(capsys.readouterr().out) == {"_id": "n"}


def test_binary_output_writes_file(tmp_path):
    def handler(request):
        return httpx.Response(200, content=b"PKzip", headers={"content-type": "application/zip"})

    out = tmp_path / "export.zip"
    run_operation(_ctx(handler), method="get", path="/salaries/export-rows",
                  query={}, extra_params=None, data=None, file_=None, output=str(out))
    assert out.read_bytes() == b"PKzip"


def test_post_with_file_reads_bytes_and_uploads(tmp_path, capsys):
    f = tmp_path / "upload.bin"
    f.write_bytes(b"PAYLOAD")

    def handler(request):
        assert b"PAYLOAD" in request.content
        assert b"upload.bin" in request.content  # Dateiname als filename
        return httpx.Response(200, json={"_id": "u"})

    run_operation(_ctx(handler), method="post", path="/assets/",
                  query={}, extra_params=None, data=None,
                  file_=str(f), output=None)
    assert json.loads(capsys.readouterr().out) == {"_id": "u"}


def test_bad_data_json_raises_bad_parameter():
    ctx = click.Context(click.Command("x"))
    ctx.obj = {"as_json": True}
    try:
        run_operation(ctx, method="post", path="/absences/", query={},
                      extra_params=None, data="{not json}", file_=None,
                      output=None, dry_run=True)
    except click.BadParameter as e:
        assert "--data" in str(e)
    else:  # pragma: no cover
        raise AssertionError("erwartete click.BadParameter")


def test_bad_extra_params_json_raises_bad_parameter():
    ctx = click.Context(click.Command("x"))
    ctx.obj = {"as_json": True}
    try:
        run_operation(ctx, method="get", path="/absences/", query={},
                      extra_params="{nope}", data=None, file_=None,
                      output=None, dry_run=True)
    except click.BadParameter as e:
        assert "--extra-params" in str(e)
    else:  # pragma: no cover
        raise AssertionError("erwartete click.BadParameter")


def test_dry_run_builds_request_without_client(capsys):
    import json as _json

    import click
    ctx = click.Context(click.Command("x"))
    ctx.obj = {"as_json": True}  # KEIN client → dry-run darf trotzdem laufen
    run_operation(ctx, method="post", path="/absences/", query={}, extra_params=None,
                  data='{"x": 1}', file_=None, output=None, dry_run=True)
    payload = _json.loads(capsys.readouterr().out)
    assert payload["method"] == "POST"
    assert payload["path"] == "/absences/"
    assert payload["body"] == {"x": 1}


def test_run_operation_blocks_confirm_without_tty(monkeypatch):
    # Without a TTY a confirm operation must fail closed (exit 2).
    from click.testing import CliRunner

    from pland_cli._codegen import runtime

    @click.command()
    @click.pass_context
    def cmd(ctx):
        ctx.obj = {"as_json": True}
        runtime.run_operation(ctx, method="delete", path="/documents/1", query={},
                              extra_params=None, data=None, file_=None, output=None,
                              dry_run=False, risk="confirm", draftable=None, assume_yes=False)
    res = CliRunner().invoke(cmd)
    assert res.exit_code == 2


def test_run_operation_dry_run_skips_guard(monkeypatch):
    from click.testing import CliRunner

    from pland_cli._codegen import runtime

    @click.command()
    @click.pass_context
    def cmd(ctx):
        ctx.obj = {"as_json": True}
        runtime.run_operation(ctx, method="delete", path="/documents/1", query={},
                              extra_params=None, data=None, file_=None, output=None,
                              dry_run=True, risk="critical", draftable=None, assume_yes=False)
    res = CliRunner().invoke(cmd)
    assert res.exit_code == 0  # dry run only shows the request, no guard
