from pathlib import Path

import yaml

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
    # An orphaned generated file (e.g. one named differently before) must
    # disappear on the next run, otherwise the conformance test counts too many
    # modules. Idempotency: out_dir then holds exactly the current modules.
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

    The package resources ``pland_cli/openapi.yaml`` and
    ``pland_cli/openapi.overlay.yaml`` are absent from the src tree
    (force-included only on wheel build), so load_spec falls back to the repo
    root. Upstream ships 421 paths; the overlay drops the ones the API does not
    serve and adds the ones it serves without documenting.
    """
    root = Path(__file__).resolve().parents[1]
    raw = load_spec(root / "openapi.yaml")
    assert len(raw["paths"]) == 421

    overlay = yaml.safe_load((root / "openapi.overlay.yaml").read_text(encoding="utf-8"))
    methods = {"get", "post", "put", "patch", "delete"}
    # A path only disappears when `remove` takes its last operation.
    dropped = sum(1 for path, gone in overlay["remove"].items()
                  if not (set(raw["paths"][path]) & methods) - set(gone))
    # Only entries for paths upstream does not have grow the count — an entry
    # correcting a documented operation replaces it in place.
    added = sum(1 for path in overlay["paths"] if path not in raw["paths"])
    assert len(load_spec()["paths"]) == len(raw["paths"]) - dropped + added


def test_overlay_removes_renames_and_adds():
    """All three overlay sections take effect on the real spec."""
    spec = load_spec()
    # remove: the route does not exist live ("Failed to parse Id: count")
    assert "/surcharges/count" not in spec["paths"]
    # remove: only GET goes away, POST stays
    assert set(spec["paths"]["/invoiceReminders/templates"]) == {"post"}
    # ...and the sibling collection keeps its GET: it serves the reminder list
    assert set(spec["paths"]["/invoiceReminders/"]) == {"get", "post"}
    # params: the API expects fieldKey, the spec said field
    names = [p["name"] for p in spec["paths"]["/invoices/distinctValues"]["get"]["parameters"]]
    assert names == ["fieldKey"]
    # params: the spec's sort example ("name:1") earns a 400 from the API
    sort = next(p for p in spec["paths"]["/invoices/"]["get"]["parameters"]
                if p["name"] == "sort")
    assert '{"by"' in sort["description"]
    # paths: undocumented resource
    assert spec["paths"]["/payTypeTemplates/"]["get"]["tags"] == ["Pay Type Templates"]


def test_overlay_is_a_pure_correction_layer():
    """Every overlay entry must still match the real spec.

    Once pland.app fixes a point upstream this fails instead of quietly doing
    nothing — which is exactly when the entry should be deleted.
    """
    root = Path(__file__).resolve().parents[1]
    raw = load_spec(root / "openapi.yaml")
    overlay = yaml.safe_load((root / "openapi.overlay.yaml").read_text(encoding="utf-8"))

    for path, methods in overlay["remove"].items():
        assert path in raw["paths"], f"remove: {path} no longer exists upstream"
        for method in methods:
            assert method in raw["paths"][path], f"remove: {method} {path} is gone"

    # A paths entry either adds a route upstream lacks, or corrects one it
    # describes wrongly. The correcting kind has to still differ from upstream:
    # the day it matches, pland.app has published the fix and the entry is dead
    # weight.
    for path, ops in overlay["paths"].items():
        if path not in raw["paths"]:
            continue
        for method, op in ops.items():
            assert raw["paths"][path].get(method) != op, (
                f"paths: {method} {path} now matches upstream — drop the entry")

    # Same contract for schema corrections.
    upstream_schemas = (raw.get("components") or {}).get("schemas") or {}
    for name, fields in (overlay.get("schemas") or {}).items():
        if name not in upstream_schemas:
            continue
        for key, value in fields.items():
            assert upstream_schemas[name].get(key) != value, (
                f"schemas: {name}.{key} now matches upstream — drop the entry")


def test_overlay_params_still_apply():
    """The parameter corrections apply exactly as often as documented.

    ``expect`` guards the name-based rules against silent creep: if upstream
    introduces the same parameter name elsewhere, or fixes these call sites, the
    count shifts and the entry wants reassessing.
    """
    root = Path(__file__).resolve().parents[1]
    raw = load_spec(root / "openapi.yaml")
    overlay = yaml.safe_load((root / "openapi.overlay.yaml").read_text(encoding="utf-8"))

    counts: dict[str, int] = {}
    for ops in raw["paths"].values():
        for op in ops.values():
            if not isinstance(op, dict):
                continue
            for param in op.get("parameters") or []:
                counts[param.get("name")] = counts.get(param.get("name"), 0) + 1

    for name, fix in overlay["params"].items():
        assert counts.get(name) == fix["expect"], (
            f"params: {name} occurs {counts.get(name)}x, expected {fix['expect']}"
        )
