---
course: "Wiskundige basistechnieken (T1AWB1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: high
tags:
  - study-unit
---

# Hoofdstuk 5: Vectorruimten en Inproductruimten

> [!abstract] Context
> Dit hoofdstuk abstraheert het concept vector tot willekeurige verzamelingen die voldoen aan de vectorruimte-axioma's (functies, veeltermen, matrices). We behandelen lineaire combinaties, deelruimten en inproductruimten.
> **Parent MOC:** [[Index]] | **Q&A:** [[Q&A - LinAlg Ch 05 Vectorruimten]] | **Oefeningen:** [[Oefensessie 10 - Vectorruimten I (Lineaire Combinaties en Deelruimten)]], [[Oefensessie 11 - Inproductruimten]]

---

## 1. Axioma's van een Reële Vectorruimte $(V, +, \cdot, \mathbb{R})$
Voor alle $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V$ en $k, l \in \mathbb{R}$:
1. **Optelling:**
   - Inwendig en overal gedefinieerd: $\mathbf{u} + \mathbf{v} \in V$
   - Associatief: $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$
   - Nulelement: $\exists \mathbf{0} \in V: \mathbf{u} + \mathbf{0} = \mathbf{u}$
   - Tegengesteld element: $\exists -\mathbf{u} \in V: \mathbf{u} + (-\mathbf{u}) = \mathbf{0}$
   - Commutatief: $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$
2. **Scalaire Vermenigvuldiging:**
   - Inwendig: $k\mathbf{u} \in V$
   - Distributief t.o.v. vectoroptelling: $k(\mathbf{u} + \mathbf{v}) = k\mathbf{u} + k\mathbf{v}$
   - Distributief t.o.v. scalaire optelling: $(k + l)\mathbf{u} = k\mathbf{u} + l\mathbf{u}$
   - Associatief: $k(l\mathbf{u}) = (kl)\mathbf{u}$
   - Eenheidselement: $1\mathbf{u} = \mathbf{u}$

---

## 2. Deelruimten
Een niet-lege deelverzameling $W \subseteq V$ is een deelruimte van $V$ ($W \le V$) $\iff$:
1. $\mathbf{0} \in W$.
2. $\forall \mathbf{u}, \mathbf{v} \in W: \mathbf{u} + \mathbf{v} \in W$ (gesloten onder optelling).
3. $\forall \mathbf{u} \in W, \forall k \in \mathbb{R}: k\mathbf{u} \in W$ (gesloten onder scalaire vermenigvuldiging).
Of compact in één voorwaarde: $\forall \mathbf{u}, \mathbf{v} \in W, \forall k, l \in \mathbb{R}: k\mathbf{u} + l\mathbf{v} \in W$.

---

## 3. Voortbrengendheid en Lineaire Combinaties
- Een vector $\mathbf{v}$ is een lineaire combinatie van $\{\mathbf{u}_1, \dots, \mathbf{u}_p\}$ als:
  $$\mathbf{v} = c_1 \mathbf{u}_1 + \dots + c_p \mathbf{u}_p$$
- De verzameling van alle lineaire combinaties heet het opspansel (lineair omhulsel):
  $$\text{span}(S) = L(S) = \{c_1 \mathbf{u}_1 + \dots + c_p \mathbf{u}_p \mid c_i \in \mathbb{R}\}$$
  $L(S)$ is altijd de kleinste deelruimte van $V$ die $S$ omvat.

---

## 4. Inproductruimten
Een reëel inproduct $\langle \mathbf{u}, \mathbf{v} \rangle$ op $V$ voldoet aan:
1. Positief definiet: $\langle \mathbf{u}, \mathbf{u} \rangle \ge 0$ en $\langle \mathbf{u}, \mathbf{u} \rangle = 0 \iff \mathbf{u} = \mathbf{0}$.
2. Symmetrisch: $\langle \mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{v}, \mathbf{u} \rangle$.
3. Bilineair: $\langle k\mathbf{u} + l\mathbf{v}, \mathbf{w} \rangle = k\langle \mathbf{u}, \mathbf{w} \rangle + l\langle \mathbf{v}, \mathbf{w} \rangle$.
- Geïnduceerde norm: $\|\mathbf{u}\| = \sqrt{\langle \mathbf{u}, \mathbf{u} \rangle}$.
- Ongelijkheid van Cauchy-Schwarz: $|\langle \mathbf{u}, \mathbf{v} \rangle| \le \|\mathbf{u}\| \|\mathbf{v}\|$.

---

> [!summary] Kernsamenvatting
> - Vectorruimten vormen het abstracte kader voor meetkunde in oneindige of hogere dimensies.
> - Een deelruimte moet steeds de nulvector bevatten en behouden blijven onder lineaire combinaties.
> - Een inproduct voorziet een vectorruimte van meetkunde (lengte, orthogonaliteit en afstanden).
