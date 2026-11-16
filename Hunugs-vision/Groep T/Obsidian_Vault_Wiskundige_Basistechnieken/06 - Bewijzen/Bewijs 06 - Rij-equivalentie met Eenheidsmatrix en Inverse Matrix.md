---
course: "Wiskundige basistechnieken (T1AWB1)"
unit_type: bewijs
status: todo
completed: false
est_hours: 1.0
priority: high
tags:
  - study-unit
---

# Bewijs 06: Rij-equivalentie met de Eenheidsmatrix en Inverse Matrix

> [!abstract] Context & Examenbelang
> **Theorievraag 6:** *"Bewijs dat elke matrix die rij-equivalent is met de eenheidsmatrix ook regulier is, en leg uit hoe dit bewijs een uitdrukking voor de inverse matrix oplevert."*
> **Verwante Theorie:** [[Ch 02 - Matrices en Echelonvormen#3. Echelonvormen en Rang]] | [[Ch 03 - Vierkante Matrices en Determinanten#1. Inverse van een Matrix]]
> **Formularium:** [[Formularium#2. Lineaire Algebra]] | **MOC:** [[00 - Index der Bewijzen]]

---

## 1. Formulering van de Stelling
Zij $A \in \mathbb{R}^{n \times n}$ een vierkante matrix.
**Stelling:**
1. Als $A$ rij-equivalent is met de eenheidsmatrix $I_n$ ($A \sim I_n$), dan is $A$ regulier (inverteerbaar).
2. De inverse matrix $A^{-1}$ is gelijk aan het product van de elementaire matrices die $A$ tot $I_n$ herleiden:
   $$A^{-1} = E_m E_{m-1} \dots E_2 E_1$$

---

## 2. Stap-voor-stap Bewijs

### Stap 1: Rij-equivalentie en Elementaire Matrices
Per definitie betekent $A \sim I_n$ dat de matrix $A$ door een eindige reeks van $m$ elementaire rij-operaties kan worden omgevormd tot de eenheidsmatrix $I_n$.
Elke elementaire rij-operatie stemt overeen met het links vermenigvuldigen met een elementaire matrix $E_k \in \mathbb{R}^{n \times n}$ ($k = 1, \dots, m$):
$$I_n = E_m E_{m-1} \dots E_2 E_1 A$$

### Stap 2: Inverteerbaarheid van Elementaire Matrices
Elke elementaire matrix $E_k$ is regulier (inverteerbaar) omdat elke elementaire rij-operatie reversibel is:
- Een rij vermenigvuldigen met $c \neq 0$ wordt ongedaan gemaakt door te vermenigvuldigen met $1/c$.
- Twee rijen wisselen is zijn eigen inverse.
- Een veelvoud van een rij optellen bij een andere rij wordt ongedaan gemaakt door hetzelfde veelvoud af te trekken.
Bijgevolg bezit elke elementaire matrix $E_k$ een inverse $E_k^{-1}$ die zelf een elementaire matrix is.

### Stap 3: Isoleren van de Matrix A
We vermenigvuldigen beide leden van $I_n = (E_m E_{m-1} \dots E_1) A$ achtereenvolgens links met de inverses van de elementaire matrices:
1. Links vermenigvuldigen met $E_m^{-1}$:
   $$E_m^{-1} I_n = E_m^{-1} (E_m E_{m-1} \dots E_1 A) = (E_m^{-1} E_m) E_{m-1} \dots E_1 A = I_n E_{m-1} \dots E_1 A$$
   $$E_m^{-1} = E_{m-1} \dots E_1 A$$
2. Herhaal deze bewerking voor $E_{m-1}^{-1}, E_{m-2}^{-1}, \dots, E_1^{-1}$:
   $$E_1^{-1} E_2^{-1} \dots E_{m-1}^{-1} E_m^{-1} = A$$

### Stap 4: Conclusies
1. **$A$ is regulier:**
   De matrix $A$ is geschreven als een eindig product van reguliere matrices ($E_k^{-1}$). Omdat het product van reguliere matrices steeds regulier is, is $A$ noodzakelijk zelf regulier.
2. **Uitdrukking voor de inverse $A^{-1}$:**
   Aangezien $(E_m E_{m-1} \dots E_1) A = I_n$, en de inverse van een vierkante matrix uniek is, geldt per definitie van de inverse matrix dat:
   $$A^{-1} = E_m E_{m-1} \dots E_2 E_1 \quad \blacksquare$$

---

## 3. Praktische Betekenis: Het Gauss-Jordan Algoritme
Dit theoretische bewijs legt direct het fundament voor het bepalen van inverses via de geaugmenteerde matrix:
$$\left[ A \;\middle|\; I_n \right] \xrightarrow{\text{elementaire rij-operaties}} \left[ I_n \;\middle|\; A^{-1} \right]$$
Immers:
$$E_m \dots E_1 \left[ A \;\middle|\; I_n \right] = \left[ (E_m \dots E_1) A \;\middle|\; (E_m \dots E_1) I_n \right] = \left[ I_n \;\middle|\; A^{-1} \right]$$
