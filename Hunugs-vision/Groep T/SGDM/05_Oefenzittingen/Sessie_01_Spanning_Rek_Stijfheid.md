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

# ⚙️ Oefenzitting 1: Spanning, Rek en Stijfheid
#oefenzitting #mechanica #elasticiteit

> [!info] Vereiste Theorie & Achtergrond
> Bestudeer eerst: [[04_Theory_Notes/H02_Stijfheid_en_Elasticiteit]]
> Relevante formules: [[01_Formularium_Master#1-stijfheid-spanning--rek]]

---

### Opgave 1: Betonnen Kolom onder Druk
Een betonnen kolom ($E = 30\text{ GPa} = 30\,000\text{ MPa}$) met rechthoekige doorsnede van $250\text{ mm} \times 375\text{ mm}$ wordt axiaal belast met een neerwaartse drukkracht van $F = 900\text{ kN} = 900\,000\text{ N}$.
1. Bereken de normaalspanning $\sigma$ op de dwarsdoorsnede.
2. Bereken de resulterende rek $\epsilon$ (veronderstel zuiver elastisch gedrag).

#### 💡 Uitwerking:
1. **Oppervlakte $A_0$**:
   $$A_0 = 250\text{ mm} \times 375\text{ mm} = 93\,750\text{ mm}^2$$
2. **Normaalspanning $\sigma$**:
   $$\sigma = \frac{-F}{A_0} = \frac{-900\,000\text{ N}}{93\,750\text{ mm}^2} = \mathbf{-9.60\text{ MPa}} \quad (\text{drukspanning})$$
3. **Rek $\epsilon$ via de wet van Hooke**:
   $$\epsilon = \frac{\sigma}{E} = \frac{-9.60\text{ MPa}}{30\,000\text{ MPa}} = \mathbf{-3.20 \times 10^{-4}} = \mathbf{-0.032\%}$$

---

### Opgave 2: Spanningen onder een Schuine Hoek
Een kubisch blokje met ribbe $10\text{ mm} \times 10\text{ mm} \times 10\text{ mm}$ ondervindt een kracht van $F = 6\text{ kN} = 6000\text{ N}$, aangrijpend onder een hoek van $\theta = 30^\circ$ met de verticaal (loodlijn op het bovenvlak).
**Gevraagd:** Bereken de normaalspanning $\sigma$ en schuifspanning $\tau$ op het bovenvlak.

#### 💡 Uitwerking:
1. **Ontbinding van de kracht**:
   * Normaalkracht loodrecht op vlak: $F_n = F \cos(30^\circ) = 6000 \times \frac{\sqrt{3}}{2} \approx 5196.15\text{ N}$
   * Schuifkracht evenwijdig met vlak: $F_s = F \sin(30^\circ) = 6000 \times 0.5 = 3000\text{ N}$
2. **Oppervlakte bovenvlak**:
   $$A = 10\text{ mm} \times 10\text{ mm} = 100\text{ mm}^2$$
3. **Spanningen**:
   $$\sigma = \frac{F_n}{A} = \frac{5196.15\text{ N}}{100\text{ mm}^2} \approx \mathbf{51.96\text{ MPa}} \approx \mathbf{52\text{ MPa}}$$
   $$\tau = \frac{F_s}{A} = \frac{3000\text{ N}}{100\text{ mm}^2} = \mathbf{30.00\text{ MPa}}$$

---

### Opgave 3: Tweetraps Compressietest (Technische vs Ware Rek)
Een cilindrisch proefstuk met beginhoogte $h_0 = 100\text{ mm}$ wordt in twee stappen gestuikt:
* Tussenhoogte: $h_1 = 70\text{ mm}$
* Eindhoogte: $h_2 = 40\text{ mm}$
**Gevraagd:** Bereken de technische rek $\epsilon_t$ en de ware rek $\epsilon_w$ voor stap 1, stap 2 en de totale vervorming van begin tot einde.

#### 💡 Uitwerking:
1. **Stap 1 ($100 \to 70\text{ mm}$)**:
   * $\epsilon_{t,1} = \frac{70 - 100}{100} = \mathbf{-0.30} \quad (-30\%)$
   * $\epsilon_{w,1} = \ln\left(\frac{70}{100}\right) = \mathbf{-0.357}$
2. **Stap 2 ($70 \to 40\text{ mm}$)**:
   * $\epsilon_{t,2} = \frac{40 - 70}{70} = \frac{-30}{70} \approx \mathbf{-0.429} \quad (-42.9\%)$
   * $\epsilon_{w,2} = \ln\left(\frac{40}{70}\right) = \mathbf{-0.560}$
3. **Totale Vervorming ($100 \to 40\text{ mm}$)**:
   * $\epsilon_{t,\text{tot}} = \frac{40 - 100}{100} = \mathbf{-0.60} \quad (-60\%)$ *(Let op: $\epsilon_{t,1} + \epsilon_{t,2} = -0.729 \ne \epsilon_{t,\text{tot}}$, technische rek is NIET additief!)*
   * $\epsilon_{w,\text{tot}} = \ln\left(\frac{40}{100}\right) = \mathbf{-0.916}$ *(Merk op: $\epsilon_{w,1} + \epsilon_{w,2} = -0.357 - 0.560 = -0.917 \approx \epsilon_{w,\text{tot}}$, ware rek is WEL exact additief!)*

---

### Opgave 4: Aluminium Balk & Volumeverandering
Een balk ($400\text{ mm} \times 25\text{ mm} \times 20\text{ mm}$) uit Al ($E = 70\text{ GPa}, \nu = 0.33, R_e = 165\text{ MPa}$) wordt belast met $F = 65\text{ kN}$.
1. **Volumeverandering $\Delta V$**:
   * Doorsnede $A_0 = 25 \times 20 = 500\text{ mm}^2$
   * Spanning $\sigma = \frac{65\,000}{500} = 130\text{ MPa} < R_e$ (elastisch)
   * Axiale rek $\epsilon_z = \frac{130}{70\,000} \approx 0.001857$
   * Volumerek $\epsilon_V = \frac{\Delta V}{V_0} = \epsilon_z(1 - 2\nu) = 0.001857 \times (1 - 2 \times 0.33) = 0.001857 \times 0.34 \approx 6.314 \times 10^{-4}$
   * $V_0 = 400 \times 25 \times 20 = 200\,000\text{ mm}^3$
   * $\Delta V = V_0 \cdot \epsilon_V = 200\,000 \times 6.314 \times 10^{-4} \approx \mathbf{126.3\text{ mm}^3}$
2. **Verlenging $\Delta L$ bij bereiken van $R_e$ ($165\text{ MPa}$)**:
   * $\epsilon_{\max} = \frac{R_e}{E} = \frac{165}{70\,000} \approx 0.002357$
   * $\Delta L = L_0 \cdot \epsilon_{\max} = 400 \times 0.002357 \approx \mathbf{0.943\text{ mm}}$
