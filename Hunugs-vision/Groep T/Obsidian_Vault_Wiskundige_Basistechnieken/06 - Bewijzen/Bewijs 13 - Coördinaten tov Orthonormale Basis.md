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

# Bewijs 13: Coördinaten t.o.v. een Orthonormale Basis

> [!abstract] Context & Examenbelang
> **Theorievraag 13:** *"Formuleer en bewijs de uitdrukking voor de coördinaatvector van een vector $u$ in een inproductruimte $V$ ten opzichte van een orthonormale basis $S = \{u_1, u_2, \dots, u_n\}$."*
> **Verwante Theorie:** [[Ch 06 - Basis, Dimensie en Coördinaten#2. Coördinaten en Basistransformaties]]
> **Formularium:** [[Formularium#2. Lineaire Algebra]] | **MOC:** [[00 - Index der Bewijzen]]

---

## 1. Formulering van de Stelling
Zij $V$ een reële inproductruimte en zij $S = \{u_1, u_2, \dots, u_n\}$ een **orthonormale basis** van $V$.
Dan worden de coördinaten van een willekeurige vector $u \in V$ ten opzichte van de basis $S$ gegeven door de inproducten van $u$ met de respectievelijke basisvectoren:
$$a_i = \langle u, u_i \rangle \quad (\text{voor } i = 1, 2, \dots, n)$$
De coördinaatvector $[u]_S$ heeft bijgevolg de expliciete gedaante:
$$[u]_S = \begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{bmatrix} = \begin{bmatrix} \langle u, u_1 \rangle \\ \langle u, u_2 \rangle \\ \vdots \\ \langle u, u_n \rangle \end{bmatrix}$$
en de vector $u$ kan ontbonden worden als:
$$u = \sum_{i=1}^n \langle u, u_i \rangle u_i$$

---

## 2. Stap-voor-stap Bewijs

### Stap 1: Ontbinding in de Basis
Aangezien $S = \{u_1, u_2, \dots, u_n\}$ een basis is van $V$, kan elke vector $u \in V$ volgens [[Bewijs 12 - Uniciteit van Lineaire Combinatie in een Basis|de uniciteitsstelling]] op unieke wijze geschreven worden als lineaire combinatie van de basisvectoren:
$$u = \sum_{j=1}^n a_j u_j = a_1 u_1 + a_2 u_2 + \dots + a_n u_n$$
waarbij $a_j$ de gezochte $j$-de coördinaat van $u$ ten opzichte van $S$ is.

### Stap 2: Inproduct Nemen met een Willekeurige Basisvector $u_i$
Neem links en rechts in deze vectorgelijkheid het inproduct met de $i$-de basisvector $u_i$ (voor een vaste $i \in \{1, 2, \dots, n\}$):
$$\langle u, u_i \rangle = \left\langle \sum_{j=1}^n a_j u_j, \; u_i \right\rangle$$

### Stap 3: Gebruik van de Bilineariteit van het Inproduct
Wegens de lineariteit van het inproduct in zijn eerste argument mogen we de sommatie en de scalairen $a_j$ buiten het inproduct brengen:
$$\langle u, u_i \rangle = \sum_{j=1}^n a_j \langle u_j, u_i \rangle$$
Uitgeschreven luidt dit:
$$\langle u, u_i \rangle = a_1 \langle u_1, u_i \rangle + \dots + a_i \langle u_i, u_i \rangle + \dots + a_n \langle u_n, u_i \rangle$$

### Stap 4: Toepassing van de Orthonormaliteitsconditie
De basis $S$ is per hypothese **orthonormaal**. Dit impliceert twee eigenschappen:
1. **Orthogonaliteit:** $\langle u_j, u_i \rangle = 0$ voor alle $j \neq i$.
2. **Normalisatie:** $\langle u_i, u_i \rangle = \|u_i\|^2 = 1$ voor alle $i$.

In termen van de Kronecker-delta $\delta_{ji}$:
$$\langle u_j, u_i \rangle = \delta_{ji} = \begin{cases} 1 & \text{als } j = i \\ 0 & \text{als } j \neq i \end{cases}$$

Substitutie van deze waarden in de som levert:
$$\sum_{j=1}^n a_j \langle u_j, u_i \rangle = a_1 \cdot 0 + \dots + a_i \cdot 1 + \dots + a_n \cdot 0 = a_i \cdot 1 = a_i$$

### Stap 5: Conclusie
Hieruit volgt direct dat:
$$a_i = \langle u, u_i \rangle$$
Dit geldt voor elke $i \in \{1, 2, \dots, n\}$. Bijgevolg is:
$$[u]_S = \begin{bmatrix} \langle u, u_1 \rangle \\ \langle u, u_2 \rangle \\ \vdots \\ \langle u, u_n \rangle \end{bmatrix} \quad \blacksquare$$

---

## 3. Waarom is dit een Fundamenteel Resultaat?
- **Vermijding van Stelsels:** In een willekeurige niet-orthogonale basis vereist het vinden van coördinaten het oplossen van een $n \times n$ lineair stelsel. In een orthonormale basis volstaan $n$ eenvoudige inproductberekeningen.
- **Individuele Berekening:** Men kan elke gewenste coördinaat $a_i = \langle u, u_i \rangle$ volledig autonoom berekenen, zonder de andere coördinaten te moeten kennen.
