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

The same orphan can break the number range instead, and that is the worse
failure. The unique index `companyId_1_numberPrefix_1_documentNumber_1` covers
the document number, and the next storno number is `max(existing) + 1`. A
record the collection keeps but no query returns — a half-written storno from a
cancel that died mid-flight — pins that maximum permanently: every further
cancel, on *any* invoice, recomputes the same number and gets `E11000`. Seen
2026-08-26: the blocking number was invisible to `invoice-storno list` (with
and without a `documentNumber` filter), to `get-distinct-values` on `_id` and
on `documentNumber`, and to `search perform-global`. No id means no
`invoice-storno delete`, and no API call moves the counter past it either (see
below). What does work: raise `nextNumber` past the blocked number in the web
UI. Verified 2026-08-26 — that is the way back, short of asking pland support to
delete the record.

Quick succession is what breeds these orphans: three `setToCanceled` inside 11
seconds left two behind. `fakturaDocumentIds` is an array — hand every id to one
call. Back-to-back calls race server-side, and each cancel is irreversible, which
is why `invoice set-canceled` is 🔴.

## Sending any faktura document: `overrideEmail` does not override
Four endpoints publish `overrideEmail` — `/stornos/send`, `/offers/send`,
`/credits/send`, `/assignmentConfirmations/send`. The API ignores that name on
every one of them and reads **`sendToEmail`** instead, as `/invoices/sendZugferd`
and `/invoices/sendXRechnung` already do in the published spec.

Ignoring it does not mean failing. What happens next depends on whether the
document can resolve a recipient of its own:

| document has a stored recipient | result with `overrideEmail` |
|---|---|
| no  | nothing is sent, document comes back in `skipped` |
| yes | **the mail goes to the customer** |

That second row is how two 2024 documents reached live customers on 2026-08-26
during a test that was meant to send to an internal address. `overrideEmail`
reads like a safe test switch and is the opposite of one.

**Never judge a send by the response.** `success` only tells you the API
accepted it; it does not tell you *who* received it. Check the recipient:

```
pland --json offers get <id>        # or invoice-storno / credit / …
#   -> statusTags[].recipient is the address it actually went to
pland --json logbuch list-for-chat <doc.chatId>
#   -> activity_sent_faktura_document_to_email, absent when nothing was sent
```

To test a send safely, pick a document where **no** address is resolvable —
neither on the document nor anywhere on the customer. Anything less and a
mistake goes out to a real customer. Note also that `/offers/send` fixes a draft
offer as a side effect, so a draft is not the harmless choice it looks like.

Verified 2026-08-26 on `/stornos/send` and `/offers/send`. For `/credits/send`
and `/assignmentConfirmations/send` only the ignored `overrideEmail` is
verified; `sendToEmail` is carried over from the other two, because every credit
and confirmation in the company has a customer address and probing it would have
risked another live mail.

## Sending a storno: a 200 that sent nothing
`pland invoice-storno create-send` needs `sendToEmail` for the recipient — the
published spec calls it `overrideEmail`, and the API ignores that name. It then
resolves no recipient and still answers 200, with the document listed under
`skipped` rather than `errors`:

```json
{"success": [], "errors": [], "skipped": ["<id>"]}
```

Nothing is sent. The only trace is a `permanent_fail` entry in `statusTags`
whose `recipient` is empty. Read the response: **`skipped` is a failure**, only
`success` means the mail went out. The second check is the logbuch — a real send
writes `activity_sent_faktura_document_to_email`, a skipped one writes nothing:

```
pland --json logbuch list-for-chat <storno.chatId>
```

Verified 2026-08-26 by sending a real storno both ways. `/credits/send`,
`/offers/send` and `/assignmentConfirmations/send` publish `overrideEmail` too
and are likely to behave the same, but that was not exercised — sending is not
something to probe on live customer documents.

Beware the inherited `statusTags`: a fresh storno already carries the `sent` and
`delivered` entries of the invoice it cancels, timestamped when *the invoice*
went out. They say nothing about the storno.

## Company settings are read-only over the API, and `nextNumber` is not the counter
`settings.<documentType>.nextNumber` reads like the running number and is not.
It is where the range starts when the prefix rolls over, and it is never
advanced afterwards. Verified 2026-08-26 on invoices and stornos alike: each
`nextNumber` sat hundreds below the highest number actually in use and matched
the *first* number of the current prefix exactly. What gets handed out is
`max(existing) + 1`.

Changing any of it over the API is impossible. `PATCH /company` is the only
write route — `PUT` answers "Method not allowed. Must be one of: GET, PATCH" —
and its handler does not resolve
(`PlanD\Components\Company\CompanyController:update is not resolvable`), with
an unchanged body just the same. `/company/`, `/company/settings`,
`/companies/{id}` and `/v1`, `/v3` all answer "Not found.". The overlay drops
the operation, so `pland company update` does not exist; `company get-info`
still reads.

This is the API surface only — the web UI writes these settings without
trouble, which is what makes it the repair path for a jammed number range.

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
