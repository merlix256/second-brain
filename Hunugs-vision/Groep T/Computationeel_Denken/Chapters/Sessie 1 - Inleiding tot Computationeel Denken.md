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

# Sessie 1: Inleiding tot Computationeel Denken

> **Navigatie:** [[Index]] | [[Exercise Session Tracker]] | [[Sessie 1 - Q&A]] | [[Oefensessie 1]]

---

## 1. Wat is Computationeel Denken?
Computationeel denken is een probleemoplossende methode waarbij menselijke denkkracht wordt gecombineerd met de computationele verwerkingskracht van een machine. Het doel is om complexe problemen zodanig te formaliseren dat een computer (of een mens) ze deterministisch kan uitvoeren.

> [!NOTE] Definitie (Wing, 2006)
> *"Computational thinking involves solving problems, designing systems, and understanding human behavior, by drawing on the concepts fundamental to computer science."*

![[Slide_Sessie1_Pillars_Diagram.png]]
*Figuur 1: De vier/vijf fundamentele pijlers van Computationeel Denken.*

### 1.1 De Vijf Fundamentele Pijlers
1. **Decompositie (Decomposition)**:
   - Het ontleden van een omvangrijk, complex probleem in kleinere, onafhankelijke en beheersbare deelproblemen.
   - *Wiskundige analogie:* Het bepalen van de oplossing van een samengesteld stelsel door substitutie van tussenfuncties:
     $$f(x, y) = g(h(x), k(y))$$
2. **Patroonherkenning (Pattern Recognition)**:
   - Het identificeren van overeenkomsten, herhalingen of wetmatigheden in gegevens of processen.
3. **Abstractie (Abstraction)**:
   - Het weglaten van niet-essentiële details om de kernstructuur van een probleem te modelleren.
   - *Voorbeeld:* Een metrokaart toont alleen topologie (haltes en verbindingen), geen werkelijke geografische afstanden.
4. **Algoritmisch Denken (Algorithmic Thinking)**:
   - Het formuleren van een eindige, stapsgewijze en ondubbelzinnige reeks instructies om het probleem op te lossen.
5. **Evaluatie & Optimalisatie (Evaluation)**:
   - Het verifiëren van de correctheid en het analyseren van de efficiëntie van de oplossing (bijvoorbeeld tijdscomplexiteit $\mathcal{O}(n)$).

---

## 2. Computerarchitectuur in een Notendop
Om imperatieve programma's te begrijpen, moeten we weten hoe hardware instructies verwerkt.

![[Slide_Sessie1_Von_Neumann_Architecture.png]]
*Figuur 2: Von Neumann-architectuur (CPU, Geheugen en I/O).*

- **Processor (CPU)**:
  - Bevat de *Arithmetic Logic Unit* (ALU) en de *Control Unit* (CU). Voert de fetch-decode-execute cyclus uit op machineniveau.
- **Primair Geheugen (RAM)**:
  - Vluchtig (*volatile*) werkgeheugen georganiseerd in adresseerbare cellen. Variabelen worden toegewezen aan specifieke geheugenadressen.
- **I/O-Eenheden**:
  - Toetsenbord, scherm, bestandsopslag (secundair geheugen).

---

## 3. Flowcharts & Algoritmische Notatie
Voordat we Python-code schrijven, visualiseren we logische controlepaden met flowcharts volgens gestandaardiseerde symbolen:

| Symbool | Betekenis | Python Equivalent |
| :--- | :--- | :--- |
| **Ovaal / Afgeronde Rechthoek** | Start / Einde van het algoritme | `def main():` / `exit()` |
| **Rechthoek** | Proces / Berekening / Toewijzing | `x = a + b` |
| **Ruit (Diamond)** | Beslissing / Conditie | `if condition:` |
| **Parallellogram** | Input / Output operaties | `input()` / `print()` |

> [!TIP] Algoritmische Evaluatie
> Een goed algoritme voldoet aan drie voorwaarden:
> 1. **Determinisme**: Voor een identieke invoer produceert het altijd exact dezelfde uitvoer.
> 2. **Eindigheid**: Het stopt na een discreet aantal stappen $k < \infty$.
> 3. **Effectiviteit**: Elke stap is elementair en uitvoerbaar.

---

## 📝 Samenvatting
Computationeel denken vormt het intellectuele fundament van programmeren in Python. Het bestaat uit vijf complementaire pijlers: decompositie, patroonherkenning, abstractie, algoritmisch denken en evaluatie. Algoritmes worden visueel geconcipieerd in flowcharts en gemodelleerd naar de werking van de CPU en het RAM-geheugen.