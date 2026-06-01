from __future__ import annotations

import json
import sys
from typing import Any

from rich.console import Console

USE_JSON = False
_console = Console()
_err_console = Console(stderr=True)


def set_json(enabled: bool) -> None:
    global USE_JSON
    USE_JSON = enabled


def _dumps(data: Any) -> str:
    return json.dumps(data, indent=2, default=str, ensure_ascii=False)


def out(data: Any) -> None:
    """Erfolgs-Ausgabe. --json: rohes JSON; sonst rich-gehighlightetes JSON."""
    if USE_JSON:
        print(_dumps(data))
    else:
        _console.print_json(_dumps(data))


def out_ok(message: str, data: dict | None = None) -> None:
    if USE_JSON:
        payload: dict = {"ok": True, "message": message}
        if data is not None:
            payload["data"] = data
        print(_dumps(payload))
    else:
        _console.print(f"[green]✓[/green] {message}")
        if data:
            _console.print_json(_dumps(data))


def out_err(status: int, title: str, detail: str, raw: dict | None = None, exit_code: int = 1) -> None:
    if USE_JSON:
        error: dict[str, Any] = {"status": status, "title": title, "detail": detail}
        payload = {"ok": False, "error": error}
        if raw:
            error["raw"] = raw
        print(_dumps(payload), file=sys.stderr)
    else:
        _err_console.print(f"[red]✗[/red] HTTP {status}: {title}")
        if detail:
            _err_console.print(f"  {detail}")
    sys.exit(exit_code)
