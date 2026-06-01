from __future__ import annotations

import re

_HASH_RE = re.compile(r"^[0-9a-f]{24,}$")
_VERB = {"get": "get", "post": "create", "patch": "update", "put": "replace", "delete": "delete"}


def kebab(s: str) -> str:
    s = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", s)
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).lower()
    return re.sub(r"-+", "-", s).strip("-")


def tag_to_group(tag: str) -> str:
    return kebab(tag)


def is_hash_opid(opid: str) -> bool:
    return bool(_HASH_RE.match(opid))


def command_name(opid: str, group: str, method: str, path: str) -> str:
    if is_hash_opid(opid):
        segs = [s for s in path.strip("/").split("/") if not s.startswith("{")]
        verb = _VERB[method]
        tail = kebab(segs[-1]) if segs else ""
        if not tail or tail.rstrip("s") in {t.rstrip("s") for t in group.split("-")}:
            return verb
        return f"{verb}-{tail}"
    cmd = kebab(opid)
    gtokens = {t.rstrip("s") for t in group.split("-")}
    toks = [t for t in cmd.split("-") if t.rstrip("s") not in gtokens]
    return "-".join(toks) or cmd
