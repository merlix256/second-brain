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

# 📖 Hoofdstuk 4: Kinetica van een Puntmassa — Wetten van Newton (Cartesisch)

> [!abstract] Overzicht & Leerdoelen
> - **Leerdoel:** Het correct opstellen van Vrijlichaamschema's (VLS) en kinetische schema's, en het toepassen van de Tweede Wet van Newton $\sum \mathbf{F} = m\mathbf{a}$ in cartesische coördinatenstelsels.
> - **Handboek:** Hibbeler Chapter 13 (§13.1 – §13.4).
> - **Master Formularium:** [[Formularium#2. Kinetica van een Puntmassa (Newton & Bewegingsvergelijkingen)]].
> - **Actieve Herroeping:** [[Chapter 4 - Q&A]].

---

## 1. Wetten van Newton

1. **Eerste Wet (Traagheidswet):** Een deeltje in rust blijft in rust, en een deeltje in beweging behoudt zijn constante vectoriële snelheid, tenzij er een netto externe kracht op inwerkt.
2. **Tweede Wet (Grondwet van de Dynamica):** De resultante van alle externe krachten die op een deeltje inwerken is gelijk aan de verandering van zijn lineair momentum in de tijd:
   $$\sum \mathbf{F} = \frac{d(m\mathbf{v})}{dt} = m \mathbf{a} \quad (\text{voor constante massa } m)$$
3. **Derde Wet (Actie-Reactie):** De krachten die twee deeltjes op elkaar uitoefenen zijn altijd gelijk in grootte, tegengesteld van zin en collineair.

---

## 2. VLS Methodologie (Vrij Lichaam Schema / Free Body Diagram)

Het Vrijlichaamschema is de absolute hoeksteen van kinetische analyse. Een correct VLS isoleert het deeltje en tekent **alleen echte interactiekrachten**:

![[Slide_VLS_Blok_Helling_Wrijving.png]]
*(Placeholder: VLS van een blok op een helling met gewicht W, normaalkracht N, wrijving Fw en trekkracht P)*

### Checklist voor een Vlekkeloos VLS:
1. **Isoleer het deeltje:** Teken de puntmassa los van zijn omgeving en fysieke contacten.
2. **Afstandskrachten:** Teken het eigen gewicht $\mathbf{W} = m\mathbf{g}$ verticaal omlaag.
3. **Contactkrachten:**
   - **Normaalkracht ($N$):** Loodrecht op het contactoppervlak, altijd duwend naar het deeltje toe.
   - **Wrijvingskracht ($F_w$):** Evenwijdig aan het contactoppervlak, tegengesteld aan de relatieve beweging ($F_w = \mu_k N$ bij glijden).
   - **Kabelspanning ($T$):** Werkt altijd in de richting van het touw, trekkend van het deeltje weg.
   - **Veerkracht ($F_v$):** Werkt langs de hartlijn van de veer: $F_v = k(l - l_0)$.
4. **GEEN Traagheidskrachten op het VLS:** De term $m\mathbf{a}$ hoort **NOOIT** op het VLS!

---

## 3. Cartesische Projecties

Kies een vast inertiaalstelsel $(x, y, z)$. Ontbind de vectoriële bewegingsvergelijking in scalaire componenten:

$$\sum F_x = m a_x$$
$$\sum F_y = m a_y$$
$$\sum F_z = m a_z$$

> [!tip] Keuze van de Assen
> Leg één as (bv. de $x$-as) parallel aan de verwachte bewegingsrichting. Als het deeltje uitsluitend langs die as versnelt, geldt $a_y = 0$, waardoor $\sum F_y = 0$ direct de normaalkracht $N$ oplevert.

---

## 📝 Samenvatting
- $\sum \mathbf{F} = m\mathbf{a}$ verbindt de oorzaak van beweging (krachten) met het kinetische gevolg (versnelling).
- Het VLS toont strikt reële krachten; het kinetisch diagram toont de resultante vector $m\mathbf{a}$.
- De wrijvingskracht $F_w = \mu_k N$ vereist altijd eerst het bepalen van de normaalkracht via de evenwichtsvergelijking loodrecht op de baan.
