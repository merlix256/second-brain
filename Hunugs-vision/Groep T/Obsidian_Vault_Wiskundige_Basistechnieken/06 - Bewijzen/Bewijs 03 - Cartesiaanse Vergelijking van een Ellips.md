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

# Bewijs 03: Cartesiaanse Vergelijking van een Ellips

> [!abstract] Context & Examenbelang
> **Theorievraag 3:** *"Leid de Cartesiaanse vergelijking af voor een ellips met een horizontale lange as en een willekeurig middelpunt."*
> **Verwante Theorie:** [[Ch 02 - Vlakke Meetkunde#2. Kegelsneden]]
> **Formularium:** [[Formularium#1. Analytische Meetkunde]] | **MOC:** [[00 - Index der Bewijzen]]

---

## 1. Formulering van de Stelling
Een liggende ellips met willekeurig middelpunt $M(m_1, m_2)$, halve grote as $a$, en halve kleine as $b$ ($a > b > 0$) bezit als Cartesiaanse vergelijking:
$$\frac{(x - m_1)^2}{a^2} + \frac{(y - m_2)^2}{b^2} = 1$$
met brandpuntsafstand $2c$, waarbij $c^2 = a^2 - b^2$.

---

## 2. Grafische Representatie
![[Bewijs_03_Ellips_Afleiding.png]]
*(Schets: Ellips gecentreerd in $M(m_1, m_2)$ met horizontale hoofdas. Brandpunten $F(m_1 - c, m_2)$ en $G(m_1 + c, m_2)$. Een willekeurig punt $X(x, y)$ op de ellips met voerstralen $d(X, F)$ en $d(X, G)$. Relatieve coördinatenvector $r = x - m$.)*

---

## 3. Stap-voor-stap Bewijs

### Stap 1: Translatie naar het Middelpunt
Laat $X(x, y)$ een willekeurig punt op de ellips zijn. We voeren een coördinatentranslatie in naar het middelpunt $M(m_1, m_2)$:
$$r = \begin{bmatrix} r_1 \ r_2 \end{bmatrix} = \begin{bmatrix} x - m_1 \ y - m_2 \end{bmatrix}$$
In dit translatiesysteem bevindt het middelpunt zich in de relatieve oorsprong $[0, 0]^T$, en liggen de brandpunten op de horizontale as in:
$$F' = \begin{bmatrix} -c \ 0 \end{bmatrix} \quad \text{en} \quad G' = \begin{bmatrix} c \ 0 \end{bmatrix}$$

### Stap 2: Meetkundige Definitie toepassen
Volgens de definitie van een ellips is de som van de afstanden van elk punt tot de twee brandpunten constant en gelijk aan $2a$:
$$d(X, F) + d(X, G) = 2a \iff \|r - F'\| + \|r - G'\| = 2a$$
In Cartesiaanse coördinaten:
$$\sqrt{(r_1 + c)^2 + r_2^2} + \sqrt{(r_1 - c)^2 + r_2^2} = 2a$$

### Stap 3: Kwadrateren van de Wortelvormen
Zonder één vierkantswortel af:
$$\sqrt{(r_1 + c)^2 + r_2^2} = 2a - \sqrt{(r_1 - c)^2 + r_2^2}$$
Kwadrateren van beide leden:
$$(r_1 + c)^2 + r_2^2 = 4a^2 - 4a \sqrt{(r_1 - c)^2 + r_2^2} + (r_1 - c)^2 + r_2^2$$
Werk de kwadraten $(r_1 + c)^2$ en $(r_1 - c)^2$ uit:
$$r_1^2 + 2c r_1 + c^2 + r_2^2 = 4a^2 - 4a \sqrt{(r_1 - c)^2 + r_2^2} + r_1^2 - 2c r_1 + c^2 + r_2^2$$
Schrap $r_1^2, c^2$ en $r_2^2$ aan weerszijden:
$$2c r_1 = 4a^2 - 4a \sqrt{(r_1 - c)^2 + r_2^2} - 2c r_1$$
Breng de resterende wortel naar het linkerlid en de overige termen naar rechts:
$$4a \sqrt{(r_1 - c)^2 + r_2^2} = 4a^2 - 4c r_1$$
Deel door 4:
$$a \sqrt{(r_1 - c)^2 + r_2^2} = a^2 - c r_1$$

### Stap 4: Tweede Kwadratering en Substitutie van $b^2$
Kwadrateren van beide leden:
$$a^2 \left( (r_1 - c)^2 + r_2^2 \right) = (a^2 - c r_1)^2$$
Werk de haakjes uit:
$$a^2 (r_1^2 - 2c r_1 + c^2 + r_2^2) = a^4 - 2a^2 c r_1 + c^2 r_1^2$$
$$a^2 r_1^2 - 2a^2 c r_1 + a^2 c^2 + a^2 r_2^2 = a^4 - 2a^2 c r_1 + c^2 r_1^2$$
Schrap $-2a^2 c r_1$ aan weerszijden:
$$a^2 r_1^2 + a^2 c^2 + a^2 r_2^2 = a^4 + c^2 r_1^2$$
Herschikken (termen in $r_1^2$ links groeperen, constanten rechts):
$$(a^2 - c^2) r_1^2 + a^2 r_2^2 = a^4 - a^2 c^2 = a^2 (a^2 - c^2)$$
We definiëren nu $b$ als de halve kleine as via het fundamentele verband $b^2 = a^2 - c^2$:
$$b^2 r_1^2 + a^2 r_2^2 = a^2 b^2$$
Delen door $a^2 b^2$:
$$\frac{r_1^2}{a^2} + \frac{r_2^2}{b^2} = 1$$

### Stap 5: Terugsubstitutie van $r_1$ en $r_2$
Vervang $r_1 = x - m_1$ en $r_2 = y - m_2$:
$$\frac{(x - m_1)^2}{a^2} + \frac{(y - m_2)^2}{b^2} = 1 \quad \blacksquare$$

---

## 4. Examenvalkuilen & Aandachtspunten
- **Dubbel kwadrateren:** Dit is een klassieke algebraïsche behendigheidstest op het examen. Isoleer steeds éérst één wortel voordat je kwadrateert, anders creëer je een onhandelbare mengterm met twee wortels.
- **Relatie tussen $a, b, c$:** Vermeld altijd de meetkundige betekenis van $b^2 = a^2 - c^2$ ($a > c$ wegens de driehoeksongelijkheid in $\triangle XFG$, zodat $a^2 - c^2 > 0$).
