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

# Active Recall Q&A — Meetkunde Ch 01: Getallen, Punten en Vectoren

> [!question] Vraag 1: Hoe definieer je de Euclidische afstand tussen twee punten $P(1, 2)$ en $Q(-3, 1)$?
> > [!success]- Antwoord & Uitwerking
> > De afstand is de norm van de verschilvector $\mathbf{q} - \mathbf{p}$:
> > $$d(P, Q) = \|\mathbf{q} - \mathbf{p}\| = \sqrt{(-3 - 1)^2 + (1 - 2)^2} = \sqrt{(-4)^2 + (-1)^2} = \sqrt{16 + 1} = \sqrt{17}$$
> > 🔗 **Theorie:** [[Ch 01 - Getallen, Punten en Vectoren#2.2 Lengte (Norm) en Afstand]]

> [!question] Vraag 2: Voor welke $k \in \mathbb{R}$ staan de vectoren $\mathbf{u} = [1, k-1]^T$ en $\mathbf{v} = [2k, 2]^T$ orthogonaal op elkaar?
> > [!success]- Antwoord & Uitwerking
> > Twee vectoren zijn orthogonaal als en slechts als hun scalair product nul is:
> > $$\mathbf{u} \cdot \mathbf{v} = 0 \iff 1 \cdot (2k) + (k - 1) \cdot 2 = 0$$
> > $$2k + 2k - 2 = 0 \iff 4k = 2 \iff k = \frac{1}{2}$$
> > 🔗 **Theorie:** [[Ch 01 - Getallen, Punten en Vectoren#2.3 Hoek en Scalair Product in R2]]

> [!question] Vraag 3: Hoe bereken je de orthogonale projectie van $\mathbf{u}$ op een niet-nul vector $\mathbf{v}$?
> > [!success]- Antwoord & Uitwerking
> > De projectievector wordt gegeven door:
> > $$\text{proj}_{\mathbf{v}}(\mathbf{u}) = \left( \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|^2} \right) \mathbf{v}$$
> > Dit representeert de schaduw van $\mathbf{u}$ op de drager van $\mathbf{v}$.
> > 🔗 **Theorie:** [[Ch 01 - Getallen, Punten en Vectoren#3. Orthogonale Projectie in R2]]
