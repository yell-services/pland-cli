from pland_cli._codegen.naming import command_name, is_hash_opid, kebab, tag_to_group


def test_tag_to_group_kebab():
    assert tag_to_group("Time Tracking") == "time-tracking"
    assert tag_to_group("Pay Types") == "pay-types"
    assert tag_to_group("Absences") == "absences"


def test_kebab_strips_non_alphanumeric():
    # Klammern (und sonstige Nicht-Alphanumerische) werden zu Bindestrichen
    # normalisiert, sonst entsteht ein nicht-importierbarer Modulname.
    assert kebab("Chat (legacy)") == "chat-legacy"
    # Bestehende Tags bleiben unverändert:
    assert kebab("Time Tracking") == "time-tracking"
    assert kebab("Pay Types") == "pay-types"
    assert kebab("API Keys") == "api-keys"


def test_tag_to_group_yields_valid_module_identifier():
    # group.replace("-", "_") muss ein gültiger Python-Identifier sein,
    # damit das generierte Modul ein importierbarer Dateiname ist.
    modname = tag_to_group("Chat (legacy)").replace("-", "_")
    assert modname == "chat_legacy"
    assert modname.isidentifier()


def test_command_name_strips_tag_noun():
    assert command_name("listAbsences", "absences", "get", "/absences/") == "list"
    assert command_name("createAbsence", "absences", "post", "/absences/") == "create"
    assert command_name("approveMultipleAbsences", "absences", "post", "/absences/approve-multiple") == "approve-multiple"


def test_command_name_keeps_distinct_verb():
    assert command_name("getUserById", "users", "get", "/users/{id}") == "get-by-id"


def test_hash_opid_detected():
    assert is_hash_opid("1c429a7c57a21ce6ee055208ff6bb54d")
    assert not is_hash_opid("createAbsence")


def test_command_name_hash_fallback_uses_path():
    name = command_name("1c429a7c57a21ce6ee055208ff6bb54d", "stornos", "post", "/stornos/{id}/addDocuments")
    assert name == "create-add-documents"
