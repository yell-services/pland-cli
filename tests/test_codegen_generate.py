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

    The package resources ``pland_cli/openapi.yaml`` and
    ``pland_cli/openapi.overlay.yaml`` are absent from the src tree
    (force-included only on wheel build), so load_spec falls back to the repo
    root. Upstream ships 421 paths; das Overlay streicht die, die die API nicht
    bedient, und ergänzt die, die sie undokumentiert bedient.
    """
    root = Path(__file__).resolve().parents[1]
    raw = load_spec(root / "openapi.yaml")
    assert len(raw["paths"]) == 421

    overlay = yaml.safe_load((root / "openapi.overlay.yaml").read_text(encoding="utf-8"))
    methods = {"get", "post", "put", "patch", "delete"}
    # Ein Pfad verschwindet nur, wenn `remove` seine letzte Operation nimmt.
    dropped = sum(1 for path, gone in overlay["remove"].items()
                  if not (set(raw["paths"][path]) & methods) - set(gone))
    assert len(load_spec()["paths"]) == len(raw["paths"]) - dropped + len(overlay["paths"])


def test_overlay_removes_renames_and_adds():
    """Die drei Overlay-Sektionen greifen auf der echten Spec."""
    spec = load_spec()
    # remove: Route existiert live nicht ("Failed to parse Id: count")
    assert "/surcharges/count" not in spec["paths"]
    # remove: nur GET fällt weg, POST bleibt stehen
    assert set(spec["paths"]["/invoiceReminders/"]) == {"post"}
    # params: die API verlangt fieldKey, die Spec schrieb field
    names = [p["name"] for p in spec["paths"]["/invoices/distinctValues"]["get"]["parameters"]]
    assert names == ["fieldKey"]
    # params: das sort-Beispiel der Spec ("name:1") quittiert die API mit 400
    sort = next(p for p in spec["paths"]["/invoices/"]["get"]["parameters"]
                if p["name"] == "sort")
    assert '{"by"' in sort["description"]
    # paths: undokumentierte Ressource
    assert spec["paths"]["/payTypeTemplates/"]["get"]["tags"] == ["Pay Type Templates"]


def test_overlay_is_a_pure_correction_layer():
    """Jeder Overlay-Eintrag muss die echte Spec treffen.

    Fixt pland.app einen Punkt upstream, schlägt das hier fehl statt still
    ins Leere zu laufen — genau dann gehört der Eintrag gelöscht.
    """
    root = Path(__file__).resolve().parents[1]
    raw = load_spec(root / "openapi.yaml")
    overlay = yaml.safe_load((root / "openapi.overlay.yaml").read_text(encoding="utf-8"))

    for path, methods in overlay["remove"].items():
        assert path in raw["paths"], f"remove: {path} gibt es upstream nicht mehr"
        for method in methods:
            assert method in raw["paths"][path], f"remove: {method} {path} ist weg"

    for path in overlay["paths"]:
        assert path not in raw["paths"], f"paths: {path} ist upstream dokumentiert"


def test_overlay_params_still_apply():
    """Die Parameter-Korrekturen greifen genau so oft wie dokumentiert.

    ``expect`` sichert die namensbasierten Regeln gegen stille Ausweitung ab:
    fuehrt upstream denselben Parameternamen anderswo ein oder korrigiert die
    Stellen, weicht die Trefferzahl ab und der Eintrag will neu bewertet werden.
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
            f"params: {name} kommt {counts.get(name)}x vor, erwartet {fix['expect']}"
        )
