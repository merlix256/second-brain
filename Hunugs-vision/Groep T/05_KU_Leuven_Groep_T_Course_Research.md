---
title: KU Leuven Campus Groep T — Thorough Semester 1 Course Research
tags:
  - research
  - kuleuven
  - groep-t
  - strategy
---

# 🔬 Grondig Vakkenonderzoek — 1e Bachelor Industriële Ingenieurswetenschappen (Groep T, Semester 1)

> 🏠 **[[00_Groep_T_Command_Center|← Command Center]]** | **[[exam_schedule|📅 Examenrooster]]**
> *Gebaseerd op officiële KU Leuven ECTS-fiches (`onderwijsaanbod.kuleuven.be`), de examendata uit [[exam_schedule]], en de cursusinhouden in deze vault.*

---

## 📊 Totaaloverzicht Semester 1 (30 ECTS)

| OPO / Vak | Code | ECTS | Evaluatievorm & Weging | Grootste Valkuil / Slaagkriterium |
| :--- | :--- | :-: | :--- | :--- |
| **Dynamica en energie** | `T1ADE1` | 3 | 100% Schriftelijk examen (3u) + VLS-toetsing | Fouten in VLS/FBD maken vervolgberekening waardeloos; constante vs. variabele versnelling verwarren |
| **Computationeel denken** | `T1ACD1` | 3 | Computerexamen Python + (+1/20 aanwezigheidsbonus) | `print()` i.p.v. `return` gebruiken; aliasing bij lijsten/2D-matrices; back-to-back met Dynamica! |
| **Wiskundige basistechnieken** | `T1AWB1` | 6 | Theorie (incl. 15 vaste bewijzen) + Oefeningen | Bewijzen verwaarlozen; rekenfouten bij parameterstelsels & delen zonder $a=0$ check; integralen zonder splitsing |
| **Chemie** | `T1ACH1` | 6 | Schriftelijk examen (hc+oef) + Labo's (incl. praktisch examen) | J vs. kJ mengen; $C_{\text{cal}}$ vergeten; $R=0.08206$ vs $8.314$; eenheden/aggregatietoestand weglaten |
| **Onderneming en ethiek** | `T1AOE1` | 3 | **3 OLA's:** Onderneming (40%) + Ethiek (40%: 16/20 ex + 4/20 paper) + Dag m. Ing. (20%) | De 60% buiten Lauwaert vergeten (Onderneming balans/M.A.R. + Dag m. Ing.); giscorrectie op MC; sjablonen niet volgen |
| **SGDM** | `T1ASD1` | 6 | 5 ECTS hc/oef (Schriftelijk examen met **eliminatiemethode!**) + 1 ECTS Labo | **Negatieve puntentelling / eliminatiemethode** (blind gokken kost punten!); labo NA door afwezigheid of slechte foutenanalyse |
| **Ingenieursbeleving 1** *(incl. Ruimtelijk Inzicht & CAD)* | `T1AIB1` | 3* | **Permanente Evaluatie** (30% Ruimtelijk Inzicht & CAD + 70% Geïnt. labo/project/seminaries) | **Geen januari-examen!** Deadline al in **december (Sessie 6 verplicht!)**; normen/lijnsoorten/arceringen niet kennen |

---

## 🔍 Diepte-Analyse per Vak (80/20 Slaaggids)

### 1. Dynamica en energie (`T1ADE1` — 3 ECTS | ma 11.01.2027, 08:30)
- **Coördinator / Docenten:** Prof. Luc Labey & Prof. Kathleen Denis (Handboek: Hibbeler *Dynamics* H12–15).
- **Toegestaan materiaal:** Officieel formularium + wetenschappelijk rekentoestel.
- **Waarom studenten zakken:** Ze proberen formules te gokken zonder tekenen van een **VLS (Vrijlichaamsschema)** + **KS (Kinetisch Schema)**.
- **80/20 Actie:**
  1. Beheers blindelings de 3 stappen: *Kinematica* ($a\,ds=v\,dv$, relatieve beweging) $\to$ *Kinetica* ($\sum F = ma$ in $x$-$y$ en $t$-$n$) $\to$ *Energie & Momentum* ($T_1+U=T_2$, $m_1 v_1 + m_2 v_2$, restitutie $e$).
  2. Oefen [[VLS_FBD_Drill_Sheet]] en maak [[Mock_Exam_Dynamica]] op tijd.

### 2. Computationeel denken (`T1ACD1` — 3 ECTS | di 12.01.2027, 08:30)
- **Docenten:** Nigel Vinckier, Ingmar Malfait, Hannelore Strauven, Jeroen Wauters.
- **Toegestaan materiaal:** **Maximaal 4 handgeschreven bladzijden (2 A4-vellen)**!
- **Critisch Examenfeit:** Dit examen valt **de dag na Dynamica**! Je hebt <24 uur ertussen. Daarom moet Python **vóór 8 januari** af zijn.
- **80/20 Actie:**
  1. Bouw je [[4_Pagina_Samenvatting_Werkblad|4-pagina samenvatting]] terwijl je Sessies 4–9 inhaalt.
  2. Beheers 100% zeker: `return` vs `print`, `for`/`while`-lussen, slicing & `.copy()`, **2D-lijst initialisatie** (`[[0 for _ in range(C)] for _ in range(R)]`), en CSV lezen via `with open(...)` + `.strip().split()`.
  3. Maak alle 3 mock exams ([[Past Exam 2024 - Semester 1 (Mock)|2024]], [[Past Exam 2025 - Semester 1 (Mock)|2025]], [[Past Exam - Herexamen Augustus (Mock)|Herexamen]]).

### 3. Wiskundige basistechnieken (`T1AWB1` — 6 ECTS | za 16.01.2027, 08:30)
- **Titularis:** Prof. dr. ir. Toon van Waterschoot.
- **Structuur:** 3 grote delen (Analytische Meetkunde, Lineaire Algebra, Analyse) met een zwaar **theorieluik (15 officiële bewijzen)** én een **oefeningenluik**.
- **80/20 Actie:**
  1. De **[[00 - Index der Bewijzen|15 Examenbewijzen]]** zijn gegarandeerde punten als je ze vooraf instudeert! Start hier vroeg mee (1–2 bewijzen per dag).
  2. Top-priority oefentypes: *Rechtenbundels/vlakkenwaaiers*, *Parameterstelsels ($a$ splitsen!)*, *Gram-Schmidt & kleinste kwadraten*, *Limieten (l'Hôpital)*, *Reeksen + randpunten machtreeksen*, *Integralen (partieel + partieelbreuken na veeltermdeling!)*.

### 4. Chemie (`T1ACH1` — 6 ECTS | di 19.01.2027, 12:30)
- **Coördinator:** Prof. Mignon Arn.
- **Structuur:** Introductiecursus (HS 1–5) + Algemene Chemie (HS 6–16) + **6 verplichte Labo's incl. praktisch labo-examen**.
- **80/20 Actie:**
  1. Onderschat HS 1–5 (naamgeving, redox, stoichiometrie) niet: alles daarna bouwt erop voort!
  2. Zorg voor snelle winst op de vaste examenblokken: Calorimetrie (met $C_{\text{cal}}$!), Lewis/VSEPR/Hybridisatie + IMK-vergelijkingen, Kinetica (snelheidswetten & Arrhenius), Evenwicht ($K_c, K_p$, Le Châtelier) & Zuur-Base/Buffers (pH + Henderson-Hasselbalch).
  3. Loop [[Examen 12-01-2024]] nauwkeurig na en rond [[chemie_labs]] puntloos af.

### 5. Onderneming en ethiek (`T1AOE1` — 3 ECTS | do 21.01.2027, 12:30)
- **Coördinator:** Geert Waeyenbergh | Ethiek: Prof. Lode Lauwaert.
- **Cruciale Weging:**
  - **40% Onderneming** (Rechtsvormen, BMC, SWOT/Strategie, Leiderschap/Kotter, **Boekhouden/Balans/Resultatenrekening/M.A.R.**)
  - **40% Ethiek** (16/20 schriftelijk + 4/20 paper; vereist de **[[01_Exam_Templates|4 exacte antwoordsjablonen van Lauwaert]]** + let op **giscorrectie** bij MC!)
  - **20% Dag met een ingenieur** (Interview + groepsverslag)
- **80/20 Actie:** Dit is een van de hoogste-rendement vakken om **14–17/20** op te scoren als je zowel de 20% opdracht, de 4/20 paper, de 4 Lauwaert-sjablonen als balans/M.A.R. meepakt!

### 6. Structuur, Gedrag en Duurzaamheid van Materialen (`T1ASD1` — 6 ECTS | vr 29.01.2027, 08:30)
- **Structuur:** 5 ECTS Hoorcollege/Oefeningen (handboek Ashby H01–H22 selectie) + **1 ECTS Labo (verplicht!)**.
- **Critische Examenregel:** Meerkeuzevragen gebruiken de **eliminatiemethode / negatieve scoring**! Raad nooit blind; schrap zekere fouten eerst (zie [[Exam_Strategy_and_Tips]]).
- **80/20 Actie:** Je hebt **7.5 volle blokdagen** na Ethiek! Leg in december het fundament (H01–H15 + Labo's + ANS-testen) en stamp/oefen tussen 22–28 jan de formules ($K_I = Y\sigma\sqrt{\pi a}$, Hall-Petch, Fick, hefboomregel, Miner, kruip, Ashby-indices).

### 7. Ruimtelijk inzicht en CAD / Ingenieursbeleving 1 (`T1AIB1` — 30% van 3 ECTS / 1e sem)
- **Blended learning:** Kennisclips 01–14 + Cursusboek + 6 Oefensessies + 3 ANS-testen.
- **Urgentie:** **Sessie 6 (Permanente Evaluatie)** is al tussen **07.12 en 17.12.2026**! Er is géén januari-examen om dit nog uit te stellen.
- **80/20 Actie:** Werk Clips 01–14 en Oefensessies 1–4 af in de **komende 10 dagen**, want met potlood, geodriehoek en ISO-regels kun je dit vlot binnenhalen.
