# Master Index — Te Kennen Bewijzen Examen

> [!info] Examenvoorbereiding Theorie
> **Vak:** Wiskundige Basistechnieken (T1AWB1) | Prof. dr. ir. Toon van Waterschoot (KU Leuven Campus Groep T)
> **Bron:** Examenleidraad *"Alle Bewijzen"* en *"Mogelijke Theorievragen"*
> **Parent MOC:** [[Index]] | **Examenstrategie:** [[Exam Preparation]]

Op het theorie-examen van Wiskundige Basistechnieken wordt verwacht dat je deze stellingen niet alleen foutloos wiskundig kunt formuleren, maar ook stap voor stap kunt bewijzen, voorzien van de juiste schets en randvoorwaarden.

---

## 📐 Deel 1: Analytische Meetkunde
- [[Bewijs 01 - Hoek tussen Twee Vectoren in R2]] — Formulering en afleiding van $\theta = \arccos\left(\frac{u \cdot v}{\|u\| \|v\|}\right)$ via de stelling van Pythagoras en de definitie van de norm.
  - Theorie: [[Ch 01 - Getallen, Punten en Vectoren#1.4 Afstand, hoek en poolcoördinaten in R2]]
- [[Bewijs 02 - Afstand tussen Punt en Rechte in R2]] — Formulering en bewijs van $d(P, e) = \frac{|A p_1 + B p_2 + C|}{\sqrt{A^2 + B^2}}$ via orthogonale projectie op de normaalvector.
  - Theorie: [[Ch 02 - Vlakke Meetkunde#1. Rechten in R2]]
- [[Bewijs 03 - Cartesiaanse Vergelijking van een Ellips]] — Afleiding van $\frac{(x - m_1)^2}{a^2} + \frac{(y - m_2)^2}{b^2} = 1$ vanuit de afstandsdefinitie met brandpunten en $b^2 = a^2 - c^2$.
  - Theorie: [[Ch 02 - Vlakke Meetkunde#2. Kegelsneden]]

---

## 🔢 Deel 2: Lineaire Algebra
- [[Bewijs 05 - Ongelijkheid van Cauchy-Schwarz]] — Bewijs van $|u \cdot v| \le \|u\| \|v\|$ via de kwadratische norm $\|r u + v\|^2 \ge 0$ en de discriminant $D \le 0$.
  - Theorie: [[Ch 05 - Vectorruimten en Inproductruimten#4. Inproductruimten]]
- [[Bewijs 06 - Rij-equivalentie met Eenheidsmatrix en Inverse Matrix]] — Bewijs dat $A \sim I_n \iff A$ regulier is en afleiding van $A^{-1} = E_m \dots E_1$ via elementaire matrices.
  - Theorie: [[Ch 02 - Matrices en Echelonvormen#3. Echelonvormen en Rang]] | [[Ch 03 - Vierkante Matrices en Determinanten#1. Inverse van een Matrix]]
- [[Bewijs 07 - Aantal Oplossingen van een Lineair Stelsel]] — Bewijs dat $AX = B$ precies $p \in \{0, 1, \infty\}$ oplossingen bezit via lineaire combinaties van oplossingen en de stelling van Rouché-Capelli.
  - Theorie: [[Ch 04 - Lineaire Stelsels#2. Oplosbaarheid Stelling van Rouché-Capelli]]
- [[Bewijs 08 - Determinant van Reguliere Matrix en Inverse]] — Bewijs dat $|A| \neq 0$ en $|A^{-1}| = \frac{1}{|A|}$ als $A$ regulier is via de multiplicatieve eigenschap van determinanten.
  - Theorie: [[Ch 03 - Vierkante Matrices en Determinanten#2. Determinanten en Eigenschappen]]
- [[Bewijs 12 - Uniciteit van Lineaire Combinatie in een Basis]] — Bewijs dat elke vector in een vectorruimte op unieke wijze geschreven kan worden als lineaire combinatie van basisvectoren.
  - Theorie: [[Ch 06 - Basis, Dimensie en Coördinaten#1. Basis en Dimensie]]
- [[Bewijs 13 - Coördinaten tov Orthonormale Basis]] — Afleiding van $[u]_S = [\langle u, u_1 \rangle, \dots, \langle u, u_n \rangle]^T$ voor een orthonormale basis via lineariteit en de Kronecker-delta.
  - Theorie: [[Ch 06 - Basis, Dimensie en Coördinaten#2. Coördinaten en Basistransformaties]]

---

## 📈 Deel 3: Analyse
- [[Bewijs 04 - Verband Afleidbaarheid en Continuïteit]] — Bewijs dat afleidbaarheid in een punt continuïteit in dat punt impliceert, inclusief het tegenvoorbeeld $f(x) = |x|$.
  - Theorie: [[Ch 05 - Afgeleiden en Toepassingen#1. Definitie en Betekenis van de Afgeleide]]
- [[Bewijs 09 - Integratie door Substitutie]] — Bewijs van $\int f(g(x)) g'(x) \, dx = \int f(u) \, du$ via de kettingregel voor afgeleiden van samengestelde functies.
  - Theorie: [[Ch 06 - Onbepaalde Integralen#2. Oplossingsmethoden]]
- [[Bewijs 10 - Partiële Integratie]] — Bewijs van $\int u \, dv = u v - \int v \, du$ via de productregel voor differentiëren.
  - Theorie: [[Ch 06 - Onbepaalde Integralen#2. Oplossingsmethoden]]
- [[Bewijs 11 - Hoofdstelling van de Integraalrekening]] — Volledig bewijs van Hulpstelling ($F'(x) = f(x)$ via de middelwaardestelling) en Hoofdstelling ($\int_a^b f(x) \, dx = F(b) - F(a)$).
  - Theorie: [[Ch 07 - Bepaalde Integralen#2. Hoofdstelling van de Integraalrekening]]
- [[Bewijs 14 - Convergentie van de p-Reeks]] — Bewijs van convergentie voor $p > 1$ en divergentie voor $p \le 1$ via de condensatietest van Cauchy.
  - Theorie: [[Ch 04 - Rijen en Reeksen van Reële Getallen#3. Numerieke Reeksen en Criteria]]
- [[Bewijs 15 - Taylorveelterm en Afleiding van Coëfficiënten]] — Bepaling van de coëfficiënten $a_k = \frac{f^{(k)}(a)}{k!}$ voor de beste $n$-de graads veeltermbenadering rond $x = a$.
  - Theorie: [[Ch 09 - Functiereeksen en Reeksontwikkelingen#2. Taylor- en Maclaurinreeksen]]
