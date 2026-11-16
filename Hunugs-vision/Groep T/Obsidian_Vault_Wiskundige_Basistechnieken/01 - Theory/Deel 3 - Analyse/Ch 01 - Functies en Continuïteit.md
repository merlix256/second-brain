---
title: "Analyse Ch 01: Functies en Continuïteit"
course: "Wiskundige basistechnieken (T1AWB1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: medium
tags:
  - study-unit
  - wiskunde
  - analyse
---

# Hoofdstuk 1: Functies en Continuïteit

> [!abstract] Context
> Basisbegrippen van reële functies: domein, bereik/beeld, symmetrieën, injectiviteit, inverse functies en formele continuïteit.
> **Parent MOC:** [[Deel 3 - Analyse]] | **Q&A:** [[Q&A - Analyse Ch 01 Functies]] | **Oefeningen:** [[Oefensessie 01 - Functies en Transcendente Functies]]

---

## 1. Reële Functies, Domein en Beeld
Een reële functie $f: D \to \mathbb{R}$ kent aan elke $x \in D = \text{dom}(f) \subseteq \mathbb{R}$ precies één functiewaarde $f(x)$ toe.
- **Domeinbeperkingen ($\text{dom}(f)$):**
  1. Noemer $\neq 0$.
  2. Onder even wortel $\ge 0$.
  3. Argument van $\ln(\cdot) > 0$ (of $\log_a(\cdot) > 0$).
  4. Argument van $\arcsin(\cdot), \arccos(\cdot) \in [-1, 1]$.
- **Beeld / Bereik:** $\text{bld}(f) = \{f(x) \mid x \in \text{dom}(f)\}$.

## 2. Eigenschappen van Functies
- **Even functie:** $f(-x) = f(x)$ $\forall x \in \text{dom}(f)$ (symmetrisch t.o.v. de $y$-as).
- **Oneven functie:** $f(-x) = -f(x)$ $\forall x \in \text{dom}(f)$ (puntsymmetrisch t.o.v. $(0,0)$).
- **Periodiek met periode $T > 0$:** $f(x + T) = f(x)$.
- **Injectief (1-op-1):** $f(x_1) = f(x_2) \implies x_1 = x_2$ (horizontale lijnentest snijdt grafiek max. 1 keer).
- **Inverse functie $f^{-1}$:** Bestaat $\iff f$ is injectief op $D$. Grafiek van $f^{-1}$ is spiegeling van $f$ t.o.v. $y = x$, en $\text{dom}(f^{-1}) = \text{bld}(f)$, $\text{bld}(f^{-1}) = \text{dom}(f)$.

## 3. Continuïteit & Tussenwaardestelling
- **Definitie:** $f$ is continu in $a \in \text{dom}(f)$ als:
  $$\lim_{x \to a} f(x) = f(a) \quad \Longleftrightarrow \quad \lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) = f(a)$$
- **Soorten discontinuïteiten:**
  1. *Ophefbaar:* limiet bestaat en is eindig, maar $\neq f(a)$ (of $f(a)$ ongedefinieerd).
  2. *Sprongdiscontinuïteit:* linker- en rechterlimiet bestaan en zijn eindig, maar ongelijk.
  3. *Essentieel / Pool:* minstens één eenzijdige limiet is $\pm\infty$ of bestaat niet.
- **Stelling van Bolzano / Tussenwaardestelling:** Als $f$ continu is op $[a, b]$ en $y_0$ ligt tussen $f(a)$ en $f(b)$, dan bestaat er minstens één $c \in [a, b]$ met $f(c) = y_0$.

> [!summary] Kernsamenvatting
> Controleer altijd eerst het domein! Voor een inverse functie moet je het domein vaak beperken zodat $f$ strikt monotoon (dus injectief) is.
