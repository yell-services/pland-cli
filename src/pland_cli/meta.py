from __future__ import annotations

import click

from pland_cli._codegen.extract import extract_operations
from pland_cli._codegen.spec import load_spec
from pland_cli.utils import output as out_mod


@click.command("schema")
@click.argument("NAME")
@click.pass_context
def schema_cmd(ctx: click.Context, name: str) -> None:
    """Zeigt eine Schema-Definition aus components/schemas."""
    out_mod.set_json(ctx.obj.get("as_json", False))
    schemas = (load_spec().get("components") or {}).get("schemas") or {}
    if name not in schemas:
        out_mod.out_err(404, "Unbekanntes Schema", name, exit_code=2)
    out_mod.out(schemas[name])


@click.command("describe")
@click.argument("GROUP")
@click.argument("COMMAND")
@click.pass_context
def describe_cmd(ctx: click.Context, group: str, command: str) -> None:
    """Zeigt Methode, Pfad und Parameter eines Commands."""
    out_mod.set_json(ctx.obj.get("as_json", False))
    for op in extract_operations(load_spec()):
        if op.group == group and op.command == command:
            out_mod.out({
                "group": op.group, "command": op.command,
                "method": op.method, "path": op.path,
                "query_params": [p["name"] for p in op.query_params],
                "path_params": [p["name"] for p in op.path_params],
                "has_json_body": op.has_json_body, "is_multipart": op.is_multipart,
            })
            return
    # Fallback: enriched/neue Commands stehen nicht in der Spec → aus dem Click-Baum
    from pland_cli.cli import main as _root
    grp = _root.commands.get(group)
    if isinstance(grp, click.Group) and command in grp.commands:
        cmd = grp.commands[command]
        out_mod.out({
            "group": group, "command": command, "source": "enriched",
            "help": (cmd.help or "").strip(),
            "options": [p.name for p in cmd.params if isinstance(p, click.Option)],
            "arguments": [p.name for p in cmd.params if isinstance(p, click.Argument)],
        })
        return
    out_mod.out_err(404, "Unbekannter Command", f"{group} {command}", exit_code=2)


def register_meta(root: click.Group) -> None:
    root.add_command(schema_cmd)
    root.add_command(describe_cmd)
