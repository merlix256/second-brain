---
title: "Oefensessie 4: Elektronenstructuur van Atomen"
tags:
  - study-unit
  - oefensessie
  - spectroscopie
  - kwantumgetallen
  - trends
course: "Chemie (T1ACH1)"
unit_type: oefensessie
status: todo
completed: false
est_hours: 2.0
priority: high
---

# ⚛️ Oefensessie 4: Elektronenstructuur - Spectroscopie & Trends

> [!abstract] Focus van de Sessie
> Berekeningen rond de de Broglie golflengte, het Bohr-waterstofatoom, orbitalen en het rationaliseren van periodieke anomalieën in ionisatie-energie en effectieve kernlading.

---

## 📌 Oefeningen & Theoretische Verankering

### Oefening 4.1: Bohr Model en Rydberg Spectroscopie
**Vraagstuk**: 
Bereken de golflengte (in nm) en identificeer het spectrumgebied van de straling die geëmitteerd wordt wanneer een elektron in een waterstofatoom terugvalt van het $n=4$ energieniveau naar het $n=2$ niveau (Balmer-reeks). ($R_H = 2.179 \times 10^{-18}\text{ J}$, $h = 6.626 \times 10^{-34}\text{ J}\cdot\text{s}$, $c = 2.998 \times 10^8\text{ m/s}$).

> [!success]- Toon Uitwerking & Backlinks
> - **Koppeling met theorie**: [[Chapter 07 - Elektronenstructuur van atomen#2.1 Bohr-Atoommodel voor Waterstof]]
> - **Energieverschil**:
>   $$\Delta E = -R_H \left( \frac{1}{n_f^2} - \frac{1}{n_i^2} \right) = -2.179 \times 10^{-18} \left( \frac{1}{2^2} - \frac{1}{4^2} \right)$$
>   $$\Delta E = -2.179 \times 10^{-18} \left( \frac{1}{4} - \frac{1}{16} \right) = -2.179 \times 10^{-18} \times \frac{3}{16} = -4.086 \times 10^{-19}\text{ J}$$
> - **Foton-golflengte**:
>   $$E_{\text{foton}} = |\Delta E| = \frac{hc}{\lambda} \implies \lambda = \frac{hc}{|\Delta E|}$$
>   $$\lambda = \frac{(6.626 \times 10^{-34})(2.998 \times 10^8)}{4.086 \times 10^{-19}} = 4.861 \times 10^{-7}\text{ m} = \mathbf{486.1\text{ nm}}$$
>   *(Zichtbaar blauw-groen licht, $\text{H}_\beta$-lijn in de Balmer-reeks).*

---

### Oefening 4.2: Periodieke Trends & $Z_{\text{eff}}$
**Vraagstuk**: 
Verklaar waarom de tweede ionisatie-energie van kalium ($IE_2(\text{K}) = 3052\text{ kJ/mol}$) meer dan zes keer groter is dan de eerste ($IE_1(\text{K}) = 419\text{ kJ/mol}$), terwijl bij calcium de verhouding veel kleiner is ($IE_1 = 590\text{ kJ/mol}, IE_2 = 1145\text{ kJ/mol}$).

> [!success]- Toon Uitwerking & Backlinks
> - **Koppeling met theorie**: [[Chapter 08 - Periodieke tabel#1. Effectieve Kernlading (Zeff)]] en [[Chapter 08 - Periodieke tabel#2.2 Ionisatie-energie (IE)]]
> - **Elektronenconfiguraties**:
>   - Kalium: $\text{K} ([\text{Ar}] 4s^1) \xrightarrow{IE_1} \text{K}^+ ([\text{Ar}]) \xrightarrow{IE_2} \text{K}^{2+} ([\text{Ne}] 3s^2 3p^5)$
>   - Calcium: $\text{Ca} ([\text{Ar}] 4s^2) \xrightarrow{IE_1} \text{Ca}^+ ([\text{Ar}] 4s^1) \xrightarrow{IE_2} \text{Ca}^{2+} ([\text{Ar}])$
> - **Verklaring**:
>   Het tweede elektron van $\text{K}$ moet verwijderd worden uit een gesloten edelgasschil ($n=3$) die veel dichter bij de kern ligt en nauwelijks wordt afgeschermd ($Z_{\text{eff}}$ is gigantisch hoog). Bij $\text{Ca}$ zijn zowel het eerste als het tweede elektron afkomstig uit de buitenste $4s$-valentiebahn.
