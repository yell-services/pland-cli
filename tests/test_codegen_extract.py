from collections import Counter
from pathlib import Path

from pland_cli._codegen.extract import extract_operations
from pland_cli._codegen.spec import load_spec

_REAL_SPEC = Path(__file__).resolve().parents[1] / "openapi.yaml"

SPEC = {
    "paths": {
        "/absences/": {
            "get": {
                "tags": ["Absences"],
                "operationId": "listAbsences",
                "summary": "List absences",
                "parameters": [
                    {"name": "limit", "in": "query", "required": False,
                     "schema": {"type": "integer", "default": 100}},
                ],
            },
            "post": {
                "tags": ["Absences"],
                "operationId": "createAbsence",
                "summary": "Create absence",
                "requestBody": {"content": {"application/json": {"schema": {"$ref": "#/c/Absence"}}}},
            },
        },
        "/documents/": {
            "post": {
                "tags": ["Documents"],
                "operationId": "createDocument",
                "requestBody": {"content": {"multipart/form-data": {"schema": {"type": "object"}}}},
            }
        },
        "/salaries/export-rows": {
            "get": {
                "tags": ["Salary"],
                "operationId": "exportSalaryRows",
                "responses": {"200": {"content": {"application/zip": {}}}},
            }
        },
    }
}


def test_extracts_all_operations():
    ops = extract_operations(SPEC)
    assert len(ops) == 4


def test_query_param_and_group():
    op = next(o for o in ops_by_id(SPEC)["listAbsences"])
    assert op.group == "absences"
    assert op.command == "list"
    assert op.query_params[0]["name"] == "limit"


def test_json_body_flag():
    op = ops_by_id(SPEC)["createAbsence"][0]
    assert op.has_json_body is True
    assert op.is_multipart is False


def test_multipart_flag():
    op = ops_by_id(SPEC)["createDocument"][0]
    assert op.is_multipart is True


def test_binary_response_flag():
    op = ops_by_id(SPEC)["exportSalaryRows"][0]
    assert op.returns_binary is True


def ops_by_id(spec):
    out: dict = {}
    for op in extract_operations(spec):
        out.setdefault(op.operation_id, []).append(op)
    return out


def test_real_spec_command_names_are_unique():
    spec = load_spec(_REAL_SPEC)
    ops = extract_operations(spec)
    assert len(ops) == 529
    counts = Counter((op.group, op.command) for op in ops)
    collisions = {key: n for key, n in counts.items() if n > 1}
    assert collisions == {}, f"Namens-Kollisionen verbleiben: {collisions}"


def test_collision_disambiguated_with_by_param():
    # Mirrors the two real-spec collisions: collection vs. item endpoints that differ
    # only by an "{id}" path param. Real spec uses hash operationIds, so the names are
    # method/path-derived ("get", "create-pdf"). The item endpoint gets the "-by-id"
    # suffix; the collection endpoint keeps the base name.
    spec = {
        "paths": {
            "/payments/": {
                "get": {"tags": ["Payments"], "operationId": "7d2b3b9ad70710384ee87de777654316",
                        "summary": ""},
            },
            "/payments/{id}": {
                "get": {
                    "tags": ["Payments"],
                    "operationId": "660a7018c8f291ca4187b111332b5053",
                    "summary": "",
                    "parameters": [{"name": "id", "in": "path"}],
                },
            },
            "/stornos/pdf": {
                "post": {"tags": ["Invoice Storno"], "operationId": "23d51d8cb626e8fc5aae330d0a42b711",
                         "summary": ""},
            },
            "/stornos/{id}/pdf": {
                "post": {
                    "tags": ["Invoice Storno"],
                    "operationId": "88d87c093f9cf13d64ef6d5b65b68aab",
                    "summary": "",
                    "parameters": [{"name": "id", "in": "path"}],
                },
            },
        }
    }
    by_path = {op.path: op for op in extract_operations(spec)}
    assert by_path["/payments/"].command == "get"
    assert by_path["/payments/{id}"].command == "get-by-id"
    assert by_path["/stornos/pdf"].command == "create-pdf"
    assert by_path["/stornos/{id}/pdf"].command == "create-pdf-by-id"


def test_collision_same_last_param_gets_numeric_suffix():
    # Three item-endpoints that all resolve to the same base command AND share the
    # same last path param ("id"). The first keeps the base name, the next gets the
    # "-by-id" suffix, and any further duplicate must fall back to a numeric suffix.
    def item(path):
        return {
            path: {
                "get": {
                    "tags": ["Things"],
                    "operationId": "a0a1b2c3d4e5f60718293a4b5c",  # hash → path-derived
                    "summary": "",
                    "parameters": [{"name": "id", "in": "path"}],
                },
            }
        }

    spec = {"paths": {}}
    for p in ("/other/{id}/things", "/sub/{id}/things", "/things/{id}"):
        spec["paths"].update(item(p))

    commands = sorted(op.command for op in extract_operations(spec))
    assert len(set(commands)) == 3
    assert commands == ["get", "get-by-id", "get-by-id-2"]


def test_operation_carries_original_tag():
    spec = {"paths": {"/timetracking/{id}/cancel": {"post": {
        "tags": ["Time Tracking"], "operationId": "cancelTt", "summary": "Cancel"}}}}
    from pland_cli._codegen.extract import extract_operations
    op = extract_operations(spec)[0]
    assert op.tag == "Time Tracking"
    assert op.group == "time-tracking"
