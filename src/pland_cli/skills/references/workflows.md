# pland — Workflow-Rezepte

## Monatsstunden eines Objekts
```bash
pland --json salary monthly-report --object-id <id> --year 2024 --month 4
# → aggregierte Arbeitsstunden des Objekts für den Monat
```

## Abgerechnete Zeiteinträge eines Zeitraums (clientseitig gefiltert)
```bash
pland --json salary for-object --object-id <id> --from 2024-04-01 --to 2024-04-30 | jq 'length'
```

## Zeiteinträge nach Arbeitstag
```bash
# alle Einträge im Zeitraum:
pland --json time-tracking in-range --from 2024-04-01 --to 2024-04-30
# nur nicht freigegebene:
pland --json time-tracking in-range --from 2024-04-01 --to 2024-04-30 --unapproved
```

## Abwesenheiten eines Zeitraums
```bash
pland --json absences in-range --from 2024-04-01 --to 2024-04-30 --approved-only
```

## Aktive Mitarbeiter exportieren
```bash
pland --json users active | jq '.[] | {id: ._id, nr: .number}'
```

## Entwurfs-Rechnungen eines Objekts
```bash
pland --json invoice drafts --object-id <id> | jq '.[]._id'
```

## Dokument an eine Rechnung anhängen
```bash
pland --json documents upload ./rechnung.pdf --kind faktura
# separater Anhang (nicht an Rechnung gemergt):
pland --json documents upload ./anhang.pdf --kind regular --user-id <id>
```

## Stundenlohn einer Lohnart auflösen
```bash
pland --json pay-types wage <PAY_TYPE_ID>
```
