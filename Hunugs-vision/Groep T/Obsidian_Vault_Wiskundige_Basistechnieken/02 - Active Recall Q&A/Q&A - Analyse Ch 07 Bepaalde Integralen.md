---
title: "Q&A - Analyse Ch 07: Bepaalde Integralen"
course: "Wiskundige basistechnieken (T1AWB1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.0
priority: high
tags:
  - study-unit
  - wiskunde
  - active-recall
---

# Active Recall Q&A — Analyse Ch 07: Bepaalde Integralen

> [!question] Vraag 1: Bereken $\frac{d}{dx} \int_{x^2}^{3x} \sin(t^2)\,dt$.
> > [!success]- Antwoord & Uitwerking
> > Via de Hoofdstelling van de Integraalrekening + kettingregel:
> > $$\sin((3x)^2)\cdot 3 - \sin((x^2)^2)\cdot 2x = 3\sin(9x^2) - 2x\sin(x^4)$$
> > 🔗 **Theorie:** [[Ch 07 - Bepaalde Integralen#2. Hoofdstelling van de Integraalrekening]] • [[Bewijs 11 - Hoofdstelling van de Integraalrekening]]

> [!question] Vraag 2: Waarom mag je $\int_{-1}^1 \frac{1}{x^2}\,dx$ niet zomaar als $\left[-\frac{1}{x}\right]_{-1}^1 = -2$ uitrekenen?
> > [!success]- Antwoord & Uitwerking
> > De integrand $\frac{1}{x^2} > 0$ heeft een **verticale asymptoot (pool)** in $x = 0 \in [-1, 1]$. Het is een oneigenlijke integraal van type II: $\int_0^1 \frac{1}{x^2}\,dx = \lim_{\varepsilon \to 0^+} (\frac{1}{\varepsilon} - 1) = +\infty$, dus de integraal **divergeert**!
> > 🔗 **Theorie:** [[Ch 07 - Bepaalde Integralen#3. Substitutie & Oneigenlijke Integralen]]
