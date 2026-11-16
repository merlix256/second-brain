---
title: "Active Recall: Hoofdstuk 11 - Intermoleculaire Krachten"
tags:
  - study-unit
  - active-recall
  - flashcards
  - IMK
  - faseleer
course: "Chemie (T1ACH1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.0
priority: medium
---

# 🧠 Active Recall Deck: Hoofdstuk 11 - Intermoleculaire Krachten

---

### Vraag 1: Kookpuntsvergelijking en Dominantie van Krachten
**Vraag**: Rangschik de volgende verbindingen volgens stijgend kookpunt en verklaar op basis van hun specifieke intermoleculaire interacties:
$$\text{Propaan } (\text{CH}_3\text{CH}_2\text{CH}_3), \quad \text{Dimethylether } (\text{CH}_3\text{OCH}_3), \quad \text{Ethanol } (\text{CH}_3\text{CH}_2\text{OH})$$

> [!success]- Toon Antwoord & Uitwerking
> - **Theoretische koppeling**: [[Chapter 11 - Intermoleculaire krachten#1.2 Van der Waals Krachten]]
> - **Kookpuntsvolgorde**:
>   $$\text{Propaan } (-42\text{ }^\circ\text{C}) < \text{Dimethylether } (-25\text{ }^\circ\text{C}) < \text{Ethanol } (+78\text{ }^\circ\text{C})$$
> - **Mechanistische verklaring**:
>   1. **Propaan ($M_w \approx 44\text{ g/mol}$)**: Apolair molecule ($\mu \approx 0.08\text{ D}$). Vertraagt enkel via zwakke London-dispersiekrachten. Weinig thermische energie vereist om moleculen te scheiden.
>   2. **Dimethylether ($M_w \approx 46\text{ g/mol}$)**: Polair molecule ($\mu \approx 1.30\text{ D}$) met een geknikte $\text{C}-\text{O}-\text{C}$ configuratie. Bevat dipool-dipoolinteracties naast London-dispersie. Kookt hoger dan propaan. Kan echter **onderling geen waterstofbruggen** vormen omdat de $\text{H}$-atomen aan $\text{C}$ gebonden zijn, niet aan $\text{O}$.
>   3. **Ethanol ($M_w \approx 46\text{ g/mol}$)**: Bevat een hydroxylgroep ($-\text{O}-\text{H}$) waarbij waterstof direct aan sterk elektronegatief zuurstof gebonden is. Vormt een uitgebreid netwerk van **waterstofbruggen** ($10 - 40\text{ kJ/mol}$), wat resulteert in een aanzienlijk hoger kookpunt.

---

### Vraag 2: Berekening Dampdruk via Clausius-Clapeyron
**Vraag**: Diethylether heeft een normale verdampingsenthalpie $\Delta H_{\text{vap}} = 26.0\text{ kJ/mol}$ en kookt bij $34.6\text{ }^\circ\text{C}$ onder $1.00\text{ atm}$ ($760\text{ mmHg}$). Bereken de dampdruk van diethylether bij $18.0\text{ }^\circ\text{C}$. ($R = 8.314\text{ J/(mol}\cdot\text{K)}$).

> [!success]- Toon Antwoord & Uitwerking
> - **Theoretische koppeling**: [[Chapter 11 - Intermoleculaire krachten#3.2 Vergelijking van Clausius-Clapeyron]]
> - **Gegevens converteren naar SI-eenheden**:
>   - $T_1 = 34.6 + 273.15 = 307.75\text{ K}$, $P_1 = 760\text{ mmHg}$
>   - $T_2 = 18.0 + 273.15 = 291.15\text{ K}$, $P_2 = ?$
>   - $\Delta H_{\text{vap}} = 26000\text{ J/mol}$
> - **Invullen in Clausius-Clapeyron**:
>   $$\ln\left(\frac{P_2}{P_1}\right) = -\frac{\Delta H_{\text{vap}}}{R} \left( \frac{1}{T_2} - \frac{1}{T_1} \right)$$
>   $$\frac{1}{T_2} - \frac{1}{T_1} = \frac{1}{291.15} - \frac{1}{307.75} = +1.852 \times 10^{-4}\text{ K}^{-1}$$
>   $$\ln\left(\frac{P_2}{P_1}\right) = -\frac{26000}{8.314} \times (1.852 \times 10^{-4}) = -0.5793$$
>   $$\frac{P_2}{P_1} = e^{-0.5793} = 0.5603 \implies P_2 = 760 \times 0.5603 = \mathbf{425.8\text{ mmHg}} \quad (\approx 0.560\text{ atm})$$

---

### Vraag 3: Fasediagram van Water (Examentype)
**Vraag**: Waarom heeft de smeltcurve ($S-L$ lijn) in het fasediagram van water een negatieve helling ($\frac{dP}{dT} < 0$), en wat gebeurt er als men ijs bij $-1\text{ }^\circ\text{C}$ onderwerpt aan hoge druk?

> [!success]- Toon Antwoord & Uitwerking
> - **Theoretische koppeling**: [[Chapter 11 - Intermoleculaire krachten#3.3 Fasediagrammen]]
> - **Antwoord**:
>   Vloeibaar water heeft een grotere dichtheid dan ijs ($V_{\text{mol,ijs}} > V_{\text{mol,water}}$). Volgens Le Châtelier verschuift het evenwicht bij externe drukverhoging naar de fase met de kleinste dichtheidsinhoud (het vloeibare water). Hierdoor daalt het smeltpunt bij hogere druk. IJs van $-1\text{ }^\circ\text{C}$ zal bij voldoende samendrukking **smelten tot vloeibaar water**.
