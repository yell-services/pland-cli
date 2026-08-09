# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- `openapi.overlay.yaml` — Korrekturschicht über der veröffentlichten Spec, für
  Stellen an denen `docs.pland.app/openapi.yaml` und die Live-API auseinander
  gehen. `load_spec()` merged sie; jeder Eintrag ist gegen
  cloud-api.pland.app verifiziert.
- 12 Endpoints ergänzt, die die API bedient, die Spec aber nicht dokumentiert:
  `custom-fields` (list/count/get-distinct-values), `exports list`,
  `pay-type-templates list` (die Tarifvorlagen aus dem pland-Release vom
  22.05.2026), `users get-own`, `absences count`/`count-new`,
  `tasks count-new`, `time-tracking count-new`, `customer-objects` und
  `service-report get-distinct-values`.
- Python 3.14 als offiziell unterstützte Version deklariert (CI testete sie
  bereits, der Classifier fehlte).

### Changed

- Dev-Toolchain und Lockfile aktualisiert (ruff 0.16, mypy 2.3, pytest 9.1,
  httpx-/click-Stack).
- GitHub Actions auf aktuelle Majors gehoben (checkout v7, setup-uv v9,
  upload-artifact v7, download-artifact v8, action-gh-release v3).
- Dependabot nutzt das `uv`-Ecosystem statt `pip` — damit wird `uv.lock`
  mitgepflegt und nicht nur `pyproject.toml`.
- `mypy` deckt jetzt auch `src/pland_cli/_codegen` ab (war bereits typsauber).
- Ruff-Regelauswahl explizit gepinnt (`select = ["E4","E7","E9","F","I"]`).
  Ohne `select` hing CI am Tool-Default, den ruff zwischen Minors ändert.

### Removed

- 19 Operationen, die die Spec dokumentiert, die API aber nicht bedient — sie
  liefen unweigerlich in einen 400. Ohne `{id}`:
  `absences get-capacity`/`time-frame-check`/`get-types`,
  `complaints get-monitor`, `material-orders get-monitor`,
  `quality-control get-monitor`, `salary get-job-occurrences-without-salaries`,
  `surcharges count`/`get-distinct-values` sowie die GET-Varianten von
  `/invoiceReminders/` und `/invoiceReminders/templates` (die API erlaubt dort
  nur POST). Mit `{id}`: `absences get-affected-jobs`/`get-replacement-jobs`,
  `complaints generate-response`, `jobs get-target-time`, `articles get-user`,
  `quality-control get-object`/`get-object-manager` und `salary get-objects`.
  Die POST-Operationen auf denselben Pfaden bleiben unangetastet.

### Fixed

- `distinct-values` funktioniert wieder: 15 Commands schickten den
  Pflichtparameter als `--field`, die API verlangt `fieldKey` und antwortete
  mit `Missing parameters`. Betrifft assignments, complaints, contacts, credit,
  customers, equipment, equipment-types, invoice, invoice-reminders,
  invoice-reminder-templates, invoice-templates, offers, material-orders,
  service-products und banking-transactions.
- `--sort` ist korrekt dokumentiert: die Spec gibt durchgängig `name:1` als
  Beispiel an, das die API mit `Sorting needs by and direction` ablehnt.
  Richtig ist `{"by":"<feld>","direction":1}` — verifiziert auf allen 35
  GET-Endpoints mit sort-Parameter. Betraf 34 Hilfetexte.
- Hilfetexte behalten ihre Anführungszeichen. Der Renderer ersetzte `"` durch
  `'`, was JSON-Beispiele in der `--help`-Ausgabe unbrauchbar machte.
- Pagination fällt nur noch bei `400` auf "ohne sort" zurück. Vorher löste
  jeder `PlandError` den Fallback aus — ein transienter 500 hätte die stabile
  Sortierung still aufgegeben und damit genau den Datenverlust zurückgeholt,
  den die Injektion verhindert.
- Pagination (`--all`/`paginate`) injiziert jetzt eine stabile Sortierung
  (`sort={"by":"_id","direction":1}`). Ohne sie liefert die API Seiten in
  nicht-deterministischer Reihenfolge, wodurch trotz `_id`-Deduplizierung
  Datensätze still verloren gingen (bei `/invoices/` fehlten 506 von 1705).
  Endpoints ohne sort-Support (400) fallen automatisch auf das alte
  Verhalten zurück.
