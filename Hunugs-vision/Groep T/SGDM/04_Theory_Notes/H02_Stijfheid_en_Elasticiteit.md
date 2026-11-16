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

# 🔬 H02: Stijfheid en Elastisch Gedrag van Materialen
#theorie #stijfheid #elasticiteit #hooke #poisson #H02

[[00_Overview_Dashboard]] | [[01_Formularium_Master#1-stijfheid-spanning--rek]] | [[05_Oefenzittingen/Sessie_01_Spanning_Rek_Stijfheid]]

---

## 1. Mechanische Spanning & Rek
Bij een uniaxiale trekbelasting op een staaf met begindoorsnede $A_0$ en beginlengte $L_0$:
* **Technische spanning ($\sigma_t$)**:
  $$\sigma_t = \frac{F}{A_0} \quad [\text{MPa} = \text{N/mm}^2]$$
* **Technische rek ($\epsilon_t$)**:
  $$\epsilon_t = \frac{\Delta L}{L_0} = \frac{L - L_0}{L_0}$$
* **Ware spanning ($\sigma_w$) en ware rek ($\epsilon_w$)**:
  Omdat het actuele oppervlak $A$ verkleint tijdens verlenging (volumebehoud in plastisch gebied $A \cdot L = A_0 \cdot L_0$):
  $$\sigma_w = \frac{F}{A} = \sigma_t (1 + \epsilon_t)$$
  $$\epsilon_w = \int_{L_0}^L \frac{dL}{L} = \ln\left(\frac{L}{L_0}\right) = \ln(1 + \epsilon_t)$$

---

## 2. Wet van Hooke & De Elasticiteitsmodulus
Voor kleine elastische vervormingen geldt het lineaire verband:
$$\sigma = E \cdot \epsilon$$
waarbij $E$ de **Young's modulus** (elasticiteitsmodulus) is.
* Typische waarden:
  * Diamant: $\sim 1000\text{ GPa}$
  * Staal: $\sim 200 - 210\text{ GPa}$
  * Aluminium: $\sim 70\text{ GPa}$
  * Polymeren (PE, PP): $\sim 0.2 - 3\text{ GPa}$
  * Rubber/Elastomeren: $\sim 0.001 - 0.05\text{ GPa}$

---

## 3. Dwarscontractie & Poisson-coëfficiënt ($\nu$)
Wanneer een materiaal in de lengterichting ($z$) wordt uitgerekt, contraheert het in de dwarsrichtingen ($x, y$):
$$\nu = -\frac{\epsilon_x}{\epsilon_z} = -\frac{\epsilon_y}{\epsilon_z}$$

```
                F_z (Trek)
                    ^
                    |
              +-----------+
              |     |     |
              |<-d1>|     |   (d1 < d0 : laterale contractie)
              |     |     |
              +-----------+
                    |
                    v
```

* **Volumerek**:
  $$\epsilon_V = \frac{\Delta V}{V_0} = \epsilon_x + \epsilon_y + \epsilon_z = \epsilon_z(1 - 2\nu)$$
  * Als $\nu = 0.5$ (zoals rubber of vloeistoffen): $\epsilon_V = 0 \implies$ **volledig onsamendrukbaar**!
  * Voor metalen ($\nu \approx 0.33$): volume neemt licht toe onder trek.
  * Voor kurk ($\nu \approx 0$): geen dwarsuitzetting bij indrukking (ideaal voor wijnkurken!).

---

## 4. Schuifspanning & Glijmodulus ($G$)
* Schuifspanning: $\tau = \frac{F_s}{A_0}$
* Afschuiving: $\gamma = \tan\theta \approx \theta$ (in radialen)
* Verband: $\tau = G \cdot \gamma$
* Isotroop verband:
  $$G = \frac{E}{2(1 + \nu)}$$

### Richtingsafhankelijkheid van Spanningen
Op een vlak onder een hoek $\theta$ t.o.v. de dwarsdoorsnede bij uniaxiale trek $\sigma$:
$$\sigma_\theta = \sigma \cos^2\theta$$
$$\tau_\theta = \sigma \sin\theta \cos\theta = \frac{\sigma}{2}\sin(2\theta)$$
* De schuifspanning $\tau_\theta$ bereikt haar **absolute maximum bij $\theta = 45^\circ$**:
  $$\tau_{\max} = \frac{\sigma}{2}$$
Dit verklaart waarom ductiele metalen onder trek plastisch beginnen afschuiven onder hoeken van ca. $45^\circ$!

---

## 5. Resiliëntie
Resiliëntie is de maximale hoeveelheid elastische vervormingsenergie per volume-eenheid:
$$u_r = \frac{R_e^2}{2E} = \frac{\sigma_y^2}{2E}$$
* Toepassing: Veermaterialen vereisen een **hoge vloeigrens $R_e$** gecombineerd met een **lage tot matige $E$-modulus** (bijv. verenstaal, titanium).

---

> [!summary] Hoofdstuksamenvatting
> Stijfheid is een stofeigenschap gedicteerd door de atomaire bindingskracht. De Poissoncoëfficiënt beschrijft de dwarscontractie, terwijl schuifspanningen maximaal worden op $45^\circ$, wat de brug vormt naar plastische deformatie via dislocaties.
