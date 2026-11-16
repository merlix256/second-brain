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

# 🔬 H17: Vermoeiing en Dynamische Belasting
#theorie #vermoeiing #woehler #S-N #goodman #striaties #H17

[[00_Overview_Dashboard]] | [[01_Formularium_Master#7-vermoeiing-dynamische-belasting]] | [[05_Oefenzittingen/Sessie_05_Breukmechanica_Vermoeiing_Kruip]]

---

## 1. Karakteristieken van Dynamische Belasting
Vermoeiing is falen onder herhaalde of wisselende spanningen die ruim onder de statische vloeigrens $\sigma_y$ liggen:
* Spanningsamplitude: $\sigma_a = \frac{\sigma_{\max} - \sigma_{\min}}{2}$
* Gemiddelde spanning: $\sigma_m = \frac{\sigma_{\max} + \sigma_{\min}}{2}$
* Spanningsinterval: $\Delta \sigma = \sigma_{\max} - \sigma_{\min} = 2\sigma_a$
* Spanningsverhouding: $R = \frac{\sigma_{\min}}{\sigma_{\max}}$ (voor symmetrisch wisselend geldt $R = -1$).

---

## 2. De Wöhler S-N Curve & Vermoeiingsgrens
In een Wöhler-proef wordt de spanningsamplitude $\sigma_a$ uitgezet tegen het aantal cycli tot breuk ($N$, logaritmische schaal):

```
 Spanning σa
     ^
     | \
     |   \  (Aluminium: geen grens, blijft dalen)
     |     \________
 σe  |..............----------------- (Staal: Vermoeiingsgrens)
     |
     +---------+-----------+----------> Cycli N (log)
              10^5        10^6      10^7
```

* **Vermoeiingsgrens (Fatigue Limit / Endurance Limit $\sigma_e$)**: Spanning waaronder het materiaal een theoretisch oneindige levensduur heeft ($N > 10^7$). Typisch voor **ferritisch staal** en titanium. Vuistregel: $\sigma_e \approx 0.35 - 0.50 \times \sigma_{\text{UTS}}$.
* **Niet-ijzerlegeringen (Al, Cu, Mg)**: Vertoont **geen** horizontale asymptoot! De curve blijft continu dalen. Hier specificeert men een "vermoeiingssterkte" voor een afgesproken aantal cycli (bijv. $10^7$ of $10^8$).

---

## 3. Invloed van Gemiddelde Spanning ($\sigma_m$)
Een statische trekspanning ($\sigma_m > 0$) versnelt scheuropening en verlaagt de toelaatbare amplitude $\sigma_a$:
* **Goodman-relatie**:
  $$\frac{\sigma_a}{\sigma_{a0}} + \frac{\sigma_m}{\sigma_{\text{UTS}}} = 1$$
* **Miner's Regel voor Cumulatieve Schade**:
  Bij variërende belastingsblokken ($n_i$ cycli bij spanningsniveau met levensduur $N_i$):
  $$\sum_{i=1}^k \frac{n_i}{N_i} = 1$$

---

## 4. De 3 Stadia van Vermoeiingsbreuk
1. **Stadium I (Initiatie)**: Ontstaat aan oppervlakte-oneffenheden, kerven of insluitsels door lokale dislocatie-afschuiving (extrusion/intrusion).
2. **Stadium II (Voortplanting)**: Scheur groeit loodrecht op de trekbelasting met microscopische vermoeiingsribbels (**striaties** — elke cyclus produceert één striatie) en macroscopische strandlijnen (**beach marks**).
3. **Stadium III (Restbreuk)**: De dragende dwarsdoorsnede wordt zó klein dat $K_I \ge K_{Ic} \implies$ plotse, brosse restbreuk!

---

> [!summary] Hoofdstuksamenvatting
> Vermoeiing veroorzaakt meer dan 80% van mechanische breuken in de praktijk. Staal vertoont een veilige vermoeiingsgrens, terwijl aluminiumlegeringen bij elke spanningswaarde op termijn bezwijken.
