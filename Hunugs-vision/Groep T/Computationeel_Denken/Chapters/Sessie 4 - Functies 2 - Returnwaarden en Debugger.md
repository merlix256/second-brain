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

# Sessie 4: Functies 2 - Returnwaarden en Debugger

> **Navigatie:** [[Index]] | [[Exercise Session Tracker]] | [[Sessie 4 - Q&A]] | [[Oefensessie 4]]

---

## 1. Returnwaarden vs. `print()`
Een van de meest voorkomende conceptuele valkuilen bij beginnende programmeurs is het verwarren van console-uitvoer (`print`) met functionele data-uitwisseling (`return`).

| Eigenschap | `print()` | `return` |
| :--- | :--- | :--- |
| **Rol** | Toont tekst in de terminal voor de menselijke gebruiker | Geeft data terug aan het aanroepende programma |
| **Datahergebruik** | Onmogelijk (resultaat verdwijnt op het scherm) | Mogelijk (kan opgeslagen worden in een variabele) |
| **Stroomcontrole** | Gaat gewoon verder met de volgende regel | Beëindigt de uitvoering van de functie onmiddellijk |
| **Retourwaarde** | `None` | De geëvalueerde expressie |

```python
# FOUTIEF:
def tel_op_verkeerd(a, b):
    print(a + b)

res = tel_op_verkeerd(3, 4)
# res bevat nu None! Verdere berekeningen falen.

# CORRECT:
def tel_op_correct(a, b):
    return a + b

res = tel_op_correct(3, 4)  # res is 7
```

### 1.1 Meervoudige Returnwaarden
Python kan meerdere waarden retourneren als een `tuple`:
```python
def deel_met_rest(deeltal, deler):
    quotient = deeltal // deler
    rest = deeltal % deler
    return quotient, rest  # Tuple packing

q, r = deel_met_rest(17, 5) # Unpacking: q = 3, r = 2
```

---

## 2. Pre- en Postcondities & Defensief Programmeren
In software engineering beschrijft een functie een wiskundig contract:

- **Preconditie**: Voorwaarden waaraan de invoerparameters moeten voldoen voor een correcte werking.
- **Postconditie**: De garantie die de functie levert over het geretourneerde resultaat, mits aan de precondities is voldaan.

```python
def bereken_wortel(x: float) -> float:
    """
    Preconditie: x >= 0.0
    Postconditie: retourneert y zodanig dat y * y == x
    """
    assert x >= 0.0, "Preconditie gefaald: x mag niet negatief zijn!"
    return x ** 0.5
```

---

## 3. Foutopsporing: De Debugger
Wanneer code crasht of onverwachte resultaten produceert (semantische fouten), is een interactieve debugger essentieel.

![[Slide_Sessie4_Debugger_Interface.png]]
*Figuur 1: Debugger tools in moderne IDE's (Breakpoints, Variable Watches en Call Stack).*

### 3.1 Belangrijkste Debugger Acties
- **Breakpoint**: Een breekpunt in de code waar de interpreter de executie pauzeert.
- **Step Over (F8)**: Voert de huidige regel uit zonder functies binnen te gaan.
- **Step Into (F7)**: Duikt in de aangeroepen functie op de huidige regel.
- **Step Out**: Voert de rest van de huidige functie uit en pauzeert bij terugkeer naar de caller.
- **Watch / Variables View**: Inspecteert live de waarden in de actieve scope op de stack.

---

## 📝 Samenvatting
`return` stuurt data terug naar het programma en beëindigt de functie, terwijl `print` enkel tekst op het scherm projecteert. Functies hanteren formele pre- en postcondities. De interactieve debugger laat toe om stap voor stap door code te lopen en variabelen in het stack frame te inspecteren om bugs systematisch te isoleren.