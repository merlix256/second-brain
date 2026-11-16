---
course: "Computationeel Denken (T1ACD1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.0
priority: medium
tags:
  - study-unit
---

# Sessie 9 - Q&A (Active Recall)

> **Verwijzingen:** [[Sessie 9 - File IO]] | [[Oefensessie 9]] | [[Index]]

---

### Vraag 1: Waarom is het gebruik van `with open(...) as f:` te verkiezen boven manuele `f.close()` aanroepen?
**Antwoord:**
Het `with`-statement implementeert het Python context-manager protocol. Het garandeert dat de file descriptor altijd netjes gesloten wordt zodra het blok wordt verlaten, zelfs als er zich halverwege het lezen/schrijven een onverwachte exception voordoet. Zonder `with` kan een crash ertoe leiden dat het bestand gelockt blijft door het OS of dat schrijf-buffers niet geflusht worden naar schijf.
*Theorielink:* [[Sessie 9 - File IO#3. Bestandsbeheer met de with-Context Manager]]

---

### Vraag 2: Wat is het verschil in functionaliteit en dataformaat tussen `f.read()`, `f.readline()` en `f.readlines()`?
**Antwoord:**
- `f.read()`: Retourneert de **volledige inhoud** van het bestand als één aaneengesloten `str`.
- `f.readline()`: Leest **één regel** vanaf de huidige cursorpositie tot aan de volgende `\n` en retourneert een `str`.
- `f.readlines()`: Leest alle regels van het bestand en retourneert ze als een **lijst van strings** (`list[str]`), waarbij elke string eindigt op `\n`.
*Theorielink:* [[Sessie 9 - File IO#4. Methoden om Bestanden te Lezen]]

---

### Vraag 3: Waarom moet je bij het parsen van regels uit een tekstbestand vrijwel altijd `.strip()` gebruiken alvorens te converteren met `float()` of `int()`?
**Antwoord:**
Regels die uit een bestand worden gelezen bevatten aan het einde vrijwel altijd een line-feed karakter (`\n` of `\r\n`). Bovendien kunnen er onzichtbare spaties aan het begin of einde staan. `.strip()` snoeit al deze whitespace tekens weg, waardoor functies zoals `.split(",")` zuivere substrings opleveren en parsing errors worden voorkomen.
*Theorielink:* [[Sessie 9 - File IO#5. Parsen van Gestructureerde Gegevens (CSV-bestanden)]]