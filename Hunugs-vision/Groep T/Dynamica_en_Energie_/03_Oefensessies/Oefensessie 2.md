---
course: "Dynamica en energie (T1ADE1)"
unit_type: oefensessie
status: todo
completed: false
est_hours: 2.0
priority: high
tags:
  - study-unit
---

# 🏋️ Oefensessie 2: Variabele Versnelling en Kromlijnige Banen

> [!info] Sessiedoelen
> - **Doel:** Analytisch integreren van niet-constante versnellingen ($a(t)$, $a(s)$, $a(v)$) en berekenen van kromtestralen $\rho$.
> - **Theoretische Grondslag:** [[Chapter 2 - Variabele Versnelling]].
> - **Relevante Formules:** [[Formularium#1. Kinematica van een Puntmassa (Rectilineair & Curvilineair)]].
> - **Sessie Status:** In behandeling (`[[Exercise Session Tracker]]`).

---

## 📑 Oefeningenoverzicht & Conceptuele Koppelingen

### Oefening 2.1 (Startniveau) — $a(t) = 3t^2 - 2t$
- **Probleem:** Gegeven $a(t) = 3t^2 - 2t$ met $s(0)=0$ en $v(0)=2\text{ m/s}$. Bepaal $v(t)$ en $s(t)$ op $t = 3\text{ s}$.
- **Vereiste Theorie:** [[Chapter 2 - Variabele Versnelling#2.1 Versnelling als functie van de tijd a = f(t)]].
- **Eindresultaat:** $v(3) = 20\text{ m/s}$, $s(3) = 23{,}25\text{ m}$.

---

### Oefening 2.2 (Gemiddeld niveau) — Weerstandskracht $a(v) = -k v^2$
- **Probleem:** Een bootje schakelt de motor uit bij $v_0 = 10\text{ m/s}$. De vertraging door waterweerstand is $a = -0{,}05 v^2$. Bepaal de tijd $t$ en afstand $s$ tot de snelheid gedaald is naar $2\text{ m/s}$.
- **Vereiste Theorie:** [[Chapter 2 - Variabele Versnelling#2.3 Versnelling als functie van de snelheid a = f(v)]].
- **Sleutelrelatie:** $dt = \frac{dv}{-0{,}05 v^2}$ en $ds = \frac{v\,dv}{-0{,}05 v^2} = \frac{dv}{-0{,}05 v}$.
- **Eindresultaat:** $t = 8\text{ s}$, $s = 32{,}2\text{ m}$.

---

### Oefening 2.3 (Moeilijk niveau) — Kromtestraal van een Skiër op Paraboolheuvel
- **Probleem:** Een skiër daalt af langs het profiel $y = \frac{1}{20} x^2$. In het punt met $x = 10\text{ m}$ bedraagt zijn baansnelheid $v = 15\text{ m/s}$ en neemt deze toe met $\dot{v} = 2\text{ m/s}^2$. Bereken $\rho$, $a_n$ en de totale versnelling $\|\mathbf{a}\|$.
- **Vereiste Theorie:**
  1. [[Chapter 2 - Variabele Versnelling#Kromtestraal van een Pad]].
  2. [[Chapter 2 - Variabele Versnelling#Curvilineaire Ontbinding]].
- **Eindresultaat:** $\rho = 56{,}57\text{ m}$, $a_n = 3{,}98\text{ m/s}^2$, $\|\mathbf{a}\| = 4{,}45\text{ m/s}^2$.
