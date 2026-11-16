# 📐 Master Formularium SGDM
#formularium #wiskunde #formules

Dit formularium bevat alle wiskundige betrekkingen, eenheden, geldigheidscriteria en rechtstreekse links naar de bijbehorende theoriehoofdstukken.

---

## 1. Stijfheid, Spanning & Rek
Zie theorie: [[04_Theory_Notes/H02_Stijfheid_en_Elasticiteit]] | Oefeningen: [[05_Oefenzittingen/Sessie_01_Spanning_Rek_Stijfheid]]

* **Technische normaalspanning ($[\text{MPa}] = [\text{N/mm}^2]$)**:
  $$\sigma_t = \frac{F}{A_0}$$
* **Technische rek ($[-]$)**:
  $$\epsilon_t = \frac{\Delta L}{L_0} = \frac{L - L_0}{L_0}$$
* **Ware normaalspanning ($[\text{MPa}]$)** (geldig vóór insnoering):
  $$\sigma_w = \frac{F}{A} = \sigma_t (1 + \epsilon_t)$$
* **Ware rek ($[-]$)**:
  $$\epsilon_w = \ln\left(\frac{L}{L_0}\right) = \ln(1 + \epsilon_t)$$
* **Wet van Hooke (1D uniaxiaal)**:
  $$\sigma = E \cdot \epsilon$$
* **Poisson-coëfficiënt (dwarscontractie)**:
  $$\nu = -\frac{\epsilon_{\text{trans}}}{\epsilon_{\text{axiaal}}} = -\frac{\epsilon_x}{\epsilon_z} = -\frac{\epsilon_y}{\epsilon_z}$$
  *(Theoretisch bereik voor isotrope materialen: $0 \le \nu \le 0.5$; metalen $\approx 0.33$, rubber $\approx 0.5$, kurk $\approx 0$)*
* **Volumerek ($\\Delta V / V_0$)**:
  $$\epsilon_V = \frac{\Delta V}{V_0} = \epsilon_x + \epsilon_y + \epsilon_z = \epsilon_z (1 - 2\nu)$$
* **Schuifspanning & Afschuiving**:
  $$\tau = \frac{F_s}{A_0}, \quad \gamma = \tan\theta \approx \theta, \quad \tau = G \cdot \gamma$$
* **Verband tussen elastische moduli ($E, G, K, \nu$) voor isotrope stoffen**:
  $$G = \frac{E}{2(1 + \nu)}, \quad K = \frac{E}{3(1 - 2\nu)}$$
* **Spanningen op een willekeurig vlak onder hoek $\theta$ (uniaxiale trek $\sigma$)**:
  $$\sigma_\theta = \sigma \cos^2\theta$$
  $$\tau_\theta = \sigma \sin\theta \cos\theta = \frac{\sigma}{2}\sin(2\theta) \quad (\tau_{\max} \text{ bij } \theta = 45^\circ)$$
* **Resiliëntie (elastische energie per volume)**:
  $$u_r = \int_0^{\epsilon_e} \sigma d\epsilon = \frac{R_e^2}{2E} = \frac{\sigma_y^2}{2E} \quad [\text{MJ/m}^3 = \text{J/cm}^3]$$

---

## 2. Plasticiteit, Vervorming & Hardheid
Zie theorie: [[04_Theory_Notes/H10_Plasticiteit_en_Trekproef]], [[04_Theory_Notes/H11_Roosterdefecten_en_Verstevigingsmechanismen]] | Oefeningen: [[05_Oefenzittingen/Sessie_02_Sterkte_Plasticiteit_Hardheid]]

* **Wet van Schmid (kritische afschuifspanning op glijsysteem)**:
  $$\tau_{\text{CRSS}} = \sigma_y \cos\phi \cos\lambda = \sigma_y \cdot m$$
  waarbij $\phi$ de hoek tussen trek-as en glijvlaknormaal is, en $\lambda$ de hoek tussen trek-as en glijrichting ($m \le 0.5$).
* **Ludwik / Hollomon vergelijking voor rekversteviging**:
  $$\sigma_w = K \cdot \epsilon_w^n$$
  *(Bij maximale uniforme rek / begin van insnoering geldt: $\epsilon_{w,\text{uniform}} = n$)*
* **Hall-Petch relatie (korrelgrensversteviging)**:
  $$\sigma_y = \sigma_0 + \frac{k_y}{\sqrt{d}}$$
  waarbij $d$ de gemiddelde korreldiameter is.
* **Elastische terugvering na trekproef**:
  $$\epsilon_{\text{terugvering}} = \frac{\sigma_{\text{ontlasting}}}{E}, \quad \epsilon_{\text{permanent}} = \epsilon_{\text{totaal}} - \frac{\sigma}{E}$$
* **Hardheidsmetingen**:
  * **Brinell (BHN)**:
    $$\text{HBW} = \frac{2P}{\pi D \left(D - \sqrt{D^2 - d^2}\right)}$$
  * **Vickers (HV)**:
    $$\text{HV} = 1.8544 \frac{P}{d^2} \quad (d = \text{gemiddelde diagonaal})$$
  * **Knoop (HK)**:
    $$\text{HK} = 14.229 \frac{P}{l^2}$$

---

## 3. Diffusie & Kinetica
Zie theorie: [[04_Theory_Notes/H13_Diffusie_en_Sinteren]] | Oefeningen: [[05_Oefenzittingen/Sessie_03_Diffusie_en_Fasediagrammen]]

* **Eerste wet van Fick (stationaire diffusie)**:
  $$J = -D \frac{dC}{dx} \quad [\text{mol}/(\text{m}^2\cdot\text{s}) \text{ of } \text{kg}/(\text{m}^2\cdot\text{s})]$$
* **Tweede wet van Fick (niet-stationair, $D$ constant)**:
  $$\frac{\partial C}{\partial t} = D \frac{\partial^2 C}{\partial x^2}$$
* **Oplossing half-oneindig medium (carburatie/ontkoling)**:
  $$\frac{C(x,t) - C_0}{C_s - C_0} = 1 - \text{erf}\left(\frac{x}{2\sqrt{Dt}}\right)$$
* **Temperatuurafhankelijkheid van diffusiecoëfficiënt (Arrhenius)**:
  $$D = D_0 \exp\left(-\frac{Q_d}{R T}\right)$$
  *(met $R = 8.314 \text{ J/(mol}\cdot\text{K)}$ of $k_B = 1.38 \times 10^{-23} \text{ J/K}$)*
* **Karakteristieke diffusie-afstand**:
  $$x \approx \sqrt{2Dt} \quad \text{of} \quad x \approx 2\sqrt{Dt}$$

---

## 4. Fasenevenwichten & Fasediagrammen
Zie theorie: [[04_Theory_Notes/H14_Fasetransformaties_en_Evenwichtsdiagrammen]] | Oefeningen: [[05_Oefenzittingen/Sessie_04_Fasediagrammen_en_Composieten]]

* **Gibbs Fasenregel (bij constante druk $p = 1\text{ atm}$)**:
  $$F = C - P + 1$$
  waarbij $F$ het aantal vrijheidsgraden is, $C$ het aantal componenten, en $P$ het aantal fasen.
* **Hefboomregel (Lever Rule)** in tweefasengebied $(\alpha + \beta)$ met totale samenstelling $C_0$:
  $$W_\alpha = \frac{C_\beta - C_0}{C_\beta - C_\alpha}, \quad W_\beta = \frac{C_0 - C_\alpha}{C_\beta - C_\alpha}$$

---

## 5. Composieten (Artificiële Materialen)
Zie theorie: [[04_Theory_Notes/H15_Artificiele_Materialen_en_Composieten]] | Oefeningen: [[05_Oefenzittingen/Sessie_04_Fasediagrammen_en_Composieten]]

* **Mengselregel (Rule of Mixtures) — Longitudinaal (Isostrain: $\epsilon_c = \epsilon_f = \epsilon_m$)**:
  $$E_{c,l} = V_f E_f + V_m E_m = V_f E_f + (1 - V_f) E_m$$
  $$\sigma_{c,l}^* = V_f \sigma_f^* + (1 - V_f) \sigma_m'$$
* **Mengselregel — Transversaal (Isostress: $\sigma_c = \sigma_f = \sigma_m$)**:
  $$\frac{1}{E_{c,t}} = \frac{V_f}{E_f} + \frac{V_m}{E_m} \implies E_{c,t} = \frac{E_f E_m}{V_f E_m + (1 - V_f) E_f}$$
* **Kritische vezellengte**:
  $$l_c = \frac{\sigma_f^* d}{2 \tau_c}$$

---

## 6. Breukmechanica
Zie theorie: [[04_Theory_Notes/H16_Breukmechanica_en_Taaiheid]] | Oefeningen: [[05_Oefenzittingen/Sessie_05_Breukmechanica_Vermoeiing_Kruip]]

* **Spanningsconcentratie aan afgeronde scheurtip**:
  $$\sigma_{\max} = 2 \sigma_0 \sqrt{\frac{a}{\rho_t}} \implies K_t = \frac{\sigma_{\max}}{\sigma_0} = 2\sqrt{\frac{a}{\rho_t}}$$
* **Griffith breukcriterium (volledig brosse materialen)**:
  $$\sigma_c = \sqrt{\frac{2 E \gamma_s}{\pi a}}$$
* **Spanningsintensiteitsfactor ($K_I$) & Breukcriterium**:
  $$K_I = Y \sigma \sqrt{\pi a}$$
  $$K_I \ge K_{Ic} \implies \text{Instabiele brosse breuk}$$
* **Kritische scheurlengte ($a_c$)**:
  $$a_c = \frac{1}{\pi} \left(\frac{K_{Ic}}{Y \sigma}\right)^2$$
  *(Voor een inwendige scheur is de totale lengte $2a$; voor een oppervlaktescheur is de diepte $a$)*.

---

## 7. Vermoeiing (Dynamische Belasting)
Zie theorie: [[04_Theory_Notes/H17_Vermoeiing_en_Dynamische_Belasting]] | Oefeningen: [[05_Oefenzittingen/Sessie_05_Breukmechanica_Vermoeiing_Kruip]]

* **Karakteristieken van cyclische belasting**:
  $$\sigma_m = \frac{\sigma_{\max} + \sigma_{\min}}{2}, \quad \sigma_a = \frac{\sigma_{\max} - \sigma_{\min}}{2}$$
  $$\Delta \sigma = \sigma_{\max} - \sigma_{\min} = 2\sigma_a, \quad R = \frac{\sigma_{\min}}{\sigma_{\max}}$$
* **Correcties voor gemiddelde spanning $\sigma_m$**:
  * **Goodman (conservatief voor ductiele metalen)**:
    $$\frac{\sigma_a}{\sigma_{a0}} + \frac{\sigma_m}{\sigma_{\text{UTS}}} = 1 \implies \sigma_a = \sigma_{a0} \left(1 - \frac{\sigma_m}{\sigma_{\text{UTS}}}\right)$$
  * **Gerber (parabolisch)**:
    $$\frac{\sigma_a}{\sigma_{a0}} + \left(\frac{\sigma_m}{\sigma_{\text{UTS}}}\right)^2 = 1$$
  * **Soderberg (vloei-conservatief)**:
    $$\frac{\sigma_a}{\sigma_{a0}} + \frac{\sigma_m}{\sigma_y} = 1$$
* **Miner's Regel voor cumulatieve schade**:
  $$\sum_{i=1}^k \frac{n_i}{N_i} = 1$$
* **Paris-Erdogan Wet (scheurgroeisnelheid)**:
  $$\frac{da}{dN} = C (\Delta K)^m = C \left(Y \Delta \sigma \sqrt{\pi a}\right)^m$$

---

## 8. Tijdsafhankelijk Gedrag & Kruip
Zie theorie: [[04_Theory_Notes/H18_Tijdsafhankelijk_Gedrag_en_Kruip]] | Oefeningen: [[05_Oefenzittingen/Sessie_05_Breukmechanica_Vermoeiing_Kruip]]

* **Totale rek bij kruip**:
  $$\epsilon_{\text{tot}}(t) = \epsilon_0 + \dot{\epsilon}_s t + \epsilon_{\text{tertiair}}(t)$$
* **Stationaire kruipsnelheid (Power-Law / Norton)**:
  $$\dot{\epsilon}_s = A \sigma^n \exp\left(-\frac{Q_{\text{kruip}}}{R T}\right)$$
* **Spanningsrelaxatie ($\\epsilon_{\text{tot}} = \text{constant}$)**:
  $$\epsilon_{\text{tot}} = \frac{\sigma(t)}{E} + \epsilon_{\text{kruip}}(t) = \text{cte} \implies \sigma(t) = \sigma_0 \exp\left(-\frac{t}{\tau_r}\right)$$
* **Larson-Miller Parameter ($LMP$)**:
  $$LMP = T \cdot (C + \log t_r) \quad (T \text{ in Kelvin, } C \approx 20, t_r \text{ in uren})$$

---

## 9. Materiaalselectie (Ashby)
Zie theorie: [[04_Theory_Notes/H22_Materiaalkeuze_en_Ashby_Methodiek]]

* **Doelfunctie koppeling**:
  $$P = f(F) \cdot f(G) \cdot f(M)$$
* **Typische prestatie-indices ($M$) bij minimaal gewicht**:
  * Trekstaaf op stijfheid: $M = \frac{E}{\rho}$
  * Buigbalk op stijfheid: $M = \frac{E^{1/2}}{\rho}$
  * Buigplaat op stijfheid: $M = \frac{E^{1/3}}{\rho}$
  * Trekstaaf op sterkte: $M = \frac{\sigma_y}{\rho}$
  * Buigbalk op sterkte: $M = \frac{\sigma_y^{2/3}}{\rho}$
