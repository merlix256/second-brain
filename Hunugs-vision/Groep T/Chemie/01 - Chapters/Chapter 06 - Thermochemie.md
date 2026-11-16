---
title: "Hoofdstuk 6: Thermochemie"
tags:
  - study-unit
  - chemie
  - thermochemie
  - thermodynamica
  - enthalpie
course: "Chemie (T1ACH1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: high
---
# 🌡️ Hoofdstuk 6: Thermochemie

> [!abstract] Kerndefinitie
> **Thermochemie** is de studie van warmteveranderingen tijdens chemische reacties en faseovergangen. Het vormt een integraal onderdeel van de thermodynamica: de wetenschap die de omzetting van warmte en andere energievormen bestudeert.

---

## 1. Systemen, Energie en de Eerste Hoofdwet

### 1.1 Classificatie van Systemen
Een **systeem** is het specifiek afgebakende deel van het universum dat we bestuderen; de rest is de **omgeving**:
- **Open systeem**: Kan zowel materie als energie uitwisselen met de omgeving (bijv. een open bekerglas).
- **Gesloten systeem**: Kan enkel energie uitwisselen met de omgeving, geen materie (bijv. een afgesloten erlenmeyer).
- **Geïsoleerd systeem**: Kan noch materie, noch energie uitwisselen met de omgeving (bijv. een ideale thermosfles/calorimeter).

### 1.2 Arbeid en Warmte
**Energie** is het vermogen om arbeid te verrichten. **Arbeid ($w$)** is een gerichte energieverandering ten gevolge van een proces (bijvoorbeeld volumearbeid door gasexpansie):
$$w = -P_{\text{ext}} \cdot \Delta V$$
waarbij een expansie ($\Delta V > 0$) betekent dat het systeem arbeid verricht *op* de omgeving ($w < 0$).

### 1.3 De Eerste Wet van de Thermodynamica
De totale hoeveelheid energie in het universum blijft constant (wet van behoud van energie):
$$\Delta U_{\text{universum}} = \Delta U_{\text{systeem}} + \Delta U_{\text{omgeving}} = 0$$
Voor een gesloten systeem geldt de verandering in interne energie ($\Delta U$ of $\Delta E$):
$$\Delta U = q + w$$
waarbij:
- $q > 0$: Endotherm proces (warmte opgenomen door systeem).
- $q < 0$: Exotherm proces (warmte afgestaan aan omgeving).

![[Slide_6_Systeem_Omgeving.png]]

---

## 2. Toestandsfuncties en Enthalpie ($H$)

### 2.1 Eigenschap van een Toestandsfunctie
> [!info] Toestandsfunctie
> Een **toestandsfunctie** is een grootheid waarvan de waarde uitsluitend afhangt van de actuele toestand van het systeem (zoals druk $P$, volume $V$, temperatuur $T$, interne energie $U$ en enthalpie $H$), en **niet** van de gevolgde weg. Warmte ($q$) en arbeid ($w$) zijn **geen** toestandsfuncties (padfuncties).

### 2.2 Afleiding van Enthalpie bij Constante Druk
Omdat chemische reacties in het lab meestal plaatsvinden onder constante atmosferische druk ($P = \text{cte}$):
$$\Delta U = q_p + w = q_p - P \Delta V$$
$$q_p = \Delta U + P \Delta V$$

We definiëren de toestandsfunctie **enthalpie ($H$)**:
$$H = U + PV$$
Bij constante druk geldt voor de enthalpieverandering ($\Delta H$):
$$\Delta H = \Delta U + P \Delta V = q_p$$

> [!tip] Cruciaal Inzicht
> De enthalpieverandering van een reactie ($\Delta H_{\text{rxn}}$) is exact gelijk aan de uitgewisselde warmte bij constante druk ($q_p$).
> - $\Delta H < 0$: **Exotherm** ($H_{\text{producten}} < H_{\text{reagentia}}$, warmte komt vrij).
> - $\Delta H > 0$: **Endotherm** ($H_{\text{producten}} > H_{\text{reagentia}}$, warmte wordt opgenomen).

---

## 3. Calorimetrie

Calorimetrie is de experimentele techniek om warmteoverdrachten kwantitatief te meten.

### 3.1 Warmtecapaciteit ($C$) en Specifieke Warmte ($s$)
- **Warmtecapaciteit ($C$)**: De warmte benodigd om de temperatuur van een object met $1\text{ }^\circ\text{C}$ ($1\text{ K}$) te doen stijgen [$\text{J}/^\circ\text{C}$].
- **Specifieke warmte ($s$ of $c$)**: De warmte benodigd om $1\text{ gram}$ van een stof met $1\text{ }^\circ\text{C}$ te doen stijgen [$\text{J}/(\text{g}\cdot^\circ\text{C})$].
$$C = m \cdot s$$
$$q = m \cdot s \cdot \Delta T \quad \text{of} \quad q = C \cdot \Delta T$$
waarbij $\Delta T = T_{\text{eind}} - T_{\text{begin}}$. (Voor vloeibaar water: $s = 4.184\text{ J}/(\text{g}\cdot^\circ\text{C})$).

### 3.2 Constante-Druk Calorimeter ("Coffee-Cup")
Toegepast voor neutralisatie-, oplos- en precipitatiereacties in waterig milieu.
$$q_{\text{geïsoleerd}} = q_{\text{rxn}} + q_{\text{oplossing}} + q_{\text{cal}} = 0$$
$$q_{\text{rxn}} = - \left( m_{\text{opl}} \cdot s_{\text{opl}} \cdot \Delta T + C_{\text{cal}} \cdot \Delta T \right)$$
Aangezien $P = \text{cte}$, is $\Delta H_{\text{rxn}} = \frac{q_{\text{rxn}}}{n_{\text{limiterend}}}$.

![[Coffee_Cup_Calorimeter.png]]

### 3.3 Constante-Volume Calorimeter ("Bomcalorimeter")
Toegepast voor verbrandingsreacties onder hoge zuurstofdruk ($P_{\text{O}_2} \approx 30\text{ atm}$):
- Omdat het volume vastligt ($\Delta V = 0$), is $w = -P \Delta V = 0$.
- Derhalve meet de bomcalorimeter de interne energieverandering:
$$\Delta U = q_v = - C_{\text{bom,tot}} \cdot \Delta T$$

![[Bomb_Calorimeter.png]]

---

## 4. Bepaling van Reactie-enthalpieën

### 4.1 Wet van Hess
> [!quote] Wet van Hess
> Aangezien enthalpie een toestandsfunctie is, is de totale enthalpieverandering van een chemisch proces gelijk aan de som van de enthalpieveranderingen van de individuele deelstappen waarin de reactie ontbonden kan worden.

Als $A \rightarrow B$ ($\Delta H_1$) en $B \rightarrow C$ ($\Delta H_2$), dan geldt voor $A \rightarrow C$:
$$\Delta H_{\text{totaal}} = \Delta H_1 + \Delta H_2$$

### 4.2 Standaardvormingsenthalpie ($\Delta H^\circ_f$)
De **standaardvormingsenthalpie ($\Delta H^\circ_f$)** is de enthalpieverandering bij de vorming van $1\text{ mol}$ van een zuivere verbinding uit haar elementen in hun meest stabiele aggregatietoestand bij standaardomstandigheden ($P = 1\text{ atm}$, conventioneel $T = 298.15\text{ K}$):
- Per definitie geldt: $\Delta H^\circ_f = 0\text{ kJ/mol}$ voor stabiele vrije elementen (bijv. $\text{O}_{2(g)}$, $\text{C}_{(\text{grafiet})}$, $\text{N}_{2(g)}$).
- Voor een willekeurige reactie:
$$\Delta H^\circ_{\text{rxn}} = \sum n \cdot \Delta H^\circ_f(\text{producten}) - \sum m \cdot \Delta H^\circ_f(\text{reagentia})$$

---

## 📝 Samenvatting
1. De Eerste Hoofdwet stelt $\Delta U = q + w$; bij volumearbeid geldt $w = -P \Delta V$.
2. Enthalpie is gedefinieerd als $H = U + PV$. Bij constante druk is $\Delta H = q_p$.
3. Warmtecapaciteit koppelt warmte aan temperatuur: $q = m s \Delta T + C_{\text{cal}} \Delta T$. In een geïsoleerd vat is $q_{\text{rxn}} = -q_{\text{omgeving}}$.
4. De Wet van Hess stelt dat reactie-enthalpieën additief zijn en berekend kunnen worden via $\Delta H^\circ_{\text{rxn}} = \sum \Delta H^\circ_f(\text{prod}) - \sum \Delta H^\circ_f(\text{reag})$.
