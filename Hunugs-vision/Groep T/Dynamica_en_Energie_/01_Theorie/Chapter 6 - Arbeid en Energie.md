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

# 📖 Hoofdstuk 6: Kinetica — Arbeid en Energie

> [!abstract] Overzicht & Leerdoelen
> - **Leerdoel:** Het berekenen van de arbeid verricht door krachten (constant, variabel, zwaartekracht, veren) en het toepassen van de stelling van arbeid en kinetische energie op puntmassa's en samengestelde systemen.
> - **Handboek:** Hibbeler Chapter 14 (§14.1 – §14.4).
> - **Master Formularium:** [[Formularium#3. Arbeid, Energie en Behoudswetten]].
> - **Actieve Herroeping:** [[Chapter 6 - Q&A]].

---

## 1. Definitie van Arbeid ($U$)

De arbeid verricht door een vectoriële kracht $\mathbf{F}$ bij een infinitesimale verplaatsing $d\mathbf{r}$ is gedefinieerd als het inwendig product:

$$dU = \mathbf{F} \cdot d\mathbf{r} = F \, ds \cos\theta$$

Voor een eindige verplaatsing van toestand 1 naar toestand 2:
$$U_{1-2} = \int_{\mathbf{r}_1}^{\mathbf{r}_2} \mathbf{F} \cdot d\mathbf{r} = \int_{s_1}^{s_2} F \cos\theta \, ds$$

Arbeid is een scalaire grootheid uitgedrukt in Joule ($\text{J} = \text{N}\cdot\text{m}$).

---

## 2. Arbeid van Specifieke Krachten

### 2.1 Constante Kracht langs een Rechte Lijn
$$U_{1-2} = (F_c \cos\theta) \,(s_2 - s_1)$$

### 2.2 Zwaartekrachtarbeid
De zwaartekracht $\mathbf{W} = -mg\mathbf{j}$ wijst continu omlaag:
$$U_{1-2} = \int_{y_1}^{y_2} (-mg)\,dy = -mg (y_2 - y_1) = -W \,\Delta y$$
- Arbeid is **positief** als het object daalt ($\Delta y < 0$).
- Arbeid is **negatief** als het object stijgt ($\Delta y > 0$).
- De arbeid hangt enkel af van het verticale hoogteverschil, niet van het horizontaal afgelegde traject!

### 2.3 Veerarbeid (Lineair Elastische Veer)
De kracht uitgeoefend door een veer op een puntmassa volgens de wet van Hooke is $F_v = -ks$, waarbij $s$ de vervorming (rek of compressie) is ten opzichte van de onbelaste lengte $l_0$:

$$U_{1-2} = \int_{s_1}^{s_2} (-ks)\,ds = -\left[\frac{1}{2} k s_2^2 - \frac{1}{2} k s_1^2\right] = \frac{1}{2} k s_1^2 - \frac{1}{2} k s_2^2$$

> [!danger] Let op de kwadraten!
> De arbeid is $U_{1-2} = \frac{1}{2}k(s_1^2 - s_2^2)$ en **NIET** $\frac{1}{2}k(s_1 - s_2)^2$!

### 2.4 Wrijvingsarbeid
Omdat de kinetische wrijvingskracht $F_w = \mu_k N$ altijd tegengesteld gericht is aan de relatieve baansnelheid, is de verrichte wrijvingsarbeid altijd strikt negatief:
$$U_{\text{wrijving}} = -\int F_w \, ds = -F_w \cdot s_{\text{traject}}$$

---

## 3. Principe van Arbeid en Kinetische Energie

Vertrekkend van de tweede wet van Newton langs de raaklijn ($F_t = m v \frac{dv}{ds}$):
$$\int_{s_1}^{s_2} F_t \, ds = \int_{v_1}^{v_2} m v \, dv \implies \sum U_{1-2} = \frac{1}{2} m v_2^2 - \frac{1}{2} m v_1^2$$

Definiëren we de kinetische energie als $T = \frac{1}{2} m v^2$, dan luidt het fundamentele werkingsprincipe:

$$T_1 + \sum U_{1-2} = T_2$$

---

## 4. Vermogen en Rendement

- **Mechanisch Vermogen ($P$):** De hoeveelheid arbeid verricht per tijdseenheid (Watt, $\text{W} = \text{J/s}$):
  $$P = \frac{dU}{dt} = \mathbf{F} \cdot \frac{d\mathbf{r}}{dt} = \mathbf{F} \cdot \mathbf{v}$$
- **Mechanisch Rendement ($\epsilon$):**
  $$\epsilon = \frac{P_{\text{uit}}}{P_{\text{in}}} = \frac{E_{\text{nuttig}}}{E_{\text{toegevoerd}}} \le 1$$

---

## 📝 Samenvatting
- Arbeid en kinetische energie verbinden krachten rechtstreeks met snelheden en verplaatsingen zonder dat versnellingen expliciet berekend hoeven te worden.
- Zwaartekracht- en veerkrachten zijn conservatief; wrijving dissipeert mechanische energie als warmte.
