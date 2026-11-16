# 🎯 SGDM Examenstrategie & Master Tips
#examen #strategie #eliminatiemethode #tips

Het examen *Structuur, Gedrag en Duurzaamheid van Materialen* (SGDM) aan KU Leuven Campus Group T hanteert een specifiek puntensysteem: de **Eliminatiemethode**. Een foutieve inschatting van dit systeem kost jaarlijks tientallen studenten punten.

---

## ⚖️ 1. Het Scoresysteem: Wiskundige Analyse

Bij elke meerkeuzevraag zijn er 4 opties (A, B, C, D) waarvan er **exact één** juist is. Je moet op het antwoordblad voor elke optie aangeven of het **"kan"** (bolletje inkleuren) of **"kan niet"** is.

### De Scoretabel

| Aantal opties aangeduid als "kan" | Juiste antwoord zit erbij? | Score |
| :---: | :---: | :---: |
| **1 optie** (Zuiver kiezen) | **JA** | **+1.00 pt** |
| 1 optie | NEEN | **-0.33 pt** |
| **2 opties** (Twijfel / Hedging) | **JA** | **+0.33 pt** |
| 2 opties | NEEN | **-0.33 pt** |
| **3 opties** (Uitsluiten van 1) | **JA** | **+0.11 pt** ($+1/9$) |
| 3 opties | NEEN | **-0.33 pt** |
| **4 opties** (of blanco gelaten) | — | **0.00 pt** |

---

## 🧮 2. Verwachtingswaarde (Expected Value - EV) & Beslisboom

### Scenario A: Je weet het 100% zeker
* Duid **1 optie** aan $\implies$ **Score: +1 pt**.

### Scenario B: Je twijfelt tussen 2 opties (50% kans per optie)
* **Strategie 1: Gokken op 1 optie**:
  $$\mathbb{E} = 0.5 \times (+1.00) + 0.5 \times (-0.33) = +0.50 - 0.167 = \mathbf{+0.333\text{ pt}}$$
* **Strategie 2: Duid BEIDE opties aan**:
  Omdat het juiste antwoord er gegarandeerd bij zit:
  $$\text{Score} = \mathbf{+0.333\text{ pt}}$$
* 💡 **Strategisch Inzicht**: De verwachtingswaarde is identiek ($+1/3$), maar Strategie 2 heeft een **variantie van 0**! Je elimineert elk risico op een negatieve score van $-0.33$. Als je een solide voldoende wilt behalen, duid je bij twijfel tussen 2 altijd **allebei** aan!

### Scenario C: Je kunt slechts 1 foute optie uitsluiten (keuze uit 3)
* Als je zuiver gokt op 1: $\mathbb{E} = \frac{1}{3}(1) + \frac{2}{3}(-1/3) = \frac{1}{3} - \frac{2}{9} = \mathbf{+0.111\text{ pt}}$
* Als je de 3 overblijvende aanduidt: $\text{Score} = \mathbf{+0.111\text{ pt}}$
* Ook hier geldt: 3 opties aanduiden levert gegarandeerd $+1/9$ pt op zonder enig risico op $-1/3$ strafpunten!

### Scenario D: Volstrekt geen idee (volledig blind)
* Duid **alle 4 opties aan** (of laat blanco) $\implies$ **0.00 pt**.
* *(Zuiver gokken op 1 optie geeft $\mathbb{E} = \frac{1}{4}(1) + \frac{3}{4}(-1/3) = 0$, maar met 75% kans op een verlies van 0.33 pt).*

---

## 🚫 3. Veelgemaakte Fouten & Formele Regels

1. **Inkleuren met balpen**: Gebruik een **zwarte of blauwe balpen**, geen potlood! Kleur het bolletje volledig in. Geen vinkjes ($\checkmark$) of kruisjes ($\times$).
2. **Correcties**: Fout gemaakt? Gebruik correctievloeistof (Tipp-Ex) netjes, of wis volgens instructie. Herteken nooit de kadertjes!
3. **Ongeldig antwoorden**:
   * Zowel "kan" als "kan niet" voor dezelfde letter inkleuren $\implies$ fout/twijfelgeval wordt manueel geïnterpreteerd als "kan".
   * Niets aanduiden voor een letter $\implies$ leidt tot interpretatieproblemen.
4. **Alleen het antwoordblad telt**: Berekeningen of antwoorden aangeduid in de vragenbundel worden genegeerd. Schrijf alles op tijd over!

---

## ⏱️ 4. Tijdmanagement (3 Uur = 180 Minuten voor ~28 Vragen)

* **Ronde 1 (0 – 75 min): Quick Wins (Theorie & Conceptvragen)**
  Beantwoord alle zuivere theorievragen, begripsdefinities en eenvoudige aflezingen (Ashby, fasen tellen). Wees meedogenloos: duid aan wat je zeker weet (+1).
* **Ronde 2 (75 – 140 min): Rekenintensieve Opgaven**
  Pak de complexe berekeningen aan: hefboomregel, $K_I$ en scheurlengte $a_c$, Poisson-contractie, Wöhler vermoeiingscycli, Schmid-factor.
* **Ronde 3 (140 – 170 min): Eliminatie-Audit & Risicobeheer**
  Overloop alle openstaande vragen. Pas de wiskundige hedging toe: twijfel tussen 2 $\implies$ duid 2 aan (+1/3). Weet je het echt niet $\implies$ duid alle 4 aan (0 pt).
* **Ronde 4 (170 – 180 min): Eindcontrole & Matrix Overdracht**
  Controleer of je studentennummer en r-nummer correct gecodeerd zijn in de matrix op pagina 1 van het antwoordblad.
