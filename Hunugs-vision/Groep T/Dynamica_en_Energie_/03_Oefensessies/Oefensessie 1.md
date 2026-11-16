---
course: "Dynamica en energie (T1ADE1)"
unit_type: oefensessie
status: todo
completed: false
est_hours: 2.0
priority: high
tags:
  - study-unit
---

# 🏋️ Oefensessie 1: Constante Versnelling en Cirkelbeweging

> [!info] Sessiedoelen
> - **Doel:** Oplossen van grafische kinematicaopgaven, tweedimensionale projectielbanen en gekoppelde cirkelbewegingsparameters.
> - **Theoretische Grondslag:** [[Chapter 1 - Constante Versnelling en Cirkelbeweging]].
> - **Relevante Formules:** [[Formularium#1. Kinematica van een Puntmassa (Rectilineair & Curvilineair)]].
> - **Sessie Status:** In behandeling (`[[Exercise Session Tracker]]`).

---

## 📑 Oefeningenoverzicht & Conceptuele Koppelingen

### Oefening 1.1 (Startniveau) — Verplaatsing uit $v(t)$-Profiel
- **Probleem:** Bepaal de totale afgelegde afstand totdat het object stopt op basis van een gegeven $v(t)$-profiel ($8\text{ m/s}$ gedurende $30\text{ s}$, daarna lineaire daling tot stilstand op $t = 60\text{ s}$).
- **Vereiste Theorie:** [[Chapter 1 - Constante Versnelling en Cirkelbeweging#3. Grafische Analyse van Bewegingen (s-t, v-t, a-t)]].
- **Sleutelrelatie:** $\Delta s = \int v\,dt = \text{Oppervlakte onder curve}$.
- **Eindresultaat:** $\Delta s_{0\to 30} = 240\text{ m}$, $\Delta s_{30\to 60} = 120\text{ m} \implies \Delta s_{\text{totaal}} = 360\text{ m}$.

---

### Oefening 1.2 (Startniveau) — $a(t)$-Grafiek met Omzetting van Eenheden
- **Probleem:** Een object start met $v_0 = 12\text{ km/u}$. Tussen $t = 0$ en $30\text{ s}$ geldt $a = +8\text{ m/s}^2$. Na $30\text{ s}$ geldt $a = -3\text{ m/s}^2$. Bepaal de maximale snelheid $v_{\max}$ en het tijdstip $t_{v=0}$ van stilstand.
- **Vereiste Theorie:**
  1. [[Chapter 1 - Constante Versnelling en Cirkelbeweging#2. Bewegingsvergelijkingen Constante Versnelling]].
  2. [[Begrippenlijst#Kinematica (Kinematics)]] & eenhedenconversie ($1\text{ km/u} = \frac{1}{3{,}6}\text{ m/s}$).
- **Eindresultaat:** $v_{\max} = 243{,}3\text{ m/s} = 876\text{ km/u}$, $t_{v=0} = 111{,}1\text{ s}$.

---

### Oefening 1.3 (Startniveau) — Kanonskogel Projectielbaan
- **Probleem:** Lancering met $v_0 = 450\text{ m/s}$ onder hoek $\theta = 30^\circ$ vanaf starthoogte $y_0 = 0{,}75\text{ m}$. Bepaal de vluchttijd tot inslag en de schootsafstand $d$.
- **Vereiste Theorie:** [[Chapter 1 - Constante Versnelling en Cirkelbeweging#4. Projectielbeweging 2D (Tweedimensionale Vrije Val)]].
- **Eindresultaat:** $t_{\text{vlucht}} = 45{,}9\text{ s}$, $d = 17{,}9\text{ km}$.

---

### Oefening 1.4 (Gemiddeld niveau) — Raket met Loslatende Boosters
- **Probleem:** Raket accelereert verticaal omhoog met $a = 15\text{ m/s}^2$ gedurende $30\text{ s}$. Boosters worden afgeworpen met een extra horizontale relatieve snelheid van $v_H = 40\text{ m/s}$ in tegengestelde richtingen. Bepaal de afstand tussen beide boosters bij inslag in de oceaan en de eindsnelheidsvector.
- **Vereiste Theorie:**
  1. [[Chapter 1 - Constante Versnelling en Cirkelbeweging#Bewegingsvergelijkingen Constante Versnelling]].
  2. [[Chapter 3 - Afhankelijke en Relatieve Beweging#Relatieve Beweging]].
- **Eindresultaat:** Afstand tussen boosters = $8{,}39\text{ km}$; eindsnelheid $\|\mathbf{v}\| = 580\text{ m/s}$.

---

### Oefening 1.5 (Moeilijk niveau) — Brekend Touw bij Cirkelbeweging
- **Probleem:** Bal draait met $v_0 = 2\text{ m/s}$ op een verticale cirkel ($R = 0{,}5\text{ m}$, as op hoogte $0{,}75\text{ m}$). Bij $\theta = 300^\circ$ breekt het touw. Bereken $\mathbf{a}$ voor en na breuk, het tijdstip van grondinslag en de inslagcoördinaat $x$.
- **Vereiste Theorie:**
  1. [[Chapter 1 - Constante Versnelling en Cirkelbeweging#5. Cirkelbeweging en Intrinsieke (t-n) Coördinaten]] ($a_n = v^2/R$).
  2. [[Chapter 1 - Constante Versnelling en Cirkelbeweging#4. Projectielbeweging 2D (Tweedimensionale Vrije Val)]].
- **Eindresultaat:** $\mathbf{a}_{\text{voor}} = 4\mathbf{i} + 6{,}93\mathbf{j}\text{ m/s}^2$, $\mathbf{a}_{\text{na}} = -9{,}81\mathbf{j}\text{ m/s}^2$, $t_{\text{grond}} = 1{,}68\text{ s}$, $x_{\text{grond}} = -0{,}89\text{ m}$.
