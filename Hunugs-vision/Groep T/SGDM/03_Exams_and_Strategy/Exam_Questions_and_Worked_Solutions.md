---
course: "SGDM (T1ASD1)"
unit_type: exam
status: todo
completed: false
est_hours: 2.5
priority: high
tags:
  - study-unit
---

# 📝 Uitgewerkte Examenvragen SGDM (2021–2024)
#examenvragen #oplossingen #stap-voor-stap

Hieronder vind je de meest representatieve, terugkerende vraagstukken uit de officiële examens van 2021 tot 2024, inclusief gedetailleerde afleidingen en theoretische koppelingen.

---

### Opgave 1: Poisson-coëfficiënt & Dwarscontractie (Examen Jan 2021 / Examenbundel)
Zie theorie: [[04_Theory_Notes/H02_Stijfheid_en_Elasticiteit]] | Formules: [[01_Formularium_Master]]

> [!question] Vraag
> Een cilindrische staaf met begindoorsnede $A_0 = 80\text{ mm}^2$ en beginlengte $L_0 = 2\text{ m} = 2000\text{ mm}$ wordt elastisch $\Delta L = 3\text{ cm} = 30\text{ mm}$ uitgerekt. De doorsnede versmalt hierbij tot $A_1 = 79.5\text{ mm}^2$.
> **Bereken de Poissoncoëfficiënt $\nu$ van het materiaal.**
> *Opties:* A: -0.42 | B: -0.21 | C: 0.21 | D: 0.42

#### ✅ Oplossing & Afleiding:
1. **Lengterek ($\epsilon_z$)**:
   $$\epsilon_z = \frac{\Delta L}{L_0} = \frac{30\text{ mm}}{2000\text{ mm}} = 0.015 = 1.5\%$$
2. **Relatie tussen doorsnede en diameter/straal**:
   Voor een cirkel geldt $A = \pi r^2$.
   $$\frac{\Delta A}{A_0} = \frac{A_1 - A_0}{A_0} = \frac{79.5 - 80.0}{80.0} = -\frac{0.5}{80} = -0.00625$$
   Omdat $A \propto r^2$, geldt bij kleine elastische rekken:
   $$\frac{\Delta A}{A_0} \approx 2 \frac{\Delta r}{r_0} = 2 \epsilon_{\text{trans}}$$
   $$\epsilon_{\text{trans}} = \frac{1}{2} \left(\frac{\Delta A}{A_0}\right) = \frac{-0.00625}{2} = -0.003125$$
3. **Berekening van $\nu$**:
   $$\nu = -\frac{\epsilon_{\text{trans}}}{\epsilon_z} = -\frac{-0.003125}{0.015} = \frac{0.003125}{0.015} \approx \mathbf{0.2083} \approx \mathbf{0.21}$$
*Correct antwoord:* **C (0.21)**.

---

### Opgave 2: Rangschikking Kritische Scheurlengte $a_c$ (Examen 2022 / Examenbundel)
Zie theorie: [[04_Theory_Notes/H16_Breukmechanica_en_Taaiheid]]

> [!question] Vraag
> De tabel toont de vloeigrens $\sigma_y$ en breuktaaiheid $K_{Ic}$ van drie materialen X, Y en Z. Rangschik de materialen volgens kritische scheurlengte $a_c$ die ze mogen bevatten voor breuk wanneer ze belast worden tot hun vloeispanning ($\sigma = \sigma_y$, neem $Y=1$).
>
> | Materiaal | $\sigma_y$ (MPa) | $K_{Ic}$ ($\text{MPa}\sqrt{\text{m}}$) |
> | :---: | :---: | :---: |
> | **X** | 180 | 18 |
> | **Y** | 300 | 22 |
> | **Z** | 600 | 28 |

#### ✅ Oplossing & Afleiding:
1. De formule voor kritische scheurlengte bij $\sigma = \sigma_y$ is:
   $$K_{Ic} = Y \sigma_y \sqrt{\pi a_c} \implies a_c = \frac{1}{\pi} \left(\frac{K_{Ic}}{\sigma_y}\right)^2$$
   De verhouding $\left(\frac{K_{Ic}}{\sigma_y}\right)$ dicteert dus rechtstreeks de toelaatbare defectgrootte!
2. Berekening van de ratio $\frac{K_{Ic}}{\sigma_y}$:
   * **Materiaal X**: $\frac{18}{180} = 0.100 \implies a_{c,X} \propto (0.100)^2 = 0.0100$
   * **Materiaal Y**: $\frac{22}{300} \approx 0.0733 \implies a_{c,Y} \propto (0.0733)^2 = 0.00538$
   * **Materiaal Z**: $\frac{28}{600} \approx 0.0467 \implies a_{c,Z} \propto (0.0467)^2 = 0.00218$
3. Rangschikking van klein naar groot:
   $$a_{c,Z} < a_{c,Y} < a_{c,X}$$
*Correct antwoord:* **$a_{c,Z} < a_{c,Y} < a_{c,X}$**.

---

### Opgave 3: Thermische Expansie & Allotropie van IJzer (Examen Jan 2024 / Examenbundel)
Zie theorie: [[04_Theory_Notes/H04_Thermische_Expansie]], [[04_Theory_Notes/H07_Kristallijne_Structuren_en_Miller_Indices]]

> [!question] Vraag
> Een staaf zuiver ijzer wordt opgewarmd van kamertemperatuur tot $1500^\circ\text{C}$. Welke kromme van lengteverandering $\Delta L$ in functie van temperatuur is correct?
> Gegeven transformaties:
> * $912^\circ\text{C}$: $\alpha\text{-Fe (KRG/BCC)} \to \gamma\text{-Fe (KGV/FCC)}$
> * $1394^\circ\text{C}$: $\gamma\text{-Fe (KGV/FCC)} \to \delta\text{-Fe (KRG/BCC)}$

#### ✅ Oplossing & Fysisch Inzicht:
1. **Kristalrooster & Atoompakkingsfactor (APF)**:
   * KRG (BCC, $\alpha$ en $\delta$): $\text{APF} = 0.68$ (minder dicht gepakt, groter volume per atoom).
   * KGV (FCC, $\gamma$): $\text{APF} = 0.74$ (dichtste stapeling, compacter volume).
2. **Gedrag bij $912^\circ\text{C}$**:
   De overgang van het lossere KRG ($\alpha$) naar het dichter gepakte KGV ($\gamma$) veroorzaakt een **plotse volumekrimp (daling van $\Delta L$)**!
3. **Gedrag bij $1394^\circ\text{C}$**:
   De overgang van het dichtgepakte KGV ($\gamma$) naar het lossere KRG ($\delta$) veroorzaakt een **plotse volumesprong omhoog (stijging van $\Delta L$)**!
*Conclusie:* De juiste grafiek vertoont een **knik/sprong naar beneden** bij $912^\circ\text{C}$ en een **sprong omhoog** bij $1394^\circ\text{C}$ (Curve A in het examen).

---

### Opgave 4: Miller-indices Vlakbepaling (Examen Vraag 30)
Zie theorie: [[04_Theory_Notes/H07_Kristallijne_Structuren_en_Miller_Indices]]

> [!question] Vraag
> Bepaal de Miller-index van het gearceerde vlak in de kubische eenheidscel met hoekpunten op $(1,0,0)$, $(0,1,1)$, en $(0,0,1)$...

#### ✅ Stappenplan:
1. Bepaal de snijpunten met de assen $x, y, z$.
2. Neem de reciproke waarden ($1/x, 1/y, 1/z$).
3. Vereenvoudig naar de kleinste gehele getallen zonder breuken $\implies (hkl)$.
