---
course: "Computationeel Denken (T1ACD1)"
unit_type: oefensessie
status: todo
completed: false
est_hours: 2.0
priority: high
tags:
  - study-unit
---

# Oefensessie 8: 2D-Lijsten & Matrices

> **Navigatie:** [[Index]] | [[Exercise Session Tracker]] | [[Sessie 8 - 2D-lijsten]] | [[Sessie 8 - Q&A]]

---

## 🎯 Doelstellingen
- Aanmaken van 2D-lijsten zonder aliasing-artefacten.
- Toepassen van dubbele geneste lussen voor rij- en kolomoperaties.
- Transponeren en vermenigvuldigen van matrices.

---

## 🛠️ Praktijkopgaven

### Opgave 8.1: Matrix Transpositie
**Probleemstelling:**
Schrijf een functie `transponeer_matrix(matrix)` die een $R \times C$ matrix omzet naar een getransponeerde $C \times R$ matrix $\mathbf{M}^T$, waarbij:
$$(\mathbf{M}^T)_{c, r} = \mathbf{M}_{r, c}$$

- **Vereiste Theoretische Concepten:**
  - Veilige matrixinitialisatie: [[Sessie 8 - 2D-lijsten#3.1 De Correcte Manier: List Comprehension of Geneste Lussen]]
  - Dubbele indexering `matrix[r][c]`: [[Sessie 8 - 2D-lijsten#2. Elementen Aanspreken en Afmetingen]]
  - Row- vs Column-major traversal: [[Sessie 8 - 2D-lijsten#4. Itereren over 2D-Lijsten]]

---

### Opgave 8.2: Conway's Game of Life (Buren Tellen)
**Probleemstelling:**
Gegeven een 2D-rooster van $R \times C$ cellen gevuld met `0` (dood) en `1` (levend). Schrijf een hulpfunctie `tel_levende_buren(grid, r, c)` die voor de cel op rij $r$ en kolom $c$ telt hoeveel van de 8 omliggende buren levend zijn. Let op de randen van het rooster!

- **Vereiste Theoretische Concepten:**
  - 2D-roostercoördinaten: [[Sessie 8 - 2D-lijsten#1. Matrices en Tweedimensionale Data]]
  - Randcondities & Bounds checking: [[Sessie 2 - Variabelen en Branching Controlestructuren#3. Conditionele Branching (if, elif, else)]]