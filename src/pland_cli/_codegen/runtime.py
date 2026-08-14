from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import click

from pland_cli.core.client import PlandError
from pland_cli.utils import output as out_mod


def _build_params(query: dict, extra_params: str | None) -> dict | None:
    params = {k: v for k, v in query.items() if v is not None}
    if extra_params:
        try:
            params.update(json.loads(extra_params))
        except json.JSONDecodeError as e:
            raise click.BadParameter(f"--extra-params is not valid JSON: {e}") from e
    return params or None


def show_dry_run(ctx: click.Context, method: str, path: str,
                 params: dict | None, body: Any = None,
                 file_: str | None = None) -> None:
    """Print the request that would have gone out, and send nothing.

    The URL is resolved from the same config the client is built from, so the
    caller reads the endpoint a real run targets. A dry run that showed only the
    path could not tell prod from beta — which is the one thing worth checking
    before a write lands in a payroll system.
    """
    from pland_cli.core.config import resolve_config

    try:
        base_url = resolve_config(profile=ctx.obj.get("profile")).base_url
    except ValueError as e:
        raise click.ClickException(str(e)) from e
    payload: dict[str, Any] = {
        "dry_run": True,
        "method": method.upper(),
        "url": base_url.rstrip("/") + "/" + path.lstrip("/"),
        "path": path,
        "params": params,
        "body": body,
    }
    if file_:
        payload["file"] = Path(file_).name
    out_mod.out(payload)


def run_operation(ctx: click.Context, *, method: str, path: str, query: dict,
                  extra_params: str | None, data: str | None,
                  file_: str | None, output: str | None,
                  dry_run: bool = False, fetch_all: bool = False,
                  risk: str = "free", draftable: str | None = None,
                  assume_yes: bool = False,
                  confirm_token: str | None = None) -> None:
    out_mod.set_json(ctx.obj.get("as_json", False))
    params = _build_params(query, extra_params)
    try:
        body: Any = json.loads(data) if data else None
    except json.JSONDecodeError as e:
        raise click.BadParameter(f"--data is not valid JSON: {e}") from e

    if dry_run:
        show_dry_run(ctx, method, path, params, body=body, file_=file_)
        return

    if risk != "free" or draftable:
        from pland_cli.core import guard

        def _lookup() -> dict:
            if "client" not in ctx.obj:
                from pland_cli.cli import _attach_client
                _attach_client(ctx)
            res = ctx.obj["client"].get(path)
            return res if isinstance(res, dict) else {}

        guard.enforce(method=method, path=path, risk=risk, draftable=draftable,
                      assume_yes=assume_yes, lookup=_lookup if draftable else None,
                      confirm_token=confirm_token)

    if "client" not in ctx.obj:
        from pland_cli.cli import _attach_client
        _attach_client(ctx)
    client = ctx.obj["client"]
    files = (
        {"file": (Path(file_).name, Path(file_).read_bytes())} if file_ else None
    )

    try:
        if method == "get":
            if fetch_all:
                from pland_cli.core.pagination import collect_all
                result = collect_all(client, path, params)
            else:
                result = client.get(path, params=params)
        elif method == "post":
            result = client.post(path, json=body, params=params, files=files)
        elif method == "patch":
            result = client.patch(path, json=body, params=params)
        elif method == "put":
            result = client.put(path, json=body, params=params)
        else:
            result = client.delete(path, params=params)
    except PlandError as e:
        out_mod.out_err(e.status, e.title, e.detail, e.raw)
        return

    if isinstance(result, bytes):
        if output:
            Path(output).write_bytes(result)
            out_mod.out_ok(f"{len(result)} Bytes → {output}")
        else:
            click.get_binary_stream("stdout").write(result)
    else:
        out_mod.out(result)
