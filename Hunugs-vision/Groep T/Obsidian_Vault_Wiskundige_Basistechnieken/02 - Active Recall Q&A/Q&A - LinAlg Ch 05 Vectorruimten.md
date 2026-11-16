---
title: "Q&A - LinAlg Ch 05: Vectorruimten en Inproductruimten"
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

# Active Recall Q&A — LinAlg Ch 05: Vectorruimten en Inproductruimten

> [!question] Vraag 1: Wat zijn de 3 snelle voorwaarden om na te gaan of $W \subseteq V$ een deelruimte is?
> > [!success]- Antwoord & Uitwerking
> > 1. **Nulvector:** $\mathbf{0} \in W$ (snelle test: check dit altijd eerst!).
> > 2. **Gesloten onder optelling:** $\mathbf{u}, \mathbf{v} \in W \implies \mathbf{u} + \mathbf{v} \in W$.
> > 3. **Gesloten onder scalaire vermenigvuldiging:** $\alpha \in \mathbb{R}, \mathbf{u} \in W \implies \alpha \mathbf{u} \in W$.
> > 🔗 **Theorie:** [[Ch 05 - Vectorruimten en Inproductruimten]]

> [!question] Vraag 2: Geef de ongelijkheid van Cauchy-Schwarz en wanneer geldt gelijkheid?
> > [!success]- Antwoord & Uitwerking
> > $$|\langle \mathbf{u}, \mathbf{v} \rangle| \le \|\mathbf{u}\| \cdot \|\mathbf{v}\|$$
> > Gelijkheid geldt $\iff \mathbf{u}$ en $\mathbf{v}$ zijn **lineair afhankelijk** (evenwijdig).
> > 🔗 **Bewijs:** [[Bewijs 05 - Ongelijkheid van Cauchy-Schwarz]] • **Theorie:** [[Ch 05 - Vectorruimten en Inproductruimten]]
