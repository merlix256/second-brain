---
course: "SGDM (T1ASD1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: medium
tags:
  - study-unit
---

# 🔬 H13: Diffusie en Poedergebaseerde Processen
#theorie #diffusie #fick #arrhenius #sinteren #H13

[[00_Overview_Dashboard]] | [[01_Formularium_Master#3-diffusie--kinetica]] | [[05_Oefenzittingen/Sessie_03_Diffusie_en_Fasediagrammen]]

---

## 1. Atomaire Mechanismen van Diffusie
Diffusie is massatransport op atomaire schaal aangedreven door thermische energie en concentratiegradiënten:
* **Vacaturediffusie**: Atomen springen naar een naburige lege roosterplaats (dominant bij substitutionele atomen en autodiffusie).
* **Interstitiële diffusie**: Kleine atomen (C, N, H) bewegen door de holtes tussen de grotere roosteratomen.
  * *Vaste vuistregel*: Interstitiële diffusie verloopt **ordes van grootte sneller** dan vacaturediffusie omdat er oneindig veel lege interstitiële holtes zijn en de activeringsenergie $Q$ beduidend lager is.

---

## 2. De Wetten van Fick
* **Eerste Wet van Fick (Stationair / Steady-State)**:
  $$J = -D \frac{dC}{dx}$$
* **Tweede Wet van Fick (Niet-stationair)**:
  $$\frac{\partial C}{\partial t} = D \frac{\partial^2 C}{\partial x^2}$$
  Oplossing voor half-oneindig medium bij constante oppervlakteconcentratie $C_s$:
  $$\frac{C(x,t) - C_0}{C_s - C_0} = 1 - \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right)$$

---

## 3. Temperatuurafhankelijkheid (Arrhenius)
$$D = D_0 \exp\left(-\frac{Q}{RT}\right)$$
* Diffusie is een exponentieel temperatuursgeactiveerd proces. Een kleine stijging in $T$ leidt tot een gigantische toename in diffusiesnelheid.
* **Diffusiepaden**:
  $$D_{\text{oppervlak}} > D_{\text{korrelgrens}} > D_{\text{rooster/bulk}}$$
  Langs open korrelgrenzen en vrije oppervlakken is de activeringsenergie $Q$ veel lager!

---

## 4. Poederprocessen & Sinteren
* **Sinteren**: Verwarmen van gecompacteerd poeder ("groenling") tot onder het smeltpunt ($T \approx 0.7 - 0.9 T_m$).
* **Drijvende kracht**: Verlaging van de totale oppervlakte-vrije energie door het elimineren van vrije korreloppervlakken.
* **Stadia**:
  1. Halsvorming (neck formation) tussen poederdeeltjes via oppervlakte- en korrelgrensdiffusie.
  2. Krimp en afronding van poriën.
  3. Densificatie tot een vast, massief onderdeel.
* **Technologieën**: Sinteren, Hot Isostatic Pressing (HIP), Selective Laser Sintering (SLS / 3D-metaalprinten).

---

> [!summary] Hoofdstuksamenvatting
> Diffusie dicteert alle warmtebehandelingen, fasetransformaties en vaste-stoffusie (sinteren). Interstitiële diffusie van koolstof in ijzer verloopt veel sneller dan substitutionele diffusie.
