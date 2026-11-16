---
course: "Computationeel Denken (T1ACD1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: medium
tags:
  - study-unit
---

# Sessie 2: Variabelen en Branching Controlestructuren

> **Navigatie:** [[Index]] | [[Exercise Session Tracker]] | [[Sessie 2 - Q&A]] | [[Oefensessie 2]]

---

## 1. Variabelen, Gegevenstypes en Toewijzing
In Python is een variabele een referentie (naam) naar een object in het geheugen.

### 1.1 Elementaire Datatypes (Primitive Types)
- **`int`**: Gehele getallen (willekeurige precisie in Python 3, bv. `42`, `-10`).
- **`float`**: Reële getallen met dubbele precisie (IEEE 754 standaard, bv. `3.14159`, `1e-4`).
- **`str`**: Tekstreeksen van immutabele Unicode-karakters (`"KU Leuven"`, `'Python'`).
- **`bool`**: Booleaanse waarden (`True` of `False`).

> [!NOTE] Typecasting (Typeconversie)
> Expliciete conversie gebeurt met constructoren:
> ```python
> a = int("123")      # Converteert string naar int
> b = float(42)       # 42.0
> c = str(3.14)       # "3.14"
> ```

### 1.2 Rekenkundige Operatoren
Laat $a$ en $b$ getallen zijn:
- Optelling: $a + b$
- Aftrekking: $a - b$
- Vermenigvuldiging: $a \cdot b$ (`a * b`)
- Reële deling: $\frac{a}{b}$ (`a / b`, retourneert altijd een `float`)
- Gehele deling (Floor division): $\lfloor \frac{a}{b} \rfloor$ (`a // b`)
- Modulo (Rest na gehele deling): $a \pmod b$ (`a % b`)
- Machtsverheffing: $a^b$ (`a ** b`)

---

## 2. Booleaanse Algebra en Logische Operatoren
Besluitvorming rust op vergelijkings- en logische operatoren:

### 2.1 Vergelijkingsoperatoren
- Gelijk aan: `==`
- Niet gelijk aan: `!=`
- Strikt kleiner / groter: `<`, `>`
- Kleiner/gelijk of groter/gelijk: `<=`, `>=`

### 2.2 Logische Connectieven & Waarheidstabellen
Laat $P$ en $Q$ booleaanse proposities zijn:
- **Conjunctie (`and`)**: $P \land Q$ (Waar desda beide waar zijn).
- **Disjunctie (`or`)**: $P \lor Q$ (Waar indien minstens één waar is).
- **Negatie (`not`)**: $\neg P$ (Inverteert de waarheidswaarde).

> [!WARNING] Wetten van De Morgan
> Handig bij het herstructureren van ingewikkelde `if`-condities:
> $$\neg (P \land Q) \iff (\neg P) \lor (\neg Q)$$
> $$\neg (P \lor Q) \iff (\neg P) \land (\neg Q)$$

---

## 3. Conditionele Branching (`if`, `elif`, `else`)
Branching stelt een programma in staat om verschillende uitvoeringspaden te kiezen op basis van een evaluatie.

![[Slide_Sessie2_Branching_Flowchart.png]]
*Figuur 1: Stroomdiagram van een meervoudige vertakking (if-elif-else).*

```python
score = float(input("Voer je behaalde score op 20 in: "))

if score >= 10.0:
    print("Geslaagd!")
elif score >= 8.0:
    print("Tolereerbare onvoldoende")
else:
    print("Niet geslaagd")
```

### 3.1 Short-Circuit Evaluatie
Python evalueert logische expressies van links naar rechts en stopt zodra het resultaat vaststaat:
- In `A and B`: als `A` evalueert naar `False`, wordt `B` **niet** uitgevoerd.
- In `A or B`: als `A` evalueert naar `True`, wordt `B` **niet** uitgevoerd.

```python
# Voorkomt een ZeroDivisionError dankzij short-circuiting:
if count != 0 and (total / count) > threshold:
    print("Drempelwaarde overschreden")
```

---

## 📝 Samenvatting
Variabelen koppelen geheugenlocaties aan datatypes zoals `int`, `float`, `str` en `bool`. Booleaanse expressies vormen het controlemechanisme voor vertakkingen via `if`-`elif`-`else`. Dankzij short-circuit evaluatie kunnen runtime-fouten elegant vermeden worden.