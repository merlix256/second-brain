---
title: "Analyse Ch 09: Functiereeksen en Reeksontwikkelingen"
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

# Hoofdstuk 9: Functiereeksen en Reeksontwikkelingen

> [!abstract] Context
> Puntsgewijze en uniforme convergentie van functiereeksen, machtreeksen (convergentiestraal en -interval), en Taylor-/Maclaurinreeksen.
> **Parent MOC:** [[Deel 3 - Analyse]] | **Q&A:** [[Q&A - Analyse Ch 09 Functiereeksen]] | **Oefeningen:** [[Oefensessie 20 - Functiereeksen]] | **Examenbewijs:** [[Bewijs 15 - Taylorveelterm en Afleiding van Coëfficiënten]]

---

## 1. Machtreeksen $\sum_{n=0}^\infty a_n (x - x_0)^n$
- **Convergentiestraal $R \in [0, \infty]$:**
  - Via d'Alembert: $\frac{1}{R} = \lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right|$ (of met volledige term $|u_{n+1}/u_n| < 1 \implies |x - x_0| < R$).
  - Via Cauchy-Hadamard: $\frac{1}{R} = \lim_{n \to \infty} \sqrt[n]{|a_n|}$.
- **Convergentie-interval:**
  - De reeks convergeert absoluut voor $|x - x_0| < R$, divergeert voor $|x - x_0| > R$.
  - **Randpunten $x = x_0 - R$ en $x = x_0 + R$:** ALTIJD afzonderlijk invullen en testen als numerieke reeks (zie [[Ch 04 - Rijen en Reeksen van Reële Getallen]])!
- **Binnen $(-R, R)$:** Mag je een machtreeks **termsgewijs afleiden** en **termsgewijs integreren** zonder dat $R$ verandert!

---

## 2. Taylor- en Maclaurinreeksen
*(Zie het volledige examenbewijs in [[Bewijs 15 - Taylorveelterm en Afleiding van Coëfficiënten]]!)*
- **Taylorreeks rond $x = a$:**
  $$f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!}(x - a)^n$$
- **Maclaurinreeks ($a = 0$) — Verplicht uit het hoofd:**
  - $e^x = \sum_{n=0}^\infty \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$ ($x \in \mathbb{R}$)
  - $\sin x = \sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{(2n+1)!} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \dots$ ($x \in \mathbb{R}$)
  - $\cos x = \sum_{n=0}^\infty \frac{(-1)^n x^{2n}}{(2n)!} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \dots$ ($x \in \mathbb{R}$)
  - $\frac{1}{1 - x} = \sum_{n=0}^\infty x^n = 1 + x + x^2 + \dots$ ($|x| < 1$)
  - $\ln(1 + x) = \sum_{n=1}^\infty \frac{(-1)^{n-1} x^n}{n} = x - \frac{x^2}{2} + \frac{x^3}{3} - \dots$ ($x \in (-1, 1]$)
  - $\arctan x = \sum_{n=0}^\infty \frac{(-1)^n x^{2n+1}}{2n+1} = x - \frac{x^3}{3} + \frac{x^5}{5} - \dots$ ($x \in [-1, 1]$)
- **Restterm van Lagrange:** $R_n(x) = \frac{f^{(n+1)}(c)}{(n+1)!}(x - a)^{n+1}$ voor een $c$ tussen $a$ en $x$.

> [!summary] Examenhack
> Gebruik bekende Maclaurinreeksen + substitutie/afleiden/integreren (bv. voor $e^{-x^2}$, $\frac{1}{1+x^2}$ of limieten $\lim_{x \to 0}$) i.p.v. $n$ keer moeizaam afleiden!
