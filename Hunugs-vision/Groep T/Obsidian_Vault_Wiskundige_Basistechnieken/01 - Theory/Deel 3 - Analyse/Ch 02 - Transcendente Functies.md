---
title: "Analyse Ch 02: Transcendente Functies"
course: "Wiskundige basistechnieken (T1AWB1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: medium
tags:
  - study-unit
  - wiskunde
  - analyse
---

# Hoofdstuk 2: Transcendente Functies

> [!abstract] Context
> Goniometrische, cyclometrische (boog-), exponentiële, logaritmische en hyperbolische functies en hun identiteiten.
> **Parent MOC:** [[Deel 3 - Analyse]] | **Q&A:** [[Q&A - Analyse Ch 02 Transcendente Functies]] | **Oefeningen:** [[Oefensessie 01 - Functies en Transcendente Functies]]

---

## 1. Goniometrische & Cyclometrische Functies
- **Grondformules:** $\sin^2 x + \cos^2 x = 1$, $\;1 + \tan^2 x = \frac{1}{\cos^2 x}$.
- **Som- en verdubbelingsformules:**
  $$\sin(2x) = 2\sin x \cos x, \qquad \cos(2x) = \cos^2 x - \sin^2 x = 1 - 2\sin^2 x = 2\cos^2 x - 1$$
  $$\sin^2 x = \frac{1 - \cos(2x)}{2}, \qquad \cos^2 x = \frac{1 + \cos(2x)}{2}$$
- **Cyclometrische (inverse) functies — Ken de domeinen & beelden exact!**
  | Functie | Domein | Beeld (Hoofdwaarde!) |
  | :--- | :---: | :---: |
  | $y = \arcsin x$ | $[-1, 1]$ | $[-\frac{\pi}{2}, \frac{\pi}{2}]$ |
  | $y = \arccos x$ | $[-1, 1]$ | $[0, \pi]$ |
  | $y = \arctan x$ | $\mathbb{R}$ | $(-\frac{\pi}{2}, \frac{\pi}{2})$ |
  | $y = \text{arccot } x$ | $\mathbb{R}$ | $(0, \pi)$ |

> [!danger] Valkuil!
> $\arcsin(\sin x) = x$ geldt **enkel** voor $x \in [-\frac{\pi}{2}, \frac{\pi}{2}]$! Bijvoorbeeld $\arcsin(\sin(\frac{3\pi}{4})) = \frac{\pi}{4}$.

## 2. Exponentiële & Logaritmische Functies
- $a^x = e^{x \ln a}$ ($a > 0, a \neq 1$).
- $\log_a(x) = \frac{\ln x}{\ln a}$ voor $x > 0$.
- $\ln(xy) = \ln x + \ln y$, $\;\ln(x^r) = r \ln x$, $\;e^{\ln x} = x$.

## 3. Hyperbolische Functies
$$\sinh x = \frac{e^x - e^{-x}}{2}, \qquad \cosh x = \frac{e^x + e^{-x}}{2}, \qquad \tanh x = \frac{\sinh x}{\cosh x}$$
- **Grondidentiteit (min-teken!):** $\cosh^2 x - \sinh^2 x = 1$.
- **Inverse hyperbolische functies (logaritmische vorm):**
  $$\text{arsinh } x = \ln\left(x + \sqrt{x^2 + 1}\right), \qquad \text{arcosh } x = \ln\left(x + \sqrt{x^2 - 1}\right) \;\;(x \ge 1)$$

> [!summary] Kernsamenvatting
> Beheers de hoofdwaarden van $\arcsin, \arccos, \arctan$ en de verdubbelingsformules van $\cos(2x)$: die heb je voortdurend nodig bij integralen!
