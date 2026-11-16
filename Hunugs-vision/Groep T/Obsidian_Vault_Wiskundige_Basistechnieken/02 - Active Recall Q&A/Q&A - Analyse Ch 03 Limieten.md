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

# Active Recall Q&A — Analyse Ch 03: Limieten

> [!question] Vraag 1: Hoe bereken je $\lim_{x \to 0} \frac{1 - \cos x}{x^2}$ zonder en met l'Hôpital?
> > [!success]- Antwoord & Uitwerking
> > - **Methode 1 (Trigonometrie):** Vermenigvuldig teller en noemer met $1 + \cos x$:
> >   $$\lim_{x \to 0} \frac{1 - \cos^2 x}{x^2(1 + \cos x)} = \lim_{x \to 0} \left(\frac{\sin x}{x}\right)^2 \cdot \frac{1}{1 + \cos x} = 1^2 \cdot \frac{1}{2} = \frac{1}{2}$$
> > - **Methode 2 (de l'Hôpital, vorm $[0/0]$):**
> >   $$\lim_{x \to 0} \frac{\sin x}{2x} = \frac{1}{2} \lim_{x \to 0} \frac{\sin x}{x} = \frac{1}{2}$$
> > 🔗 **Theorie:** [[Ch 03 - Limieten#2.2 Belangrijke Standaardlimiet (Sinus Cardinalis)]] en [[Ch 03 - Limieten#3. Regel van de l'Hôpital]]
