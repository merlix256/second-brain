---
course: "Dynamica en energie (T1ADE1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.0
priority: medium
tags:
  - study-unit
---

# ❓ Active Recall Q&A: Hoofdstuk 2

> [!tip] Instructie
> Test je parate kennis rond variabele versnelling en kromtestraal.

---

### Vraag 2.1: Versnelling gegeven als Positiefunctie $a(s)$
**Vraag:** Een deeltje start vanuit rust ($v(0) = 0$) bij $s=0$ en ondergaat een versnelling $a(s) = 2s + 1$. Hoe bereken je de snelheid op positie $s = 3\text{ m}$?

> [!success]- Toon Uitwerking & Verwijzing
> **Antwoord:** $v = 4\text{ m/s}$.
> **Stapsgewijze berekening:**
> 1. Gebruik de kettingregel differentiaalrelatie:
>    $$a\,ds = v\,dv$$
> 2. Stel de integralen op met de corresponderende grenzen:
>    $$\int_0^3 (2s + 1)\,ds = \int_0^v v'\,dv'$$
> 3. Integreer beide zijden:
>    $$\left[ s^2 + s \right]_0^3 = \left[ \frac{1}{2}v^2 \right]_0^v \implies (9 + 3) - 0 = \frac{1}{2}v^2 \implies 12 = \frac{1}{2}v^2 \implies v^2 = 24 \implies v = \sqrt{24} \approx 4{,}90\text{ m/s}$$
> 👉 *Theorie review:* [[Chapter 2 - Variabele Versnelling#2.2 Versnelling als functie van de positie a = f(s)]].

---

### Vraag 2.2: Kromtestraal in de Top van een Parabool
**Vraag:** Gegeven de paraboolbaan $y = 10 - 0{,}1 x^2$. Wat is de kromtestraal $\rho$ in de top van het traject ($x = 0$)?

> [!success]- Toon Uitwerking & Verwijzing
> **Antwoord:** $\rho = 5\text{ m}$.
> **Stapsgewijze berekening:**
> 1. Bereken de eerste en tweede afgeleide van $y(x)$:
>    $$\frac{dy}{dx} = -0{,}2 x, \qquad \frac{d^2y}{dx^2} = -0{,}2$$
> 2. Evalueer in $x = 0$:
>    $$\left.\frac{dy}{dx}\right|_{x=0} = 0, \qquad \left.\frac{d^2y}{dx^2}\right|_{x=0} = -0{,}2$$
> 3. Pas de kromtestraalformule toe:
>    $$\rho = \frac{\left[1 + (0)^2\right]^{3/2}}{\|-0{,}2\|} = \frac{1}{0{,}2} = 5\text{ m}$$
> 👉 *Theorie review:* [[Chapter 2 - Variabele Versnelling#Kromtestraal van een Pad]].
