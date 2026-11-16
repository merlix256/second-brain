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

# Bewijs 10: Partiële Integratie

> [!abstract] Context & Examenbelang
> **Theorievraag 10:** *"Formuleer en bewijs de stelling waarop partiële integratie gebaseerd is."*
> **Verwante Theorie:** [[Ch 06 - Onbepaalde Integralen#2. Oplossingsmethoden]]
> **Formularium:** [[Formularium#3. Analyse]] | **MOC:** [[00 - Index der Bewijzen]]

---

## 1. Formulering van de Stelling
Zij $u = f(x)$ en $v = g(x)$ twee afleidbare functies van $x$ op een open interval $I$.
Dan geldt voor de onbepaalde integraal van hun product:
$$\int u \, dv = u \cdot v - \int v \, du$$
of in functievoorschrift:
$$\int f(x) g'(x) \, dx = f(x) g(x) - \int g(x) f'(x) \, dx$$

---

## 2. Stap-voor-stap Bewijs

### Stap 1: Productregel voor Afgeleiden
Zijn $f(x)$ en $g(x)$ afleidbare functies, dan is hun product $f(x) \cdot g(x)$ eveneens afleidbaar. Volgens de productregel van Leibniz geldt:
$$\frac{d}{dx} [f(x) \cdot g(x)] = f'(x) \cdot g(x) + f(x) \cdot g'(x)$$

### Stap 2: Omzetting naar Differentialen
Vermenigvuldig beide leden met de differentiaal $dx$:
$$d[f(x) \cdot g(x)] = [f'(x) \cdot g(x) + f(x) \cdot g'(x)] \, dx$$
Splits de som:
$$d[f(x) \cdot g(x)] = g(x) \cdot f'(x) \, dx + f(x) \cdot g'(x) \, dx$$
Omdat $u = f(x) \implies du = f'(x) \, dx$ en $v = g(x) \implies dv = g'(x) \, dx$, kunnen we dit compacter noteren in termen van de variabelen $u$ en $v$:
$$d(u \cdot v) = v \, du + u \, dv$$

### Stap 3: Herschikken van de Termen
Isoleer de term $u \, dv$:
$$u \, dv = d(u \cdot v) - v \, du$$

### Stap 4: Termsgewijs Integreren
Integreer beide leden onbepaald:
$$\int u \, dv = \int d(u \cdot v) - \int v \, du$$
Aangezien de onbepaalde integraal van een differentiaal $d(u \cdot v)$ gelijk is aan $u \cdot v$ (de integratieconstante wordt geabsorbeerd in de resterende integraal):
$$\int u \, dv = u \cdot v - \int v \, du \quad \blacksquare$$

---

## 3. Uitbreiding naar Bepaalde Integralen
Voor een bepaald interval $[a, b]$ luidt de formule:
$$\int_a^b u(x) v'(x) \, dx = \Big[ u(x) v(x) \Big]_a^b - \int_a^b v(x) u'(x) \, dx$$
Dit volgt rechtstreeks door integratie over $[a, b]$ en toepassing van de Hoofdstelling van de Integraalrekening.
