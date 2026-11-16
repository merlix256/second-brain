---
title: "Q&A - Analyse Ch 09: Functiereeksen en Reeksontwikkelingen"
course: "Wiskundige basistechnieken (T1AWB1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.5
priority: high
tags:
  - study-unit
  - wiskunde
  - active-recall
---

# Active Recall Q&A — Analyse Ch 09: Functiereeksen en Reeksontwikkelingen

> [!question] Vraag 1: Vind de Maclaurinreeks van $f(x) = \frac{x}{1 + x^2}$ en geef het convergentie-interval.
> > [!success]- Antwoord & Uitwerking
> > Gebruik $\frac{1}{1 - u} = \sum_{n=0}^\infty u^n$ voor $|u| < 1$ met $u = -x^2$:
> > $$\frac{x}{1 + x^2} = x \sum_{n=0}^\infty (-1)^n x^{2n} = \sum_{n=0}^\infty (-1)^n x^{2n+1}$$
> > Convergentie-interval: $|-x^2| < 1 \iff x \in (-1, 1)$ (in $x=\pm 1$ divergeert de algemene term want $a_n \not\to 0$).
> > 🔗 **Theorie:** [[Ch 09 - Functiereeksen en Reeksontwikkelingen#2. Taylor- en Maclaurinreeksen]]

> [!question] Vraag 2: Waarom moeten de randpunten $x_0 \pm R$ van een machtreeks altijd apart onderzocht worden?
> > [!success]- Antwoord & Uitwerking
> > De d'Alembert- en worteltest leveren op de rand $L = 1$, waar de test **geen uitspraak** doet! Je moet $x = x_0 - R$ en $x = x_0 + R$ invullen en elk apart testen (vaak met $p$-reeks of Leibniz).
> > 🔗 **Theorie:** [[Ch 09 - Functiereeksen en Reeksontwikkelingen#1. Machtreeksen]] • [[Bewijs 15 - Taylorveelterm en Afleiding van Coëfficiënten]]
