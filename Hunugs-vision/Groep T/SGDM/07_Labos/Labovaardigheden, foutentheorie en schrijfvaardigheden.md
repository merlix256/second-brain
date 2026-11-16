---
title: Labovaardigheden, foutentheorie en schrijfvaardigheden
course: "SGDM (T1ASD1)"
unit_type: labo
status: todo
completed: false
est_hours: 2.0
priority: high
tags:
  - study-unit
  - sgdm
  - labo
---

# 📏 Labovaardigheden, Foutentheorie & Schrijfvaardigheden

> [!warning] Grootste Puntenverliezer in SGDM-verslagen
> Correcte metingen leveren weinig op als **beduidende cijfers**, **eenheden** of **foutenvoortplanting** ontbreken!

---

## 📐 Kernformules Foutentheorie
1. **Gemiddelde en Standaardafwijking ($s$):**
   $$\bar{x} = \frac{1}{N}\sum_{i=1}^N x_i, \qquad s = \sqrt{\frac{1}{N-1}\sum_{i=1}^N (x_i - \bar{x})^2}$$
2. **Absolute Fout ($\Delta y$) en Relatieve Fout ($\frac{\Delta y}{|y|}$):**
   - **Som/Verschil ($y = a \pm b$):** Absolute fouten optellen:
     $$\Delta y = \Delta a + \Delta b \quad \text{(of kwadratisch: } \sqrt{\Delta a^2 + \Delta b^2}\text{)}$$
   - **Product/Quotiënt ($y = \frac{a \cdot b}{c}$):** Relatieve fouten optellen:
     $$\frac{\Delta y}{|y|} = \frac{\Delta a}{|a|} + \frac{\Delta b}{|b|} + \frac{\Delta c}{|c|}$$
   - **Macht ($y = a^n$):** $\frac{\Delta y}{|y|} = |n| \frac{\Delta a}{|a|}$ (bv. bij cirkeloppervlak $A = \frac{\pi d^2}{4}$ telt de fout op $d$ **dubbel** mee!).
3. **Afrondingsregels:**
   - Fout $\Delta y$ afronden op **1 (of max. 2) beduidende cijfers**.
   - Meetwaarde $y$ afronden op **dezelfde decimaal** als $\Delta y$! (Bv. $E = 208 \pm 6\text{ GPa}$, nooit $208.347 \pm 6.12\text{ GPa}$).

---

## ✍️ Schrijfvaardigheden Checklist
- [ ] Zakelijke, onpersoonlijke stijl (*"De trekproef werd uitgevoerd..."*, niet *"Wij deden..."*).
- [ ] Figuren hebben nummer + verklarend onderschrift **onder** de figuur; tabellen hebben nummer + titel **boven** de tabel.
- [ ] Elke variabele in formules gedefinieerd met symbool + SI-eenheid.
- [ ] Geen Excel-lijntjes tussen losse meetpunten zonder fysisch model (gebruik lineaire regressie in het elastisch gebied voor $E$-modulus!).

## 🔗 Navigatie
- [[sgdm_labs|← Terug naar SGDM Labo's]]
- [[Laboteksten en Verslagsjablonen SGDM]]
