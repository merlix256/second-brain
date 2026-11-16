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

# Sessie 8: 2D-lijsten

> **Navigatie:** [[Index]] | [[Exercise Session Tracker]] | [[Sessie 8 - Q&A]] | [[Oefensessie 8]]

---

## 1. Matrices en Tweedimensionale Data
Veel praktische ingenieursvraagstukken vereisen 2D-roosters, zoals numerieke matrices, tabellen, sensordata en beeldrasterpunten (pixels). In Python wordt een 2D-structuur gerepresenteerd als een **lijst van lijsten** (*nested list*).

$$\mathbf{M} = \begin{bmatrix}
m_{0,0} & m_{0,1} & m_{0,2} \\
m_{1,0} & m_{1,1} & m_{1,2} \\
m_{2,0} & m_{2,1} & m_{2,2}
\end{bmatrix}$$

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

![[Slide_Sessie8_Matrix_Grid_Indices.png]]
*Figuur 1: Indexering in een 2D-lijst via rij- en kolomcoördinaten (rij $r$, kolom $c$).*

---

## 2. Elementen Aanspreken en Afmetingen
Om een specifiek element op rij $r$ en kolom $c$ te bereiken, gebruiken we dubbele haken:
$$\text{Element} = \text{matrix}[r][c]$$

- Aantal rijen: $R = \text{len}(\text{matrix})$
- Aantal kolommen (bij rechthoekige matrix): $C = \text{len}(\text{matrix}[0])$

```python
val = matrix[1][2] # Rij-index 1, Kolom-index 2 -> Waarde: 6
```

---

## 3. Initialisatie en de "Aliasing Trap"
Een van de meest gemaakte en ernstige fouten bij 2D-lijsten in Python is foutieve initialisatie met vermenigvuldiging.

> [!WARNING] De Fatale Valkuil: `[[0] * C] * R`
> ```python
> # FOUT:
> bad_matrix = [[0] * 3] * 3
> bad_matrix[0][0] = 99
> print(bad_matrix)
> # Uitvoer: [[99, 0, 0], [99, 0, 0], [99, 0, 0]]!
> ```
> **Waarom gebeurt dit?** De buitenste `* 3` dupliceert de **referentie** naar exact dezelfde binnenste lijst 3 keer. Aanpassing van 1 rij wijzigt alle rijen!

### 3.1 De Correcte Manier: List Comprehension of Geneste Lussen
```python
# CORRECT via list comprehension:
R, C = 3, 3
correct_matrix = [[0 for _ in range(C)] for _ in range(R)]
correct_matrix[0][0] = 99
# Uitvoer: [[99, 0, 0], [0, 0, 0], [0, 0, 0]]
```

---

## 4. Itereren over 2D-Lijsten
We gebruiken geneste `for`-lussen om een matrix te doorkruisen:

### 4.1 Rij-per-rij (Row-major traversal)
```python
for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        print(matrix[r][c], end=" ")
    print()
```

### 4.2 Kolom-per-kolom (Column-major traversal)
Handig voor het berekenen van kolomsommen:
```python
for c in range(len(matrix[0])):
    kolom_som = 0
    for r in range(len(matrix)):
        kolom_som += matrix[r][c]
    print(f"Som kolom {c}: {kolom_som}")
```

---

## 📝 Samenvatting
2D-lijsten representeren matrices via geneste lijsten. Elementen worden aangesproken via `matrix[r][c]`. Initialisatie mag nooit gebeuren met `[[0]*C]*R` wegens aliasing van rijen, maar vereist een list comprehension. Doorkruisen van matrices gebeurt met dubbele lussen in $\mathcal{O}(R \times C)$ tijdscomplexiteit.