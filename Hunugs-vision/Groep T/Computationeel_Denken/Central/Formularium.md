# 📐 Formularium & Syntaxiswijzer (Formula Sheet)

> **Navigatie:** [[Index]] | [[Exercise Session Tracker]] | [[Begrippenlijst]] | [[Exam Preparation]]

---

## 1. Wiskundige Formules & Reeksen in de Cursus

| Domein / Toepassing | Formule / Notatie (LaTeX) | Betekenis & Toelichting | Relevante Sessie |
| :--- | :--- | :--- | :--- |
| **Pijler Decompositie** | $$f(x, y) = g(h(x), k(y))$$ | Probleem decompositie in tussenfuncties | [[Sessie 1 - Inleiding tot Computationeel Denken#1.1 De Vijf Fundamentele Pijlers]] |
| **Gehele Deling** | $$q = \lfloor a / b \rfloor$$ | `a // b` (naar beneden afgerond quotiënt) | [[Sessie 2 - Variabelen en Branching Controlestructuren#1.2 Rekenkundige Operatoren]] |
| **Modulo (Rest)** | $$r = a \pmod b$$ | `a % b` (restwaarde na deling) | [[Sessie 2 - Variabelen en Branching Controlestructuren#1.2 Rekenkundige Operatoren]] |
| **De Morgan (Conjunctie)** | $$\neg (P \land Q) \iff (\neg P) \lor (\neg Q)$$ | Negatie van een logische `and` | [[Sessie 2 - Variabelen en Branching Controlestructuren#2.2 Logische Connectieven & Waarheidstabellen]] |
| **De Morgan (Disjunctie)** | $$\neg (P \lor Q) \iff (\neg P) \land (\neg Q)$$ | Negatie van een logische `or` | [[Sessie 2 - Variabelen en Branching Controlestructuren#2.2 Logische Connectieven & Waarheidstabellen]] |
| **Aantal Iteraties `range()`** | $$N = \max\left(0, \left\lceil \frac{\text{stop} - \text{start}}{\text{step}} \right\rceil\right)$$ | Aantal stappen in `range(start, stop, step)` | [[Sessie 5 - For- en While-lussen#3.1 De range(start, stop, step) Functie]] |
| **Kwadratische Sommatie** | $$\sum_{i=1}^{n} i = \frac{n(n+1)}{2} \implies \mathcal{O}(n^2)$$ | Aantal bewerkingen bij geneste driehoekige lussen | [[Sessie 5 - For- en While-lussen#5.1 Wiskundige Complexiteitsanalyse]] |
| **Rechthoekige Matrix Lus** | $$\sum_{i=1}^{R} \sum_{j=1}^{C} 1 = R \times C \implies \mathcal{O}(R \cdot C)$$ | Complexiteit van complete 2D-matrix doorloop | [[Sessie 8 - 2D-lijsten#4. Itereren over 2D-Lijsten]] |
| **Hoofddiagonaal Matrix** | $$m_{i, j} \quad \text{waarbij } i = j$$ | Elementen op de symmetrie-as van een vierkante matrix | [[Sessie 8 - 2D-lijsten#2. Elementen Aanspreken en Afmetingen]] |
| **Matrix Transpositie** | $$(\mathbf{M}^T)_{c, r} = \mathbf{M}_{r, c}$$ | Rij- en kolomcoördinaten omwisselen | [[Sessie 8 - 2D-lijsten#1. Matrices en Tweedimensionale Data]] |

---

## 2. Python Complexiteits- & Slicingwijzer

### 2.1 Slicing Formule
Gegeven een lijst `lst` met lengte $L$:
$$\text{Syntaxis: } \text{lst}[\text{start}:\text{stop}:\text{step}]$$
- Negatieve step: omkeren met `[::-1]`.
- Zie theorie: [[Sessie 6 - Lijsten#2.1 List Slicing: lst[start:stop:step]]]

### 2.2 Asymptotische Tijdscomplexiteit ($\mathcal{O}$-notatie)
- **$\mathcal{O}(1)$ (Constante tijd):**
  - Indexeren van lijst: `lst[i]`
  - Toevoegen achteraan: `lst.append(x)`
  - Lengte opvragen: `len(lst)`
  - Zie theorie: [[Sessie 6 - Lijsten#3.1 In-Place Wijzigingen]]
- **$\mathcal{O}(n)$ (Lineaire tijd):**
  - Zoeken in lijst: `x in lst` of `lst.index(x)`
  - Invoegen vooraan: `lst.insert(0, x)`
  - Verwijderen vooraan: `lst.pop(0)`
  - Kopiëren van een lijst: `lst.copy()`
  - Zie theorie: [[Sessie 6 - Lijsten#4. Geheugenreferenties: De Aliasing Valkuil]]
- **$\mathcal{O}(n^2)$ (Kwadratische tijd):**
  - Geneste lussen: [[Sessie 5 - For- en While-lussen#5. Geneste Lussen & Algoritmische Complexiteit]]
  - 2D-matrix initialisatie & verwerking: [[Sessie 8 - 2D-lijsten#3. Initialisatie en de 'Aliasing Trap']]