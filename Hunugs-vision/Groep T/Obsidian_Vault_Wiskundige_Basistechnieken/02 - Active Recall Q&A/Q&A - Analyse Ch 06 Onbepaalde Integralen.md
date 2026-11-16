---
course: "Wiskundige basistechnieken (T1AWB1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.0
priority: medium
tags:
  - study-unit
---

# Active Recall Q&A — Analyse Ch 06: Onbepaalde Integralen

> [!question] Vraag 1: Hoe splits je $\frac{x^2 + 2}{(x+1)^2(x-2)}$ in partieelbreuken en hoe vind je de coëfficiënten?
> > [!success]- Antwoord & Uitwerking
> > Aangezien $\deg(\text{teller}) = 2 < \deg(\text{noemer}) = 3$, is geen veeltermdeling nodig.
> > Stel de partieelbreukvorm op:
> > $$\frac{x^2 + 2}{(x+1)^2(x-2)} = \frac{A_1}{x+1} + \frac{A_2}{(x+1)^2} + \frac{B}{x-2}$$
> > Coëfficiënten via limietmethode (cover-up):
> > - $B = \lim_{x \to 2} \frac{x^2 + 2}{(x+1)^2} = \frac{4 + 2}{3^2} = \frac{6}{9} = \frac{2}{3}$.
> > - $A_2 = \lim_{x \to -1} \frac{x^2 + 2}{x-2} = \frac{1 + 2}{-1 - 2} = \frac{3}{-3} = -1$.
> > - $A_1$: Breng op gelijke noemer of vul een testwaarde in (bv. $x = 0$): $\frac{2}{-2} = A_1 - 1 - \frac{1}{3} \implies A_1 = -\frac{2}{3}$.
> > 🔗 **Theorie:** [[Ch 06 - Onbepaalde Integralen#3. Integratie van Rationale Functies (Partieelbreuksplitsing)]]
