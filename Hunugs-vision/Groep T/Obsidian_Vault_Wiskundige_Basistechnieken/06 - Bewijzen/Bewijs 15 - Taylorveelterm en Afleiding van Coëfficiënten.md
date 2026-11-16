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

# Bewijs 15: De Taylorveelterm en Afleiding van de Coëfficiënten

> [!abstract] Context & Examenbelang
> **Theorievraag 15:** *"Leid de uitdrukking af voor de beste $n$-de graads veeltermbenadering (Taylorveelterm) van een functie $f(x)$ in de omgeving van een ontwikkelingspunt $x = a$."*
> **Verwante Theorie:** [[Ch 09 - Functiereeksen en Reeksontwikkelingen#2. Taylor- en Maclaurinreeksen]]
> **Formularium:** [[Formularium#3. Analyse]] | **MOC:** [[00 - Index der Bewijzen]]

---

## 1. Formulering van de Stelling
Zij $f: I \subseteq \mathbb{R} \to \mathbb{R}$ een functie die minstens $n$ maal continu afleidbaar is in een omgeving van het punt $x = a$.
De **beste $n$-de graads veeltermbenadering** van $f(x)$ in de omgeving van $x = a$ is de veelterm $P_n(x)$ van ten hoogste graad $n$ die in het punt $x = a$ dezelfde functiewaarde én dezelfde eerste $n$ afgeleiden bezit als de functie $f(x)$:
$$P_n^{(k)}(a) = f^{(k)}(a) \quad \text{voor alle } k \in \{0, 1, 2, \dots, n\}$$
Deze veelterm wordt gegeven door de **Taylorveelterm van orde $n$**:
$$P_n(x) = \sum_{k=0}^n \frac{f^{(k)}(a)}{k!} (x - a)^k$$
waarbij de Taylor-coëfficiënten $a_k$ gegeven worden door:
$$a_k = \frac{f^{(k)}(a)}{k!}$$

---

## 2. Stap-voor-stap Bewijs

### Stap 1: Algemene Vorm van een $n$-de Graads Veelterm rond $x = a$
Een willekeurige veelterm van de graad $n$ kan altijd ontwikkeld worden naar opklimmende machten van $(x - a)$:
$$P_n(x) = a_0 + a_1(x - a) + a_2(x - a)^2 + a_3(x - a)^3 + \dots + a_n(x - a)^n = \sum_{i=0}^n a_i (x - a)^i$$
waarbij $a_0, a_1, \dots, a_n \in \mathbb{R}$ nog te bepalen onbekende coëfficiënten zijn.

### Stap 2: Berekening van Opeenvolgende Afgeleiden
We differentiëren $P_n(x)$ herhaaldelijk naar $x$:

1. **Nulde afgeleide ($k = 0$, de veelterm zelf):**
   $$P_n(x) = a_0 + a_1(x - a) + a_2(x - a)^2 + a_3(x - a)^3 + \dots + a_n(x - a)^n$$
2. **Eerste afgeleide ($k = 1$):**
   $$P_n'(x) = a_1 + 2 a_2(x - a) + 3 a_3(x - a)^2 + \dots + n a_n(x - a)^{n-1}$$
3. **Tweede afgeleide ($k = 2$):**
   $$P_n''(x) = 2 \cdot 1 \cdot a_2 + 3 \cdot 2 \cdot a_3(x - a) + 4 \cdot 3 \cdot a_4(x - a)^2 + \dots + n(n-1) a_n(x - a)^{n-2}$$
4. **Derde afgeleide ($k = 3$):**
   $$P_n'''(x) = 3 \cdot 2 \cdot 1 \cdot a_3 + 4 \cdot 3 \cdot 2 \cdot a_4(x - a) + \dots + n(n-1)(n-2) a_n(x - a)^{n-3}$$

### Stap 3: Algemene $k$-de Afgeleide ($k \le n$)
Voor een willekeurige afgeleide van orde $k$ splitsen we de sommatie op in drie categorieën termen:
- Termen met graad $i < k$: deze zijn na $k$ keer afleiden gelijk aan nul ($\frac{d^k}{dx^k}[(x - a)^i] = 0$).
- De term met graad $i = k$:
  $$\frac{d^k}{dx^k}[a_k (x - a)^k] = a_k \cdot k!$$
- Termen met graad $i > k$:
  $$\frac{d^k}{dx^k}[a_i (x - a)^i] = a_i \cdot \frac{i!}{(i - k)!} (x - a)^{i - k}$$

De algemene $k$-de afgeleide luidt bijgevolg:
$$P_n^{(k)}(x) = k! \cdot a_k + \sum_{i = k+1}^n a_i \frac{i!}{(i - k)!} (x - a)^{i - k}$$

### Stap 4: Evaluatie in het Ontwikkelingspunt $x = a$
Vul nu $x = a$ in in de uitdrukking voor $P_n^{(k)}(x)$:
Voor alle termen in de sommatie met $i \ge k + 1$ bevat de factor $(x - a)^{i - k}$ een strikt positieve macht van $(x - a)$.
Bijgevolg wordt voor $x = a$:
$$(a - a)^{i - k} = 0^{i - k} = 0 \quad (\text{voor alle } i > k)$$
Hierdoor verdwijnt de volledige sommatie, en blijft uitsluitend de constante term over:
$$P_n^{(k)}(a) = k! \cdot a_k + 0 = k! \cdot a_k$$

### Stap 5: Opleggen van de Contactvoorwaarde
De voorwaarde voor de beste veeltermbenadering dicteert dat:
$$P_n^{(k)}(a) = f^{(k)}(a)$$
Gelijkstellen levert de fundamentele vergelijking:
$$k! \cdot a_k = f^{(k)}(a)$$
Aangezien $k! \neq 0$ (met afspraak $0! = 1$), kunnen we direct delen door $k!$:
$$a_k = \frac{f^{(k)}(a)}{k!} \quad \blacksquare$$

Substitutie van deze unieke coëfficiënten in de veelterm levert de gezochte Taylorveelterm:
$$P_n(x) = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \dots + \frac{f^{(n)}(a)}{n!}(x - a)^n = \sum_{k=0}^n \frac{f^{(k)}(a)}{k!} (x - a)^k$$

---

## 3. Maclaurinveelterm als Bijzonder Geval
Wanneer het ontwikkelingspunt gekozen wordt als de oorsprong $a = 0$, verkrijgen we de **Maclaurinveelterm**:
$$P_n(x) = \sum_{k=0}^n \frac{f^{(k)}(0)}{k!} x^k$$
