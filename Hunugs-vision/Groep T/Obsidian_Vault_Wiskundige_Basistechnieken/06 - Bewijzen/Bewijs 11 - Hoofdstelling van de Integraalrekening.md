---
course: "Wiskundige basistechnieken (T1AWB1)"
unit_type: bewijs
status: todo
completed: false
est_hours: 1.0
priority: high
tags:
  - study-unit
---

# Bewijs 11: Hoofdstelling van de Integraalrekening

> [!abstract] Context & Examenbelang
> **Theorievraag 11:** *"Formuleer en bewijs de hoofdstelling van de integraalrekening (hulpstelling + hoofdstelling)."*
> **Verwante Theorie:** [[Ch 07 - Bepaalde Integralen#2. Hoofdstelling van de Integraalrekening]]
> **Formularium:** [[Formularium#3. Analyse]] | **MOC:** [[00 - Index der Bewijzen]]

---

## 1. De Hulpstelling (Differentiatie van de Oppervlaktefunctie)

### 1.1 Formulering van de Hulpstelling
Zij $f: [a, b] \to \mathbb{R}$ een continue functie op het gesloten interval $[a, b]$, en zij $k \in [a, b]$ een vast referentiepunt.
Dan is de functie $F: [a, b] \to \mathbb{R}$ gedefinieerd door:
$$F(x) = \int_k^x f(t) \, dt$$
een primitieve functie van $f$ op $[a, b]$, hetgeen betekent dat:
$$F'(x) = \frac{d}{dx} \left[ \int_k^x f(t) \, dt \right] = f(x) \quad (\forall x \in [a, b])$$

### 1.2 Grafische Representatie van de Hulpstelling
![[Bewijs_11_Hulpstelling_Integraal.png]]
*(Schets: Oppervlakte onder $f(t)$ vanaf $k$ tot $x$. Een kleine toename $\Delta x$ geeft een oppervlaktestrook met oppervlakte $F(x + \Delta x) - F(x) = \int_x^{x + \Delta x} f(t) \, dt$, die volgens de middelwaardestelling gelijk is aan een rechthoek met breedte $\Delta x$ en hoogte $f(c)$ met $c \in [x, x + \Delta x]$.)*

### 1.3 Bewijs van de Hulpstelling
We berekenen de afgeleide van $F(x)$ via de definitie van het differentiequotiënt:
$$F'(x) = \lim_{\Delta x \to 0} \frac{F(x + \Delta x) - F(x)}{\Delta x}$$
Bereken de functietoename in de teller:
$$F(x + \Delta x) - F(x) = \int_k^{x + \Delta x} f(t) \, dt - \int_k^x f(t) \, dt$$
Gebruikmakend van de additiviteit van de integratiegrenzen ($\int_k^x + \int_x^{x + \Delta x} = \int_k^{x + \Delta x}$):
$$F(x + \Delta x) - F(x) = \int_x^{x + \Delta x} f(t) \, dt$$
Omdat $f(t)$ continu is op het interval $[x, x + \Delta x]$, kunnen we de **Middelwaardestelling van de Integraalrekening** toepassen:
Er bestaat minstens één punt $c \in [x, x + \Delta x]$ zodanig dat:
$$\int_x^{x + \Delta x} f(t) \, dt = f(c) \cdot \Delta x$$
Substitueer dit in het differentiequotiënt:
$$\frac{F(x + \Delta x) - F(x)}{\Delta x} = \frac{f(c) \cdot \Delta x}{\Delta x} = f(c)$$
Neem nu de limiet voor $\Delta x \to 0$. Omdat $c$ ingeklemd ligt tussen $x$ en $x + \Delta x$, geldt:
$$\Delta x \to 0 \implies c \to x$$
Wegens de continuïteit van de functie $f$ in het punt $x$ volgt:
$$\lim_{c \to x} f(c) = f(x)$$
Bijgevolg is:
$$F'(x) = \lim_{\Delta x \to 0} f(c) = f(x)$$
Dit bewijst dat $F(x)$ een primitieve functie is van $f(x)$ op $[a, b]$. $\blacksquare$

---

## 2. De Hoofdstelling van de Integraalrekening (Newton-Leibniz)

### 2.1 Formulering van de Hoofdstelling
Zij $f: [a, b] \to \mathbb{R}$ een continue functie op $[a, b]$, en zij $G(x)$ een **willekeurige** primitieve functie van $f$ op $[a, b]$ (d.w.z. $G'(x) = f(x)$). Dan geldt:
$$\int_a^b f(x) \, dx = G(b) - G(a) = \Big[ G(x) \Big]_a^b$$

### 2.2 Bewijs van de Hoofdstelling
1. Volgens de Hulpstelling is de functie $F(x) = \int_a^x f(t) \, dt$ een primitieve functie van $f(x)$ op $[a, b]$.
2. Zij $G(x)$ een willekeurige andere primitieve functie van $f(x)$ op $[a, b]$.
3. Twee primitieve functies van dezelfde functie verschillen op een interval slechts door een constante $C \in \mathbb{R}$:
   $$G(x) = F(x) + C = \int_a^x f(t) \, dt + C$$
4. We bepalen de constante $C$ door het punt $x = a$ in te vullen:
   $$G(a) = \int_a^a f(t) \, dt + C = 0 + C = C \implies C = G(a)$$
5. De uitdrukking voor $G(x)$ wordt dus:
   $$G(x) = \int_a^x f(t) \, dt + G(a)$$
6. Vul nu $x = b$ in:
   $$G(b) = \int_a^b f(t) \, dt + G(a)$$
7. Isoleer de bepaalde integraal:
   $$\int_a^b f(t) \, dt = G(b) - G(a) \quad \blacksquare$$

---

## 3. Examenvalkuilen & Aandachtspunten
- **Hulpstelling én Hoofdstelling:** Zorg dat je beide delen structureel uitschrijft. De vraag vereist expliciet de Hulpstelling (het bewijs dat de integraal met variabele bovengrens afleidbaar is en $f(x)$ oplevert) als opstap voor de Hoofdstelling van Newton-Leibniz.
- **De rol van de Middelwaardestelling:** Noem expliciet de Middelwaardestelling van de Integraalrekening en vermeld de continuïteitseis van $f$ waardoor $\lim_{c \to x} f(c) = f(x)$.
