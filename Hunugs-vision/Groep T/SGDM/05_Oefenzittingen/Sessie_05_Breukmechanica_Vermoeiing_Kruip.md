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

# ⚙️ Oefenzitting 5: Breuk, Vermoeiing en Kruip
#oefenzitting #breukmechanica #vermoeiing #kruip #examen-focus

> [!info] Vereiste Theorie & Achtergrond
> Bestudeer eerst: [[04_Theory_Notes/H16_Breukmechanica_en_Taaiheid]], [[04_Theory_Notes/H17_Vermoeiing_en_Dynamische_Belasting]], [[04_Theory_Notes/H18_Tijdsafhankelijk_Gedrag_en_Kruip]]
> Formules: [[01_Formularium_Master#6-breukmechanica]] & [[01_Formularium_Master#7-vermoeiing-dynamische-belasting]]

---

### Opgave 1: Kritische Oppervlaktescheurgrootte in Hoogsterktestaal
Een hoogsterktestaal heeft een vloeigrens van $\sigma_y = 1460\text{ MPa}$ en een breuktaaiheid van $K_{Ic} = 98\text{ MPa}\sqrt{\text{m}}$.
Bereken de diepte van de kleinste oppervlaktescheur ($a_c$) die catastrofale brosse breuk veroorzaakt bij een aangelegde trekspanning van $50\%$ van de vloeigrens (neem meetfactor $Y = 1.0$).

#### 💡 Uitwerking:
1. **Aangelegde spanning**:
   $$\sigma = 0.50 \times \sigma_y = 0.50 \times 1460 = 730\text{ MPa}$$
2. **Kritische scheurlengte $a_c$**:
   $$K_{Ic} = Y \sigma \sqrt{\pi a_c} \implies a_c = \frac{1}{\pi} \left(\frac{K_{Ic}}{Y \sigma}\right)^2$$
   $$a_c = \frac{1}{\pi} \left(\frac{98}{1.0 \times 730}\right)^2 = \frac{1}{\pi} (0.13425)^2 = \frac{0.01802}{\pi} \approx \mathbf{5.74 \times 10^{-3}\text{ m}} = \mathbf{5.74\text{ mm}}$$

---

### Opgave 2: Keramische Oppervlaktedefecten (SiC vs $\text{ZrO}_2$)
Niet-destructief onderzoek garandeert dat een component geen oppervlaktedefecten groter dan $a = 25\,\mu\text{m} = 25 \times 10^{-6}\text{m}$ bevat ($Y = 1.12$).
Bereken de maximaal toelaatbare trekspanning $\sigma_{\max}$ voor:
1. Siliciumcarbide (SiC): $K_{Ic} = 3\text{ MPa}\sqrt{\text{m}}$
   $$\sigma_{\max} = \frac{K_{Ic}}{Y \sqrt{\pi a}} = \frac{3}{1.12 \times \sqrt{\pi \times 25 \times 10^{-6}}} = \frac{3}{1.12 \times 0.008862} \approx \mathbf{302\text{ MPa}}$$
2. Gestabiliseerd Zirconia ($\text{ZrO}_2$): $K_{Ic} = 9\text{ MPa}\sqrt{\text{m}}$
   $$\sigma_{\max} = \frac{9}{1.12 \times 0.008862} \approx \mathbf{907\text{ MPa}}$$
*Inzicht:* Dankzij transformatietaaiing heeft $\text{ZrO}_2$ een 3x hogere breuktaaiheid, waardoor het bij identieke defecten een **3x hogere veilige spanning** toelaat!

---

### Opgave 3: Vermoeiing & Wöhler Berekening
Een cilindrische as uit staal 1045 wordt symmetrisch wisselend belast ($R = -1$, dus $\sigma_m = 0$) met een krachtamplitude van $F_a = 66.7\text{ kN} = 66\,700\text{ N}$.
Uit de Wöhler-curve van staal 1045 blijkt dat de vermoeiingsgrens voor oneindige levensduur $\sigma_e = 300\text{ MPa}$ bedraagt.
**Bereken de minimale doorsnede $A$ om breuk te vermijden.**

#### 💡 Uitwerking:
$$\sigma_a = \frac{F_a}{A} \le \sigma_e \implies A \ge \frac{F_a}{\sigma_e} = \frac{66\,700\text{ N}}{300\text{ N/mm}^2} \approx \mathbf{222.33\text{ mm}^2}$$
De minimale diameter bedraagt:
$$d = \sqrt{\frac{4A}{\pi}} = \sqrt{\frac{4 \times 222.33}{\pi}} \approx \mathbf{16.8\text{ mm}}$$
