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

# Bewijs 08: Determinant van een Reguliere Matrix en Inverse

> [!abstract] Context & Examenbelang
> **Theorievraag 8:** *"Bewijs welke waarden $|A|$ kan aannemen en hoe $|A^{-1}|$ in verband staat met $|A|$ indien $A \in \mathbb{R}^{n \times n}$ een reguliere matrix is."*
> **Verwante Theorie:** [[Ch 03 - Vierkante Matrices en Determinanten#2. Determinanten en Eigenschappen]]
> **Formularium:** [[Formularium#2. Lineaire Algebra]] | **MOC:** [[00 - Index der Bewijzen]]

---

## 1. Formulering van de Stelling
Zij $A \in \mathbb{R}^{n \times n}$ een reguliere (inverteerbare) vierkante matrix. Dan geldt:
1. De determinant van $A$ is strikt verschillend van nul:
   $$|A| \neq 0 \quad (\text{of } \det(A) \neq 0)$$
2. De determinant van de inverse matrix $A^{-1}$ is het omgekeerde van de determinant van $A$:
   $$|A^{-1}| = \frac{1}{|A|}$$

---

## 2. Stap-voor-stap Bewijs

### Stap 1: Uitgangspunt via de Definitie van de Inverse Matrix
Omdat de matrix $A$ regulier is, bestaat per definitie de inverse matrix $A^{-1}$ zodanig dat:
$$A A^{-1} = I_n$$
waarbij $I_n$ de $n \times n$ eenheidsmatrix voorstelt.

### Stap 2: Toepassen van de Determinantfunctie
We nemen de determinant van beide leden:
$$\det(A A^{-1}) = \det(I_n)$$
We weten dat de determinant van de eenheidsmatrix gelijk is aan 1:
$$\det(I_n) = 1$$
Bijgevolg geldt:
$$\det(A A^{-1}) = 1$$

### Stap 3: Multiplicatieve Eigenschap van Determinanten
Volgens de fundamentele multiplicatieve stelling voor determinanten (de stelling van Binet-Cauchy) is de determinant van een product van twee vierkante matrices gelijk aan het product van hun respectievelijke determinanten:
$$\det(A B) = \det(A) \cdot \det(B)$$
Toepassing op ons product levert:
$$\det(A) \cdot \det(A^{-1}) = 1 \quad \text{of in notatie met rechte strepen:} \quad |A| \cdot |A^{-1}| = 1$$

### Stap 4: Bewijs dat $|A| \neq 0$
De gelijkheid $|A| \cdot |A^{-1}| = 1$ stelt een product voor van twee reële getallen $|A|$ en $|A^{-1}|$ dat gelijk is aan 1.
Indien $|A| = 0$ zou zijn, dan zou:
$$0 \cdot |A^{-1}| = 0 \neq 1$$
wat tot een contradictie leidt.
Bijgevolg kan $|A|$ nooit gelijk zijn aan nul:
$$|A| \neq 0$$
(Evenzo is $|A^{-1}| \neq 0$).

### Stap 5: Verband tussen $|A^{-1}|$ en $|A|$
Omdat we zojuist bewezen hebben dat $|A| \neq 0$, mogen we beide leden van de gelijkheid $|A| \cdot |A^{-1}| = 1$ delen door $|A|$:
$$|A^{-1}| = \frac{1}{|A|} \quad \blacksquare$$

---

## 3. Examenvalkuilen & Uitbreidingen
- **Waarom $|A| \neq 0$ eerst bewijzen?** Je mag pas door $|A|$ delen nàdat je rigoureus hebt beargumenteerd dat $|A| \neq 0$ (omdat het product gelijk is aan 1). Een deling door nul is niet gedefinieerd.
- **Orthogonale Matrices:** Als $A$ een orthogonale matrix is ($A^T A = I_n$), dan is $A^{-1} = A^T$. Omdat $|A^T| = |A|$, geldt $|A|^2 = 1 \implies |A| = \pm 1$.
