---
course: "Dynamica en energie (T1ADE1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.0
priority: medium
tags:
  - study-unit
---

# ❓ Active Recall Q&A: Hoofdstuk 5

> [!tip] Instructie
> Test je inzicht in de kinetica van gekromde banen en normaal-tangentiële projecties.

---

### Vraag 5.1: Loslatingsconditie op een Heuvel
**Vraag:** Een wagen met massa $m$ rijdt over een cirkelvormige heuvel met kromtestraal $\rho = 50\text{ m}$. Welke maximale snelheid $v$ mag de wagen in de top van de heuvel hebben zonder dat de wielen loskomen van het wegdek?

> [!success]- Toon Uitwerking & Verwijzing
> **Antwoord:** $v_{\max} = 22{,}15\text{ m/s} \approx 79{,}7\text{ km/u}$.
> **Stapsgewijze berekening:**
> 1. VLS in de top: De zwaartekracht $W = mg$ wijst omlaag (naar het krommingscentrum, langs de normale as $\mathbf{u}_n$). De normaalkracht $N$ wijst omhoog (weg van het centrum).
> 2. Bewegingsvergelijking langs de normale as (positief naar het centrum):
>    $$\sum F_n = m a_n \implies mg - N = m \frac{v^2}{\rho}$$
> 3. Loslaten treedt op wanneer het contact verdwijnt $\implies N = 0$:
>    $$mg - 0 = m \frac{v^2}{\rho} \implies g = \frac{v^2}{\rho} \implies v = \sqrt{g\rho}$$
> 4. Numeriek:
>    $$v = \sqrt{9{,}81 \times 50} = \sqrt{490{,}5} = 22{,}15\text{ m/s}$$
> 👉 *Theorie review:* [[Chapter 5 - Kinetica Newton t-n Stelsels#3. Typische Examenthema's: Looping en Loslaten]].

---

### Vraag 5.2: Normaalkracht in een Looping
**Vraag:** Waarom is de normaalkracht $N$ op een bobslee in het laagste punt van een looping altijd veel groter dan het statische gewicht $mg$?

> [!success]- Toon Uitwerking & Verwijzing
> **Antwoord:**
> In het laagste punt wijst het krommingsmiddelpunt verticaal omhoog. De normale as $\mathbf{u}_n$ is dus naar boven gericht.
> De bewegingsvergelijking luidt:
> $$\sum F_n = m a_n \implies N - mg = m \frac{v^2}{\rho} \implies N = mg + m \frac{v^2}{\rho}$$
> De baan moet niet alleen het statische gewicht dragen, maar tevens de vereiste opwaartse centripetale versnelling leveren om de bobslee uit zijn rechte lijn in de bocht te dwingen.
> 👉 *Theorie review:* [[Chapter 5 - Kinetica Newton t-n Stelsels#2. Bewegingsvergelijkingen in t-n-b]].
