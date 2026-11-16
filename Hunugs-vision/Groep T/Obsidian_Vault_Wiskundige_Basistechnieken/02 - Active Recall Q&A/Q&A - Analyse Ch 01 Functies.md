---
title: "Q&A - Analyse Ch 01: Functies en Continuïteit"
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

# Active Recall Q&A — Analyse Ch 01: Functies en Continuïteit

> [!question] Vraag 1: Bepaal het domein van $f(x) = \frac{\ln(x - 1)}{\sqrt{9 - x^2}}$.
> > [!success]- Antwoord & Uitwerking
> > - Voor $\ln(x - 1)$: $x - 1 > 0 \implies x > 1$.
> > - Voor $\sqrt{9 - x^2}$ in de noemer: $9 - x^2 > 0 \implies -3 < x < 3$.
> > - Doorsnede: $\text{dom}(f) = (1, 3)$.
> > 🔗 **Theorie:** [[Ch 01 - Functies en Continuïteit#1. Reële Functies, Domein en Beeld]]

> [!question] Vraag 2: Wanneer is $f$ continu in $x = a$ en wat zijn de drie types discontinuïteiten?
> > [!success]- Antwoord & Uitwerking
> > $\lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) = f(a)$. Types: ophefbaar (limiet bestaat en is eindig maar $\neq f(a)$), sprong (eenzijdige limieten eindig maar ongelijk), en essentieel/pool (limiet $\pm\infty$ of onbestaand).
> > 🔗 **Theorie:** [[Ch 01 - Functies en Continuïteit#3. Continuïteit & Tussenwaardestelling]]
