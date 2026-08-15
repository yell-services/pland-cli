from __future__ import annotations

from importlib import resources
from pathlib import Path

import yaml

_METHODS = ("get", "post", "put", "patch", "delete")


def _read(name: str) -> str | None:
    """Paket-Ressource lesen; im editable dev-tree Fallback auf das Repo-Root.

    Both YAMLs are copied into the package only on a wheel build
    (``[tool.hatch.build.targets.wheel.force-include]``).
    """
    res = resources.files("pland_cli").joinpath(name)
    if res.is_file():
        return res.read_text(encoding="utf-8")
    root = Path(__file__).resolve().parents[3] / name
    return root.read_text(encoding="utf-8") if root.exists() else None


def apply_overlay(spec: dict, overlay: dict) -> dict:
    """Korrekturen aus openapi.overlay.yaml auf die Spec anwenden.

    Four sections: ``remove`` (operations the API does not serve), ``params``
    (misnamed or misdocumented query parameters), ``paths`` (endpoints the spec
    does not know about, or operations it describes wrongly) and ``schemas``
    (corrections to ``components/schemas``, merged per top-level key so an entry
    fixing ``required`` leaves ``properties`` untouched). See the comments in
    that file.
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

    schemas = spec.setdefault("components", {}).setdefault("schemas", {})
    for name, fields in (overlay.get("schemas") or {}).items():
        schemas.setdefault(name, {}).update(fields)

    return spec


def load_spec(path: Path | None = None) -> dict:
    """The spec used for generation, overlay included.

    An explicitly passed ``path`` is loaded raw — for test fixtures and for
    comparing against the untouched upstream spec.
    """
    if path is not None:
        return yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    raw = _read("openapi.yaml")
    if raw is None:
        raise FileNotFoundError(
            "openapi.yaml not found — neither as a package resource nor at the repo root."
        )
    spec = yaml.safe_load(raw)
    overlay = _read("openapi.overlay.yaml")
    return apply_overlay(spec, yaml.safe_load(overlay)) if overlay else spec
