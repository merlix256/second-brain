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

# 🔬 H14: Fasetransformaties en Evenwichtsdiagrammen
#theorie #fasediagrammen #hefboomregel #Fe-C #staal #TTT #H14

[[00_Overview_Dashboard]] | [[01_Formularium_Master#4-fasenevenwichten--fasediagrammen]] | [[05_Oefenzittingen/Sessie_04_Fasediagrammen_en_Composieten]]

---

## 1. Fasen, Vrijheidsgraden & De Gibbs Fasenregel
* **Fase**: Een macroscopisch homogeen, fysisch en chemisch te onderscheiden deel van een materiaalsysteem.
* **Gibbs Fasenregel** (bij constante atmosferische druk $p = 1\text{ atm}$):
  $$F = C - P + 1$$
  waarbij:
  * $F$ = aantal thermodynamische vrijheidsgraden (temperatuur, fasensamenstellingen).
  * $C$ = aantal componenten (chemische elementen/verbindingen).
  * $P$ = aantal gelijktijdig aanwezige fasen.
  * In een 3-fasengebied van een binair systeem ($C=2, P=3$):
    $$F = 2 - 3 + 1 = \mathbf{0} \quad (\text{Invariant punt!})$$
    Temperatuur en samenstellingen van alle 3 de fasen liggen onwrikbaar vast!

---

## 2. Kwantitatieve Fasenanalyse: De Hefboomregel (Lever Rule)
In een tweefasengebied $(\alpha + \beta)$ met totale bulksamenstelling $C_0$:

```
      Tielijn bij constante T
      C_alpha           C_0             C_beta
   ------+---------------+---------------+------
         |<-   a   ->|   |<-   b   ->|
```

* **Samenstelling van elke fase**: rechtstreeks aflezen op de tielijn aan de fasengrenzen ($C_\alpha$ en $C_\beta$).
* **Relatieve hoeveelheid (massafractie)** via de hefboomregel (kruislingse hefboom):
  $$W_\alpha = \frac{C_\beta - C_0}{C_\beta - C_\alpha} = \frac{b}{a + b}$$
  $$W_\beta = \frac{C_0 - C_\alpha}{C_\beta - C_\alpha} = \frac{a}{a + b}$$

---

## 3. Belangrijke Invariante Reacties
1. **Eutecticum**: Vloeistof transformeert bij afkoeling simultaan in twee vaste fasen:
   $$L \xrightarrow{\text{stolling}} \alpha + \beta$$
2. **Eutectoïde**: Vaste fase ontleedt bij afkoeling in twee nieuwe vaste fasen:
   $$\gamma \xrightarrow{\text{afkoeling}} \alpha + \beta$$
3. **Peritecticum**: Vloeistof reageert met een reeds gestolde vaste fase tot een nieuwe vaste fase:
   $$L + \alpha \xrightarrow{\text{reactie}} \beta$$

---

## 4. Het IJzer-Koolstof ($\text{Fe}-\text{Fe}_3\text{C}$) Fasediagram
Het belangrijkste technische fasediagram in de metallurgie:

```
 T (°C)
 1538 |---(Liquid)
      |  \           /
 1147 |----\--------/---- (Eutectisch punt: 4.30 wt% C, L -> γ + Fe3C)
      |     \  γ   /
  912 |---   \    /
      |   \   \  /
  727 |----+---+--------- (Eutectoïde punt: 0.76 wt% C, γ -> α + Fe3C)
      | α  |       |
      +----+-------+-----> wt% C
         0.022   0.76    6.67 (Fe3C)
```

* **Microstructuren in Staal**:
  * **Ferriet ($\alpha$)**: KRG, zacht, ductiel, max $0.022\text{ wt}\%\text{ C}$.
  * **Austeniet ($\gamma$)**: KGV, ductiel, niet-magnetisch, max $2.14\text{ wt}\%\text{ C}$.
  * **Cementiet ($\text{Fe}_3\text{C}$)**: Intermetallische verbinding met exact $6.67\text{ wt}\%\text{ C}$, extreem hard en bros.
  * **Perliet**: Lamellaire mix van $\alpha$ en $\text{Fe}_3\text{C}$ (gevormd bij $0.76\text{ wt}\%\text{ C}$ onder $727^\circ\text{C}$).

---

## 5. Kinetica & TTT-diagrammen (Time-Temperature-Transformation)
Evenwichtsdiagrammen veronderstellen oneindig trage afkoeling. Bij reële afkoelsnelheden dicteert de kinetica de microstructuur:
* **Kiemvormingssnelheid ($\dot{N}$)**: Neemt toe naarmate de onderkoeling $\Delta T = T_e - T$ groter is.
* **Kiemgroeisnelheid ($\dot{G}$)**: Neemt exponentieel af bij lagere temperatuur door trage atomaire diffusie.
* **Resultaat**: De totale transformatiesnelheid bereikt een maximum bij tussenliggende temperaturen $\implies$ **C-vormige neus** in het TTT-diagram!
* **Martensiet**: Bij extreem snel afschrikken ("quenching") ontbreekt de tijd voor C-diffusie. Het KGV-rooster klapt diffusieloos afschuivend om naar een oververzadigd ruimtelijk tetragonale structuur (BCT). Martensiet is extreem hard en bros. Door **ontlaten** (temperen) rond $200 - 600^\circ\text{C}$ wordt spanning verlicht en taaiheid herwonnen.

---

> [!summary] Hoofdstuksamenvatting
> De hefboomregel berekent de fasehoeveelheden in tweefasengebieden. In staal stuurt de afkoelsnelheid of men zacht perliet, taai bainiet of keihard martensiet vormt.
