# pland — Fallstricke (Detail)

## Unix-Millisekunden
Alle Zeitstempel (`from`, `to`, `dtStart`, `dtEnd`, `trackingJobDate`) sind ms seit Epoch.
Umrechnung: `datetime.timestamp() * 1000`.

## Unzuverlässige Serverfilter
`from`/`to` an `/salaries/`, `/absences/`, `/timetracking/list` unterschlagen frisch
synchronisierte Einträge. **Lösung:** alle Einträge ziehen (paginiert) und clientseitig
nach dem Datumsfeld filtern. Die enriched Commands tun das bereits — nutze sie statt der
generischen `list`-Commands:

- `pland salary for-object --object-id <id> --from YYYY-MM-DD --to YYYY-MM-DD`
  → abgerechnete Zeiteinträge eines Objekts im Zeitraum.
- `pland time-tracking in-range --from <d> --to <d> [--unapproved]`
  → Zeiteinträge nach Arbeitstag (clientseitig nach `trackingJobDate` gefiltert).
- `pland absences in-range --from <d> --to <d> [--approved-only]`
  → Abwesenheiten im Zeitraum (clientseitig nach `dtStart` gefiltert).

## Ignorierter objectId-Filter (Invoices)
`/invoices/?objectId=…` liefert trotzdem alle Rechnungen der Company. **Lösung:**
`pland invoice drafts --object-id <id>` filtert clientseitig nach `objectId`;
Entwürfe sind Rechnungen ohne `fixDate`.

## Überlappende Pagination
Aufeinanderfolgende Seiten können Einträge doppelt liefern → per `_id` deduplizieren
(macht `--all` / die enriched Commands automatisch).

## Dokument-Typ faktura
`pland documents upload <pdf> --kind faktura` legt das Dokument in
`attachedFakturaDocumentIds` (an Rechnung gemergt); `--kind regular` landet in
`attachedDocumentIds`. GET/DELETE müssen denselben Typ verwenden.

## Invoice-PATCH
Vor einem PATCH die Read-only-Felder strippen: `_id, object, customer, recipient,
assignments, previousInvoices, totals, status, companyId`.

## Schutzlayer für Schreibvorgänge
DELETE/PATCH auf kritische Daten sind 🟡/🔴 markiert und verlangen Bestätigung.
Entwürfe (Rechnungen/Angebote ohne `fixDate`) werden automatisch als unkritisch
behandelt. Audit-Log: `~/.local/state/pland/audit.jsonl`.
