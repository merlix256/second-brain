---
course: "Computationeel Denken (T1ACD1)"
unit_type: oefensessie
status: done
completed: true
est_hours: 2.0
priority: high
tags:
  - study-unit
---
# Oefensessie 2: Variabelen, Types & Branching

> **Navigatie:** [[Index]] | [[Exercise Session Tracker]] | [[Sessie 2 - Variabelen en Branching Controlestructuren]] | [[Sessie 2 - Q&A]]

---

## 🎯 Doelstellingen
- Correct omgaan met types (`int`, `float`, `str`, `bool`) en expliciete typecasting.
- Toepassen van rekenkundige operatoren (`//`, `%`, `**`).
- Implementeren van samengestelde `if`-`elif`-`else` vertakkingen met short-circuit logica.

---

## 🛠️ Praktijkopgaven

### Opgave 2.1: Splitsing van Tijdsintervallen (Gehele Deling & Modulo)
**Probleemstelling:**
Schrijf een programma dat een geheel aantal seconden $S$ inleest van de gebruiker en dit converteert naar uren, minuten en resterende seconden:
$$\text{Uren} = \lfloor S / 3600 \rfloor$$
$$\text{Resterend} = S \pmod{3600}$$
$$\text{Minuten} = \lfloor \text{Resterend} / 60 \rfloor$$
$$\text{Seconden} = \text{Resterend} \pmod{60}$$

- **Vereiste Theoretische Concepten:**
  - Gehele deling `//` en Modulo `%`: [[Sessie 2 - Variabelen en Branching Controlestructuren#1.2 Rekenkundige Operatoren]]
  - Typecasting van `input()` naar `int`: [[Sessie 2 - Variabelen en Branching Controlestructuren#1.1 Elementaire Datatypes (Primitive Types)]]

---

### Opgave 2.2: Driehoekvalidatie en Classificatie
**Probleemstelling:**
Lees drie zijden $a, b, c \in \mathbb{R}^+$ in. Controleer eerst via de driehoeksongelijkheid of deze zijden een geldige driehoek kunnen vormen:
$$a + b > c \quad \land \quad a + c > b \quad \land \quad b + c > a$$
Zo ja, bepaal of de driehoek gelijkzijdig ($a = b = c$), gelijkbenig, of ongelijkzijdig is.

- **Vereiste Theoretische Concepten:**
  - Booleaanse expressies en logische `and`: [[Sessie 2 - Variabelen en Branching Controlestructuren#2.2 Logische Connectieven & Waarheidstabellen]]
  - Meervoudige branching met `if-elif-else`: [[Sessie 2 - Variabelen en Branching Controlestructuren#3. Conditionele Branching (if, elif, else)]]