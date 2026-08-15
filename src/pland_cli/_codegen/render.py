from __future__ import annotations

import json
import keyword
import re

from pland_cli._codegen.extract import Operation
from pland_cli._codegen.security import classify, draftable_for

_PYTYPE = {"integer": "int", "number": "float", "boolean": "bool"}


def _ident(name: str) -> str:
    out = re.sub(r"[^a-zA-Z0-9_]", "_", name)
    if keyword.iskeyword(out):
        out += "_"
    return out


def _group_var(group: str) -> str:
    return _ident(group) + "_group"


def _path_ident(name: str) -> str:
    """Identifier for a path parameter, matching what Click derives from it.

    Arguments are declared as ``@click.argument("USERID")`` and Click builds the
    parameter name by lowercasing that decl. A camelCase identifier such as
    ``userId`` therefore never receives its value and the command raises
    TypeError on invocation. Lowercase first, then run the keyword guard, so a
    path parameter named e.g. ``Class`` does not become the keyword ``class``.
    """
    return _ident(name.lower())


def render_command(op: Operation) -> str:
    # GET is always read-only -> free (classify() only reasons about write ops
    # and would fall through to its confirm fail-safe for reads).
    risk = "free" if op.method == "get" else classify(op.method, op.path, op.tag)
    marker = {"confirm": "🟡 ", "critical": "🔴 "}.get(risk, "")
    if marker:
        short = json.dumps((marker + (op.summary or ""))[:100], ensure_ascii=False)
        lines: list[str] = [
            f'@{_group_var(op.group)}.command("{op.command}", short_help={short})'
        ]
    else:
        lines = [f'@{_group_var(op.group)}.command("{op.command}")']
    sig_params: list[str] = []

    for p in op.path_params:
        arg = p["name"]
        lines.append(f'@click.argument("{arg.upper()}")')
        sig_params.append(_path_ident(arg))

    for p in op.query_params:
        opt = p["name"]
        flag = "--" + opt.replace("_", "-")
        schema = p.get("schema", {})
        # json.dumps emits the literal including quotes and escapes " properly —
        # a blind " -> ' swap would make JSON examples in help text unusable.
        help_txt = json.dumps((p.get("description") or "")[:120], ensure_ascii=False)
        extra = ""
        if "enum" in schema:
            choices = ", ".join(f'"{c}"' for c in schema["enum"])
            extra = f", type=click.Choice([{choices}])"
        elif schema.get("type") in _PYTYPE:
            extra = f", type={_PYTYPE[schema['type']]}"
        lines.append(
            f'@click.option("{flag}", "{_ident(opt)}", default=None{extra}, help={help_txt})'
        )
        sig_params.append(_ident(opt))

    if op.is_multipart:
        lines.append('@click.option("--file", "file_", type=click.Path(exists=True), help="File (multipart).")')
        sig_params.append("file_")
    elif op.has_json_body:
        lines.append('@click.option("--data", default=None, help="Request body as a JSON string.")')
        sig_params.append("data")

    if op.returns_binary:
        lines.append('@click.option("--output", type=click.Path(), help="Write the response to a file.")')
        sig_params.append("output")

    # Every write gets --dry-run; a free one has no gate to clear, so --yes and
    # --confirm would only be flags that do nothing.
    gated = risk in ("confirm", "critical")
    if op.method != "get":
        lines.append('@click.option("--dry-run", "dry_run", is_flag=True, help="Show the request without sending it.")')
        sig_params.append("dry_run")
    if gated:
        lines.append('@click.option("--yes", "assume_yes", is_flag=True, help="Skip the confirmation (🟡 only; 🔴 needs a terminal or --confirm).")')
        sig_params.append("assume_yes")
        lines.append('@click.option("--confirm", "confirm_token", metavar="TOKEN", help="Pass the confirmation token instead of typing it at a terminal. For a caller without a TTY that has the user\'s explicit go; the token still has to match.")')
        sig_params.append("confirm_token")

    is_list_get = op.method == "get" and not op.path_params and not op.returns_binary
    if is_list_get:
        lines.append('@click.option("--all", "fetch_all", is_flag=True, help="Paginate through all pages.")')
        sig_params.append("fetch_all")

    lines.append('@click.option("--extra-params", default=None, help="Additional query params as JSON.")')
    sig_params.append("extra_params")
    lines.append("@click.pass_context")

    fn = f"_cmd_{_ident(op.group)}_{_ident(op.command)}"
    arglist = ", ".join(["ctx", *sig_params])
    lines.append(f"def {fn}({arglist}):")
    lines.append(f'    """{op.summary}"""')
    lines.append("    from pland_cli._codegen.runtime import run_operation")
    qp = "{" + ", ".join(f'"{p["name"]}": {_ident(p["name"])}' for p in op.query_params) + "}"
    path_expr = '"' + op.path + '"'
    for p in op.path_params:
        path_expr = path_expr.replace("{" + p["name"] + "}", '" + ' + _path_ident(p["name"]) + ' + "')
    lines.append("    run_operation(")
    lines.append(f"        ctx, method={op.method!r}, path={path_expr},")
    fetch_arg = "fetch_all" if is_list_get else "False"
    lines.append(f"        query={qp}, extra_params=extra_params, fetch_all={fetch_arg},")
    body_arg = "data" if op.has_json_body else "None"
    file_arg = "file_" if op.is_multipart else "None"
    out_arg = "output" if op.returns_binary else "None"
    dry_arg = "dry_run" if op.method != "get" else "False"
    yes_arg = "assume_yes" if gated else "False"
    token_arg = "confirm_token" if gated else "None"
    draft = draftable_for(op.method, op.path, op.tag)
    draft_arg = f'"{draft}"' if draft else "None"
    lines.append(f"        data={body_arg}, file_={file_arg}, output={out_arg}, dry_run={dry_arg},")
    lines.append(f'        risk="{risk}", draftable={draft_arg}, assume_yes={yes_arg},')
    lines.append(f'        confirm_token={token_arg},')
    lines.append("    )")
    return "\n".join(lines)
