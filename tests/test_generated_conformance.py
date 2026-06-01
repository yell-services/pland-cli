import importlib
import pkgutil

import pland_cli.commands as commands_pkg
from pland_cli._codegen.extract import extract_operations
from pland_cli._codegen.spec import load_spec


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
