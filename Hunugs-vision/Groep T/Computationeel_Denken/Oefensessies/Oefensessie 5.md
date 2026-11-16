---
course: "Computationeel Denken (T1ACD1)"
unit_type: oefensessie
status: done
completed: true
est_hours: 2.0
priority: high
tags:
  - study-unit
---
# Oefensessie 5: Lussen (For & While)

> **Navigatie:** [[Index]] | [[Exercise Session Tracker]] | [[Sessie 5 - For- en While-lussen]] | [[Sessie 5 - Q&A]]

---

## 🎯 Doelstellingen
- Kiezen tussen `while` (onbekend aantal stappen) en `for` (vooraf gekende iteraties).
- Werken met `range()` en loop-modificaties (`break`, `continue`).
- Implementeren van geneste lussen voor tweedimensionale patronen.

---

## 🛠️ Praktijkopgaven

### Opgave 5.1: Benadering van $\pi$ via de Leibniz-reeks
**Probleemstelling:**
De constante $\pi$ kan benaderd worden via de oneindige alternerende reeks van Leibniz:
$$\frac{\pi}{4} = \sum_{k=0}^{n} \frac{(-1)^k}{2k + 1} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \dots$$
Schrijf een functie `benader_pi(n_termen)` die met behulp van een `for`-lus de som over de eerste $n$ termen berekent en vermenigvuldigt met 4.

- **Vereiste Theoretische Concepten:**
  - For-lus met teller: [[Sessie 5 - For- en While-lussen#3. De for-lus en de range()-functie]]
  - Rekenkundige sommatie en accumulatie: [[Sessie 5 - For- en While-lussen#5.1 Wiskundige Complexiteitsanalyse]]

---

### Opgave 5.2: Het Collatz-vermoeden (While-lus)
**Probleemstelling:**
Start met een willekeurige integer $n > 0$.
- Is $n$ even: $n_{k+1} = n_k / 2$
- Is $n$ oneven: $n_{k+1} = 3 n_k + 1$
Herhaal dit proces tot $n = 1$. Schrijf een functie `collatz_lengte(n)` die met een `while`-lus het aantal stappen telt tot $1$ bereikt is.

- **Vereiste Theoretische Concepten:**
  - While-condities en vermijden van oneindige lussen: [[Sessie 5 - For- en While-lussen#2. De while-lus]]
  - Modulo-operator voor pariteitscontrole: [[Sessie 2 - Variabelen en Branching Controlestructuren#1.2 Rekenkundige Operatoren]]