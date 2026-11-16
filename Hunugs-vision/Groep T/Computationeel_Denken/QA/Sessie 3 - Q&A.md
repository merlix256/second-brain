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

# Sessie 3 - Q&A (Active Recall)

> **Verwijzingen:** [[Sessie 3 - Functies 1 - Definitie, Aanroep en Parameters]] | [[Oefensessie 3]] | [[Index]]

---

### Vraag 1: Wat is het fundamentele verschil tussen formele en actuele parameters?
**Antwoord:**
- **Formele parameters** zijn de variabelenamen die in de functiekop (*header*) gedefinieerd staan (bijvoorbeeld `def f(x, y):`). Ze fungeren als tijdelijke placeholders in de lokale scope.
- **Actuele parameters (argumenten)** zijn de werkelijke expressies, variabelen of concrete waarden die aan de functie worden meegegeven bij de function call (bijvoorbeeld `f(a + 2, 10)`).
*Theorielink:* [[Sessie 3 - Functies 1 - Definitie, Aanroep en Parameters#2.1 Formele vs. Actuele Parameters]]

---

### Vraag 2: Waarom moeten default parameters altijd achteraan in de parameterlijst staan?
**Antwoord:**
Omdat Python bij de aanroep argumenten positioneel van links naar rechts toewijst. Als een parameter met defaultwaarde vooraan zou staan, ontstaat ambiguïteit bij het weglaten van argumenten: de interpreter kan niet bepalen welk argument bedoeld is voor welke parameter. Daarom geeft Python een `SyntaxError: non-default argument follows default argument`.
*Theorielink:* [[Sessie 3 - Functies 1 - Definitie, Aanroep en Parameters#3.2 Default Parameters]]

---

### Vraag 3: Hoe verloopt de LEGB-scoperesolutie wanneer binnen een functie een variabele wordt gelezen?
**Antwoord:**
Python zoekt de naam in vier hiërarchische niveaus:
1. **L**ocal: Bestaat de variabele binnen de huidige functie-executie op het actieve stack frame?
2. **E**nclosing: Bestaat de variabele in een omsluitende functie (bij geneste functies)?
3. **G**lobal: Is de variabele gedefinieerd op het hoogste niveau van het script/module?
4. **B**uilt-in: Is het een standaard ingebouwde naam van Python (zoals `abs`, `sum`, `len`)?
Wordt de naam nergens gevonden, dan werpt Python een `NameError`.
*Theorielink:* [[Sessie 3 - Functies 1 - Definitie, Aanroep en Parameters#4.1 LEGB-Regel voor Scope Resolutie]]