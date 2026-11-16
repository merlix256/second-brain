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

# Hoofdstuk 1: Getallen, Punten en Vectoren

> [!abstract] Context
> Dit hoofdstuk legt de basis voor de meetkundige representatie van getallen en vectoren in $\mathbb{R}^0$, $\mathbb{R}^1$ en $\mathbb{R}^2$. We formaliseren Euclidische concepten zoals lengte, afstand, hoek en projectie.
> **Parent MOC:** [[Index]] | **Q&A:** [[Q&A - Meetkunde Ch 01]] | **Oefeningen:** [[Oefensessie 02 - Vectoralgebra in R2 en R3]]

---

## 1. De Oorsprong en Eendimensionale Ruimte
### 1.1 $\mathbb{R}^0$ en $\mathbb{R}^1$
- $\mathbb{R}^0$: Bestaat enkel uit het element $0$, het universele referentiepunt in fysische modellering.
- $\mathbb{R}^1$: De reële rechte. Punten worden aangeduid met $U(u)$, vectoren als gerichte lijnstukken vanuit de oorsprong $\mathbf{u}$.

![[Punt_en_Vector_R1.png]]

### 1.2 Bewerkingen in $\overline{\mathbb{R}}$ en Onbepaalde Vormen
Voor limietberekeningen breiden we $\mathbb{R}$ uit tot $\overline{\mathbb{R}} = \mathbb{R} \cup \{-\infty, +\infty\}$.
- Geldige bewerkingen:
  $$a + (+\infty) = +\infty \quad (a \in \mathbb{R})$$
  $$\frac{a}{\pm\infty} = 0 \quad (a \in \mathbb{R})$$
- Onbepaalde vormen:
  $$\pm\infty - (\pm\infty), \quad 0 \cdot (\pm\infty), \quad \frac{\pm\infty}{\pm\infty}, \quad \frac{0}{0}$$

---

## 2. Het Cartesiaans Vlak $\mathbb{R}^2$
### 2.1 Cartesiaanse Coördinaten en Vectorbewerkingen
Een punt $P(p_1, p_2)$ of vector $\mathbf{u} = \begin{bmatrix} u_1 \\ u_2 \end{bmatrix} \in \mathbb{R}^2$.
- **Optelling:** $\mathbf{u} + \mathbf{v} = \begin{bmatrix} u_1 + v_1 \\ u_2 + v_2 \end{bmatrix}$ (kop-staart methode / parallellogramregel).
- **Scalaire vermenigvuldiging:** $k\mathbf{u} = \begin{bmatrix} k u_1 \\ k u_2 \end{bmatrix}$.

![[Vector_Optelling_Parallellogram.png]]

### 2.2 Lengte (Norm) en Afstand
- **Euclidische norm (2-norm):**
  $$\|\mathbf{u}\| = \sqrt{u_1^2 + u_2^2}$$
- **Afstand tussen punten $P$ en $Q$:**
  $$d(P, Q) = \|\mathbf{q} - \mathbf{p}\| = \sqrt{(q_1 - p_1)^2 + (q_2 - p_2)^2}$$
- **Algemene $p$-norm:** $\|\mathbf{u}\|_p = (|u_1|^p + |u_2|^p)^{1/p}$. Voor $p \to \infty$: $\|\mathbf{u}\|_\infty = \max(|u_1|, |u_2|)$.

### 2.3 Hoek en Scalair Product in $\mathbb{R}^2$
- **Definitie Scalair Product:**
  $$\mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2$$
- **Meetkundige relatie:**
  $$\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\| \|\mathbf{v}\| \cos\theta$$
- **Orthogonaliteit:**
  $$\mathbf{u} \perp \mathbf{v} \iff \mathbf{u} \cdot \mathbf{v} = 0$$

![[Hoek_Tussen_Vectoren_Driehoek.png]]

### 2.4 Poolcoördinaten in $\mathbb{R}^2$
Een punt $P$ wordt vastgelegd door $(r, \theta)$ met $r \ge 0$ en $\theta \in (-\pi, \pi]$ (of $[0, 2\pi)$):
$$x = r \cos\theta, \quad y = r \sin\theta$$
$$r = \sqrt{x^2 + y^2}, \quad \theta = \text{atan2}(y, x)$$

---

## 3. Orthogonale Projectie in $\mathbb{R}^2$
De orthogonale projectie van vector $\mathbf{u}$ op vector $\mathbf{v} \neq \mathbf{0}$:
$$\text{proj}_{\mathbf{v}}(\mathbf{u}) = \left( \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|^2} \right) \mathbf{v}$$
De component van $\mathbf{u}$ loodrecht op $\mathbf{v}$: $\mathbf{u}_{\perp} = \mathbf{u} - \text{proj}_{\mathbf{v}}(\mathbf{u})$.

---

> [!summary] Kernsamenvatting
> - Vectoren in $\mathbb{R}^2$ worden algebraïsch gekarakteriseerd door coördinaten en meetkundig door lengte en richting.
> - Het inwendig product $\mathbf{u} \cdot \mathbf{v}$ vormt de spil tussen algebraïsche componenten en meetkundige concepten (lengte, hoek $\theta$, projecties).
> - Poolcoördinaten $(r, \theta)$ bieden een essentieel alternatief assenstelsel voor cirkels, rotaties en periodieke fenomenen.
