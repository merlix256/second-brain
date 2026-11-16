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

# Sessie 3: Functies 1 - Definitie, Aanroep en Parameters

> **Navigatie:** [[Index]] | [[Exercise Session Tracker]] | [[Sessie 3 - Q&A]] | [[Oefensessie 3]]

---

## 1. Functies als Decompositie-instrument
Functies zijn fundamenteel voor de pijler **decompositie**: het opdelen van een complex script in zelfstandige, herbruikbare bouwstenen.

### 1.1 Doelstellingen van Modulariteit
- **Herbruikbaarheid (DRY-principe: Don't Repeat Yourself)**: Voorkomt gedupliceerde code.
- **Leesbaarheid**: Abstractie van complexe logica achter een expressieve functienaam.
- **Testbaarheid**: Deeloplossingen kunnen geïsoleerd worden getest via unit tests.

---

## 2. Syntaxis: Definitie en Aanroep
Een functie wordt gedefinieerd met het sleutelwoord `def`, gevolgd door de naam en parameters:

```python
def bereken_oppervlakte_rechthoek(lengte, breedte):
    oppervlakte = lengte * breedte
    print(f"De oppervlakte is: {oppervlakte}")

# Aanroep:
bereken_oppervlakte_rechthoek(5.0, 3.0)
```

### 2.1 Formele vs. Actuele Parameters
- **Formele parameters**: De variabelen zoals gedefinieerd in de functieheader (`lengte`, `breedte`).
- **Actuele parameters (argumenten)**: De concrete waarden of variabelen die worden meegegeven bij de function call (`5.0`, `3.0`).

---

## 3. Parameteroverdracht: Positioneel, Default en Keyword
Python biedt flexibele manieren om parameters te voeden:

### 3.1 Positionele vs. Keyword Argumenten
```python
def bereken_kracht(massa, versnelling):
    return massa * versnelling

# Positioneel:
f1 = bereken_kracht(10, 9.81)

# Keyword (volgorde maakt niet uit):
f2 = bereken_kracht(versnelling=9.81, massa=10)
```

### 3.2 Default Parameters
Parameters kunnen een standaardwaarde krijgen. Default parameters moeten **achteraan** de parameterlijst staan!
```python
def begroeting(naam, titel="Ing."):
    print(f"Dag {titel} {naam}")
```

---

## 4. Variabelenscope en de Call Stack
Wanneer een functie wordt aangeroepen, maakt de Python interpreter een nieuw **lokaal frame** (stack frame) aan op de **Call Stack**.

![[Slide_Sessie3_Call_Stack_Diagram.png]]
*Figuur 1: De Call Stack en isolatie van lokale variabelen tijdens functie-executie.*

### 4.1 LEGB-Regel voor Scope Resolutie
Python zoekt namen op in vier niveaus:
1. **L**ocal: Binnen de huidige functie.
2. **E**nclosing: In omsluitende functies (bij geneste functies).
3. **G**lobal: Op module-/scriptniveau.
4. **B**uilt-in: Ingebouwde namen van Python (`print`, `len`, `range`).

> [!WARNING] Vermijd `global`
> Het wijzigen van globale variabelen binnen functies leidt tot "side effects" (neveneffecten) en bemoeilijkt debuggen. Geef data altijd door via parameters en retourneer resultaten!

---

## 📝 Samenvatting
Functies operationaliseren decompositie en abstractie in code. We onderscheiden formele van actuele parameters en kunnen argumenten positioneel of per keyword doorgeven. Variabelen binnen een functie hebben een lokale scope en leven op het actieve stack frame van de call stack.