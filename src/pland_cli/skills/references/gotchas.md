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

## Storno: Body-Felder, Endgültigkeit, Waisen
`pland invoice set-canceled` erwartet `fakturaDocumentIds` (nicht `ids`) und
`canceledAtDate` als Pflichtfeld — die veröffentlichte Spec ist an beiden Punkten
falsch, korrigiert im Overlay. Body abrufbar mit
`pland schema SetInvoicesCanceledRequest`.

Ein Storno ist **nicht zurücknehmbar**: es gibt keine Un-Storno-Route (nur Time
Tracking hat `unCancel`), und `canceledDate` per PATCH zu leeren wird angenommen,
ändert aber nichts. Die Rechnung selbst bleibt mit ihrer Nummer erhalten.

Beim Stornieren entsteht ein eigener `InvoiceStorno`-Datensatz, den die Rechnung
nicht verlinkt (`stornoId` bleibt `null`). `invoice delete` löscht ihn **nicht**
mit — der Record bleibt als Waise zurück. Weil ein Unique-Index auf
`referenceId` liegt, scheitert ein späteres Storno mit derselben `referenceId`
an `E11000 duplicate key`. Aufräumen über
`pland invoice-storno list --all` (nach `referenceId` suchen) und
`pland invoice-storno delete <id>`.

## Schutzlayer für Schreibvorgänge
DELETE/PATCH auf kritische Daten sind 🟡/🔴 markiert und verlangen Bestätigung.
Entwürfe (Rechnungen/Angebote ohne `fixDate`) werden automatisch als unkritisch
behandelt. Audit-Log: `~/.local/state/pland/audit.jsonl`.
