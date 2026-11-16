---
title: "Q&A - Analyse Ch 04: Rijen en Reeksen"
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

# Active Recall Q&A — Analyse Ch 04: Rijen en Reeksen

> [!question] Vraag 1: Onderzoek de convergentie van $\sum_{n=1}^\infty \frac{n!}{3^n}$ en $\sum_{n=1}^\infty \frac{2n+1}{n^3 + 4}$.
> > [!success]- Antwoord & Uitwerking
> > - **Reeks 1 (d'Alembert):** $\lim_{n\to\infty} \frac{(n+1)!/3^{n+1}}{n!/3^n} = \lim_{n\to\infty} \frac{n+1}{3} = +\infty > 1 \implies$ **divergent** (zelfs de algemene term gaat naar $\infty$!).
> > - **Reeks 2 (Limietvergelijking met $v_n = \frac{1}{n^2}$):** $\lim_{n\to\infty} \frac{(2n+1)/(n^3+4)}{1/n^2} = 2 \in (0, \infty)$. Omdat $\sum \frac{1}{n^2}$ een $p$-reeks is met $p=2 > 1$, **convergeert** de reeks!
> > 🔗 **Theorie:** [[Ch 04 - Rijen en Reeksen van Reële Getallen#3. Numerieke Reeksen en Criteria]] • [[Bewijs 14 - Convergentie van de p-Reeks]]

> [!question] Vraag 2: Wat is het verschil tussen absolute en voorwaardelijke convergentie? Geef een klassiek voorbeeld.
> > [!success]- Antwoord & Uitwerking
> > $\sum u_n$ is *absoluut convergent* als $\sum |u_n|$ convergeert (bv. $\sum \frac{(-1)^n}{n^2}$). Ze is *voorwaardelijk convergent* als $\sum u_n$ convergeert (vaak via Leibniz) maar $\sum |u_n|$ divergeert (bv. de alternerende harmonische reeks $\sum \frac{(-1)^{n-1}}{n}$).
> > 🔗 **Theorie:** [[Ch 04 - Rijen en Reeksen van Reële Getallen#3.3 Alternerende Reeksen & Absolute Convergentie]]
