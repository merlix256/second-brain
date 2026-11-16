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
# Oefensessie 1: Inleiding & Algoritmisch Denken

> **Navigatie:** [[Index]] | [[Exercise Session Tracker]] | [[Sessie 1 - Inleiding tot Computationeel Denken]] | [[Sessie 1 - Q&A]]

---

## 🎯 Doelstellingen
- Een gespecificeerd probleem ontleden via **decompositie**.
- Een ondubbelzinnig stappenplan ontwerpen en uittekenen in een flowchart.
- De eerste elementaire console input- en outputbewerkingen uitvoeren.

---

## 🛠️ Praktijkopgaven

### Opgave 1.1: Flowchart & Berekening van Trajecttijd
**Probleemstelling:**
Een robotwagen beweegt over een afstand $s$ (in meters) met een constante snelheid $v$ (in $\text{m/s}$). Teken een stroomdiagram en schrijf een Python-script dat de benodigde reistijd $t$ in seconden berekent:
$$t = \frac{s}{v}$$
Indien de ingevoerde snelheid $v \le 0$, dient het programma een foutmelding te tonen en niet te delen door nul.

- **Vereiste Theoretische Concepten:**
  - Pijler Decompositie en Algoritmisch denken: [[Sessie 1 - Inleiding tot Computationeel Denken#1.1 De Vijf Fundamentele Pijlers]]
  - Flowchart beslissings- en procesblokken: [[Sessie 1 - Inleiding tot Computationeel Denken#3. Flowcharts & Algoritmische Notatie]]
  - CPU & I/O interactie: [[Sessie 1 - Inleiding tot Computationeel Denken#2. Computerarchitectuur in een Notendop]]

**Voorbeeldinteractie:**
```text
Voer de afstand in (m): 150
Voer de snelheid in (m/s): 10
De berekende reistijd bedraagt: 15.0 seconden.
```

---

### Opgave 1.2: Verval van Isotopen (Evaluatie & Testing)
**Probleemstelling:**
Stel een algoritme op dat voor een radioactieve stof met beginmassa $M_0$ en halveringstijd $T_{1/2}$ berekent hoeveel gram er overblijft na $t$ dagen:
$$M(t) = M_0 \cdot \left(\frac{1}{2}\right)^{\frac{t}{T_{1/2}}}$$
Formuleer minstens 3 representatieve testgevallen (normale invoer, $t = 0$, en $t = T_{1/2}$).

- **Vereiste Theoretische Concepten:**
  - Evaluatie & Testgevallen: [[Sessie 1 - Inleiding tot Computationeel Denken#1.1 De Vijf Fundamentele Pijlers]]
  - Algoritmische determinisme: [[Sessie 1 - Inleiding tot Computationeel Denken#3. Flowcharts & Algoritmische Notatie]]