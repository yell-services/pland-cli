from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from pland_cli._codegen.extract import extract_operations


def build_commands_reference(spec: dict) -> str:
    ops = extract_operations(spec)
    by_group: dict[str, list] = defaultdict(list)
    for op in ops:
        by_group[op.group].append(op)
    lines = ["# pland — Command-Referenz (generiert)", ""]
    for group in sorted(by_group):
        lines.append(f"## {group}")
        lines.append("")
        lines.append("| Command | Methode | Beschreibung |")
        lines.append("|---|---|---|")
        for op in sorted(by_group[group], key=lambda o: o.command):
            summ = (op.summary or "").replace("|", "\\|")
            lines.append(f"| `pland {group} {op.command}` | {op.method.upper()} | {summ} |")
        lines.append("")
    return "\n".join(lines)


def main() -> None:
    from pland_cli._codegen.spec import load_spec

    out = Path(__file__).resolve().parents[1] / "skills" / "references" / "commands.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build_commands_reference(load_spec()), encoding="utf-8")
    print(f"→ {out}")


if __name__ == "__main__":
    main()
