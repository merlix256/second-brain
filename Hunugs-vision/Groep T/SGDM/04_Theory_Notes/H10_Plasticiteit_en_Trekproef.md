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

# 🔬 H10: Plasticiteit en de Trekproef
#theorie #plasticiteit #trekproef #luedersbanden #cottrell #versteviging #H10

[[00_Overview_Dashboard]] | [[01_Formularium_Master#2-plasticiteit-vervorming--hardheid]] | [[05_Oefenzittingen/Sessie_02_Sterkte_Plasticiteit_Hardheid]]

---

## 1. De Trekproef & Spanning-Rekkromme
In een gestandaardiseerde trekproef wordt een proefstaaf uniaxiaal uitgerekt tot breuk bij constante vervormingssnelheid:

```
 Spanning σ
     ^
 σUTS|                      ___ (Treksterkte)
     |                     /   \
  ReH|       _            /     \ (Insnoering / Necking)
     |      / \          /       \
  ReL|.....+---/\_/\_/\_/         * Breuk (εf)
     |    / (Lüdersbanden)
     |   /
     |  / (Lineair elastisch, helling E)
     +-----------------------------------> Rek ε
```

### Karakteristieke Grootheden:
* **Elasticiteitsgrens ($R_e$) of $0.2\%$-Rekgrens ($\sigma_{0.2}$)**: Spanning waarbij na ontlasting een blijvende plastische rek van exact $0.002$ ($0.2\%$) resteert.
* **Treksterkte ($\sigma_{\text{UTS}}$)**: De maximaal gedragen technische spanning ($\sigma_{\text{UTS}} = F_{\max} / A_0$).
* **Homogene rek ($\epsilon_u$)**: De uniforme plastische verlenging tot het punt $\sigma_{\text{UTS}}$.
* **Breukrek ($\epsilon_f$)**: Maatstaf voor de ductiliteit van het materiaal.

---

## 2. Vloeigebied, Lüdersbanden & Cottrell-wolken
In zacht koolstofstaal treedt een uitgesproken discontinu vloeiverschijnsel op met een **bovenste vloeigrens ($R_{eH}$)** en een **onderste vloeigrens ($R_{eL}$)**:
1. **Oorzaak (Microscopisch)**: Kleine interstitiële koolstof- en stikstofatomen diffunderen naar de gerekte roosterzone onder randdislocaties (de **Cottrell-wolk**). Hierdoor worden dislocaties verankerd ("gepind").
2. **Doorbreekgrens ($R_{eH}$)**: Om de dislocaties plotseling los te trekken uit deze potentiële energiedalletjes is een hoge initiële spanning vereist.
3. **Propagatie ($R_{eL}$)**: Eenmaal losgetrokken bewegen de vrije dislocaties met een veel lagere spanning voort. Dit manifesteert zich macroscopisch als zichtbare schuine rekbanden over het proefstuk: **Lüdersbanden**.
* **Oplossing in de industrie**: Staalplaten voor carrosserieën ondergaan vooraf een lichte koude walsstap ("skin pass" van ca. $1\%$) om alle dislocaties los te breken en vorming van oppervlaktefouten (sinaasappelhuid) tijdens dieptrekken te vermijden.

---

## 3. Rekversteviging & Wet van Ludwik / Hollomon
Na de uniforme vloeiing vereist verdere deformatie steeds hogere spanningen door vermenigvuldiging en interactie van dislocaties:
$$\sigma_w = K \cdot \epsilon_w^n$$
waarbij:
* $K$ = sterktecoëfficiënt (MPa)
* $n$ = verstevigingsexponent ($0 < n < 1$; typisch $0.15 - 0.50$ voor metalen)
* **Considère Criterium voor Insnoering**:
  Insnoering start wanneer de toename in ware spanning door oppervlakteverkleining de versteviging overtreft:
  $$\frac{d\sigma_w}{d\epsilon_w} = \sigma_w \implies \mathbf{\epsilon_{w,\text{insnoering}} = n}$$

---

> [!summary] Hoofdstuksamenvatting
> Plastische vervorming is het resultaat van collectieve dislocatiebeweging. De spanning-rekkromme toont achtereenvolgens elastisch gedrag, vloeien (eventueel met Lüdersbanden door Cottrell-wolken), uniforme versteviging en insnoering.
