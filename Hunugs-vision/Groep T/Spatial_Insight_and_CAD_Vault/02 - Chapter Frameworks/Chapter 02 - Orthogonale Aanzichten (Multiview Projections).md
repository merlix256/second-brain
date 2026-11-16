---
title: Chapter 02 - Orthogonale Aanzichten (Multiview Projections)
tags:
  - study-unit
  - theory
  - chapter-note
  - orthogonal-views
course: "Ruimtelijk inzicht en CAD (T1AIB1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: medium
---

# 📖 Hoofdstuk 02: Orthogonale Aanzichten (Multiview Projections)

> [!abstract] Hoofdstuk Samenvatting
> Dit hoofdstuk behandelt de theorie en praktijk van parallelle loodrechte projectie (orthogonale projectie) om driedimensionale lichamen foutloos vast te leggen in tweedimensionale vlakken.

---

## 1. Projectietheorie
- **Orthogonale Projectie**: Projectiestralen lopen evenwijdig aan elkaar en loodrecht op het projectievlak.
  $$P_{xy}: (x, y, z) \mapsto (x, y, 0)$$
- **Projectiesystemen**:
  - **First Angle (Europese projectie)**: Het object bevindt zich tussen de waarnemer en het projectievlak.
  - **Third Angle (Amerikaanse projectie)**: Het projectievlak bevindt zich tussen de waarnemer en het object.
  - Verwijs naar [[Clip 02 - Projection Theory]] en [[Clip 06 - Projection Systems]].

## 2. Geometrische Elementen in Projectie
- **Punten**: Bepaald door cartesische coördinaten $(x,y,z)$.
- **Rechten**:
  - *Ware grootte (true length)*: Wanneer een rechte evenwijdig loopt aan het projectievlak.
  - *Verkorting (foreshortening)*: Wanneer een rechte een hoek maakt met het projectievlak.
  - *Puntprojectie*: Wanneer een rechte loodrecht op het projectievlak staat.
- **Vlakken**:
  - *Ware gedaante (true shape)*: Vlak evenwijdig aan het projectievlak.
  - *Lijnstuk (edge view)*: Vlak loodrecht op het projectievlak.
  - Zie [[Clip 03 - Projection of Geometric Elements]].

## 3. Aanzichten Tekenen & Keuze Vooraanzicht
- De zes hoofdprojectievlakken: Vooraanzicht (VA), Bovenaanzicht (BA), Linkeraanzicht (LA), Rechterkantzicht (RA), Onderaanzicht (OA), Achteraanzicht (AA).
- **Keuze van het Vooraanzicht**:
  - Moet het object tonen in zijn meest karakteristieke vorm en/of functionele gebruiksstand.
  - Moet het aantal onzichtbare lijnen in de aanzichten minimaliseren.
- **Projectie-uitlijning**:
  - Gebruik van een 45°-versteklijn (*miter line*) om dieptematen direct over te dragen tussen BA en LA/RA.
  - Zie [[Clip 04 - Draw Views]] en [[Clip 07 - Creating a Multiview Drawing]].

## 4. Overgangen en Afrondingen
- **Reële snijlijnen**: Scherpe hoeken $\rightarrow$ brede doorlopende lijn (Lijntype A).
- **Tangentiële overgangen**: Vloeiende overgang zonder knik $\rightarrow$ geen lijn!
- **Fictieve overgangslijnen**: Representeren virtuele snijdingspunten bij afgeronde hoeken $\rightarrow$ smalle doorlopende lijn (Lijntype B), die stopt vóór de contour.
- Zie [[Clip 05 - Tangential and Intersecting Transitions]].

## 5. Doorsnijdingen van Lichamen
- Snijlijnen van prisma's, cilinders en kegels.
- Bij cilinders met gelijke diameter die loodrecht snijden: snijlijn projecteert als twee rechte gekruiste lijnstukken.
- Zie [[Clip 08 - Intersecting Features and Bodies]].

## 6. Omwentelingslichamen & Bijzondere Aanzichten
- Gebruik van aslijnen/hartlijnen (smalle streep-stip lijn).
- Grondvormsymbolen ($\varnothing$, $\Box$) maken een tweede aanzicht vaak overbodig.
- Zie [[Clip 09 - Bodies of Revolution and Indication of Basic Shape]] en [[Clip 10 - Special Views]].

---

## 📌 Samenvatting
Orthogonale projectie combineert gekoppelde aanzichten volgens strikte afspraken (First Angle). Correcte aanzichtenkeuze, lijnsoorthiërarchie en maatprojectie via de versteklijn garanderen eenduidigheid.
