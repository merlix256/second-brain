---
title: "Hoofdstuk 11: Intermoleculaire Krachten en Vloeistoffen"
tags:
  - study-unit
  - chemie
  - IMK
  - waterstofbruggen
  - faseleer
course: "Chemie (T1ACH1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: high
---

# 💧 Hoofdstuk 11: Intermoleculaire Krachten en Fase-overgangen

> [!abstract] Kernconcept
> **Intermoleculaire krachten (IMK)** zijn aantrekkingskrachten *tussen* moleculen. Hoewel ze aanzienlijk zwakker zijn dan intramoleculaire chemische bindingen (covalente, ionaire bindingen: $100 - 1000\text{ kJ/mol}$), dicteren ze de macroscopische aggregatietoestand, kookpunten, viscositeit, dampdruk en oplosbaarheid.

---

## 1. Classificatie van Intermoleculaire Krachten

![[Slide_11_IMK_Overview.png]]

### 1.1 Ion-Dipool Krachten
- **Mechanisme**: Elektrostatische aantrekking tussen een volwaardig ion ($\text{Na}^+, \text{Cl}^-$) en de tegengestelde partiële lading van een permanent dipoolmolecule ($\text{H}_2\text{O}$).
- **Voorbeeld**: Hydratatiemantels rond zoutionen bij het oplossen in water:
$$\Delta H_{\text{hydratatie}} \propto \frac{q_{\text{ion}}}{r_{\text{ion}}}$$

### 1.2 Van der Waals Krachten

#### A. Dipool-Dipool Interacties
- Treden op tussen permanente dipoolmoleculen (polaire moleculen met een netto dipoolmoment $\mu > 0$).
- Oriëntatie-effect: $\delta^+$ trekt $\delta^-$ aan.
- **Voorbeeld**: $\text{HCl}\cdots\text{HCl}$, $\text{CH}_3\text{OCH}_3$ (dimethylether).

#### B. Waterstofbruggen (Speciaal geval van Dipool-Dipool)
> [!important] Randvoorwaarden voor een Waterstofbrug
> Een waterstofbrug ontstaat uitsluitend wanneer een waterstofatoom covalent gebonden is aan een **zeer elektronegatief, klein atoom met vrije elektronenparen**:
> $$\text{A}-\text{H} \cdots :\text{B} \quad (\text{waarbij A, B} \in \{\text{N, O, F}\})$$
> - **Oorzaak van extreme sterkte ($10 - 40\text{ kJ/mol}$)**:
>   1. Zeer groot elektronegativiteitsverschil ($\Delta \text{EN}$) genereert hoge partiële ladingen ($\delta^+ / \delta^-$).
>   2. Zeer kleine atoomstraal van $\text{H}$, waardoor de interactieafstand $r$ in Coulomb's wet ($F \propto \frac{q_1 q_2}{r^2}$) uiterst klein is.

![[Hydrogen_Bonding_Water.png]]

#### C. Dispersiekrachten (Londonkrachten)
- Treden op tussen **alle** atomen en moleculen (zowel apolair als polair).
- **Oorsprong**: Fluctuaties in de elektronenwolk induceren een kortstondig, tijdelijk dipoolmoment, dat op zijn beurt een geïnduceerd dipoolmoment opwekt in naburige moleculen.
- **Bepalende factoren**:
  1. **Polariseerbaarheid**: Hoe groter het aantal elektronen en hoe diffusier de elektronenwolk (grotere molaire massa), hoe gemakkelijker vervormbaar $\rightarrow$ sterkere London-dispersie. (Bijv. Kookpunt: $\text{He} < \text{Ne} < \text{Ar} < \text{Kr} < \text{Xe}$).
  2. **Moleculaire geometrie (contactoppervlak)**: Lineaire ketens hebben een groter contactoppervlak dan compacte, vertakte isomeren (bijv. $n$-pentaan kookt hoger dan neopentaan).

```
Interacting Particles Decision Tree:
[Ions involved?]
   ├── YES ──> [Polar molecules present?] ──> YES: Ion-Dipole (e.g. NaCl in H2O)
   │                                      └── NO:  Ionic Bond (e.g. NaCl lattice)
   └── NO  ──> [Polar molecules present?]
                 ├── YES ──> [H bonded to N, O, or F?] ──> YES: Hydrogen Bonding (H2O, HF)
                 │                                     └── NO:  Dipole-Dipole (HCl, CH3Cl)
                 └── NO  ──> London Dispersion Forces ONLY (CH4, CCl4, Ar)
```

---

## 2. Eigenschappen van Vloeistoffen

- **Oppervlaktespanning**: Energie vereist om het vloeistofoppervlak met één eenheid te vergroten. Moleculen aan het oppervlak ervaren een netto neerwaartse trekkracht door ontbrekende bovenburen.
- **Viscositeit**: Weerstand tegen stroming; stijgt bij sterkere IMK en langere polymeerketens.
- **Wateranomalie**:
  - Dichtheid van ijs is lager dan die van vloeibaar water door het open, hexagonale netwerk van 4 waterstofbruggen per $\text{H}_2\text{O}$-molecule.
  - Maximale dichtheid van vloeibaar water ligt bij **$3.98\text{ }^\circ\text{C}$**. Dit verklaart waarom meren van bovenaf bevriezen: water van $4\text{ }^\circ\text{C}$ zinkt naar de bodem, terwijl kouder water ($<4\text{ }^\circ\text{C}$) naar de oppervlakte stijgt en ijs vormt dat thermisch isoleert.

---

## 3. Faseovergangen en Dampdruk

### 3.1 Dynamisch Dampdrukevenwicht
In een gesloten vat stelt zich een dynamisch evenwicht in tussen verdamping en condensatie:
$$\text{Vloeistof} \rightleftharpoons \text{Damp}$$
De **dampdruk ($P_{\text{damp}}$)** is de druk van het gas in evenwicht met zijn vloeistof bij een specifieke temperatuur:
- Sterke IMK $\implies$ lage dampdruk, hoge verdampingsenthalpie ($\Delta H_{\text{vap}}$), hoog kookpunt.
- **Kookpunt**: Temperatuur waarbij de evenwichtsdampdruk exact gelijk is aan de externe omgevingsdruk. (Normaal kookpunt bij $P = 1\text{ atm}$).

### 3.2 Vergelijking van Clausius-Clapeyron
Het verband tussen dampdruk en absolute temperatuur $T$:
$$\ln(P) = -\frac{\Delta H_{\text{vap}}}{R} \cdot \frac{1}{T} + C$$
Voor twee meetpunten ($T_1, P_1$) en ($T_2, P_2$):
$$\ln\left(\frac{P_1}{P_2}\right) = \frac{\Delta H_{\text{vap}}}{R} \left( \frac{1}{T_2} - \frac{1}{T_1} \right)$$
waarbij $R = 8.314\text{ J}/(\text{mol}\cdot\text{K})$.

### 3.3 Fasediagrammen
Een fasediagram brengt de aggregatietoestanden in kaart als functie van $P$ en $T$:
- **Tripelpunt**: De unieke conditie ($T_{\text{tr}}, P_{\text{tr}}$) waar vast, vloeibaar en gas gelijktijdig in thermodynamisch evenwicht zijn.
- **Kritisch punt**: Boven de kritische temperatuur ($T_c$) en kritische druk ($P_c$) verdwijnt het meniscusvlak en ontstaat een **superkritisch fluïdum**.
- **Smeltcurve van Water**: Vertoont een **negatieve helling** ($\frac{dP}{dT} < 0$) omdat de vaste toestand (ijs) een groter specifiek volume heeft dan de vloeistof. Drukverhoging doet ijs smelten.

![[Phase_Diagram_Water_vs_CO2.png]]

---

## 📝 Samenvatting
1. Intermoleculaire krachten bepalen macroscopische vloeistof- en vaste-stofeigenschappen.
2. Krachtvolgorde: $\text{Ion-ion} > \text{Ion-dipool} > \text{Waterstofbrug} > \text{Dipool-dipool} \approx \text{Dispersie}$.
3. Waterstofbruggen vereisen $\text{H}$ covalent aan $\text{N, O, F}$ met vrije elektronenparen.
4. Clausius-Clapeyron correleert dampdruk $P$ met temperatuur via $\Delta H_{\text{vap}}$.
5. Water vertoont een uitzonderlijke negatieve smeltcurve in zijn fasediagram.
