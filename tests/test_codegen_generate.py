from pland_cli._codegen.generate import generate_modules
from pland_cli._codegen.spec import load_spec

SPEC = {
    "paths": {
        "/absences/": {
            "get": {"tags": ["Absences"], "operationId": "listAbsences", "summary": "List"},
            "post": {"tags": ["Absences"], "operationId": "createAbsence", "summary": "Create",
                     "requestBody": {"content": {"application/json": {"schema": {}}}}},
        },
        "/pay-types/": {
            "get": {"tags": ["Pay Types"], "operationId": "listPayTypes", "summary": "List"},
        },
    }
}


def test_generates_one_module_per_group(tmp_path):
    written = generate_modules(SPEC, tmp_path)
    names = {p.name for p in written}
    assert names == {"absences.py", "pay_types.py"}


def test_generate_modules_removes_orphaned_files(tmp_path):
    # Eine verwaiste (z.B. vorher anders benannte) generierte Datei muss beim
    # erneuten Lauf verschwinden, sonst zählt der Konformitätstest zu viele
    # Module. Idempotenz: out_dir enthält danach exakt die aktuellen Module.
    orphan = tmp_path / "chat_(legacy).py"
    orphan.write_text("# verwaist\n")
    generate_modules(SPEC, tmp_path)
    assert not orphan.exists()
    assert {p.name for p in tmp_path.glob("*.py")} == {"absences.py", "pay_types.py"}


def test_generated_module_is_valid_python(tmp_path):
    generate_modules(SPEC, tmp_path)
    source = (tmp_path / "absences.py").read_text()
    compile(source, "absences.py", "exec")  # SyntaxError → Testfehler
    assert "def register(root" in source
    assert '@absences_group.command("list")' in source


def test_collision_raises(tmp_path, monkeypatch):
    # extract_operations._disambiguate() already resolves any (group, command)
    # collision before generate_modules sees it, so a true collision can only
    # reach the guard if extraction itself misbehaves. We force that here to
    # prove the defensive guard fires instead of silently overwriting a command.
    from pland_cli._codegen import generate as gen_mod
    from pland_cli._codegen.extract import Operation

    dup = [
        Operation(operation_id="listX", tag="X", method="get", path="/a/",
                  group="x", command="list", summary=""),
        Operation(operation_id="listX", tag="X", method="post", path="/a/",
                  group="x", command="list", summary=""),
    ]
    monkeypatch.setattr(gen_mod, "extract_operations", lambda spec: dup)

    import pytest
    with pytest.raises(ValueError, match="Kollision"):
        generate_modules({}, tmp_path)


def test_load_spec_dev_tree_resolves_real_spec():
    """load_spec() with no args must work in the editable dev tree.

    The package resource ``pland_cli/openapi.yaml`` is absent from the src
    tree (force-included only on wheel build), so load_spec falls back to the
    repo-root ``openapi.yaml``. The real spec has 421 paths.
    """
    spec = load_spec()
    assert len(spec["paths"]) == 421
