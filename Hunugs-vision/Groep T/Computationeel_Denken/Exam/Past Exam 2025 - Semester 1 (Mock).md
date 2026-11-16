---
title: Past Exam 2025 - Semester 1 (Mock)
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

# 💻 Mock Exam 2025 — Semester 1 (Computerexamen Simulatie)

## Opgave 1: Lussen & Reeksen (Collatz / Stopcriterium)
Schrijf `stappen_tot_een(n)` die voor een strikt positief geheel getal $n$ het aantal stappen teruggeeft tot $n = 1$ bereikt wordt (even $\to n // 2$, oneven $\to 3n + 1$). Geef `-1` terug als `n <= 0`.

> [!success]- Modeluitwerking
> ```python
> def stappen_tot_een(n):
>     if n <= 0:
>         return -1
>     stappen = 0
>     while n != 1:
>         if n % 2 == 0:
>             n = n // 2
>         else:
>             n = 3 * n + 1
>         stappen += 1
>     return stappen
> ```

---

## Opgave 2: 1D-Lijsten zonder Mutatie (Aliasing-trap!)
Schrijf `schuif_op(lijst, k)` die een **nieuwe** lijst teruggeeft waarin elk element `k` posities naar rechts is doorgeschoven (wrap-around), **zonder** de originele `lijst` te wijzigen!

> [!success]- Modeluitwerking
> ```python
> def schuif_op(lijst, k):
>     n = len(lijst)
>     if n == 0:
>         return []
>     k = k % n
>     nieuwe = [0] * n
>     for i in range(n):
>         nieuwe[(i + k) % n] = lijst[i]
>     return nieuwe
> ```

---

## Opgave 3: 2D-Matrix Transformatie (Diagonaal & Randen)
Schrijf `maak_omranding(R, C, waarde)` die een $R \times C$ matrix aanmaakt met `waarde` op alle randcellen (eerste/laatste rij, eerste/laatste kolom) en `0` binnenin. Gebruik correcte matrix-initialisatie (`[[0 for _ in range(C)] for _ in range(R)]`).

> [!success]- Modeluitwerking
> ```python
> def maak_omranding(R, C, waarde):
>     m = [[0 for _ in range(C)] for _ in range(R)]
>     for r in range(R):
>         for c in range(C):
>             if r == 0 or r == R - 1 or c == 0 or c == C - 1:
>                 m[r][c] = waarde
>     return m
> ```
