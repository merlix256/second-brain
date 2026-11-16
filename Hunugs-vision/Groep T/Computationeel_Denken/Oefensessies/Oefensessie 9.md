---
course: "Computationeel Denken (T1ACD1)"
unit_type: oefensessie
status: todo
completed: false
est_hours: 2.0
priority: high
tags:
  - study-unit
---

# Oefensessie 9: Bestandsbewerking & File I/O

> **Navigatie:** [[Index]] | [[Exercise Session Tracker]] | [[Sessie 9 - File IO]] | [[Sessie 9 - Q&A]]

---

## 🎯 Doelstellingen
- Robuust bestanden openen met de `with open(...)` context manager.
- Tekstbestanden regel voor regel inlezen en parsen (`.strip()`, `.split()`).
- Berekende statistieken formatteren en wegschrijven naar een nieuw uitvoerbestand.

---

## 🛠️ Praktijkopgaven

### Opgave 9.1: Analyse van Examenresultaten uit CSV
**Probleemstelling:**
Gegeven een CSV-bestand `studenten.csv` met de structuur:
```csv
Studentnummer,Voornaam,Achternaam,Score
r0123456,Jan,Janssens,14.5
r0987654,Marie,Peeters,17.0
```
Schrijf een functie `analyseer_cijfers(bestandsnaam)` die het bestand inleest en een dictionary of tuple retourneert met:
1. Het gemiddelde cijfer op 20.
2. De hoogst behaalde score.
3. Het aantal studenten dat geslaagd is ($\ge 10.0$).

- **Vereiste Theoretische Concepten:**
  - Context manager `with open(...)`: [[Sessie 9 - File IO#3. Bestandsbeheer met de with-Context Manager]]
  - File reading via iteratie: [[Sessie 9 - File IO#4. Methoden om Bestanden te Lezen]]
  - String parsing met `.strip()` en `.split(',')`: [[Sessie 9 - File IO#5. Parsen van Gestructureerde Gegevens (CSV-bestanden)]]

---

### Opgave 9.2: Automatisch Logbestand Genereren
**Probleemstelling:**
Schrijf een functie `schrijf_foutrapport(foutenlijst, logpad)` die een lijst van foutmeldingen wegrijft naar een tekstbestand met tijdstempel in `'a'` (append) mode.

- **Vereiste Theoretische Concepten:**
  - File writing modes `'w'` en `'a'`: [[Sessie 9 - File IO#2. De open() Functie en File Modes]]