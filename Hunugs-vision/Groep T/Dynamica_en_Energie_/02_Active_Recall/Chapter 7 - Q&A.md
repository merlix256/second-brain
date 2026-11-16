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

# ❓ Active Recall Q&A: Hoofdstuk 7

> [!tip] Instructie
> Test je begrip van potentiële energie en behoudswetten.

---

### Vraag 7.1: Nulpunt van de Potentiële Energie
**Vraag:** Maakt het voor de berekening van de eindsnelheid via $T_1 + V_1 = T_2 + V_2$ uit waar je de zwaartekrachtdatum ($y = 0$) legt? Verklaar.

> [!success]- Toon Uitwerking & Verwijzing
> **Antwoord:** **Neen, de keuze van de datum is volkomen arbitrair.**
> **Verklaring:** In de energievergelijking telt enkel het *verschil* in potentiële energie:
> $$T_2 - T_1 = V_1 - V_2 = mg(y_1 - y_2) = -mg \Delta y$$
> Een verschuiving van de referentielijn met een constante hoogte $h_0$ voegt aan zowel $V_1$ als $V_2$ de term $mgh_0$ toe, welke aan weerszijden van de gelijkheid tegen elkaar wegvalt.
> 👉 *Theorie review:* [[Chapter 7 - Behoud van Energie#1.1 Zwaartekracht Potentiële Energie (V_g)]].

---

### Vraag 7.2: Verticaal Gelanceerde Massa tegen een Veer
**Vraag:** Een blok van $2\text{ kg}$ wordt vanop de grond verticaal omhoog geschoten met $v_1 = 10\text{ m/s}$ en botst op een hoogte van $3\text{ m}$ tegen een ongespannen verticale veer met $k = 500\text{ N/m}$. Hoe bereken je de maximale indrukking $x$ van de veer?

> [!success]- Toon Uitwerking & Verwijzing
> **Antwoord:**
> 1. Toestand 1 (lanceerpunt op de grond, datum $y=0$):
>    $$T_1 = \frac{1}{2} m v_1^2 = \frac{1}{2} \times 2 \times 10^2 = 100\text{ J}, \qquad V_1 = 0$$
> 2. Toestand 2 (maximale indrukking van de veer, massa staat ogenblikkelijk stil):
>    $$T_2 = 0$$
>    Totale hoogte is $y_2 = 3 + x$.
>    $$V_2 = V_{g,2} + V_{e,2} = mg(3 + x) + \frac{1}{2} k x^2 = 2 \times 9{,}81 (3 + x) + 250 x^2$$
> 3. Energiebehoud $T_1 + V_1 = T_2 + V_2$:
>    $$100 = 19{,}62 (3 + x) + 250 x^2 \implies 250 x^2 + 19{,}62 x - 41{,}14 = 0$$
> 4. Oplossen van de vierkantsvergelijking levert de positieve compressie $x$.
> 👉 *Theorie review:* [[Chapter 7 - Behoud van Energie#2. Behoud van Mechanische Energie]].
