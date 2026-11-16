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

# Hoofdstuk 2: Vlakke Meetkunde

> [!abstract] Context
> Dit hoofdstuk behandelt krommen in het Cartesiaanse vlak $\mathbb{R}^2$: rechten, kegelsneden (parabool, ellips, hyperbool) en poolkrommen.
> **Parent MOC:** [[Index]] | **Q&A:** [[Q&A - Meetkunde Ch 02]] | **Oefeningen:** [[Oefensessie 04 - Vlakke Meetkunde I (Rechten)]], [[Oefensessie 05 - Vlakke Meetkunde II (Kegelsneden en Poolkrommen)]]

---

## 1. Rechten in $\mathbb{R}^2$
### 1.1 Voorstellingswijzen
- **Cartesiaanse (algemene) vergelijking:**
  $$e: Ax + By + C = 0 \quad ((A, B) \neq (0,0))$$
  - Normaalvector: $\mathbf{n} = \begin{bmatrix} A \\ B \end{bmatrix} \perp e$.
  - Richtingsvector: $\mathbf{r} = \begin{bmatrix} -B \\ A \end{bmatrix} \parallel e$.
- **Expliciete functievorm (rico):**
  $$y = mx + q \quad (m = -A/B, \text{ mits } B \neq 0)$$
- **Parametervergelijking:**
  $$\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} p_1 \\ p_2 \end{bmatrix} + k \begin{bmatrix} r_1 \\ r_2 \end{bmatrix}, \quad k \in \mathbb{R}$$

### 1.2 Rechtenbundels
De verzameling van alle rechten door het snijpunt $S$ van twee snijdende rechten $e_1: A_1 x + B_1 y + C_1 = 0$ en $e_2: A_2 x + B_2 y + C_2 = 0$:
$$k(A_1 x + B_1 y + C_1) + l(A_2 x + B_2 y + C_2) = 0, \quad (k, l) \neq (0,0)$$
Of met één parameter $\lambda$: $(A_1 x + B_1 y + C_1) + \lambda(A_2 x + B_2 y + C_2) = 0$.

![[Rechtenbundel_Snijpunt.png]]

---

## 2. Kegelsneden
Gedefinieerd als meetkundige plaats van punten $P$ waarvan de verhouding van de afstand tot een brandpunt $F$ en een richtlijn $d$ constant is ($e = \text{excentriciteit}$):
$$\frac{d(P, F)}{d(P, d)} = e$$
- $e = 0$: Cirkel
- $0 < e < 1$: Ellips
- $e = 1$: Parabool
- $e > 1$: Hyperbool

### 2.1 Parabool ($e = 1$)
- Top in de oorsprong, brandpunt $F(a, 0)$, richtlijn $x = -a$:
  $$y^2 = 4ax$$
- Top $T(t_1, t_2)$ en horizontale symmetrie-as:
  $$(y - t_2)^2 = 4a(x - t_1)$$

### 2.2 Ellips ($0 < e < 1$)
- Middelpunt $M(m_1, m_2)$, halve lange as $a$, halve korte as $b$, brandpuntsafstand $c = \sqrt{a^2 - b^2}$ met $e = c/a$:
  $$\frac{(x - m_1)^2}{a^2} + \frac{(y - m_2)^2}{b^2} = 1$$
- Parametervergelijking:
  $$x = m_1 + a\cos\theta, \quad y = m_2 + b\sin\theta, \quad \theta \in (-\pi, \pi]$$

### 2.3 Hyperbool ($e > 1$)
- Middelpunt $M(m_1, m_2)$, brandpunten op de $x$-as, $c = \sqrt{a^2 + b^2}$, asymptoten $y - m_2 = \pm \frac{b}{a}(x - m_1)$:
  $$\frac{(x - m_1)^2}{a^2} - \frac{(y - m_2)^2}{b^2} = 1$$

![[Kegelsneden_Overzicht.png]]

---

## 3. Poolkrommen
Krommen gedefinieerd door $r = f(\theta)$.
- **Kegelsneden in poolcoördinaten** (brandpunt in oorsprong, richtlijn $x = \pm d$ of $y = \pm d$):
  $$r = \frac{e \cdot d}{1 \pm e\cos\theta} \quad \text{of} \quad r = \frac{e \cdot d}{1 \pm e\sin\theta}$$
- **Klassieke poolkrommen:**
  - Cirkels: $r = 2R\cos\theta$ of $r = 2R\sin\theta$
  - Cardioïde / Limaçon: $r = a + b\cos\theta$
  - Rozetten: $r = a\cos(n\theta)$ of $r = a\sin(n\theta)$ ($n$ even $\implies 2n$ bladeren; $n$ oneven $\implies n$ bladeren).
- **Stappenplan voor schetsen:**
  1. Bepaal periode en symmetrie (t.o.v. poolas als $f(-\theta) = f(\theta)$).
  2. Tabel van karakteristieke waarden (nulpunten, extrema).
  3. Schets eerst $r$ i.f.v. $\theta$ Cartesisch, transfereer daarna naar het polaire vlak.

---

> [!summary] Kernsamenvatting
> - Rechten worden gekarakteriseerd door normaalvector $\mathbf{n}$ en richtingsvector $\mathbf{r}$. Rechtenbundels laten toe rechten door snijpunten te vinden zonder eerst het stelsel op te lossen.
> - Kegelsneden worden geünificeerd door de excentriciteit $e$.
> - Poolkrommen vereenvoudigen de beschrijving van krommen met hoeksymmetrieën.
