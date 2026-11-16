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

# 🔬 H16: Breukmechanica en Taaiheid
#theorie #breukmechanica #griffith #spanningsintensiteit #K1c #charpy #H16

[[00_Overview_Dashboard]] | [[01_Formularium_Master#6-breukmechanica]] | [[05_Oefenzittingen/Sessie_05_Breukmechanica_Vermoeiing_Kruip]]

---

## 1. De Breukparadox & Spanningsconcentraties
Theoretische breuksterkten op basis van atoombindingen liggen rond $\sigma_{th} \approx \frac{E}{10} \approx 10\,000\text{ MPa}$. Werkelijke brosse materialen (zoals glas) bezwijken al rond $50 - 100\text{ MPa}$.
* **Oorzaak (Inglis & Griffith)**: Scherpe microscopische scheuren en defecten concentreren de aangelegde spanning lokaal aan de scheurtip:
  $$\sigma_{\max} = 2 \sigma_0 \sqrt{\frac{a}{\rho_t}}$$
  waarbij $a$ de scheurgrootte is en $\rho_t$ de afrondingsstraal van de tip. Voor een atomair scherpe scheur ($\rho_t \to 0$) divergeert de lokale spanning!

---

## 2. Lineair Elastische Breukmechanica (LEFM)
De elastische spanningsverdeling nabij een scheurtip onder trekspanning $\sigma$ (Mode I - openingsmode) wordt eenduidig gekarakteriseerd door de **spanningsintensiteitsfactor ($K_I$)**:
$$K_I = Y \sigma \sqrt{\pi a} \quad [\text{MPa}\sqrt{\text{m}}]$$
waarbij $Y$ een dimensieloze geometriefactor is (voor een oneindige plaat met inwendige scheur $2a$ is $Y = 1$; voor oppervlaktedefecten $Y \approx 1.12$).

### Breukcriterium:
Instabiele scheurgroei treedt op zodra $K_I$ de kritische materiaalgrens overschrijdt:
$$K_I \ge K_{Ic} \implies \text{Catastrofale breuk!}$$
* **$K_{Ic}$ (Breuktaaiheid onder vlakke rek / Plane Strain Fracture Toughness)**: Een echte intrinsieke materiaaleigenschap, gemeten op voldoende dikke proefstukken ($B \ge 2.5 (K_{Ic}/\sigma_y)^2$).

---

## 3. Taai-Brosse Overgangstemperatuur (DBTT)
Met de **Charpy kerfslagproef** wordt de slagenergie (joules) gemeten bij impact als functie van temperatuur:
* **KRG-metalen ($\alpha$-Fe)** vertonen een scherpe val in slagenergie: de **Ductile-to-Brittle Transition Temperature (DBTT)**. Beneden DBTT bevriezen de dislocatie-glijsystemen en breekt staal catastrofaal bros (oorzaak van het zinken van de Titanic en breken van Liberty-schepen in WO II!).
* **KGV-metalen (Al, Cu, austenitisch rvs)** bezitten 12 actieve glijsystemen $\{111\}\langle 110 \rangle$ die zelfs bij vloeibare stikstoftemperaturen mobiel blijven: **zij vertonen géén DBTT** en blijven taai!

---

## 4. Fractografie (SEM-kenmerken)
* **Ductiele breuk**: Treedt op met aanzienlijke insnoering. Breukoppervlak toont microscopische kratertjes (**dimples**) veroorzaakt door het samensmelten (coalescentie) van micro-holtes rond insluitsels.
* **Brosse breuk**: Vlak en glinsterend. Vertoont transgranulaire **splijting (cleavage)** met karakteristieke rivierpatronen ("river patterns") of intergranulaire breuk langs korrelgrenzen.

---

> [!summary] Hoofdstuksamenvatting
> Breuktaaiheid $K_{Ic}$ kwantificeert de weerstand tegen scheurgroei. KGV-kristallen behouden hun taaiheid bij vriestemperaturen, terwijl KRG-stalen een gevaarlijke taai-bros overgang vertonen.
