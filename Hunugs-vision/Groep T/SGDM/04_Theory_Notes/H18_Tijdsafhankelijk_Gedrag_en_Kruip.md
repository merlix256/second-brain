---
course: "SGDM (T1ASD1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: medium
tags:
  - study-unit
---

# 🔬 H18: Tijdsafhankelijk Gedrag en Kruip
#theorie #kruip #nabarro-herring #coble #spanningsrelaxatie #H18

[[00_Overview_Dashboard]] | [[01_Formularium_Master#8-tijdsafhankelijk-gedrag--kruip]] | [[05_Oefenzittingen/Sessie_05_Breukmechanica_Vermoeiing_Kruip]]

---

## 1. Wat is Kruip?
Kruip is de tijdsafhankelijke, permanente plastische vervorming van een materiaal onder **constante mechanische belasting**.
* **Temperatuurdrempel**: Wordt dominant zodra de homologe temperatuur $T_h > 0.4 T_m$ (voor metalen in Kelvin) of $T > T_g$ (voor polymeren).

```
 Rek ε
   ^                                   * Kruipbreuk
   |                                 /
   |             Secundair          / (Tertiair)
   |           (Stationair: dε/dt) /
   |      Primair  +--------------+
   |     /--------/
 ε0|----+ (Elastische beginrek)
   +-------------------------------------> Tijd t
```

* **De Drie Kruipstadia**:
  1. **Primair (Transient)**: Reksnelheid $\dot{\epsilon}$ daalt door toenemende dislocatieverstrengeling (rekversteviging).
  2. **Secundair (Stationair / Steady-State)**: $\dot{\epsilon}_s$ is strikt constant. Dynamisch evenwicht tussen koudversteviging en thermisch herstel. Dit stadium bepaalt de operationele levensduur!
  3. **Tertiair**: Reksnelheid versnelt explosief door vorming van interne holtes (caviteiten) op korrelgrenzen, gevolgd door insnoering en kruipbreuk.

---

## 2. Fysische Mechanismen van Metaalkruip
1. **Dislocatieklimmen (Dislocation Climb)**: Dislocaties die geblokkeerd worden door obstakels kunnen dankzij thermisch geactiveerde vacaturediffusie loodrecht uit hun glijvlak klimmen en verder bewegen ($T > 0.5 T_m$).
2. **Nabarro-Herring Kruip (Bulkdiffusie)**: Vacatures migreren dwars door de korrels van trekzones naar drukzones. Dominant bij **zeer hoge temperaturen**.
3. **Coble Kruip (Korrelgrensdiffusie)**: Vacatures diffunderen langs het netwerk van korrelgrenzen. Dominant bij **tussenliggende temperaturen**.

> [!tip] Ontwerpinzicht voor Kruipweerstand
> Voor statische sterkte bij kamertemperatuur wil men fijne korrels (Hall-Petch). Maar voor **hoge kruipweerstand** zijn kleine korrels nefast (veel korrelgrenzen $\implies$ snelle Coble-kruip)! Vliegtuigturbineschoepen worden daarom vervaardigd uit **gerichte gestolde korrels of éénkristallen** zonder korrelgrenzen!

---

## 3. Spanningsrelaxatie
Bij constante opgelegde vervorming ($\epsilon_{\text{tot}} = \epsilon_{el} + \epsilon_{\text{kruip}} = \text{cte}$):
De elastische rek wordt geleidelijk omgezet in permanente kruiprek, waardoor de spanning exponentieel wegzakt:
$$\sigma(t) = \sigma_0 \exp\left(-\frac{t}{\tau_r}\right)$$
* Voorbeeld: Voorspanning in boutverbindingen of klemmen die na verloop van tijd los gaan zitten.

---

> [!summary] Hoofdstuksamenvatting
> Boven $0.4 T_m$ vervormen materialen continu onder constante spanning via diffusie en dislocatieklimmen. Grote korrels of éénkristallen maximaliseren de kruipweerstand.
