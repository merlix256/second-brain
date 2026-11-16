---
course: "Computationeel Denken (T1ACD1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.0
priority: medium
tags:
  - study-unit
---

# Sessie 5 - Q&A (Active Recall)

> **Verwijzingen:** [[Sessie 5 - For- en While-lussen]] | [[Oefensessie 5]] | [[Index]]

---

### Vraag 1: Welke waarden genereert `range(12, 2, -3)` en hoeveel iteraties zijn dit?
**Antwoord:**
De startwaarde is $12$, de stopwaarde is $2$ (exclusief), en de stap is $-3$.
De getallen zijn: $12, 9, 6, 3$.
Aantal iteraties: $4$.
Formule:
$$N = \left\lceil \frac{\text{start} - \text{stop}}{|\text{step}|} \right\rceil = \left\lceil \frac{12 - 2}{3} \right\rceil = \left\lceil \frac{10}{3} \right\rceil = 4$$
*Theorielink:* [[Sessie 5 - For- en While-lussen#3.1 De range(start, stop, step) Functie]]

---

### Vraag 2: Wat is het verschil in uitvoering tussen `break` en `continue`?
**Antwoord:**
- `break` breekt de lus **volledig af**; het programma springt direct naar de eerste instructie buiten de lusconstructie.
- `continue` beëindigt enkel de **huidige iteratie**; resterende code in de body van de lus wordt voor die stap overgeslagen en de lus gaat direct verder met de controle van de volgende iteratie.
*Theorielink:* [[Sessie 5 - For- en While-lussen#4. Loop Interrupties: break en continue]]

---

### Vraag 3: Waarom heeft een geneste lus van de vorm `for i in range(n): for j in range(i):` een tijdscomplexiteit van $\mathcal{O}(n^2)$?
**Antwoord:**
Voor elke $i$ van $0$ tot $n-1$ loopt de binnenste lus $i$ keer. Het totale aantal uitgevoerde bewerkingen is de rekenkundige som:
$$\sum_{i=0}^{n-1} i = \frac{(n-1) \cdot n}{2} = \frac{1}{2}n^2 - \frac{1}{2}n$$
Voor grote $n$ domineert de term $n^2$, waardoor de asymptotische complexiteit gelijk is aan $\mathcal{O}(n^2)$.
*Theorielink:* [[Sessie 5 - For- en While-lussen#5.1 Wiskundige Complexiteitsanalyse]]