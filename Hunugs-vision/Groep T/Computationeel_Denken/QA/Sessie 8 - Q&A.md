---
course: "Computationeel Denken (T1ACD1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.0
priority: medium
tags:
  - study-unit
---

# Sessie 8 - Q&A (Active Recall)

> **Verwijzingen:** [[Sessie 8 - 2D-lijsten]] | [[Oefensessie 8]] | [[Index]]

---

### Vraag 1: Waarom leidt `m = [[0] * 3] * 3` tot fouten en wat is de juiste manier om een matrix van $R \times C$ nullen te maken?
**Antwoord:**
De expressie `[0] * 3` creëert één lijst in het geheugen met drie nullen. De buitenste `* 3` maakt vervolgens een lijst met drie referenties die **alle drie naar diezelfde ene lijst** wijzen. Wordt `m[0][0] = 5` uitgevoerd, dan worden `m[1][0]` en `m[2][0]` eveneens 5.
De correcte methode maakt voor elke rij een nieuw object via een list comprehension:
```python
m = [[0 for _ in range(C)] for _ in range(R)]
```
*Theorielink:* [[Sessie 8 - 2D-lijsten#3. Initialisatie en de 'Aliasing Trap']]

---

### Vraag 2: Hoe itereer je kolom-per-kolom over een rechthoekige matrix $M$?
**Antwoord:**
Laat de buitenste lus lopen over de kolomindex $c$ van $0$ tot $C-1$ en de binnenste lus over de rij-index $r$ van $0$ tot $R-1$:
```python
R = len(matrix)
C = len(matrix[0])
for c in range(C):
    for r in range(R):
        element = matrix[r][c]
```
*Theorielink:* [[Sessie 8 - 2D-lijsten#4.2 Kolom-per-kolom (Column-major traversal)]]

---

### Vraag 3: Hoe bereken je de som van de hoofddiagonaal van een vierkante matrix van $n \times n$?
**Antwoord:**
Op de hoofddiagonaal geldt dat de rij-index gelijk is aan de kolom-index ($r = c$):
```python
som_diagonaal = 0
for i in range(len(matrix)):
    som_diagonaal += matrix[i][i]
```
Dit vergt slechts één lus met complexiteit $\mathcal{O}(n)$, i.p.v. een geneste lus $\mathcal{O}(n^2)$ met een `if r == c` conditie.
*Theorielink:* [[Sessie 8 - 2D-lijsten#2. Elementen Aanspreken en Afmetingen]]