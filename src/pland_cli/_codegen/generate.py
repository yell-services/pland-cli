from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from pland_cli._codegen.extract import extract_operations
from pland_cli._codegen.render import _group_var, render_command

_HEADER = '''"""Auto-generiert aus openapi.yaml — NICHT manuell editieren.
Regenerieren: python -m pland_cli._codegen.generate
"""
import click
'''


def generate_modules(spec: dict, out_dir: Path) -> list[Path]:
    ops = extract_operations(spec)
    by_group: dict[str, list] = defaultdict(list)
    seen: set[tuple[str, str]] = set()
    for op in ops:
        key = (op.group, op.command)
        if key in seen:
            raise ValueError(f"Command-Kollision: {key}")
        seen.add(key)
        by_group[op.group].append(op)

    out_dir.mkdir(parents=True, exist_ok=True)
    # Idempotent: drop the previously generated modules first, otherwise
    # bei umbenannten/entfernten Gruppen verwaiste *.py-Dateien liegen.
    for stale in out_dir.glob("*.py"):
        stale.unlink()
    written: list[Path] = []
    for group, group_ops in sorted(by_group.items()):
        gvar = _group_var(group)
        parts = [_HEADER, "", f'@click.group("{group}")', f"def {gvar}():",
                 f'    """{group}-Operationen."""', "    pass", ""]
        for op in group_ops:
            parts.append(render_command(op))
            parts.append("")
        parts.append("def register(root):")
        parts.append(f"    root.add_command({gvar})")
        parts.append("")
        module_name = group.replace("-", "_") + ".py"
        target = out_dir / module_name
        target.write_text("\n".join(parts), encoding="utf-8")
        written.append(target)
    return written


def main() -> None:
    from pland_cli._codegen.spec import load_spec

    out_dir = Path(__file__).resolve().parents[1] / "commands"
    written = generate_modules(load_spec(), out_dir)
    (out_dir / "__init__.py").write_text('"""Auto-generierte Command-Module."""\n', encoding="utf-8")
    print(f"wrote {len(written)} modules to {out_dir}")


if __name__ == "__main__":
    main()
