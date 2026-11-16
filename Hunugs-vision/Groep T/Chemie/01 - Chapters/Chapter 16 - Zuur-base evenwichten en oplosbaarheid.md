---
title: "Hoofdstuk 16: Zuur-Base Evenwichten en Oplosbaarheidsproduct"
tags:
  - study-unit
  - chemie
  - buffers
  - titraties
  - oplosbaarheid
  - Ksp
course: "Chemie (T1ACH1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: high
---

# 🛡️ Hoofdstuk 16: Bufferoplossingen, Titraties en Oplosbaarheidsproduct

> [!abstract] Kernconcept
> Dit hoofdstuk integreert geavanceerde waterige evenwichten: hoe **bufferoplossingen** plotse pH-veranderingen weerstaan, hoe **titratiecurves** kwantitatief verlopen en hoe het **oplosbaarheidsproduct ($K_{sp}$)** neerslagvorming voorspelt.

---

## 1. Het Gemeenschappelijk-Ion Effect en Buffers

### 1.1 Gemeenschappelijk-Ion Effect
Volgens Le Châtelier verschuift de ionisatie van een zwak elektrolyt naar links bij toevoeging van een zout dat een gemeenschappelijk ion deelt.

### 1.2 Bufferoplossingen
Een **buffer** is een oplossing die pH-veranderingen minimaliseert bij toevoeging van kleine hoeveelheden sterk zuur of sterke base.
- **Samenstelling**: Bestaat uit een zwak zuur en zijn geconjugeerde base (bijv. $\text{CH}_3\text{COOH} / \text{CH}_3\text{COO}^-$) óf een zwakke base en zijn geconjugeerd zuur (bijv. $\text{NH}_3 / \text{NH}_4^+$).

### 1.3 De Henderson-Hasselbalch Vergelijking
Voor een buffermengsel:
$$\text{pH} = \text{p}K_a + \log\left( \frac{[\text{Base}]}{[\text{Zuur}]} \right) = \text{p}K_a + \log\left( \frac{n_{\text{base}}}{n_{\text{zuur}}} \right)$$
- **Optimale buffercapaciteit**: Wordt bereikt wanneer $[\text{Base}] = [\text{Zuur}]$, waardoor $\text{pH} = \text{p}K_a$.
- **Werkzaam buffergebied**: $\text{pH} = \text{p}K_a \pm 1$.

---

## 2. Zuur-Base Titraties

![[Titration_Curves_Comparison.png]]

### 2.1 Titratie van Sterk Zuur met Sterke Base
- Vóór het equivalentiepunt: $\text{pH}$ bepaald door overmaat sterk zuur.
- **Equivalentiepunt (EP)**: $\text{pH} = 7.00$ (enkel neutraal zout en water aanwezig).
- Na het EP: $\text{pH}$ bepaald door overmaat sterke base.

### 2.2 Titratie van Zwak Zuur met Sterke Base
1. **Beginpunt ($V_b = 0$)**: Zwak zuurevenwicht ($[\text{H}_3\text{O}^+] \approx \sqrt{K_a c_a}$).
2. **Buffergebied (halverwege EP)**: $n_{\text{zuur}} = n_{\text{geconj. base}} \implies \mathbf{\text{pH} = \text{p}K_a}$.
3. **Equivalentiepunt (EP)**: Alle zwak zuur is omgezet in de geconjugeerde base $\text{A}^-$. Door anionhydrolyse is **$\text{pH} > 7.00$**!
   $$[\text{OH}^-] = \sqrt{K_b \cdot [\text{A}^-]_{EP}}$$
4. **Na het EP**: Overmaat sterke base domineert de pH.

---

## 3. Oplosbaarheidsproduct ($K_{sp}$)

Voor een slecht oplosbaar zout $M_m X_n$:
$$M_m X_{n(s)} \rightleftharpoons m M^{n+}_{(aq)} + n X^{m-}_{(aq)}$$
Het **oplosbaarheidsproduct ($K_{sp}$)** is de evenwichtsconstante van dit heterogene evenwicht:
$$K_{sp} = [M^{n+}]^m \cdot [X^{m-}]^n$$

### 3.1 Molaire Oplosbaarheid ($s$)
De molaire oplosbaarheid $s$ is de hoeveelheid mol zout die maximaal oplost in $1\text{ liter}$ water:
- Voor $1:1$ zout (bijv. $\text{AgCl}$): $K_{sp} = s^2 \implies s = \sqrt{K_{sp}}$
- Voor $1:2$ zout (bijv. $\text{PbCl}_2, \text{Mg(OH)}_2$): $K_{sp} = s \cdot (2s)^2 = 4s^3 \implies s = \sqrt[3]{\frac{K_{sp}}{4}}$
- Voor $1:3$ zout (bijv. $\text{Al(OH)}_3$): $K_{sp} = 27s^4 \implies s = \sqrt[4]{\frac{K_{sp}}{27}}$

### 3.2 Neerslagvoorspelling via het Ionenproduct ($Q_{sp}$)
- $Q_{sp} < K_{sp}$: Onverzadigde oplossing, geen neerslag.
- $Q_{sp} = K_{sp}$: Verzadigde oplossing in dynamisch evenwicht.
- $Q_{sp} > K_{sp}$: Oververzadigde oplossing $\implies$ **neerslag treedt op** totdat $Q_{sp} = K_{sp}$.

---

## 📝 Samenvatting
1. Buffers bestaan uit een geconjugeerd zwak zuur-base paar en volgen Henderson-Hasselbalch: $\text{pH} = \text{p}K_a + \log([B]/[Z])$.
2. Bij halverwege titratie van een zwak zuur geldt $\text{pH} = \text{p}K_a$; bij het equivalentiepunt is $\text{pH} > 7$.
3. $K_{sp}$ beheerst verzadiging; neerslag treedt op zodra het ionenproduct $Q_{sp} > K_{sp}$.
