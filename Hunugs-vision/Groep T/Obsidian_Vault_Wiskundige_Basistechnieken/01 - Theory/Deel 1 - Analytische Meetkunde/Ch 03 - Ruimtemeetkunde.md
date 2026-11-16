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

# Hoofdstuk 3: Ruimtemeetkunde

> [!abstract] Context
> Dit hoofdstuk breidt analytische meetkunde uit naar de driedimensionale ruimte $\mathbb{R}^3$. We introduceren het vectorieel product, vergelijkingen van rechten en vlakken, en vlakkenwaaiers als opstap naar stelsels in lineaire algebra.
> **Parent MOC:** [[Index]] | **Q&A:** [[Q&A - Meetkunde Ch 03]] | **Oefeningen:** [[Oefensessie 06 - Ruimtemeetkunde I]], [[Oefensessie 07 - Ruimtemeetkunde II]]

---

## 1. Vectoralgebra in $\mathbb{R}^3$
### 1.1 Scalair Product en Norm in $\mathbb{R}^3$
Voor $\mathbf{u} = \begin{bmatrix} u_1 \\ u_2 \\ u_3 \end{bmatrix}$ en $\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ v_3 \end{bmatrix}$:
- $\|\mathbf{u}\| = \sqrt{u_1^2 + u_2^2 + u_3^2}$
- $\mathbf{u} \cdot \mathbf{v} = u_1 v_1 + u_2 v_2 + u_3 v_3 = \|\mathbf{u}\| \|\mathbf{v}\| \cos\theta$

### 1.2 Vectorieel Product (Kruisproduct)
Het vectorieel product $\mathbf{u} \times \mathbf{v}$ bestaat enkel in $\mathbb{R}^3$ en levert een vector op die **loodrecht** staat op zowel $\mathbf{u}$ als $\mathbf{v}$:
$$\mathbf{u} \times \mathbf{v} = \det \begin{bmatrix} \mathbf{e}_x & \mathbf{e}_y & \mathbf{e}_z \\ u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \end{bmatrix} = \begin{bmatrix} u_2 v_3 - u_3 v_2 \\ u_3 v_1 - u_1 v_3 \\ u_1 v_2 - u_2 v_1 \end{bmatrix}$$
- **Eigenschappen:**
  - Anticommutatief: $\mathbf{u} \times \mathbf{v} = -(\mathbf{v} \times \mathbf{u})$.
  - Norm: $\|\mathbf{u} \times \mathbf{v}\| = \|\mathbf{u}\| \|\mathbf{v}\| \sin\theta$ (= oppervlakte van het opgespannen parallellogram).
  - Evenwijdigheidscriterium: $\mathbf{u} \parallel \mathbf{v} \iff \mathbf{u} \times \mathbf{v} = \mathbf{0}$.

![[Vectorieel_Product_Rechterhandregel.png]]

### 1.3 Gemengd Product (Spatproduct)
$$\mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = \det \begin{bmatrix} u_1 & u_2 & u_3 \\ v_1 & v_2 & v_3 \\ w_1 & w_2 & w_3 \end{bmatrix}$$
- De absolute waarde stelt het **volume** van het opgespannen parallellepipedum voor.
- Drie vectoren zijn coplanair (liggen in hetzelfde vlak) $\iff \mathbf{u} \cdot (\mathbf{v} \times \mathbf{w}) = 0$.

---

## 2. Vlakken in $\mathbb{R}^3$
### 2.1 Vergelijkingen van een Vlak $\alpha$
- **Cartesiaanse vergelijking:**
  $$Ax + By + Cz + D = 0$$
  waarbij $\mathbf{n} = \begin{bmatrix} A \\ B \\ C \end{bmatrix}$ de normaalvector van het vlak is.
- **Door punt $P$ loodrecht op $\mathbf{n}$:**
  $$A(x - p_1) + B(y - p_2) + C(z - p_3) = 0$$
- **Parametervergelijking (bepaald door punt $P$ en twee niet-evenwijdige richtingsvectoren $\mathbf{r}, \mathbf{s}$):**
  $$\mathbf{x} = \mathbf{p} + k\mathbf{r} + l\mathbf{s}, \quad k, l \in \mathbb{R}$$
  waarbij $\mathbf{n} = \mathbf{r} \times \mathbf{s}$.

### 2.2 Afstand van een Punt tot een Vlak
$$d(Q, \alpha) = \frac{|A q_1 + B q_2 + C q_3 + D|}{\sqrt{A^2 + B^2 + C^2}}$$

---

## 3. Rechten in $\mathbb{R}^3$
Een rechte kan in $\mathbb{R}^3$ niet door één Cartesiaanse vergelijking worden voorgesteld, maar wel als doorsnede van twee niet-evenwijdige vlakken:
- **Stelsel van Cartesiaanse vergelijkingen:**
  $$\begin{cases} A_1 x + B_1 y + C_1 z + D_1 = 0 \\ A_2 x + B_2 y + C_2 z + D_2 = 0 \end{cases}$$
  Richtingsvector rechte: $\mathbf{r} = \mathbf{n}_1 \times \mathbf{n}_2$.
- **Parametervergelijking:**
  $$\begin{bmatrix} x \\ y \\ z \end{bmatrix} = \begin{bmatrix} p_1 \\ p_2 \\ p_3 \end{bmatrix} + k \begin{bmatrix} r_1 \\ r_2 \\ r_3 \end{bmatrix}, \quad k \in \mathbb{R}$$

### 3.3 Vlakkenwaaiers
De verzameling van alle vlakken door de snijlijn van twee vlakken $\alpha_1$ en $\alpha_2$:
$$k(A_1 x + B_1 y + C_1 z + D_1) + l(A_2 x + B_2 y + C_2 z + D_2) = 0$$

![[Vlakkenwaaier_Aslijn.png]]

---

> [!summary] Kernsamenvatting
> - Het kruisproduct levert de normaalvector van een vlak op basis van twee richtingsvectoren.
> - Een rechte in $\mathbb{R}^3$ ontstaat als snijlijn van twee vlakken (stelsel met 1 vrijheidsgraad).
> - De meetkundige intersecties van punten, rechten en vlakken vormen het fundament voor lineaire stelsels in $\mathbb{R}^n$.
