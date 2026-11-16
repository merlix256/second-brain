---
course: "Computationeel Denken (T1ACD1)"
unit_type: theory
status: todo
completed: false
est_hours: 2.5
priority: medium
tags:
  - study-unit
---

# Sessie 6: Lijsten

> **Navigatie:** [[Index]] | [[Exercise Session Tracker]] | [[Sessie 6 - Q&A]] | [[Oefensessie 6]]

---

## 1. De `list` Datastructuur
Een lijst in Python is een geordende, veranderlijke (*mutable*) sequentie van elementen. Elementen mogen heterogeen zijn (verschillende datatypes in één lijst).

```python
getallen = [10, 20, 30, 40, 50]
```

---

## 2. Indexering en Slicing
Python hanteert zero-based indexering ($0, 1, \dots, n-1$) en negatieve indexering (vanaf het einde: $-1, -2, \dots, -n$).

![[Slide_Sessie6_List_Indexing.png]]
*Figuur 1: Positieve en negatieve indices van een lijst.*

### 2.1 List Slicing: `lst[start:stop:step]`
Haalt een sublijst op vanaf index `start` tot aan (exclusief) `stop` met stapgrootte `step`:
```python
letters = ['a', 'b', 'c', 'd', 'e', 'f']

sub1 = letters[1:4]      # ['b', 'c', 'd']
sub2 = letters[:3]       # ['a', 'b', 'c'] (vanaf begin)
sub3 = letters[::2]      # ['a', 'c', 'e'] (om de twee)
sub4 = letters[::-1]     # ['f', 'e', 'd', 'c', 'b', 'a'] (omkeren!)
```

---

## 3. Mutabiliteit en Veelgebruikte Lijstmethodes
In tegenstelling tot `str` en `tuple` zijn lijsten veranderlijk (*mutable*).

### 3.1 In-Place Wijzigingen
- `lst.append(x)`: Voegt element `x` toe aan het einde van de lijst (complexiteit $\mathcal{O}(1)$).
- `lst.extend(iterable)`: Voegt alle elementen uit een andere collectie toe.
- `lst.insert(index, x)`: Voegt element in op positie `index` (verschuift rest, $\mathcal{O}(n)$).
- `lst.pop(index)`: Verwijdert en retourneert het element op `index` (standaard laatste element).
- `lst.remove(x)`: Verwijdert de *eerste* voorkomst van waarde `x`.
- `len(lst)`: Geeft het aantal elementen terug ($\mathcal{O}(1)$).

---

## 4. Geheugenreferenties: De Aliasing Valkuil
Omdat lijsten objecten in het heap-geheugen zijn, kopieert een eenvoudige toewijzing `b = a` enkel het **geheugenadres (pointer)**, niet de data!

![[Slide_Sessie6_List_Memory_Pointers.png]]
*Figuur 2: Aliasing (twee variabelen wijzen naar hetzelfde lijst-object in het geheugen).*

```python
a = [1, 2, 3]
b = a          # ALIASING: b wijst naar exact hetzelfde object!
b.append(4)

print(a)       # [1, 2, 3, 4] -> a is mee veranderd!
```

> [!WARNING] Oplossing: Expliciet Kopiëren
> Om een onafhankelijke kopie te maken:
> ```python
> c = a.copy()   # of c = a[:] of c = list(a)
> c.append(99)   # a blijft ongewijzigd
> ```

---

## 5. Algoritmes op Lijsten: Lineair Zoeken & Accumulatie
Veelvoorkomende patronen:
```python
# Accumulator patroon (sommeren)
def bereken_gemiddelde(waarden):
    if len(waarden) == 0:
        return 0.0
    totaal = 0.0
    for w in waarden:
        totaal += w
    return totaal / len(waarden)
```

---

## 📝 Samenvatting
Lijsten zijn geordende en veranderlijke datastructuren. Elementen worden aangesproken via 0-based en negatieve indices of geselecteerd via slicing `[start:stop:step]`. Toewijzing van een lijst creëert aliasing; om onbedoelde neveneffecten te voorkomen dient men methodes zoals `.copy()` of `[:]` te gebruiken.