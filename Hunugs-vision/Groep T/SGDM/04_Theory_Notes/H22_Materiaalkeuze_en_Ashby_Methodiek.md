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

# 🔬 H22: Materiaalkeuze en Ashby-diagrammen
#theorie #ashby #materiaalkeuze #indices #H22

[[00_Overview_Dashboard]] | [[01_Formularium_Master#9-materiaalselectie-ashby]]

---

## 1. Het 4-Stappen Model van Ashby
Michael Ashby formaliseerde het systematische selectieproces van materialen in de engineering:

```
[ Ontwerpvereisten ] ---> 1. VERTALING (Functie, Doelstelling, Randvoorwaarden, Vrije Variabelen)
                                  |
                                  v
                          2. SCREENING (Elimineer materialen die randvoorwaarden schenden)
                                  |
                                  v
                          3. RANGSCHIKKING (Sorteer via Prestatie-index M)
                                  |
                                  v
                          4. DOCUMENTATIE (Onderzoek beste kandidaten: kosten, milieu, toelevering)
```

---

## 2. Afleiding van Materiaalprestatie-indices ($M$)
Het ontkoppelen van de doelfunctie:
$$P = f_1(\text{Functionele eisen}) \times f_2(\text{Geometrie}) \times f_3(\text{Materiaaleigenschappen } M)$$

### Voorbeeld: Minimale Massa van een Lichte, Stijve Trekstaaf
1. **Functie**: Trekstaaf met lengte $L$.
2. **Doelstelling**: Minimaliseer massa:
   $$m = \rho \cdot A \cdot L$$
3. **Randvoorwaarde**: Maximale elastische verlenging $\Delta L$ bij kracht $F$:
   $$\Delta L = \frac{F L}{E A} \implies A = \frac{F L}{E \Delta L}$$
4. **Substitueer vrije variabele $A$ in de doelfunctie**:
   $$m = \rho \left(\frac{F L}{E \Delta L}\right) L = (F L^2 / \Delta L) \cdot \left(\frac{\rho}{E}\right)$$
5. **Maximaliseer de Materiaalindex**:
   Om $m$ te minimaliseren, moet $\frac{\rho}{E}$ geminimaliseerd worden, ofwel:
   $$M = \frac{E}{\rho} \quad \text{maximaliseren!}$$

### Samenvatting Standaardindices:
* Trekstaaf (stijfheid): $M = \frac{E}{\rho}$
* Buigbalk (stijfheid): $M = \frac{E^{1/2}}{\rho}$
* Buigplaat (stijfheid): $M = \frac{E^{1/3}}{\rho}$
* Buigbalk (sterkte): $M = \frac{\sigma_y^{2/3}}{\rho}$

---

> [!summary] Hoofdstuksamenvatting
> De Ashby-methodiek scheidt geometrische en functionele randvoorwaarden van materiaaleigenschappen, resulterend in wiskundig afgeleide selectie-indices $M$.
