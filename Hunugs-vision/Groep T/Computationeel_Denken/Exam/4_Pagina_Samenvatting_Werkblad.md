---
title: 4-Pagina Handgeschreven Samenvatting Werkblad
course: "Computationeel Denken (T1ACD1)"
unit_type: exam
status: todo
completed: false
est_hours: 2.0
priority: high
tags:
  - study-unit
  - python
  - cheat-sheet
---

# 📝 Werkblad: Jouw 4-Pagina Handgeschreven Samenvatting

> [!important] Officieel Reglement (KU Leuven Groep T)
> Je mag op het computerexamen **maximaal 4 handgeschreven bladzijden (2 A4-vellen voor- en achterkant)** meenemen! Schrijf ze zelf met de hand: het schrijven zelf is al 50% van de herhaling!

---

## 📄 Bladzijde 1: Basis, Types & Branching (Sessie 1–2)
- `//` (gehele deling), `%` (modulo), `**` (macht), `int()`, `float()`, `str()`, `bool()`
- Prioriteit operatoren: `**` $\to$ `*, /, //, %` $\to$ `+, -` $\to$ `<, <=, ==, !=` $\to$ `not` $\to$ `and` $\to$ `or`
- Wetten van De Morgan: `not (A and B) == (not A) or (not B)`
- `if / elif / else` vs. meerdere aparte `if`s!

## 📄 Bladzijde 2: Functies, Scope & Return (Sessie 3–4)
- `def naam(param1, param2=default):` (defaultwaarden altijd achteraan!)
- `return` stopt de functie meteen en geeft waarde terug; `print()` toont enkel op scherm en geeft `None` terug!
- Scope: lokale variabelen bestaan enkel binnen de functie. Pas geen globale variabelen aan; geef parameters mee!
- Debugger: breakpoints, *Step Over* vs. *Step Into*, Call Stack inspecteren.

## 📄 Bladzijde 3: Lussen & 1D-Lijsten (Sessie 5–6)
- `for i in range(start, stop, step):` (`stop` is **exclusief**!)
- `while` met stopconditie (voorkom oneindige lus!) + `break` / `continue`
- Slicing: `L[start:stop:step]`, omkeren: `L[::-1]`, kopiëren: `L.copy()` of `L[:]`
- Lijstmethodes: `.append(x)`, `.insert(i, x)`, `.pop(i)`, `.remove(x)`, `len(L)`, `sum(L)`, `min(L)`, `max(L)`
- **Aliasing trap:** `b = a` wijst naar dezelfde lijst; gebruik `b = a.copy()`!

## 📄 Bladzijde 4: 2D-Lijsten & File I/O (Sessie 8–9)
- **Veilige 2D-matrix:** `m = [[0 for _ in range(C)] for _ in range(R)]` (NOOIT `[[0]*C]*R`!)
- **Rij-per-rij:** `for r in range(len(m)): for c in range(len(m[0])):`
- **Kolom-per-kolom:** buitenste lus over `c in range(len(m[0]))`, binnenste over `r in range(len(m))`!
- **Lezen:**
  ```python
  with open(pad, "r", encoding="utf-8") as f:
      for lijn in f:
          delen = lijn.strip().split(",")
  ```
- **Schrijven:** `with open(pad, "w", encoding="utf-8") as f: f.write(... + "\n")`

## ✅ Klaar-Checklist
- [ ] Alle 4 zijden met de hand uitgeschreven op 2 A4-vellen
- [ ] Gebruikt tijdens het maken van alle 3 de Mock Exams!
