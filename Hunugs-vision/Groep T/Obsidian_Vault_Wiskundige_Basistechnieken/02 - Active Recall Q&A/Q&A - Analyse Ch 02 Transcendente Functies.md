---
title: "Q&A - Analyse Ch 02: Transcendente Functies"
course: "Wiskundige basistechnieken (T1AWB1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.0
priority: medium
tags:
  - study-unit
  - wiskunde
  - active-recall
---

# Active Recall Q&A — Analyse Ch 02: Transcendente Functies

> [!question] Vraag 1: Vereenvoudig $\cos(\arcsin x)$ voor $x \in [-1, 1]$ en $\arcsin(\sin(\frac{5\pi}{6}))$.
> > [!success]- Antwoord & Uitwerking
> > - Zij $\theta = \arcsin x \in [-\frac{\pi}{2}, \frac{\pi}{2}]$, dan is $\cos\theta \ge 0$, dus $\cos(\arcsin x) = \sqrt{1 - \sin^2\theta} = \sqrt{1 - x^2}$.
> > - $\sin(\frac{5\pi}{6}) = \frac{1}{2} = \sin(\frac{\pi}{6})$, en $\frac{\pi}{6} \in [-\frac{\pi}{2}, \frac{\pi}{2}] \implies \arcsin(\sin(\frac{5\pi}{6})) = \frac{\pi}{6}$.
> > 🔗 **Theorie:** [[Ch 02 - Transcendente Functies#1. Goniometrische & Cyclometrische Functies]]

> [!question] Vraag 2: Bewijs vanuit de definities dat $\cosh^2 x - \sinh^2 x = 1$.
> > [!success]- Antwoord & Uitwerking
> > $$\left(\frac{e^x + e^{-x}}{2}\right)^2 - \left(\frac{e^x - e^{-x}}{2}\right)^2 = \frac{(e^{2x} + 2 + e^{-2x}) - (e^{2x} - 2 + e^{-2x})}{4} = \frac{4}{4} = 1$$
> > 🔗 **Theorie:** [[Ch 02 - Transcendente Functies#3. Hyperbolische Functies]]
