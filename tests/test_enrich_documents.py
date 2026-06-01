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


def test_doc_params_helper():
    from pland_cli.enrichment.documents import _doc_params
    assert _doc_params("faktura") == {"type": "faktura"}
    assert _doc_params("regular") == {}
