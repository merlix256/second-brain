---
title: Past Exam - Herexamen Augustus (Mock)
course: "Computationeel Denken (T1ACD1)"
unit_type: exam
status: todo
completed: false
est_hours: 2.0
priority: medium
tags:
  - study-unit
  - python
  - mock-exam
---

# 💻 Mock Exam — Herexamen Simulatie (Integratie)

## Opgave: Temperatuurlogboek Verwerken & Filteren
Gegeven een tekstbestand `temps.txt` waarbij elke regel komma-gescheiden uurlijkse temperaturen van één dag bevat (bv. `12.5,14.0,15.2,...`).
1. Schrijf `lees_matrix(pad)` die het bestand inleest als een 2D-lijst van `float`s.
2. Schrijf `hittegolf_dagen(matrix, drempel)` die de **0-gebaseerde dagindices** teruggeeft waar de maximumtemperatuur $\ge$ `drempel` is én het gemiddelde $>$ `drempel - 3.0`.
3. Schrijf `schrijf_rapport(pad, dagen)` die per gevonden dag een regel `Dag X` wegschrijft naar een nieuw bestand.

> [!success]- Modeluitwerking
> ```python
> def lees_matrix(pad):
>     matrix = []
>     with open(pad, "r", encoding="utf-8") as f:
>         for lijn in f:
>             lijn = lijn.strip()
>             if lijn == "":
>                 continue
>             rij = []
>             for stuk in lijn.split(","):
>                 rij.append(float(stuk))
>             matrix.append(rij)
>     return matrix
>
> def hittegolf_dagen(matrix, drempel):
>     dagen = []
>     for i in range(len(matrix)):
>         rij = matrix[i]
>         if len(rij) == 0:
>             continue
>         mx = max(rij)
>         gem = sum(rij) / len(rij)
>         if mx >= drempel and gem > drempel - 3.0:
>             dagen.append(i)
>     return dagen
>
> def schrijf_rapport(pad, dagen):
>     with open(pad, "w", encoding="utf-8") as f:
>         for d in dagen:
>             f.write(f"Dag {d}\n")
> ```
