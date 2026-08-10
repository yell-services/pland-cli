# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `pland batch run --file <json>` runs many operations behind a single risk gate,
  derived as the maximum risk across the file's entries. Prints a plan first,
  continues past individual failures, exits 1 if any entry failed.

### Fixed

- 42 commands raised `TypeError` on invocation instead of doing anything. The
  generator wrote camelCase identifiers for path parameters (`userId`) while
  Click derives lowercase ones from the argument declaration (`userid`), so the
  value never reached the function. Affected every command with a camelCase path
  parameter, among them `salary get-user-salaries`, `jobs list-for-user`,
  `time-tracking list-from-user`, `users get-by-number` and
  `client upload-documents`. Command names, arguments and help output are
  unchanged — only the generated identifiers.
- `test_generated_conformance.py` now checks that every generated
  `@click.argument` has a matching function parameter. The previous checks
  covered module count, importability and command count, none of which can see
  a signature mismatch.

## [0.2.0] - 2026-08-09

Two silent data-loss bugs in `--all` and a batch of commands that could never
have worked. If you script against this CLI, read the Removed and Fixed
sections — some call sites need adjusting.

### Added

- `openapi.overlay.yaml` — a correction layer over the published spec, for the
  places where `docs.pland.app/openapi.yaml` and the live API disagree.
  `load_spec()` merges it on top; every entry is verified against
  cloud-api.pland.app. See CONTRIBUTING.md.
- 12 endpoints the API serves but does not document: `custom-fields`
  (list/count/get-distinct-values), `exports list`, `pay-type-templates list`
  (the collective-agreement templates from the pland release of 2026-05-22),
  `users get-own`, `absences count`/`count-new`, `tasks count-new`,
  `time-tracking count-new`, plus `customer-objects` and
  `service-report get-distinct-values`.
- Python 3.14 declared as officially supported (CI already tested it, the
  classifier was missing).

### Changed

- **Breaking:** `distinct-values` commands take `--fieldKey` instead of
  `--field`. See Fixed below.
- Dev toolchain and lockfile updated (ruff 0.16, mypy 2.3, pytest 9.1,
  httpx/click stack).
- GitHub Actions raised to current majors (checkout v7, setup-uv v9,
  upload-artifact v7, download-artifact v8, action-gh-release v3).
- Dependabot uses the `uv` ecosystem instead of `pip`, so `uv.lock` is kept
  up to date and not just `pyproject.toml`.
- `mypy` now also covers `src/pland_cli/_codegen` (it was already type-clean).
- Ruff rule selection pinned explicitly (`select = ["E4","E7","E9","F","I"]`).
  Without `select`, CI depended on the tool default, which ruff reshuffles
  between minor releases.

### Removed

- **Breaking:** 19 operations the spec documents but the API does not serve —
  they always ran into a 400. Without `{id}`:
  `absences get-capacity`/`time-frame-check`/`get-types`,
  `complaints get-monitor`, `material-orders get-monitor`,
  `quality-control get-monitor`, `salary get-job-occurrences-without-salaries`,
  `surcharges count`/`get-distinct-values`, and the GET variants of
  `/invoiceReminders/` and `/invoiceReminders/templates` (the API only allows
  POST there). With `{id}`: `absences get-affected-jobs`/`get-replacement-jobs`,
  `complaints generate-response`, `jobs get-target-time`, `articles get-user`,
  `quality-control get-object`/`get-object-manager`, and `salary get-objects`.
  The POST operations on those same paths are untouched.

### Fixed

- `--all` dropped more than half the data. The offset advanced by the
  *requested* page size, but some endpoints cap server-side regardless of
  `limit` (`/salaries/` at 200). With `page_size=500` every round skipped 300
  rows: measured 9800 instead of 24483 records, a 60 % loss. The offset now
  advances by the number of rows actually returned. A page ceiling aborts with
  an error rather than returning a partial result, should a server cap the
  offset and keep handing back the same page.
- Pagination (`--all`/`paginate`) now injects a stable sort
  (`sort={"by":"_id","direction":1}`). Without it the API returns pages in
  non-deterministic order, so records were silently lost despite `_id`
  deduplication (506 of 1705 missing on `/invoices/`). Endpoints that reject
  the sort parameter (400) fall back to the previous behaviour.
- That fallback now triggers on `400` only. Previously any `PlandError` caused
  it — a transient 500 would have silently abandoned the stable sort, bringing
  back the very data loss the injection prevents.
- **Breaking:** `distinct-values` works again. 15 commands sent the required
  parameter as `--field`; the API expects `fieldKey` and answered with
  `Missing parameters`. Affects assignments, complaints, contacts, credit,
  customers, equipment, equipment-types, invoice, invoice-reminders,
  invoice-reminder-templates, invoice-templates, offers, material-orders,
  service-products and banking-transactions.
- `--sort` is documented correctly. The spec gives `name:1` as the example
  throughout, which the API rejects with `Sorting needs by and direction`. The
  correct form is `{"by":"<field>","direction":1}` — verified on all 35 GET
  endpoints carrying a sort parameter. 34 help texts were affected.
- Help texts keep their double quotes. The renderer replaced `"` with `'`,
  which made JSON examples in `--help` output unusable.

[0.2.0]: https://github.com/yell-services/pland-cli/compare/v0.1.0...v0.2.0
