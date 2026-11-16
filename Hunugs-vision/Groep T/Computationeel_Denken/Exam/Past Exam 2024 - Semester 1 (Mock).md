---
title: Past Exam 2024 - Semester 1 (Mock)
course: "Computationeel Denken (T1ACD1)"
unit_type: exam
status: todo
completed: false
est_hours: 2.5
priority: high
tags:
  - study-unit
  - python
  - mock-exam
---

# 💻 Mock Exam 2024 — Semester 1 (Computerexamen Simulatie)

> [!info] Simulatievoorwaarden
> - **Tijd:** 120 minuten (Python zonder internet/AI; enkel de [[4_Pagina_Samenvatting_Werkblad|4-pagina handgeschreven samenvatting]]!).
> - **Regel:** Gebruik `return`, NOOIT `print()` binnen een functie die een waarde moet teruggeven! Test met lege lijsten en randgevallen.

---

## Opgave 1: Functies & Branching (Energieverbruik)
Schrijf een functie `bereken_factuur(kwh_dag, kwh_nacht, is_sociaal_tarief)` die de elektriciteitskost berekent:
- Dagtarief: `€0.32/kWh`, Nachttarief: `€0.21/kWh`.
- Voor de eerste `100 kWh` dagverbruik geldt een korting van `10%`.
- Indien `is_sociaal_tarief` `True` is, wordt het totaalbedrag met `35%` verminderd.
- Geef het resultaat terug afgerond op 2 decimalen (`round(..., 2)`).

> [!success]- Modeluitwerking
> ```python
> def bereken_factuur(kwh_dag, kwh_nacht, is_sociaal_tarief):
>     if kwh_dag <= 100:
>         kost_dag = kwh_dag * 0.32 * 0.90
>     else:
>         kost_dag = 100 * 0.32 * 0.90 + (kwh_dag - 100) * 0.32
>     totaal = kost_dag + kwh_nacht * 0.21
>     if is_sociaal_tarief:
>         totaal *= 0.65
>     return round(totaal, 2)
> ```

---

## Opgave 2: 2D-Lijsten & Kolomverwerking (Sensordata)
Gegeven een 2D-lijst `metingen` (rijen = dagen, kolommen = sensoren). Schrijf een functie `defecte_sensoren(metingen, drempel)` die een lijst teruggeeft van alle **kolomindices** (sensornummers) waarvan het gemiddelde over alle dagen strikt groter is dan `drempel` of die minstens één negatieve meting bevatten.

> [!success]- Modeluitwerking
> ```python
> def defecte_sensoren(metingen, drempel):
>     if len(metingen) == 0 or len(metingen[0]) == 0:
>         return []
>     n_rijen = len(metingen)
>     n_kol = len(metingen[0])
>     resultaat = []
>     for k in range(n_kol):
>         som = 0
>         heeft_negatief = False
>         for r in range(n_rijen):
>             val = metingen[r][k]
>             som += val
>             if val < 0:
>                 heeft_negatief = True
>         gemiddelde = som / n_rijen
>         if heeft_negatief or gemiddelde > drempel:
>             resultaat.append(k)
>     return resultaat
> ```

---

## Opgave 3: File I/O & Dataverwerking
Gegeven een CSV-bestand `punten.csv` met lijnen `StudentNaam;Vak;Score`. Schrijf een functie `geslaagde_studenten(bestandsnaam, min_score)` die een lijst teruggeeft met de namen (zonder duplicaten!) van studenten die minstens één score $\ge$ `min_score` behaalden.

> [!success]- Modeluitwerking
> ```python
> def geslaagde_studenten(bestandsnaam, min_score):
>     geslaagd = []
>     with open(bestandsnaam, "r", encoding="utf-8") as f:
>         for lijn in f:
>             lijn = lijn.strip()
>             if lijn == "":
>                 continue
>             delen = lijn.split(";")
>             naam = delen[0]
>             score = float(delen[2])
>             if score >= min_score and naam not in geslaagd:
>                 geslaagd.append(naam)
>     return geslaagd
> ```
