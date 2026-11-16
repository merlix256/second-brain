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

# ❓ Active Recall Q&A: Hoofdstuk 1

> [!tip] Instructie
> Test je parate kennis. Probeer eerst zelfstandig het antwoord te formuleren vooraleer je de toelichting openklikt. Gebruik de backlinks om hiaten in de theorie onmiddellijk te remediëren.

---

### Vraag 1.1: Voorwaarde voor de Kwadratische Formule
**Vraag:** Mag je de formule $v^2 = v_0^2 + 2 a_c (s - s_0)$ toepassen op een object waarvan de versnelling gegeven is door $a(t) = 3t^2$? Waarom wel of niet?

> [!success]- Toon Uitwerking & Verwijzing
> **Antwoord:** **Neen, absoluut niet.**
> **Verklaring:** De vergelijking $v^2 = v_0^2 + 2 a_c (s - s_0)$ is het wiskundige resultaat van de integratie van $a\,ds = v\,dv$ onder de strikte aanname dat $a$ constant ($a_c$) is en buiten de integraal gehaald mag worden. Wanneer $a(t) = 3t^2$, is de versnelling tijdsafhankelijk en moet men eerst integreren via $v(t) = \int a(t)\,dt$ en vervolgens $s(t) = \int v(t)\,dt$.
> 👉 *Theorie review:* [[Chapter 1 - Constante Versnelling en Cirkelbeweging#Bewegingsvergelijkingen Constante Versnelling]] en [[Chapter 2 - Variabele Versnelling#Differentiële Grondrelaties]].

---

### Vraag 1.2: Berekening van Totale Afstand uit een $v(t)$-Grafiek
**Vraag:** Een voorwerp beweegt gedurende 30 seconden met een constante snelheid van $8\text{ m/s}$ en vertraagt vervolgens lineair tot stilstand op $t = 60\text{ s}$ (zie Oefening 1.1). Wat is de totale afgelegde afstand?

> [!success]- Toon Uitwerking & Verwijzing
> **Antwoord:** $\Delta s_{\text{totaal}} = 360\text{ m}$.
> **Stapsgewijze berekening:**
> De totale afstand is gelijk aan de oppervlakte onder de $v(t)$-grafiek:
> 1. Fase 1 ($0 \to 30\text{ s}$): Rechthoek $\implies \Delta s_1 = v \cdot \Delta t = 8\text{ m/s} \times 30\text{ s} = 240\text{ m}$.
> 2. Fase 2 ($30 \to 60\text{ s}$): Driehoek $\implies \Delta s_2 = \frac{1}{2} \cdot \text{basis} \cdot \text{hoogte} = \frac{1}{2} \times (60 - 30)\text{ s} \times 8\text{ m/s} = 120\text{ m}$.
> 3. Totaal: $\Delta s_{\text{totaal}} = 240\text{ m} + 120\text{ m} = 360\text{ m}$.
> 👉 *Theorie review:* [[Chapter 1 - Constante Versnelling en Cirkelbeweging#3. Grafische Analyse van Bewegingen (s-t, v-t, a-t)]].

---

### Vraag 1.3: Brekend Touw bij Verticale Cirkelbeweging
**Vraag:** Een massa wordt met een constante snelheid $v_0 = 2\text{ m/s}$ in een verticaal vlak rondgedraaid aan een touw met lengte $R = 0{,}5\text{ m}$. Wat is de versnelling van de massa vlak vóór het breken van het touw, en wat is de versnelling onmiddellijk na het breken (zie Oefening 1.5)?

> [!success]- Toon Uitwerking & Verwijzing
> **Antwoord:**
> - **Vlak vóór het breken:** De massa voert een cirkelbeweging uit. Omdat $v_0$ constant is, is $a_t = 0$. Er is enkel een normale/centripetale versnelling gericht naar het rotatiecentrum:
>   $$a_n = \frac{v_0^2}{R} = \frac{2^2}{0{,}5} = 8\text{ m/s}^2$$.
>   In vectoriële cartesische componenten (bij $\theta = 300^\circ$): $\mathbf{a} = 4\mathbf{i} + 6{,}93\mathbf{j}\text{ m/s}^2$.
> - **Vlak na het breken:** De fysieke dwangkracht (touwkracht) valt ogenblikkelijk weg. De massa voert vanaf dat ogenblik een vrije valbeweging uit. De enige versnelling is de zwaartekrachtversnelling:
>   $$\mathbf{a} = -g \mathbf{j} = -9{,}81\mathbf{j}\text{ m/s}^2$$.
> 👉 *Theorie review:* [[Chapter 1 - Constante Versnelling en Cirkelbeweging#5. Cirkelbeweging en Intrinsieke (t-n) Coördinaten]].
