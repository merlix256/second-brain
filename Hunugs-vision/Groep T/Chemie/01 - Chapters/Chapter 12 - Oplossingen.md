---
title: "Hoofdstuk 12: Fysische Eigenschappen van Oplossingen"
tags:
  - study-unit
  - chemie
  - oplossingen
  - concentraties
  - colligatieve-eigenschappen
course: "Chemie (T1ACH1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: high
---

# 🧪 Hoofdstuk 12: Fysische Eigenschappen van Oplossingen

> [!abstract] Kernconcept
> Een **oplossing** is een homogeen mengsel van twee of meer componenten. Oplosbaarheid wordt gedreven door intermoleculaire interacties en entropie. De aanwezigheid van opgeloste niet-vluchtige deeltjes wijzigt de fysische eigenschappen van het solvent fundamenteel: de **colligatieve eigenschappen**.

---

## 1. Oplossingsprocessen en Oplosbaarheid

### 1.1 Thermodynamica van Oplossen
Het oplossen van een opgeloste stof in een solvent bestaat conceptueel uit drie stappen:
1. Scheiding van solventmoleculen: $\Delta H_1 > 0$ (endotherm, overwinnen van solvent-solvent IMK).
2. Scheiding van solutedeeltjes: $\Delta H_2 > 0$ (endotherm, overwinnen van roosterenergie of solute IMK).
3. Vorming van solute-solvent interacties: $\Delta H_3 < 0$ (exotherm, solvatatie/hydratatie).

De totale oplossingsenthalpie bedraagt:
$$\Delta H_{\text{opl}} = \Delta H_1 + \Delta H_2 + \Delta H_3$$
- **"Soort zoekt soort" (*Similia similibus solvuntur*)**: Polaire/ionaire stoffen lossen op in polaire solventen (bijv. $\text{NaCl}$ in $\text{H}_2\text{O}$); apolaire stoffen in apolaire solventen (bijv. vetten in hexaan).

### 1.2 Invloed van Temperatuur en Druk op Oplosbaarheid
- **Vaste stoffen**: Oplosbaarheid stijgt meestal met temperatuur als $\Delta H_{\text{opl}} > 0$.
- **Gassen**: Oplosbaarheid van gassen in water daalt altijd bij stijgende temperatuur (ontsnappen van gasmoleculen).
- **Wet van Henry (Gasdruk)**:
  De oplosbaarheid ($c$) van een gas is direct evenredig met de partiële druk ($P$) van dat gas boven de oplossing:
  $$c = k_H \cdot P$$
  waarbij $k_H$ de constante van Henry is [$\text{mol}/(\text{L}\cdot\text{atm})$].

---

## 2. Concentratiematen

Kwantitatieve analyse vereist exacte concentratiedefinities:

| Concentratiemaat | Symbool | Definitieformule | Temperatuurafhankelijk? |
| :--- | :---: | :---: | :---: |
| **Molariteit** | $M$ | $M = \frac{n_{\text{solute}}}{V_{\text{oplossing}} \text{ (L)}}$ | **Ja** (volume expandeert bij verhitting) |
| **Molaliteit** | $m$ | $m = \frac{n_{\text{solute}}}{m_{\text{solvent}} \text{ (kg)}}$ | **Nee** (massa is temperatuuronafhankelijk) |
| **Molfractie** | $X_A$ | $X_A = \frac{n_A}{n_{\text{totaal}}}$ | **Nee** |
| **Massaprocent** | $\%(m/m)$| $\frac{m_{\text{solute}}}{m_{\text{totaal}}} \times 100\%$ | **Nee** |

Omrekening tussen $M$ en $m$ vereist altijd de **dichtheid ($\rho$)** van de oplossing!

---

## 3. Colligatieve Eigenschappen

> [!important] Definitie Colligatieve Eigenschappen
> Eigenschappen die uitsluitend afhangen van het **aantal opgeloste deeltjes** per volume-eenheid solvent, en **niet** van de chemische identiteit van de deeltjes.
> Voor elektrolyten die dissociëren in ionen vermenigvuldigen we met de **van 't Hoff factor ($i$)**:
> $$i = \frac{\text{werkelijk aantal deeltjes in oplossing}}{\text{aantal ingevoegde formule-eenheden}}$$
> (Voor glucose/ureum: $i = 1$; voor $\text{NaCl}$: $i \approx 2$; voor $\text{CaCl}_2$: $i \approx 3$).

### 3.1 Dampdrukverlaging (Wet van Raoult)
Niet-vluchtige solutedeeltjes aan het vloeistofoppervlak belemmeren verdamping van solventmoleculen:
$$P_{\text{opl}} = X_{\text{solvent}} \cdot P^\circ_{\text{solvent}}$$
$$\Delta P = P^\circ_{\text{solvent}} - P_{\text{opl}} = i \cdot X_{\text{solute}} \cdot P^\circ_{\text{solvent}}$$

### 3.2 Kookpuntsverhoging (Ebullioscopie)
Doordat de dampdruk verlaagd wordt, moet de temperatuur hoger stijgen om $P_{\text{damp}} = P_{\text{ext}}$ te bereiken:
$$\Delta T_b = i \cdot K_b \cdot m$$
waarbij $K_b$ de ebullioscopische constante van het solvent is [$\text{K}\cdot\text{kg}/\text{mol}$].

### 3.3 Vriespuntsverlaging (Cryoscopie)
Solutedeeltjes verstoren de ordening van het kristalrooster van het solvent tijdens bevriezing:
$$\Delta T_f = i \cdot K_f \cdot m$$
waarbij $K_f$ de cryoscopische constante van het solvent is (voor water: $K_f = 1.86\text{ }^\circ\text{C}\cdot\text{kg}/\text{mol}$).
Let op: $T_{f,\text{nieuw}} = T^\circ_f - \Delta T_f$.

### 3.4 Osmotische Druk ($\Pi$)
De hydrostatische druk vereist om de netto stroom van zuiver solvent door een semipermeabel membraan naar de geconcentreerde oplossing te stoppen:
$$\Pi = i \cdot M \cdot R \cdot T$$
waarbij $M$ de molaire concentratie is [$\text{mol/L}$], $R = 0.08206\text{ L}\cdot\text{atm}/(\text{mol}\cdot\text{K})$, en $T$ in Kelvin.
- **Isotonisch**: Gelijke osmotische druk.
- **Hypotonisch**: Lagere druk (veroorzaakt hemolyse bij rode bloedcellen).
- **Hypertonisch**: Hogere druk (veroorzaakt crenatie/uitdroging).

![[Colligative_Properties_Diagram.png]]

---

## 4. Colloïdale Dispersies
Tussenoplossing tussen echte homogene oplossingen ($< 1\text{ nm}$) en heterogene suspensies ($> 1000\text{ nm}$): colloïden ($1 - 1000\text{ nm}$).
- **Tyndall-effect**: Verstrooiing van zichtbaar licht door colloïdale deeltjes (bijv. koplampen in mist).

---

## 📝 Samenvatting
1. Oplosbaarheid volgt "soort zoekt soort"; gasoplosbaarheid volgt Henry's wet: $c = k_H P$.
2. Molariteit ($M$) hangt af van volume en $T$; Molaliteit ($m$) hangt af van massa solvent en is constant met $T$.
3. Colligatieve eigenschappen schalen met het deeltjesaantal via de van 't Hoff factor $i$.
4. De 4 colligatieve wetten: $\Delta P = i X_2 P_1^\circ$, $\Delta T_b = i K_b m$, $\Delta T_f = i K_f m$, en $\Pi = i M R T$.
