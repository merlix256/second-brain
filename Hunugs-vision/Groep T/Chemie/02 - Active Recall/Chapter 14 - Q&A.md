---
title: "Active Recall: Hoofdstuk 14 - Chemisch Evenwicht"
tags:
  - study-unit
  - active-recall
  - flashcards
  - chemisch-evenwicht
  - le-chatelier
course: "Chemie (T1ACH1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.0
priority: medium
---

# 🧠 Active Recall Deck: Hoofdstuk 14 - Chemisch Evenwicht

---

### Vraag 1: Berekening van $K_p$ en Evenwichtssamenstelling via ICE
**Vraag**: In een vat van $2.00\text{ L}$ bij $400\text{ K}$ wordt $0.800\text{ mol }\text{PCl}_5(g)$ gebracht. Bij evenwicht is $0.200\text{ mol }\text{Cl}_2(g)$ aanwezig volgens:
$$\text{PCl}_{5(g)} \rightleftharpoons \text{PCl}_{3(g)} + \text{Cl}_{2(g)}$$
1. Bereken de evenwichtsconcentraties van alle componenten en $K_c$.
2. Bereken $K_p$ bij deze temperatuur. ($R = 0.08206\text{ L}\cdot\text{atm}/(\text{mol}\cdot\text{K})$).

> [!success]- Toon Antwoord & Uitwerking
> - **Theoretische koppeling**: [[Chapter 14 - Chemisch evenwicht#1. De Evenwichtsconstante (Kc en Kp)]] en [[Chapter 14 - Chemisch evenwicht#3. Berekeningen met ICE-tabellen]]
> - **ICE-Tabel (in Molariteit $M = n / 2.00\text{ L}$)**:
>   - Begin: $[\text{PCl}_5]_0 = 0.400\text{ M}$, $[\text{PCl}_3]_0 = 0$, $[\text{Cl}_2]_0 = 0$
>   - Evenwicht: $[\text{Cl}_2]_{eq} = \frac{0.200\text{ mol}}{2.00\text{ L}} = 0.100\text{ M} \implies x = 0.100\text{ M}$
>   - $[\text{PCl}_3]_{eq} = x = 0.100\text{ M}$
>   - $[\text{PCl}_5]_{eq} = 0.400 - x = 0.300\text{ M}$
> - **1. Berekening van $K_c$**:
>   $$K_c = \frac{[\text{PCl}_3][\text{Cl}_2]}{[\text{PCl}_5]} = \frac{(0.100)(0.100)}{0.300} = \mathbf{0.0333\text{ M}}$$
> - **2. Berekening van $K_p$**:
>   $$\Delta n_{\text{gas}} = (1 + 1) - 1 = +1$$
>   $$K_p = K_c(RT)^{\Delta n} = (0.0333)(0.08206 \times 400)^1 = \mathbf{1.09\text{ atm}}$$

---

### Vraag 2: Le Châtelier Dynamische Verschuivingen
**Vraag**: Beschouw het exotherme Haber-Bosch proces:
$$\text{N}_{2(g)} + 3\text{H}_{2(g)} \rightleftharpoons 2\text{NH}_{3(g)} \quad \Delta H^\circ = -92.4\text{ kJ/mol}$$
Voorspel het effect (verschuiving links/rechts/geen + verandering van $K$) van:
1. Drukverhoging door volumehalvering.
2. Continue verwijdering van ammoniak via condensatie.
3. Temperatuurstijging.
4. Toevoegen van een ijzerkatalysator.

> [!success]- Toon Antwoord & Uitwerking
> - **Theoretische koppeling**: [[Chapter 14 - Chemisch evenwicht#4. Het Principe van Le Châtelier]]
> - **Antwoorden**:
>   1. **Drukverhoging**: Links zijn 4 mol gas, rechts 2 mol gas. Verschuift naar **rechts** (minste gasmollen). $K$ blijft gelijk.
>   2. **Verwijdering $\text{NH}_3$**: Verschuift naar **rechts** om het producttekort aan te vullen. $K$ blijft gelijk.
>   3. **Temperatuurstijging**: Reactie is exotherm (warmte is 'product'). Systeem wil afkoelen $\implies$ verschuift naar **links**. **$K$ daalt**.
>   4. **Katalysator**: Versnelt heen- en terugreactie evenveel. **Geen verschuiving**, $K$ blijft constant.
