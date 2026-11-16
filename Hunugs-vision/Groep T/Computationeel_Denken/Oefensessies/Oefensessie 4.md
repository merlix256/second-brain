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
# Oefensessie 4: Functies 2 - Returnwaarden & Debugging

> **Navigatie:** [[Index]] | [[Exercise Session Tracker]] | [[Sessie 4 - Functies 2 - Returnwaarden en Debugger]] | [[Sessie 4 - Q&A]]

---

## 🎯 Doelstellingen
- Functies correct data laten terugsturen via `return` in plaats van `print()`.
- Unpacken van meervoudige returnwaarden.
- Gebruikmaken van de IDE-debugger om logische fouten en stack frames te analyseren.

---

## 🛠️ Praktijkopgaven

### Opgave 4.1: Oplossen van de Vierkantsvergelijking
**Probleemstelling:**
Schrijf een functie `los_vierkantsvergelijking_op(a, b, c)` die de reële wortels zoekt van $a x^2 + b x + c = 0$.
1. Bereken de discriminant: $D = b^2 - 4ac$.
2. Als $D > 0$: retourneer twee wortels $x_1 = \frac{-b + \sqrt{D}}{2a}$ en $x_2 = \frac{-b - \sqrt{D}}{2a}$.
3. Als $D = 0$: retourneer één wortel $x = \frac{-b}{2a}$.
4. Als $D < 0$: retourneer `None`.

- **Vereiste Theoretische Concepten:**
  - Returnwaarden en tuples: [[Sessie 4 - Functies 2 - Returnwaarden en Debugger#1.1 Meervoudige Returnwaarden]]
  - Onderscheid return vs print: [[Sessie 4 - Functies 2 - Returnwaarden en Debugger#1. Returnwaarden vs. print()]]
  - Preconditie dat $a \neq 0$: [[Sessie 4 - Functies 2 - Returnwaarden en Debugger#2. Pre- en Postcondities & Defensief Programmeren]]

---

### Opgave 4.2: Debugging van een Cumulatieve Berekening
**Probleemstelling:**
Onderstaande functie bevat een semantische fout waardoor de sommatie niet klopt. Plaats een breakpoint op regel 3, gebruik *Step Into* en *Variable Watches* om de fout te lokaliseren en te herstellen.

```python
def bereken_totale_prijs(prijzen, btw_tarief=0.21):
    totaal = 0
    for p in prijzen:
        totaal = p + (p * btw_tarief) # BUG: overschrijft 'totaal' i.p.v. te sommeren!
    return totaal
```

- **Vereiste Theoretische Concepten:**
  - Breakpoints en stepping in de debugger: [[Sessie 4 - Functies 2 - Returnwaarden en Debugger#3.1 Belangrijkste Debugger Acties]]