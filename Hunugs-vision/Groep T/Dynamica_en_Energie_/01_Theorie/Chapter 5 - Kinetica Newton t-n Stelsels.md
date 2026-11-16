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

# 📖 Hoofdstuk 5: Kinetica van een Puntmassa — Normaal-Tangentiële Stelsels ($t-n$)

> [!abstract] Overzicht & Leerdoelen
> - **Leerdoel:** Het opstellen van bewegingsvergelijkingen voor deeltjes die gekromde banen doorlopen met behulp van het intrinsieke $t-n-b$ assenstelsel, en het berekenen van bochtenkrachten, normaalkrachten en loslatingsvoorwaarden.
> - **Handboek:** Hibbeler Chapter 13 (§13.5).
> - **Master Formularium:** [[Formularium#2. Kinetica van een Puntmassa (Newton & Bewegingsvergelijkingen)]].
> - **Actieve Herroeping:** [[Chapter 5 - Q&A]].

---

## 1. Het Intrinsieke Coördinatenstelsel ($t-n-b$)

Wanneer de baan van een deeltje gekend is (bv. cirkelbaan, looping, achtbaan, kromme heuvelkam), is ontbinding volgens de raaklijn en normaal aanzienlijk eenvoudiger dan volgens vaste cartesische assen:

![[Slide_tnb_Coordinate_System.png]]
*(Placeholder: Deeltje op kromme baan met assen ut tangentiëel, un normaal naar binnen gericht, en ub binormaal)*

- **Tangentiële as $\mathbf{u}_t$:** Rakend aan de baan, in de richting van de momentane snelheid.
- **Normale as $\mathbf{u}_n$:** Loodrecht op $\mathbf{u}_t$, liggend in het osculerende vlak en wijzend naar het krommingsmiddelpunt.
- **Binormale as $\mathbf{u}_b$:** Loodrecht op het $t-n$ vlak: $\mathbf{u}_b = \mathbf{u}_t \times \mathbf{u}_n$.

---

## 2. Bewegingsvergelijkingen in $t-n-b$

Toepassing van $\sum \mathbf{F} = m\mathbf{a}$ met $\mathbf{a} = a_t \mathbf{u}_t + a_n \mathbf{u}_n + 0 \mathbf{u}_b$:

$$\sum F_t = m a_t = m \frac{dv}{dt} = m \left(v \frac{dv}{ds}\right)$$
$$\sum F_n = m a_n = m \frac{v^2}{\rho}$$
$$\sum F_b = 0$$

> [!tip] Fysische Betekenis
> - $\sum F_t$ zorgt voor verandering van de *grootte* van de snelheid (versnellen of afremmen).
> - $\sum F_n$ levert de benodigde centripetale kracht om het deeltje in zijn bocht te dwingen. Deze kracht wordt geleverd door echte fysieke interacties (zoals normaalkracht, wrijving, gravitatiecomponent of draadkracht).

---

## 3. Typische Examenthema's: Looping en Loslaten

Bij een object dat over een bolle heuvel rijdt of binnenin een verticale cirkelbaan beweegt:
- De normaalkracht $N$ van de ondergrond wijst altijd duwend naar het deeltje toe ($N \ge 0$).
- **Loslatingscriterium:** Het deeltje verliest contact met de ondergrond precies op het ogenblik dat:
  $$N = 0$$
  Substitueer $N=0$ in $\sum F_n = m \frac{v^2}{\rho}$ om de kritieke snelheid of kritieke loslatingshoek $\theta_{\text{los}}$ te berekenen.

---

## 📝 Samenvatting
- In het $t-n$ stelsel is de normale versnelling altijd gekoppeld aan de baansnelheid via $a_n = v^2/\rho$.
- Er is geen versnelling loodrecht op het osculerende vlak: $\sum F_b = 0$.
- Loslaten van een oppervlak betekent dynamisch dat de normaalkracht $N$ naar nul nadert.
