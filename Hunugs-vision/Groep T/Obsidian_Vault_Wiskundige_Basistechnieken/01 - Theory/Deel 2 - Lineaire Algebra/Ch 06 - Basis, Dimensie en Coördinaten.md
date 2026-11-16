---
course: "Wiskundige basistechnieken (T1AWB1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: high
tags:
  - study-unit
---

# Hoofdstuk 6: Basis, Dimensie en Coördinaten

> [!abstract] Context
> Dit hoofdstuk behandelt lineaire onafhankelijkheid, het begrip basis, de dimensie van een vectorruimte, coördinatentransformaties en orthonormale basissen via Gram-Schmidt.
> **Parent MOC:** [[Index]] | **Q&A:** [[Q&A - LinAlg Ch 06 Basis en Dimensie]] | **Oefeningen:** [[Oefensessie 12 - Vectorruimten II (Lineaire Afhankelijkheid en Basis)]], [[Oefensessie 13 - Vectorruimten III (Dimensie en Coördinaten)]]

---

## 1. Lineaire (On)afhankelijkheid
Een verzameling vectoren $\{\mathbf{u}_1, \dots, \mathbf{u}_p\}$ is lineair onafhankelijk $\iff$:
$$c_1 \mathbf{u}_1 + c_2 \mathbf{u}_2 + \dots + c_p \mathbf{u}_p = \mathbf{0} \implies c_1 = c_2 = \dots = c_p = 0$$
Indien er niet-triviale oplossingen bestaan (niet alle $c_i = 0$), is de verzameling lineair afhankelijk (minstens één vector is te schrijven als lineaire combinatie van de overige).

---

## 2. Basis en Dimensie
### 2.1 Basis
Een deelverzameling $\mathcal{B} = \{\mathbf{b}_1, \dots, \mathbf{b}_n\}$ van $V$ is een basis $\iff$:
1. $\mathcal{B}$ is lineair onafhankelijk.
2. $\mathcal{B}$ brengt $V$ voort ($L(\mathcal{B}) = V$).

### 2.2 Dimensie
De dimensie $\dim(V)$ is het aantal vectoren in een willekeurige basis van $V$.
- Voor $\mathbb{R}^n$: $\dim = n$.
- Voor $\mathbb{R}^{m \times n}$: $\dim = m \cdot n$.
- Voor $\mathcal{P}_n$ (veeltermen tot graad $n$): $\dim = n + 1$.

---

## 3. Coördinaten t.o.v. een Basis
Als $\mathcal{B} = \{\mathbf{b}_1, \dots, \mathbf{b}_n\}$ een geordende basis is van $V$, kan elke $\mathbf{v} \in V$ **uniek** geschreven worden als:
$$\mathbf{v} = x_1 \mathbf{b}_1 + \dots + x_n \mathbf{b}_n$$
De coördinatenvector is $[\mathbf{v}]_\mathcal{B} = \begin{bmatrix} x_1 \\ \vdots \\ x_n \end{bmatrix} \in \mathbb{R}^n$.

---

## 4. Orthonormale Basissen en Gram-Schmidt
Een basis $\{\mathbf{q}_1, \dots, \mathbf{q}_n\}$ is orthonormaal als:
$$\langle \mathbf{q}_i, \mathbf{q}_j \rangle = \delta_{ij} = \begin{cases} 1 & \text{als } i = j \\ 0 & \text{als } i \neq j \end{cases}$$
- Coördinaten t.o.v. een orthonormale basis berekenen vereist geen stelsel op te lossen, maar enkel inproducten:
  $$x_i = \langle \mathbf{v}, \mathbf{q}_i \rangle$$

### Gram-Schmidt orthogonalisatieproces
Gegeven basis $\{\mathbf{u}_1, \dots, \mathbf{u}_p\}$, construeer orthogonale basis $\{\mathbf{v}_1, \dots, \mathbf{v}_p\}$:
$$\mathbf{v}_1 = \mathbf{u}_1$$
$$\mathbf{v}_2 = \mathbf{u}_2 - \frac{\langle \mathbf{u}_2, \mathbf{v}_1 \rangle}{\|\mathbf{v}_1\|^2} \mathbf{v}_1$$
$$\mathbf{v}_k = \mathbf{u}_k - \sum_{j=1}^{k-1} \frac{\langle \mathbf{u}_k, \mathbf{v}_j \rangle}{\|\mathbf{v}_j\|^2} \mathbf{v}_j$$
Normaliseer vervolgens: $\mathbf{q}_k = \frac{\mathbf{v}_k}{\|\mathbf{v}_k\|}$.

---

> [!summary] Kernsamenvatting
> - Een basis is een minimaal voortbrengend en maximaal lineair onafhankelijk stel vectoren.
> - Coördinaten koppelen elke abstracte $n$-dimensionale vectorruimte isomorf aan $\mathbb{R}^n$.
> - Orthonormale basissen vereenvoudigen projecties en coördinaatberekeningen drastisch.
