---
course: "Wiskundige basistechnieken (T1AWB1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.0
priority: medium
tags:
  - study-unit
---

# Active Recall Q&A — LinAlg Ch 06: Basis, Dimensie en Coördinaten

> [!question] Vraag 1: Hoe test je of een verzameling vectoren $\{\mathbf{u}_1, \mathbf{u}_2, \mathbf{u}_3\}$ in $\mathbb{R}^3$ een basis vormt?
> > [!success]- Antwoord & Uitwerking
> > Omdat $\dim(\mathbb{R}^3) = 3$ en de verzameling exact 3 vectoren bevat, volstaat het om te controleren of de vectoren lineair onafhankelijk zijn.
> > Dit kan door ze als kolommen in een matrix $A$ te plaatsen en te verifiëren dat $\det(A) \neq 0$ (of $\text{rang}(A) = 3$).
> > 🔗 **Theorie:** [[Ch 06 - Basis, Dimensie en Coördinaten#2. Basis en Dimensie]]

> [!question] Vraag 2: Wat is het voordeel van een orthonormale basis bij het bepalen van coördinaten?
> > [!success]- Antwoord & Uitwerking
> > Bij een willekeurige basis moet men een stelsel lineaire vergelijkingen oplossen. Bij een orthonormale basis $\{\mathbf{q}_1, \dots, \mathbf{q}_n\}$ is de $i$-de coördinaat rechtstreeks het inwendig product:
> > $$x_i = \langle \mathbf{v}, \mathbf{q}_i \rangle$$
> > 🔗 **Theorie:** [[Ch 06 - Basis, Dimensie en Coördinaten#4. Orthonormale Basissen en Gram-Schmidt]]
