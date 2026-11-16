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

# 🔬 H03: De Opbouw van Materie: Atomen en Bindingen
#theorie #bindingen #kwantumgetallen #potentiaalput #H03

[[00_Overview_Dashboard]] | [[01_Formularium_Master]] | [[04_Theory_Notes/H02_Stijfheid_en_Elasticiteit]]

---

## 1. Atomaire Structuur & Kwantumgetallen
Elektronen bevinden zich in discrete energieniveaus beschreven door 4 kwantumgetallen:
1. **Hoofdkwantumgetal ($n = 1, 2, 3, \dots$)**: Bepaalt de hoofdschil en het voornaamste energieniveau.
2. **Nevenkwantumgetal ($l = 0, 1, \dots, n-1$)**: Bepaalt de vorm van de subschil ($s, p, d, f$).
3. **Magnetisch kwantumgetal ($m_l = -l, \dots, +l$)**: Ruimtelijke oriëntatie van het orbitaal ($2l + 1$ orbitalen).
4. **Spin-kwantumgetal ($m_s = \pm 1/2$)**: Eigen impuls van het elektron.
* **Pauli Uitsluitingsprincipe**: Geen twee elektronen in één atoom kunnen identieke vier kwantumgetallen hebben.

---

## 2. Typen Chemische Bindingen

| Bindingstype | Aard van de interactie | Karakteristieken | Voorbeelden |
| :--- | :--- | :--- | :--- |
| **Ionisch** | Elektrostatische Coulomb-aantrekking tussen ionen ($\Delta\text{EN} > 1.7$) | Niet-directioneel, hoge stijfheid, bros, lage geleiding | $\text{NaCl}, \text{Al}_2\text{O}_3, \text{ZrO}_2$ |
| **Covalent** | Gemeenschappelijk delen van elektronenparen ($\Delta\text{EN}$ klein) | Strikt directioneel, zeer hoge $E$ en smeltpunt, bros | Diamant, $\text{SiC}, \text{SiO}_2$ |
| **Metallisch** | Positieve atoomrompen in een delokaliseerde 'zee' van vrije valentie-elektronen | Niet-directioneel, uitstekende elektrische/thermische geleiding, ductiel | $\text{Fe}, \text{Al}, \text{Cu}$ |
| **Secundair (Van der Waals)** | Dipool-dipool interacties en dispersiekrachten | Zeer zwak ($< 40\text{ kJ/mol}$), lage $E$, laag smeltpunt | Tussen polymeerketens |

---

## 3. De Interatomaire Potentiaalkromme
De interactie-energie tussen twee atomen als functie van hun afstand $r$:
$$U(r) = U_{\text{aantrekking}}(r) + U_{\text{afstoting}}(r) = -\frac{A}{r^m} + \frac{B}{r^n} \quad (n > m)$$

```
 Energie U(r)
      ^
      |           /
      |          /   Afstoting
   0 -+---------+-----------------------> Afstand r
      |        / \
      |       /   \___ Aantrekking
 -U0 -+......* (Evenwichtsafstand r0)
      |   (Diepe put = hoog smeltpunt, hoge E-modulus)
```

* **Evenwichtsafstand ($r_0$)**: Waar de nettokracht $F(r) = -\frac{dU}{dr} = 0$.
* **Elasticiteitsmodulus ($E$)**: Rechtstreeks evenredig met de kromming op de bodem van de put:
  $$E \propto \left( \frac{d^2 U}{dr^2} \right)_{r = r_0}$$
  Een diepe, smalle potentiaalput betekent: **hoog smeltpunt $T_m$**, **hoge E-modulus** en **lage thermische expansie $\alpha$**!

---

> [!summary] Hoofdstuksamenvatting
> Primaire bindingen (ionisch, covalent, metallisch) bepalen de intrinsieke stijfheid en smelttemperatuur via de diepte en kromming van de interatomaire potentiaalput.
