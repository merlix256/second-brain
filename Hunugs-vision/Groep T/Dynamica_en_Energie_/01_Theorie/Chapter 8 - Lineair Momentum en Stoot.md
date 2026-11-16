---
course: "Dynamica en energie (T1ADE1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: high
tags:
  - study-unit
---

# 📖 Hoofdstuk 8: Lineair Momentum, Impuls en Botsingen

> [!abstract] Overzicht & Leerdoelen
> - **Leerdoel:** Het toepassen van het principe van lineaire impuls en momentum op puntmassa's en systemen, het analyseren van stootkrachten over korte tijdsintervallen en het oplossen van centrale en schuine botsingen met behulp van de restitutiecoëfficiënt $e$.
> - **Handboek:** Hibbeler Chapter 15 (§15.1 – §15.4).
> - **Master Formularium:** [[Formularium#4. Impuls en Lineair Momentum]].
> - **Actieve Herroeping:** [[Chapter 8 - Q&A]].

---

## 1. Lineair Momentum en Lineaire Impuls

### 1.1 Lineair Momentum (Hoeveelheid van Beweging)
Het lineair momentum $\mathbf{L}$ van een puntmassa met massa $m$ en snelheid $\mathbf{v}$ is een vectorgrootheid:
$$\mathbf{L} = m\mathbf{v} \quad [\text{kg}\cdot\text{m/s} = \text{N}\cdot\text{s}]$$

### 1.2 Lineaire Impuls (Stoot van een Kracht)
De lineaire impuls $\mathbf{I}$ van een kracht $\mathbf{F}$ over een tijdsinterval $[t_1, t_2]$ is de tijdsintegraal:
$$\mathbf{I} = \int_{t_1}^{t_2} \mathbf{F}\,dt$$

---

## 2. Principe van Lineaire Impuls en Momentum

Integratie van Newton's tweede wet $\sum \mathbf{F} = \frac{d(m\mathbf{v})}{dt}$ over de tijd levert:

$$m \mathbf{v}_1 + \sum \int_{t_1}^{t_2} \mathbf{F}\,dt = m \mathbf{v}_2$$

Dit principe stelt dat het initiële momentum plus alle externe krachtenimpulsen gelijk moet zijn aan het finale momentum van het deeltje.

---

## 3. Behoud van Lineair Momentum

Wanneer de resultante van de externe krachten op een deeltjessysteem gelijk aan nul is (of verwaarloosbaar klein t.o.v. de interne krachten, zoals tijdens een plotse explosie of botsing):

$$\sum m_i \mathbf{v}_{i,1} = \sum m_i \mathbf{v}_{i,2}$$

---

## 4. Botsingen (Centraal en Schuin)

Bij een botsing tussen twee deeltjes $A$ en $B$ definiëren we de **botsingslijn** (normaal $n$, de gemeenschappelijke loodlijn op het contactvlak) en het **contactvlak** (rakend $t$).

![[Slide_Impact_Central_Oblique.png]]
*(Placeholder: Botsing tussen deeltjes A en B met botsingslijn n en raaklijn t)*

### 4.1 Restitutiecoëfficiënt ($e$)
De restitutiecoëfficiënt kwantificeert de elasticiteit van de stoot langs de botsingslijn:

$$e = \frac{(v_B)_{n,2} - (v_A)_{n,2}}{(v_A)_{n,1} - (v_B)_{n,1}}$$

- **Volkomen elastische botsing ($e = 1$):** Geen energieverlies, kinetische energie blijft behouden.
- **Volkomen inelastische (plastische) botsing ($e = 0$):** Maximale energieverlies, beide lichamen blijven aan elkaar plakken en bewegen met gelijke eindsnelheid verder.
- **Reële botsing ($0 < e < 1$):** Gedeeltelijk herstel met plastische deformatie en warmtedissipatie.

### 4.2 Behoud langs de assen:
1. **Langs de raaklijn ($t$):** Bij afwezigheid van wrijvingskrachten tijdens de stoot blijft het momentum van elk deeltje afzonderlijk behouden:
   $$(v_A)_{t,2} = (v_A)_{t,1}, \qquad (v_B)_{t,2} = (v_B)_{t,1}$$
2. **Langs de botsingslijn ($n$):** Het totale momentum van het tweedelige systeem blijft behouden:
   $$m_A (v_A)_{n,1} + m_B (v_B)_{n,1} = m_A (v_A)_{n,2} + m_B (v_B)_{n,2}$$

---

## 📝 Samenvatting
- Impuls en momentum zijn bij uitstek geschikt voor problemen waarbij krachten inwerken gedurende een expliciet bekend tijdsinterval $\Delta t$.
- Tijdens een botsing zijn interactiekrachten impulsief, waardoor externe niet-impulsieve krachten (zoals zwaartekracht) tijdens de fractie van de botsing mogen worden verwaarloosd.
