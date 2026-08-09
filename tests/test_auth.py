from click.testing import CliRunner

from pland_cli.cli import main
from pland_cli.core import config as config_mod


def test_auth_set_key_writes_config(tmp_path, monkeypatch):
    monkeypatch.setattr(config_mod, "CONFIG_PATH", tmp_path / "config.toml")
    result = CliRunner().invoke(main, ["auth", "set-key", "--profile", "prod"], input="abc:def\n")
    assert result.exit_code == 0
    assert (tmp_path / "config.toml").exists()


def test_auth_bootstrap_saves_key_not_credentials(tmp_path, monkeypatch):
    monkeypatch.setattr(config_mod, "CONFIG_PATH", tmp_path / "config.toml")
    captured = {}

    def fake_bootstrap(base_url, login_id, password, name="pland-cli"):
        captured["login_id"] = login_id
        captured["password"] = password
        return "newid:newsecret"

    monkeypatch.setattr("pland_cli.auth.bootstrap_api_key", fake_bootstrap)
    result = CliRunner().invoke(
        main,
        ["auth", "bootstrap", "--profile", "prod", "--login-id", "4711"],
        input="mypassword\n",
    )
    assert result.exit_code == 0
    # Logikseitig kamen die Credentials an …
    assert captured["login_id"] == "4711"
    assert captured["password"] == "mypassword"
    # … but ONLY the key is persisted, never the credentials.
    saved = (tmp_path / "config.toml").read_text()
    assert "newid:newsecret" in saved
    assert "mypassword" not in saved
    assert "4711" not in saved
    # Neither the password nor the key itself may appear in the output.
    assert "mypassword" not in result.output
    assert "newsecret" not in result.output


def test_auth_status_reports_source(monkeypatch):
    monkeypatch.setenv("PLAND_API_KEY", "envkey")
    result = CliRunner().invoke(main, ["--json", "auth", "status"])
    assert result.exit_code == 0
    assert "prod" in result.output
