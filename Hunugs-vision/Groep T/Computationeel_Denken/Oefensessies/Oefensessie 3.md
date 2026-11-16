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
# Oefensessie 3: Functies 1 - Definitie & Parameters

> **Navigatie:** [[Index]] | [[Exercise Session Tracker]] | [[Sessie 3 - Functies 1 - Definitie, Aanroep en Parameters]] | [[Sessie 3 - Q&A]]

---

## 🎯 Doelstellingen
- Problemen modulair opdelen in functies (`def`).
- Onderscheid hanteren tussen formele parameters en actuele argumenten.
- Beheersen van default parameters en lokale variabelenscope.

---

## 🛠️ Praktijkopgaven

### Opgave 3.1: Valversnelling op Hemellichamen
**Probleemstelling:**
Definieer een functie `bereken_gewicht(massa, gravitatie=9.81)` die de zwaartekracht $F_z = m \cdot g$ berekent. Roep de functie positioneel aan voor de aarde ($g = 9.81$ via de defaultwaarde) en via keyword parameters voor de maan ($g = 1.62$).

- **Vereiste Theoretische Concepten:**
  - Functiedefinitie en syntaxis: [[Sessie 3 - Functies 1 - Definitie, Aanroep en Parameters#2. Syntaxis: Definitie en Aanroep]]
  - Default parameters: [[Sessie 3 - Functies 1 - Definitie, Aanroep en Parameters#3.2 Default Parameters]]
  - Positionele vs Keyword argumenten: [[Sessie 3 - Functies 1 - Definitie, Aanroep en Parameters#3.1 Positionele vs. Keyword Argumenten]]

---

### Opgave 3.2: Scope Experiment en Shadowing
**Probleemstelling:**
Gegeven onderstaande code. Voorspel zonder Python uit te voeren de exacte console-output en verklaar waarom variabele `x` op globaal niveau niet overschreven wordt door de lokale functie-executie.

```python
x = 50

def transformeer(x):
    x = x * 2
    print(f"Binnen functie: {x}")

transformeer(x)
print(f"Buiten functie: {x}")
```

- **Vereiste Theoretische Concepten:**
  - Lokale variabelen en stack frames: [[Sessie 3 - Functies 1 - Definitie, Aanroep en Parameters#4. Variabelenscope en de Call Stack]]
  - LEGB-scoperegels: [[Sessie 3 - Functies 1 - Definitie, Aanroep en Parameters#4.1 LEGB-Regel voor Scope Resolutie]]