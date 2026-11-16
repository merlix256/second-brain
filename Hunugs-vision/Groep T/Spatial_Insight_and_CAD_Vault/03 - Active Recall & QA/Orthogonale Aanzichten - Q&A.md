---
title: Active Recall Q&A - Orthogonale Aanzichten
tags:
  - study-unit
  - active-recall
  - flashcards
  - orthogonal-views
course: "Ruimtelijk inzicht en CAD (T1AIB1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.0
priority: medium
---

# 🧠 Active Recall Q&A: Orthogonale Aanzichten

> [!tip] Instructie voor Zelfoverhoring
> Klap de callouts uit om het modelantwoord en de theorieverwijzing te bekijken. Gebruik deze vragen voor spaced repetition.

---

### Vraag 1: Wat zijn de fundamentele eigenschappen van een orthogonale parallelprojectie?
> [!question]- Klik voor Antwoord & Uitleg
> **Antwoord**: 
> 1. Alle projectiestralen lopen onderling strikt evenwijdig.
> 2. Alle projectiestralen vallen loodrecht ($90^\circ$) in op het projectievlak.
> Hierdoor blijven evenwijdige lijnen in de ruimte ook evenwijdig in de projectie, en behouden vlakken evenwijdig aan het projectievlak hun ware vorm en afmetingen.
> **Theorie Backlink**: [[Chapter 02 - Orthogonale Aanzichten (Multiview Projections)#1. Projectietheorie]] • [[Clip 02 - Projection Theory]]

---

### Vraag 2: Hoe liggen de aanzichten gerangschikt volgens de First Angle (Europese) projectiemethode?
> [!question]- Klik voor Antwoord & Uitleg
> **Antwoord**:
> Uitgaande van het **Vooraanzicht (VA)** in het midden:
> - **Bovenaanzicht (BA)**: bevindt zich *onder* het VA.
> - **Onderaanzicht (OA)**: bevindt zich *boven* het VA.
> - **Linkeraanzicht (LA)**: bevindt zich *rechts* van het VA (kijk vanaf links, projecteer naar rechts).
> - **Rechterkantzicht (RA)**: bevindt zich *links* van het VA.
> - **Achteraanzicht (AA)**: bevindt zich uiterst rechts (of links).
> **Theorie Backlink**: [[ISO Tekennormen & Lijnsoorten#Projectiesystemen]] • [[Clip 06 - Projection Systems]]

---

### Vraag 3: Wanneer vertoont een 3D-rechte zich in "Ware Grootte" op een aanzicht?
> [!question]- Klik voor Antwoord & Uitleg
> **Antwoord**:
> Een rechte wordt uitsluitend in ware grootte (lengte $L$) afgebeeld wanneer zij strikt evenwijdig loopt aan het desbetreffende projectievlak. Zodra de rechte een hoek $\theta > 0^\circ$ maakt met het projectievlak, is de geprojecteerde lengte verkort volgens:
> $$L_{\text{proj}} = L \cdot \cos(\theta)$$
> Staat de rechte loodrecht op het vlak ($\theta = 90^\circ$), dan projecteert zij als een enkel punt.
> **Theorie Backlink**: [[Chapter 02 - Orthogonale Aanzichten (Multiview Projections)#2. Geometrische Elementen in Projectie]] • [[Clip 03 - Projection of Geometric Elements]]

---

### Vraag 4: Hoe worden overgangen bij afrondingen (fillets) aangeduid volgens ISO-conventies?
> [!question]- Klik voor Antwoord & Uitleg
> **Antwoord**:
> - Echte scherpe snijdingsranden krijgen een brede volle lijn (Lijntype A).
> - Bij zuiver tangentiële overgangen wordt *geen* lijn getekend.
> - Indien een virtuele snijlijn ter verduidelijking gewenst is, gebruikt men een **smalle volle lijn (Lijntype B)** die *stopt vóór* de begrenzende contourlijnen (fictieve overgangslijn).
> **Theorie Backlink**: [[Chapter 02 - Orthogonale Aanzichten (Multiview Projections)#4. Overgangen en Afrondingen]] • [[Clip 05 - Tangential and Intersecting Transitions]]

---

### Vraag 5: Wat is de wiskundige functie van de 45°-versteklijn (miter line)?
> [!question]- Klik voor Antwoord & Uitleg
> **Antwoord**:
> De versteklijn onder $45^\circ$ maakt een directe, foutloze geometrische transformatie mogelijk van de dieptemaat ($y$-as) tussen het Bovenaanzicht en het Linker-/Rechterkantzicht zonder handmatig te hoeven meten:
> $$\Delta x_{\text{zij}} = \Delta y_{\text{boven}} \cdot \tan(45^\circ) = \Delta y_{\text{boven}}$$
> **Theorie Backlink**: [[Formularium & Geometrische Regels#Versteklijn (Miter Line) Meetkunde]] • [[Clip 04 - Draw Views]]
