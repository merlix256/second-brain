---
title: "Active Recall: Hoofdstuk 13 - Chemische Kinetica"
tags:
  - study-unit
  - active-recall
  - flashcards
  - kinetica
  - reactie-orde
course: "Chemie (T1ACH1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.0
priority: medium
---

# 🧠 Active Recall Deck: Hoofdstuk 13 - Chemische Kinetica

---

### Vraag 1: Bepaling van Snelheidswet en Orde
**Vraag**: Voor de reactie $2A + B \rightarrow C$ zijn de volgende initiële snelheden gemeten:
- Exp 1: $[A]_0 = 0.10\text{ M}$, $[B]_0 = 0.10\text{ M} \implies v_0 = 1.2 \times 10^{-3}\text{ M/s}$
- Exp 2: $[A]_0 = 0.10\text{ M}$, $[B]_0 = 0.20\text{ M} \implies v_0 = 2.4 \times 10^{-3}\text{ M/s}$
- Exp 3: $[A]_0 = 0.20\text{ M}$, $[B]_0 = 0.10\text{ M} \implies v_0 = 4.8 \times 10^{-3}\text{ M/s}$
Bepaal de differentiële snelheidswet, de individuele en totale orde, en bereken de snelheidsconstante $k$ inclusief correcte eenheden.

> [!success]- Toon Antwoord & Uitwerking
> - **Theoretische koppeling**: [[Chapter 13 - Kinetica#2. Snelheidswetten en Reactie-orde]]
> - **Uitwerking**:
>   - **Orde in B**: Vergelijk Exp 1 en Exp 2 ($[A]$ constant): $[B]$ verdubbelt ($2\times$), $v_0$ verdubbelt ($2\times$) $\implies 2^n = 2 \implies \mathbf{n = 1}$ (eerste orde in B).
>   - **Orde in A**: Vergelijk Exp 1 en Exp 3 ($[B]$ constant): $[A]$ verdubbelt ($2\times$), $v_0$ verviervoudigt ($4\times$) $\implies 2^m = 4 \implies \mathbf{m = 2}$ (tweede orde in A).
>   - **Snelheidswet**: $v = k [A]^2 [B]^1$ (totale orde = $2 + 1 = 3$).
>   - **Constante $k$**:
>     $$k = \frac{v_0}{[A]_0^2 [B]_0} = \frac{1.2 \times 10^{-3}\text{ M/s}}{(0.10\text{ M})^2(0.10\text{ M})} = \mathbf{1.2\text{ L}^2/(\text{mol}^2\cdot\text{s})}$$

---

### Vraag 2: Activeringsenergie via Arrhenius
**Vraag**: De snelheidsconstante van een reactie verdrievoudigt wanneer de temperatuur verhoogd wordt van $20.0\text{ }^\circ\text{C}$ naar $40.0\text{ }^\circ\text{C}$. Bereken de activeringsenergie $E_a$ van deze reactie. ($R = 8.314\text{ J/(mol}\cdot\text{K)}$).

> [!success]- Toon Antwoord & Uitwerking
> - **Theoretische koppeling**: [[Chapter 13 - Kinetica#3.2 De Arrheniusvergelijking]]
> - **Gegevens**:
>   - $T_1 = 20.0 + 273.15 = 293.15\text{ K}$, $T_2 = 40.0 + 273.15 = 313.15\text{ K}$
>   - $\frac{k_2}{k_1} = 3.00$
> - **Arrhenius tweepuntsformule**:
>   $$\ln\left(\frac{k_2}{k_1}\right) = -\frac{E_a}{R} \left( \frac{1}{T_2} - \frac{1}{T_1} \right)$$
>   $$\ln(3.00) = 1.0986$$
>   $$\frac{1}{T_2} - \frac{1}{T_1} = \frac{1}{313.15} - \frac{1}{293.15} = -2.1767 \times 10^{-4}\text{ K}^{-1}$$
>   $$E_a = - \frac{R \cdot \ln(k_2/k_1)}{\frac{1}{T_2} - \frac{1}{T_1}} = - \frac{(8.314)(1.0986)}{-2.1767 \times 10^{-4}} = 41965\text{ J/mol} = \mathbf{42.0\text{ kJ/mol}}$$
