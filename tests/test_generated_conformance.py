import importlib
import pkgutil
import re
from pathlib import Path

import pland_cli.commands as commands_pkg
from pland_cli._codegen.extract import extract_operations
from pland_cli._codegen.spec import load_spec

_ARGUMENT_THEN_DEF = re.compile(
    r'@click\.argument\("([A-Z_0-9]+)"\)\n(?:@click[^\n]*\n)*@click\.pass_context\n'
    r"def (_cmd_[a-z0-9_]+)\(ctx, ([a-zA-Z_0-9]+)",
)


def test_one_module_per_group():
    spec_groups = {op.group for op in extract_operations(load_spec())}
    module_groups = {m.name for m in pkgutil.iter_modules(commands_pkg.__path__)}
    expected = {g.replace("-", "_") for g in spec_groups}
    assert module_groups == expected


def test_all_modules_import_cleanly():
    for m in pkgutil.iter_modules(commands_pkg.__path__):
        importlib.import_module(f"pland_cli.commands.{m.name}")


def test_command_count_matches_spec():
    # The generated command groups are the same singletons registered on `main`,
    # so importing the CLI (which any other test may have already triggered)
    # mutates them in place via the enrichment overlay. To stay a pure check on
    # the *generated* layer, count only the (group, command) pairs that come from
    # the spec itself — enrichment-added commands (new=True) are simply not in it.
    ops = extract_operations(load_spec())
    spec_pairs = {(op.group, op.command) for op in ops}

    total = 0
    for m in pkgutil.iter_modules(commands_pkg.__path__):
        mod = importlib.import_module(f"pland_cli.commands.{m.name}")
        group_var = [v for k, v in vars(mod).items() if k.endswith("_group")][0]
        total += sum(
            1 for cmd_name in group_var.commands
            if (group_var.name, cmd_name) in spec_pairs
        )
    assert total == len(ops)


def test_every_write_command_offers_dry_run():
    """One hook in the generator covers every write; this is what proves it did.

    Reads GET is deliberately excluded — nothing to simulate there, and the flag
    would only be noise in help output and docs.
    """
    ops = extract_operations(load_spec())
    writes = {(op.group, op.command) for op in ops if op.method != "get"}
    checked, missing = 0, []
    for m in pkgutil.iter_modules(commands_pkg.__path__):
        mod = importlib.import_module(f"pland_cli.commands.{m.name}")
        group_var = [v for k, v in vars(mod).items() if k.endswith("_group")][0]
        for cmd_name, cmd in group_var.commands.items():
            if (group_var.name, cmd_name) not in writes:
                continue
            checked += 1
            if not any(p.name == "dry_run" for p in cmd.params):
                missing.append(f"{group_var.name} {cmd_name}")
    assert not missing, f"{len(missing)} write commands without --dry-run: {missing[:10]}"
    assert checked == len(writes), "not every write operation was reached"


def test_confirmation_flags_only_where_there_is_a_gate():
    """--yes and --confirm exist exactly on the commands that can be gated.

    On a free write they would clear nothing, so offering them suggests a
    confirmation that never happens. The pairing matters in the other direction
    too: a gated command missing --confirm cannot be run by a caller without a
    TTY at all.
    """
    from pland_cli._codegen.security import classify

    seen = 0
    for m in pkgutil.iter_modules(commands_pkg.__path__):
        mod = importlib.import_module(f"pland_cli.commands.{m.name}")
        group_var = [v for k, v in vars(mod).items() if k.endswith("_group")][0]
        for cmd_name, cmd in group_var.commands.items():
            names = {p.name for p in cmd.params}
            gated = {"assume_yes", "confirm_token"} <= names
            partial = bool({"assume_yes", "confirm_token"} & names) and not gated
            assert not partial, f"{group_var.name} {cmd_name} has only one of the two flags"
            if not gated:
                continue
            seen += 1
    ops = extract_operations(load_spec())
    expected = sum(
        1 for op in ops
        if op.method != "get" and classify(op.method, op.path, op.tag) in ("confirm", "critical")
    )
    assert seen == expected, f"{seen} commands carry the flags, {expected} operations are gated"


def test_click_argument_names_match_the_function_parameter():
    """Click lowercases an argument name; the signature has to agree.

    A mismatch raises TypeError the moment the command is invoked, so neither
    an import check nor a command count can see it.
    """
    mismatches = []
    for source in sorted(Path(commands_pkg.__path__[0]).glob("*.py")):
        for argument, func, param in _ARGUMENT_THEN_DEF.findall(source.read_text()):
            if argument.lower() != param:
                mismatches.append(
                    f"{source.name}: {func} takes {param!r}, Click passes {argument.lower()!r}"
                )
    assert not mismatches, f"{len(mismatches)} mismatches:\n" + "\n".join(mismatches)
