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

# Bewijs 14: Convergentie en Divergentie van de p-Reeks

> [!abstract] Context & Examenbelang
> **Theorievraag 14:** *"Geef de algemene uitdrukking voor de $p$-reeks en toon aan voor welke waarden van $p \in \mathbb{R}$ deze reeks convergeert/divergeert."*
> **Verwante Theorie:** [[Ch 04 - Rijen en Reeksen van Reële Getallen#3. Numerieke Reeksen en Criteria]]
> **Formularium:** [[Formularium#3. Analyse]] | **MOC:** [[00 - Index der Bewijzen]]

---

## 1. Formulering van de Stelling
De **$p$-reeks** (of hyperharmonische reeks) is de oneindige numerieke reeks van de vorm:
$$\sum_{n=1}^\infty \frac{1}{n^p} = 1 + \frac{1}{2^p} + \frac{1}{3^p} + \frac{1}{4^p} + \dots \quad (p \in \mathbb{R})$$
**Stelling:**
- De $p$-reeks is **convergent** als en slechts als $p > 1$.
- De $p$-reeks is **divergent** als en slechts als $p \le 1$.
*(In het bijzonder voor $p = 1$ is $\sum_{n=1}^\infty \frac{1}{n}$ de bekende divergente harmonische reeks).*

---

## 2. Stap-voor-stap Bewijs

We onderscheiden twee gevallen voor de parameter $p$: $p \le 0$ en $p > 0$.

### Geval 1: $p \le 0$
Beschouw de algemene term $u_n = \frac{1}{n^p} = n^{-p}$.
- Als $p = 0$: $u_n = \frac{1}{n^0} = 1$ voor alle $n$.
  $$\lim_{n \to \infty} u_n = \lim_{n \to \infty} 1 = 1 \neq 0$$
- Als $p < 0$: stel $p = -q$ met $q > 0$. Dan is $u_n = n^q$.
  $$\lim_{n \to \infty} u_n = \lim_{n \to \infty} n^q = +\infty \neq 0$$

Volgens de **Divergentietest** (de noodzakelijke voorwaarde voor convergentie) kan een reeks $\sum u_n$ slechts convergeren als $\lim_{n \to \infty} u_n = 0$.
Aangezien de limiet van de algemene term voor alle $p \le 0$ niet gelijk is aan 0, is de $p$-reeks **divergent voor $p \le 0$**.

---

### Geval 2: $p > 0$ (Toepassing van de Condensatietest van Cauchy)
Als $p > 0$, dan is de functie $f(x) = \frac{1}{x^p}$ strikt positief en monotoon dalend op $[1, +\infty[$.
De termen $u_n = \frac{1}{n^p}$ vormen bijgevolg een dalende rij van positieve getallen.
We kunnen de **Condensatietest van Cauchy** toepassen:
> *Een reeks met positieve, dalende termen $\sum_{n=1}^\infty u_n$ convergeert als en slechts als haar gecondenseerde reeks $\sum_{k=0}^\infty 2^k u_{2^k}$ convergeert.*

Stel $n = 2^k$. De term $u_{2^k}$ wordt:
$$u_{2^k} = \frac{1}{(2^k)^p} = \frac{1}{2^{kp}}$$
De algemene term van de gecondenseerde reeks is:
$$2^k \cdot u_{2^k} = 2^k \cdot \frac{1}{2^{kp}} = \frac{2^k}{(2^p)^k} = \left( \frac{2}{2^p} \right)^k = \left( \frac{1}{2^{p-1}} \right)^k$$
De gecondenseerde reeks is dus:
$$\sum_{k=0}^\infty 2^k u_{2^k} = \sum_{k=0}^\infty \left( \frac{1}{2^{p-1}} \right)^k$$

Dit is een **meetkundige reeks** $\sum_{k=0}^\infty r^k$ met reden:
$$r = \frac{1}{2^{p-1}} = 2^{1-p}$$
We weten dat een meetkundige reeks met positieve termen convergeert $\iff r < 1$, en divergeert $\iff r \ge 1$:
1. **Convergentie ($r < 1$):**
   $$\frac{1}{2^{p-1}} < 1 \iff 2^{p-1} > 1 \iff p - 1 > 0 \iff p > 1$$
2. **Divergentie ($r \ge 1$):**
   $$\frac{1}{2^{p-1}} \ge 1 \iff 2^{p-1} \le 1 \iff p - 1 \le 0 \iff p \le 1$$

Wegens de condensatietest van Cauchy vertoont de oorspronkelijke $p$-reeks precies hetzelfde convergentiegedrag als de gecondenseerde reeks.
Bijgevolg convergeert de $p$-reeks voor $p > 1$ en divergeert zij voor $0 < p \le 1$.

---

### Stap 3: Samenvattend Besluit
Door het samenvoegen van Geval 1 en Geval 2 verkrijgen we het volledige besluit:
$$\sum_{n=1}^\infty \frac{1}{n^p} \quad \begin{cases} \text{convergeert} & \text{als } p > 1 \\ \text{divergeert} & \text{als } p \le 1 \end{cases} \quad \blacksquare$$

---

## 3. Alternatieve Afleiding: De Integraaltest
Op het examen mag dit bewijs ook geleverd worden via de **Integraaltest** van Maclaurin-Cauchy:
$$\int_1^{+\infty} \frac{1}{x^p} \, dx = \lim_{M \to +\infty} \int_1^M x^{-p} \, dx$$
- Voor $p \neq 1$:
  $$\int_1^M x^{-p} \, dx = \left[ \frac{x^{1-p}}{1 - p} \right]_1^M = \frac{M^{1-p} - 1}{1 - p}$$
  Als $p > 1 \implies 1 - p < 0 \implies \lim_{M \to +\infty} M^{1-p} = 0$, dus de integraal convergeert naar $\frac{1}{p - 1}$.
  Als $p < 1 \implies 1 - p > 0 \implies \lim_{M \to +\infty} M^{1-p} = +\infty$, dus divergent.
- Voor $p = 1$:
  $$\int_1^{+\infty} \frac{1}{x} \, dx = \lim_{M \to +\infty} [\ln x]_1^M = \lim_{M \to +\infty} \ln M = +\infty \quad (\text{divergent})$$
