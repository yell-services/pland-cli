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

## Cancelling an invoice: body fields, finality, orphans
`pland invoice set-canceled` wants `fakturaDocumentIds` (not `ids`) and requires
`canceledAtDate` — the published spec is wrong on both counts, corrected in the
overlay. Fetch the body with `pland schema SetInvoicesCanceledRequest`.

A cancel **cannot be taken back**. There is no un-cancel route (only Time
Tracking has `unCancel`), and clearing `canceledDate` via PATCH is accepted and
ignored. The invoice itself survives and keeps its number.

Cancelling creates an `InvoiceStorno` record that the invoice does not link —
`stornoId` stays `null`. `invoice delete` does **not** take it along, so the
record is left orphaned. A unique index on `referenceId` then makes a later
cancel under the same `referenceId` fail with `E11000 duplicate key`. Clean up
via `pland invoice-storno list --all` (match on `referenceId`) and
`pland invoice-storno delete <id>`.

## Assignment confirmations: everything works except finding one
The resource is fully covered — create them from accepted offers with
`pland offers generate-assignment-confirmations`, then `get`, `send`, `delete`,
`create-preview`, the two PDF commands, `attach-documents-to` and
`list-referenced-documents` under `pland assignment-confirmations`. All ten
routes have a command.

Every one of them except the generator needs an id, and **nothing ever hands
one out**. The generator answers `{"message": "Assignment confirmations
generated"}` — no ids. No assignment or offer field carries the id either
(`attachedFakturaDocumentIds` on an offer holds other document types), and the
spec has no `assignmentConfirmationId` anywhere.

There is also no way to list them. Probed 2026-08-15, all answering "Not found."
or `Failed to parse Id` against a control probe on the same resource:
`/assignmentConfirmations/` (plus `/list`, `/all`, `/count`) and
`/fakturaDocuments/` as a generic entry point. Unlike the storno collection,
this one is not merely undocumented — the API does not serve it, so no overlay
entry can fix it. Do not re-probe these.

Net effect: a confirmation you generate is write-only from the API's side. Ask
pland.app for either a collection route or ids in the generator's response.

## Schutzlayer für Schreibvorgänge
DELETE/PATCH auf kritische Daten sind 🟡/🔴 markiert und verlangen Bestätigung.
Entwürfe (Rechnungen/Angebote ohne `fixDate`) werden automatisch als unkritisch
behandelt. Audit-Log: `~/.local/state/pland/audit.jsonl`.
