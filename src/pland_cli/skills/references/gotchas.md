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

## Reaching a document that has no collection route
`/assignmentConfirmations/` does not exist — there is no collection to list,
and the generator (`pland offers generate-assignment-confirmations`) answers
`{"message": "Assignment confirmations generated"}` without ids. That looks
like a dead end but is not: the id comes from the **offer it was generated
from**.

```
pland --json assignment-confirmations list                  # walks every offer
pland --json assignment-confirmations list --offer-id <ID>  # skips the walk
```

That command does the rounds for you and tags each hit with its `offerId`. It
costs one request per offer (~20 s at a few hundred) because no bulk route
exists, and it warns on stderr if any offer could not be read — a short list
must not read as a complete one. By hand it is two steps:

```
pland --json offers list-referenced-faktura-documents-for <OFFER_ID>
#   -> [{documentType: "invoice", ...}, {documentType: "assignment_confirmation", _id: ...}]
pland --json assignment-confirmations get <CONFIRMATION_ID>
```

`referencedFakturaDocuments` is the general mechanism linking faktura documents
to each other, and every type carries it: a storno points at its invoice, a
credit and an invoice reminder likewise. Reach for it whenever a document type
has no collection of its own. Note `attachedFakturaDocumentIds` on the document
is *not* the same thing and does not hold the related document.

Do not conclude from a missing collection route that a type is unreachable —
check the documents it is generated from first. Verified 2026-08-15: all 11
assignment confirmations in the company were found this way, from 221 offers.

## Schutzlayer für Schreibvorgänge
DELETE/PATCH auf kritische Daten sind 🟡/🔴 markiert und verlangen Bestätigung.
Entwürfe (Rechnungen/Angebote ohne `fixDate`) werden automatisch als unkritisch
behandelt. Audit-Log: `~/.local/state/pland/audit.jsonl`.
