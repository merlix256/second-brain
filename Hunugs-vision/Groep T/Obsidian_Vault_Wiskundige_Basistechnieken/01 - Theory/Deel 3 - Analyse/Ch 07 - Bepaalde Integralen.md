---
title: "Analyse Ch 07: Bepaalde Integralen"
course: "Wiskundige basistechnieken (T1AWB1)"
unit_type: theory
status: todo
completed: false
est_hours: 3.0
priority: high
tags:
  - study-unit
  - wiskunde
  - analyse
---

# Hoofdstuk 7: Bepaalde Integralen

> [!abstract] Context
> Riemann-sommen, eigenschappen van de bepaalde integraal, de Hoofdstelling van de Integraalrekening, substitutie met grensaanpassing en oneigenlijke integralen.
> **Parent MOC:** [[Deel 3 - Analyse]] | **Q&A:** [[Q&A - Analyse Ch 07 Bepaalde Integralen]] | **Oefeningen:** [[Oefensessie 22 - Goniometrische Substitutie en Bepaalde Integralen]] | **Examenbewijs:** [[Bewijs 11 - Hoofdstelling van de Integraalrekening]]

---

## 1. Riemann-sommen & Eigenschappen
- De bepaalde integraal $\int_a^b f(x)\,dx = \lim_{\|P\| \to 0} \sum_{i=1}^n f(c_i)\Delta x_i$ (onder- en bovensommen convergeren naar dezelfde limiet voor continue of stuksgewijs continue functies op $[a, b]$).
- **Symmetrie op $[-a, a]$:**
  - $f$ **even** $\implies \int_{-a}^a f(x)\,dx = 2\int_0^a f(x)\,dx$.
  - $f$ **oneven** $\implies \int_{-a}^a f(x)\,dx = 0$.
- **Middelwaardestelling voor integralen:** $\exists c \in [a, b]$ zodat $\int_a^b f(x)\,dx = f(c)(b - a)$.

---

## 2. Hoofdstelling van de Integraalrekening
*(Zie het volledige examenbewijs in [[Bewijs 11 - Hoofdstelling van de Integraalrekening]]!)*
1. **Deel 1 (Afgeleide van een integraalfunctie):** Als $f$ continu is op $[a, b]$, dan is $F(x) = \int_a^x f(t)\,dt$ afleidbaar op $[a, b]$ en $F'(x) = f(x)$.
   - Met kettingregel: $\frac{d}{dx} \int_{g(x)}^{h(x)} f(t)\,dt = f(h(x))h'(x) - f(g(x))g'(x)$.
2. **Deel 2 (Newton-Leibniz):** Als $G$ een willekeurige primitieve is van $f$, dan:
   $$\int_a^b f(x)\,dx = \Big[ G(x) \Big]_a^b = G(b) - G(a)$$

---

## 3. Substitutie & Oneigenlijke Integralen
- **Substitutie bij bepaalde integralen:** Pas **meteen de integratiegrenzen aan** ($x=a \to u=g(a)$, $x=b \to u=g(b)$), zodat je niet hoeft terug te substitueren!
- **Oneigenlijke integralen:**
  - *Type I (Oneindig interval):* $\int_a^\infty f(x)\,dx = \lim_{R \to \infty} \int_a^R f(x)\,dx$.
  - *Type II (Verticale asymptoot in $c \in [a, b]$):* Splits in $c$ op en neem de limiet! (Valkuil: $\int_{-1}^1 \frac{1}{x^2}\,dx$ is NIET $-2$, maar divergeert naar $+\infty$ omdat $x=0$ een pool is!).
  - **$p$-Integraal:** $\int_1^\infty \frac{1}{x^p}\,dx$ convergeert $\iff p > 1$; $\;\int_0^1 \frac{1}{x^p}\,dx$ convergeert $\iff p < 1$.

> [!summary] Kernsamenvatting
> Check vóór je een bepaalde integraal uitrekent altijd of er binnen $[a, b]$ geen polen (noemer = 0) zitten!
