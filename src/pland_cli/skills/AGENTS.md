# pland-cli — Anleitung für Agenten

Agent-native CLI für die pland.app API. Befehl: `pland`.

## Installation & Key
```bash
uv tool install git+https://github.com/yell-services/pland-cli
export PLAND_API_KEY="<id>:<secret>"   # oder: pland auth set-key
```

## Bedienung
- Immer `--json`: `pland --json <gruppe> <command>`.
- Discovery: `pland --help`, `pland <gruppe> --help`, `pland describe <gruppe> <command>`, `pland schema <Name>`.
- Listen: `--all` für vollständige Pagination.
- Writes (POST/PATCH/PUT/DELETE): preview with `--dry-run` first. It sends nothing
  and returns `{"dry_run": true, "method", "url", "path", "params", "body"}` —
  verify `url` matches the profile you meant. Reads have no `--dry-run`.
- Profile: `--profile prod|beta|local` (Default `prod`).

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
  zeigen, dann den User die Datei freigeben lassen. With `--json` it returns
  `{dry_run, count, risk, confirmToken, operations}`; read `operations` to check
  every request the file would send. 🔴 verlangt weiterhin ein
  Terminal — ein Agent kann das nicht selbst auslösen. Query-Parameter lassen sich
  in einem Batch-Eintrag nicht abbilden — u. a. `jobs delete` (`splitDate`, `type`,
  `teamId`) niemals batchen, sondern einzeln ausführen.

## Wichtige Fallstricke
- Zeitstempel sind Unix-Millisekunden.
- `from`/`to`-Serverfilter unzuverlässig → enriched Commands filtern clientseitig:
  - `pland salary for-object --object-id <id> --from YYYY-MM-DD --to YYYY-MM-DD`
  - `pland time-tracking in-range --from <d> --to <d> [--unapproved]`
  - `pland absences in-range --from <d> --to <d> [--approved-only]`
- `objectId` bei Invoices ignoriert → `pland invoice drafts --object-id <id>`.
- Dokumente: `pland documents upload <pdf> --kind faktura|regular`.

Vollständige Referenz: `references/commands.md` (53 Gruppen, 529 Commands).
Workflows: `references/workflows.md`. Details: `references/gotchas.md`.
