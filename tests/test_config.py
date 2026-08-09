import os
from pathlib import Path

import pytest

from pland_cli.core import config as config_mod
from pland_cli.core.config import (
    PROFILES,
    _default_config_path,
    resolve_config,
    save_api_key,
)


def test_default_profile_is_prod(monkeypatch, tmp_path):
    monkeypatch.delenv("PLAND_API_KEY", raising=False)
    monkeypatch.delenv("PLAND_PROFILE", raising=False)
    cfg = resolve_config(config_path=tmp_path / "c.toml")
    assert cfg.profile == "prod"
    assert cfg.base_url == PROFILES["prod"]


def test_cli_arg_overrides_env(monkeypatch, tmp_path):
    monkeypatch.setenv("PLAND_API_KEY", "env-key")
    cfg = resolve_config(api_key="arg-key", config_path=tmp_path / "c.toml")
    assert cfg.api_key == "arg-key"


def test_env_key_used_when_no_arg(monkeypatch, tmp_path):
    monkeypatch.setenv("PLAND_API_KEY", "env-key")
    cfg = resolve_config(config_path=tmp_path / "c.toml")
    assert cfg.api_key == "env-key"


def test_unknown_profile_raises(tmp_path):
    with pytest.raises(ValueError):
        resolve_config(profile="staging", config_path=tmp_path / "c.toml")


def test_save_and_load_key_roundtrip(monkeypatch, tmp_path):
    monkeypatch.delenv("PLAND_API_KEY", raising=False)
    path = tmp_path / "config.toml"
    save_api_key("secret123", profile="prod", path=path)
    cfg = resolve_config(config_path=path)
    assert cfg.api_key == "secret123"
    # POSIX only: Windows has no 0o600 bits via chmod.
    if os.name == "posix":
        assert oct(path.stat().st_mode)[-3:] == "600"


def test_config_path_explicit_override(monkeypatch, tmp_path):
    monkeypatch.setenv("PLAND_CONFIG", str(tmp_path / "x.toml"))
    assert _default_config_path() == tmp_path / "x.toml"


def test_config_path_respects_xdg(monkeypatch, tmp_path):
    monkeypatch.delenv("PLAND_CONFIG", raising=False)
    monkeypatch.setenv("XDG_CONFIG_HOME", str(tmp_path))
    assert _default_config_path() == tmp_path / "pland" / "config.toml"


def test_config_path_windows_uses_appdata(monkeypatch, tmp_path):
    # Patch _is_windows() rather than os.name — the latter would force pathlib
    # to instantiate WindowsPath, which is impossible off Windows.
    monkeypatch.delenv("PLAND_CONFIG", raising=False)
    monkeypatch.delenv("XDG_CONFIG_HOME", raising=False)
    monkeypatch.setattr(config_mod, "_is_windows", lambda: True)
    monkeypatch.setenv("APPDATA", str(tmp_path / "AppData"))
    assert _default_config_path() == tmp_path / "AppData" / "pland" / "config.toml"


def test_config_path_default_is_dotconfig(monkeypatch):
    monkeypatch.delenv("PLAND_CONFIG", raising=False)
    monkeypatch.delenv("XDG_CONFIG_HOME", raising=False)
    monkeypatch.setattr(config_mod, "_is_windows", lambda: False)
    path = _default_config_path()
    assert path == Path.home() / ".config" / "pland" / "config.toml"
