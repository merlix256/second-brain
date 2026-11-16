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

# Bewijs 12: Uniciteit van de Lineaire Combinatie in een Basis

> [!abstract] Context & Examenbelang
> **Theorievraag 12:** *"Bewijs dat elke vector $u$ in een reële vectorruimte $V$ op een unieke manier geschreven kan worden als een lineaire combinatie van basisvectoren in een basis $S = \{u_1, u_2, \dots, u_n\}$ voor $V$."*
> **Verwante Theorie:** [[Ch 06 - Basis, Dimensie en Coördinaten#1. Basis en Dimensie]]
> **Formularium:** [[Formularium#2. Lineaire Algebra]] | **MOC:** [[00 - Index der Bewijzen]]

---

## 1. Formulering van de Stelling
Zij $V$ een reële vectorruimte en zij $S = \{u_1, u_2, \dots, u_n\} \subset V$ een basis van $V$.
Dan kan elke vector $u \in V$ op **precies één unieke manier** geschreven worden als een lineaire combinatie van de basisvectoren uit $S$:
$$u = \sum_{i=1}^n a_i u_i = a_1 u_1 + a_2 u_2 + \dots + a_n u_n \quad (a_i \in \mathbb{R})$$

---

## 2. Stap-voor-stap Bewijs

Het bewijs bestaat uit twee fundamentele onderdelen: **existentie** (het bestaan van de combinatie) en **uniciteit** (de uniekheid van de coëfficiënten).

### Stap 1: Existentie van de Lineaire Combinatie
Per definitie is een basis $S$ een verzameling vectoren die:
1. De vectorruimte $V$ **voortbrengt** ($\text{span}(S) = V$), en
2. **Lineair onafhankelijk** is.

Omdat $S$ voortbrengend is voor $V$, kan elke willekeurige vector $u \in V$ geschreven worden als een lineaire combinatie van elementen uit $S$. Er bestaan dus reële getallen $a_1, a_2, \dots, a_n \in \mathbb{R}$ zodanig dat:
$$u = a_1 u_1 + a_2 u_2 + \dots + a_n u_n$$

### Stap 2: Hypothese van Niet-Uniciteit
Veronderstel nu (uit het ongerijmde of ter verificatie van de uniciteit) dat dezelfde vector $u$ op een tweede manier geschreven kan worden als lineaire combinatie van dezelfde basisvectoren met coëfficiënten $b_1, b_2, \dots, b_n \in \mathbb{R}$:
$$u = b_1 u_1 + b_2 u_2 + \dots + b_n u_n$$

### Stap 3: Lid aan Lid Aftrekken
We trekken beide representaties van $u$ lid aan lid van elkaar af:
$$u - u = (a_1 u_1 + a_2 u_2 + \dots + a_n u_n) - (b_1 u_1 + b_2 u_2 + \dots + b_n u_n)$$
Aangezien $u - u = \mathbf{0}$ (de nulvector van $V$), kunnen we de termen groeperen met behulp van de vectorruimte-axioma's (distributiviteit en associativiteit):
$$\mathbf{0} = (a_1 - b_1) u_1 + (a_2 - b_2) u_2 + \dots + (a_n - b_n) u_n$$

### Stap 4: Toepassing van Lineaire Onafhankelijkheid
De gelijkheid:
$$(a_1 - b_1) u_1 + (a_2 - b_2) u_2 + \dots + (a_n - b_n) u_n = \mathbf{0}$$
is een lineaire combinatie van de basisvectoren $u_1, u_2, \dots, u_n$ die gelijk is aan de nulvector.
Omdat $S$ een basis is, is de verzameling $\{u_1, u_2, \dots, u_n\}$ per definitie **lineair onafhankelijk**.
De definitie van lineaire onafhankelijkheid dicteert dat een lineaire combinatie van deze vectoren slechts dan de nulvector kan opleveren als **alle coëfficiënten strikt gelijk zijn aan nul**:
$$a_i - b_i = 0 \quad \text{voor alle } i \in \{1, 2, \dots, n\}$$
Hieruit volgt onmiddellijk dat:
$$a_1 = b_1, \quad a_2 = b_2, \quad \dots, \quad a_n = b_n$$

### Stap 5: Conclusie
De twee veronderstelde lineaire combinaties zijn volkomen identiek. De voorstelling van de vector $u$ ten opzichte van de basis $S$ is bijgevolg strikt uniek. $\blacksquare$

---

## 3. Belang voor het Begrip "Coördinaten"
Deze stelling is de formele rechtvaardiging voor het begrip **coördinaten**:
Omdat de scalairen $a_1, \dots, a_n$ uniek zijn voor een gegeven basis $S$, kunnen we de unieke coördinaatvector van $u$ definiëren als:
$$[u]_S = \begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{bmatrix} \in \mathbb{R}^n$$
Zonder uniciteit zou het toekennen van een coördinaatvector aan een willekeurige vector mathematisch ongeldig zijn.
