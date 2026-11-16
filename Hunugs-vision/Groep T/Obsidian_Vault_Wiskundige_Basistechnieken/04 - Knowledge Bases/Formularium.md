# Formularium — Wiskundige Basistechnieken

> [!info] Formule-overzicht
> Dit formularium bevat alle kernformules van het vak Wiskundige Basistechnieken (Analytische Meetkunde, Lineaire Algebra en Analyse) met directe verwijzingen naar de theoriepagina's.

---

## 📐 Deel 1: Analytische Meetkunde
- **Scalair product:**
  $$\mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^n u_i v_i = \|\mathbf{u}\| \|\mathbf{v}\| \cos\theta$$
  🔗 [[Ch 01 - Getallen, Punten en Vectoren#2.3 Hoek en Scalair Product in R2]]
- **Orthogonale projectie in $\mathbb{R}^2$:**
  $$\text{proj}_{\mathbf{v}}(\mathbf{u}) = \left(\frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{v}\|^2}\right) \mathbf{v}$$
  🔗 [[Ch 01 - Getallen, Punten en Vectoren#3. Orthogonale Projectie in R2]]
- **Rechtenbundel in $\mathbb{R}^2$:**
  $$k(A_1 x + B_1 y + C_1) + l(A_2 x + B_2 y + C_2) = 0$$
  🔗 [[Ch 02 - Vlakke Meetkunde#1.2 Rechtenbundels]]
- **Vectorieel product in $\mathbb{R}^3$:**
  $$\mathbf{u} \times \mathbf{v} = \begin{bmatrix} u_2 v_3 - u_3 v_2 \\ u_3 v_1 - u_1 v_3 \\ u_1 v_2 - u_2 v_1 \end{bmatrix}, \quad \|\mathbf{u} \times \mathbf{v}\| = \|\mathbf{u}\| \|\mathbf{v}\| \sin\theta$$
  🔗 [[Ch 03 - Ruimtemeetkunde#1.2 Vectorieel Product (Kruisproduct)]]
- **Afstand van punt $Q$ tot vlak $\alpha: Ax + By + Cz + D = 0$:**
  $$d(Q, \alpha) = \frac{|A q_1 + B q_2 + C q_3 + D|}{\sqrt{A^2 + B^2 + C^2}}$$
  🔗 [[Ch 03 - Ruimtemeetkunde#2.2 Afstand van een Punt tot een Vlak]]

---

## 🔢 Deel 2: Lineaire Algebra
- **Formule van De Moivre & Complexe Machten:**
  $$(r e^{i\theta})^n = r^n (\cos(n\theta) + i\sin(n\theta))$$
  🔗 [[Ch 01 - Complexe Getallen#2.3 Formule van De Moivre]]
- **$n$-demachtswortels van $z = r e^{i\theta}$:**
  $$w_k = \sqrt[n]{r} \exp\left(i\frac{\theta + 2k\pi}{n}\right), \quad k = 0, \dots, n-1$$
  🔗 [[Ch 01 - Complexe Getallen#3. n-demachtswortels van een Complex Getal]]
- **Inverse via Adjunct:**
  $$A^{-1} = \frac{1}{\det(A)} \text{adj}(A)$$
  🔗 [[Ch 03 - Vierkante Matrices en Determinanten#3. Adjunctmatrix en Formule voor de Inverse]]
- **Regel van Cramer:**
  $$x_j = \frac{\det(A_j)}{\det(A)}$$
  🔗 [[Ch 04 - Lineaire Stelsels#3.3 Methode van Cramer]]
- **Gram-Schmidt Orthogonalisatiestap:**
  $$\mathbf{v}_k = \mathbf{u}_k - \sum_{j=1}^{k-1} \frac{\langle \mathbf{u}_k, \mathbf{v}_j \rangle}{\|\mathbf{v}_j\|^2} \mathbf{v}_j$$
  🔗 [[Ch 06 - Basis, Dimensie en Coördinaten#4. Orthonormale Basissen en Gram-Schmidt]]
- **Kleinste-kwadraten normaalvergelijking:**
  $$A^T A \hat{\mathbf{x}} = A^T \mathbf{b}$$
  🔗 [[Ch 07 - Beste Benadering en Orthogonale Projecties#4. Toepassing Kleinste-kwadratenmethode]]

---

## 📈 Deel 3: Analyse
- **Sinus Cardinalis Limiet:**
  $$\lim_{x \to 0} \frac{\sin x}{x} = 1, \quad \lim_{x \to 0} \frac{1 - \cos x}{x^2} = \frac{1}{2}$$
  🔗 [[Ch 03 - Limieten#2.2 Belangrijke Standaardlimiet (Sinus Cardinalis)]]
- **Regel van de l'Hôpital:**
  $$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)} \quad \left(\text{voor } \left[\frac{0}{0}\right] \text{ of } \left[\frac{\infty}{\infty}\right]\right)$$
  🔗 [[Ch 03 - Limieten#3. Regel van de l'Hôpital]]
- **Convergentietest van d'Alembert:**
  $$\lim_{n \to \infty} \frac{u_{n+1}}{u_n} = \rho \quad (\rho < 1 \implies \text{conv}, \; \rho > 1 \implies \text{div})$$
  🔗 [[Ch 04 - Rijen en Reeksen van Reële Getallen#3. Convergentiecriteria voor Reeksen met Positieve Termen]]
- **Partiële Integratie:**
  $$\int u \, dv = u v - \int v \, du$$
  🔗 [[Ch 06 - Onbepaalde Integralen#2.2 Partiële Integratie]]
- **Oppervlakte van een poolgebied:**
  $$A = \frac{1}{2} \int_\alpha^\beta [f(\theta)]^2 \, d\theta$$
  🔗 [[Ch 08 - Toepassingen van Bepaalde Integralen#1.3 Poolkromme]]
- **Booglengte van een Cartesische kromme:**
  $$L = \int_a^b \sqrt{1 + [f'(x)]^2} \, dx$$
  🔗 [[Ch 08 - Toepassingen van Bepaalde Integralen#2. Booglengte van een Gladde Kromme]]
- **Taylor- en Maclaurinreeks:**
  $$f(x) = \sum_{n=0}^\infty \frac{f^{(n)}(0)}{n!} x^n$$
  🔗 [[Ch 09 - Functiereeksen en Reeksontwikkelingen#3. Taylor- en Maclaurinreeksen]]
