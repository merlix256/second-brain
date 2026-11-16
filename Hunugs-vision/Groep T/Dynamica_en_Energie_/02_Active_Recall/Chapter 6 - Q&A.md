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

# ❓ Active Recall Q&A: Hoofdstuk 6

> [!tip] Instructie
> Test je vermogen om arbeidsintegralen correct op te stellen en het principe van arbeid en kinetische energie toe te passen.

---

### Vraag 6.1: Arbeid van een Veer
**Vraag:** Een veer met stijfheid $k = 400\text{ N/m}$ heeft een onbelaste lengte $l_0 = 0{,}5\text{ m}$. De veer wordt eerst uitgerekt tot een lengte $l_1 = 0{,}7\text{ m}$ en vervolgens verder uitgerekt tot $l_2 = 0{,}9\text{ m}$. Hoeveel arbeid heeft de veerkracht verricht op het aangesloten deeltje tijdens deze verplaatsing van toestand 1 naar 2?

> [!success]- Toon Uitwerking & Verwijzing
> **Antwoord:** $U_{1-2} = -24\text{ J}$.
> **Stapsgewijze berekening:**
> 1. Bereken de rek $s$ ten opzichte van $l_0$:
>    $$s_1 = l_1 - l_0 = 0{,}7 - 0{,}5 = 0{,}2\text{ m}$$
>    $$s_2 = l_2 - l_0 = 0{,}9 - 0{,}5 = 0{,}4\text{ m}$$
> 2. Pas de formule voor veerarbeid toe:
>    $$U_{1-2} = -\left[\frac{1}{2} k s_2^2 - \frac{1}{2} k s_1^2\right] = \frac{1}{2} k (s_1^2 - s_2^2)$$
> 3. Numeriek invullen:
>    $$U_{1-2} = \frac{1}{2} \times 400 \times \left(0{,}2^2 - 0{,}4^2\right) = 200 \times (0{,}04 - 0{,}16) = 200 \times (-0{,}12) = -24\text{ J}$$
> 4. Het minteken klopt fysisch omdat de veerkracht naar binnen trekt terwijl het deeltje naar buiten beweegt.
> 👉 *Theorie review:* [[Chapter 6 - Arbeid en Energie#2.3 Veerarbeid (Lineair Elastische Veer)]].

---

### Vraag 6.2: Vergelijking Newton vs Arbeid-Energie
**Vraag:** Wanneer kies je bij voorkeur voor het Principe van Arbeid en Kinetische Energie in plaats van de Tweede Wet van Newton $\sum \mathbf{F} = m\mathbf{a}$?

> [!success]- Toon Uitwerking & Verwijzing
> **Antwoord:**
> Arbeid en energie heeft de voorkeur wanneer de opgave vraagt naar snelheden en posities/verplaatsingen zonder dat de versnelling of de verstreken tijd expliciet vereist zijn. Omdat arbeid een scalaire grootheid is, vermijd je vectoriële ontbindingen langs tussenliggende banen en heffen interne krachten en loodrechte normaalkrachten elkaar vanzelf op.
> 👉 *Theorie review:* [[Chapter 6 - Arbeid en Energie#3. Principe van Arbeid en Kinetische Energie]].
