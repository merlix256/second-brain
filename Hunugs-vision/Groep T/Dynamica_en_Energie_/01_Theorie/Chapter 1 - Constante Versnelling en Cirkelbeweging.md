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

# 📖 Hoofdstuk 1: Constante Versnelling en Uniforme Cirkelbeweging

> [!abstract] Overzicht & Leerdoelen
> - **Leerdoel:** Het wiskundig en fysisch beschrijven van rechtlijnige bewegingen onder invloed van een constante versnelling, inclusief tweedimensionale val- en projectielbewegingen en vlakke cirkelbewegingen.
> - **Handboek:** Hibbeler Chapter 12 (§12.1 – §12.6).
> - **Master Formularium:** [[Formularium#1. Kinematica van een Puntmassa (Rectilineair & Curvilineair)]].
> - **Actieve Herroeping:** [[Chapter 1 - Q&A]].

---

## 1. Inleiding en Puntmassa-Hypothese

In de kinematica bestuderen we de geometrie van de beweging zonder de oorzakelijke krachten in beschouwing te nemen. We modelleren een voorwerp als een **puntmassa (particle)** wanneer:
1. De ruimtelijke afmetingen en geometrische vorm geen invloed hebben op de dynamische respons van de baan.
2. De beweging volledig kan worden gekarakteriseerd door de translatie van het massamiddelpunt $G$, waarbij rotaties rondom het zwaartepunt verwaarloosbaar zijn.

---

## 2. Bewegingsvergelijkingen Constante Versnelling

Wanneer de versnelling constant is ($a(t) = a_c = \text{constant}$), kunnen de fundamentele differentiaalvergelijkingen analytisch worden geïntegreerd tussen tijdstip $t=0$ (met beginvoorwaarden $s(0) = s_0$ en $v(0) = v_0$) en tijdstip $t$:

### 2.1 Snelheid als functie van de tijd
Vertrekkend van de definitie van versnelling:
$$a_c = \frac{dv}{dt} \implies \int_{v_0}^{v} dv = \int_{0}^{t} a_c \, dt \implies v(t) = v_0 + a_c t$$

### 2.2 Positie als functie van de tijd
Substitutie van $v(t) = \frac{ds}{dt}$ geeft:
$$\frac{ds}{dt} = v_0 + a_c t \implies \int_{s_0}^{s} ds = \int_{0}^{t} (v_0 + a_c t) \, dt \implies s(t) = s_0 + v_0 t + \frac{1}{2} a_c t^2$$

### 2.3 Tijdsonafhankelijk verband tussen snelheid en positie
Door eliminatie van de parameter $t$ ($t = \frac{v - v_0}{a_c}$) in de positievergelijking verkrijgen we de kwadratische snelheidsrelatie:
$$v^2 = v_0^2 + 2 a_c (s - s_0)$$

> [!danger] Cruciale Voorwaarde
> Deze drie formules gelden **uitsluitend** indien $a_c$ strikt constant is in de tijd en over het traject. Indien $a = f(t)$, $a = f(s)$ of $a = f(v)$, zijn deze vergelijkingen ongeldig en moet direct geïntegreerd worden (zie [[Chapter 2 - Variabele Versnelling#Differentiële Grondrelaties]]).

---

## 3. Grafische Analyse van Bewegingen ($s-t$, $v-t$, $a-t$)

Bij discontinue of stuksgewijs constante fasen wordt de beweging vaak grafisch voorgesteld:

![[Slide_v_t_Graph_Oefening1_1.png]]
*(Placeholder: $v(t)$-grafiek met constante snelheid gevolgd door lineaire vertraging)*

- **Oppervlakte onder de $v(t)$-curve:** Representeert de netto verplaatsing over het tijdsinterval $[t_1, t_2]$:
  $$\Delta s = s(t_2) - s(t_1) = \int_{t_1}^{t_2} v(t) \, dt$$
- **Oppervlakte onder de $a(t)$-curve:** Representeert de snelheidsverandering over het tijdsinterval $[t_1, t_2]$:
  $$\Delta v = v(t_2) - v(t_1) = \int_{t_1}^{t_2} a(t) \, dt$$
- **Helling (Afgeleide):** De raaklijn aan de $s(t)$-curve levert de momentane snelheid $v = \dot{s}$; de raaklijn aan de $v(t)$-curve levert de momentane versnelling $a = \dot{v}$.

---

## 4. Projectielbeweging 2D (Tweedimensionale Vrije Val)

Een projectiel dat onderhevig is aan uitsluitend de zwaartekrachtversnelling $\mathbf{g}$ (waarbij luchtweerstand verwaarloosd wordt) voert een ontkoppelde tweedimensionale beweging uit:

![[Figuur_1_3_Kanon_Projectiel.png]]
*(Placeholder: Ballistische baan van een kanonskogel met lanceerhoek $\alpha$ en hoogteverschil)*

Kiezen we een orthonormaal assenstelsel met de $x$-as horizontaal en de $y$-as verticaal omhoog gericht:
$$\mathbf{a} = a_x \mathbf{i} + a_y \mathbf{j} = 0 \mathbf{i} - g \mathbf{j}$$

### Bewegingsvergelijkingen per as:
1. **Horizontale as ($x$):** Eenparig rechtlijnige beweging ($a_x = 0$):
   $$v_x(t) = v_{0x} = v_0 \cos\theta$$
   $$x(t) = x_0 + (v_0 \cos\theta) t$$
2. **Verticale as ($y$):** Eenparig veranderlijke beweging met constante valversnelling ($a_y = -g$):
   $$v_y(t) = v_{0y} - g t = v_0 \sin\theta - g t$$
   $$y(t) = y_0 + (v_0 \sin\theta) t - \frac{1}{2} g t^2$$
   $$v_y^2 = v_{0y}^2 - 2 g (y - y_0)$$

---

## 5. Cirkelbeweging en Intrinsieke ($t-n$) Coördinaten

Voor een deeltje dat een cirkelvormig pad beschrijft met straal $R = \rho$, wordt de versnellingsvector $\mathbf{a}$ ontbonden volgens het intrinsieke lokale assenstelsel $(\mathbf{u}_t, \mathbf{u}_n)$:

![[Slide_Intrinsieke_Assen_Cirkel.png]]
*(Placeholder: Baan van een deeltje op een cirkel met eenheidsvectoren $u_t$ rakend en $u_n$ loodrecht naar het centrum gericht)*

$$\mathbf{a} = a_t \mathbf{u}_t + a_n \mathbf{u}_n$$

1. **Tangentiële versnellingscomponent ($a_t$):** Wijst rakend aan de baan en kwantificeert de verandering in snelheidshoogte (magnitude):
   $$a_t = \frac{dv}{dt} = \dot{v}$$
2. **Normale versnellingscomponent ($a_n$):** Wijst loodrecht op de baan naar het krommingsmiddelpunt en kwantificeert de richtingsverandering:
   $$a_n = \frac{v^2}{\rho} = \frac{v^2}{R}$$
3. **Totale versnellingsgrootte:**
   $$\|\mathbf{a}\| = \sqrt{a_t^2 + a_n^2}$$

Bij een **uniforme cirkelbeweging (UCM)** is de baansnelheid constant ($v = \text{const}$), waardoor $a_t = 0$ en de versnelling zuiver normaal (centripetaal) gericht is: $\mathbf{a} = \frac{v^2}{R} \mathbf{u}_n$.

---

## 📝 Samenvatting
- Constante versnelling laat directe integratie toe naar eenvoudige algebraïsche relaties voor $s(t)$, $v(t)$ en $v^2(s)$.
- Oppervlakten onder curves leveren fysische overdrachten op: $\int v\,dt = \Delta s$ en $\int a\,dt = \Delta v$.
- Ballistische projectielbanen ontkoppelen volledig in een horizontale beweging met constante snelheid en een verticale valbeweging onder invloed van $g$.
- Bij kromlijnige paden induceert de verandering van richtingsvector altijd een centripetale versnelling $a_n = v^2/\rho$, zelfs wanneer de snelheid scalair constant blijft.
