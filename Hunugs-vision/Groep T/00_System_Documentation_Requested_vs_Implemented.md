---
title: System Documentation — Requested vs. Implemented
tags:
  - documentation
  - groep-t
  - architecture
---

# 📋 Groep T Study OS — Wat Gevraagd Werd vs. Wat Geïmplementeerd Is

> 🏠 **[[00_Groep_T_Command_Center|← Terug naar Groep T Command Center]]** • **[[00_Complete_System_and_Program_User_Guide|📘 Uitgebreide Systeem- & Gebruikershandleiding]]**

---

## 1. Overzicht van Jouw Vraag

| Onderdeel van Jouw Verzoek | Hoe Het Geïmplementeerd Is | Locatie / Bestanden |
| :--- | :--- | :--- |
| **Volledig Obsidian studiesysteem voor 1ste jaar Groep T** | Centraal War Room Command Center + interactieve Canvas + 7 gekoppelde vakvaults | [[00_Groep_T_Command_Center]] • [[06_Groep_T_War_Room.canvas]] |
| **Grondig onderzoek naar elk Semester-1 vak** | Officieel KU Leuven onderzoek (ECTS, OPO/OLA-wegingen, examenvormen, negatieve scoring, verplichte evaluaties, 80/20 slaagplan voor alle 30 ECTS) | [[05_KU_Leuven_Groep_T_Course_Research]] |
| **~1 maand inhaalsprint vanaf nul (doel: $\ge 90\%$ slagen)** | Dag-per-dag 30-Dagen Inhaalsprint (15 nov – 15 dec) + Blok- en Examenexecutieplan (16 dec – 29 jan) | [[01_30_Day_Catchup_Sprint_Plan]] |
| **Dagelijkse studie-uren bijhouden** | Native **Obsidian Bases** dashboard (`00_Study_Hours_Base.base`) gekoppeld aan `Study_Logs/` én rechtstreeks geïntegreerd in je [[Templates/Daily_Journal_Template\|Daily Journal]] & `daily_journal.py` | [[03_Daily_Study_Hours_Tracker]] • [[00_Study_Hours_Base.base]] • [[Study_Logs/2026-11-15]] |
| **Checklist voor alle lesmateriaal, lectures & wat nog overblijft** | Master checklist over alle **270 studiemodules** + live **Obsidian Bases** voortgangsdatabase met resterende uren en status per vak | [[02_Master_Course_Checklists]] • [[00_Course_Progress_Base.base]] |
| **Alle onvolledige vakken aanvullen & kapotte structuur/links fixen** | Alle ontbrekende hoofdstukken, Q&A's, oefensessies, mock exams, Onderneming-luik (60% van `T1AOE1`), gebroken LaTeX-escapes en dode links opgelost | Zie Sectie 2 hieronder |
| **Labo's toevoegen** | Alle 9 Chemie labo-notes, alle 9 SGDM labo-notes, Python practica, Dynamica VLS-drill, Dag met een Ingenieur & Ruimtelijk Inzicht Permanente Evaluatie | [[04_Labos_and_Permanente_Evaluatie_Hub]] |
| **Examentijden uit `exam_schedule.md` integreren** | Examenrooster verrijkt met ECTS, aftelmatrix, rustdagen-analyse en urgente decemberdeadlines, gelinkt in elk vak en het Command Center | [[exam_schedule]] |
| **Aparte MD-file over wat gevraagd en geïmplementeerd is** | Dit document | [[00_System_Documentation_Requested_vs_Implemented]] |

---

## 2. Audit & Aanvullingen per Vak (Wat Ontbrak vs. Wat Toegevoegd Is)

### 2.1 Wiskundige Basistechnieken (`T1AWB1` — 6 ECTS)
- **Wat ontbrak / kapot was:**
  - Alle **9 hoofdstukken van Deel 3 - Analyse** ontbraken volledig.
  - **11 Active Recall Q&A-pagina's** en **20 van de 24 Oefensessies** ontbraken.
  - **3 Part MOC-pagina's** (`Deel 1`, `Deel 2`, `Deel 3`) en **3 Mock Exams** ontbraken.
  - **LaTeX-corruptie** (`\frac`, `\theta`, `\neq`, `\right`, `\arccos`, `\blacksquare`, `\begin`) in `00 - Index der Bewijzen.md`, `Bewijs 01`, `Bewijs 02`, `Bewijs 03`, `Exam Preparation.md`.
- **Geïmplementeerd:**
  - Alle 9 Analyse-hoofdstukken (`Ch 01` t.e.m. `Ch 09`) geschreven met volledige LaTeX-theorie en links naar de bewijzen.
  - Alle 11 ontbrekende Q&A-pagina's en alle 20 ontbrekende oefensessies aangemaakt.
  - 3 Deel-MOC's + 3 Mock Exams + Oplossingen & Rubric aangemaakt.
  - Alle LaTeX-escapes hersteld.

### 2.2 Chemie (`T1ACH1` — 6 ECTS)
- **Wat ontbrak / kapot was:**
  - Alle 9 notities gelinkt in [[chemie_labs]] ontbraken.
  - Tab/carriage-return corruptie in LaTeX (`\text`, `\rho`) in 6 bestanden.
- **Geïmplementeerd:**
  - Alle **9 labonotities** aangemaakt in `Chemie/06 - Labos/` ([[Praktische afspraken Chemie]], [[Kennisclips Chemie]], [[Testen Chemie]], [[Labo 1 Onbekend Metaal]] t.e.m. [[Labo 6 Praktisch labo examen]]).
  - LaTeX-escapes hersteld in alle 6 bestanden en `Chemie/00 - Meta/Index.md` bijgewerkt.

### 2.3 SGDM — Structuur, Gedrag en Duurzaamheid van Materialen (`T1ASD1` — 6 ECTS)
- **Wat ontbrak:**
  - Alle 9 labonotities gelinkt in [[sgdm_labs]] ontbraken.
- **Geïmplementeerd:**
  - Alle **9 SGDM-labonotities** aangemaakt in `SGDM/07_Labos/` (van [[Algemene informatie en introductie sessie SGDM]] en [[Labo voorbereiding testen ANS]] tot [[Labovaardigheden, foutentheorie en schrijfvaardigheden]] en [[Evaluatie en feedback SGDM]]).
  - `00_Overview_Dashboard.md` bijgewerkt met examen- & labolinks.

### 2.4 Onderneming en Ethiek (`T1AOE1` — 3 ECTS)
- **Wat ontbrak / kapot was:**
  - De vault bevatte enkel het luik **Ethiek (40%)** — het luik **Onderneming (40%)** en **Dag met een ingenieur (20%)** ontbraken volledig!
  - In `00_Course_Index.md` stonden 5 dode modulelinks door bestandsnaamverschillen.
- **Geïmplementeerd:**
  - Alle 5 links in `00_Course_Index.md` hersteld.
  - Nieuw `Ethiek-/05_Onderneming/` luik gebouwd met 4 theoriehoofdstukken (Rechtsvormen & BMC, Strategie/SWOT/Stakeholders, Leiderschap/Kotter/Motivatie, **Boekhouden/Balans/Resultatenrekening/M.A.R.**) + Q&A-oefeningen + [[Dag_met_een_Ingenieur_Opdracht_Tracker]] (direct gelinkt aan je interview-taak!).

### 2.5 Computationeel Denken (`T1ACD1` — 3 ECTS)
- **Wat ontbrak / kapot was:**
  - De 3 Mock Exam-bestanden gelinkt in `Exam Preparation.md` ontbraken.
  - `Index.md` had placeholder-wikilinks in het ASCII-diagram.
- **Geïmplementeerd:**
  - Alle 3 uitgewerkte Mock Exams ([[Past Exam 2024 - Semester 1 (Mock)|2024]], [[Past Exam 2025 - Semester 1 (Mock)|2025]], [[Past Exam - Herexamen Augustus (Mock)|Herexamen]]) + [[4_Pagina_Samenvatting_Werkblad]] + [[Practicum_en_Feedbacktest_Tracker]] aangemaakt en `Index.md` hersteld.

### 2.6 Dynamica en Energie (`T1ADE1` — 3 ECTS)
- **Geïmplementeerd:**
  - [[VLS_FBD_Drill_Sheet]] (voor de verplichte VLS-competenties) + [[Mock_Exam_Dynamica]] (3-uur examensimulatie met VLS & uitgewerkte oplossingen) toegevoegd aan `Dynamica_en_Energie_/00_Meta/`.

### 2.7 Ruimtelijk Inzicht en CAD / Ingenieursbeleving 1 (`T1AIB1`)
- **Geïmplementeerd:**
  - [[Ingenieursbeleving_1_Overview]] toegevoegd om de directe decemberdeadline (Permanente Evaluatie **Sessie 6: 07.12 – 17.12.2026**) én het 70%-luik scherp zichtbaar te maken.

---

## 3. Technische Architectuur & Compatibiliteit met Jouw Plugins

- **Obsidian Bases (`bases: true`):** Omdat Dataview niet geïnstalleerd is maar **Obsidian Bases** en **TaskNotes** wél actief zijn, gebruiken beide live dashboards ([[00_Study_Hours_Base.base]] en [[00_Course_Progress_Base.base]]) native `.base` YAML-queries. Alle **270 studiemodules** kregen uniforme YAML-properties (`course`, `unit_type`, `status`, `completed`, `est_hours`, `priority`, `study-unit`).
- **Daily Journal Integratie:** [[Templates/Daily_Journal_Template]] en `daily_journal.py` bevatten nu de velden `study_hours_total` en `hrs_<vak>`, zodat elke dagnotitie automatisch in [[00_Study_Hours_Base.base]] verschijnt.
- **Obsidian Canvas (`canvas: true`):** [[06_Groep_T_War_Room.canvas]] visualiseert het hele Semester-1 ecosysteem op één scherm.

---

## 4. Hoe Je Vandaag Start (Dagelijkse Workflow van 30 Seconden)

1. Open **[[00_Groep_T_Command_Center]]** (pin of bookmark deze pagina in Obsidian!).
2. Kijk in **[[01_30_Day_Catchup_Sprint_Plan]]** wat vandaag op de planning staat (Dag 1 = `zo 15/11`).
3. Werk je focusblokken af en log aan het einde van de dag je uren in [[Templates/Daily_Journal_Template|Daily Journal]] of [[Study_Logs/2026-11-15]].
4. Zet bij elke afgeronde note `completed: true` (of `status: done`) in Properties + vink af in [[02_Master_Course_Checklists]].
