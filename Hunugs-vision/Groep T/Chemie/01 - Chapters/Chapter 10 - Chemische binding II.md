---
title: "Hoofdstuk 10: Chemische Binding II - Moleculaire Geometrie en Hybridisatie"
tags:
  - study-unit
  - chemie
  - VSEPR
  - hybridisatie
  - dipoolmoment
course: "Chemie (T1ACH1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: high
---

# 📐 Hoofdstuk 10: Moleculaire Geometrie en Hybridisatie

> [!abstract] Kernconcept
> De driedimensionale ruimtelijke rangschikking van atomen in een molecuul dicteert fysische eigenschappen zoals polariteit en spectroscopisch gedrag. Deze vorm wordt voorspeld met het **VSEPR-model** en gekoppeld aan kwantummechanische golffuncties via **orbitaalhybridisatie**.

---

## 1. Het VSEPR Model

Het **Valence Shell Electron Pair Repulsion (VSEPR)** model stelt dat elektronenparen (bindend en niet-bindend) rond een centraal atoom zich in de 3D-ruimte zodanig oriënteren dat de onderlinge elektrostatische afstoting geminimaliseerd wordt.

### 1.1 Sterisch Getal ($SN$) en Afstotingshiërarchie
$$SN = (\text{aantal gebonden atomen}) + (\text{aantal vrije elektronenparen op centraal atoom})$$

> [!warning] Afstotingshiërarchie
> Niet-bindende vrije elektronenparen (lone pairs, LP) nemen meer ruimte in beslag dan bindende paren (bonding pairs, BP):
> $$\text{LP - LP} > \text{LP - BP} > \text{BP - BP}$$
> Dit verklaart waarom de bindingshoeken in water ($\text{H}_2\text{O}$, 2 LP) worden samengedrukt tot $104.5^\circ$ vergeleken met methaan ($\text{CH}_4$, $109.5^\circ$).

### 1.2 Geometrie Overzichtstabel

| $SN$ | Elektronenpaar-geometrie | Vrije paren | Moleculaire geometrie | Ideale hoek | Voorbeeld |
| :---: | :--- | :---: | :--- | :---: | :--- |
| **2** | Lineair | 0 | **Lineair** | $180^\circ$ | $\text{BeCl}_2, \text{CO}_2$ |
| **3** | Trigonaal planair | 0 | **Trigonaal planair** | $120^\circ$ | $\text{BF}_3$ |
| **3** | Trigonaal planair | 1 | **Geknikt (Bent)** | $<120^\circ$ | $\text{SO}_2, \text{NO}_2^-$ |
| **4** | Tetraëdrisch | 0 | **Tetraëdrisch** | $109.5^\circ$ | $\text{CH}_4$ |
| **4** | Tetraëdrisch | 1 | **Trigonale piramide** | $107^\circ$ | $\text{NH}_3$ |
| **4** | Tetraëdrisch | 2 | **Geknikt (Bent)** | $104.5^\circ$ | $\text{H}_2\text{O}$ |
| **5** | Trigonaal bipiramidaal | 0 | **Trigonaal bipiramidaal**| $90^\circ, 120^\circ$ | $\text{PCl}_5$ |
| **5** | Trigonaal bipiramidaal | 1 | **Wip (Seesaw)** | $<90^\circ, <120^\circ$| $\text{SF}_4$ |
| **5** | Trigonaal bipiramidaal | 2 | **T-vormig** | $<90^\circ$ | $\text{ClF}_3$ |
| **5** | Trigonaal bipiramidaal | 3 | **Lineair** | $180^\circ$ | $\text{I}_3^-, \text{XeF}_2$ |
| **6** | Octaëdrisch | 0 | **Octaëdrisch** | $90^\circ$ | $\text{SF}_6$ |
| **6** | Octaëdrisch | 1 | **Vierkante piramide** | $<90^\circ$ | $\text{BrF}_5$ |
| **6** | Octaëdrisch | 2 | **Vierkant planair** | $90^\circ$ | $\text{XeF}_4$ |

*Regel voor $SN=5$*: Vrije elektronenparen bezetten altijd de **equatoriale** posities om $90^\circ$ afstotingen te minimaliseren!

![[VSEPR_Geometries_Comprehensive.png]]

---

## 2. Moleculaire Polariteit en Dipoolmoment

Een binding is polair als $\Delta \text{EN} > 0.4$. Het netto **dipoolmoment ($\mu$)** is de vectoriële som van alle individuele bindingsdipolen:
$$\vec{\mu} = \sum q_i \cdot \vec{r}_i$$
- Een molecuul kan polaire bindingen bevatten maar macroscopisch **apolair** zijn door ruimtelijke symmetrie (bijv. $\text{CO}_2, \text{CCl}_4, \text{BF}_3, \text{SF}_6 \implies \vec{\mu} = 0$).
- Asymmetrische moleculen met netto ladingsverschuiving zijn **polair** (bijv. $\text{H}_2\text{O}, \text{NH}_3, \text{CHCl}_3 \implies \vec{\mu} > 0$).

---

## 3. Valentiebindingstheorie en Hybridisatie

Atomaire orbitalen mengen tot nieuwe equivalente **hybride orbitalen** gericht op optimale overlapping.

### 3.1 Overzicht van Hybridisatietoestanden

| Sterisch getal ($SN$) | Hybridisatie | Geometrie hybriden | Max $\sigma$-bindingen | Vrije $p$-orbitalen (voor $\pi$) |
| :---: | :---: | :--- | :---: | :---: |
| **2** | $sp$ | Lineair ($180^\circ$) | 2 | 2 (geschikt voor twee $\pi$) |
| **3** | $sp^2$ | Trigonaal planair ($120^\circ$) | 3 | 1 (geschikt voor één $\pi$) |
| **4** | $sp^3$ | Tetraëdrisch ($109.5^\circ$) | 4 | 0 |
| **5** | $sp^3d$ | Trigonaal bipiramidaal | 5 | 0 (deelname $d$-orbitaal) |
| **6** | $sp^3d^2$ | Octaëdrisch | 6 | 0 (deelname $d$-orbitalen) |

### 3.2 Sigma ($\sigma$) en Pi ($\pi$) Bindingen
- **$\sigma$-binding**: Axiale kop-aan-kop overlapping met elektronendichtheid symmetrisch langs de bindingsas (sterk, vrije rotatie mogelijk).
- **$\pi$-binding**: Laterale zijdelingse overlapping van ongehybridiseerde parallelle $p$-orbitalen boven en onder de kernas (zwakker dan $\sigma$, blokkeert rotatie $\implies$ cis/trans isomerie).
  - Enkele binding = $1\sigma$
  - Dubbele binding = $1\sigma + 1\pi$
  - Drievoudige binding = $1\sigma + 2\pi$

![[Hybridization_Ethylene_Acetylene.png]]

---

## 📝 Samenvatting
1. VSEPR voorspelt 3D-vormen via minimalisatie van elektronenafstoting ($LP-LP > LP-BP > BP-BP$).
2. Een molecuul is polair als de vectoriële som van de bindingsdipoolmomenten niet nul is.
3. Hybridisatie verklaart waargenomen bindingshoeken: $SN=2 \rightarrow sp$, $SN=3 \rightarrow sp^2$, $SN=4 \rightarrow sp^3$.
4. Dubbele bindingen bestaan uit $1\sigma + 1\pi$; drievoudige uit $1\sigma + 2\pi$.
