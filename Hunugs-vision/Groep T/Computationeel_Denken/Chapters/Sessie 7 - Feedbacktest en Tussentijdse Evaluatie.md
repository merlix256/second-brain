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

# Sessie 7: Feedbacktest en Tussentijdse Evaluatie

> **Navigatie:** [[Index]] | [[Exercise Session Tracker]] | [[Sessie 7 - Q&A]] | [[Oefensessie 7 - Feedbacktest]]

---

## 1. Doel en Structuur van de Feedbacktest
Tijdens deze sessie wordt een tussentijdse formatieve feedbacktest georganiseerd over de eerste helft van de cursus (Sessie 1 t.e.m. Sessie 6).

> [!NOTE] Formele Modaliteiten (Toledo)
> - **Formatief karakter**: De score telt **niet** mee voor het finale eindcijfer.
> - **Doel**: Geeft objectieve feedback over de beheersing van basissyntaxis, controlepaden, functies en lijstmanipulatie.
> - **Regels**: De docent verstrekt ter plekke de toegangscode. Studenten mogen een **handgeschreven samenvatting** gebruiken (zie [[Exam Preparation#De 4-Pagina Strategie]]).

---

## 2. Inhoudelijke Focus & Synthese
De feedbacktest toetst of de student theorie kan omzetten in correct werkende Python-code.

### 2.1 Kerncompetenties
1. **Flowchart & Logica omzetten**: Een beschreven algoritme implementeren met de juiste `if`-vertakkingen en lussen.
2. **Functiespecificaties respecteren**: Exact de gevraagde functienaam, parameters en type returnwaarde implementeren.
3. **Off-by-One Fouten Vermijden**: Begrijpen dat `range(n)` stopt bij $n-1$ en indices lopen van $0$ tot $\text{len}(lst)-1$.
4. **Randvoorwaarden (Edge Cases) afhandelen**:
   - Lege lijst (`[]`) of lengte 0.
   - Negatieve getallen of nuldelingen ($/ 0$).
   - Reeds gesorteerde data of data met dubbele waarden.

---

## 3. Typische Examen- en Testfouten
Analyse van veelgemaakte fouten tijdens de feedbacktest:
- **`return` in plaats van `print`**: De testomgeving controleert de returnwaarde van functies. Wie `print()` gebruikt, retourneert `None` en scoort 0 punten op de testcase.
- **Te vroege `return` in een lus**: Een `return` statement in de body van een `for`-lus zorgt dat de lus na 1 iteratie stopt.
- **Modificeren van een lijst tijdens iteratie**:
  ```python
  # SLECHT:
  for x in lst:
      if x % 2 == 0:
          lst.remove(x) # Verstoort de interne indexering van de lus!
  ```

---

## 📝 Samenvatting
Sessie 7 fungeert als ijkmoment voor de praktische programmeervaardigheid. Er wordt getest op het nauwkeurig volgen van functiespecificaties, randgevallen en het vermijden van typische valkuilen zoals aliasing of foute returnconstructies.