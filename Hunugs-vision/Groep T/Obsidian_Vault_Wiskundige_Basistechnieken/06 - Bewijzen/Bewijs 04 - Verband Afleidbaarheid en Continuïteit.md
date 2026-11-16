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

# Bewijs 04: Verband tussen Afleidbaarheid en Continuïteit

> [!abstract] Context & Examenbelang
> **Theorievraag 4:** *"Definieer en bewijs het verband tussen afleidbaarheid en continuïteit van een functie $f(x)$ in een punt $x_1$."*
> **Verwante Theorie:** [[Ch 05 - Afgeleiden en Toepassingen#1. Definitie en Betekenis van de Afgeleide]]
> **Formularium:** [[Formularium#3. Analyse]] | **MOC:** [[00 - Index der Bewijzen]]

---

## 1. Formulering van de Stelling
Zij $f: D \subseteq \mathbb{R} \to \mathbb{R}$ een functie en $x_1 \in D$.
**Stelling:** Als de functie $f(x)$ afleidbaar (differentieerbaar) is in het punt $x_1$, dan is $f(x)$ ook continu in het punt $x_1$.

> [!warning] Belangrijke Opmerking over het Omgekeerde
> Het omgekeerde geldt in het algemeen **niet**: continuïteit in een punt impliceert geenszins dat de functie in dat punt afleidbaar is.

---

## 2. Grafische Representatie & Tegenvoorbeeld
![[Bewijs_04_Afleidbaarheid_Continuiteit.png]]
*(Schets: Links: Gladde curve met raaklijn in $x_1$, waaruit blijkt dat de functiewaarde geleidelijk nadert zonder sprong. Rechts: De functie $f(x) = |x|$ in $x = 0$, die continu is maar een knik vertoont waardoor de linker- en rechterafgeleide verschillen).*

---

## 3. Stap-voor-stap Bewijs

### Stap 1: Gegeven en te Bewijzen Definiëren
- **Gegeven:** $f$ is afleidbaar in $x_1$. Dit betekent dat de limiet van het differentiequotiënt bestaat en eindig is:
  $$f'(x_1) = \lim_{\Delta x \to 0} \frac{f(x_1 + \Delta x) - f(x_1)}{\Delta x}$$
- **Te bewijzen:** $f$ is continu in $x_1$, hetgeen per definitie betekent dat:
  $$\lim_{x \to x_1} f(x) = f(x_1) \iff \lim_{\Delta x \to 0} f(x_1 + \Delta x) = f(x_1) \iff \lim_{\Delta x \to 0} [f(x_1 + \Delta x) - f(x_1)] = 0$$

### Stap 2: Algebraïsche Herschrijving van het Verschil
Voor elke $\Delta x \neq 0$ kunnen we de toename $f(x_1 + \Delta x) - f(x_1)$ identiek vermenigvuldigen en delen door $\Delta x$:
$$f(x_1 + \Delta x) - f(x_1) = \frac{f(x_1 + \Delta x) - f(x_1)}{\Delta x} \cdot \Delta x$$

### Stap 3: Limietovergang voor $\Delta x \to 0$
We nemen nu de limiet voor $\Delta x \to 0$ van beide leden:
$$\lim_{\Delta x \to 0} [f(x_1 + \Delta x) - f(x_1)] = \lim_{\Delta x \to 0} \left[ \frac{f(x_1 + \Delta x) - f(x_1)}{\Delta x} \cdot \Delta x \right]$$
Aangezien de limiet van een product gelijk is aan het product van de limieten (wanneer beide limieten bestaan):
$$\lim_{\Delta x \to 0} [f(x_1 + \Delta x) - f(x_1)] = \left( \lim_{\Delta x \to 0} \frac{f(x_1 + \Delta x) - f(x_1)}{\Delta x} \right) \cdot \left( \lim_{\Delta x \to 0} \Delta x \right)$$
Wegens de hypothese is de eerste factor gelijk aan de eindige afgeleide $f'(x_1)$, en de tweede factor is triviaal 0:
$$\lim_{\Delta x \to 0} [f(x_1 + \Delta x) - f(x_1)] = f'(x_1) \cdot 0 = 0$$

### Stap 4: Conclusie
Hieruit volgt onmiddellijk:
$$\lim_{\Delta x \to 0} f(x_1 + \Delta x) - \lim_{\Delta x \to 0} f(x_1) = 0 \iff \lim_{\Delta x \to 0} f(x_1 + \Delta x) = f(x_1)$$
Substitutie van $x = x_1 + \Delta x$ (waarbij $x \to x_1$ als $\Delta x \to 0$) levert:
$$\lim_{x \to x_1} f(x) = f(x_1)$$
Bijgevolg is $f(x)$ continu in het punt $x_1$. $\blacksquare$

---

## 4. Tegenvoorbeeld voor het Omgekeerde (Examenvereiste!)
Beschouw de functie $f(x) = |x|$ in het punt $x_1 = 0$:
1. **Continuïteit:**
   $$\lim_{x \to 0} |x| = 0 = f(0)$$
   De functie is dus perfect continu in $x = 0$.
2. **Niet-afleidbaarheid:**
   Bereken de linker- en rechterlimiet van het differentiequotiënt in $x = 0$:
   - Linkerafgeleide:
     $$f'_-(0) = \lim_{\Delta x \to 0^-} \frac{|\Delta x| - 0}{\Delta x} = \lim_{\Delta x \to 0^-} \frac{-\Delta x}{\Delta x} = -1$$
   - Rechterafgeleide:
     $$f'_+(0) = \lim_{\Delta x \to 0^+} \frac{|\Delta x| - 0}{\Delta x} = \lim_{\Delta x \to 0^+} \frac{\Delta x}{\Delta x} = +1$$
   Omdat $f'_-(0) \neq f'_+(0)$, bestaat $f'(0)$ niet. $f$ is continu maar niet afleidbaar in 0.
