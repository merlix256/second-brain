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
# Oefensessie 7: Tussentijdse Feedbacktest (Simulatie)

> **Navigatie:** [[Index]] | [[Exercise Session Tracker]] | [[Sessie 7 - Feedbacktest en Tussentijdse Evaluatie]] | [[Sessie 7 - Q&A]]

---

## 🎯 Doelstellingen
- Tussentijdse formatieve proef over Sessie 1 t.e.m. Sessie 6.
- Programmeren onder tijdsdruk met enkel een handgeschreven 4-pagina spiekbrief.
- Automatische validatie via unit-tests.

---

## 🛠️ Examen-simulatie Opgaven

### Proefopgave 1: Voortschrijdend Gemiddelde (Moving Average)
**Opgave:**
Schrijf een functie `moving_average(waarden, venstergrootte)` die voor een lijst getallen het voortschrijdend gemiddelde berekent over een venster van lengte $k$.
Voor elk venster van $i$ tot $i + k$:
$$\mu_i = \frac{1}{k} \sum_{j=0}^{k-1} \text{waarden}[i + j]$$
Retourneer een lijst van deze gemiddelden. Indien $\text{len}(\text{waarden}) < k$, retourneer een lege lijst `[]`.

- **Vereiste Theoretische Concepten:**
  - Slicing van deelrijen: [[Sessie 6 - Lijsten#2.1 List Slicing: lst[start:stop:step]]]
  - Geneste lussen en accumulator: [[Sessie 5 - For- en While-lussen#5. Geneste Lussen & Algoritmische Complexiteit]]
  - Randgevallen en defensief programmeren: [[Sessie 4 - Functies 2 - Returnwaarden en Debugger#2. Pre- en Postcondities & Defensief Programmeren]]

---

### Proefopgave 2: Compacte Run-Length Encoding (RLE)
**Opgave:**
Implementeer een functie `rle_encode(tekst)` die opeenvolgende identieke tekens comprimeert tot paren van `(karakter, aantal)`. Bij invoer `"AAABBBCCDAA"` retourneert het `[('A', 3), ('B', 3), ('C', 2), ('D', 1), ('A', 2)]`.

- **Vereiste Theoretische Concepten:**
  - Lijstmanipulaties en tuples: [[Sessie 4 - Functies 2 - Returnwaarden en Debugger#1.1 Meervoudige Returnwaarden]]
  - Loopcondities en iteratiestructuren: [[Sessie 5 - For- en While-lussen#1. Iteratieve Controlestructuren]]