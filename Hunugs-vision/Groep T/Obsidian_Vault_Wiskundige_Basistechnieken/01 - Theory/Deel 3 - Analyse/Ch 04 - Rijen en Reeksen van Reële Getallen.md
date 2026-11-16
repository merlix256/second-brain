---
title: "Analyse Ch 04: Rijen en Reeksen van Reële Getallen"
course: "Wiskundige basistechnieken (T1AWB1)"
unit_type: theory
status: todo
completed: false
est_hours: 3.5
priority: high
tags:
  - study-unit
  - wiskunde
  - analyse
---

# Hoofdstuk 4: Rijen en Reeksen van Reële Getallen

> [!abstract] Context
> Convergentie van rijen, partiële sommen van numerieke reeksen, en het volledige beslissingsschema van convergentiecriteria.
> **Parent MOC:** [[Deel 3 - Analyse]] | **Q&A:** [[Q&A - Analyse Ch 04 Rijen en Reeksen]] | **Oefeningen:** [[Oefensessie 19 - Rijen en Reeksen]] | **Examenbewijs:** [[Bewijs 14 - Convergentie van de p-Reeks]]

---

## 1. Rijen $(u_n)_{n \in \mathbb{N}}$
- Convergentie: $\lim_{n \to \infty} u_n = L \in \mathbb{R}$.
- **Monotone convergentiestelling:** Elke begrensde monotone rij convergeert.
- **Stelling van Cauchy:** Een reële rij convergeert $\iff$ het is een Cauchy-rij.

## 2. Numerieke Reeksen $\sum_{n=n_0}^\infty u_n$
- De reeks convergeert naar $S$ als de rij van partiële sommen $S_N = \sum_{n=n_0}^N u_n$ convergeert naar $S$.
- **Meetkundige reeks:** $\sum_{n=0}^\infty a r^n$ convergeert $\iff |r| < 1$, met som $S = \frac{a}{1 - r}$.
- **Telescoopreeks:** $u_n = v_n - v_{n+1} \implies S_N = v_{n_0} - v_{N+1}$.

## 3. Numerieke Reeksen en Criteria
### 3.1 Noodzakelijke Voorwaarde (Divergentietest)
Als $\sum u_n$ convergeert, dan $\lim_{n \to \infty} u_n = 0$.
*(Omgekeerde geldt NIET! Zie de harmonische reeks $\sum \frac{1}{n} = \infty$. Maar als $\lim u_n \neq 0$, divergeert de reeks onmiddellijk!)*

### 3.2 Criteria voor Reeksen met Positieve Termen ($u_n > 0$)
1. **$p$-Reeks (Referentiereeks):** $\sum_{n=1}^\infty \frac{1}{n^p}$ convergeert $\iff p > 1$ (zie [[Bewijs 14 - Convergentie van de p-Reeks]]).
2. **Vergelijkingstest:** Als $0 \le u_n \le v_n$: $\sum v_n$ conv. $\implies \sum u_n$ conv.; $\sum u_n$ div. $\implies \sum v_n$ div.
3. **Limietvergelijkingstest:** $\lim_{n \to \infty} \frac{u_n}{v_n} = L \in (0, \infty) \implies$ zelfde convergentiegedrag.
4. **Quotiënttest (d'Alembert):** $L = \lim_{n \to \infty} \frac{u_{n+1}}{u_n}$. $L < 1 \implies$ conv., $L > 1 \implies$ div., $L = 1 \implies$ geen besluit! (Ideaal bij faculteiten $n!$ en machten $a^n$).
5. **Worteltest (Cauchy):** $L = \lim_{n \to \infty} \sqrt[n]{u_n}$. $L < 1 \implies$ conv., $L > 1 \implies$ div., $L = 1 \implies$ geen besluit.
6. **Integraaltest:** Voor $f$ positief, continu en dalend: $\sum_{n=1}^\infty f(n)$ conv. $\iff \int_1^\infty f(x)\,dx < \infty$.

### 3.3 Alternerende Reeksen & Absolute Convergentie
- **Leibniz-criterium:** $\sum (-1)^n a_n$ ($a_n > 0$) convergeert als $a_n$ **monotoon dalend** is én $\lim_{n \to \infty} a_n = 0$.
- **Absoluut convergent:** $\sum |u_n|$ convergeert $\implies \sum u_n$ convergeert.
- **Voorwaardelijk (relatief) convergent:** $\sum u_n$ convergeert, maar $\sum |u_n|$ divergeert (bv. $\sum \frac{(-1)^{n-1}}{n}$).

> [!summary] Stappenplan op het Examen
> 1) Check $\lim u_n \neq 0$ (Divergentietest). 2) Bevat het $n!$ of $a^n$? $\rightarrow$ d'Alembert / Cauchy. 3) Rationaal in $n$? $\rightarrow$ Limietvergelijking met $1/n^p$. 4) Alternerend $(-1)^n$? $\rightarrow$ Absolute conv. + Leibniz.
