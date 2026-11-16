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

# Bewijs 05: De Ongelijkheid van Cauchy-Schwarz

> [!abstract] Context & Examenbelang
> **Theorievraag 5:** *"Formuleer en bewijs de ongelijkheid van Cauchy-Schwarz."*
> **Verwante Theorie:** [[Ch 05 - Vectorruimten en Inproductruimten#4. Inproductruimten]]
> **Formularium:** [[Formularium#2. Lineaire Algebra]] | **MOC:** [[00 - Index der Bewijzen]]

---

## 1. Formulering van de Stelling
Zij $V$ een reële inproductruimte (bijvoorbeeld $\mathbb{R}^n$ met het standaard inproduct).
Voor willekeurige vectoren $u, v \in V$ geldt:
$$|\langle u, v \rangle| \le \|u\| \|v\|$$
In het bijzonder voor $\mathbb{R}^n$ met het Euclidische inproduct $u \cdot v = \sum_{i=1}^n u_i v_i$:
$$\left| \sum_{i=1}^n u_i v_i \right| \le \sqrt{\sum_{i=1}^n u_i^2} \sqrt{\sum_{i=1}^n v_i^2}$$
Gelijkheid geldt als en slechts als de vectoren $u$ en $v$ lineair afhankelijk zijn.

---

## 2. Stap-voor-stap Bewijs

### Stap 1: Triviaal Geval (Minstens één nulvector)
- Indien $u = \mathbf{0}$, dan is $\langle \mathbf{0}, v \rangle = 0$ en $\|u\| = 0$. De ongelijkheid herleidt zich tot $|0| \le 0 \cdot \|v\| \iff 0 \le 0$, wat triviaal waar is (gelijkheid).
- Analoog, indien $v = \mathbf{0}$, is eveneens voldaan aan $0 \le 0$.

### Stap 2: Niet-triviaal Geval ($u \neq \mathbf{0}$ en $v \neq \mathbf{0}$)
Stel $u \neq \mathbf{0}$ en $v \neq \mathbf{0}$. Beschouw voor een willekeurige reële parameter $r \in \mathbb{R}$ de vector:
$$w = r u + v \in V$$
Wegens het axioma van strikte positiviteit van het inproduct geldt dat de norm van elke vector niet-negatief is, en dus:
$$\|w\|^2 = \langle r u + v, \; r u + v \rangle \ge 0 \quad (\forall r \in \mathbb{R})$$

### Stap 3: Uitwerken als Kwadratische Veelterm in r
Met behulp van de bilineariteit en symmetrie van het inproduct werken we deze uitdrukking uit:
$$\langle r u + v, \; r u + v \rangle = \langle r u, r u \rangle + \langle r u, v \rangle + \langle v, r u \rangle + \langle v, v \rangle$$
$$\ge r^2 \langle u, u \rangle + 2r \langle u, v \rangle + \langle v, v \rangle \ge 0$$
We definiëren de reële functie $p(r)$:
$$p(r) = a r^2 + 2b r + c \ge 0$$
waarbij de coëfficiënten gedefinieerd worden als:
- $a = \langle u, u \rangle = \|u\|^2 > 0$ (aangezien $u \neq \mathbf{0}$)
- $b = \langle u, v \rangle \in \mathbb{R}$
- $c = \langle v, v \rangle = \|v\|^2 > 0$

### Stap 4: Analyse van de Discriminant
De functie $p(r) = a r^2 + 2b r + c$ stelt een dalparabool voor (want $a > 0$).
Opdat $p(r) \ge 0$ voor álle $r \in \mathbb{R}$, mag de grafiek van de parabool de $r$-as hoogstens raken, maar er nooit onder duiken. Dit impliceert dat de vergelijking $p(r) = 0$ ten hoogste één reële wortel bezit, en de discriminant $D$ bijgevolg niet-positief moet zijn:
$$D \le 0$$
De discriminant van $a r^2 + 2b r + c = 0$ is:
$$D = (2b)^2 - 4ac = 4b^2 - 4ac$$
De voorwaarde $D \le 0$ betekent dus:
$$4b^2 - 4ac \le 0 \iff 4b^2 \le 4ac \iff b^2 \le ac$$

### Stap 5: Substitutie van de Inproducten
Substitueer $a, b, c$ terug in de ongelijkheid $b^2 \le ac$:
$$(\langle u, v \rangle)^2 \le \langle u, u \rangle \cdot \langle v, v \rangle$$
Aangezien $\langle u, u \rangle = \|u\|^2$ en $\langle v, v \rangle = \|v\|^2$:
$$(\langle u, v \rangle)^2 \le \|u\|^2 \|v\|^2$$
Neem aan beide zijden de positieve vierkantswortel:
$$\sqrt{(\langle u, v \rangle)^2} \le \sqrt{\|u\|^2 \|v\|^2}$$
$$|\langle u, v \rangle| \le \|u\| \|v\| \quad \blacksquare$$

---

## 3. Gevolgen en Toepassingen
1. **Definitie van de Hoek in Algemene Ruimten:**
   Omdat $|\langle u, v \rangle| \le \|u\| \|v\|$, geldt voor $u, v \neq \mathbf{0}$:
   $$-1 \le \frac{\langle u, v \rangle}{\|u\| \|v\|} \le 1$$
   Hierdoor bestaat er altijd een unieke hoek $\theta \in [0, \pi]$ zodanig dat $\cos\theta = \frac{\langle u, v \rangle}{\|u\| \|v\|}$.
2. **Driehoeksongelijkheid:**
   $$\|u + v\| \le \|u\| + \|v\|$$
   *(Bewijs volgt direct door kwadrateren en toepassen van Cauchy-Schwarz).*
