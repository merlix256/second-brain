---
title: "Active Recall: Hoofdstuk 6 - Thermochemie"
tags:
  - study-unit
  - active-recall
  - flashcards
  - thermochemie
course: "Chemie (T1ACH1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.0
priority: medium
---

# 🧠 Active Recall Deck: Hoofdstuk 6 - Thermochemie

---

### Vraag 1: Toestandsfuncties en Padfuncties
**Vraag**: Waarom zijn warmte ($q$) en arbeid ($w$) geen toestandsfuncties, terwijl enthalpie ($H$) en interne energie ($U$) dat wel zijn? Wat is de praktische consequentie hiervan bij chemische reacties?

> [!success]- Toon Antwoord & Uitwerking
> - **Theoretische koppeling**: [[Chapter 06 - Thermochemie#2. Toestandsfuncties en Enthalpie (H)]]
> - **Antwoord**: 
>   Een toestandsfunctie hangt louter af van de actuele toestand van het systeem (zoals $T, P, V$), ongeacht het doorlopen pad. Warmte en arbeid zijn **padfuncties**: de verdeling van de totale energieverandering over warmte en arbeid verschilt naargelang het proces isotherm, adiabatisch, reversibel of irreversibel verloopt.
> - **Praktische consequentie**: Omdat $H$ een toestandsfunctie is, kan de Wet van Hess worden toegepast: we kunnen de reactiewarmte van gevaarlijke of extreem trage reacties exact berekenen via alternatieve reactiepaden ([[Chapter 06 - Thermochemie#4.1 Wet van Hess]]).

---

### Vraag 2: Constant Volume vs. Constante Druk
**Vraag**: Een chemische reactie genereert gas ($n_{\text{gas,producten}} > n_{\text{gas,reagentia}}$). Zal de uitgewisselde warmte groter zijn in een bomcalorimeter ($q_v$) of in een open bekerglas ($q_p$)? Verklaar thermodynamisch.

> [!success]- Toon Antwoord & Uitwerking
> - **Theoretische koppeling**: [[Chapter 06 - Thermochemie#1.2 Arbeid en Warmte]] en [[Chapter 06 - Thermochemie#2.2 Afleiding van Enthalpie bij Constante Druk]]
> - **Antwoord**:
>   1. In een bomcalorimeter is $\Delta V = 0$, waardoor er geen volumearbeid verricht kan worden ($w = 0$). Alle energieverandering manifesteert zich als warmte: $q_v = \Delta U$.
>   2. In een open bekerglas ($P = \text{cte}$) expandeert het gevormde gas tegen de atmosferische druk in. Het systeem verricht arbeid *op* de atmosfeer: $w = -P \Delta V < 0$.
>   3. Omdat $\Delta U = q_p - P \Delta V$, volgt dat $q_p = \Delta U + P \Delta V$.
>   4. Bij een exotherme reactie ($\Delta U < 0$) zal een deel van de vrijgekomen energie verbruikt worden om de atmosfeer weg te duwen ($P\Delta V$), waardoor $|q_p| < |q_v|$: er komt minder warmte vrij naar de omgeving bij constante druk.

---

### Vraag 3: Kwantitatieve Calorimetrie (Examentype)
**Vraag**: $85.0\text{ mL}$ van $0.700\text{ M }\text{HCl}$ wordt gemengd met $85.0\text{ mL}$ van $0.900\text{ M }\text{KOH}$ in een constante-druk calorimeter met $C_{\text{cal}} = 325\text{ J/}^\circ\text{C}$. Beide oplossingen hebben $T_{\text{begin}} = 18.24\text{ }^\circ\text{C}$. De neutralisatiewarmte bedraagt $\Delta H^\circ_{\text{neutralisatie}} = -56.2\text{ kJ/mol}$. 
Bereken de eindtemperatuur $T_{\text{eind}}$. (Neem aan: $\rho = 1.00\text{ g/mL}$, $s = 4.184\text{ J/(g}\cdot^\circ\text{C)}$ en volumes zijn additief).

> [!success]- Toon Antwoord & Uitwerking
> - **Theoretische koppeling**: [[Chapter 06 - Thermochemie#3.2 Constante-Druk Calorimeter ("Coffee-Cup")]]
> - **Stap 1: Stoichiometrie & Limiterend Reagens**
>   - $n(\text{H}^+) = 0.0850\text{ L} \times 0.700\text{ mol/L} = 0.0595\text{ mol}$
>   - $n(\text{OH}^-) = 0.0850\text{ L} \times 0.900\text{ mol/L} = 0.0765\text{ mol}$
>   - Limiterend reagens = $\text{H}^+$ ($0.0595\text{ mol}$ water gevormd).
> - **Stap 2: Berekening van $q_{\text{rxn}}$**
>   $$q_{\text{rxn}} = n \cdot \Delta H^\circ = 0.0595\text{ mol} \times (-56200\text{ J/mol}) = -3343.9\text{ J}$$
> - **Stap 3: Warmtecapaciteit van het calorimetersysteem**
>   - Totale massa vloeistof: $m = 85.0\text{ g} + 85.0\text{ g} = 170.0\text{ g}$
>   - $C_{\text{opl}} = 170.0\text{ g} \times 4.184\text{ J/(g}\cdot^\circ\text{C)} = 711.28\text{ J/}^\circ\text{C}$
>   - $C_{\text{totaal}} = C_{\text{opl}} + C_{\text{cal}} = 711.28 + 325 = 1036.28\text{ J/}^\circ\text{C}$
> - **Stap 4: Berekening van $\Delta T$ en $T_{\text{eind}}$**
>   $$q_{\text{systeem}} = -q_{\text{rxn}} = +3343.9\text{ J}$$
>   $$\Delta T = \frac{q_{\text{systeem}}}{C_{\text{totaal}}} = \frac{3343.9\text{ J}}{1036.28\text{ J/}^\circ\text{C}} = +3.23\text{ }^\circ\text{C}$$
>   $$T_{\text{eind}} = 18.24\text{ }^\circ\text{C} + 3.23\text{ }^\circ\text{C} = 21.47\text{ }^\circ\text{C} \approx \mathbf{21.5\text{ }^\circ\text{C}}$$
