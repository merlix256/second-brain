---
title: ISO Tekennormen & Lijnsoorten
tags:
  - knowledge-base
  - iso-standards
  - conventions
  - lines
---

# 📏 ISO Tekennormen & Lijnsoorten (ISO 128)

> [!abstract] Referentiekaart Lijnconventies
> Volgens **ISO 128** moeten technische tekeningen een strikte scheiding in lijndikte en lijntype hanteren om vorm, inwendige geometrie en maatvoering eenduidig te communiceren.

---

## 1. Lijnsoorten en Toepassingen (ISO 128-20)

| Type | Benaming | Visuele Weergave | Aanbevolen Dikte | Primaire Toepassing |
| :---: | :--- | :--- | :---: | :--- |
| **A** | Brede doorlopende lijn | `━━━━━━━━━━` | $0.50 - 0.70\text{ mm}$ | Zichtbare omtrekken, zichtbare ribben, grens van bruikbare schroefdraad |
| **B** | Smalle doorlopende lijn | `──────────` | $0.25 - 0.35\text{ mm}$ | Maatlijnen, maat-hulplijnen, arceringen, fictieve overgangslijnen, kerndiameter schroefdraad |
| **C** | Smalle vrijehandlijn | `~~~/\~~~/\~` | $0.25 - 0.35\text{ mm}$ | Begrenzing van gedeeltelijke of onderbroken aanzichten en doorsneden |
| **E / F** | Smalle streeplijn | `----------` | $0.25 - 0.35\text{ mm}$ | Onzichtbare omtrekken, onzichtbare ribben |
| **G** | Smalle streep-stiplijn | `─ · ─ · ─ ·` | $0.25 - 0.35\text{ mm}$ | Aslijnen, hartlijnen, symmetrielijnen, steekcirkels |
| **H** | Smalle streep-stip met brede uiteinden | `━ · ─ · ─ · ━` | Uiteinden $0.7\text{ mm}$ / Midden $0.25\text{ mm}$ | Snijlijnen voor doorsneden (richtingsveranderingen eveneens breed) |

---

## 2. Lijnprioriteit bij Samenvallende Lijnen
Wanneer twee of meer lijnen op een aanzicht samenvallen, geldt de volgende **strikte voorrangsorde**:
1. **Brede volle lijn (Lijntype A)** — Zichtbare omtrekken/ribben overschrijven alles!
2. **Smalle streeplijn (Lijntype E/F)** — Onzichtbare omtrekken/ribben.
3. **Snijlijn (Lijntype H)** — Snijdende vlakken.
4. **Smalle streep-stiplijn (Lijntype G)** — Hartlijnen en symmetrie-assen.
5. **Maatlijnen en hulplijnen (Lijntype B)**.

---

## 3. Projectiesymbolen (Titelhoek / Titelslag)
In het titelhoek van elke tekening moet verplicht de projectiemethode worden vermeld:

- **First Angle (Europese projectie)**:
  - Symbool: Afgeknotte kegel met de cirkelprojecties aan de **rechterzijde**.
  - Formele referentie: ISO 5456-2.
- **Third Angle (Amerikaanse projectie)**:
  - Symbool: Afgeknotte kegel met de cirkelprojecties aan de **linkerzijde**.
