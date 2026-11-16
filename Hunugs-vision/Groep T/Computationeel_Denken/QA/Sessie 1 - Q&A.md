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

# Sessie 1 - Q&A (Active Recall)

> **Verwijzingen:** [[Sessie 1 - Inleiding tot Computationeel Denken]] | [[Oefensessie 1]] | [[Index]]

---

### Vraag 1: Wat zijn de vijf pijlers van Computationeel Denken en hoe verschillen decompositie en abstractie van elkaar?
**Antwoord:**
De vijf pijlers zijn:
1. Decompositie
2. Patroonherkenning
3. Abstractie
4. Algoritmisch denken
5. Evaluatie & testing

Het verschil tussen decompositie en abstractie is fundamenteel:
- **Decompositie** breekt een probleem structureel op in kleinere, zelfstandige deelproblemen (bijvoorbeeld een programma opdelen in meerdere hulpfuncties).
- **Abstractie** verwijdert irrelevante context en details om een vereenvoudigd conceptueel model of algemene datastructuur over te houden (bijvoorbeeld een complex object voorstellen als een tuple of integer in plaats van alle fysieke eigenschappen te modelleren).
*Theorielink:* [[Sessie 1 - Inleiding tot Computationeel Denken#1.1 De Vijf Fundamentele Pijlers]]

---

### Vraag 2: Welke rol spelen de Von Neumann-componenten bij de uitvoering van een expressie zoals `x = a + b`?
**Antwoord:**
1. De **Control Unit (CU)** in de CPU haalt de instructie op (*fetch*) uit het geheugen (RAM).
2. De CU decodeert de instructie (*decode*) en laadt de waarden van variabelen `a` en `b` uit hun respectievelijke RAM-adressen naar de interne CPU-registers.
3. De **Arithmetic Logic Unit (ALU)** voert de optelling $a + b$ fysiek uit.
4. De CU slaat het resultaat (*writeback*) op in het geheugenadres dat geassocieerd is met variabele `x`.
*Theorielink:* [[Sessie 1 - Inleiding tot Computationeel Denken#2. Computerarchitectuur in een Notendop]]

---

### Vraag 3: Aan welke formele eisen moet een algoritme voldoen en hoe wordt een voorwaardelijke splitsing voorgesteld in een flowchart?
**Antwoord:**
Een deugdelijk algoritme is:
- **Deterministisch**: Gelijke invoer levert steeds dezelfde uitvoer op.
- **Eindig**: Het proces stopt gegarandeerd na een eindig aantal stappen ($k < \infty$).
- **Effectief**: Alle instructies zijn uitvoerbaar en ondubbelzinnig.

In een flowchart wordt een voorwaardelijke splitsing voorgesteld door een **Ruit (Diamond)** met minstens twee uitgaande pijlen (bv. *True* en *False*).
*Theorielink:* [[Sessie 1 - Inleiding tot Computationeel Denken#3. Flowcharts & Algoritmische Notatie]]