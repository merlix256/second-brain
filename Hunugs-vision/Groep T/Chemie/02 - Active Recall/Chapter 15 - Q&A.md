---
title: "Active Recall: Hoofdstuk 15 - Zuren en Basen"
tags:
  - study-unit
  - active-recall
  - flashcards
  - zuren
  - basen
  - pH
course: "Chemie (T1ACH1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.0
priority: medium
---

# 🧠 Active Recall Deck: Hoofdstuk 15 - Zuren en Basen

---

### Vraag 1: pH van een Zwak Zuur en Validatie van de Benadering
**Vraag**: Bereken de pH en de ionisatiegraad $\alpha$ van een $0.150\text{ M}$ oplossing van azijnzuur ($\text{CH}_3\text{COOH}$). ($K_a = 1.8 \times 10^{-5}$). Is de $5\%$-benadering hier gerechtvaardigd?

> [!success]- Toon Antwoord & Uitwerking
> - **Theoretische koppeling**: [[Chapter 15 - Zuren en basen#2.2 Zwakke Zuren en Zuurconstante (Ka)]]
> - **Evenwichtsvergelijking**:
>   $$\text{CH}_3\text{COOH} + \text{H}_2\text{O} \rightleftharpoons \text{CH}_3\text{COO}^- + \text{H}_3\text{O}^+$$
>   $$K_a = \frac{x^2}{c_a - x} \approx \frac{x^2}{c_a}$$
>   $$x = [\text{H}_3\text{O}^+] = \sqrt{K_a \cdot c_a} = \sqrt{(1.8 \times 10^{-5})(0.150)} = 1.643 \times 10^{-3}\text{ M}$$
> - **Validatie van de $5\%$-regel**:
>   $$\alpha = \frac{1.643 \times 10^{-3}}{0.150} \times 100\% = \mathbf{1.10\%} < 5\% \implies \text{benadering is volledig gerechtvaardigd!}$$
> - **pH berekening**:
>   $$\text{pH} = -\log(1.643 \times 10^{-3}) = \mathbf{2.78}$$

---

### Vraag 2: Hydrolyse en pH van een Zoutoplossing
**Vraag**: Bereken de pH van een $0.200\text{ M}$ oplossing van natriumformiaat ($\text{HCOONa}$). Voor mierenzuur geldt $K_a = 1.8 \times 10^{-4}$. ($K_w = 1.0 \times 10^{-14}$).

> [!success]- Toon Antwoord & Uitwerking
> - **Theoretische koppeling**: [[Chapter 15 - Zuren en basen#3. Zoutoplossingen en Hydrolyse]]
> - **Mechanisme**:
>   $\text{HCOONa}$ splitst volledig in $\text{Na}^+$ (inert kation) en $\text{HCOO}^-$ (zwak basisch anion).
>   $$\text{HCOO}^- + \text{H}_2\text{O} \rightleftharpoons \text{HCOOH} + \text{OH}^-$$
> - **$K_b$ van de geconjugeerde base**:
>   $$K_b = \frac{K_w}{K_a} = \frac{1.0 \times 10^{-14}}{1.8 \times 10^{-4}} = 5.56 \times 10^{-11}$$
> - **Berekening van $[\text{OH}^-]$**:
>   $$[\text{OH}^-] = \sqrt{K_b \cdot c_b} = \sqrt{(5.56 \times 10^{-11})(0.200)} = 3.33 \times 10^{-6}\text{ M}$$
>   $$\text{pOH} = -\log(3.33 \times 10^{-6}) = 5.48$$
>   $$\text{pH} = 14.00 - 5.48 = \mathbf{8.52} \quad (\text{basisch zout})$$
