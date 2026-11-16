---
title: "Hoofdstuk 14: Chemisch Evenwicht"
tags:
  - study-unit
  - chemie
  - evenwicht
  - le-chatelier
  - evenwichtsconstante
course: "Chemie (T1ACH1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: high
---

# ⚖️ Hoofdstuk 14: Chemisch Evenwicht

> [!abstract] Kernconcept
> Een chemische reactie bereikt een **dynamisch evenwicht** wanneer de snelheid van de heengaande reactie exact gelijk is aan de snelheid van de teruggaande reactie ($v_{\text{heen}} = v_{\text{terug}}$). De macroscopische concentraties blijven constant, hoewel de microscopische reacties continu doorgaan.

---

## 1. De Evenwichtsconstante ($K_c$ en $K_p$)

Voor een algemene omkeerbare reactie:
$$aA + bB \rightleftharpoons cC + dD$$

### 1.1 Concentratieconstante ($K_c$)
$$K_c = \frac{[C]^c [D]^d}{[A]^a [B]^b}$$
> [!warning] Belangrijke Conventie
> Zuivere vaste stoffen ($(s)$) en zuivere vloeistoffen ($(l)$) hebben een activiteit van 1 en worden **nooit** opgenomen in de evenwichtsuitdrukking!

### 1.2 Drukconstante ($K_p$) voor Gasevenwichten
$$K_p = \frac{P_C^c \cdot P_D^d}{P_A^a \cdot P_B^b}$$
Koppeling tussen $K_p$ en $K_c$ via de ideale gaswet ($P = \frac{n}{V}RT = CRT$):
$$K_p = K_c (RT)^{\Delta n_{\text{gas}}}$$
waarbij $\Delta n_{\text{gas}} = (c + d) - (a + b)$ het verschil in gasmollen is.

---

## 2. Het Reactiequotiënt ($Q$)

Het **reactiequotiënt ($Q$)** heeft dezelfde mathematische vorm als $K$, maar berekend met concentraties op een willekeurig niet-evenwichtstijdstip:
- $Q < K$: Te veel reagens, reactie verschuift **naar rechts (producten)**.
- $Q = K$: Systeem bevindt zich in **dynamisch evenwicht**.
- $Q > K$: Te veel product, reactie verschuift **naar links (reagentia)**.

---

## 3. Berekeningen met ICE-tabellen (Begin, Verandering, Evenwicht)

Voor kwantitatieve evenwichtsberekeningen:
1. **Initial**: Beginconcentraties.
2. **Change**: Veranderingen uitgedrukt in $x$, gekoppeld aan stoichiometrische verhoudingen.
3. **Equilibrium**: Som van Initial + Change.
4. Invullen in $K_c$ en oplossen naar $x$ (evt. met de $5\%$-benadering indien $K$ zeer klein is).

---

## 4. Het Principe van Le Châtelier

> [!quote] Principe van Le Châtelier
> Wanneer een systeem in dynamisch evenwicht wordt onderworpen aan een externe verstoring (concentratie, druk, temperatuur), zal het systeem zodanig verschuiven dat het effect van die verstoring gedeeltelijk wordt tegengewerkt.

| Verstoring | Resulterende Verschuiving | Verandert $K$? |
| :--- | :--- | :---: |
| **Toevoegen van reagens** | Verschuift naar **rechts** | Nee |
| **Verwijderen van product** | Verschuift naar **rechts** | Nee |
| **Volume verkleinen (druk verhogen)** | Verschuift naar kant met **minste gasmollen** | Nee |
| **Volume vergroten (druk verlagen)** | Verschuift naar kant met **meeste gasmollen** | Nee |
| **Temperatuur verhogen (Exotherm $\Delta H < 0$)** | Verschuift naar **links** | **Ja ($K$ daalt)** |
| **Temperatuur verhogen (Endotherm $\Delta H > 0$)**| Verschuift naar **rechts** | **Ja ($K$ stijgt)** |
| **Toevoegen katalysator** | Geen verschuiving (versnelt enkel evenwichtsinstelling)| Nee |

![[Le_Chatelier_Disturbances.png]]

---

## 📝 Samenvatting
1. Dynamisch evenwicht treedt op als $v_{\text{heen}} = v_{\text{terug}}$.
2. $K_p = K_c(RT)^{\Delta n}$; zuivere vaste stoffen en vloeistoffen vallen weg uit $K$.
3. Vergelijk $Q$ met $K$ om de spontane reactierichting te bepalen.
4. Le Châtelier voorspelt verschuivingen; **alleen temperatuurveranderingen wijzigen de numerieke waarde van $K$**.
