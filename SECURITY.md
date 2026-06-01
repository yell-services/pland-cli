# Security policy

## Reporting a vulnerability

Please report suspected vulnerabilities **privately** via a
[GitHub Security Advisory](https://github.com/yell-services/pland-cli/security/advisories/new)
on this repository. Do **not** file a public issue for anything that could
disclose a live API key or customer data.

We'll triage within one week. Fixes that land in `main` get an immediate patch
release.

## Scope

`pland-cli` authenticates to the pland.app API with an `x-API-Key` and can read
and write HR, time-tracking, payroll, absence, invoice and customer data. In
scope:

- API-key leakage from any path the CLI writes to disk, logs, or stdout/stderr
  (including error messages, tracebacks, and `--json` output).
- Reading the key from a place it shouldn't (e.g. echoing it back, embedding it
  in request URLs instead of the header).
- Customer / personal data (names, salaries, absences) leaking into logs,
  caches, or test fixtures.
- TOCTOU / symlink attacks against `~/.config/pland/config.toml`.
- Destructive operations without confirmation: the 3-tier guard (🟢/🟡/🔴) must
  hold; any way to trigger a 🔴 operation without a terminal entry is a reportable
  bug.

Out of scope:

- pland.app's own API behaviour, authentication, or rate limits — report those
  directly to pland.app.
- Issues that require an attacker to already control the user's account or
  `~/.config/pland/`.

## Handling keys and data safely

If you're writing a PR, a bug report, or sharing logs:

- **Never paste a real `<id>:<secret>` API key** into an issue, PR, CI log, or
  transcript. Redact it entirely.
- **Never paste real customer or employee data** — names, salaries, object IDs.
  Use the scrubbed fixtures under `tests/fixtures/` as a model (`"***"`
  placeholders, synthetic IDs).
- The key is read from `PLAND_API_KEY` or the config file and sent only as the
  `x-API-Key` request header. It is never logged. If you find a code path that
  prints it, that's a reportable bug.
- **Windows:** the config file cannot be locked down with POSIX `chmod 600` —
  prefer the `PLAND_API_KEY` environment variable over storing the key on disk.

## Supported versions

This project is pre-1.0. Only the latest released version receives security
fixes.
