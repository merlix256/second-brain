# 🎯 Exam Preparation & Strategy: Computationeel Denken (B-KUL-T1ACD1)

> **Navigatie:** [[Index]] | [[Exercise Session Tracker]] | [[Formularium]] | [[Begrippenlijst]]

---

## 🏛️ 1. Examenreglement & Organisatie (KU Leuven)

Volgens de officiële ECTS-onderwijsfiche van KU Leuven (Campus Groep T Leuven):
- **Type evaluatie:** Computerexamen tijdens de examenperiode (eerste semester).
- **Vorm:** Praktijkexamen / schriftelijk op computer via open programmeervragen.
- **Doel:** Zelfstandig omzetten van beschreven probleemstellingen naar correct werkende, geteste Python-implementaties.
- **Cijfer:** Eén finaal deelcijfer op 20.

> [!IMPORTANT] 🌟 Het Aanwezigheidsbonuspunt (+1/20)
> *"Aanwezigheid tijdens de lesmomenten is niet verplicht, maar studenten die alle sessies bijwonen krijgen één (1) bonuspunt op 20 bovenop de score voor hun examen (mits totaalscore $\le 20$)."*
> - Houd je aanwezigheden nauwkeurig bij via de [[Exercise Session Tracker]]!

---

## 📝 2. De 4-Pagina Samenvattingsstrategie (Toegestaan Materiaal)

Volgens de cursusrichtlijnen:
> *"Studenten mogen hierbij een handgeschreven samenvatting gebruiken van maximaal 4 bladzijden (dus 2 fysieke vellen A4-papier)."*

### Aanbevolen Indeling van je 4 A4-Zijden:

```
┌─────────────────────────┐  ┌─────────────────────────┐
│ Bladzijde 1: BASICS     │  │ Bladzijde 2: FUNCTIES   │
│ - Datatypes & casting   │  │ - Scope & LEGB regels   │
│ - Rekenkunde: //, %, ** │  │ - return vs print       │
│ - De Morgan & Logica    │  │ - Pre-/postcondities    │
│ - if-elif-else templates│  │ - Debugger shortcuts    │
└─────────────────────────┘  └─────────────────────────┘
┌─────────────────────────┐  ┌─────────────────────────┐
│ Bladzijde 3: LUSSEN/1D  │  │ Bladzijde 4: 2D & I/O   │
│ - range(start,stop,step)│  │ - 2D list comprehension │
│ - break / continue      │  │ - Rij vs Kolom loops    │
│ - Slicing: [start:stop] │  │ - with open(..., 'r')   │
│ - Aliasing & .copy()    │  │ - .strip() & .split(',')│
└─────────────────────────┘  └─────────────────────────┘
```

- **Bladzijde 1 (Theorie 1-2):**
  - Overzicht van `//`, `%`, `**` en typecasting functies (`int()`, `float()`, `str()`).
  - Booleaanse waarheidstabellen en Wetten van De Morgan: [[Sessie 2 - Variabelen en Branching Controlestructuren#2.2 Logische Connectieven & Waarheidstabellen]].
- **Bladzijde 2 (Theorie 3-4):**
  - Syntaxis van functies, default parameters (achteraan!), en meervoudige returnwaarden (`tuple unpacking`).
  - Herinnering: *NOOIT `print` gebruiken als er `return` gevraagd wordt!* (Zie [[Sessie 4 - Functies 2 - Returnwaarden en Debugger#1. Returnwaarden vs. print()]]).
- **Bladzijde 3 (Theorie 5-6):**
  - `range()` syntaxis en formules voor stapgroottes: [[Sessie 5 - For- en While-lussen#3.1 De range(start, stop, step) Functie]].
  - Slicing regels `lst[start:stop:step]` en lijstmethodes (`.append()`, `.pop()`, `.extend()`).
  - Rode waarschuwingskader: **Aliasing vermijden via `.copy()`**: [[Sessie 6 - Lijsten#4. Geheugenreferenties: De Aliasing Valkuil]].
- **Bladzijde 4 (Theorie 8-9):**
  - De veilige constructie van 2D-matrices: `[[0 for _ in range(C)] for _ in range(R)]`: [[Sessie 8 - 2D-lijsten#3.1 De Correcte Manier: List Comprehension of Geneste Lussen]].
  - File I/O sjabloon met `with open(..., 'r', encoding='utf-8') as f:` en regelschoonmaak via `.strip().split(',')`: [[Sessie 9 - File IO#5. Parsen van Gestructureerde Gegevens (CSV-bestanden)]].

---

## 🛠️ 3. Stappenplan voor het Computerexamen

Wanneer je een examenopgave leest, volg altijd deze vaste 5 stappen:

1. **Stap 1: Decompositie & Functie-handtekening controleren**
   - Lees de opgave twee keer. Welke naam moet de functie hebben? Welke parameters? Wat is het type van de returnwaarde?
   - Definieer direct de header in je editor: `def functie_naam(parameters):`.
2. **Stap 2: Algoritmisch stappenplan op klad**
   - Schrijf in 3 regels pseudocode op welke datastructuur je bijhoudt (accumulator, vlag, nieuwe lijst).
3. **Stap 3: Implementatie**
   - Schrijf de code lineair en gebruik betekenisvolle variabelenamen.
4. **Stap 4: Randvoorwaarden Testen (Edge Cases)**
   - Test vóór het indienen altijd:
     - Lege lijst `[]` of lege string `""`.
     - Lijst met 1 element.
     - Negatieve getallen en nuldelingen.
     - Zijn alle return-waarden exact van het gevraagde type (int, float, list)?
5. **Stap 5: Syntax- en Lintercontrole**
   - Controleer inspringing (indentation errors), dubbele punten achter `if/for/def`, en haakjes.

---

## 📂 4. Past Exams & Oefenopgaven (Placeholders)

- [[Past Exam 2024 - Semester 1 (Mock)]]
- [[Past Exam 2025 - Semester 1 (Mock)]]
- [[Past Exam - Herexamen Augustus (Mock)]]