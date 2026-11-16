---
title: "Analyse Ch 05: Afgeleiden en Toepassingen"
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

# Hoofdstuk 5: Afgeleiden en Toepassingen

> [!abstract] Context
> Differentiequotiënt, afleidbaarheid vs. continuïteit, afleidingsregels, impliciet en logaritmisch differentiëren, Rolle, Lagrange (MVT) en optimalisatie.
> **Parent MOC:** [[Deel 3 - Analyse]] | **Q&A:** [[Q&A - Analyse Ch 05 Afgeleiden]] | **Oefeningen:** [[Oefensessie 16 - Afgeleiden I]] • [[Oefensessie 17 - Afgeleiden II en Toepassingen]] | **Examenbewijs:** [[Bewijs 04 - Verband Afleidbaarheid en Continuïteit]]

---

## 1. Definitie en Betekenis van de Afgeleide
$$f'(a) = \lim_{h \to 0} \frac{f(a+h) - f(a)}{h} = \lim_{x \to a} \frac{f(x) - f(a)}{x - a}$$
- **Meetkundige betekenis:** Richtingscoëfficiënt van de raaklijn aan de grafiek van $f$ in $(a, f(a))$:
  $$y - f(a) = f'(a)(x - a)$$
- **Stelling ([[Bewijs 04 - Verband Afleidbaarheid en Continuïteit]]):** Afleidbaarheid in $a \implies$ continuïteit in $a$. (Omgekeerde is vals: $f(x) = |x|$ is continu in $0$, maar $f'_-(0) = -1 \neq +1 = f'_+(0)$!).

---

## 2. Rekenregels en Standaardafgeleiden
- **Productregel:** $(uv)' = u'v + uv'$ | **Quotiëntregel:** $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$
- **Kettingregel:** $(f(g(x)))' = f'(g(x)) \cdot g'(x)$
- **Inverse functie:** $(f^{-1})'(y_0) = \frac{1}{f'(x_0)}$ waarbij $y_0 = f(x_0)$.
- **Belangrijke afgeleiden:**
  - $(\arcsin x)' = \frac{1}{\sqrt{1 - x^2}}$, $\;(\arccos x)' = \frac{-1}{\sqrt{1 - x^2}}$, $\;(\arctan x)' = \frac{1}{1 + x^2}$
  - $(\sinh x)' = \cosh x$, $\;(\cosh x)' = \sinh x$ (geen minteken!)
- **Logaritmisch differentiëren (bij $f(x)^{g(x)}$):** Neem $\ln y = g(x)\ln f(x)$ en leid impliciet af: $\frac{y'}{y} = \dots$

---

## 3. Middelwaardestellingen & Functieverloop
- **Stelling van Rolle:** Als $f$ continu op $[a, b]$, afleidbaar op $(a, b)$ en $f(a) = f(b)$, dan $\exists c \in (a, b): f'(c) = 0$.
- **Middelwaardestelling van Lagrange (MVT):** Als $f$ continu op $[a, b]$ en afleidbaar op $(a, b)$, dan $\exists c \in (a, b)$:
  $$f'(c) = \frac{f(b) - f(a)}{b - a}$$
- **Functieverloop & Optimalisatie:**
  - $f'(x) = 0$ of ongedefinieerd $\rightarrow$ kritieke punten.
  - $f''(x) > 0 \implies$ lokaal minimum / concaaf naar boven (bol); $f''(x) < 0 \implies$ lokaal maximum / hol.
  - $f''(x) = 0$ met tekenwissel $\implies$ **buigpunt**.

> [!summary] Kernsamenvatting
> Vergeet bij cyclometrische functies niet het verschil tussen $(\arcsin x)'$ (positief) en $(\arccos x)'$ (negatief), en gebruik logaritmisch differentiëren voor functie-tot-de-macht-functie.
