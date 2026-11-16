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

# Hoofdstuk 3: Vierkante Matrices en Determinanten

> [!abstract] Context
> Dit hoofdstuk behandelt de inverse matrix, determinanten van willekeurige orde, de methode van ordeverlaging, de adjunctmatrix en orthogonale matrices.
> **Parent MOC:** [[Index]] | **Q&A:** [[Q&A - LinAlg Ch 03 Vierkante Matrices]] | **Oefeningen:** [[Oefensessie 08 - Matrices II (Vierkante Matrices)]]

---

## 1. De Inverse Matrix
Een vierkante matrix $A \in \mathbb{R}^{n \times n}$ is inverteerbaar (regulier) als er een $A^{-1}$ bestaat zodanig dat:
$$A A^{-1} = A^{-1} A = I_n$$
- $(AB)^{-1} = B^{-1} A^{-1}$
- $(A^T)^{-1} = (A^{-1})^T$
- **Praktische berekening via Gauss-Jordan:**
  $$[A \mid I_n] \xrightarrow{\text{rij-operaties}} [I_n \mid A^{-1}]$$

---

## 2. De Determinant van een Matrix
### 2.1 Determinanten van Orde 2 en 3
- Voor $2 \times 2$: $\det \begin{bmatrix} a & b \\ c & d \end{bmatrix} = ad - bc$.
- Voor $3 \times 3$: Regel van Sarrus.

### 2.2 Ontwikkeling naar een Rij of Kolom (Laplace)
$$\det(A) = \sum_{j=1}^n a_{ij} (-1)^{i+j} M_{ij}$$
waarbij $M_{ij}$ de minor is (determinant van submatrix door weglaten van rij $i$ en kolom $j$).

### 2.3 Eigenschappen van Determinanten
1. $\det(A^T) = \det(A)$.
2. $\det(AB) = \det(A) \cdot \det(B)$.
3. $\det(A^{-1}) = \frac{1}{\det(A)}$ (mits $\det(A) \neq 0$).
4. Rijverwisseling verwisselt het teken van de determinant.
5. Een rij schalen met $k$ schaalt de determinant met $k$: $\det(k A) = k^n \det(A)$.
6. $R_i + k R_j$ verandert de determinant niet!

### 2.4 Methode van Ordeverlaging
Door middel van rij-operaties $R_i + k R_j$ maakt men alle elementen behalve één in een gekozen rij of kolom gelijk aan nul, waarna Laplace-ontwikkeling de orde met 1 verlaagt.

---

## 3. Adjunctmatrix en Formule voor de Inverse
De cofactor $C_{ij} = (-1)^{i+j} M_{ij}$. De adjunctmatrix is de getransponeerde van de cofactorenmatrix:
$$\text{adj}(A) = [C_{ij}]^T$$
$$A^{-1} = \frac{1}{\det(A)} \text{adj}(A)$$

---

## 4. Orthogonale Matrices
Een matrix $Q \in \mathbb{R}^{n \times n}$ is orthogonaal als:
$$Q^T Q = Q Q^T = I_n \iff Q^{-1} = Q^T$$
- De kolommen (en rijen) van $Q$ vormen een orthonormale basis van $\mathbb{R}^n$.
- $\det(Q) = \pm 1$.

---

> [!summary] Kernsamenvatting
> - $A$ is inverteerbaar $\iff \det(A) \neq 0 \iff \text{rang}(A) = n$.
> - Ordeverlaging via rij-operaties is numeriek veel efficiënter dan pure cofactorontwikkeling.
> - Orthogonale matrices behouden lengtes en hoeken ($\|Q\mathbf{x}\| = \|\mathbf{x}\|$).
