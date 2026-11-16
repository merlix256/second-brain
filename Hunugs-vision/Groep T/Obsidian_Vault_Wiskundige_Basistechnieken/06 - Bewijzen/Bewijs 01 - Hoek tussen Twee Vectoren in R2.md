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

# Bewijs 01: Hoek tussen Twee Vectoren in R2

> [!abstract] Context & Examenbelang
> **Theorievraag 1:** *"Formuleer en bewijs de uitdrukking voor de hoek tussen twee vectoren $u, v \in \mathbb{R}^2$."*
> **Verwante Theorie:** [[Ch 01 - Getallen, Punten en Vectoren#1.4 Afstand, hoek en poolcoördinaten in R2]]
> **Formularium:** [[Formularium#1. Analytische Meetkunde]] | **MOC:** [[00 - Index der Bewijzen]]

---

## 1. Formulering van de Stelling
Zij $u = [u_1, u_2]^T \in \mathbb{R}^2$ en $v = [v_1, v_2]^T \in \mathbb{R}^2$ twee niet-nulvectoren in het Cartesiaans vlak. De hoek $\theta \in [0, \pi]$ tussen $u$ en $v$ voldoet aan:
$$\cos\theta = \frac{u_1 v_1 + u_2 v_2}{\|u\| \|v\|} = \frac{u \cdot v}{\|u\| \|v\|}$$
of expliciet:
$$\theta = \arccos\left(\frac{u \cdot v}{\|u\| \|v\|}\right)$$

---

## 2. Grafische Representatie
![[Bewijs_01_Hoek_Tussen_Vectoren.png]]
*(Schets: Twee vectoren $u$ en $v$ met vertrekpunt in de oorsprong $O$. Hoogtelijn $h$ vanuit het eindpunt van $v$ loodrecht op de drager van $u$. Basisstukken $b_1$ en $b_2$, en de verschilvector $u - v$ die de eindpunten verbindt.)*

---

## 3. Stap-voor-stap Bewijs

### Stap 1: Uitdrukking via de Stelling van Pythagoras
Zonder verlies van algemeenheid veronderstellen we dat $\|u\| \ge \|v\|$ (indien niet, verwisselen we de rollen van $u$ en $v$, wat de hoek $\theta$ niet beïnvloedt). We ontbinden de driehoek gevormd door $u$, $v$ en $u - v$ met behulp van een hoogtelijn $h$ loodrecht op de drager van $u$:
- De hoogte van de rechthoekige driehoek is:
  $$h = \|v\| \sin\theta$$
- De projectie van $v$ op $u$ levert een basissegment:
  $$b_1 = \|v\| \cos\theta$$
- Het resterende basissegment $b_2$ van de rechthoekige driehoek met hypotenusa $\|u - v\|$ is:
  $$b_2 = \|u\| - b_1 = \|u\| - \|v\|\cos\theta \quad (\text{voor } 0 \le \theta \le \pi/2)$$
  *(Voor een stompe hoek $\pi/2 < \theta \le \pi$ is $b_2 = \|u\| + |b_1| = \|u\| - \|v\|\cos\theta$, aangezien $\cos\theta < 0$, waardoor de formule identiek blijft).*

Toepassing van de stelling van Pythagoras op deze rechthoekige driehoek geeft:
$$\|u - v\|^2 = h^2 + b_2^2$$
Substitutie van $h$ en $b_2$:
$$\|u - v\|^2 = (\|v\|\sin\theta)^2 + (\|u\| - \|v\|\cos\theta)^2$$
Uitwerken van het kwadraat:
$$\|u - v\|^2 = \|v\|^2 \sin^2\theta + \|u\|^2 - 2\|u\| \|v\| \cos\theta + \|v\|^2 \cos^2\theta$$
Gebruikmakend van de grondformule van de goniometrie $\sin^2\theta + \cos^2\theta = 1$:
$$\|u - v\|^2 = \|u\|^2 + \|v\|^2 - 2\|u\| \|v\| \cos\theta \quad \text{--- (Vergelijking 1)}$$

### Stap 2: Analytische Uitdrukking via de Norm in R2
Anderzijds kunnen we de norm van de verschilvector $u - v = [u_1 - v_1, \; u_2 - v_2]^T$ rechtstreeks analytisch berekenen:
$$\|u - v\|^2 = (u_1 - v_1)^2 + (u_2 - v_2)^2$$
Uitwerken van de tweetermen:
$$\|u - v\|^2 = (u_1^2 - 2 u_1 v_1 + v_1^2) + (u_2^2 - 2 u_2 v_2 + v_2^2)$$
Herschikken van de termen:
$$\|u - v\|^2 = (u_1^2 + u_2^2) + (v_1^2 + v_2^2) - 2(u_1 v_1 + u_2 v_2)$$
Aangezien $\|u\|^2 = u_1^2 + u_2^2$ en $\|v\|^2 = v_1^2 + v_2^2$:
$$\|u - v\|^2 = \|u\|^2 + \|v\|^2 - 2(u_1 v_1 + u_2 v_2) \quad \text{--- (Vergelijking 2)}$$

### Stap 3: Gelijkstelling en Conclusie
Stel Vergelijking 1 en Vergelijking 2 aan elkaar gelijk:
$$\|u\|^2 + \|v\|^2 - 2\|u\| \|v\| \cos\theta = \|u\|^2 + \|v\|^2 - 2(u_1 v_1 + u_2 v_2)$$
Schrap $\|u\|^2 + \|v\|^2$ aan weerszijden:
$$-2\|u\| \|v\| \cos\theta = -2(u_1 v_1 + u_2 v_2)$$
Deel beide leden door $-2$:
$$\|u\| \|v\| \cos\theta = u_1 v_1 + u_2 v_2$$
Aangezien $u \neq \mathbf{0}$ en $v \neq \mathbf{0}$, geldt $\|u\| \|v\| \neq 0$. Delen door $\|u\| \|v\|$ levert:
$$\cos\theta = \frac{u_1 v_1 + u_2 v_2}{\|u\| \|v\|}$$
En bijgevolg, vermits $\theta \in [0, \pi]$:
$$\theta = \arccos\left(\frac{u \cdot v}{\|u\| \|v\|}\right) \quad \blacksquare$$

---

## 4. Examenvalkuilen & Aandachtspunten
- **Scherpe vs. Stompe hoek:** Vermeld expliciet dat de formule geldig is voor zowel scherpe als stompe hoeken. Teken eventueel beide gevallen of verklaar waarom het teken van $\cos\theta$ het verschil in $b_2$ automatisch opvangt.
- **Definitie van het Inproduct:** Merk op dat deze meetkundige afleiding de fundering vormt voor de algebraïsche definitie van het inproduct $u \cdot v = u_1 v_1 + u_2 v_2$.
