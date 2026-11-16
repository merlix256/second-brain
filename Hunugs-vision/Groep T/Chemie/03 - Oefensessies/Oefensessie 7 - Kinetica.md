---
title: "Oefensessie 7: Chemische Kinetica"
tags:
  - study-unit
  - oefensessie
  - kinetica
  - arrhenius
  - mechanismen
course: "Chemie (T1ACH1)"
unit_type: oefensessie
status: todo
completed: false
est_hours: 2.0
priority: high
---

# ⏱️ Oefensessie 7: Chemische Kinetica - Snelheidswetten & Mechanismen

> [!abstract] Focus van de Sessie
> Integratie van de initiële snelhedenmethode, bepalen van halfwaardetijden en snelheidsconstanten, lineaire Arrhenius-plots en het afleiden van experimentele snelheidswetten uit reactiemechanismen.

---

## 📌 Oefeningen & Theoretische Verankering

### Oefening 7.1: Eerste-Orde Radioactief Verval
**Vraagstuk**: 
Het radioactieve isotoop jodium-131 ($^{131}\text{I}$), gebruikt bij schildkliertherapie, vervalt via een eerste-orde proces met een halfwaardetijd $t_{1/2} = 8.04\text{ dagen}$.
1. Bereken de vervalconstante $k$ in $\text{dag}^{-1}$ en $\text{s}^{-1}$.
2. Hoeveel procent van een initiële dosis blijft over in het lichaam na exact $30.0\text{ dagen}$?

> [!success]- Toon Uitwerking & Backlinks
> - **Koppeling met theorie**: [[Chapter 13 - Kinetica#2.1 Overzicht Geïntegreerde Snelheidswetten]]
> - **1. Berekening van $k$**:
>   $$k = \frac{\ln 2}{t_{1/2}} = \frac{0.69315}{8.04\text{ dagen}} = \mathbf{0.0862\text{ dag}^{-1}}$$
>   $$k = \frac{0.0862}{86400\text{ s/dag}} = \mathbf{9.98 \times 10^{-7}\text{ s}^{-1}}$$
> - **2. Resterend percentage na 30 dagen**:
>   $$\ln\left(\frac{[A]_t}{[A]_0}\right) = -kt = -(0.0862\text{ dag}^{-1})(30.0\text{ dagen}) = -2.586$$
>   $$\frac{[A]_t}{[A]_0} = e^{-2.586} = 0.0753 = \mathbf{7.53\%}$$

---

### Oefening 7.2: Reactiemechanismen en Snelheidsbepalende Stap
**Vraagstuk**: 
Voor de reactie $2\text{NO}_{2(g)} + \text{F}_{2(g)} \rightarrow 2\text{NO}_2\text{F}_{(g)}$ wordt experimenteel vastgesteld dat de snelheidswet $v = k[\text{NO}_2][\text{F}_2]$ is.
Twee mechanismen worden voorgesteld:
- **Mechanisme 1**: 
  Stap 1: $\text{NO}_2 + \text{F}_2 \xrightarrow{k_1} \text{NO}_2\text{F} + \text{F}$ (traag)
  Stap 2: $\text{NO}_2 + \text{F} \xrightarrow{k_2} \text{NO}_2\text{F}$ (snel)
- **Mechanisme 2**:
  Stap 1: $2\text{NO}_2 + \text{F}_2 \xrightarrow{k} 2\text{NO}_2\text{F}$ (één termoleculaire stap)
Motiveer welk mechanisme compatibel is met de kinetische gegevens.

> [!success]- Toon Uitwerking & Backlinks
> - **Koppeling met theorie**: [[Chapter 13 - Kinetica#4. Reactiemechanismen en Katalyse]] en [[Exam Preparation#Vraag 2 Organisch Reactiemechanisme, Kinetica & Hybridisatie]]
> - **Analyse**:
>   - In **Mechanisme 1** is Stap 1 de snelheidsbepalende stap (RDS). Omdat dit een bimoleculaire elementaire stap is, is de theoretische snelheidswet:
>     $$v = k_1 [\text{NO}_2] [\text{F}_2]$$
>     Dit komt exact overeen met de experimentele snelheidswet.
>   - In Mechanisme 2 zou een termoleculaire botsing tussen 3 deeltjes moeten plaatsvinden, wat extreem onwaarschijnlijk is en zou leiden tot $v = k[\text{NO}_2]^2[\text{F}_2]$, wat in strijd is met het experiment.
>   - **Conclusie**: Mechanisme 1 is het correcte mechanisme; atomair fluor ($\text{F}$) fungeert hier als kortlevend reactie-intermediair.
