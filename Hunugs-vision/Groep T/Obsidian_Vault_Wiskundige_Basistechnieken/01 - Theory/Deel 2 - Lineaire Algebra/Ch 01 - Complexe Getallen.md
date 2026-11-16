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

# Hoofdstuk 1: Complexe Getallen

> [!abstract] Context
> Dit hoofdstuk introduceert het lichaam van de complexe getallen $\mathbb{C}$, de algebraïsche en goniometrische voorstellingen, de formule van De Moivre, exponentiële notatie van Euler en $n$-demachtswortels.
> **Parent MOC:** [[Index]] | **Q&A:** [[Q&A - LinAlg Ch 01 Complexe Getallen]] | **Oefeningen:** [[Oefensessie 24 - Complexe Getallen]]

---

## 1. Algebraïsche Vorm
Een complex getal $z \in \mathbb{C}$:
$$z = a + bi \quad (a, b \in \mathbb{R}, \; i^2 = -1)$$
- Reëel deel: $\text{Re}(z) = a$, Imaginair deel: $\text{Im}(z) = b$.
- Complex toegevoegde (geconjugeerde): $\bar{z} = a - bi$.
- Modulus: $|z| = \sqrt{a^2 + b^2} = \sqrt{z \bar{z}}$.
- Eigenschappen van deling:
  $$\frac{a + bi}{c + di} = \frac{(a + bi)(c - di)}{(c + di)(c - di)} = \frac{(ac + bd) + (bc - ad)i}{c^2 + d^2}$$

![[Complex_Vlak_Gauss.png]]

---

## 2. Goniometrische en Exponentiële Vorm
### 2.1 Polaire Voorstelling
Met $r = |z|$ en $\theta = \arg(z) \in (-\pi, \pi]$:
$$z = r(\cos\theta + i\sin\theta) = r e^{i\theta}$$
waarbij $e^{i\theta} = \cos\theta + i\sin\theta$ de **formule van Euler** is.

### 2.2 Vermenigvuldiging en Deler
- Product: $z_1 z_2 = r_1 r_2 e^{i(\theta_1 + \theta_2)} = r_1 r_2 [\cos(\theta_1 + \theta_2) + i\sin(\theta_1 + \theta_2)]$
- Quotiënt: $\frac{z_1}{z_2} = \frac{r_1}{r_2} e^{i(\theta_1 - \theta_2)}$

### 2.3 Formule van De Moivre
Voor alle $n \in \mathbb{Z}$:
$$(\cos\theta + i\sin\theta)^n = \cos(n\theta) + i\sin(n\theta) \iff (e^{i\theta})^n = e^{in\theta}$$

---

## 3. $n$-demachtswortels van een Complex Getal
De $n$ verschillende complexe wortels van $z = r e^{i\theta}$ zijn gegeven door:
$$w_k = \sqrt[n]{r} \left( \cos\left(\frac{\theta + 2k\pi}{n}\right) + i\sin\left(\frac{\theta + 2k\pi}{n}\right) \right) = \sqrt[n]{r} e^{i\frac{\theta + 2k\pi}{n}}, \quad k = 0, 1, \dots, n-1$$
- Meetkundig vormen de $n$-demachtswortels de hoekpunten van een regelmatige $n$-hoek op een cirkel met straal $\sqrt[n]{r}$ gecentreerd in de oorsprong.

![[Complexe_Eenheidswortels_Polygoon.png]]

---

> [!summary] Kernsamenvatting
> - Complexe getallen verenigen algebra met vlakke meetkunde in het Gauss-vlak.
> - Vermenigvuldiging vertaalt zich in het schalen van moduli en het optellen van argumenten.
> - De Moivre en Euler maken het berekenen van machten en wortels elegant en direct.
