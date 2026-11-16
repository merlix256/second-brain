---
title: "Analyse Ch 03: Limieten"
course: "Wiskundige basistechnieken (T1AWB1)"
unit_type: theory
status: todo
completed: false
est_hours: 3.0
priority: high
tags:
  - study-unit
  - wiskunde
  - analyse
---

# Hoofdstuk 3: Limieten

> [!abstract] Context
> Limietdefinitie, onbepaalde vormen, standaardlimieten (sinus cardinalis, getal $e$), asymptoten en de regel van de l'Hôpital.
> **Parent MOC:** [[Deel 3 - Analyse]] | **Q&A:** [[Q&A - Analyse Ch 03 Limieten]] | **Oefeningen:** [[Oefensessie 15 - Limieten]]

---

## 1. Definitie, Rekenregels en Onbepaaldheden
- **$\varepsilon$-$\delta$-definitie:** $\lim_{x \to a} f(x) = L \iff \forall \varepsilon > 0, \exists \delta > 0 : 0 < |x - a| < \delta \implies |f(x) - L| < \varepsilon$.
- **Zeven onbepaalde vormen:**
  $$\left[\frac{0}{0}\right], \quad \left[\frac{\infty}{\infty}\right], \quad [0 \cdot \infty], \quad [\infty - \infty], \quad [1^\infty], \quad [0^0], \quad [\infty^0]$$
- **Technieken zonder l'Hôpital:**
  - Factoriseren & schrappen bij veeltermen/rationale functies ($[0/0]$).
  - Vermenigvuldigen met de **toegevoegde tweeterm** bij wortelvormen ($[\infty - \infty]$ of $[0/0]$).
  - Hoogste graad buiten haakjes brengen bij $x \to \pm\infty$ (let op $\sqrt{x^2} = |x| = -x$ voor $x \to -\infty$!).
  - **Insluitstelling (Sandwich-stelling):** Als $g(x) \le f(x) \le h(x)$ en $\lim g = \lim h = L$, dan $\lim f = L$.

---

## 2. Standaardlimieten & Asymptoten
### 2.1 Asymptoten
- **Verticale asymptoot (VA):** $x = a$ als $\lim_{x \to a^\pm} f(x) = \pm\infty$.
- **Horizontale asymptoot (HA):** $y = b$ als $\lim_{x \to \pm\infty} f(x) = b$.
- **Schuine asymptoot (SA):** $y = ax + b$ met $a = \lim_{x \to \pm\infty} \frac{f(x)}{x}$ ($\neq 0, \pm\infty$) en $b = \lim_{x \to \pm\infty} (f(x) - ax)$.

### 2.2 Belangrijke Standaardlimiet (Sinus Cardinalis)
$$\lim_{x \to 0} \frac{\sin x}{x} = 1 \qquad \text{en analoog:} \quad \lim_{x \to 0} \frac{\tan x}{x} = 1, \quad \lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}$$
- **Exponentiële standaardlimiet:**
  $$\lim_{x \to \pm\infty} \left(1 + \frac{a}{x}\right)^{bx} = e^{ab}, \qquad \lim_{x \to 0} \frac{e^x - 1}{x} = 1, \qquad \lim_{x \to 0} \frac{\ln(1+x)}{x} = 1$$

---

## 3. Regel van de l'Hôpital
Als $\lim_{x \to a} \frac{f(x)}{g(x)}$ een zuivere onbepaalde vorm $\left[\frac{0}{0}\right]$ of $\left[\frac{\infty}{\infty}\right]$ oplevert, $f$ en $g$ afleidbaar zijn in een omgeving van $a$ ($g'(x) \neq 0$), en $\lim_{x \to a} \frac{f'(x)}{g'(x)}$ bestaat (eindig of $\pm\infty$), dan:
$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$
- **Bij $[0 \cdot \infty]$:** Herschrijf $f \cdot g = \frac{f}{1/g}$ naar $[0/0]$ of $[\infty/\infty]$.
- **Bij machtsvormen $[1^\infty], [0^0], [\infty^0]$:** Gebruik $f(x)^{g(x)} = e^{g(x)\ln f(x)}$ en bereken eerst $\lim g(x)\ln f(x)$.

> [!danger] Valkuil
> Gebruik NOOIT l'Hôpital als het géén $[0/0]$ of $[\infty/\infty]$ is! En vermijd circulaire redeneringen bij $\lim_{x \to 0} \frac{\sin x}{x}$ als je die voor de afgeleide van $\sin x$ nodig hebt.
