# Contributing

Issues and PRs welcome. This is an **inofficial, community** client for the
pland.app API — not affiliated with pland.app.

## Before opening a PR

Run the same checks CI runs (Python 3.11+, [uv](https://docs.astral.sh/uv/)):

```sh
uv sync --extra dev
uv run pytest -q -m "not live"
uv run ruff check src tests
uv run mypy src/pland_cli/core src/pland_cli/utils src/pland_cli/enrichment
```

A PR that fails any of them will not merge.

## Generated vs. hand-written code

`src/pland_cli/commands/` is **auto-generated** from `openapi.yaml` — do not edit
it by hand. To pick up an API change, regenerate:

```sh
curl -sL https://docs.pland.app/openapi.yaml -o openapi.yaml
uv run python -m pland_cli._codegen.generate   # rebuilds commands/
uv run python -m pland_cli._codegen.skillgen   # rebuilds skills/references/commands.md
uv run pytest -q
```

Behaviour that can't be expressed in the spec (broken server-side filters,
client-side pagination, convenience flows) lives in `src/pland_cli/enrichment/`
as hand-maintained **enriched commands**, registered via the `@enrich` registry.
That's the right place for new logic.

## No private data

Never commit real API keys, customer names, salaries, object IDs, or any
pland.app account data — not in code, tests, fixtures, or commit messages. Test
fixtures under `tests/fixtures/` are scrubbed (`"***"` names, synthetic IDs);
keep them that way. See [SECURITY.md](./SECURITY.md).

## Commit style

Short, imperative subject line. Reference the issue in the body, not the subject.
Keep the working tree green (`pytest`/`ruff`/`mypy`) on every commit.
