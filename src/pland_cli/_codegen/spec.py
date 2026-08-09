from __future__ import annotations

from importlib import resources
from pathlib import Path

import yaml

_METHODS = ("get", "post", "put", "patch", "delete")


def _read(name: str) -> str | None:
    """Paket-Ressource lesen; im editable dev-tree Fallback auf das Repo-Root.

    Beide YAMLs werden nur beim Wheel-Build ins Paket kopiert
    (``[tool.hatch.build.targets.wheel.force-include]``).
    """
    res = resources.files("pland_cli").joinpath(name)
    if res.is_file():
        return res.read_text(encoding="utf-8")
    root = Path(__file__).resolve().parents[3] / name
    return root.read_text(encoding="utf-8") if root.exists() else None


def apply_overlay(spec: dict, overlay: dict) -> dict:
    """Korrekturen aus openapi.overlay.yaml auf die Spec anwenden.

    Drei Sektionen: ``remove`` (Operationen, die die API nicht hat),
    ``rename_params`` (falsch benannte Query-Parameter) und ``paths``
    (Endpoints, die die Spec nicht kennt). Siehe die Kommentare dort.
    """
    paths = spec.setdefault("paths", {})

    for path, methods in (overlay.get("remove") or {}).items():
        ops = paths.get(path)
        if not ops:
            continue
        for method in methods:
            ops.pop(method, None)
        if not any(m in ops for m in _METHODS):
            del paths[path]

    fixes = overlay.get("params") or {}
    for op in (o for ops in paths.values() for o in ops.values() if isinstance(o, dict)):
        for param in op.get("parameters") or []:
            fix = fixes.get(param.get("name"))
            if fix:
                param.update(fix["set"])

    for path, ops in (overlay.get("paths") or {}).items():
        paths.setdefault(path, {}).update(ops)

    return spec


def load_spec(path: Path | None = None) -> dict:
    """Die Spec, gegen die generiert wird — inklusive Overlay.

    Ein explizit übergebener ``path`` wird roh geladen (Test-Fixtures und der
    Vergleich gegen die unveränderte Upstream-Spec).
    """
    if path is not None:
        return yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    raw = _read("openapi.yaml")
    if raw is None:
        raise FileNotFoundError(
            "openapi.yaml nicht gefunden — weder als Paket-Ressource noch im Repo-Root."
        )
    spec = yaml.safe_load(raw)
    overlay = _read("openapi.overlay.yaml")
    return apply_overlay(spec, yaml.safe_load(overlay)) if overlay else spec
