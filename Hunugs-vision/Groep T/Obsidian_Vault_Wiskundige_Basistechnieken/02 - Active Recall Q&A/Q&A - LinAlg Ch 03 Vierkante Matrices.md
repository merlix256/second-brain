---
title: "Q&A - LinAlg Ch 03: Vierkante Matrices en Determinanten"
course: "Wiskundige basistechnieken (T1AWB1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.0
priority: high
tags:
  - study-unit
  - wiskunde
  - active-recall
---

# Active Recall Q&A — LinAlg Ch 03: Vierkante Matrices en Determinanten

> [!question] Vraag 1: Hoe verandert $\det(A)$ bij elk van de drie elementaire rij-operaties voor een $n \times n$ matrix?
> > [!success]- Antwoord & Uitwerking
> > 1. $R_i \leftrightarrow R_j$: teken wisselt ($\times -1$).
> > 2. $R_i \leftarrow k R_i$ ($k \neq 0$): determinant wordt vermenigvuldigd met $k$.
> > 3. $R_i \leftarrow R_i + k R_j$: determinant blijft **onveranderd**!
> > 🔗 **Theorie:** [[Ch 03 - Vierkante Matrices en Determinanten#2.3 Eigenschappen van Determinanten]]

> [!question] Vraag 2: Zij $A \in \mathbb{R}^{3\times 3}$ met $\det(A) = 4$. Wat is $\det(2 A^{-1} A^T)$?
> > [!success]- Antwoord & Uitwerking
> > $$\det(2 A^{-1} A^T) = 2^3 \cdot \det(A^{-1}) \cdot \det(A^T) = 8 \cdot \frac{1}{4} \cdot 4 = 8$$
> > Let op de macht $2^n = 2^3 = 8$ omdat $A \in \mathbb{R}^{3\times 3}$!
> > 🔗 **Theorie:** [[Ch 03 - Vierkante Matrices en Determinanten#2.3 Eigenschappen van Determinanten]] • [[Bewijs 08 - Determinant van Reguliere Matrix en Inverse]]
