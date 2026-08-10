---
name: pland-cli
description: Use when interacting with the pland.app API — HR, time tracking, payroll/salaries, absences, invoices, offers, customer objects, quality control, documents. Provides the `pland` CLI (522 commands across 56 resource groups) with JSON output for agents.
---

# pland-cli

Agent-native CLI für die pland.app API (deutsche HR-/ERP-/Facility-Plattform).

## Setup (einmalig)

```bash
# Installieren — direkt von GitHub, kein PyPI nötig:
uv tool install git+https://github.com/<user>/pland-cli
# oder ohne Installation ausführen:
uvx --from git+https://github.com/<user>/pland-cli pland --help

# API-Key hinterlegen (eine Variante):
export PLAND_API_KEY="<id>:<secret>"      # Umgebungsvariable
pland auth set-key                          # oder persistent (~/.config/pland)
```

## Grundregeln für Agenten

- **Immer `--json`** für maschinenlesbare Ausgabe: `pland --json <gruppe> <command>`.
- **Discovery statt Raten** — die CLI hat 522 Commands; finde sie so:
  - `pland --help` → alle 56 Gruppen
  - `pland <gruppe> --help` → Commands der Gruppe
  - `pland describe <gruppe> <command>` → Methode, Pfad, Parameter
  - `pland schema <Name>` → Request-/Response-Schema (z. B. `pland schema Absence`)
- **Listen:** Default eine Seite; `--all` paginiert vollständig (mit Dedup).
- **Schreiben (POST/PATCH/DELETE):** erst `--dry-run` ansehen, dann ohne Flag ausführen.
- **Profile:** `--profile prod|beta|local` (Default `prod`).

## Schreibende Operationen — Schutzlayer

Commands sind nach Risiko markiert: 🟡 (confirm) und 🔴 (critical) im `--help`.

- **Niemals** eigenmächtig `--yes` setzen, um eine 🟡-Bestätigung zu umgehen — frage
  zuerst den User ausdrücklich um Zustimmung in dieser Sitzung.
- 🔴-Operationen (Lohn, Zeiterfassungs-Freigaben, Mitarbeiter löschen, Massen-
  löschung, Account-Änderung) verlangen eine Terminal-Eingabe durch einen Menschen
  und lassen sich nicht per Flag auslösen — fordere den User auf, sie selbst zu bestätigen.
- Vor jedem Schreiben erst `--dry-run` zeigen, dann fragen.
- **Viele Schreibvorgänge:** `pland batch run --file ops.json` bündelt sie hinter
  **einer** Rückfrage (Stufe = höchstes Risiko in der Datei). Erst `--dry-run`
  zeigen, dann den User die Datei freigeben lassen. 🔴 verlangt weiterhin ein
  Terminal — ein Agent kann das nicht selbst auslösen. Query-Parameter lassen sich
  in einem Batch-Eintrag nicht abbilden — u. a. `jobs delete` (`splitDate`, `type`,
  `teamId`) niemals batchen, sondern einzeln ausführen.

## Fallstricke (sonst falsche Ergebnisse) — Details: references/gotchas.md

- **Timestamps sind Unix-Millisekunden** (`from`, `to`, `dtStart`, `dtEnd`, `trackingJobDate`).
- **`from`/`to`-Serverfilter sind unzuverlässig** bei Salaries/Absences/Time Tracking → nutze
  die enriched Commands, die clientseitig filtern, statt der generischen:
  - `pland salary for-object --object-id <id> --from YYYY-MM-DD --to YYYY-MM-DD`
  - `pland time-tracking in-range --from <d> --to <d> [--unapproved]`
  - `pland absences in-range --from <d> --to <d> [--approved-only]`
- **`objectId` wird bei Invoices ignoriert** → `pland invoice drafts --object-id <id>` filtert clientseitig.
- **Dokumente:** `pland documents upload <pdf> --kind faktura|regular` — `faktura` mergt an die Rechnung.

## Häufige Workflows — references/workflows.md

- Monatsstunden eines Objekts: `pland --json salary monthly-report --object-id <id> --year 2024 --month 4`
- Abgerechnete Zeiteinträge im Zeitraum: `pland --json salary for-object --object-id <id> --from 2024-04-01 --to 2024-04-30`
- Aktive Mitarbeiter: `pland --json users active`
- Entwurfs-Rechnungen: `pland --json invoice drafts --object-id <id>`
- Stundenlohn einer Lohnart: `pland --json pay-types wage <PAY_TYPE_ID>`

## Vollständige Command-Liste

Siehe `references/commands.md` (generiert, 56 Gruppen, 522 Commands). Bei Bedarf laden — nicht
vorab komplett lesen.

## Fehlerformat

Fehler kommen als `{"ok": false, "error": {"status", "title", "detail"}}` (Exit ≠ 0).
