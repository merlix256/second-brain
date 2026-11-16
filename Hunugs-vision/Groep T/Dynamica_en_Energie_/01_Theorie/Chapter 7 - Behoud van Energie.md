---
course: "Dynamica en energie (T1ADE1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: high
tags:
  - study-unit
---

# 📖 Hoofdstuk 7: Kinetica — Behoud van Mechanische Energie

> [!abstract] Overzicht & Leerdoelen
> - **Leerdoel:** Het definiëren van potentiële energiefuncties voor conservatieve krachtvelden en het toepassen van de wet van behoud van mechanische energie op dynamische systemen met zwaartekracht en elastische elementen.
> - **Handboek:** Hibbeler Chapter 14 (§14.5, §14.6).
> - **Master Formularium:** [[Formularium#3. Arbeid, Energie en Behoudswetten]].
> - **Actieve Herroeping:** [[Chapter 7 - Q&A]].

---

## 1. Conservatieve Krachten en Potentiële Energie

Een kracht $\mathbf{F}$ is **conservatief** indien de arbeid verricht op een deeltje tussen twee punten onafhankelijk is van het gekozen pad. Voor een conservatieve kracht kan een scalaire potentiële energiefunctie $V(\mathbf{r})$ worden gedefinieerd zodanig dat:

$$U_{1-2} = V_1 - V_2 = -\Delta V$$

### 1.1 Zwaartekracht Potentiële Energie ($V_g$)
Ten opzichte van een willekeurig gekozen referentievlak (datum $y = 0$):
$$V_g = m g y$$
- Boven de datum: $V_g > 0$.
- Onder de datum: $V_g < 0$.

### 1.2 Elastische Potentiële Energie ($V_e$)
Voor een lineaire veer met veerconstante $k$ en rek $s = l - l_0$:
$$V_e = \frac{1}{2} k s^2$$
Omdat $s$ gekwadrateerd wordt, is de potentiële energie van een ideale veer **altijd positief of nul** ($V_e \ge 0$), ongeacht of de veer uitgerekt of ingedrukt is!

---

## 2. Behoud van Mechanische Energie

Wanneer op een mechanisch systeem uitsluitend conservatieve krachten werkzaam zijn (of wanneer niet-conservatieve krachten zoals normaalkrachten geen arbeid verrichten omdat ze loodrecht op de verplaatsing staan):

$$T_1 + V_1 = T_2 + V_2$$

Of uitgeschreven met alle energiecomponenten:
$$\frac{1}{2} m v_1^2 + m g y_1 + \frac{1}{2} k s_1^2 = \frac{1}{2} m v_2^2 + m g y_2 + \frac{1}{2} k s_2^2$$

### Algemene formulering met wrijving of externe arbeid:
Indien er ook niet-conservatieve krachten arbeid verrichten ($U_{1-2}^{\text{nc}}$):
$$T_1 + V_1 + \sum U_{1-2}^{\text{nc}} = T_2 + V_2$$

---

## 📝 Samenvatting
- Potentiële energie vervangt de arbeidsintegraal van conservatieve krachten door een eenvoudig toestandskenmerk.
- Het behoud van mechanische energie is de krachtigste oplosmethode wanneer begin- en eindtoestanden van snelheid en positie gevraagd zijn zónder expliciet tijdsverloop.
