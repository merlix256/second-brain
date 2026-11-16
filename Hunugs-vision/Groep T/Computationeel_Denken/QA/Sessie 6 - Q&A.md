---
course: "Computationeel Denken (T1ACD1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.0
priority: medium
tags:
  - study-unit
---

# Sessie 6 - Q&A (Active Recall)

> **Verwijzingen:** [[Sessie 6 - Lijsten]] | [[Oefensessie 6]] | [[Index]]

---

### Vraag 1: Wat is het effect van `lst[::-1]` op een lijst en wijzigt dit de originele lijst in-place?
**Antwoord:**
`lst[::-1]` creëert en retourneert een **nieuwe lijst** met alle elementen in omgekeerde volgorde via slicing met een stapgrootte van $-1$.
Het wijzigt de originele lijst **niet** in-place (in tegenstelling tot de methode `lst.reverse()`, die `None` retourneert en de lijst ter plekke muteert).
*Theorielink:* [[Sessie 6 - Lijsten#2.1 List Slicing: lst[start:stop:step]]]

---

### Vraag 2: Wat is 'Aliasing' bij lijsten en hoe kan het voorkomen worden?
**Antwoord:**
Aliasing ontstaat wanneer twee variabelen naar hetzelfde object in het heap-geheugen verwijzen na een toewijzing:
```python
a = [1, 2, 3]
b = a # b en a verwijzen naar exact dezelfde geheugenlocatie
```
Een wijziging via `b.append(4)` beïnvloedt automatisch ook `a`.
Preventie gebeurt door een ondiepe kopie (*shallow copy*) te forceren:
`b = a.copy()` of `b = a[:]` of `b = list(a)`.
*Theorielink:* [[Sessie 6 - Lijsten#4. Geheugenreferenties: De Aliasing Valkuil]]

---

### Vraag 3: Wat is het verschil in tijdscomplexiteit tussen `lst.append()` en `lst.insert(0, x)`?
**Antwoord:**
- `lst.append(x)` heeft gemiddeld een constante tijdscomplexiteit $\mathcal{O}(1)$, omdat het element direct aan het gereserveerde einde van de lijst-array wordt toegevoegd.
- `lst.insert(0, x)` heeft een lineaire tijdscomplexiteit $\mathcal{O}(n)$, omdat alle $n$ bestaande elementen in het geheugen één positie naar rechts moeten worden opgeschoven om vooraan plaats te maken.
*Theorielink:* [[Sessie 6 - Lijsten#3.1 In-Place Wijzigingen]]