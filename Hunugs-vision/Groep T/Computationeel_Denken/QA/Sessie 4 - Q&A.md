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

# Sessie 4 - Q&A (Active Recall)

> **Verwijzingen:** [[Sessie 4 - Functies 2 - Returnwaarden en Debugger]] | [[Oefensessie 4]] | [[Index]]

---

### Vraag 1: Waarom crasht een programma als men een functie die `print()` gebruikt in plaats van `return` aanwendt in een wiskundige berekening?
**Antwoord:**
Een functie zonder expliciet `return`-statement retourneert impliciet het speciale singleton object `None` (van het type `NoneType`). Als het aanroepende script probeert te rekenen met dat resultaat (bijv. `res = bereken() * 2`), crasht het programma met een `TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'`.
*Theorielink:* [[Sessie 4 - Functies 2 - Returnwaarden en Debugger#1. Returnwaarden vs. print()]]

---

### Vraag 2: Wat is het conceptuele verschil tussen een preconditie en een postconditie bij defensief programmeren?
**Antwoord:**
- Een **preconditie** is een contractuele eis die aan de *aanroeper* van de functie wordt opgelegd (bv. "argument `n` moet een strikt positieve integer zijn").
- Een **postconditie** is de garantie die de functie levert aan de aanroeper *nadat* de berekening succesvol is uitgevoerd (bv. "het geretourneerde getal is de wortel van de invoer met een afwijking $< 10^{-6}$").
In Python worden precondities vaak gecontroleerd via `assert` of `raise ValueError()`.
*Theorielink:* [[Sessie 4 - Functies 2 - Returnwaarden en Debugger#2. Pre- en Postcondities & Defensief Programmeren]]

---

### Vraag 3: Welke acties verrichten 'Step Over' en 'Step Into' in een debugger?
**Antwoord:**
- **Step Over (F8)**: Voert de huidige regel code volledig uit als één enkele stap. Indien de regel een functie-aanroep bevat, wordt de functie op de achtergrond afgewerkt zonder dat de debugger regel-voor-regel in die functie stapt.
- **Step Into (F7)**: Duikt naar binnen in de functie die op de huidige regel wordt aangeroepen, zodat je de interne stappen en lokale variabelen van die functie regel voor regel kunt inspecteren.
*Theorielink:* [[Sessie 4 - Functies 2 - Returnwaarden en Debugger#3.1 Belangrijkste Debugger Acties]]