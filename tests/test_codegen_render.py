from pland_cli._codegen.extract import Operation
from pland_cli._codegen.render import _group_var, render_command


def _op(**kw):
    base = dict(operation_id="x", tag="Absences", method="get", path="/absences/",
               group="absences", command="list", summary="List", path_params=[],
               query_params=[], has_json_body=False, is_multipart=False,
               returns_binary=False)
    base.update(kw)
    return Operation(**base)


def test_get_with_query_param_renders_option():
    op = _op(query_params=[{"name": "limit", "schema": {"type": "integer"}, "description": "Max"}])
    code = render_command(op)
    assert '@absences_group.command("list")' in code
    assert '@click.option("--limit"' in code
    # Thin generated command delegates dispatch to run_operation; the rendered
    # text carries the method, the actual client.get(...) lives in runtime.py.
    assert "method='get'" in code


def test_path_param_renders_argument():
    op = _op(command="get", path="/absences/{id}", path_params=[{"name": "id"}])
    code = render_command(op)
    assert '@click.argument("ID")' in code


def test_post_json_body_renders_data_option():
    op = _op(command="create", method="post", path="/absences/", has_json_body=True)
    code = render_command(op)
    assert '@click.option("--data"' in code
    assert "method='post'" in code


def test_multipart_renders_file_option():
    op = _op(command="create", method="post", path="/documents/", is_multipart=True)
    code = render_command(op)
    assert '@click.option("--file"' in code
    # Multipart wiring: the file option value is passed through to run_operation
    # as file_=...; the files={...} httpx call itself lives in runtime.py.
    assert "file_=file_" in code


def test_binary_renders_output_option():
    op = _op(command="export-rows", path="/salaries/export-rows", returns_binary=True)
    code = render_command(op)
    assert '@click.option("--output"' in code


def test_write_method_renders_dry_run():
    op = _op(command="create", method="post", path="/absences/", has_json_body=True)
    code = render_command(op)
    assert '@click.option("--dry-run"' in code
    assert "dry_run=dry_run" in code


def test_get_has_no_dry_run():
    op = _op(query_params=[{"name": "limit", "schema": {"type": "integer"}}])
    code = render_command(op)
    assert "--dry-run" not in code


def test_list_get_renders_all_flag_and_fetch_all():
    # Collection GET (no path params, not binary) gets the pagination flag and
    # threads fetch_all into run_operation so --all pages through everything.
    op = _op(query_params=[{"name": "limit", "schema": {"type": "integer"}}])
    code = render_command(op)
    assert '@click.option("--all", "fetch_all"' in code
    assert "fetch_all=fetch_all" in code


def test_item_get_has_no_all_flag():
    # Item endpoints (an {id} path param) must NOT expose --all.
    op = _op(command="get", path="/absences/{id}", path_params=[{"name": "id"}])
    code = render_command(op)
    assert '"--all"' not in code
    assert "fetch_all=False" in code


def test_binary_get_has_no_all_flag():
    # Binary downloads aren't paginated lists → no --all.
    op = _op(command="export-rows", path="/salaries/export-rows", returns_binary=True)
    code = render_command(op)
    assert '"--all"' not in code
    assert "fetch_all=False" in code


def test_write_method_has_no_all_flag():
    op = _op(command="create", method="post", path="/absences/", has_json_body=True)
    code = render_command(op)
    assert '"--all"' not in code
    assert "fetch_all=False" in code


def test_python_keyword_query_param_renders_compilable_code():
    # "from" is a real API query-param name in 23 operations and a Python
    # keyword → the rendered Python variable must be escaped (from_), otherwise
    # the generated module is a SyntaxError on import.
    op = _op(query_params=[{"name": "from", "schema": {"type": "string"}}])
    code = render_command(op)
    # (a) the rendered command must compile (wrap it in a real group so the
    #     decorator resolves to render.py's actual _group_var name).
    src = (
        'import click\n'
        f'@click.group("g")\ndef {_group_var(op.group)}():\n    pass\n'
        + code
    )
    compile(src, "x", "exec")  # raises SyntaxError if the keyword leaks through
    # (b) the escaped Python variable is used.
    assert "from_" in code
    # (c) the real API query-param name is preserved as the dict KEY.
    assert '"from":' in code


# --- Task 8: Generator embeds --yes, risk=, draftable= -----------------------

def test_render_embeds_risk_and_yes_flag():
    # delete /salaries/{id} -> critical, gets a --yes flag + assume_yes threading.
    code = render_command(
        _op(method="delete", path="/salaries/{id}", tag="Salary",
            command="delete", group="salary", path_params=[{"name": "id"}])
    )
    assert 'risk="critical"' in code
    assert '"--yes"' in code and "assume_yes" in code


def test_render_marks_draftable_delete():
    code = render_command(
        _op(method="delete", path="/invoices/{id}", tag="Invoice",
            command="delete", group="invoice", path_params=[{"name": "id"}])
    )
    assert 'draftable="Invoice"' in code


def test_render_get_has_no_yes_flag():
    code = render_command(
        _op(method="get", path="/salaries/{id}", tag="Salary",
            command="get", group="salary", path_params=[{"name": "id"}])
    )
    assert "--yes" not in code
    assert 'risk="free"' in code


# --- Task 10: risk marker (🟡/🔴) in short_help ------------------------------

def test_render_help_shows_risk_marker():
    # critical -> 🔴 marker in short_help
    code = render_command(
        _op(method="delete", path="/salaries/{id}", tag="Salary",
            command="delete", group="salary", path_params=[{"name": "id"}])
    )
    assert 'short_help=' in code and '🔴' in code
    # confirm -> 🟡 marker in short_help
    code2 = render_command(
        _op(method="delete", path="/documents/{id}", tag="Documents",
            command="delete", group="documents", path_params=[{"name": "id"}])
    )
    assert '🟡' in code2


def test_render_free_has_no_risk_marker():
    # free (e.g. a GET) stays unmarked: no marker, no short_help override.
    code = render_command(
        _op(method="get", path="/salaries/{id}", tag="Salary",
            command="get", group="salary", path_params=[{"name": "id"}])
    )
    assert "🟡" not in code and "🔴" not in code


def test_render_keeps_quotes_and_emoji_literal():
    """Help texts containing " must survive as valid JSON, emojis as UTF-8.

    Ein blindes " -> ' machte JSON-Beispiele im Hilfetext unbrauchbar; ein
    json.dumps without ensure_ascii=False escapes the risk emojis into surrogate
    pairs, which blow up with UnicodeEncodeError when the file is written.
    """
    code = render_command(
        _op(method="get", path="/invoices/", tag="Invoice", command="list",
            group="invoice",
            query_params=[{"name": "sort", "description": 'JSON: {"by":"_id"}'}])
    )
    assert 'help="JSON: {\\"by\\":\\"_id\\"}"' in code
    compile(code, "gen.py", "exec")

    marked = render_command(
        _op(method="delete", path="/salaries/{id}", tag="Salary",
            command="delete", group="salary", path_params=[{"name": "id"}])
    )
    assert "🔴" in marked and "\\ud83d" not in marked
    marked.encode("utf-8")  # Surrogate -> UnicodeEncodeError
