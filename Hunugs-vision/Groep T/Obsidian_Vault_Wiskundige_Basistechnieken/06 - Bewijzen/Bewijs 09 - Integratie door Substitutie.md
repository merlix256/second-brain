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

# Bewijs 09: Integratie door Substitutie

> [!abstract] Context & Examenbelang
> **Theorievraag 9:** *"Formuleer en bewijs de stelling waarop integratie door substitutie gebaseerd is."*
> **Verwante Theorie:** [[Ch 06 - Onbepaalde Integralen#2. Oplossingsmethoden]]
> **Formularium:** [[Formularium#3. Analyse]] | **MOC:** [[00 - Index der Bewijzen]]

---

## 1. Formulering van de Stelling
Zij $u = g(x)$ een continu afleidbare (differentieerbare) functie van $x$ op een interval $I$, en zij $f(u)$ een continue functie op het beeld $g(I)$.
Dan geldt:
$$\int f(g(x)) \cdot g'(x) \, dx = \int f(u) \, du$$
waarbij $u = g(x)$ en $du = g'(x) \, dx$.

---

## 2. Stap-voor-stap Bewijs

### Stap 1: Introductie van een Primitieve Functie
Zij $F(u)$ een willekeurige primitieve functie van $f(u)$ op het beeld $g(I)$.
Volgens de definitie van een primitieve functie geldt:
$$F'(u) = \frac{dF}{du} = f(u) \iff dF = F'(u) \, du = f(u) \, du$$
Bijgevolg is:
$$\int f(u) \, du = F(u) + C$$

### Stap 2: Samengestelde Functie en Kettingregel
Beschouw nu de samengestelde functie van $x$:
$$H(x) = (F \circ g)(x) = F(g(x))$$
Omdat $F$ en $g$ afleidbaar zijn, is $H(x)$ afleidbaar volgens de kettingregel:
$$\frac{d}{dx}[H(x)] = \frac{d}{dx}[F(g(x))] = F'(g(x)) \cdot g'(x)$$
Substitueer $F'(u) = f(u)$ met $u = g(x)$:
$$\frac{d}{dx}[F(g(x))] = f(g(x)) \cdot g'(x)$$

### Stap 3: Differentiaalnotatie
In termen van differentialen betekent dit:
$$d[F(g(x))] = f(g(x)) \cdot g'(x) \, dx$$

### Stap 4: Onbepaalde Integratie
Integreer beide leden naar $x$:
$$\int d[F(g(x))] = \int f(g(x)) \cdot g'(x) \, dx$$
Aangezien integratie de inverse bewerking is van differentiëren (op een willekeurige constante $C$ na):
$$F(g(x)) + C = \int f(g(x)) \cdot g'(x) \, dx$$

### Stap 5: Vergelijken van Beide Resultaten
Vergelijk:
1. $\int f(u) \, du = F(u) + C = F(g(x)) + C$
2. $\int f(g(x)) g'(x) \, dx = F(g(x)) + C$

Aangezien beide integralen dezelfde familie van functies $F(g(x)) + C$ opleveren, geldt:
$$\int f(g(x)) \cdot g'(x) \, dx = \int f(u) \, du \quad \blacksquare$$

---

## 3. Alternatieve Differentiatie-Verificatie (Methode van Leibniz)
Men kan de gelijkheid $\int f(x) \, dx = \int f(g(t)) g'(t) \, dt$ (met $x = g(t)$) eveneens aantonen door beide leden af te leiden naar de variabele $x$:
- Linkerlid:
  $$\frac{d}{dx} \left[ \int f(x) \, dx \right] = f(x)$$
- Rechterlid via de kettingregel:
  $$\frac{d}{dx} \left[ \int f(g(t)) g'(t) \, dt \right] = \frac{d}{dt} \left[ \int f(g(t)) g'(t) \, dt \right] \cdot \frac{dt}{dx} = f(g(t)) g'(t) \cdot \frac{1}{\frac{dx}{dt}} = f(g(t)) g'(t) \cdot \frac{1}{g'(t)} = f(g(t)) = f(x)$$
Aangezien de afgeleiden van beide leden identiek zijn aan $f(x)$, verschillen de onbepaalde integralen hoogstens met een constante.
