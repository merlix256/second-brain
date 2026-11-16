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

# Bewijs 07: Aantal Oplossingen van een Lineair Stelsel

> [!abstract] Context & Examenbelang
> **Theorievraag 7:** *"Beschouw een stelsel van lineaire vergelijkingen $AX = B$ met $A \in \mathbb{R}^{m \times n}, X \in \mathbb{R}^n, B \in \mathbb{R}^m$. Veronderstel dat dit stelsel $p$ verschillende oplossingen heeft.*
> *1. Bewijs wat de mogelijke waarden voor $p$ zijn.*
> *2. Leg uit hoe $p$ afhangt van de eigenschappen van $A$ en $B$."*
> **Verwante Theorie:** [[Ch 04 - Lineaire Stelsels#2. Oplosbaarheid Stelling van Rouché-Capelli]]
> **Formularium:** [[Formularium#2. Lineaire Algebra]] | **MOC:** [[00 - Index der Bewijzen]]

---

## 1. Formulering van de Stelling
Voor elk lineair stelsel $AX = B$ met reële coëfficiënten geldt dat het aantal oplossingen $p$ slechts drie mogelijke waarden kan aannemen:
$$p \in \{0, 1, \infty\}$$
Er zijn dus:
- Geen oplossingen ($p = 0$, het stelsel is strijdig),
- Precies één unieke oplossing ($p = 1$, het stelsel is bepaald),
- Oneindig veel oplossingen ($p = \infty$, het stelsel is onbepaald).

---

## 2. Stap-voor-stap Bewijs van Deel 1

### Geval 1: $p = 0$ bestaat
Beschouw het stelsel in $\mathbb{R}^2$:
$$\begin{cases} x + y = 0 \\ x + y = 1 \end{cases}$$
Lid aan lid aftrekken geeft $0 = 1$, een contradictie. Dit stelsel bezit 0 oplossingen.

### Geval 2: $p = 1$ bestaat
Beschouw het stelsel:
$$\begin{cases} x = 2 \\ y = 3 \end{cases}$$
Dit stelsel bezit exact $p = 1$ unieke oplossing, namelijk $[2, 3]^T$.

### Geval 3: Zodra $p \ge 2$, is $p = \infty$
Veronderstel dat het stelsel $AX = B$ minstens twee verschillende oplossingen bezit, zeg $X_1$ en $X_2$ met $X_1 \neq X_2$.
Omdat $X_1$ en $X_2$ oplossingen zijn, geldt:
$$A X_1 = B \quad \text{en} \quad A X_2 = B$$
Beschouw nu voor een willekeurige reële parameter $k \in \mathbb{R}$ de lineaire combinatie:
$$X(k) = k X_1 + (1 - k) X_2$$
We testen of $X(k)$ een oplossing is van het stelsel door het product met $A$ te nemen:
$$A X(k) = A \big( k X_1 + (1 - k) X_2 \big)$$
Wegens de lineariteit van de matrixvermenigvuldiging (distributiviteit en homogeniteit):
$$A X(k) = k (A X_1) + (1 - k) (A X_2)$$
Substitueer $A X_1 = B$ en $A X_2 = B$:
$$A X(k) = k B + (1 - k) B = [k + (1 - k)] B = 1 \cdot B = B$$
Dus $X(k)$ is een geldige oplossing van $AX = B$ voor **elke** $k \in \mathbb{R}$.

Omdat $X_1 \neq X_2$, levert elke verschillende keuze van $k$ een unieke vector $X(k)$ op:
$$X(k_1) - X(k_2) = (k_1 - k_2)(X_1 - X_2) \neq \mathbf{0} \quad \text{als } k_1 \neq k_2$$
Aangezien er over het veld $\mathbb{R}$ oneindig veel verschillende reële waarden voor $k$ gekozen kunnen worden, bezit het stelsel oneindig veel oplossingen ($p = \infty$).
Er bestaat dus geen enkel stelsel met bijvoorbeeld exact 2, 3 of 42 oplossingen. $\blacksquare$

---

## 3. Verband met de Eigenschappen van $A$ en $B$ (Deel 2)
Het aantal oplossingen $p$ wordt volledig bepaald door de rang van de coëfficiëntenmatrix $A$ en de uitgebreide matrix $[A \mid B]$ via de **Stelling van Rouché-Capelli**:

1. **$p = 0$ (Strijdig stelsel):**
   $$\text{rang}(A) < \text{rang}([A \mid B])$$
   Er ontstaat in de echelonvorm een strijdige rij van de vorm $[0 \; 0 \; \dots \; 0 \mid c]$ met $c \neq 0$.
2. **$p = 1$ (Unieke oplossing):**
   $$\text{rang}(A) = \text{rang}([A \mid B]) = n \quad (\text{aantal onbekenden})$$
   Elke kolom bevat een spilpositie; er zijn geen vrije variabelen.
3. **$p = \infty$ (Oneindig veel oplossingen):**
   $$\text{rang}(A) = \text{rang}([A \mid B]) = r < n$$
   Het stelsel is compatibel, maar er zijn $n - r > 0$ vrije parameters (vrijheidsgraden).
