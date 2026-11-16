---
title: "Analyse Ch 06: Onbepaalde Integralen"
course: "Wiskundige basistechnieken (T1AWB1)"
unit_type: theory
status: todo
completed: false
est_hours: 4.0
priority: high
tags:
  - study-unit
  - wiskunde
  - analyse
---

# Hoofdstuk 6: Onbepaalde Integralen

> [!abstract] Context
> Primitieve functies, basisintegralen, integratie door substitutie, partiële integratie, splitsen in partieelbreuken en goniometrische substituties.
> **Parent MOC:** [[Deel 3 - Analyse]] | **Q&A:** [[Q&A - Analyse Ch 06 Onbepaalde Integralen]] | **Oefeningen:** [[Oefensessie 18 - Onbepaalde Integralen I (Substitutie en Partieel)]] • [[Oefensessie 21 - Onbepaalde Integralen II (Rationale Functies)]] • [[Oefensessie 22 - Goniometrische Substitutie en Bepaalde Integralen]] | **Examenbewijzen:** [[Bewijs 09 - Integratie door Substitutie]] • [[Bewijs 10 - Partiële Integratie]]

---

## 1. Primitieven & Standaardintegralen
$F$ is een primitieve van $f$ op $I$ als $F'(x) = f(x)$. De onbepaalde integraal is:
$$\int f(x)\,dx = F(x) + C \quad (C \in \mathbb{R})$$
- **Cruciale standaardvormen:**
  - $\int \frac{1}{x}\,dx = \ln|x| + C$ (vergeet de absoluutstrepen niet!)
  - $\int \frac{1}{x^2 + a^2}\,dx = \frac{1}{a}\arctan\left(\frac{x}{a}\right) + C$
  - $\int \frac{1}{\sqrt{a^2 - x^2}}\,dx = \arcsin\left(\frac{x}{a}\right) + C$ ($a > 0$)

---

## 2. Oplossingsmethoden
### 2.1 Substitutiemethode ([[Bewijs 09 - Integratie door Substitutie]])
$$\int f(g(x)) g'(x)\,dx = \int f(u)\,du \quad \text{met } u = g(x),\; du = g'(x)\,dx$$
- Herken direct de structuur $\int \frac{f'(x)}{f(x)}\,dx = \ln|f(x)| + C$.

### 2.2 Partiële Integratie ([[Bewijs 10 - Partiële Integratie]])
$$\int u\,dv = u \cdot v - \int v\,du$$
- **LIATE-keuzevolgorde voor $u$:** **L**ogaritmisch ($\ln x$) $\to$ **I**nvers goniometrisch ($\arctan x, \arcsin x$) $\to$ **A**lgebraïsch ($x^n$) $\to$ **T**rigonometrisch ($\sin x, \cos x$) $\to$ **E**xponentieel ($e^x$).
- Bij $\int e^{ax}\sin(bx)\,dx$: pas $2\times$ partieel integreren toe en los algebraïsch op naar $I$!

### 2.3 Rationale Functies via Partieelbreuksplitsing $\int \frac{P(x)}{Q(x)}\,dx$
1. **Stap 1 (Altijd eerst checken!):** Als $\deg(P) \ge \deg(Q) \implies$ eerst **Euclidische veeltermdeling** uitvoeren: $\frac{P(x)}{Q(x)} = S(x) + \frac{R(x)}{Q(x)}$ met $\deg(R) < \deg(Q)$.
2. **Stap 2:** Ontbind $Q(x)$ in lineaire factoren $(x - r)^k$ en onherleidbare kwadratische factoren $(ax^2 + bx + c)^m$ ($D < 0$).
3. **Stap 3:** Stel splitsing op:
   - $(x - r)^k \to \frac{A_1}{x-r} + \frac{A_2}{(x-r)^2} + \dots + \frac{A_k}{(x-r)^k}$
   - $(x^2 + px + q) \to \frac{Bx + C}{x^2 + px + q}$ (splits op in $\ln$ via afgeleide noemer + $\arctan$ via kwadraatafsplitsing!).

### 2.4 Goniometrische & Irrationale Substituties
- $\sqrt{a^2 - x^2} \implies x = a\sin t$ ($dx = a\cos t\,dt$, $\sqrt{a^2 - x^2} = a\cos t$)
- $\sqrt{a^2 + x^2} \implies x = a\tan t$ (of $x = a\sinh t$)
- $\sqrt{x^2 - a^2} \implies x = \frac{a}{\cos t}$ (of $x = a\cosh t$)
- Algemene goniometrische substitutie ($t$-formules): $t = \tan(x/2) \implies \sin x = \frac{2t}{1+t^2}, \;\cos x = \frac{1-t^2}{1+t^2}, \;dx = \frac{2\,dt}{1+t^2}$.

> [!summary] Kernsamenvatting
> Bij elke rationale integraal: **eerst graad teller vs. noemer vergelijken!** Vergeet nooit $+C$ bij onbepaalde integralen.
