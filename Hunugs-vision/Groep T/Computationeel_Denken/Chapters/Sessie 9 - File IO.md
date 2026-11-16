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

# Sessie 9: File I/O (Input/Output)

> **Navigatie:** [[Index]] | [[Exercise Session Tracker]] | [[Sessie 9 - Q&A]] | [[Oefensessie 9]]

---

## 1. Persistente Gegevensopslag
Variabelen in het RAM-geheugen verdwijnen zodra het programma stopt. Om data persistent te bewaren en externe datasets te laden, communiceren we met het bestandssysteem via **File I/O Streams**.

---

## 2. De `open()` Functie en File Modes
Syntaxis: `file_object = open(bestandsnaam, mode, encoding="utf-8")`

| Mode | Betekenis | Gedrag indien bestand niet bestaat | Overschrijft data? |
| :---: | :--- | :--- | :---: |
| `'r'` | **Read** (lezen, standaard) | Werpt `FileNotFoundError` | Nee (alleen-lezen) |
| `'w'` | **Write** (schrijven) | Maakt nieuw bestand aan | **Ja**, wist bestaande inhoud! |
| `'a'` | **Append** (toevoegen) | Maakt nieuw bestand aan | Nee, schrijft achteraan |

---

## 3. Bestandsbeheer met de `with`-Context Manager
In professionele Python-code openen we bestanden altijd met het `with`-statement. Dit garandeert dat de stream automatisch gesloten wordt, zelfs als er een runtime fout optreedt.

```python
with open("data.txt", "r", encoding="utf-8") as f:
    inhoud = f.read()
# Hier is de bestandsverbinding gegarandeerd gesloten!
```

---

## 4. Methoden om Bestanden te Lezen
1. **`f.read()`**: Leest het volledige bestand in als één grote string (`str`).
2. **`f.readline()`**: Leest één enkele regel (tot en met de `\n` newline).
3. **`f.readlines()`**: Leest alle regels in als een lijst van strings (`list[str]`).
4. **Direct itereren over de file handler** (Meest geheugenefficiënt!):
   ```python
   with open("data.txt", "r", encoding="utf-8") as f:
       for line in f:
           clean_line = line.strip() # Verwijdert 
 en spaties aan de randen
           print(clean_line)
   ```

---

## 5. Parsen van Gestructureerde Gegevens (CSV-bestanden)
Data wordt vaak aangeleverd als CSV (Comma-Separated Values). We combineren bestandsverwerking met stringmanipulatie:

```python
def lees_meetwaarden(pad):
    resultaten = []
    with open(pad, "r", encoding="utf-8") as f:
        for regel in f:
            onderdelen = regel.strip().split(",")
            tijdstip = float(onderdelen[0])
            spanning = float(onderdelen[1])
            resultaten.append([tijdstip, spanning])
    return resultaten
```

---

## 📝 Samenvatting
File I/O stelt programma's in staat om persistente data op schijf te lezen en schrijven. Het `with open(...)` construct fungeert als veilige context manager. Bij het parsen van tekstbestanden zijn methodes zoals `.strip()` (verwijderen van trailing whitespaces/newlines) en `.split()` (opsplitsen op delimiters) onmisbaar.