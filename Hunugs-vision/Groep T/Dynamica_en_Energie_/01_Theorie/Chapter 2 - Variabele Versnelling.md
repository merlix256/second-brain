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

# 📖 Hoofdstuk 2: Variabele Versnelling en Kromlijnige Kinematica

> [!abstract] Overzicht & Leerdoelen
> - **Leerdoel:** Het beheersen van de analytische integratietechnieken voor niet-constante versnellingsfuncties $a(t)$, $a(s)$, en $a(v)$, alsook de algebraïsche bepaling van de kromtestraal $\rho$ en curvilineaire versnellingscomponenten.
> - **Handboek:** Hibbeler Chapter 12 (§12.2, §12.3, §12.7, §12.10).
> - **Master Formularium:** [[Formularium#1. Kinematica van een Puntmassa (Rectilineair & Curvilineair)]].
> - **Actieve Herroeping:** [[Chapter 2 - Q&A]].

---

## 1. Differentiële Grondrelaties

Wanneer de versnelling varieert, zijn de algebraïsche formules uit Hoofdstuk 1 ongeldig. De exacte beweging moet worden afgeleid uit de drie fundamentele definities:

1. **Snelheid:**
   $$v = \frac{ds}{dt} \implies ds = v\,dt$$
2. **Versnelling:**
   $$a = \frac{dv}{dt} = \frac{d^2s}{dt^2} \implies dv = a\,dt$$
3. **Kettingregel (tijdsonafhankelijke differentiaalvorm):**
   $$a = \frac{dv}{dt} = \frac{dv}{ds} \frac{ds}{dt} = v \frac{dv}{ds} \implies a\,ds = v\,dv$$

---

## 2. Integratieschema's per Versnellingsafhankelijkheid

De keuze van de integratiestrategie wordt gedicteerd door de wiskundige vorm van $a$:

```
Vorm van de versnelling:
├── a = f(t) ──> Scheid variabelen: dv = f(t) dt  ──> Integreer v(t), daarna ds = v(t) dt
├── a = f(s) ──> Gebruik a ds = v dv              ──> Integreer f(s) ds = v dv naar v(s)
└── a = f(v) ──> Keuze:
                 ├── Naar de tijd t:      dt = dv / f(v)  ──> Integreer naar t(v)
                 └── Naar de positie s:   ds = v dv / f(v)──> Integreer naar s(v)
```

### 2.1 Versnelling als functie van de tijd: $a = f(t)$
$$\int_{v_0}^{v} dv = \int_{0}^{t} f(t)\,dt \implies v(t) = v_0 + \int_{0}^{t} f(t)\,dt$$
$$\int_{s_0}^{s} ds = \int_{0}^{t} v(t)\,dt \implies s(t) = s_0 + \int_{0}^{t} v(t)\,dt$$

### 2.2 Versnelling als functie van de positie: $a = f(s)$
$$\int_{v_0}^{v} v\,dv = \int_{s_0}^{s} f(s)\,ds \implies \frac{1}{2}(v^2 - v_0^2) = \int_{s_0}^{s} f(s)\,ds$$
Zodra $v(s)$ bekend is, volgt de tijd via:
$$dt = \frac{ds}{v(s)} \implies t = \int_{s_0}^{s} \frac{ds}{v(s)}$$

### 2.3 Versnelling als functie van de snelheid: $a = f(v)$
- Tijdsverloop:
  $$dt = \frac{dv}{f(v)} \implies t = \int_{v_0}^{v} \frac{dv}{f(v)}$$
- Positieverloop:
  $$ds = \frac{v\,dv}{f(v)} \implies s - s_0 = \int_{v_0}^{v} \frac{v\,dv}{f(v)}$$

---

## 3. Curvilineaire Ontbinding ($t-n$ Stelsel)

Voor een willekeurig 2D-pad $\mathbf{r}(t)$ definiëren we op elk punt een osculerend vlak opgespannen door:
- De raaklijn (tangens) met eenheidsvector $\mathbf{u}_t = \frac{\mathbf{v}}{\|\mathbf{v}\|}$.
- De normaalvector $\mathbf{u}_n$, loodrecht op $\mathbf{u}_t$ en wijzend naar de holle zijde (het krommingscentrum $O'$).

![[Slide_Osculerende_Cirkel_Kromtestraal.png]]
*(Placeholder: Osculerende cirkel met raaklijn, kromtestraal $\rho$ en centrum $O'$)*

$$\mathbf{v} = v \mathbf{u}_t$$
$$\mathbf{a} = \dot{\mathbf{v}} = \frac{d(v\mathbf{u}_t)}{dt} = \dot{v} \mathbf{u}_t + v \dot{\mathbf{u}}_t = a_t \mathbf{u}_t + a_n \mathbf{u}_n$$
waarbij:
$$a_t = \dot{v} = \frac{dv}{dt} = v \frac{dv}{ds}$$
$$a_n = \frac{v^2}{\rho}$$

---

## 4. Kromtestraal van een Pad: $\rho$

Wanneer het traject analytisch gegeven is in cartesische coördinaten als $y = f(x)$, kan de kromtestraal $\rho$ op elk punt berekend worden via de differentiaalmeetkunde:

$$\rho = \frac{\left[1 + \left(\frac{dy}{dx}\right)^2\right]^{3/2}}{\left|\frac{d^2y}{dx^2}\right|}$$

> [!tip] Praktische Toepassing
> In een hoogste punt (top van een parabool $\frac{dy}{dx} = 0$) vereenvoudigt de uitdrukking tot:
> $$\rho = \frac{1}{\left|\frac{d^2y}{dx^2}\right|}$$

---

## 📝 Samenvatting
- Bij variabele versnelling is differentiëren en integreren de enige wiskundig sluitende methode.
- De universele schakelvergelijking $a\,ds = v\,dv$ koppelt kinetische variabelen zonder expliciete tijdsafhankelijkheid.
- De normale versnelling $a_n = v^2/\rho$ ontstaat zuiver door koerswijziging; de kromtestraal $\rho$ volgt uit de 1e en 2e afgeleide van de geometrische padvergelijking $y(x)$.
