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

# 🔬 H07: Kristallijne Structuren en Miller-indices
#theorie #kristallografie #miller-indices #KGV #KRG #HCP #H07

[[00_Overview_Dashboard]] | [[01_Formularium_Master]] | [[04_Theory_Notes/H11_Roosterdefecten_en_Verstevigingsmechanismen]]

---

## 1. De Drie Belangrijkste Metallische Kristalstructuren

| Eigenschap | KGV / FCC (Vlakgecentreerd Kubisch) | KRG / BCC (Ruimtelijk Gecentreerd) | DPH / HCP (Hexagonaal Dichtstgepakt) |
| :--- | :--- | :--- | :--- |
| **Eenheidscel Schets** | Atomen op hoekpunten + 6 vlakcentra | Atomen op hoekpunten + 1 centraal atoom | Boven/onder hexagonaal vlak + 3 tussenatomen |
| **Aantal atomen / cel ($n$)** | $8 \times \frac{1}{8} + 6 \times \frac{1}{2} = \mathbf{4}$ | $8 \times \frac{1}{8} + 1 = \mathbf{2}$ | $12 \times \frac{1}{6} + 2 \times \frac{1}{2} + 3 = \mathbf{6}$ |
| **Roosterconstante $a(R)$** | $a = 2\sqrt{2} R = \frac{4R}{\sqrt{2}}$ | $a = \frac{4R}{\sqrt{3}}$ | $a = 2R, \quad c \approx 1.633 a$ |
| **Coördinatiegetal (CN)** | **12** | **8** | **12** |
| **Atoompakkingsfactor (APF)**| **0.74** (dichtste stapeling) | **0.68** (losser/opener) | **0.74** (dichtste stapeling) |
| **Stapelvolgorde vlakken** | $ABCABC\dots$ langs $\{111\}$ | Geen dichtstgepakte vlakken | $ABABAB\dots$ langs $\{0001\}$ |
| **Voorbeelden** | $\text{Al}, \text{Cu}, \text{Ni}, \gamma\text{-Fe}, \text{Au}, \text{Ag}$ | $\alpha\text{-Fe}, \text{Cr}, \text{W}, \text{Mo}, \text{V}$ | $\text{Ti}, \text{Mg}, \text{Zn}, \text{Zr}$ |

```
        KGV (FCC)                            KRG (BCC)
      O---------O                          O---------O
     /|  O     /|                         /|        /|
    / |       / |                        / |   O    / |
   O---------O  |                       O---------O  |
   |O |   O  | O|                       |  |  (1) |  |
   |  O------|--O                       |  O------|--O
   | /       | /                        | /       | /
   O---------O                          O---------O
```

---

## 2. Kristallografische Richtingen $[uvw]$
1. Leg de oorsprong vast in een roosterhoekpunt.
2. Bepaal de coördinaten van het eindpunt min beginpunt van de richtingsvector in eenheden van de roosterparameters $a, b, c$.
3. Vermenigvuldig of deel met een gemeenschappelijke factor tot de **kleinste gehele getallen** zijn bekomen.
4. Schrijf tussen rechte haken: $[uvw]$ (negatieve waarden met een bovenstreep $[\bar{u}vw]$).
* Een familie van symmetrisch equivalente richtingen noteert men met haken: $\langle 100 \rangle$.

---

## 3. Kristallografische Vlakken en Miller-indices $(hkl)$
1. **Bepaal de snijpunten** van het vlak met de kristalassen $x, y, z$ in termen van eenheidscelribben $a, b, c$. (Als een vlak evenwijdig loopt met een as, is het snijpunt $\infty$).
2. **Neem de reciproke waarden** (omgekeerden) van deze snijpunten: $(1/x_1, 1/y_1, 1/z_1)$.
3. **Breng op gelijke noemer** en herleid tot de kleinste gehele getallen.
4. Plaats tussen ronde haken: $(hkl)$ (bijv. $(111)$, $(011)$, $(1\bar{1}0)$).
* Een familie van symmetrische vlakken noteert men met accolades: $\{111\}$.

> [!tip] Examentip Miller-indices
> Als het vlak door de oorsprong gaat, **moet je eerst de oorsprong verschuiven** naar een naburig hoekpunt van de eenheidscel alvorens de snijpunten te bepalen!

---

> [!summary] Hoofdstuksamenvatting
> KGV en DPH bereiken de maximale atomaire stapeling (APF = 0.74). De dichtstgepakte vlakken $\{111\}$ in KGV en de dichtstgepakte richtingen $\langle 110 \rangle$ vormen de primaire glijsystemen voor dislocaties.
