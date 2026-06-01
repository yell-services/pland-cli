from pland_cli._codegen.skillgen import build_commands_reference

SPEC = {"paths": {
    "/absences/": {
        "get": {"tags": ["Absences"], "operationId": "listAbsences", "summary": "List absences"},
        "post": {"tags": ["Absences"], "operationId": "createAbsence", "summary": "Create absence"},
    },
}}


def test_reference_groups_commands_by_group():
    md = build_commands_reference(SPEC)
    assert "## absences" in md
    assert "`pland absences list`" in md
    assert "List absences" in md
    assert "`pland absences create`" in md
