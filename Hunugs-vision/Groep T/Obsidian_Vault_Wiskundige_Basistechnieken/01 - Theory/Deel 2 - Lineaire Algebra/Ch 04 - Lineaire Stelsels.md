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

# Hoofdstuk 4: Lineaire Stelsels

> [!abstract] Context
> Dit hoofdstuk behandelt het oplossen van stelsels lineaire vergelijkingen via Gauss en Gauss-Jordan eliminatie, stelsels met parameters, de stelling van Rouché-Capelli en de methode van Cramer.
> **Parent MOC:** [[Index]] | **Q&A:** [[Q&A - LinAlg Ch 04 Lineaire Stelsels]] | **Oefeningen:** [[Oefensessie 09 - Lineaire Stelsels]]

---

## 1. Algemene Vorm en Matrixnotatie
Een stelsel van $m$ lineaire vergelijkingen met $n$ onbekenden:
$$A \mathbf{x} = \mathbf{b}$$
met coëfficiëntenmatrix $A \in \mathbb{R}^{m \times n}$, onbekendenvector $\mathbf{x} \in \mathbb{R}^n$, en rechterlid $\mathbf{b} \in \mathbb{R}^m$.
De uitgebreide matrix is $[A \mid \mathbf{b}]$.

---

## 2. Oplosbaarheid: Stelling van Rouché-Capelli
Een stelsel $A\mathbf{x} = \mathbf{b}$ is oplosbaar (compatibel) $\iff$:
$$\text{rang}(A) = \text{rang}([A \mid \mathbf{b}])$$
- **Unieke oplossing:** $\text{rang}(A) = \text{rang}([A \mid \mathbf{b}]) = n$ (aantal onbekenden).
- **Oneindig veel oplossingen:** $\text{rang}(A) = \text{rang}([A \mid \mathbf{b}]) = r < n$. Aantal vrije parameters (vrijheidsgraad) is $n - r$.
- **Strijdig (geen oplossing):** $\text{rang}(A) < \text{rang}([A \mid \mathbf{b}])$.

---

## 3. Oplossingsmethoden
### 3.1 Gauss-eliminatie
Herleid $[A \mid \mathbf{b}]$ naar rij-echelonvorm (REF) en los op via achterwaartse substitutie.

### 3.2 Gauss-Jordan eliminatie
Herleid $[A \mid \mathbf{b}]$ naar canonieke rij-echelonvorm (RREF). De oplossingen kunnen direct worden afgelezen.

### 3.3 Methode van Cramer (voor vierkante stelsels $n \times n$ met $\det(A) \neq 0$)
$$x_j = \frac{\det(A_j)}{\det(A)}$$
waarbij $A_j$ de matrix is waarin de $j$-de kolom vervangen is door de vector $\mathbf{b}$.

---

## 4. Stelsels met Parameters
Bij stelsels met een parameter (bv. $a, k$) moeten gevallen onderscheiden worden op basis van de pivots:
1. Deel nooit door een uitdrukking in de parameter vóór gecontroleerd is of deze nul kan zijn.
2. Identificeer de kritieke parameterwaarden waarbij rijen wegvallen of strijdigheid ontstaat.

---

> [!summary] Kernsamenvatting
> - Het vergelijken van $\text{rang}(A)$ en $\text{rang}([A \mid \mathbf{b}])$ bepaalt onmiddellijk de aard van de oplossingsverzameling.
> - Gauss-Jordan levert een parametrische voorstelling van de affiene deelruimte aan oplossingen.
