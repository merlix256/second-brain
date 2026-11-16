---
course: "Dynamica en energie (T1ADE1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: high
tags:
  - study-unit
---

# 📖 Hoofdstuk 3: Afhankelijke en Relatieve Beweging

> [!abstract] Overzicht & Leerdoelen
> - **Leerdoel:** Het systematisch analyseren van gekoppelde mechanismen (zoals katrolsystemen met constante kabellengtes) en het toepassen van translerende referentiestelsels voor relatieve snelheids- en versnellingsvectoren.
> - **Handboek:** Hibbeler Chapter 12 (§12.9, §12.10).
> - **Master Formularium:** [[Formularium#1. Kinematica van een Puntmassa (Rectilineair & Curvilineair)]].
> - **Actieve Herroeping:** [[Chapter 3 - Q&A]].

---

## 1. Katrolsystemen en Kinematische Koppelingen

In mechanische takelsystemen zijn de posities van meerdere lichamen aan elkaar gekoppeld via onrekbare kabels die over al dan niet bewegende katrollen lopen.

![[Slide_Katrol_Stappenplan_Datum.png]]
*(Placeholder: Katrolsysteem met vaste referentielijn (datum), positiecoördinaten $s_A$ en $s_B$ en kabelsegmenten)*

### Stappenplan voor Afhankelijke Beweging (Katrollen):
1. **Bepaal een vast referentiepunt (Datum):** Kies een vaste, niet-bewegende horizontale of verticale referentielijn.
2. **Definieer positiecoördinaten:** Ken aan elk bewegend lichaam of elke bewegende katrolas een positiecoördinaat $s_i$ toe, gemeten vanaf de datum parallel aan de bewegingsas.
3. **Stel de lengtevergelijking op:** Druk de totale lengte van de kabel $L$ uit als som van de variabele segmenten (segmenten over katrolschijven zijn constant en worden gegroepeerd in $C$):
   $$L = \sum c_i s_i + C = \text{constant}$$
4. **Differentieer 1e maal naar de tijd (Snelheden):**
   $$\frac{dL}{dt} = 0 \implies \sum c_i \dot{s}_i = 0 \implies \sum c_i v_i = 0$$
5. **Differentieer 2e maal naar de tijd (Versnellingen):**
   $$\frac{d^2L}{dt^2} = 0 \implies \sum c_i \ddot{s}_i = 0 \implies \sum c_i a_i = 0$$

> [!warning] Tekenconventie
> Positieve waarden voor $s_i$, $v_i$ en $a_i$ wijzen altijd in de richting **weg van de gekozen datum**. Als een berekende snelheid negatief is, beweegt het lichaam naar de datum toe.

---

## 2. Relatieve Beweging (Translerend Referentiekader)

Wanneer we de beweging van een deeltje $B$ bestuderen ten opzichte van een bewegend deeltje $A$, koppelen we een translerend (niet-roterend) assenstelsel $(x', y', z')$ aan $A$:

![[Slide_Relatieve_Vectoren_A_B.png]]
*(Placeholder: Vectordiagram met absolute positievectoren $r_A, r_B$ en relatieve vector $r_{B/A}$)*

### 2.1 Positievectoren
$$\mathbf{r}_B = \mathbf{r}_A + \mathbf{r}_{B/A}$$
waarbij $\mathbf{r}_{B/A}$ de positie van $B$ is zoals waargenomen vanuit $A$.

### 2.2 Snelheidsvectoren
Differentiëren naar de tijd levert de vectoriële snelheidsrelatie:
$$\mathbf{v}_B = \mathbf{v}_A + \mathbf{v}_{B/A}$$
waarbij $\mathbf{v}_{B/A}$ de relatieve snelheid van $B$ ten opzichte van $A$ voorstelt.

### 2.3 Versnellingsvectoren
$$\mathbf{a}_B = \mathbf{a}_A + \mathbf{a}_{B/A}$$
Omdat het referentiestelsel enkel transleert (en niet roteert), hoeven er geen Coriolis-termen in rekening te worden gebracht.

---

## 📝 Samenvatting
- Bij kabel- en katrolsystemen vertaalt de eis van onrekbaarheid ($\Delta L = 0$) zich rechtstreeks in lineaire algebraïsche koppelingen tussen snelheden en versnellingen.
- Relatieve beweging laat toe complexe bewegingen op te splitsen in de absolute beweging van een referentiepunt plus de relatieve beweging ten opzichte van dat punt.
