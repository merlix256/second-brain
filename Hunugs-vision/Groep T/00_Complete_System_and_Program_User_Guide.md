---
title: Groep T Study OS — Complete System, Program & User Guide
tags:
  - documentation
  - manual
  - groep-t
  - system-guide
---

# 📘 Groep T Study OS — Complete System, Program & User Guide

> 🏠 **[[00_Groep_T_Command_Center|← Terug naar Groep T Command Center]]** • **[[00_System_Documentation_Requested_vs_Implemented|📋 Requested vs. Implemented]]** • **[[06_Groep_T_War_Room.canvas|🗺️ Visual War Room]]**

Dit handboek legt **tot in detail** uit hoe jouw complete Obsidian-studiesysteem werkt: zowel de **onderliggende software & plugins ("the program")**, als de **architectuur, YAML-properties, Obsidian Bases-formules, Python-automatisering en dagelijkse/wekelijkse workflows**.

---

## 1. Architectuur van het Systeem (Overzicht)

Jouw vault `Hunugs-vision` is opgebouwd uit **vier samenwerkende lagen**:

1. **Command & Strategy Laag (`Groep T/` root):** Centrale dashboards, 30-dagen inhaalplan, master checklists, examenrooster, onderzoeksrapporten en visuele Canvas.
2. **Live Database Laag (`.base` bestanden + YAML Properties):** Native **Obsidian Bases** die automatisch alle **270 studiemodules** en alle **dagelijkse studielogs** live filteren, groeperen en optellen zonder externe plugins zoals Dataview.
3. **7 Vak-Vaults (`Groep T/<Vak>/`):** De inhoudelijke cursussen (hoofdstukken, kennisclips, oefensessies, Q&A-kaarten, bewijzen, labo's, practica en mock exams) van alle 30 ECTS in Semester 1.
4. **Dagelijkse Executie & Automatisering (`Daily_Journal/`, `Study_Logs/`, `Templates/`, `TaskNotes/`, `daily_journal.py`):** Dagelijkse planning, tijdblokken, taakbeheer en geautomatiseerde aanmaak van dagnotities via Python.

### 📁 Volledige Mappen- en Bestandenstructuur

```text
Hunugs-vision/
├── daily_journal.py                          ← Python CLI-programma voor automatische dagnotities (+ cron)
├── Daily_Journal/                            ← Dagelijkse planner + habit + Groep T study log per dag
│   └── 2026-11-15.md                         ← Vandaag aangemaakt met study-hour properties
├── Templates/
│   ├── Daily_Journal_Template.md             ← Template gebruikt door daily_journal.py & Daily Notes plugin
│   └── daily_planner.md
├── TaskNotes/
│   └── Views/                                ← agenda-default.base, kanban-default.base, pomodoro-stats.base, ...
└── Groep T/
    ├── 00_Groep_T_Command_Center.md          ← ⭐ HOOFDDASHBOARD (start hier elke dag)
    ├── 00_Course_Progress_Base.base          ← Live voortgangsdatabase over alle 270 studiemodules
    ├── 00_Study_Hours_Base.base              ← Live uren-database (dag- & weektotalen per vak)
    ├── 00_Complete_System_and_Program_User_Guide.md   ← Dit handboek
    ├── 00_System_Documentation_Requested_vs_Implemented.md ← Audit: gevraagd vs. gebouwd
    ├── 01_30_Day_Catchup_Sprint_Plan.md      ← Inhaalsprint 15 nov – 15 dec + blokplanning tot 29 jan
    ├── 02_Master_Course_Checklists.md        ← Klikbare master-checklist van alle 270 units
    ├── 03_Daily_Study_Hours_Tracker.md       ← Uitleg & embedded uren-dashboard
    ├── 04_Labos_and_Permanente_Evaluatie_Hub.md ← Verplichte labo's, ANS-testen & dec-deadlines
    ├── 05_KU_Leuven_Groep_T_Course_Research.md  ← ECTS, puntensplitsing, 80/20 slaagregels per vak
    ├── 06_Groep_T_War_Room.canvas            ← Visuele mindmap/roadmap van heel Semester 1
    ├── exam_schedule.md                      ← Officieel examenrooster + lokalen + rustdagen
    ├── Study_Logs/
    │   ├── Study_Log_Template.md             ← Standalone dag-studielog template
    │   └── 2026-11-15.md                     ← Starter studielog voor Dag 1
    ├── Chemie/                               ← 50 study units (Chapters, Q&A, 9 Labo's, Exam Prep)
    ├── Computationeel_Denken/                ← 32 study units (Lectures, Practica, 4-p. Samenvatting, 3 Mocks)
    ├── Dynamica_en_Energie_/                 ← 28 study units (Chapters, Q&A, VLS/FBD Drill, Mock Exam)
    ├── Ethiek-/                              ← 15 study units (Ethiek 40% + Onderneming 40% + Dag m. Ing. 20%)
    ├── Obsidian_Vault_Wiskundige_Basistechnieken/ ← 80 study units (Deel 1-3, 15 Bewijzen, 24 Oefensessies, Q&A, Mocks)
    ├── SGDM/                                 ← 37 study units (Modules, Cases, Q&A, 9 Labo-notes)
    └── Spatial_Insight_and_CAD_Vault/        ← 28 study units (Ruimtelijk inzicht, CAD, IB1 70%-luik)
```

---

## 2. De Software & Plugins ("The Program")

Dit systeem is bewust afgestemd op de **exacte plugins** die actief zijn in jouw `.obsidian/` configuratie (`.obsidian/core-plugins.json` en `.obsidian/community-plugins.json`).

### 2.1 Core Plugins (Ingebouwd in Obsidian)
| Plugin | Status | Rol in het Groep T Systeem |
| :--- | :---: | :--- |
| **`bases`** (Obsidian Bases) | ✅ Aan | Motor achter [[00_Course_Progress_Base.base]] en [[00_Study_Hours_Base.base]]. Vervangt Dataview volledig met native tabellen, formules, groeperingen en sommaties. |
| **`properties`** | ✅ Aan | Geeft elke note bovenaan een nette formulier-UI om `completed`, `status`, `hrs_wiskunde`, enz. aan te passen zonder YAML-code te moeten typen. |
| **`canvas`** | ✅ Aan | Draait [[06_Groep_T_War_Room.canvas]] als visueel whiteboard. |
| **`daily-notes`** | ✅ Aan | Gekoppeld aan map `Daily_Journal` (`.obsidian/daily-notes.json`), formaat `YYYY-MM-DD`, template `Templates/Daily_Journal_Template.md`. |
| **`templates`** | ✅ Aan | Laat je handmatig templates (zoals [[Study_Logs/Study_Log_Template]]) invoegen in nieuwe notities. |
| **`bookmarks`** | ✅ Aan | Voor het vastpinnen van je Command Center, Sprint Plan en War Room Canvas in de linkerzijbalk. |
| **`switcher`** / **`global-search`** | ✅ Aan | Snel navigeren (`Ctrl/Cmd + O` voor bestanden, `Ctrl/Cmd + Shift + F` voor tekst zoeken). |
| **`graph`** / **`backlink`** / **`outline`** | ✅ Aan | Toont verbanden tussen theorie, bewijzen, Q&A's, oefensessies en labo's. |

> [!important] Waarom geen Dataview?
> Dataview is **niet geïnstalleerd** in deze vault. Alle dashboards zijn daarom gebouwd met **Obsidian Bases (`.base`)** en **YAML Properties**. Je hoeft dus geen extra community plugins te installeren: alles werkt out-of-the-box in moderne Obsidian.

### 2.2 Community Plugins
| Plugin ID | Waarvoor gebruikt in dit systeem |
| :--- | :--- |
| **`tasknotes`** | Beheert `#task`-taken met deadlines (`📅YYYY-MM-DD`), prioriteiten (`!high`) en projecten. In je Daily Journal is `![[TaskNotes/Views/agenda-default.base]]` al ingebed; extra views staan in `TaskNotes/Views/` (o.a. `tasks-default.base`, `kanban-default.base`, `pomodoro-stats.base`). |
| **`calendar`** | Geeft een kalender rechts in Obsidian waarmee je rechtstreeks naar eender welke dag in `Daily_Journal/` klikt. |
| **`obsidian-excalidraw-plugin`** | Ideaal om snel vrije-lichaamsschema's (VLS/FBD) voor **Dynamica**, projecties/CAD-schetsen voor **Ruimtelijk inzicht**, of Lewis-/VSEPR-structuren voor **Chemie** te tekenen en in te bedden. |
| **`obsidian-style-settings`** | Visuele theme-/stijlinstellingen van je vault. |
| **`quran-inserter`** | Gebruikt binnen je persoonlijke Daily Journal workflow. |

### 2.3 Het Python-Programma: `daily_journal.py`

In de root van je vault staat `daily_journal.py` — een zelfstandig Python 3 CLI-script dat automatisch dagelijkse journal- en studielog-pagina's genereert op basis van `Templates/Daily_Journal_Template.md`.

#### Wat doet het script?
1. Leest `Templates/Daily_Journal_Template.md` (met een ingebouwde `FALLBACK_TEMPLATE` als het bestand niet gevonden wordt).
2. Vervangt automatisch alle template-variabelen:
   - `{{date}}` / `{{title}}` $\to$ `YYYY-MM-DD`
   - `{{weekday}}` $\to$ naam van de weekdag (bv. `Sunday`)
   - `{{yesterday}}` / `{{tomorrow}}` $\to$ gisteren en morgen in `YYYY-MM-DD`
   - `{{year}}`, `{{month}}`, `{{day}}`, `{{time}}`
3. Schrijft het bestand weg naar `Daily_Journal/YYYY-MM-DD.md`. Bestaat dat bestand al, dan **overschrijft het niets** (tenzij `--force` wordt gebruikt), zodat je notities nooit verloren gaan.
4. Doordat `Daily_Journal_Template.md` nu automatisch de tag `study-log` en de velden `study_hours_total` + `hrs_*` bevat, verschijnt **elke gegenereerde dagnotitie automatisch in [[00_Study_Hours_Base.base]]**!

#### Alle CLI-commando's van `daily_journal.py`
Open een terminal in `/home/merlix/Documents/Obsidian_Vaults/Hunugs-vision` en gebruik:

| Commando | Effect |
| :--- | :--- |
| `python3 daily_journal.py` | Maakt de dagpagina voor **vandaag** aan (als hij nog niet bestaat). |
| `python3 daily_journal.py --date 2026-11-16` | Maakt de pagina voor een **specifieke datum** aan (`YYYY-MM-DD`). |
| `python3 daily_journal.py --tomorrow` | Bereidt de pagina voor **morgen** al voor. |
| `python3 daily_journal.py --list` | Toont een overzicht van alle bestaande dagnotities in `Daily_Journal/`. |
| `python3 daily_journal.py --install-cron` | Installeert een Linux cronjob die het script **elke dag om 06:00 AM** automatisch draait (logt naar `.journal_cron.log`). |
| `python3 daily_journal.py --force` | Overschrijft een bestaande dagpagina met een verse template *(voorzichtig: verwijdert handmatige invulling van die dag!)*. |

### 2.4 De All-in-One Companion Web App: `groep_t_app.py`

Naast `daily_journal.py` bevat je vault nu ook een **volledige lokale web-app** (`groep_t_app.py` + map `groep_t_app/`) die alle data uit Obsidian samenbrengt, live visualiseert én terugschrijft naar je Markdown-bestanden.

- **Starten (1 commando, zonder extra pip-packages):**
  ```bash
  python3 groep_t_app.py
  ```
  Opent automatisch op `http://127.0.0.1:8765` (gebruik `--port 8080` of `--no-open` indien gewenst, of `--export-only` om alleen JSON/CSV/Markdown-snapshots te updaten).
- **Belangrijkste functies:**
  - **📊 Consistency Heatmap & Grafieken:** GitHub-stijl kalenderheatmap (nov 2026 – jan 2027), gestapelde dagelijkse studiegrafiek met 6u-doellijn, urenverdeling per vak (donut) en focusscore-trendlijn.
  - **⏳ Pomodoro / Deep Work Timer & Live Logger:** Timer (25/50/90 min of stopwatch) die sessies direct wegschrijft naar `Daily_Journal/` of `Study_Logs/` (`hrs_*`, `study_hours_total`, focusscore + Markdown-tabelrij).
  - **✅ Live 270-Units Checklist & Note Reader:** Filter op vak/type/status/prioriteit, vink modules af (synchroniseert zowel de YAML-properties als [[02_Master_Course_Checklists]]) en voeg snelle notities toe aan eender welk `.md`-bestand.
  - **🎯 Examen Aftelklok & 90%-ECTS Simulator:** Simuleer je verwachte punten op `/20` om te zien of je veilig $\ge 27/30$ ECTS haalt + overzicht van verplichte labo's.
  - **🗂️ JSON, CSV & Obsidian Snapshot Export:** Synchroniseert automatisch `Groep T/study_telemetry.json`, `Groep T/study_logs_export.csv`, `Groep T/study_units_export.csv` en schrijft met één klik [[07_Study_Analytics_Snapshot]] rechtstreeks in Obsidian.
  - **🛠️ Technische Configuratie & API:** Zie [[00_Companion_App_Architecture_and_Config_Guide]] voor alle configuratiepunten, HTTP endpoints en troubleshooting.

---

## 3. Hoe de Live Databases & YAML Properties Werken

### 3.1 De 270 Studiemodules (`00_Course_Progress_Base.base`)

Elke les-, hoofdstuk-, oefensessie-, Q&A-, bewijs-, labo- en mock-exam-note in `Groep T/` bevat gestandaardiseerde YAML-frontmatter:

```yaml
---
course: "Wiskundige basistechnieken (T1AWB1)"
unit_type: "oefensessie"
status: "todo"
completed: false
est_hours: 1.5
priority: "high"
tags:
  - study-unit
---
```

#### Betekenis van elk veld
| Property | Mogelijke Waarden | Waarvoor gebruikt? |
| :--- | :--- | :--- |
| `course` | Exact 1 van de 7 namen:<br>• `"Ruimtelijk inzicht en CAD (T1AIB1)"`<br>• `"Dynamica en energie (T1ADE1)"`<br>• `"Computationeel Denken (T1ACD1)"`<br>• `"Wiskundige basistechnieken (T1AWB1)"`<br>• `"Chemie (T1ACH1)"`<br>• `"Onderneming en ethiek (T1AOE1)"`<br>• `"SGDM (T1ASD1)"` | Groepeert en sorteert alle modules per vak in Bases. |
| `unit_type` | `theory`, `kennisclip`, `oefensessie`, `qa`, `bewijs`, `labo`, `permanente-evaluatie`, `mock-exam`, `index` *(of `practice`/`summary` afhankelijk van module)* | Filtert aparte tabs in de Base (bv. *Oefensessies*, *Labs & Mandatory Evals*, *Theory & Kennisclips*). |
| `status` | `"todo"`, `"in-progress"`, `"done"` | Bepaalt het status-icoon (🔴 Todo, 🟡 In Progress, 🟢 Done). |
| `completed` | `true` of `false` (checkbox in Obsidian) | Zodra `completed: true` OF `status: "done"` staat, telt de unit als **afgerond** (`hoursLeft = 0`). |
| `est_hours` | Getal in uren (bv. `1.5`, `2.0`, `3.0`) | Geschatte studietijd. Als het leeg is, rekent de Base automatisch `1.5` uur via de formule `hoursLeft`. |
| `priority` | `"high"`, `"medium"`, `"low"` | Stuurt de sortering (`priorityRank`: `high` = 1, `medium` = 2, `low` = 3) zodat je altijd de belangrijkste vakken bovenaan ziet. |
| `tags` | Moet `study-unit` bevatten | Filtervoorwaarde van [[00_Course_Progress_Base.base]] (`file.hasTag("study-unit")`). |

#### De 6 ingebouwde Views van `00_Course_Progress_Base.base`
Klik bovenaan in de Base-tabel (of via het dropdown-menu linksboven in het ingebedde blok) om te wisselen tussen:
1. **All Courses Summary** — Alle 270 units gegroepeerd per vak, met som van *Done*, *Est. Hours* en *Hours Left*.
2. **Remaining (Todo)** — Alleen modules waarvoor `completed != true` én `status != "done"`, gesorteerd op prioriteit (`high` eerst). **Gebruik deze tab elke ochtend om te zien wat er nog open staat!**
3. **Labs & Mandatory Evals** — Alle `labo` en `permanente-evaluatie` units zodat je geen enkele verplichte sessie mist.
4. **Oefensessies** — Alle oefensessies per vak op een rij.
5. **Theory & Kennisclips** — Alle hoorcolleges en kennisclips.
6. **Completed** — Alles wat al afgevinkt is + totaal aantal afgeronde geschatte uren (handig voor motivatie!).

---

### 3.2 De Studie-Uren Tracker (`00_Study_Hours_Base.base`)

[[00_Study_Hours_Base.base]] scant automatisch elke note in je hele vault die **óf de tag `#study-log` heeft, óf de property `study_hours_total` bevat**. Dat werkt dus zowel voor `Daily_Journal/YYYY-MM-DD.md` als voor losse bestanden in `Groep T/Study_Logs/`.

#### De YAML-velden voor urenregistratie
```yaml
study_hours_total: 6.5
hrs_cad: 1.5
hrs_dynamica: 2.0
hrs_comp_denken: 0
hrs_wiskunde: 3.0
hrs_chemie: 0
hrs_sgdm: 0
hrs_ethiek: 0
study_focus_score: 8
```

#### Slimme formules in `00_Study_Hours_Base.base`
- **`subjectSum`**: Telt automatisch de 7 `hrs_*` vakvelden bij elkaar op.
- **`totalHours`**: Gebruikt `study_hours_total` als die `> 0` is, en valt anders automatisch terug op `subjectSum`. *(Tip: als je alleen de `hrs_*` velden invult en `study_hours_total` op `0` laat staan, berekent de Base zelf het exacte totaal!)*
- **`targetMet`** (Dagdoel-indicator voor jouw 30-dagen sprint):
  - $\ge 6.0$ uur $\to$ `✅ 6h+ Target`
  - $\ge 4.0$ uur $\to$ `🟡 4h+`
  - $> 0$ uur $\to$ `🟠 <4h`
  - $0$ uur $\to$ `🔴 0h`
- **2 Views:**
  1. **Daily Study Hours:** Elke dag als rij (nieuwste bovenaan), met totaalsom per vak onderaan + gemiddelde `Focus (1-10)`.
  2. **Weekly Totals:** Gegroepeerd per ISO-week (`YYYY-[W]WW`), ideaal om te controleren of je de geplande **45–52 uur/week** haalt.

> [!warning] Voorkom Dubbeltelling tussen `Daily_Journal/` en `Study_Logs/`!
> Omdat zowel `Daily_Journal/YYYY-MM-DD.md` als `Groep T/Study_Logs/YYYY-MM-DD.md` de tag `#study-log` dragen, moet je **één vaste plek** kiezen om je uren in te vullen (advies: gebruik gewoon je **Daily Journal**, omdat daar ook je gewoontes, gebeden en TaskNotes-agenda al in staan). Gebruik `Study_Logs/` alleen als je op een dag geen Daily Journal gebruikt — of laat de `hrs_*` velden in één van de twee op `0` staan.

---

## 4. Stap-voor-Stap Handleiding: Hoe Je Het Systeem Gebruikt

### Stap A: Eenmalige Setup (5 minuten)
1. **Open de vault** `/home/merlix/Documents/Obsidian_Vaults/Hunugs-vision` in Obsidian.
2. **Pin je startpagina's:** Open [[00_Groep_T_Command_Center]], klik rechtsboven op de drie puntjes $\to$ **Bookmark** (doe hetzelfde voor [[01_30_Day_Catchup_Sprint_Plan]] en [[06_Groep_T_War_Room.canvas]]).
3. **Activeer optioneel automatische dagpagina's:** Draai eenmalig in de terminal:
   ```bash
   python3 daily_journal.py --install-cron
   ```
   Vanaf dan staat elke ochtend om 06:00 uur jouw verse `Daily_Journal/YYYY-MM-DD.md` klaar (of open hem via de Calendar-plugin in Obsidian).
4. **Check je Properties-paneel:** Druk op `Ctrl/Cmd + P` $\to$ *"Properties view: Show file properties"* als je het Properties-blok bovenaan notities niet ziet.

---

### Stap B: Dagelijkse Workflow (Ochtend $\to$ Studiesessie $\to$ Avond)

#### 🌅 1. Ochtendstart (2 minuten)
1. Open vandaag in `Daily_Journal/` (bijv. [[Daily_Journal/2026-11-15]]).
2. Open [[01_30_Day_Catchup_Sprint_Plan]] en lees welke **Fase & Focusvakken** vandaag aan de beurt zijn (bijv. Fase 1: *Ruimtelijk Inzicht/CAD + Dynamica + Wiskunde Analyse*).
3. Vul onder *Groep T Daily Study Log* en *Most Important Tasks* in je Daily Journal maximaal **3 concrete blokken** in:
   - **Morning Deep Work (2.5–3u):** Moeilijk kernvak (Wiskunde / Dynamica / Chemie).
   - **Afternoon Practice (2–2.5u):** Oefensessie, Python-practicum of CAD-oefening.
   - **Evening Active Recall (1–1.5u):** Q&A-kaartjes, kennisclip of Onderneming & Ethiek lezen.

#### 🧠 2. Tijdens het Studeren (Per Module)
1. Ga naar [[00_Course_Progress_Base.base]] $\to$ tab **Remaining (Todo)** (of rechtstreeks via [[02_Master_Course_Checklists]]).
2. Klik op de notitie die je gaat doen (bv. een Chapter, Oefensessie, Q&A of Labo).
3. Zet in Properties bovenaan `status` naar `in-progress`.
4. **Werk de module af volgens de Groep T-methode:**
   - **Theory / Kennisclips:** Begrijp het kernprincipe, maak eigen notities in de markdown-file of teken schema's in Excalidraw.
   - **Q&A / Bewijzen:** Probeer het antwoord of bewijs **zonder spieken** op papier te schrijven vóór je naar de uitwerking kijkt.
   - **Oefensessies / Practica:** Maak zelf de opgaven op papier of in Python; noteer fouten meteen onderaan de notitie onder een kopje `## ⚠️ Valkuilen & Fouten`.
5. **Afronden:**
   - Klik het vinkvakje **`completed`** bovenaan in Properties aan (`true`) — *of vink het rechtstreeks aan in de Base-tabel!* — en zet `status` op `done`.
   - De module verdwijnt nu automatisch uit *Remaining (Todo)* en je resterende uren (`Hours Left`) zakken direct.
   - *(Optioneel)* Vink hem ook af in [[02_Master_Course_Checklists]] als visuele checklist.

#### 🌙 3. Avondafsluiting (2 minuten)
1. Ga naar de **Properties** bovenaan in je `Daily_Journal/YYYY-MM-DD.md`.
2. Vul bij elk vak waar je vandaag aan gewerkt hebt het aantal uren in (bv. `hrs_wiskunde: 3.0`, `hrs_dynamica: 2.0`, `hrs_cad: 1.5`) en je focusscore (`study_focus_score: 8`). Laat `study_hours_total` op `0` staan (dan telt de Base automatisch exact op) óf vul zelf het totaal in.
3. Bekijk in [[00_Groep_T_Command_Center]] hoe je dagdoel op **`✅ 6h+ Target`** springt.

---

### Stap C: Wekelijkse Zondag-Review (10 minuten)
Elke zondagavond:
1. Open [[00_Study_Hours_Base.base]] $\to$ tab **Weekly Totals**. Haalde je $\ge 42\text{–}48$ uur? Zo niet, kijk welk vak achterloopt (`hrs_*`-kolommen onderaan).
2. Open [[04_Labos_and_Permanente_Evaluatie_Hub]]. Check alle verplichte deadlines in de komende 14 dagen:
   - **Ruimtelijk inzicht & CAD:** Permanente Evaluatie **Sessie 6 (`07.12 – 17.12.2026`)** — geen examen in januari!
   - **Chemie:** Kennisclips + voorbereidende testen vóór Labo 1–6 en **Labo 6 Praktisch Labo Examen**.
   - **SGDM:** **ANS-voorbereidingstesten** + verplichte labo's & verslagen.
   - **Dynamica:** **VLS-tussentijdse test**.
   - **Computationeel Denken:** **Feedbacktest** + practica voor de **+1/20 bonus** + opbouwen van je **4-pagina handgeschreven samenvatting**.
   - **Onderneming en Ethiek:** **Dag met een Ingenieur** (interview + reflectieverslag = 20% van het vak) + Ethiek-paper (4/20).
3. Open [[00_Course_Progress_Base.base]] $\to$ tab **Remaining (Todo)** en bepaal je top-prioriteiten voor de volgende week.

---

### Stap D: Blok- & Examenstrategie (16 dec 2026 – 29 jan 2027)
Zodra de inhaalsprint op 15 december eindigt, verschuift je focus van *stof bijbenen* naar **Mock Exams & Past Exams in examenvolgorde** (zie [[exam_schedule]]):

1. **11 jan (`ma 08:30`) — Dynamica en energie (`T1ADE1`):** Gebruik [[VLS_FBD_Drill_Sheet]] + [[Mock_Exam_Dynamica]].
2. **12 jan (`di 08:30`) — Computationeel denken (`T1ACD1`):** *Back-to-back direct na Dynamica!* Werk vooraf in de kerstblok alle 3 de Mock Exams + je [[4_Pagina_Samenvatting_Werkblad]] al 100% af.
3. **16 jan (`za 08:30`) — Wiskundige basistechnieken (`T1AWB1` — 6 ECTS):** 3 dagen ertussen $\to$ herhaal de 15 bewijzen uit [[00 - Index der Bewijzen]] + maak Mock Exam 1–3 op tijd.
4. **19 jan (`di 12:30`) — Chemie (`T1ACH1` — 6 ECTS):** 2,5 dagen ertussen $\to$ focus op stoichiometrie, thermodynamica, kinetiek, evenwichten, zuren/basen en alle past exams (`Examen 12-01-2024`, enz.).
5. **21 jan (`do 12:30`) — Onderneming en ethiek (`T1AOE1`):** 1,5 dag ertussen $\to$ herhaal de Ethiek-modules + Onderneming (BMC, SWOT, Balans/Resultatenrekening/M.A.R.) + Oefeningen.
6. **29 jan (`vr 08:30`) — SGDM (`T1ASD1` — 6 ECTS):** 7 dagen ruimte $\to$ maximale herhaling + **let op de negatieve scoring / eliminatiemethode** op meerkeuzevragen!

---

## 5. Aanpassen, Uitbreiden & Troubleshooting

### Nieuwe studienote toevoegen zodat de Base hem meteen herkent
Plak dit bovenaan elke nieuwe cursusnotitie in `Groep T/`:
```yaml
---
course: "Chemie (T1ACH1)"
unit_type: "oefensessie"
status: "todo"
completed: false
est_hours: 1.5
priority: "medium"
tags:
  - study-unit
---
```
Gebruik precies één van de 7 bestaande `course`-strings zodat de Base geen apart groepje aanmaakt.

### Veelvoorkomende Problemen & Oplossingen
| Probleem | Oorzaak | Oplossing |
| :--- | :--- | :--- |
| `.base` bestand toont ruwe YAML-tekst i.p.v. tabel | Obsidian-versie te oud of Core Plugin **Bases** uitgeschakeld | Update Obsidian (v1.9+) en zet *Settings $\to$ Core Plugins $\to$ Bases* op **Aan**. |
| Uren van vandaag tellen niet op in `00_Study_Hours_Base.base` | Waarde ingevuld als tekst (`"2 uur"`) i.p.v. getal (`2` of `2.0`), of tag `study-log` ontbreekt | Vul alleen decimale getallen in (`2.5`) zonder eenheid, en controleer dat `study-log` in `tags` staat. |
| Uren lijken dubbel geteld | Zowel in `Daily_Journal/YYYY-MM-DD.md` als in `Study_Logs/YYYY-MM-DD.md` uren ingevuld | Zet in één van beide bestanden alle `hrs_*` en `study_hours_total` op `0`. |
| `python3 daily_journal.py` vindt template niet | Script gedraaid buiten de juiste map | Script gebruikt `SCRIPT_DIR` relatief t.o.v. zichzelf — controleer of `Templates/Daily_Journal_Template.md` bestaat. |
| Vreemde symbolen in Wiskunde/Chemie-formules | Oude LaTeX escape-fouten | De 11 gevonden bestanden zijn hersteld; zie je er nog één, open in **Reading View** of meld de bestandsnaam. |
