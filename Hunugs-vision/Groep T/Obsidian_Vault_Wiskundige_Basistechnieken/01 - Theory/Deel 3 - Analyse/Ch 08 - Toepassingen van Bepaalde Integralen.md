---
title: "Analyse Ch 08: Toepassingen van Bepaalde Integralen"
course: "Wiskundige basistechnieken (T1AWB1)"
unit_type: theory
status: todo
completed: false
est_hours: 3.0
priority: medium
tags:
  - study-unit
  - wiskunde
  - analyse
---

# Hoofdstuk 8: Toepassingen van Bepaalde Integralen

> [!abstract] Context
> Oppervlakte tussen krommen (Cartesisch, parametrisch en in poolcoördinaten), booglengte en volume/manteloppervlakte van omwentelingslichamen.
> **Parent MOC:** [[Deel 3 - Analyse]] | **Q&A:** [[Q&A - Analyse Ch 08 Toepassingen Integralen]] | **Oefeningen:** [[Oefensessie 23 - Toepassingen van Bepaalde Integralen]]

---

## 1. Oppervlakte van Vlakke Gebieden
1. **Cartesisch:**
   $$A = \int_a^b |f(x) - g(x)|\,dx \quad \text{of (horizontale stroken): } A = \int_c^d |x_{\text{rechts}}(y) - x_{\text{links}}(y)|\,dy$$
2. **Parametrisch ($x(t), y(t)$):**
   $$A = \int_{t_1}^{t_2} |y(t) \cdot x'(t)|\,dt$$
3. **Poolcoördinaten ($r = f(\theta)$):**
   $$A = \frac{1}{2} \int_{\theta_1}^{\theta_2} r(\theta)^2\,d\theta \quad \text{(tussen 2 krommen: } \frac{1}{2}\int_{\theta_1}^{\theta_2} (r_{\text{buiten}}^2 - r_{\text{binnen}}^2)\,d\theta\text{)}$$

---

## 2. Booglengte van een Kromme
- **Cartesisch $y = f(x)$:** $L = \int_a^b \sqrt{1 + [f'(x)]^2}\,dx$
- **Parametrisch $(x(t), y(t))$:** $L = \int_{t_1}^{t_2} \sqrt{[x'(t)]^2 + [y'(t)]^2}\,dt$
- **Poolkromme $r(\theta)$:** $L = \int_{\theta_1}^{\theta_2} \sqrt{r(\theta)^2 + [r'(\theta)]^2}\,d\theta$

---

## 3. Volumes van Omwentelingslichamen
1. **Schijvenmethode (om $x$-as, $y=0$):**
   $$V_x = \pi \int_a^b \left( [f(x)]^2 - [g(x)]^2 \right) dx \quad \text{(nooit } [f(x)-g(x)]^2 \text{!)}$$
2. **Om $y$-as (schijven in $y$ of cilinderschillenmethode):**
   - *Cilinderschillen (Shell method):* $V_y = 2\pi \int_a^b x \cdot |f(x) - g(x)|\,dx$ (voor $0 \le a < b$).
3. **Om verschoven as $y = k$:** Vervang straal door $|f(x) - k|$.

> [!danger] Klassieke Examenfout
> Bij volume tussen twee krommen rond de $x$-as is de oppervlakte van een ring $\pi(R^2 - r^2)$, dus $\pi \int (f^2 - g^2)\,dx$ en **NOOIT** $\pi \int (f - g)^2\,dx$!
