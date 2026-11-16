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

# ❓ Active Recall Q&A: Hoofdstuk 3

> [!tip] Instructie
> Test je vaardigheid in het analyseren van gekoppelde katrollen en relatieve bewegingsvectoren.

---

### Vraag 3.1: Katrol met Dubbele Lus
**Vraag:** Een blok $A$ hangt aan een vaste katrol, en een blok $B$ hangt in een lus van een bewegende katrol ondersteund door dezelfde onrekbare kabel waarvan de lengte constant is ($s_A + 2s_B = L$). Blok $A$ daalt met een snelheid van $4\text{ m/s}$. Wat is de snelheid en bewegingsrichting van blok $B$?

> [!success]- Toon Uitwerking & Verwijzing
> **Antwoord:** Blok $B$ stijgt met een snelheid van $2\text{ m/s}$ ($v_B = -2\text{ m/s}$).
> **Stapsgewijze berekening:**
> 1. Noteer de lengtevergelijking t.o.v. de vaste ophanging (datum bovenaan):
>    $$s_A + 2 s_B = L$$
> 2. Differentiëren naar de tijd $t$:
>    $$\dot{s}_A + 2 \dot{s}_B = 0 \implies v_A + 2 v_B = 0$$
> 3. Blok $A$ daalt $\implies v_A = +4\text{ m/s}$ (weg van de datum):
>    $$4 + 2 v_B = 0 \implies 2 v_B = -4 \implies v_B = -2\text{ m/s}$$
> 4. Het minteken betekent dat $s_B$ afneemt: blok $B$ beweegt naar de datum toe (stijgt).
> 👉 *Theorie review:* [[Chapter 3 - Afhankelijke en Relatieve Beweging#Katrolsystemen en Kinematische Koppelingen]].

---

### Vraag 3.2: Relatieve Snelheid van Schepen
**Vraag:** Schip $A$ vaart noordwaarts met $30\text{ km/u}$. Schip $B$ vaart oostwaarts met $40\text{ km/u}$. Wat is de relatieve snelheid $\mathbf{v}_{B/A}$ van schip $B$ ten opzichte van schip $A$?

> [!success]- Toon Uitwerking & Verwijzing
> **Antwoord:** $\|\mathbf{v}_{B/A}\| = 50\text{ km/u}$, gericht naar het zuidoosten (richtingshoek $-36{,}87^\circ$).
> **Stapsgewijze berekening:**
> 1. Stel de vectoren op in een $(x = \text{Oost}, y = \text{Noord})$ stelsel:
>    $$\mathbf{v}_A = 30\mathbf{j}\text{ km/u}, \qquad \mathbf{v}_B = 40\mathbf{i}\text{ km/u}$$
> 2. Relatieve snelheidsdefinitie:
>    $$\mathbf{v}_{B/A} = \mathbf{v}_B - \mathbf{v}_A = 40\mathbf{i} - 30\mathbf{j}\text{ km/u}$$
> 3. Grootte:
>    $$\|\mathbf{v}_{B/A}\| = \sqrt{40^2 + (-30)^2} = 50\text{ km/u}$$
> 👉 *Theorie review:* [[Chapter 3 - Afhankelijke en Relatieve Beweging#2. Relatieve Beweging (Translerend Referentiekader)]].
