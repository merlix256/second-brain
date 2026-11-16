---
course: "Wiskundige basistechnieken (T1AWB1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: high
tags:
  - study-unit
---

# Hoofdstuk 2: Matrices en Echelonvormen

> [!abstract] Context
> Dit hoofdstuk behandelt reële matrices, bewerkingen, getransponeerde matrices, elementaire rij-operaties en de herleiding naar (canonieke) rij-echelonvorm.
> **Parent MOC:** [[Index]] | **Q&A:** [[Q&A - LinAlg Ch 02 Matrices]] | **Oefeningen:** [[Oefensessie 03 - Matrices I (Algebraïsche Bewerkingen)]]

---

## 1. Definities en Matrixbewerkingen
Een $(m \times n)$-matrix $A = [a_{ij}]$ heeft $m$ rijen en $n$ kolommen.
- **Optelling:** $(A + B)_{ij} = a_{ij} + b_{ij}$ (alleen voor gelijke afmetingen).
- **Scalaire vermenigvuldiging:** $(kA)_{ij} = k a_{ij}$.
- **Matrixproduct:** Als $A \in \mathbb{R}^{m \times p}$ en $B \in \mathbb{R}^{p \times n}$, dan is $C = AB \in \mathbb{R}^{m \times n}$ met:
  $$c_{ij} = \sum_{k=1}^p a_{ik} b_{kj}$$
  > [!warning] Niet-commutatief!
  > In het algemeen geldt $AB \neq BA$.

- **Getransponeerde Matrix:** $A^T$ ontstaat door rijen en kolommen te wisselen: $(A^T)_{ij} = a_{ji}$.
  - Eigenschap: $(AB)^T = B^T A^T$.
  - Symmetrisch als $A^T = A$; Scheefsymmetrisch als $A^T = -A$.

---

## 2. Elementaire Rij-operaties en Elementaire Matrices
De drie toegelaten bewerkingen op rijen:
1. $R_i \leftrightarrow R_j$: Verwisselen van twee rijen.
2. $k R_i$ ($k \neq 0$): Vermenigvuldigen van een rij met een scalair.
3. $R_i + k R_j$: Optellen van een scalair veelvoud van rij $j$ bij rij $i$.

Elke elementaire rij-operatie komt overeen met het links vermenigvuldigen met een elementaire matrix $E$: $A \to EA$.

---

## 3. Rij-echelonvormen en Rang
### 3.1 Rij-echelonvorm (REF)
Een matrix staat in echelonvorm als:
1. Eventuele nulrijen onderaan staan.
2. Het eerste niet-nul element van een rij (spilelement of pivot) strikt rechts staat van het spilelement van de vorige rij.

### 3.2 Gereduceerde / Canonieke Rij-echelonvorm (RREF)
Een matrix staat in canonieke echelonvorm als bijkomend:
1. Elk spilelement gelijk is aan $1$.
2. Elk spilelement het enige niet-nul element in zijn kolom is.

> [!tip] Eigenschap
> Elke matrix heeft oneindig veel echelonvormen, maar **precies één unieke canonieke echelonvorm**.

### 3.3 Rang van een Matrix
$$\text{rang}(A) = \text{aantal niet-nulrijen in de echelonvorm van } A$$
- Het geeft het aantal lineair onafhankelijke rijen (en kolommen) weer.

---

> [!summary] Kernsamenvatting
> - Matrixvermenigvuldiging is associatief maar niet commutatief; inversie van producten volgt $(AB)^T = B^T A^T$.
> - Elementaire rij-operaties bewaren de oplossingsruimte van lineaire systemen.
> - De rang van een matrix is invariant onder rij-operaties en fundamenteel voor oplosbaarheid van stelsels.
