from pland_cli._codegen.security import classify
from pland_cli._codegen.spec import load_spec

_WRITE = {"post", "put", "patch", "delete"}

def _write_ops():
    spec = load_spec()
    for path, methods in (spec.get("paths") or {}).items():
        for method, op in (methods or {}).items():
            if method in _WRITE and isinstance(op, dict):
                tag = (op.get("tags") or ["Untagged"])[0]
                yield method, path, tag

def test_every_write_op_has_valid_level():
    for method, path, tag in _write_ops():
        level = classify(method, path, tag)
        assert level in {"free", "confirm", "critical"}, (method, path, tag, level)

def test_distribution_matches_spec():
    from collections import Counter
    c = Counter(classify(m, p, t) for m, p, t in _write_ops())
    # Verteilung (verifiziert gegen die aktuelle Spec). Bei Spec-Updates bewusst anpassen.
    # 29 -> 30 / 168 -> 167: setToCanceled is critical again (see security.py).
    assert c["critical"] == 30, c
    assert c["free"] == 167, c
    # 123 -> 122: the overlay drops PATCH /company, a 🟡 the API cannot serve.
    assert c["confirm"] == 122, c
    assert sum(c.values()) == 319, c
