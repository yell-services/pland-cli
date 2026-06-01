from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field

from pland_cli._codegen.naming import command_name, tag_to_group

_METHODS = ("get", "post", "put", "patch", "delete")
_NON_JSON = ("application/pdf", "application/zip", "application/xml",
             "application/octet-stream", "image/jpeg")


@dataclass
class Operation:
    operation_id: str
    tag: str
    method: str
    path: str
    group: str
    command: str
    summary: str
    path_params: list[dict] = field(default_factory=list)
    query_params: list[dict] = field(default_factory=list)
    has_json_body: bool = False
    is_multipart: bool = False
    returns_binary: bool = False


def extract_operations(spec: dict) -> list[Operation]:
    ops: list[Operation] = []
    for path, methods in (spec.get("paths") or {}).items():
        for method, op in (methods or {}).items():
            if method not in _METHODS or not isinstance(op, dict):
                continue
            tag = (op.get("tags") or ["Untagged"])[0]
            group = tag_to_group(tag)
            opid = op.get("operationId", "")
            params = op.get("parameters", [])
            path_params = [p for p in params if p.get("in") == "path"]
            query_params = [p for p in params if p.get("in") == "query"]
            content = (op.get("requestBody") or {}).get("content", {})
            resp_cts = {
                ct
                for r in (op.get("responses") or {}).values()
                for ct in (r.get("content") or {})
            }
            ops.append(
                Operation(
                    operation_id=opid,
                    tag=tag,
                    method=method,
                    path=path,
                    group=group,
                    command=command_name(opid, group, method, path),
                    summary=op.get("summary", "") or (op.get("description") or "")[:80],
                    path_params=path_params,
                    query_params=query_params,
                    has_json_body="application/json" in content,
                    is_multipart="multipart/form-data" in content,
                    returns_binary=any(ct in _NON_JSON for ct in resp_cts),
                )
            )
    _disambiguate(ops)
    return ops


def _disambiguate(ops: list[Operation]) -> None:
    """Resolve ``(group, command)`` collisions deterministically, in place.

    Item- vs. collection-endpoints (differing only by an ``{id}`` path param)
    otherwise collapse onto the same command name, which would hard-fail the
    generator. The naming rule itself stays untouched; collisions are resolved
    here as a post-processing step.
    """
    by_key: dict[tuple[str, str], list[Operation]] = defaultdict(list)
    for op in ops:
        by_key[(op.group, op.command)].append(op)

    for group_ops in by_key.values():
        if len(group_ops) < 2:
            continue
        # First (fewest path params, i.e. usually the collection endpoint) keeps
        # its name; every further op gets a "-by-<last-path-param>" suffix.
        group_ops.sort(key=lambda o: (len(o.path_params), o.path))
        used = {group_ops[0].command}
        for op in group_ops[1:]:
            suffix = op.path_params[-1]["name"] if op.path_params else "x"
            candidate = f"{op.command}-by-{suffix}"
            # If that still collides (multiple ops share the same last param),
            # append a numeric suffix until unique.
            unique = candidate
            n = 2
            while unique in used:
                unique = f"{candidate}-{n}"
                n += 1
            op.command = unique
            used.add(unique)
