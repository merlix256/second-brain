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

# ⚙️ Oefenzitting 3: Diffusie en Kinetica
#oefenzitting #diffusie #fick #arrhenius

> [!info] Vereiste Theorie & Achtergrond
> Bestudeer eerst: [[04_Theory_Notes/H13_Diffusie_en_Sinteren]]
> Formules: [[01_Formularium_Master#3-diffusie--kinetica]]

---

### Opgave 1: Stationaire Diffusie door Membraan (Fick I)
Een membraan van $\alpha$-ijzer (dikte $\Delta x = 1.5\text{ mm} = 0.0015\text{ m}$) scheidt twee gascompartimenten bij $700^\circ\text{C}$.
De koolstofconcentraties aan de oppervlakken bedragen $C_1 = 0.85\text{ kg/m}^3$ en $C_2 = 0.10\text{ kg/m}^3$.
Bij $700^\circ\text{C}$ is $D = 1.2 \times 10^{-10}\text{ m}^2/\text{s}$.
**Bereken de stationaire diffusieflux $J$.**

#### 💡 Uitwerking:
$$J = -D \frac{dC}{dx} = -D \frac{C_2 - C_1}{\Delta x} = -1.2 \times 10^{-10} \times \frac{0.10 - 0.85}{0.0015} = \mathbf{6.0 \times 10^{-8}\text{ kg}/(\text{m}^2\cdot\text{s})}$$

---

### Opgave 2: Oppervlaktecarburatie van Tandwielstaal (Fick II)
Een laag-koolstofstaal met $C_0 = 0.20\text{ wt}\%\text{ C}$ wordt gecarbureerd bij $950^\circ\text{C}$ in een gasatmosfeer die het oppervlak constant op $C_s = 1.20\text{ wt}\%\text{ C}$ houdt.
Bij $950^\circ\text{C}$ in $\gamma$-ijzer geldt $D = 1.5 \times 10^{-11}\text{ m}^2/\text{s}$.
**Gevraagd:** Bepaal de vereiste behandeltijd $t$ (in uren) om op een diepte van $x = 0.8\text{ mm} = 8 \times 10^{-4}\text{ m}$ een koolstofgehalte van $C(x,t) = 0.60\text{ wt}\%\text{ C}$ te bereiken.

#### 💡 Uitwerking:
1. **Errorfunctie verhouding**:
   $$\frac{C(x,t) - C_0}{C_s - C_0} = \frac{0.60 - 0.20}{1.20 - 0.20} = \frac{0.40}{1.00} = 0.40$$
   Volgens de oplossing van de tweede wet van Fick:
   $$\frac{C(x,t) - C_0}{C_s - C_0} = 1 - \text{erf}(z) \implies 1 - \text{erf}(z) = 0.40 \implies \text{erf}(z) = 0.60$$
2. **Waarde van $z$ opzoeken in de foutfunctie-tabel**:
   * $\text{erf}(0.55) = 0.5633$
   * $\text{erf}(0.60) = 0.6039$
   Lineaire interpolatie:
   $$z \approx 0.55 + (0.60 - 0.55) \times \frac{0.60 - 0.5633}{0.6039 - 0.5633} = 0.55 + 0.05 \times \frac{0.0367}{0.0406} \approx \mathbf{0.595}$$
3. **Koppeling aan $x$ en $t$**:
   $$z = \frac{x}{2\sqrt{Dt}} \implies 2\sqrt{Dt} = \frac{x}{z} = \frac{8 \times 10^{-4}}{0.595} \approx 1.3445 \times 10^{-3}\text{ m}$$
   $$\sqrt{Dt} = 6.723 \times 10^{-4} \implies Dt = 4.52 \times 10^{-7}\text{ m}^2$$
   $$t = \frac{4.52 \times 10^{-7}}{1.5 \times 10^{-11}} \approx 30\,132\text{ seconden} \approx \mathbf{8.37\text{ uur}}$$
