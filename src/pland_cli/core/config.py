from __future__ import annotations

import os
import tomllib
from dataclasses import dataclass
from pathlib import Path

PROFILES = {
    "prod": "https://cloud-api.pland.app/v2",
    "beta": "https://beta-api.pland.app/v2",
    "local": "http://localhost:3000/v2",
}
DEFAULT_PROFILE = "prod"


def _is_windows() -> bool:
    return os.name == "nt"


def _default_config_path() -> Path:
    """Plattformgerechter Pfad zur config.toml.

    Reihenfolge: explizites ``PLAND_CONFIG`` > ``XDG_CONFIG_HOME`` (Linux/macOS)
    > ``%APPDATA%`` (Windows) > ``~/.config`` (Default). So bleibt der bisherige
    Linux/macOS-Pfad erhalten, Windows nutzt den OS-idiomatischen Ort.
    """
    override = os.environ.get("PLAND_CONFIG")
    if override:
        return Path(override)
    xdg = os.environ.get("XDG_CONFIG_HOME")
    if xdg:
        return Path(xdg) / "pland" / "config.toml"
    if _is_windows():
        appdata = os.environ.get("APPDATA")
        base = Path(appdata) if appdata else Path.home() / ".config"
        return base / "pland" / "config.toml"
    return Path.home() / ".config" / "pland" / "config.toml"


CONFIG_PATH = _default_config_path()


@dataclass
class Config:
    base_url: str
    api_key: str
    profile: str


def load_config_file(path: Path = CONFIG_PATH) -> dict:
    if not path.exists():
        return {}
    with path.open("rb") as fh:
        return tomllib.load(fh)


def resolve_config(
    profile: str | None = None,
    api_key: str | None = None,
    config_path: Path | None = None,
) -> Config:
    cfg = load_config_file(config_path if config_path is not None else CONFIG_PATH)
    profile = (
        profile
        or os.environ.get("PLAND_PROFILE")
        or cfg.get("default_profile")
        or DEFAULT_PROFILE
    )
    if profile not in PROFILES:
        raise ValueError(
            f"Unbekanntes Profil: {profile!r} (erlaubt: {', '.join(PROFILES)})"
        )
    prof_cfg = cfg.get("profiles", {}).get(profile, {})
    base_url = os.environ.get("PLAND_BASE_URL") or prof_cfg.get("base_url") or PROFILES[profile]
    key = api_key or os.environ.get("PLAND_API_KEY") or prof_cfg.get("api_key") or ""
    return Config(base_url=base_url, api_key=key, profile=profile)


def save_api_key(api_key: str, profile: str = DEFAULT_PROFILE, path: Path | None = None) -> Path:
    import tomli_w

    path = path if path is not None else CONFIG_PATH
    cfg = load_config_file(path)
    cfg.setdefault("profiles", {}).setdefault(profile, {})["api_key"] = api_key
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as fh:
        tomli_w.dump(cfg, fh)
    # POSIX: Key nur für den User lesbar machen. Auf Windows kennt chmod keine
    # echten POSIX-Bits (no-op/Read-only) — dort ist PLAND_API_KEY der sichere
    # Weg. Fehler hier dürfen das Speichern nie verhindern.
    try:
        path.chmod(0o600)
    except (OSError, NotImplementedError):
        pass
    return path
