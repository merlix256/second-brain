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

# Hoofdstuk 7: Beste Benadering en Orthogonale Projecties

> [!abstract] Context
> Dit hoofdstuk behandelt de orthogonale projectie van een vector op een deelruimte, de beste benaderingsstelling en de kleinste-kwadratenmethode.
> **Parent MOC:** [[Index]] | **Q&A:** [[Q&A - LinAlg Ch 07 Beste Benadering]] | **Oefeningen:** [[Oefensessie 14 - Vectorruimten IV (Beste Benadering en Projectie)]]

---

## 1. Orthogonale Deelruimten en Orthogonaal Complement
Voor een deelruimte $W \le V$ is het orthogonaal complement:
$$W^\perp = \{\mathbf{v} \in V \mid \langle \mathbf{v}, \mathbf{w} \rangle = 0, \; \forall \mathbf{w} \in W\}$$
- $V = W \oplus W^\perp$ (directe som).
- Elke vector $\mathbf{v} \in V$ kan op unieke wijze geschreven worden als:
  $$\mathbf{v} = \mathbf{w} + \mathbf{w}^\perp \quad (\mathbf{w} \in W, \; \mathbf{w}^\perp \in W^\perp)$$

---

## 2. Orthogonale Projectie op een Deelruimte
Als $\{\mathbf{q}_1, \dots, \mathbf{q}_k\}$ een **orthonormale basis** is van $W$:
$$\text{proj}_W(\mathbf{v}) = \sum_{i=1}^k \langle \mathbf{v}, \mathbf{q}_i \rangle \mathbf{q}_i$$
Indien de basis $\{\mathbf{w}_1, \dots, \mathbf{w}_k\}$ orthogonaal is (niet genormaliseerd):
$$\text{proj}_W(\mathbf{v}) = \sum_{i=1}^k \frac{\langle \mathbf{v}, \mathbf{w}_i \rangle}{\|\mathbf{w}_i\|^2} \mathbf{w}_i$$

---

## 3. Stelling van de Beste Benadering
Voor elke $\mathbf{v} \in V$ en elke vector $\mathbf{w}' \in W$ geldt:
$$\|\mathbf{v} - \text{proj}_W(\mathbf{v})\| \le \|\mathbf{v} - \mathbf{w}'\|$$
De orthogonale projectie $\hat{\mathbf{v}} = \text{proj}_W(\mathbf{v})$ is het unieke element in $W$ dat de afstand tot $\mathbf{v}$ minimaliseert.

![[Orthogonale_Projectie_Deelruimte.png]]

---

## 4. Toepassing: Kleinste-kwadratenmethode (Least Squares)
Wanneer een lineair stelsel $A\mathbf{x} = \mathbf{b}$ strijdig is, zoekt men de vector $\hat{\mathbf{x}}$ die de residu-fout $\|A\mathbf{x} - \mathbf{b}\|$ minimaliseert.
Dit leidt tot de **normaalvergelijkingen**:
$$A^T A \hat{\mathbf{x}} = A^T \mathbf{b}$$
Indien de kolommen van $A$ lineair onafhankelijk zijn, is $A^T A$ inverteerbaar en geldt:
$$\hat{\mathbf{x}} = (A^T A)^{-1} A^T \mathbf{b}$$

---

> [!summary] Kernsamenvatting
> - De projectie van $\mathbf{v}$ op $W$ minimaliseert de kwadratische foutafstand.
> - Het residu $\mathbf{v} - \hat{\mathbf{v}}$ staat orthogonaal op alle vectoren in $W$.
> - Kleinste kwadraten vormt het wiskundige hart van datafitting, regressie en signaalverwerking.
