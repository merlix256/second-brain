---
title: Formularium & Geometrische Regels
tags:
  - knowledge-base
  - formulas
  - math
  - geometry
---

# 📐 Formularium & Geometrische Regels

> [!abstract] Master Formularium
> Alle geometrische, wiskundige en normatieve formules voor **Ruimtelijk Inzicht en CAD**, voorzien van directe verwijzingen naar de theoriehoofdstukken.

---

## 1. Projectietransformaties & Coördinaten
Bij orthogonale parallelprojectie op de cartesische referentievlakken worden de 3D-coördinaten $(x, y, z)$ gereduceerd via orthogonale projectiematrices:

- **Vooraanzicht (Front View - $xz$-vlak)**:
  $$\mathbf{P}_{xz} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} x \\ 0 \\ z \end{pmatrix}$$
  *Uitleg*: [[Chapter 02 - Orthogonale Aanzichten (Multiview Projections)#1. Projectietheorie]] • [[Clip 02 - Projection Theory]]

- **Bovenaanzicht (Top View - $xy$-vlak)**:
  $$\mathbf{P}_{xy} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} x \\ y \\ 0 \end{pmatrix}$$
  *Uitleg*: [[Chapter 02 - Orthogonale Aanzichten (Multiview Projections)#1. Projectietheorie]] • [[Clip 04 - Draw Views]]

- **Linkeraanzicht (Side View - $yz$-vlak)**:
  $$\mathbf{P}_{yz} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 0 \\ y \\ z \end{pmatrix}$$
  *Uitleg*: [[Chapter 02 - Orthogonale Aanzichten (Multiview Projections)#1. Projectietheorie]] • [[Clip 04 - Draw Views]]

---

## 2. Ware Grootte en Hoekverkorting (Foreshortening)
Een rechte $L$ in de 3D-ruimte tussen punten $(x_1, y_1, z_1)$ en $(x_2, y_2, z_2)$:
$$L = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2 + (z_2 - z_1)^2}$$

Wanneer de rechte een hellingshoek $\theta$ maakt ten opzichte van een projectievlak, bedraagt de geprojecteerde lengte:
$$L_{\text{projectie}} = L \cdot \cos(\theta)$$

- Als $\theta = 0^\circ$: $L_{\text{projectie}} = L$ (**Ware Grootte / True Length**).
- Als $\theta = 90^\circ$: $L_{\text{projectie}} = 0$ (**Puntprojectie**).
*Uitleg*: [[Chapter 02 - Orthogonale Aanzichten (Multiview Projections)#2. Geometrische Elementen in Projectie]] • [[Clip 03 - Projection of Geometric Elements]]

---

## 3. Versteklijn (Miter Line) Meetkunde
De $45^\circ$-versteklijn verbindt het dieptecoördinaatverschil $\Delta y$ van het Bovenaanzicht met het Linkeraanzicht:
$$\Delta x_{\text{LA}} = \Delta y_{\text{BA}} \cdot \tan(45^\circ) = \Delta y_{\text{BA}}$$
*Uitleg*: [[Chapter 02 - Orthogonale Aanzichten (Multiview Projections)#3. Aanzichten Tekenen]] • [[Clip 04 - Draw Views]]

---

## 4. Papierformaten en Schaalwet (ISO 216)
Standaard ISO-A papierformaten bezitten de verhouding:
$$\frac{\text{Lengte}}{\text{Breedte}} = \sqrt{2} \approx 1.4142$$
Waarbij $A0$ een oppervlakte heeft van exact $1\text{ m}^2$:
$$x \cdot y = 1 \quad \text{en} \quad y = x\sqrt{2} \implies x = 0.841\text{ m}, \; y = 1.189\text{ m}$$

**Gestandaardiseerde Tekenschalen (ISO 5455)**:
- Vergroting: $50:1, \; 20:1, \; 10:1, \; 5:1, \; 2:1$
- Ware grootte: $1:1$
- Verkleining: $1:2, \; 1:5, \; 1:10, \; 1:20, \; 1:50, \; 1:100, \; 1:200$
*Uitleg*: [[Chapter 01 - Inleiding en Standaardisatie (ISO Normen)#2. ISO Standaarden als Referentiekader]]

---

## 5. Kegelsneden en Penetratiekrommen
Bij doorsnijding van een cilinder met diameter $d = 2r$ door een vlak onder hoek $\alpha$ met de rotatie-as:
- Als $\alpha = 90^\circ$: Snede is een **cirkel** met straal $r$.
- Als $0^\circ < \alpha < 90^\circ$: Snede is een **ellips** met:
  $$\text{Kleine as } b = 2r, \quad \text{Grote as } a = \frac{2r}{\sin(\alpha)}$$
*Uitleg*: [[Chapter 02 - Orthogonale Aanzichten (Multiview Projections)#5. Doorsnijdingen van Lichamen]] • [[Clip 08 - Intersecting Features and Bodies]]
