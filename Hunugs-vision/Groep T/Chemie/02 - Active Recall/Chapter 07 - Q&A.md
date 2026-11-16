---
title: "Active Recall: Hoofdstuk 7 - Elektronenstructuur van Atomen"
tags:
  - study-unit
  - active-recall
  - flashcards
  - kwantumchemie
course: "Chemie (T1ACH1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.0
priority: medium
---

# 🧠 Active Recall Deck: Hoofdstuk 7 - Elektronenstructuur van Atomen

---

### Vraag 1: Golflengte en Fotonenergie
**Vraag**: Een laser zendt licht uit met een golflengte van $\lambda = 488\text{ nm}$. 
1. Bereken de energie van één enkel foton in Joule en in elektronvolt ($1\text{ eV} = 1.602 \times 10^{-19}\text{ J}$).
2. Hoeveel fotonen per seconde zendt een laserpuls van $15\text{ mJ}$ uit?

> [!success]- Toon Antwoord & Uitwerking
> - **Theoretische koppeling**: [[Chapter 07 - Elektronenstructuur van atomen#1.2 Planck's Kwantumtheorie en Foto-elektrisch Effect]]
> - **Berekening 1**:
>   $$E = \frac{h \cdot c}{\lambda} = \frac{(6.626 \times 10^{-34}\text{ J}\cdot\text{s})(2.998 \times 10^8\text{ m/s})}{488 \times 10^{-9}\text{ m}} = 4.071 \times 10^{-19}\text{ J}$$
>   $$E_{\text{eV}} = \frac{4.071 \times 10^{-19}\text{ J}}{1.602 \times 10^{-19}\text{ J/eV}} = \mathbf{2.54\text{ eV}}$$
> - **Berekening 2**:
>   $$N_{\text{fotonen}} = \frac{E_{\text{puls}}}{E_{\text{foton}}} = \frac{15 \times 10^{-3}\text{ J}}{4.071 \times 10^{-19}\text{ J/foton}} = \mathbf{3.68 \times 10^{16}\text{ fotonen}}$$

---

### Vraag 2: Kwantumgetallen Valideren
**Vraag**: Bepaal welke van de volgende combinaties van kwantumgetallen ($n, l, m_l, m_s$) fysisch toegestaan zijn en motiveer:
A) $(3, 2, -1, +\frac{1}{2})$
B) $(2, 2, 0, -\frac{1}{2})$
C) $(4, 0, 0, +1)$
D) $(1, 0, 0, -\frac{1}{2})$

> [!success]- Toon Antwoord & Uitwerking
> - **Theoretische koppeling**: [[Chapter 07 - Elektronenstructuur van atomen#3. Quantumgetallen en Atomaire Orbitalen]]
> - **Analyse**:
>   - **A is Geldig**: $n=3$, $l=2$ ($d$-subschil, $l < n$), $m_l = -1$ (tussen $-2$ en $+2$), $m_s = +1/2$.
>   - **B is Ongeldig**: $n=2, l=2$. Het nevenkwantumgetal kan maximaal $n-1$ zijn; voor $n=2$ kan $l$ enkel 0 of 1 zijn.
>   - **C is Ongeldig**: $m_s$ kan uitsluitend $+\frac{1}{2}$ of $-\frac{1}{2}$ bedragen, nooit $+1$.
>   - **D is Geldig**: Beschrijft een elektron in een $1s$-orbitaal met spin omlaag.

---

### Vraag 3: Afwijkende Elektronenconfiguraties
**Vraag**: Schrijf de volledige elektronenconfiguratie van Chroom (Cr, $Z=24$) en Koper (Cu, $Z=29$) in de grondtoestand en verklaar waarom ze afwijken van het standaard Aufbau-schema.

> [!success]- Toon Antwoord & Uitwerking
> - **Theoretische koppeling**: [[Chapter 07 - Elektronenstructuur van atomen#4.2 Uitzonderingen bij Overgangsmetalen]]
> - **Configuraties**:
>   - $\text{Cr}: [\text{Ar}] 4s^1 3d^5$ (in plaats van $[\text{Ar}] 4s^2 3d^4$)
>   - $\text{Cu}: [\text{Ar}] 4s^1 3d^{10}$ (in plaats van $[\text{Ar}] 4s^2 3d^9$)
> - **Verklaring**:
>   Halve bezetting ($d^5$) en volledige bezetting ($d^{10}$) van de $3d$-subschil bieden uitzonderlijke symmetrische stabilisatie en minimaliseren de interelektronische afstotingsenergie vergeleken met het plaatsen van twee gepaarde elektronen in het $4s$-orbitaal.
