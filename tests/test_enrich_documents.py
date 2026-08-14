import httpx
from click.testing import CliRunner

from pland_cli.cli import main


def _mk(handler):
    from pland_cli.core.client import PlandClient
    from pland_cli.core.config import Config
    return PlandClient(
        Config(base_url="https://api.test/v2", api_key="k", profile="prod"),
        transport=httpx.MockTransport(handler),
    )


def test_document_upload_sends_faktura_type(tmp_path, monkeypatch):
    pdf = tmp_path / "rechnung.pdf"
    pdf.write_bytes(b"%PDF-1.4 test")
    seen = {}

    def handler(request):
        seen["type"] = request.url.params.get("type")
        seen["is_multipart"] = request.headers["content-type"].startswith("multipart/")
        return httpx.Response(200, json={"_id": "doc1"})

    import pland_cli.enrichment.documents as doc
    monkeypatch.setattr(doc, "get_client", lambda ctx: _mk(handler))

    result = CliRunner().invoke(
        main, ["--json", "documents", "upload", str(pdf), "--kind", "faktura"]
    )
    assert result.exit_code == 0
    assert seen["type"] == "faktura"
    assert seen["is_multipart"] is True


def test_document_upload_regular_sends_no_type(tmp_path, monkeypatch):
    pdf = tmp_path / "anhang.pdf"
    pdf.write_bytes(b"%PDF-1.4 test")
    seen = {}

    def handler(request):
        seen["type"] = request.url.params.get("type")
        return httpx.Response(200, json={"_id": "doc2"})

    import pland_cli.enrichment.documents as doc
    monkeypatch.setattr(doc, "get_client", lambda ctx: _mk(handler))

    result = CliRunner().invoke(main, ["--json", "documents", "upload", str(pdf)])
    assert result.exit_code == 0
    assert seen["type"] is None


def test_document_upload_sends_user_id_form_field(tmp_path, monkeypatch):
    pdf = tmp_path / "rechnung.pdf"
    pdf.write_bytes(b"%PDF-1.4 test")
    seen = {}

    def handler(request):
        body = request.content.decode("latin-1")
        seen["has_user_field"] = 'name="userId"' in body
        seen["has_user_value"] = "u42" in body
        return httpx.Response(200, json={"_id": "doc3"})

    import pland_cli.enrichment.documents as doc
    monkeypatch.setattr(doc, "get_client", lambda ctx: _mk(handler))

    result = CliRunner().invoke(
        main, ["--json", "documents", "upload", str(pdf), "--user-id", "u42"]
    )
    assert result.exit_code == 0
    assert seen["has_user_field"] is True
    assert seen["has_user_value"] is True


def test_document_upload_dry_run_sends_nothing(tmp_path, monkeypatch):
    """The one hand-written write command has to preview like every generated one."""
    import json

    pdf = tmp_path / "lohnabrechnung.pdf"
    pdf.write_bytes(b"%PDF-1.4 test")

    def handler(request):  # pragma: no cover - reaching this IS the failure
        raise AssertionError(f"a dry run sent {request.method} {request.url}")

    import pland_cli.enrichment.documents as doc
    monkeypatch.setattr(doc, "get_client", lambda ctx: _mk(handler))
    monkeypatch.setenv("PLAND_BASE_URL", "https://api.test/v2")

    result = CliRunner().invoke(
        main,
        ["--json", "documents", "upload", str(pdf), "--kind", "faktura", "--dry-run"],
    )
    assert result.exit_code == 0
    payload = json.loads(result.stdout)
    assert payload["method"] == "POST"
    assert payload["url"] == "https://api.test/v2/documents/"
    assert payload["params"] == {"type": "faktura"}
    assert payload["file"] == "lohnabrechnung.pdf"


def test_document_upload_dry_run_needs_no_api_key(tmp_path, monkeypatch):
    """A preview must work before a key exists — get_client is never reached."""
    pdf = tmp_path / "anhang.pdf"
    pdf.write_bytes(b"%PDF-1.4 test")

    def _no_client(ctx):  # pragma: no cover - reaching this IS the failure
        raise AssertionError("dry run resolved a client")

    import pland_cli.enrichment.documents as doc
    monkeypatch.setattr(doc, "get_client", _no_client)

    result = CliRunner().invoke(main, ["--json", "documents", "upload", str(pdf), "--dry-run"])
    assert result.exit_code == 0


def test_doc_params_helper():
    from pland_cli.enrichment.documents import _doc_params
    assert _doc_params("faktura") == {"type": "faktura"}
    assert _doc_params("regular") == {}
