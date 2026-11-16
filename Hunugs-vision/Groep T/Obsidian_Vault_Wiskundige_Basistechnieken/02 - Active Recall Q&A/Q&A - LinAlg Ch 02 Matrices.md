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

# Active Recall Q&A — LinAlg Ch 02: Matrices en Echelonvormen

> [!question] Vraag 1: Wat is het verschil tussen een echelonvorm (REF) en de canonieke echelonvorm (RREF)?
> > [!success]- Antwoord & Uitwerking
> > - In een REF zijn alle elementen onder de spilelementen nul en schuiven spilelementen naar rechts. Er zijn oneindig veel echelonvormen.
> > - In een RREF zijn bovendien alle spilelementen genormaliseerd naar $1$ én zijn de elementen *boven* de spilelementen ook nul. De canonieke echelonvorm is wiskundig **uniek**.
> > 🔗 **Theorie:** [[Ch 02 - Matrices en Echelonvormen#3. Rij-echelonvormen en Rang]]

> [!question] Vraag 2: Waarom geldt voor twee matrices in het algemeen $(AB)^T = B^T A^T$ en niet $A^T B^T$?
> > [!success]- Antwoord & Uitwerking
> > Bij matrixvermenigvuldiging worden de rijen van $A$ vermenigvuldigd met de kolommen van $B$. Door te transponeren worden kolommen van $B$ de rijen van $B^T$, waardoor $B^T$ vooraan moet staan opdat de binnenafmetingen overeenkomen en de componenten $(AB)^T_{ij} = (AB)_{ji} = \sum A_{jk} B_{ki} = \sum B^T_{ik} A^T_{kj} = (B^T A^T)_{ij}$ kloppen.
> > 🔗 **Theorie:** [[Ch 02 - Matrices en Echelonvormen#1. Definities en Matrixbewerkingen]]
