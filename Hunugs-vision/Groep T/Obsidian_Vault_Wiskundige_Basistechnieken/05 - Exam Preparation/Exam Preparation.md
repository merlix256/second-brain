# Examenvoorbereiding & Strategie — Wiskundige Basistechnieken

> [!abstract] Doelstelling
> Strategisch draaiboek voor het succesvol afronden van het examen Wiskundige Basistechnieken (KU Leuven Campus Groep T).
> **Parent MOC:** [[Index]] | **Te Kennen Bewijzen:** [[00 - Index der Bewijzen]]

---

## 🏛️ Structuur van het Examen
Het eindexamen bestaat uit twee complementaire luiken:
1. **Theoriedeel:**
   - Evaluatie van conceptueel inzicht, definities, stellingen en **rigoureuze bewijzen**.
   - Meestal wordt minstens één groot theoriebewijs gevraagd uit de lijst van 15 vaste bewijzen (zie [[00 - Index der Bewijzen]]).
   - Korte inzichtsvragen (bv. geef een tegenvoorbeeld voor het omgekeerde van de stelling rond afleidbaarheid en continuïteit, of interpreteer de determinant meetkundig).
2. **Oefeningendeel:**
   - Oplossen van concrete vraagstukken analoog aan de 24 oefensessies (zie [[Exercise Session Tracker]]).
   - Parameterstelsels, Gram-Schmidt orthogonalisatie, partieelbreuksplitsing, oppervlakteberekeningen van poolkrommen, etc.

---

## 📜 De 15 Officiële Examenbewijzen (Top Prioriteit)
Zorg dat je deze 15 bewijzen blindelings kunt neerschrijven, inclusief de juiste voorwaarden en grafische representaties:
1. [[Bewijs 01 - Hoek tussen Twee Vectoren in R2]] — Cosinusregel / Pythagoras versus algebraïsche norm.
2. [[Bewijs 02 - Afstand tussen Punt en Rechte in R2]] — Projectie op de eenheidsnormaalvector.
3. [[Bewijs 03 - Cartesiaanse Vergelijking van een Ellips]] — Dubbel kwadrateren vanuit afstandsdefinitie $d(X, F) + d(X, G) = 2a$.
4. [[Bewijs 04 - Verband Afleidbaarheid en Continuïteit]] — Toename herschrijven met differentiequotiënt en tegenvoorbeeld $f(x) = |x|$.
5. [[Bewijs 05 - Ongelijkheid van Cauchy-Schwarz]] — Positieve kwadratische norm $\|ru + v\|^2 \ge 0 \implies D \le 0$.
6. [[Bewijs 06 - Rij-equivalentie met Eenheidsmatrix en Inverse Matrix]] — Product van elementaire matrices $A^{-1} = E_m \dots E_1$.
7. [[Bewijs 07 - Aantal Oplossingen van een Lineair Stelsel]] — Convexe combinatie van 2 oplossingen levert oneindig veel oplossingen.
8. [[Bewijs 08 - Determinant van Reguliere Matrix en Inverse]] — Multiplicativiteit $|A| \cdot |A^{-1}| = 1 \implies |A| \neq 0$ en $|A^{-1}| = 1/|A|$.
9. [[Bewijs 09 - Integratie door Substitutie]] — Afleiding via kettingregel van samengestelde primitieve functie.
10. [[Bewijs 10 - Partiële Integratie]] — Afleiding via productregel $d(uv) = u \, dv + v \, du$.
11. [[Bewijs 11 - Hoofdstelling van de Integraalrekening]] — Hulpstelling via middelwaardestelling van integralen + Hoofdstelling via constante $C = G(a)$.
12. [[Bewijs 12 - Uniciteit van Lineaire Combinatie in een Basis]] — Gelijkstellen van twee combinaties en toepassing van lineaire onafhankelijkheid.
13. [[Bewijs 13 - Coördinaten tov Orthonormale Basis]] — Inproduct nemen met basisvector $u_i$ en toepassing Kronecker-delta $\langle u_j, u_i \rangle = \delta_{ji}$.
14. [[Bewijs 14 - Convergentie van de p-Reeks]] — Condensatietest van Cauchy herleidt naar meetkundige reeks met reden $r = 1/2^{p-1}$.
15. [[Bewijs 15 - Taylorveelterm en Afleiding van Coëfficiënten]] — $k$-de afgeleide evalueren in $x = a$ levert $P_n^{(k)}(a) = k! a_k = f^{(k)}(a)$.

---

## 🧠 Examenstrategie per Domein

### 1. Analytische Meetkunde
- **Rechtenbundels:** Bij vragen over een rechte door het snijpunt van twee rechten en evenwijdig/loodrecht op een derde: gebruik altijd $e_1 + \lambda e_2 = 0$. Los het snijpunt niet apart op, dat bespaart veel tijd!
- **Kruisproduct:** Verifieer je vectorieel product altijd met het inproduct: $n \cdot r_1 = 0$ en $n \cdot r_2 = 0$.

### 2. Lineaire Algebra
- **Parameterstelsels:** Onderzoek nauwkeurig de spilposities. Splits expliciet per parameterwaarde ($a = a_0$ vs $a \neq a_0$). Deel nooit door een parameter vóór je gecontroleerd hebt of deze nul kan zijn.
- **Deelruimten:** Controleer altijd eerst of $\mathbf{0} \in W$. Zo niet: direct géén deelruimte.
- **Gram-Schmidt:** Vereenvoudig breuken bij elke projectiestap om escalatie van getallen te voorkomen.

### 3. Analyse
- **Limieten:** Pas de l'Hôpital enkel toe na strikte verificatie van $[0/0]$ of $[\infty/\infty]$.
- **Reeksen:** Check altijd eerst $\lim_{n \to \infty} u_n$. Is dit niet $0$, dan convergeert de reeks nooit (Divergentietest)!
- **Integralen:** Voer bij rationale functies altijd eerst een euclidische veeltermdeling uit als $\deg(P) \ge \deg(Q)$.

---

## 📑 Oefenexamens & Mock Tests (Placeholders)
- [[Mock Exam 1 - Proefexamen Halverwege Semester (Kennismakingsexamen)]]
- [[Mock Exam 2 - Volledig Proefexamen Deel 1, 2 en 3]]
- [[Mock Exam 3 - Oplossingen en Zelfevaluatie Rubric]]
