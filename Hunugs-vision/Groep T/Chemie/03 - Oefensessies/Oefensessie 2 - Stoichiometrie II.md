---
title: "Oefensessie 2: Stoichiometrie II"
tags:
  - study-unit
  - oefensessie
  - redox
  - gaswetten
course: "Chemie (T1ACH1)"
unit_type: oefensessie
status: todo
completed: false
est_hours: 2.0
priority: high
---

# 💨 Oefensessie 2: Stoichiometrie II - Complexe Redox & Ideale Gassen

> [!abstract] Focus van de Sessie
> Balanceren van geavanceerde redoxvergelijkingen via de ion-elektronmethode (deelreacties in zuur en basisch milieu) en stoichiometrische berekeningen gekoppeld aan de algemene gaswet ($PV = nRT$).

---

## 📌 Oefeningen & Theoretische Verankering

### Oefening 2.1: Redox Balanceren via Ion-Elektronmethode in Zuur Milieu
**Vraagstuk**: 
Balanceer de volgende redoxreactie in **zuur milieu**:
$$\text{MnO}_4^- + \text{C}_2\text{O}_4^{2-} \longrightarrow \text{Mn}^{2+} + \text{CO}_2$$

> [!success]- Toon Uitwerking & Backlinks
> - **Koppeling met theorie**: [[Chapter 08 - Periodieke tabel#1. Effectieve Kernlading (Zeff)]] en [[Chapter 09 - Chemische binding I#2.2 Formele Lading (FL)]]
> - **Reductie deelreactie**:
>   1. Atomen: $\text{MnO}_4^- \rightarrow \text{Mn}^{2+}$
>   2. Zuurstof compenseren met water: $\text{MnO}_4^- \rightarrow \text{Mn}^{2+} + 4\text{H}_2\text{O}$
>   3. Waterstof compenseren met protonen: $\text{MnO}_4^- + 8\text{H}^+ \rightarrow \text{Mn}^{2+} + 4\text{H}_2\text{O}$
>   4. Lading compenseren met elektronen:
>      $$\text{MnO}_4^- + 8\text{H}^+ + 5e^- \longrightarrow \text{Mn}^{2+} + 4\text{H}_2\text{O} \quad (\times 2)$$
> - **Oxidatie deelreactie**:
>   1. Atomen: $\text{C}_2\text{O}_4^{2-} \rightarrow 2\text{CO}_2$
>   2. Lading compenseren:
>      $$\text{C}_2\text{O}_4^{2-} \longrightarrow 2\text{CO}_2 + 2e^- \quad (\times 5)$$
> - **Totale gebalanceerde vergelijking**:
>   $$\mathbf{2\text{MnO}_4^- + 5\text{C}_2\text{O}_4^{2-} + 16\text{H}^+ \longrightarrow 2\text{Mn}^{2+} + 10\text{CO}_2 + 8\text{H}_2\text{O}}$$

---

### Oefening 2.2: Gasstoichiometrie ($PV = nRT$)
**Vraagstuk**: 
Een monster van $3.25\text{ g }\text{KClO}_3$ wordt thermisch ontleed:
$$2\text{KClO}_{3(s)} \longrightarrow 2\text{KCl}_{(s)} + 3\text{O}_{2(g)}$$
Het gevormde $\text{O}_2$-gas wordt opgevangen over water bij $22.0\text{ }^\circ\text{C}$ en een totale atmosferische druk van $752\text{ mmHg}$. De evenwichtsdampdruk van water bij $22.0\text{ }^\circ\text{C}$ bedraagt $19.8\text{ mmHg}$. Bereken het volume opgevangen gas in liters.

> [!success]- Toon Uitwerking & Backlinks
> - **Koppeling met theorie**: [[Chapter 11 - Intermoleculaire krachten#3.1 Dynamisch Dampdrukevenwicht]] en [[Chapter 12 - Oplossingen#1.2 Invloed van Temperatuur en Druk op Oplosbaarheid]]
> - **Partiële druk van droog zuurstofgas (Wet van Dalton)**:
>   $$P_{\text{O}_2} = P_{\text{tot}} - P_{\text{H}_2\text{O}} = 752 - 19.8 = 732.2\text{ mmHg} = \frac{732.2}{760} = 0.9634\text{ atm}$$
> - **Mollen $\text{O}_2$**:
>   - $n(\text{KClO}_3) = \frac{3.25\text{ g}}{122.55\text{ g/mol}} = 0.02652\text{ mol}$
>   - $n(\text{O}_2) = \frac{3}{2} \times 0.02652 = 0.03978\text{ mol}$
> - **Ideale gaswet**:
>   $$V = \frac{nRT}{P} = \frac{(0.03978\text{ mol})(0.08206\text{ L}\cdot\text{atm}/(\text{mol}\cdot\text{K}))(295.15\text{ K})}{0.9634\text{ atm}} = \mathbf{1.00\text{ L}}$$
