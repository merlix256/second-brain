---
course: "Wiskundige basistechnieken (T1AWB1)"
unit_type: bewijs
status: todo
completed: false
est_hours: 1.0
priority: high
tags:
  - study-unit
---

# Bewijs 02: Afstand tussen Punt en Rechte in R2

> [!abstract] Context & Examenbelang
> **Theorievraag 2:** *"Formuleer en bewijs de uitdrukking voor de afstand tussen een punt en een rechte in $\mathbb{R}^2$."*
> **Verwante Theorie:** [[Ch 02 - Vlakke Meetkunde#1. Rechten in R2]]
> **Formularium:** [[Formularium#1. Analytische Meetkunde]] | **MOC:** [[00 - Index der Bewijzen]]

---

## 1. Formulering van de Stelling
Gegeven een rechte $e$ in $\mathbb{R}^2$ met Cartesiaanse vergelijking $e: Ax + By + C = 0$ (met $A, B$ niet gelijktijdig nul), en een willekeurig punt $P(p_1, p_2) \in \mathbb{R}^2$.
De loodrechte afstand $d(P, e)$ van het punt $P$ tot de rechte $e$ wordt gegeven door:
$$d(P, e) = \frac{|A p_1 + B p_2 + C|}{\sqrt{A^2 + B^2}}$$

---

## 2. Grafische Representatie
![[Bewijs_02_Afstand_Punt_Rechte.png]]
*(Schets: Rechte $e: Ax + By + C = 0$ met normaalvector $n = [A, B]^T$. Punt $P$ met positievector $p = [p_1, p_2]^T$ en zijn loodrechte projectie $Q(q_1, q_2) \in e$ met positievector $q$. De projecties van $p$ en $q$ op de drager van de normaalvector $n$ met hoogtematen $g$ en $h$.)*

---

## 3. Stap-voor-stap Bewijs

### Stap 1: Karakterisering van de Projectie op de Normaalvector
Zij $n = [A, B]^T$ de normaalvector van de rechte $e$. De norm van $n$ is:
$$\|n\| = \sqrt{A^2 + B^2}$$
Zij $Q(q_1, q_2)$ de loodrechte projectie van het punt $P(p_1, p_2)$ op de rechte $e$. Omdat $Q \in e$, voldoen zijn coördinaten aan de vergelijking van de rechte:
$$A q_1 + B q_2 + C = 0 \iff A q_1 + B q_2 = -C \iff q \cdot n = -C$$

### Stap 2: Orthogonale Projectie van Vectoren op n
De vector van $Q$ naar $P$ staat loodrecht op de rechte $e$, en heeft bijgevolg dezelfde richting als de normaalvector $n$.
De afstand $d(P, e)$ is per definitie gelijk aan de lengte van de verschilvector $p - q$:
$$d(P, e) = \|p - q\|$$
Aangezien $p - q$ evenwijdig is met $n$, is de lengte van $p - q$ exact gelijk aan het verschil in de orthogonale projecties van de positievectoren $p$ en $q$ op de eenheidsnormaalvector $\frac{n}{\|n\|}$.

De scalaire projectie van een willekeurige vector $x$ op de normaalvector $n$ is:
$$\text{comp}_n(x) = \frac{x \cdot n}{\|n\|}$$

### Stap 3: Uitwerken van het Verschil
De afstand is derhalve:
$$d(P, e) = |\text{comp}_n(p) - \text{comp}_n(q)| = \left| \frac{p \cdot n}{\|n\|} - \frac{q \cdot n}{\|n\|} \right|$$
Breng alles op één noemer $\|n\|$:
$$d(P, e) = \frac{|p \cdot n - q \cdot n|}{\|n\|}$$
Substitueer de bekende waarden:
- $p \cdot n = A p_1 + B p_2$
- $q \cdot n = -C$ (omdat $Q$ op de rechte ligt)
- $\|n\| = \sqrt{A^2 + B^2}$

Dit levert:
$$d(P, e) = \frac{|(A p_1 + B p_2) - (-C)|}{\sqrt{A^2 + B^2}} = \frac{|A p_1 + B p_2 + C|}{\sqrt{A^2 + B^2}} \quad \blacksquare$$

---

## 4. Examenvalkuilen & Aandachtspunten
- **Absoluutstrepen in de teller:** Vergeet nooit de modulus $|\dots|$ in de teller. Afstand is per definitie strikt niet-negatief ($d \ge 0$).
- **Geldigheid van $q \cdot n = -C$:** Benadruk expliciet dat het punt $Q$ op de rechte ligt, waardoor de constante $C$ via $A q_1 + B q_2 = -C$ in de formule verschijnt.
