---
title: "Hoofdstuk 7: Elektronenstructuur van Atomen"
tags:
  - study-unit
  - chemie
  - quantumchemie
  - orbitalen
  - spectroscopie
course: "Chemie (T1ACH1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: high
---

# ⚛️ Hoofdstuk 7: Elektronenstructuur van Atomen

> [!abstract] Kernconcept
> Om de chemische reactiviteit en binding van materie te begrijpen, moeten elektronen niet beschreven worden als klassieke deeltjes in banen, maar via **golfmechanica en kwantumtheorie**, waarbij waarschijnlijkheidsverdelingen (orbitalen) centraal staan.

---

## 1. Elektromagnetische Straling en Kwantisering

### 1.1 Golfkarakter van Licht
Licht propageert als een transversale elektromagnetische golf met constante lichtsnelheid $c = 2.998 \times 10^8\text{ m/s}$:
$$c = \lambda \cdot \nu$$
waarbij $\lambda$ de golflengte (m) is en $\nu$ de frequentie (Hz of $\text{s}^{-1}$).

### 1.2 Planck's Kwantumtheorie en Foto-elektrisch Effect
- **Max Planck (1900)**: Energie-uitwisseling tussen materie en straling gebeurt in discrete pakketjes (**kwanta**):
  $$E = h \cdot \nu = \frac{h \cdot c}{\lambda}$$
  waarbij $h = 6.626 \times 10^{-34}\text{ J}\cdot\text{s}$ (constante van Planck).
- **Albert Einstein (1905)**: Licht bestaat uit deeltjes genaamd **fotonen**. Bij het foto-elektrisch effect worden elektronen pas geëjecteerd als de fotonenergie groter is dan de uittreedarbeid ($W$ of $\Phi$):
  $$h\nu = W + E_{k,\text{max}} = h\nu_0 + \frac{1}{2}m_e v^2$$

![[Photoelectric_Effect_Diagram.png]]

---

## 2. Het Bohr-model en Dualiteit

### 2.1 Bohr-Atoommodel voor Waterstof
Niels Bohr postuleerde dat het elektron in een waterstofatoom enkel in gekwantiseerde cirkelbanen met discreet baanimpulsmoment kan bewegen:
$$E_n = -R_H \left( \frac{1}{n^2} \right)$$
waarbij $R_H = 2.179 \times 10^{-18}\text{ J}$ (Rydberg-constante) en $n \in \{1, 2, 3, \dots\}$.
Bij een elektronovergang tussen niveau $n_i$ en $n_f$:
$$\Delta E = h\nu = -R_H \left( \frac{1}{n_f^2} - \frac{1}{n_i^2} \right)$$
- Emissielijnen: Lyman-reeks ($n_f = 1$, UV), Balmer-reeks ($n_f = 2$, zichtbaar), Paschen-reeks ($n_f = 3$, IR).

### 2.2 Golf-deeltje Dualiteit (de Broglie)
Louis de Broglie (1924) stelde dat elk bewegend deeltje met massa $m$ en snelheid $v$ (impuls $p = mv$) een karakteristieke golflengte bezit:
$$\lambda = \frac{h}{p} = \frac{h}{m \cdot v}$$

### 2.3 Heisenberg Onzekerheidsrelatie
Het is fundamenteel onmogelijk om tegelijkertijd de exacte positie ($x$) en de exacte impuls ($p_x$) van een subatomair deeltje exact te bepalen:
$$\Delta x \cdot \Delta p_x \ge \frac{h}{4\pi}$$

---

## 3. Quantumgetallen en Atomaire Orbitalen

De toestand van een elektron in de golfvergelijking van Schrödinger ($\hat{H}\psi = E\psi$) wordt uniek beschreven door vier **kwantumgetallen**:

| Kwantumgetal | Symbool | Toegestane Waarden | Fysische Betekenis |
| :--- | :---: | :--- | :--- |
| **Hoofdkwantumgetal** | $n$ | $1, 2, 3, 4, \dots$ | Schil, hoofdniveau, gemiddelde afstand tot kern |
| **Nevenkwantumgetal** | $l$ | $0, 1, 2, \dots, (n-1)$ | Subschil, vorm van het orbitaal ($s, p, d, f$) |
| **Magnetisch kwantumgetal** | $m_l$ | $-l, \dots, 0, \dots, +l$ | Ruimtelijke oriëntatie van het orbitaal |
| **Spinkwantumgetal** | $m_s$ | $+\frac{1}{2}, -\frac{1}{2}$ | Intrinsiek spin-impulsmoment van het elektron |

- $l = 0 \implies s$-orbitaal (sferisch symmetrisch, 1 per schil).
- $l = 1 \implies p$-orbitaal (haltervormig met knoopvlak, 3 per schil: $p_x, p_y, p_z$).
- $l = 2 \implies d$-orbitaal (klaverbladvormig, 5 per schil).
- $l = 3 \implies f$-orbitaal (7 per schil).

![[Atomic_Orbitals_Shapes.png]]

---

## 4. Elektronenconfiguraties in Meerelektronatomen

### 4.1 De Drie Fundamentele Regels
1. **Aufbau-principe**: Elektronen bezetten eerst de laagst beschikbare energieniveaus ($1s < 2s < 2p < 3s < 3p < 4s < 3d < 4p < \dots$).
2. **Pauli-uitsluitingsprincipe**: Twee elektronen in een atoom kunnen nooit dezelfde set van 4 kwantumgetallen hebben. Maximaal 2 elektronen per orbitaal met tegengestelde spin (antiparallel: $\uparrow\downarrow$).
3. **Regel van Hund**: Bij ontaarde orbitalen (gelijke energie, bijv. $2p_x, 2p_y, 2p_z$) bezetten elektronen deze zoveel mogelijk met parallelle spin om interelektronische afstoting te minimaliseren.

### 4.2 Uitzonderingen bij Overgangsmetalen
Extra stabiliteit van halfgevulde ($d^5$) of geheel gevulde ($d^{10}$) subschillen:
- **Chroom (Cr, $Z=24$)**: $[\text{Ar}] 4s^1 3d^5$ (i.p.v. $[\text{Ar}] 4s^2 3d^4$).
- **Koper (Cu, $Z=29$)**: $[\text{Ar}] 4s^1 3d^{10}$ (i.p.v. $[\text{Ar}] 4s^2 3d^9$).

---

## 📝 Samenvatting
1. Licht gedraagt zich als golven ($c = \lambda\nu$) en als fotonen ($E = h\nu$).
2. Materie vertoont golf-deeltje dualiteit: $\lambda = \frac{h}{mv}$.
3. Elektronen bevinden zich in orbitalen gedefinieerd door 4 kwantumgetallen: $n, l, m_l, m_s$.
4. De elektronenverdeling volgt het Aufbau-principe, Pauli-uitsluitingsprincipe en de regel van Hund.
