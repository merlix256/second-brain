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

# 🔬 H15: Artificiële Materialen en Composieten
#theorie #composieten #vezelversterking #voigt-reuss #H15

[[00_Overview_Dashboard]] | [[01_Formularium_Master#5-composieten-artificiële-materialen]] | [[05_Oefenzittingen/Sessie_04_Fasediagrammen_en_Composieten]]

---

## 1. Definitie & Doel van Composieten
Een artificieel materiaal (composiet) is een macroscopisch heterogeen mengsel van twee of meer fysisch onderscheiden fasen:
1. **Matrixfase**: Continu (polymeer, metaal of keramiek); omsluit de versterking, beschermt tegen omgeving en draagt schuifspanningen over.
2. **Versterkingsfase**: Discontinu (vezels, partikels, whiskers); draagt het leeuwendeel van de mechanische belasting.

---

## 2. Micromechanica van Unidirectionele Vezelcomposieten

### A. Longitudinale Belasting (Isostrain conditie)
Vezels en matrix rekken evenveel uit ($\epsilon_c = \epsilon_f = \epsilon_m$):
$$E_{c,l} = V_f E_f + V_m E_m = V_f E_f + (1 - V_f) E_m$$
*(Voigt bovengrens — de stijve vezels dragen vrijwel de gehele belasting).*

### B. Transversale Belasting (Isostress conditie)
Vezels en matrix ervaren dezelfde spanning ($\sigma_c = \sigma_f = \sigma_m$):
$$\frac{1}{E_{c,t}} = \frac{V_f}{E_f} + \frac{V_m}{E_m} \implies E_{c,t} = \frac{E_f E_m}{V_f E_m + (1 - V_f) E_f}$$
*(Reuss ondergrens — de zachte matrix vervormt dominant).*

---

## 3. Kritische Vezellengte ($l_c$)
Om de volle treksterkte $\sigma_f^*$ van een vezel te benutten, moet de schuifspanning $\tau_c$ aan de matrix-vezel interface voldoende lengte hebben om de trekspanning op te bouwen:
$$l_c = \frac{\sigma_f^* \cdot d}{2 \tau_c}$$
* Als $l \gg l_c$: continue vezel (optimale versterking).
* Als $l < l_c$: discontinue vezel (matrix vloeit vooraleer de vezel breekt).

---

> [!summary] Hoofdstuksamenvatting
> Composieten combineren de hoge stijfheid van vezels met de taaiheid van de matrix. Ze vertonen uitgesproken mechanische anisotropie volgens de Voigt/Reuss grenzen.
