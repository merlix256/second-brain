---
title: "Waarden in Technologie: Typologie & Botsingen"
course: "Ethiek"
tags:
  - ethiek/waarden
  - techniekfilosofie
  - botsingsprobleem
date_created: 2026-11-10
---

# ⚖️ Waarden in Technologie: Typologie & Botsingen

## 1. De Hiërarchie van Waarden

```mermaid
flowchart TD
    W["WAARDEN"]

    W --> WH["1. Waarde HEBBEN"]
    WH --> WH_INST["Instrumentele Waarde<br/>(Dient een doel, e.g. een hamer of AI-code)"]
    WH --> WH_FIN["Finale / Emotionele Waarde<br/>(Waarde op zich door sentiment, e.g. trouwring)"]

    W --> WZ["2. Waarde ZIJN"]
    WZ --> WZ_NEUT["Moreel Neutrale Waarden<br/>(Efficiëntie, Accuraatheid, Waarheid, Snelheid)"]
    WZ --> WZ_MOR["Moreel Geladen Waarden<br/>(Fairness, Privacy, Duurzaamheid, Autonomie)"]
```

* **Cruciaal:** De Neutraliteitsthese (smalle zin) heeft uitsluitend betrekking op de claim dat technologie **per definitie vrij is van waarden die 'zijn' in morele zin**.

---

## 2. Het Botsingsprobleem (Trade-Off Analyse)

Wanneer ingenieurs morele waarden willen integreren in het ontwerp van een algoritme (Value-Sensitive Design), botsen deze waarden onvermijdelijk met moreel neutrale waarden:

```mermaid
quadrantChart
    title Waarde-afweging bij AI-kredietsystemen
    x-axis Lage Fairness --> Hoge Fairness (Statistische Pariteit)
    y-axis Lage Accuraatheid --> Hoge Accuraatheid (Exacte Predictie)
    quadrant-1 "Ideaal (Wiskundig Onmogelijk)"
    quadrant-2 "Zuiver Technisch (Groot Bias-risico)"
    quadrant-3 "Slecht Systeem (Beide Falen)"
    quadrant-4 "Ethisch Gelijk (Minder Accuraat)"
    "Standaard Bank-AI": [0.2, 0.85]
    "Gecorrigeerd Ethisch Algoritme": [0.85, 0.4]
```

### De Wiskundige Onmogelijkheid van Dubbele Fairness
Onderzoek naar risico-taxatietools (zoals COMPAS) bewijst dat bij verschillende basisincidenties tussen twee groepen:
1. **Statistische Pariteit** (gelijk percentage gunstige beslissingen), en
2. **Predictieve Gelijkheid** (gelijke kans op fout-positieven en fout-negatieven),
**nooit wiskundig gelijktijdig verwezenlijkt kunnen worden.**
