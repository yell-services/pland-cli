from __future__ import annotations

from importlib import resources
from pathlib import Path

import yaml


def load_spec(path: Path | None = None) -> dict:
    if path is not None:
        return yaml.safe_load(Path(path).read_text())
    res = resources.files("pland_cli").joinpath("openapi.yaml")
    if res.is_file():
        return yaml.safe_load(res.read_text())
    # dev-tree fallback: openapi.yaml lives at repo root, force-included only on
    # wheel build, so the package resource is absent from the editable src tree.
    root = Path(__file__).resolve().parents[3] / "openapi.yaml"
    return yaml.safe_load(root.read_text())
