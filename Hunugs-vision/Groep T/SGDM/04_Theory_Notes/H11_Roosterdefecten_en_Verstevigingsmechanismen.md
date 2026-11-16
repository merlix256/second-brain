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

# 🔬 H11: Roosterdefecten en Verstevigingsmechanismen
#theorie #defecten #dislocaties #schmid #hall-petch #H11

[[00_Overview_Dashboard]] | [[01_Formularium_Master#2-plasticiteit-vervorming--hardheid]] | [[05_Oefenzittingen/Sessie_02_Sterkte_Plasticiteit_Hardheid]]

---

## 1. Classificatie van Roosterdefecten
* **0D (Puntdefecten)**: Vacatures (onbezette roosterplaatsen), interstitiëlen (kleine atomen in holtes), substitutionele vreemde atomen.
* **1D (Lijndefecten / Dislocaties)**:
  * **Randdislocatie**: Extra half atoomvlak in het rooster; Burgersvector $\vec{b} \perp$ dislocatielijn $\vec{l}$.
  * **Schroefdislocatie**: Spiraalvormige verschuiving; Burgersvector $\vec{b} \parallel$ dislocatielijn $\vec{l}$.
* **2D (Vlakdefecten)**: Korrelgrenzen, tweelinggrenzen, fasegrenzen.
* **3D (Volumedefecten)**: Poriën, scheuren, niet-metallische insluitsels.

```
 Randdislocatie (Lijndefect)
     O   O   O   O   O
     |   |   |   |   |
     O   O   O   O   O
     |   |   |   |   |
     O   O | O | O   O    <-- Extra halfvlak
         |   |
     O   O   O   O   O
     |   |   |   |   |
     O   O   O   O   O
```

---

## 2. Dislocatiebeweging & De Wet van Schmid
Zonder dislocaties zou het gelijktijdig afschuiven van alle atoombindingen een theoretische spanning vereisen van $\tau_{th} \approx \frac{G}{6} \approx 1000 - 10\,000\text{ MPa}$.
Dankzij dislocaties verschuift telkens slechts één atoomrij tegelijk (analogie: **de rimpel in het tapijt**), waardoor werkelijke vloeispanningen 100 tot 1000 keer lager liggen!

### Schmid-factor & CRSS:
$$\tau_{\text{res}} = \sigma \cos\phi \cos\lambda = \sigma \cdot m$$
Vloei treedt op wanneer $\tau_{\text{res}} = \tau_{\text{CRSS}}$ (Critical Resolved Shear Stress).
* $\tau_{\text{res}}$ is maximaal wanneer $\phi = \lambda = 45^\circ \implies m = 0.5 \implies \sigma_y = 2 \tau_{\text{CRSS}}$.

---

## 3. De 4 Fundamentele Verstevigingsmechanismen
Elk verstevigingsmechanisme berust op hetzelfde principe: **het belemmeren van de beweging van dislocaties**!

1. **Oplossingsversteviging (Solid Solution Hardening)**:
   Vreemde atomen creëren lokale druk- of trekspanningsvelden in het rooster die interageren met het spanningsveld van dislocaties.
2. **Precipitatieversteviging / Deeltjesharding**:
   Dislocaties worden gedwongen om door harde secundaire deeltjes heen te snijden of eromheen te buigen (Orowan-lussen).
3. **Korrelgrensversteviging (Hall-Petch relatie)**:
   Dislocaties kunnen niet zomaar de willekeurige oriëntatiesprong over een korrelgrens maken en stapelen zich op ("pile-up"):
   $$\sigma_y = \sigma_0 + \frac{k_y}{\sqrt{d}}$$
   *Uniek voordeel*: Korrelverfijning is het **enige** mechanisme dat zowel de **sterkte als de taaiheid** verhoogt!
4. **Vervormingsversteviging (Strain Hardening / Cold Work)**:
   Door plastische deformatie stijgt de dislocatiedichtheid $\rho$ explosief van $10^7\text{ cm}^{-2}$ naar $10^{12}\text{ cm}^{-2}$. Dislocaties verstrengelen tot onbeweeglijke netwerken ("dislocatiewouden").

---

> [!summary] Hoofdstuksamenvatting
> Dislocaties maken metalen ductiel bij lage spanningen. Door het inbrengen van roosterobstakels (opgeloste atomen, precipitaten, korrelgrenzen of andere dislocaties) wordt de vloeigrens verhoogd ten koste van ductiliteit.
