---
title: "Q&A - LinAlg Ch 01: Complexe Getallen"
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

# Active Recall Q&A — LinAlg Ch 01: Complexe Getallen

> [!question] Vraag 1: Schrijf $z = 1 - \sqrt{3}\,i$ in goniometrische en exponentiële vorm en bereken $z^6$.
> > [!success]- Antwoord & Uitwerking
> > - Modulus: $|z| = \sqrt{1^2 + (-\sqrt{3})^2} = 2$.
> > - Argument (4e kwadrant!): $\theta = -\frac{\pi}{3}$ (of $\frac{5\pi}{3}$).
> > - Goniometrisch/Exponentieel: $z = 2\left(\cos(-\frac{\pi}{3}) + i\sin(-\frac{\pi}{3})\right) = 2 e^{-i\pi/3}$.
> > - De Moivre: $z^6 = 2^6 e^{-6i\pi/3} = 64 e^{-2\pi i} = 64$.
> > 🔗 **Theorie:** [[Ch 01 - Complexe Getallen]]

> [!question] Vraag 2: Hoe vind je alle $n$ complexe $n$-demachtswortels van $w = r e^{i\theta}$?
> > [!success]- Antwoord & Uitwerking
> > $$z_k = \sqrt[n]{r} \cdot e^{i\frac{\theta + 2k\pi}{n}}, \quad k = 0, 1, \dots, n-1$$
> > Meetkundig liggen de $n$ wortels op de hoekpunten van een regelmatige $n$-hoek op een cirkel met straal $\sqrt[n]{r}$.
> > 🔗 **Theorie:** [[Ch 01 - Complexe Getallen]]
