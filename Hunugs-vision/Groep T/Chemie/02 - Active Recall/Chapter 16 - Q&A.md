---
title: "Active Recall: Hoofdstuk 16 - Buffers en Oplosbaarheidsproduct"
tags:
  - study-unit
  - active-recall
  - flashcards
  - buffers
  - Ksp
course: "Chemie (T1ACH1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.0
priority: medium
---

# 🧠 Active Recall Deck: Hoofdstuk 16 - Buffers en Oplosbaarheidsproduct

---

### Vraag 1: Bufferwerking en pH-verschuiving
**Vraag**: Een bufferoplossing bevat $0.300\text{ mol }\text{CH}_3\text{COOH}$ en $0.300\text{ mol }\text{CH}_3\text{COONa}$ in $1.00\text{ L}$ water ($K_a = 1.8 \times 10^{-5}, \text{p}K_a = 4.74$).
1. Bereken de initiële pH van de buffer.
2. Bereken de nieuwe pH na toevoeging van $0.050\text{ mol}$ gasvormig $\text{HCl}$ (zonder volume-effect).

> [!success]- Toon Antwoord & Uitwerking
> - **Theoretische koppeling**: [[Chapter 16 - Zuur-base evenwichten en oplosbaarheid#1.3 De Henderson-Hasselbalch Vergelijking]]
> - **1. Initiële pH**:
>   $$\text{pH} = \text{p}K_a + \log\left(\frac{0.300}{0.300}\right) = \text{p}K_a + 0 = \mathbf{4.74}$$
> - **2. Na toevoeging van sterk zuur $\text{H}^+$**:
>   De geconjugeerde base neutraliseert het sterke zuur kwantitatief:
>   $$\text{CH}_3\text{COO}^- + \text{H}^+ \longrightarrow \text{CH}_3\text{COOH}$$
>   - $n(\text{base})_{\text{nieuw}} = 0.300 - 0.050 = 0.250\text{ mol}$
>   - $n(\text{zuur})_{\text{nieuw}} = 0.300 + 0.050 = 0.350\text{ mol}$
>   $$\text{pH} = 4.74 + \log\left(\frac{0.250}{0.350}\right) = 4.74 + \log(0.7143) = 4.74 - 0.15 = \mathbf{4.59}$$
>   *(De pH daalt met slechts 0.15 eenheden dankzij de bufferwerking!)*

---

### Vraag 2: Neerslagvorming met Gemeenschappelijk Ion
**Vraag**: Het oplosbaarheidsproduct van lood(II)jodide bedraagt $K_{sp}(\text{PbI}_2) = 1.4 \times 10^{-8}$. 
1. Bereken de molaire oplosbaarheid van $\text{PbI}_2$ in zuiver water.
2. Bereken de molaire oplosbaarheid van $\text{PbI}_2$ in een $0.10\text{ M }\text{KI}$ oplossing (gemeenschappelijk-ion effect).

> [!success]- Toon Antwoord & Uitwerking
> - **Theoretische koppeling**: [[Chapter 16 - Zuur-base evenwichten en oplosbaarheid#3. Oplosbaarheidsproduct (Ksp)]]
> - **1. In zuiver water**:
>   $$\text{PbI}_{2(s)} \rightleftharpoons \text{Pb}^{2+} + 2\text{I}^- \implies K_{sp} = s(2s)^2 = 4s^3$$
>   $$s = \sqrt[3]{\frac{1.4 \times 10^{-8}}{4}} = \mathbf{1.52 \times 10^{-3}\text{ mol/L}}$$
> - **2. In $0.10\text{ M KI}$**:
>   $[\text{I}^-] \approx 0.10\text{ M}$ (gedomineerd door het volledig opgeloste zout $\text{KI}$).
>   $$K_{sp} = [\text{Pb}^{2+}][\text{I}^-]^2 = s' \cdot (0.10)^2$$
>   $$s' = \frac{1.4 \times 10^{-8}}{0.010} = \mathbf{1.40 \times 10^{-6}\text{ mol/L}}$$
>   *(De oplosbaarheid daalt meer dan duizendvoudig door het gemeenschappelijk ion!)*
