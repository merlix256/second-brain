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

# Sessie 2 - Q&A (Active Recall)

> **Verwijzingen:** [[Sessie 2 - Variabelen en Branching Controlestructuren]] | [[Oefensessie 2]] | [[Index]]

---

### Vraag 1: Wat is het verschil in resultaat en datatype tussen `/` en `//` in Python?
**Antwoord:**
- `/` is de reële deling. Deze operator retourneert **altijd** een `float`, zelfs als de deling exact opgaat (bijv. `8 / 4` levert `2.0` op).
- `//` is de gehele deling (floor division). Deze operator rondt het quotiënt af naar beneden op het dichtstbijzijnde gehele getal: $\lfloor \frac{a}{b} \rfloor$. Indien beide operanden integers zijn, is het resultaat een `int` (bijv. `7 // 2` levert `3` op; let op: `-7 // 2` levert `-4` op!).
*Theorielink:* [[Sessie 2 - Variabelen en Branching Controlestructuren#1.2 Rekenkundige Operatoren]]

---

### Vraag 2: Hoe werkt 'Short-Circuit Evaluatie' en waarom voorkomt dit runtime crashes bij samengestelde condities?
**Antwoord:**
Short-circuit evaluatie betekent dat Python stopt met het evalueren van een booleaanse expressie zodra de uiteindelijke uitkomst onherroepelijk vaststaat:
- Bij `A and B`: als `A` `False` is, wordt `B` nooit bekeken.
- Bij `A or B`: als `A` `True` is, wordt `B` nooit bekeken.

Dit voorkomt fouten zoals `ZeroDivisionError` of `IndexError` door de beschermende conditie eerst te plaatsen:
```python
if noemer != 0 and teller / noemer > 1:
    print("Geldig")
```
Als `noemer == 0`, zorgt de eerste conditie dat `teller / noemer` nooit uitgevoerd wordt.
*Theorielink:* [[Sessie 2 - Variabelen en Branching Controlestructuren#3.1 Short-Circuit Evaluatie]]

---

### Vraag 3: Hoe luiden de Wetten van De Morgan en hoe vereenvoudig je `not (x > 0 and y == 5)`?
**Antwoord:**
De wetten luiden:
1. $\neg (P \land Q) \iff (\neg P) \lor (\neg Q)$
2. $\neg (P \lor Q) \iff (\neg P) \land (\neg Q)$

Vereenvoudiging van `not (x > 0 and y == 5)`:
- Negatie van `x > 0` is `x <= 0`
- `and` wordt `or`
- Negatie van `y == 5` is `y != 5`
Resultaat: `(x <= 0) or (y != 5)`.
*Theorielink:* [[Sessie 2 - Variabelen en Branching Controlestructuren#2.2 Logische Connectieven & Waarheidstabellen]]