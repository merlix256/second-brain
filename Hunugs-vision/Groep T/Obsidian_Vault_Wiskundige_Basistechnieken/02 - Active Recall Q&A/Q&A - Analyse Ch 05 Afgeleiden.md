---
title: "Q&A - Analyse Ch 05: Afgeleiden en Toepassingen"
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

# Active Recall Q&A — Analyse Ch 05: Afgeleiden en Toepassingen

> [!question] Vraag 1: Bepaal $y'$ voor $y = x^{\sin x}$ ($x > 0$).
> > [!success]- Antwoord & Uitwerking
> > Gebruik **logaritmisch differentiëren**:
> > $\ln y = \sin x \cdot \ln x \implies \frac{y'}{y} = \cos x \ln x + \frac{\sin x}{x} \implies y' = x^{\sin x}\left(\cos x \ln x + \frac{\sin x}{x}\right)$.
> > 🔗 **Theorie:** [[Ch 05 - Afgeleiden en Toepassingen#2. Rekenregels en Standaardafgeleiden]]

> [!question] Vraag 2: Waarom heeft $f(x) = |x|$ in $x = 0$ géén afgeleide hoewel ze er continu is?
> > [!success]- Antwoord & Uitwerking
> > $\lim_{h\to 0^-} \frac{|h|-0}{h} = -1 \neq +1 = \lim_{h\to 0^+} \frac{|h|-0}{h}$. Linker- en rechterafgeleide zijn verschillend (knikpunt).
> > 🔗 **Bewijs:** [[Bewijs 04 - Verband Afleidbaarheid en Continuïteit]]
