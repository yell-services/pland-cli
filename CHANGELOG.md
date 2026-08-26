# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.7.1] - 2026-08-26

### Fixed

- The four faktura send routes take `sendToEmail` for the recipient, not the
  published `overrideEmail`. The API ignores the documented name — and does not
  fail on it: a document with no recipient of its own comes back under `skipped`
  with nothing sent, while a document that has one delivers **to the customer**.
  A recipient override that silently mails the customer is worse than none, and
  it sent two 2024 documents to live customers before the cause was found.
  Verified on `/stornos/send` and `/offers/send`; on `/credits/send` and
  `/assignmentConfirmations/send` only the ignored `overrideEmail` is verified,
  since probing the fix there would have risked another live mail. The overlay
  comments record which is which.
- `credit send` takes `fakturaDocumentIds`, not the published `ids` — the API
  says so in its 400.

### Documented

- A send response never tells you who received the mail. `success` means the API
  accepted the call, nothing more; `statusTags[].recipient` and the logbuch entry
  `activity_sent_faktura_document_to_email` are the only proof. Testing a send
  safely needs a document with no address anywhere on it or its customer — and
  `/offers/send` fixes a draft offer as a side effect, so drafts are not the
  harmless choice they look like.

## [0.7.0] - 2026-08-26

### Removed

- `company update`. The route is registered but has no handler behind it —
  `PATCH /company` answers "CompanyController:update is not resolvable", with an
  unchanged body just as much as a changed one, and `PUT` confirms the router
  knows the method ("Must be one of: GET, PATCH"). The command could only ever
  collect its 🟡 confirmation and then fail, so the overlay drops it. Company
  settings are read-only over the API; `company get-info` still reads them.

### Documented

- Orphaned stornos break the document number range, not just `referenceId`. The
  unique index covers the number, and the next one is `max(existing) + 1`, so a
  record the collection keeps but no query returns pins that maximum and every
  further cancel — on any invoice — repeats the same `E11000`. Neither `list`
  (with or without a `documentNumber` filter), `get-distinct-values`, nor
  `search perform-global` reveals it, so there is no id to delete and no way to
  move the counter past it either.
- `settings.<documentType>.nextNumber` is the value the range starts at when the
  prefix rolls over, not the running counter, and it is never advanced. Raising
  it in the web UI is the way out of a jammed range — the API cannot write it,
  the UI can.

## [0.6.0] - 2026-08-16

### Added

- `assignment-confirmations list` finds confirmations that have no collection
  route, by walking the offers they were generated from and reading each one's
  `referencedFakturaDocuments`. `--offer-id` skips the walk. One request per
  offer, since no bulk route exists (~20 s at a few hundred), and any offer
  that cannot be read is reported on stderr rather than silently shortening the
  result. Found all 14 confirmations in a live company across 221 offers.
- `invoice get-referenced-faktura-documents`. The spec documents
  `referencedFakturaDocuments` on six faktura types but not on invoices, where
  the API serves it just the same — verified against a control probe on the
  same resource. It is the second route to an assignment confirmation, since
  the invoice raised from an offer references it too.

## [0.5.0] - 2026-08-15

### Changed

- The docs no longer claim 🔴 cannot be cleared without a terminal. `--confirm`
  has done exactly that since it was added, for a caller with the user's
  explicit go, and four places still said otherwise: two in the skill, the
  `--yes` help text, and the guard's own no-TTY error. That error now names the
  token to pass. Wrong in the dangerous direction — a reader took 🔴 for
  human-enforced and relied on it.
- **Breaking:** `--yes` and `--confirm` are gone from free commands, where they
  cleared nothing and implied a confirmation that never happened. They stay on
  all 152 gated writes; the other 168 keep `--dry-run`. A script passing `--yes`
  to a free command now fails with "no such option" — notably
  `invoice set-canceled`, free since this release. A conformance test pins the
  pairing in both directions.

### Added

- `invoice-storno list`, `count` and `get-distinct-values`. The spec reaches a
  storno only through `/stornos/{id}`, and nothing hands out that id: cancelling
  an invoice creates a storno record behind the scenes while the invoice keeps
  `stornoId: null`. A storno raised in error could therefore be neither found
  nor deleted. The collection turns out to be served but undocumented — verified
  2026-08-15, 200 with 364 records, against a control probe on the same resource
  that reports "Failed to parse Id". Same dead end, and same fix, as the
  `/invoiceReminders/` entry.

### Changed

- `invoice set-canceled` is no longer 🔴 critical, it runs unprompted. Cancelling
  stamps `canceledDate` and removes nothing — the invoice keeps its number and
  stays in the ledger. The critical tier demanded a human at a terminal, which
  blocked every non-interactive caller from an everyday bookkeeping step.

### Fixed

- `invoice set-canceled` works at all. Verified against the live API on
  2026-08-15 by cancelling a real 0 EUR invoice: the published body is wrong
  twice over. The field is `fakturaDocumentIds`, not `ids` (which earns
  "Required parameters are: fakturaDocumentIds"), and `canceledAtDate` is
  mandatory despite being documented as optional and nullable — leaving it out
  makes the API fail with a PHP type error. Corrected in the overlay, and the
  body is now reachable as `pland schema SetInvoicesCanceledRequest`.
- `invoice create` documents `address` as required. Without it the API answers
  "Missing parameters. Required parameters are: customerId, positions, currency,
  issuedOn, address", though upstream lists only the other five.
- The overlay can correct operations and schemas, not just add missing routes.
  A `paths` entry for a documented path replaces that operation; the new
  `schemas` section merges into `components/schemas` per top-level key. Both
  keep the drift guard: an entry that comes to match upstream fails the suite,
  which is when it should be deleted.

- `invoice-reminders list` exists again. The overlay dropped `GET /invoiceReminders/`
  as a route the API does not serve, but a plain GET returns the reminder list — and
  it is the only way to reach a reminder at all, because an invoice carries no
  reminder id, just `remindedDate` and `newestReminderTitle`. Without it, a reminder
  raised in error could be neither found nor deleted. The sibling entries in that
  overlay block (`/surcharges/count`, `/surcharges/distinctValues`,
  `/invoiceReminders/templates`) were re-probed and are correct: they stay removed.

## [0.3.0] - 2026-08-14

### Added

- `--dry-run` now reports the full target URL, not just the request path, so a
  preview tells prod from beta before a write lands in payroll or invoicing. A
  multipart upload also names the file. The output gained a `dry_run: true` marker
  so a caller can tell a preview from an API response.
- `documents upload` accepts `--dry-run`. Being hand-written rather than generated,
  it never passed through the shared hook and was the only one of the 522 commands
  that could write without a preview. A conformance test now fails if any write
  command lacks the flag.
- `batch run --dry-run --json` lists every request the file would send under
  `operations`, each in the same shape a single command's dry run prints. It used
  to report only how many entries there were, which an agent cannot check against
  what it meant to do. The counter moved to `count`.
- `pland batch run --file <json>` runs many operations behind a single risk gate,
  derived as the maximum risk across the file's entries. Prints a plan first,
  continues past individual failures, exits 1 if any entry failed.

### Fixed

- A path argument containing `..` retargeted the request at a different endpoint
  than the one the guard classified. `holiday delete` is 🟢, but
  `pland holiday delete '../../users/<id>'` was sent as `DELETE /users/<id>` — a
  🔴 endpoint — because httpx resolves dot segments client-side. `PlandClient`
  now refuses such a path before the request leaves, which covers every generated
  command, `batch run` and any future caller at once.
- A `Retry-After` header in its HTTP-date form (RFC 7231 allows it) raised
  `ValueError` in the middle of a 429 retry. It is parsed now, and every retry
  delay is clamped to at most 60 s so a large value cannot hang the CLI.
- Confirmation prompts went to stdout, so under `--json` a 🟡 or 🔴 prompt at a
  terminal made the result unparseable. They go to stderr now; the risk tiers and
  the fail-closed no-TTY behaviour are unchanged.
- The last German user-facing strings — two guard prompts and seven `--help`
  texts — are English, completing the sweep started in 849d7d5.
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

[0.7.1]: https://github.com/yell-services/pland-cli/compare/v0.7.0...v0.7.1
[0.7.0]: https://github.com/yell-services/pland-cli/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/yell-services/pland-cli/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/yell-services/pland-cli/compare/v0.4.0...v0.5.0
[0.4.0]: https://github.com/yell-services/pland-cli/compare/v0.3.0...v0.4.0
[0.3.0]: https://github.com/yell-services/pland-cli/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/yell-services/pland-cli/compare/v0.1.0...v0.2.0
