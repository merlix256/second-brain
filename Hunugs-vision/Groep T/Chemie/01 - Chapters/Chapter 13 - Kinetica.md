---
title: "Hoofdstuk 13: Chemische Kinetica"
tags:
  - study-unit
  - chemie
  - kinetica
  - reactiesnelheid
  - arrhenius
  - mechanismen
course: "Chemie (T1ACH1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: high
---

# ⏱️ Hoofdstuk 13: Chemische Kinetica

> [!abstract] Kernconcept
> Terwijl thermodynamica bepaalt *of* een reactie spontaan kán verlopen ($\Delta G < 0$), bestudeert de **chemische kinetica** *hoe snel* de omzetting verloopt en via welke opeenvolging van moleculaire elementaire stappen (**het reactiemechanisme**).

---

## 1. Reactiesnelheid

Voor een algemene reactie:
$$aA + bB \longrightarrow cC + dD$$
is de reactiesnelheid ($v$) gedefinieerd als de concentratieverandering per tijdseenheid genormaliseerd door stoichiometrische coëfficiënten:
$$v = -\frac{1}{a}\frac{d[A]}{dt} = -\frac{1}{b}\frac{d[B]}{dt} = +\frac{1}{c}\frac{d[C]}{dt} = +\frac{1}{d}\frac{d[D]}{dt}$$

---

## 2. Snelheidswetten en Reactie-orde

De **experimentele snelheidswet** drukt de snelheid uit in functie van reagensconcentraties:
$$v = k [A]^m [B]^n$$
waarbij:
- $k$ de reactiesnelheidsconstante is.
- $m, n$ de **partiële reactie-ordes** zijn (moeten **experimenteel** bepaald worden en zijn NIET noodzakelijk gelijk aan stoichiometrische coëfficiënten $a, b$!).
- $m + n$ de **totale reactie-orde** is.

### 2.1 Overzicht Geïntegreerde Snelheidswetten

| Orde | Differentiële wet | Geïntegreerde snelheidswet | Lineaire plot voor rechte | Halfwaardetijd ($t_{1/2}$) | Eenheid van $k$ |
| :---: | :--- | :--- | :---: | :---: | :---: |
| **0** | $v = k$ | $[A]_t = -kt + [A]_0$ | $[A]$ vs $t$ | $t_{1/2} = \frac{[A]_0}{2k}$ | $\text{mol}/(\text{L}\cdot\text{s})$ |
| **1** | $v = k[A]$ | $\ln[A]_t = -kt + \ln[A]_0$ | $\ln[A]$ vs $t$ | $t_{1/2} = \frac{\ln 2}{k} = \frac{0.693}{k}$ | $\text{s}^{-1}$ |
| **2** | $v = k[A]^2$ | $\frac{1}{[A]_t} = kt + \frac{1}{[A]_0}$ | $\frac{1}{[A]}$ vs $t$ | $t_{1/2} = \frac{1}{k[A]_0}$ | $\text{L}/(\text{mol}\cdot\text{s})$ |

> [!important] Eerste Orde Halfwaardetijd
> Voor een eerste-orde proces is de halfwaardetijd $t_{1/2} = \frac{0.693}{k}$ **volledig onafhankelijk van de beginconcentratie** $[A]_0$ (fundamenteel principe achter radioactief verval).

---

## 3. Temperatuurinvloed en Arrheniusvergelijking

### 3.1 Botsingstheorie
Reactiesnelheid hangt af van drie voorwaarden:
1. Moleculen moeten botsen.
2. Botsingsenergie $\ge$ de **activeringsenergie ($E_a$)**.
3. Juiste ruimtelijke oriëntatie (sterische factor $p$).

### 3.2 De Arrheniusvergelijking
$$k = A \cdot e^{-\frac{E_a}{RT}}$$
In lineaire vorm:
$$\ln k = -\frac{E_a}{R} \cdot \frac{1}{T} + \ln A$$
Twee-temperatuurformule:
$$\ln\left(\frac{k_2}{k_1}\right) = -\frac{E_a}{R} \left( \frac{1}{T_2} - \frac{1}{T_1} \right)$$

![[Arrhenius_Energy_Profile.png]]

---

## 4. Reactiemechanismen en Katalyse

### 4.1 Elementaire Stappen en Moleculariteit
Complexe reacties verlopen in discrete micro-stappen. Voor een **elementaire stap** geldt dat de partiële orde wél exact overeenkomt met de moleculaire coëfficiënt:
- Unimoleculair: $A \rightarrow \text{producten} \implies v = k[A]$
- Bimoleculair: $A + B \rightarrow \text{producten} \implies v = k[A][B]$

### 4.2 Snelheidsbepalende Stap (Rate Determining Step - RDS)
De traagste stap in een reactiemechanisme dicteert de totale macroscopische reactiesnelheid.
- *Tussenproduct (Intermediair)*: Gevormd in stap 1, verbruikt in stap 2 (verschijnt niet in de nettovergelijking).
- *Katalysator*: Aanwezig vóór reactie, verlaagt de activeringsenergie ($E_a$), wordt geregenereerd aan het einde van de cyclus.

---

## 📝 Samenvatting
1. Reactie-orde kan alleen experimenteel bepaald worden (methode van initiële snelheden).
2. Geïntegreerde wetten: 0e orde $[A]$, 1e orde $\ln[A]$, 2e orde $1/[A]$ vs tijd.
3. Arrhenius koppelt $k$ aan temperatuur: $\ln(k_2/k_1) = -\frac{E_a}{R}(1/T_2 - 1/T_1)$.
4. De snelheidsbepalende stap (RDS) bepaalt de kinetische vorm van de experimentele snelheidswet.
