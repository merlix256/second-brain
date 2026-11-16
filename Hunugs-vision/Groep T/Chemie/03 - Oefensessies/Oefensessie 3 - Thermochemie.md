---
title: "Oefensessie 3: Thermochemie"
tags:
  - study-unit
  - oefensessie
  - thermochemie
  - calorimetrie
  - wet-van-hess
course: "Chemie (T1ACH1)"
unit_type: oefensessie
status: todo
completed: false
est_hours: 2.0
priority: high
---

# 🔥 Oefensessie 3: Thermochemie - Calorimetrie & Hess

> [!abstract] Focus van de Sessie
> Toepassing van warmtebalansen in open en geïsoleerde systemen, correcte integratie van de calorimeter-warmtecapaciteit en het berekenen van standaardreactie-enthalpieën via de wet van Hess.

---

## 📌 Oefeningen & Theoretische Verankering

### Oefening 3.1: Kwantitatieve Calorimetrie met $C_{\text{cal}}$ (Examenmodel)
**Vraagstuk**: 
In een constante-druk calorimeter met warmtecapaciteit $C_{\text{cal}} = 297\text{ J/}^\circ\text{C}$ wordt $65.0\text{ mL}$ van $2.00\text{ M }\text{Ba(NO}_3)_2$ gemengd met $50.0\text{ mL}$ van $2.00\text{ M }\text{K}_2\text{SO}_4$. Beide oplossingen hebben $T_{\text{begin}} = 16.35\text{ }^\circ\text{C}$.
$$\text{Ba}^{2+}_{(aq)} + \text{SO}_{4(aq)}^{2-} \longrightarrow \text{BaSO}_{4(s)} \quad \Delta H^\circ_{\text{precipitatie}} = -26.3\text{ kJ/mol}$$
Bereken de eindtemperatuur $T_{\text{eind}}$. (Neem $\rho = 1.00\text{ g/mL}$, $s = 4.184\text{ J/(g}\cdot^\circ\text{C)}$).

> [!success]- Toon Uitwerking & Backlinks
> - **Koppeling met theorie**: [[Chapter 06 - Thermochemie#3.2 Constante-Druk Calorimeter ("Coffee-Cup")]] en [[Exam Preparation#Vraag 3 Thermochemie & Calorimetrie]]
> - **Stoichiometrie**:
>   - $n(\text{Ba}^{2+}) = 0.065\text{ L} \times 2.00\text{ M} = 0.130\text{ mol}$
>   - $n(\text{SO}_4^{2-}) = 0.050\text{ L} \times 2.00\text{ M} = 0.100\text{ mol}$
>   - Limiterend reagens = $\text{SO}_4^{2-}$ ($0.100\text{ mol}$ neerslag gevormd).
> - **Vrijgekomen warmte**:
>   $$q_{\text{rxn}} = 0.100\text{ mol} \times (-26300\text{ J/mol}) = -2630\text{ J}$$
> - **Totale warmtecapaciteit**:
>   - Massa oplossing = $65.0\text{ g} + 50.0\text{ g} = 115.0\text{ g}$
>   - $C_{\text{opl}} = 115.0 \times 4.184 = 481.16\text{ J/}^\circ\text{C}$
>   - $C_{\text{tot}} = C_{\text{opl}} + C_{\text{cal}} = 481.16 + 297 = 778.16\text{ J/}^\circ\text{C}$
> - **Temperatuurstijging**:
>   $$\Delta T = \frac{-q_{\text{rxn}}}{C_{\text{tot}}} = \frac{+2630\text{ J}}{778.16\text{ J/}^\circ\text{C}} = +3.38\text{ }^\circ\text{C}$$
>   $$T_{\text{eind}} = 16.35\text{ }^\circ\text{C} + 3.38\text{ }^\circ\text{C} = \mathbf{19.73\text{ }^\circ\text{C}}$$

---

### Oefening 3.2: Wet van Hess Cyclus
**Vraagstuk**: 
Bereken de standaardreactie-enthalpie voor de synthese van acetyleen:
$$2\text{C}_{(\text{grafiet})} + \text{H}_{2(g)} \longrightarrow \text{C}_2\text{H}_{2(g)}$$
gegeven de volgende verbrandingsenthalpieën:
1. $\text{C}_{(\text{grafiet})} + \text{O}_{2(g)} \rightarrow \text{CO}_{2(g)} \quad \Delta H_1 = -393.5\text{ kJ/mol}$
2. $\text{H}_{2(g)} + \frac{1}{2}\text{O}_{2(g)} \rightarrow \text{H}_2\text{O}_{(l)} \quad \Delta H_2 = -285.8\text{ kJ/mol}$
3. $\text{C}_2\text{H}_{2(g)} + \frac{5}{2}\text{O}_{2(g)} \rightarrow 2\text{CO}_{2(g)} + \text{H}_2\text{O}_{(l)} \quad \Delta H_3 = -1299.6\text{ kJ/mol}$

> [!success]- Toon Uitwerking & Backlinks
> - **Koppeling met theorie**: [[Chapter 06 - Thermochemie#4.1 Wet van Hess]]
> - **Lineaire combinatie**:
>   $$2 \times (\text{Reactie 1}) + 1 \times (\text{Reactie 2}) - 1 \times (\text{Reactie 3})$$
>   $$\Delta H_{\text{rxn}} = 2(-393.5) + (-285.8) - (-1299.6)$$
>   $$\Delta H_{\text{rxn}} = -787.0 - 285.8 + 1299.6 = \mathbf{+226.8\text{ kJ/mol}} \quad (\text{endotherm})$$
