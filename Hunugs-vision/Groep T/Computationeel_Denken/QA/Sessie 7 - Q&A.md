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

# Sessie 7 - Q&A (Active Recall)

> **Verwijzingen:** [[Sessie 7 - Feedbacktest en Tussentijdse Evaluatie]] | [[Oefensessie 7 - Feedbacktest]] | [[Index]]

---

### Vraag 1: Waarom slaagt een functie die een algoritme berekent lokaal op het oog wel met `print()`, maar faalt deze met 0/20 in de automatische evaluatiesoftware van Toledo?
**Antwoord:**
Automatische testsuites (zoals PyTest of grading scripts op Toledo) importeren de studentenfunctie en evalueren de expressie `assert student_functie(invoer) == verwachte_uitvoer`.
Als de functie de waarde print i.p.v. te retourneren met `return`, retourneert de functie `None`. De test evalueert `None == verwachte_uitvoer`, wat resulteert in `False`, waardoor alle geautomatiseerde testgevallen falen.
*Theorielink:* [[Sessie 7 - Feedbacktest en Tussentijdse Evaluatie#3. Typische Examen- en Testfouten]]

---

### Vraag 2: Welke edge-cases moet je altijd systematisch controleren bij functies die lijsten verwerken?
**Antwoord:**
1. De lege lijst: `[]` (risico op `ZeroDivisionError` bij gemiddelden of `IndexError`).
2. Een lijst met exact één element: `[x]`.
3. Lijsten met enkel negatieve getallen (gevaarlijk als initialisatie van `maximum = 0` gekozen werd i.p.v. `maximum = lst[0]`).
4. Lijsten met duplicaten of identieke waarden: `[5, 5, 5]`.
*Theorielink:* [[Sessie 7 - Feedbacktest en Tussentijdse Evaluatie#2.1 Kerncompetenties]]

---

### Vraag 3: Wat mag je meenemen naar de feedbacktest en het eindexamen qua hulpmiddelen?
**Antwoord:**
Een **handgeschreven samenvatting van maximaal 4 bladzijden** (dit betekent 2 fysieke A4-vellen, recto-verso beschreven). Geen gedrukte documenten of digitaal doorzoekbare notities!
*Theorielink:* [[Sessie 7 - Feedbacktest en Tussentijdse Evaluatie#1. Doel en Structuur van de Feedbacktest]]