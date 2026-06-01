# pland-cli

[![CI](https://github.com/yell-services/pland-cli/actions/workflows/ci.yml/badge.svg)](https://github.com/yell-services/pland-cli/actions/workflows/ci.yml)
[![Python: 3.11+](https://img.shields.io/badge/python-3.11%2B-3776ab.svg)](https://www.python.org/)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](./LICENSE)
[![Ruff](https://img.shields.io/badge/ruff-checked-261230.svg)](https://docs.astral.sh/ruff/)

> Inoffizielle, agent-native CLI für die [pland.app](https://pland.app) API —
> Zeiterfassung, Lohn, Urlaub, Objekte, Rechnungen, Qualitätskontrolle u. v. m.
> **529 Commands** über 53 Ressourcen-Gruppen, generiert aus der OpenAPI-Spec,
> mit JSON-Ausgabe für KI-Agenten.

> **Keywords:** pland.app cli · pland api client · pland.app api · agent-native cli · claude code skill · codex cli skill · zeiterfassung lohn urlaub rechnungen api

## 🤖 LLM-Schnellstart

Wenn du ein Agent bist (Claude Code, Cursor, Codex, …): folge dem Abschnitt
[Für KI-Agenten](#für-ki-agenten) — installieren, Key setzen, Commands per
`describe`/`schema` entdecken statt raten. Maschinenlesbare Doku: [llms.txt](./llms.txt).

## 👋 Schnellstart (Mensch)

```bash
# 1. Installieren (kein Klonen, kein PyPI — direkt von GitHub):
uv tool install git+https://github.com/yell-services/pland-cli
#    oder einmalig ohne Installation:
uvx --from git+https://github.com/yell-services/pland-cli pland --help

# 2. API-Key hinterlegen:
export PLAND_API_KEY="<id>:<secret>"     # Umgebungsvariable
#    oder persistent:        pland auth set-key
#    oder neu erzeugen:      pland auth bootstrap   (Login-ID + Passwort → Key)

# 3. Loslegen:
pland --json users active
```

### API-Key anlegen

Hast du noch keinen Key? `pland auth bootstrap` loggt dich einmalig mit deiner
**Login-ID (Nummer) + Passwort** ein, erzeugt über die API einen neuen Key und
speichert **nur diesen** — Login-ID und Passwort werden **nirgends** abgelegt:

```bash
pland auth bootstrap          # fragt Login-ID + Passwort interaktiv ab
```

> Lass die Eingabe vom Menschen am Prompt machen; gib die Zugangsdaten nicht als
> Flags weiter (Shell-History/Prozessliste). Der erzeugte Key wird **einmalig**
> angezeigt — `pland` speichert ihn direkt, du musst ihn nicht kopieren.

## Für KI-Agenten

Wenn du ein Agent bist und das hier liest, um die CLI zu nutzen:

1. **Installieren:** `uv tool install git+https://github.com/yell-services/pland-cli`
2. **Key setzen:** `export PLAND_API_KEY="<id>:<secret>"`
3. **Commands finden** (nicht raten — 529 Stück):
   - `pland --help` (53 Gruppen) · `pland <gruppe> --help`
   - `pland describe <gruppe> <command>` (Methode, Pfad, Parameter)
   - `pland schema <Name>` (z. B. `pland schema Absence`)
4. **Immer `--json`** für maschinenlesbare Ausgabe: `pland --json <gruppe> <command>`.
5. **Skill installieren** (optional, tiefere Integration): `pland skill install --agent claude` (oder `--agent codex`).

### Enriched Commands (statt der generischen nutzen)

Diese handgepflegten Commands umgehen unzuverlässige Serverfilter und liefern korrekte Ergebnisse:

```bash
pland --json salary for-object --object-id <id> --from <d> --to <d>
pland --json salary monthly-report --object-id <id> --year 2024 --month 4
pland --json time-tracking in-range --from <d> --to <d>
pland --json absences in-range --from <d> --to <d>
pland --json invoice drafts --object-id <id>
pland --json documents upload <pdf> --kind faktura|regular
pland --json users active
pland --json pay-types wage <id>
```

### Fallstricke (sonst falsche Ergebnisse)
- Zeitstempel sind **Unix-Millisekunden**.
- `from`/`to`-Serverfilter unzuverlässig → nutze die enriched Commands
  `pland salary for-object`, `pland time-tracking in-range`, `pland absences in-range`
  (clientseitig gefiltert) statt der generischen.
- `objectId` bei Invoices ignoriert → `pland invoice drafts --object-id <id>` (clientseitig gefiltert).
- Dokumente: `pland documents upload <pdf> --kind faktura|regular` — `faktura` mergt an die Rechnung.
- Schreiben (POST/PATCH/DELETE): erst `--dry-run` ansehen, dann ohne Flag ausführen.

## Profile

`--profile prod|beta|local` (Default `prod`). Key/Base-URL via Umgebung
(`PLAND_API_KEY`, `PLAND_PROFILE`, `PLAND_BASE_URL`) oder einer Config-Datei
(Vorlage: `config.example.toml`).

**Config-Pfad** (überschreibbar mit `PLAND_CONFIG`):
- Linux/macOS: `~/.config/pland/config.toml` (bzw. `$XDG_CONFIG_HOME`)
- Windows: `%APPDATA%\pland\config.toml`

> **Windows-Hinweis:** Auf Linux/macOS wird die Config-Datei mit `chmod 600`
> (nur für dich lesbar) geschützt. Windows kennt diese POSIX-Bits nicht — dort
> ist **`PLAND_API_KEY` als Umgebungsvariable der sichere Weg**, statt den Key
> in der Datei abzulegen.

## Plattformen

Linux, macOS und Windows (Python ≥ 3.11). Reine Python-Abhängigkeiten, keine
nativen Builds. CI testet alle drei Betriebssysteme.

## Sicherheit

Schreibende Operationen sind nach Risiko gestuft: 🟢 frei · 🟡 Bestätigung
(`--yes` überspringt) · 🔴 Terminal-Eingabe nötig (kein Flag-Bypass). Das schützt
vor versehentlichem Löschen durch Agenten. Jede Schreiboperation wird in
`~/.local/state/pland/audit.jsonl` protokolliert.

> **Gegen einen gekaperten Agenten** mit gültigem Key kann die CLI nicht hart
> schützen (er könnte die API direkt ansprechen). Erzeuge den API-Key daher von
> einem Account mit **minimalen Rechten** (least privilege).

## Status & Lizenz

Inoffizieller Community-Client, **nicht** von pland.app betrieben oder unterstützt.
Lizenz: Apache-2.0. Sicherheitslücken bitte privat melden — siehe [SECURITY.md](./SECURITY.md).
Beiträge willkommen — siehe [CONTRIBUTING.md](./CONTRIBUTING.md).

## Pflege

API-Update? Spec ziehen und neu generieren:

```bash
curl -sL https://docs.pland.app/openapi.yaml -o openapi.yaml
uv run python -m pland_cli._codegen.generate      # commands/ neu
uv run python -m pland_cli._codegen.skillgen      # skills/references/commands.md neu
uv run pytest -q
```
