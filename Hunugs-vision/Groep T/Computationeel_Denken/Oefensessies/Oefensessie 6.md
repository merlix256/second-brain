---
course: "Computationeel Denken (T1ACD1)"
unit_type: oefensessie
status: todo
completed: false
est_hours: 2.0
priority: high
tags:
  - study-unit
---
# Oefensessie 6: 1D-Lijsten & Algoritmes

> **Navigatie:** [[Index]] | [[Exercise Session Tracker]] | [[Sessie 6 - Lijsten]] | [[Sessie 6 - Q&A]]

---

## 🎯 Doelstellingen
- Manipuleren van lijsten via indexering en slicing `[start:stop:step]`.
- Toepassen van methodes (`.append()`, `.pop()`, `.remove()`).
- Vermijden van de aliasing-valkuil door expliciet kopiëren.

---

## 🛠️ Praktijkopgaven

### Opgave 6.1: Filteren en Normaliseren van Sensordata
**Probleemstelling:**
Schrijf een functie `normaliseer_metingen(metingen)` die een lijst van getallen ontvangt.
1. Vind het minimum $x_{\min}$ en maximum $x_{\max}$.
2. Maak een **nieuwe** lijst met genormaliseerde waarden $z_i \in [0, 1]$ volgens:
   $$z_i = \frac{x_i - x_{\min}}{x_{\max} - x_{\min}}$$
3. De originele lijst `metingen` mag **niet** gemuteerd worden!

- **Vereiste Theoretische Concepten:**
  - Mutabiliteit en kopiëren van lijsten: [[Sessie 6 - Lijsten#4. Geheugenreferenties: De Aliasing Valkuil]]
  - Lijstaccumulatie en `.append()`: [[Sessie 6 - Lijsten#3.1 In-Place Wijzigingen]]
  - Itereren over lijsten: [[Sessie 6 - Lijsten#5. Algoritmes op Lijsten: Lineair Zoeken & Accumulatie]]

---

### Opgave 6.2: Palindroomdetector via Slicing
**Probleemstelling:**
Schrijf een functie `is_palindroom(woord)` die controleert of een opgegeven string van links naar rechts gelijk is aan van rechts naar links (bijv. "lepel" of "racecar"). Los dit op in één enkele regel code gebruikmakend van extended slicing.

- **Vereiste Theoretische Concepten:**
  - Slicing met negatieve step `[::-1]`: [[Sessie 6 - Lijsten#2.1 List Slicing: lst[start:stop:step]]]