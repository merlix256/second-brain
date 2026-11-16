---
title: "Q&A - LinAlg Ch 07: Beste Benadering en Orthogonale Projecties"
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

# Active Recall Q&A — LinAlg Ch 07: Beste Benadering en Orthogonale Projecties

> [!question] Vraag 1: Hoe bereken je de orthogonale projectie $\text{proj}_W(\mathbf{v})$ op een deelruimte $W$ met orthogonale basis $\{\mathbf{u}_1, \dots, \mathbf{u}_k\}$?
> > [!success]- Antwoord & Uitwerking
> > $$\text{proj}_W(\mathbf{v}) = \sum_{i=1}^k \frac{\langle \mathbf{v}, \mathbf{u}_i \rangle}{\langle \mathbf{u}_i, \mathbf{u}_i \rangle} \mathbf{u}_i$$
> > Als $\{\mathbf{u}_i\}$ **orthonormaal** is, valt de noemer weg ($\langle \mathbf{u}_i, \mathbf{u}_i \rangle = 1$). De foutvector $\mathbf{v} - \text{proj}_W(\mathbf{v})$ staat loodrecht op $W$ en heeft de kleinst mogelijke norm $\|\mathbf{v} - \mathbf{w}\|$ voor alle $\mathbf{w} \in W$.
> > 🔗 **Theorie:** [[Ch 07 - Beste Benadering en Orthogonale Projecties]]

> [!question] Vraag 2: Hoe pas je dit toe bij de kleinste-kwadratenmethode voor een overgedetermineerd stelsel $A\mathbf{x} = \mathbf{b}$?
> > [!success]- Antwoord & Uitwerking
> > Los de **normaalvergelijkingen** op:
> > $$A^T A \hat{\mathbf{x}} = A^T \mathbf{b}$$
> > Meetkundig is $A\hat{\mathbf{x}}$ precies de orthogonale projectie van $\mathbf{b}$ op de kolomruimte $\text{Col}(A)$.
> > 🔗 **Theorie:** [[Ch 07 - Beste Benadering en Orthogonale Projecties]]
