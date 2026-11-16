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

# ⚙️ Oefenzitting 2: Sterkte, Plasticiteit en Hardheid
#oefenzitting #trekproef #hardheid #ludwik

> [!info] Vereiste Theorie & Achtergrond
> Bestudeer eerst: [[04_Theory_Notes/H10_Plasticiteit_en_Trekproef]] en [[04_Theory_Notes/H11_Roosterdefecten_en_Verstevigingsmechanismen]]
> Formules: [[01_Formularium_Master#2-plasticiteit-vervorming--hardheid]]

---

### Opgave 1: Kwalitatieve Rangschikking Trekkrommen
Gegeven zijn drie materialen A, B en C:
* **Curve A**: Zeer steile lineaire helling, bereikt zeer hoge spanning, breekt vrijwel direct zonder veel rek.
* **Curve B**: Matig steile helling, duidelijke vloeigrens rond 300 MPa, aanzienlijke plastische rek tot breuk rond 15%.
* **Curve C**: Lage helling, zeer lage spanning, zeer grote rek (> 50%).

#### 💡 Rangschikkingen:
1. **Stijfheid (E-modulus = initiële helling)**: $\mathbf{A > B > C}$
2. **Treksterkte ($\sigma_{\text{UTS}} = \text{piekspanning}$)**: $\mathbf{A > B > C}$
3. **Ductiliteit (breukrek $\epsilon_f$)**: $\mathbf{C > B > A}$
4. **Taaiheid (totale oppervlakte onder de kromme)**: $\mathbf{B > C > A}$ *(Materiaal B combineert hoge spanning met behoorlijke plastische rek en absorbeert de meeste energie)*.

---

### Opgave 2: Bi-lineair Materiaal & Permanente Rek
Een cilindrische staaf met diameter $d = 20\text{ mm}$ heeft een bi-lineair spanning-rekgedrag:
* Vloeispanning: $\sigma_y = 450\text{ MPa}$ bij $\epsilon_y = 0.00225$
* Treksterkte: $\sigma_{\text{UTS}} = 500\text{ MPa}$ bij $\epsilon = 0.030$
Er wordt een trekkracht $P = 150\text{ kN}$ aangelegd en vervolgens weggenomen.
**Gevraagd:** Bepaal de E-modulus en de permanente rek $\epsilon_{\text{perm}}$ na ontlasting.

#### 💡 Uitwerking:
1. **E-modulus (uit het elastische deel)**:
   $$E = \frac{\sigma_y}{\epsilon_y} = \frac{450\text{ MPa}}{0.00225} = \mathbf{200\,000\text{ MPa}} = \mathbf{200\text{ GPa}}$$
2. **Optredende spanning bij $P = 150\text{ kN}$**:
   $$A_0 = \frac{\pi}{4} (20)^2 \approx 314.16\text{ mm}^2$$
   $$\sigma_{\text{appl}} = \frac{150\,000\text{ N}}{314.16\text{ mm}^2} \approx \mathbf{477.46\text{ MPa}}$$
   Omdat $450\text{ MPa} < \sigma_{\text{appl}} < 500\text{ MPa}$, bevindt het materiaal zich in het plastische bereik!
3. **Totale rek $\epsilon_{\text{tot}}$ bij $477.46\text{ MPa}$**:
   De helling van het plastische traject is:
   $$E_p = \frac{500 - 450}{0.030 - 0.00225} = \frac{50}{0.02775} \approx 1801.8\text{ MPa}$$
   $$\epsilon_{\text{tot}} = \epsilon_y + \frac{\sigma_{\text{appl}} - \sigma_y}{E_p} = 0.00225 + \frac{477.46 - 450}{1801.8} = 0.00225 + 0.01524 \approx \mathbf{0.01749}$$
4. **Elastische terugvering & Permanente rek**:
   Bij ontlasting ontlast het materiaal elastisch met de oorspronkelijke helling $E$:
   $$\epsilon_{\text{elastisch}} = \frac{\sigma_{\text{appl}}}{E} = \frac{477.46}{200\,000} \approx 0.00239$$
   $$\epsilon_{\text{perm}} = \epsilon_{\text{tot}} - \epsilon_{\text{elastisch}} = 0.01749 - 0.00239 = \mathbf{0.0151} = \mathbf{1.51\%}$$

---

### Opgave 3: Hardheidsberekeningen (Brinell & Vickers)
1. **Brinell Hardheid**: Kogel $D = 2.5\text{ mm}$, belasting $P = 31.25\text{ kgf}$, indrukdiameter $d = 0.748\text{ mm}$.
   $$\text{HBW} = \frac{2P}{\pi D [D - \sqrt{D^2 - d^2}]} = \frac{2 \times 31.25}{\pi \times 2.5 \times [2.5 - \sqrt{2.5^2 - 0.748^2}]} \approx \mathbf{68.5\text{ HBW}}$$
2. **Vickers Hardheid**: Diamantpiramide onder $P = 100\text{ kgf}$, gemiddelde diagonaal $d = 0.855\text{ mm}$.
   $$\text{HV} = 1.8544 \times \frac{P}{d^2} = 1.8544 \times \frac{100}{(0.855)^2} \approx \mathbf{253.7\text{ HV}}$$
