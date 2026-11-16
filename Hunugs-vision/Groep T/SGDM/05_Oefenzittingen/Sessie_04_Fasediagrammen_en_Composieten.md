---
course: "SGDM (T1ASD1)"
unit_type: oefensessie
status: todo
completed: false
est_hours: 2.0
priority: high
tags:
  - study-unit
---

# ⚙️ Oefenzitting 4: Fasediagrammen en Composieten
#oefenzitting #fasediagrammen #hefboomregel #composieten

> [!info] Vereiste Theorie & Achtergrond
> Bestudeer eerst: [[04_Theory_Notes/H14_Fasetransformaties_en_Evenwichtsdiagrammen]] en [[04_Theory_Notes/H15_Artificiele_Materialen_en_Composieten]]
> Formules: [[01_Formularium_Master#4-fasenevenwichten--fasediagrammen]] & [[01_Formularium_Master#5-composieten-artificiële-materialen]]

---

### Opgave 1: Het $\text{MgO}-\text{Al}_2\text{O}_3$ Spinelsysteem
In het binaire $\text{MgO}-\text{Al}_2\text{O}_3$ systeem ontstaat de tussenfase spinel ($\text{MgAl}_2\text{O}_4$).
Bij $1600^\circ\text{C}$ zijn de evenwichtsfase-grenzen:
* Vaste oplossing van $\text{MgO}$: van 0 tot 5 wt% $\text{Al}_2\text{O}_3$
* Spinelfase ($\text{MgAl}_2\text{O}_4$): stabiel tussen 48 wt% en 62 wt% $\text{Al}_2\text{O}_3$
* $\text{Al}_2\text{O}_3$ vaste oplossing: vanaf 98 wt% $\text{Al}_2\text{O}_3$

**Vraag A:** Wat zijn de samenstelling en massafracties bij $1600^\circ\text{C}$ voor een mengsel met $C_0 = 40\text{ wt}\%\text{ Al}_2\text{O}_3$?
* Het mengsel ligt in het tweefasengebied $(\text{MgO}_{\text{ss}} + \text{Spinel})$.
* Grens 1 ($\text{MgO}_{\text{ss}}$): $C_{\text{MgO}} = 5\text{ wt}\%\text{ Al}_2\text{O}_3$
* Grens 2 (Spinel): $C_{\text{Spinel}} = 48\text{ wt}\%\text{ Al}_2\text{O}_3$
* **Hefboomregel**:
  $$W_{\text{MgO}} = \frac{48 - 40}{48 - 5} = \frac{8}{43} \approx \mathbf{18.6\%}$$
  $$W_{\text{Spinel}} = \frac{40 - 5}{48 - 5} = \frac{35}{43} \approx \mathbf{81.4\%}$$

---

### Opgave 2: Koolstofvezel-Versterkte Epoxy (CFRP)
Een unidirectionele composiet bestaat uit $V_f = 60\text{ vol}\%$ koolstofvezels ($E_f = 250\text{ GPa}, \sigma_f^* = 3000\text{ MPa}$) in een epoxymatrix ($E_m = 3.5\text{ GPa}, \sigma_m^* = 70\text{ MPa}$).
1. **Longitudinale stijfheid $E_{c,l}$ (Isostrain)**:
   $$E_{c,l} = V_f E_f + (1 - V_f) E_m = (0.60 \times 250) + (0.40 \times 3.5) = 150 + 1.4 = \mathbf{151.4\text{ GPa}}$$
2. **Transversale stijfheid $E_{c,t}$ (Isostress)**:
   $$E_{c,t} = \frac{E_f E_m}{V_f E_m + (1 - V_f) E_f} = \frac{250 \times 3.5}{(0.60 \times 3.5) + (0.40 \times 250)} = \frac{875}{2.1 + 100} = \frac{875}{102.1} \approx \mathbf{8.57\text{ GPa}}$$
*Inzicht:* De longitudinale modulus is bijna **18 keer hoger** dan de transversale modulus; dit illustreert de extreme anisotropie van unidirectionele composieten!
