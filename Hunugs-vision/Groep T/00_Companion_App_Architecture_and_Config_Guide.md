---
title: Groep T Companion App — Technical Architecture, Config & Maintenance Guide
tags:
  - documentation
  - architecture
  - companion-app
  - groep-t
---

# 🛠️ Groep T Companion App (`groep_t_app.py`) — Architecture, Config & Fix Guide

> 🏠 **[[00_Groep_T_Command_Center|← Command Center]]** • **[[00_Complete_System_and_Program_User_Guide|📘 User Guide]]** • **[[07_Study_Analytics_Snapshot|📈 Live Analytics Snapshot]]**

Dit document is de **technische handleiding** voor de all-in-one companion web-app (`groep_t_app.py` + `groep_t_app/`). Hiermee begrijp je exact **hoe de code werkt**, **waar alle instellingen staan** (poort, vakken, examendata, kleuren, doellijn, UI), en **hoe je zelf bugs oplost of nieuwe functies toevoegt**.

---

## 1. Overzicht van Alle App-Bestanden

```text
Hunugs-vision/
├── groep_t_app.py                ← Python 3 HTTP-server + Markdown/YAML/JSON/CSV sync engine
├── daily_journal.py              ← Hergebruikt door groep_t_app.py (via `import daily_journal`) om ontbrekende dagnotities te genereren
├── groep_t_app/
│   ├── index.html                ← HTML-structuur (5 tabs + Slide-over Note Drawer + Tooltip)
│   ├── style.css                 ← Donker thema, responsive CSS Grid/Flexbox, progress bars, heatmap-kleuren
│   └── app.js                    ← Frontend logica (SVG heatmap & charts, Pomodoro/Stopwatch, API calls, localStorage)
└── Groep T/
    ├── study_telemetry.json      ← Gestructureerde sessiehistoriek (bron voor sessietabel & unit_logged aftrek)
    ├── study_logs_export.csv     ← Automatisch geëxporteerde dagtotalen per vak
    ├── study_units_export.csv    ← Automatisch geëxporteerde status van alle 270 studiemodules
    └── 07_Study_Analytics_Snapshot.md ← Gegenereerd door `Sync Obsidian Snapshot` of `--export-only`
```

**Belangrijk ontwerpprincipe:** De app gebruikt **geen externe libraries** (geen pip-installaties, geen npm/React/Chart.js). Alles draait op Python 3 stdlib (`http.server`, `socketserver`, `json`, `csv`, `re`, `pathlib`, `datetime`) en pure vanilla HTML/CSS/JS + inline SVG.

---

## 2. Architectuur & Dataflow (Hoe Alles Samenwerkt)

```text
[Browser: index.html + app.js]
        │  GET /api/state
        │  POST /api/log/session  |  POST /api/unit/update  |  POST /api/obsidian/snapshot
        ▼
[groep_t_app.py — GroepTRequestHandler (ThreadingTCPServer)]
        ├── Leest/schrijft YAML-properties in `Groep T/**/*.md` (alle #study-unit files)
        ├── Vinkt `- [ ]` ↔ `- [x]` aan/uit in `Groep T/02_Master_Course_Checklists.md`
        ├── Leest/schrijft `Daily_Journal/YYYY-MM-DD.md` & `Groep T/Study_Logs/YYYY-MM-DD.md`
        ├── Slaat gedetailleerde sessies op in `Groep T/study_telemetry.json`
        └── Exporteert `study_logs_export.csv`, `study_units_export.csv` & `07_Study_Analytics_Snapshot.md`
```

### Hoe Uren, Voortgang & Resterende Tijd Berekend Worden (`build_state()`)
1. **Studie-uren (`scan_study_logs()`):**
   - Scant `Daily_Journal/*.md` en `Groep T/Study_Logs/*.md` op notes met tag `study-log` óf property `study_hours_total`.
   - Berekent `subject_sum = sum(hrs_*)` en neemt `max(study_hours_total, subject_sum)` voor het dagtotaal.
   - **Anti-dubbeltelling:** Als zowel `Daily_Journal/YYYY-MM-DD.md` als `Study_Logs/YYYY-MM-DD.md` voor dezelfde datum bestaan, neemt hij per vak `max(entry1, entry2)`.
2. **Focusscore (`avg_focus`):**
   - Enkel dagen waar `study_focus_score > 0` tellen mee in het gemiddelde (`0` of leeg geldt als *nog niet ingevuld*, niet als `0/10`).
3. **Resterende studie-uren (`est_hours_left`):**
   - Voor elke niet-afgeronde module (`completed == false`) kijkt `build_state()` naar `unit_logged[path]` uit `study_telemetry.json` en trekt die gelogde uren af: `max(0.0, est_hours - logged_hours)`.
   - Zodra je een sessie logt gekoppeld aan een specifieke module zonder `mark_unit_done` aan te vinken, zet `/api/log/session` die module automatisch van `todo` naar **`in-progress`**.

---

## 3. Configuratiepunten (Wat Je Zelf Kunt Aanpassen)

### 3.1 Vakken, ECTS, Examendata & Kleuren (`groep_t_app.py`)
Bovenaan in `groep_t_app.py` staat de lijst `COURSES`. Wil je later **Semester 2 vakken** toevoegen, een **examendatum aanpassen**, of **kleuren wijzigen**, bewerk dan één dict in `COURSES`:

```python
{
    "id": "dynamica",                         # Unieke interne ID (gebruikt in API & localStorage)
    "name": "Dynamica en energie (T1ADE1)",   # Exacte `course:` string in de .md YAML-properties!
    "short": "Dynamica & Energie",            # Korte naam in UI, grafieken en snapshot
    "hrs_key": "hrs_dynamica",                # Exacte YAML-property naam voor uren van dit vak
    "ects": 3,                                # Aantal studiepunten (gebruikt in 90% ECTS Simulator)
    "exam_date": "2027-01-11",                # YYYY-MM-DD (gebruikt voor aftelklok & heatmap marker)
    "exam_label": "ma 11.01.2027 08:30",      # Tekst op examenkaartjes
    "location": "DV1 - 02.54",                # Lokaal
    "color": "#f97316",                       # Hex-kleur voor bar chart, donut, progress bar & kaart
    "index_file": "Groep T/Dynamica_en_Energie_/00_Meta/Index.md",
}
```
> [!warning] Let op bij het toevoegen van een nieuw vak!
> Als je een nieuwe `hrs_key` toevoegt (bv. `hrs_fysica`), voeg die property ook toe aan `Templates/Daily_Journal_Template.md` en `Groep T/00_Study_Hours_Base.base` als je die ook in Obsidian Bases wilt zien.

### 3.2 Standaard Poort, Host & Browser-Launch (`main()`)
- Standaard start de server op **`127.0.0.1:8765`** (`--host` en `--port` in `argparse`).
- Wil je hem altijd op poort `9000` zonder terminal-argumenten, pas `default=8765` in `main()` aan — of start met:
  ```bash
  python3 groep_t_app.py --port 9000 --no-open
  ```

### 3.3 Sprint Startdatum & Heatmap Datumvenster
- **In `groep_t_app.py` (`build_state()`):**
  - `"sprint_start": "2026-11-15"` bepaalt de `Sprint Day X/30` teller bovenaan.
- **In `groep_t_app/app.js` (`renderHeatmap()` & `renderDailyBarChart()`):**
  - `let startISO = "2026-10-01";` en `let endISO = "2027-01-31";` bepalen het standaardbereik van de Consistency Heatmap. Als er oudere/nieuwere logs bestaan, rekt de code dit automatisch mee op!
  - **6u-doellijn in de grafiek:** in `renderDailyBarChart()` bepaalt `const isTarget = val === 6;` de groene stippellijn (`6h`). In `renderHeatmap()` bepalen de drempels `hrs >= 6`, `>= 4`, `>= 2`, `> 0` de 5 groentinten.

### 3.4 Pomodoro Timers (`MODES` in `groep_t_app/app.js`)
Bovenaan in `app.js` kun je bloktijden wijzigen of een 5e knop toevoegen:
```javascript
const MODES = {
  pomo25: { label: "25m Pomodoro", seconds: 25 * 60, stopwatch: false },
  pomo50: { label: "50m Deep Work", seconds: 50 * 60, stopwatch: false },
  pomo90: { label: "90m Exam Block", seconds: 90 * 60, stopwatch: false },
  stopwatch: { label: "Stopwatch", seconds: 0, stopwatch: true },
};
```
*(Als je in `app.js` een modus aanpast, pas ook de knop `data-mode="..."` in `groep_t_app/index.html` aan.)*

### 3.5 Browser `localStorage` Sleutels
De frontend bewaart twee dingen lokaal in je browser:
- `groep_t_timer` — De lopende/gepauzeerde timerstand zodat tabwissels of page reloads geen sessie kwijtmaken.
- `groep_t_ects_sim` — De schuifregelaars (`/20`) in de *90% ECTS Pass Simulator*.
*(Resetten in Chrome/Firefox DevTools Console: `localStorage.removeItem("groep_t_timer")` of `localStorage.removeItem("groep_t_ects_sim")`.)*

---

## 4. Backend HTTP API Reference (`GroepTRequestHandler`)

Alle endpoints draaien op `http://127.0.0.1:8765`:

| Method | Endpoint | Wat het doet | Payload / Query |
| :---: | :--- | :--- | :--- |
| `GET` | `/api/state` | Leest heel de vault live uit (units, logs, streak, sessies, course stats) | — |
| `GET` | `/api/unit/content` | Haalt ruwe Markdown-tekst van één studienote op (met path-traversal check) | `?path=Groep T/.../note.md` |
| `GET` | `/api/export/csv` | Genereert & downloadt actuele CSV | `?type=logs` of `?type=units` |
| `GET` | `/api/export/json` | Downloadt volledige `study_telemetry.json` | — |
| `POST` | `/api/unit/update` | Past YAML (`completed`, `status`, `priority`, `est_hours`) + checklist + optionele notitie aan | `{"path": "...", "completed": true, "append_note": "..."}` |
| `POST` | `/api/log/session` | Maakt dagfile aan indien nodig, verhoogt `hrs_*` & `study_hours_total`, updatet `Actual Total` tekst, voegt Markdown-rij toe, schrijft `study_telemetry.json` & CSV's | `{"date": "YYYY-MM-DD", "target": "daily_journal"\|"study_log", "course_id": "wiskunde", "hours": 1.5, "focus_score": 8, "pomodoros": 2, "unit_path": "...", "mark_unit_done": false, "notes": "..."}` |
| `POST` | `/api/obsidian/snapshot` | Schrijft/ververst `Groep T/07_Study_Analytics_Snapshot.md` + CSV's | `{}` |

---

## 5. Hoe Bugs Voorkomen & Oplossen (Debugging & Pitfalls)

### 5.1 Tijdzone-valkuil in JavaScript (`toISOString()` bug — al opgelost!)
In Europa (`UTC+1`/`UTC+2`) zet `new Date("2026-11-15T00:00:00").toISOString().slice(0, 10)` de lokale middernacht terug naar **`"2026-11-14"`** (1 uur vroeger in UTC!).
- **Regel in `app.js`:** Gebruik **altijd** `parseLocalDate(iso)`, `toLocalISO(dt)` en `addDaysISO(iso, delta)` — **nooit** `.toISOString().slice(0, 10)`.

### 5.2 YAML Frontmatter Parser (`parse_simple_yaml` & `update_frontmatter_keys`)
- De eigen parser ondersteunt flat `key: value` paren, booleans (`true`/`false`), getallen, strings, inline arrays (`[a, b]`) en multi-line `- item` lijsten.
- **Valkuil:** Vermijd complexe geneste YAML-objecten in studienotes of studielogs, want `update_frontmatter_keys` vervangt platte top-level keys terwijl hij bestaande regels en volgorde behoudt.

### 5.3 Veilig Data Herstellen of Verwijderen (als je een foutieve test-log wilt terugdraaien)
Als je ooit per ongeluk een foute sessie gelogd hebt:
1. Open de betreffende `Daily_Journal/YYYY-MM-DD.md` (of `Study_Logs/YYYY-MM-DD.md`) en corrigeer `hrs_*` en `study_hours_total` in Properties (en verwijder eventueel de sessieregel onderaan).
2. Open `Groep T/study_telemetry.json` en verwijder dat ene sessie-object uit de `"sessions": [...]` array (let op dat er geen trailing comma achterblijft!).
3. Klik in de webapp rechtsboven op **`🔄 Reload Vault`** (en optioneel **`📝 Sync Obsidian Snapshot`**) om CSV's en grafieken opnieuw te synchroniseren.

### 5.4 Snelle Test- & Herstelcommando's in de Terminal
```bash
# 1. Alleen JSON, CSV's en 07_Study_Analytics_Snapshot.md verversen (zonder server)
python3 groep_t_app.py --export-only

# 2. Controleren of python-code syntactisch geldig is
python3 -m py_compile groep_t_app.py daily_journal.py

# 3. Poort al bezet? ("Address already in use") -> start op andere poort of zoek proces
python3 groep_t_app.py --port 8766
```
