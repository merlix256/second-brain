---
course: "Computationeel Denken (T1ACD1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: medium
tags:
  - study-unit
---

# Sessie 5: For- en While-lussen

> **Navigatie:** [[Index]] | [[Exercise Session Tracker]] | [[Sessie 5 - Q&A]] | [[Oefensessie 5]]

---

## 1. Iteratieve Controlestructuren
Iteratie stelt een computer in staat om repetitieve instructies razendsnel en zonder afwijking uit te voeren. We onderscheiden twee hoofdvormen:
1. **Conditie-gestuurde herhaling (`while`)**: Herhaalt zolang een booleaanse conditie `True` is.
2. **Collectie- of teller-gestuurde herhaling (`for`)**: Itereert over een discrete verzameling of getallenreeks.

---

## 2. De `while`-lus
Syntaxis:
```python
while conditie:
    # instructies
    # mutatie van loop-variabele (cruciaal!)
```

### 2.1 Het risico op oneindige lussen (Infinite Loops)
Als de conditie nooit naar `False` evalueert, raakt het programma geblokkeerd:
```python
i = 1
while i <= 5:
    print(i)
    i += 1  # Zonder deze stap ontstaat een oneindige lus!
```

---

## 3. De `for`-lus en de `range()`-functie
De `for`-lus in Python is een iterator-gestuurde constructie:

```python
for element in collectie:
    doe_iets(element)
```

### 3.1 De `range(start, stop, step)` Functie
Genereert een rekenkundige reeks getallen:
$$\text{Reeks: } [\text{start}, \text{start} + \text{step}, \dots] \quad \text{tot } < \text{stop}$$

- `range(5)`: $0, 1, 2, 3, 4$
- `range(2, 8)`: $2, 3, 4, 5, 6, 7$
- `range(10, 0, -2)`: $10, 8, 6, 4, 2$ (dalende reeks)

> [!NOTE] Aantal elementen in `range(start, stop, step)`
> Voor positieve stapgrootte $\text{step} > 0$:
> $$N = \max\left(0, \left\lceil \frac{\text{stop} - \text{start}}{\text{step}} \right\rceil\right)$$

---

## 4. Loop Interrupties: `break` en `continue`
- **`break`**: Beëindigt de huidige lus onmiddellijk en springt naar de code na de lus.
- **`continue`**: Slaat de resterende instructies van de huidige iteratie over en springt direct naar de volgende iteratiestap.

```python
for n in range(1, 10):
    if n % 2 == 0:
        continue  # Sla even getallen over
    if n > 7:
        break     # Stop zodra n groter is dan 7
    print(n)      # Uitvoer: 1, 3, 5, 7
```

---

## 5. Geneste Lussen & Algoritmische Complexiteit
Wanneer een lus binnen een andere lus wordt geplaatst, spreken we van geneste lussen.

```python
rows = 3
cols = 4
for r in range(rows):
    for c in range(cols):
        print(f"({r},{c})", end=" ")
    print()
```

### 5.1 Wiskundige Complexiteitsanalyse
Als de buitenste lus $n$ keer loopt en de binnenste lus $m$ keer:
$$\text{Totale operaties} = \sum_{i=1}^{n} m = n \times m \implies \mathcal{O}(n \times m)$$
Bij een driehoekige geneste lus:
$$\sum_{i=1}^{n} i = \frac{n(n + 1)}{2} = \frac{n^2 + n}{2} \implies \mathcal{O}(n^2)$$

---

## 📝 Samenvatting
`while`-lussen herhalen op basis van een dynamische conditie (met risico op oneindige lussen), terwijl `for`-lussen met `range()` een vooraf gekend domein doorlopen. Met `break` en `continue` kan de controleflow gemanipuleerd worden. Geneste lussen vermenigvuldigen het aantal bewerkingen en verhogen de tijdscomplexiteit tot kwadratische ordes $\mathcal{O}(n^2)$.