---
title: Mock Exam Dynamica en Energie (T1ADE1)
course: "Dynamica en energie (T1ADE1)"
unit_type: exam
status: todo
completed: false
est_hours: 3.0
priority: high
tags:
  - study-unit
  - dynamica
  - mock-exam
---

# 🎯 Mock Exam: Dynamica en Energie (3-Uur Simulatie)

> [!info] Eerste Examen in Januari!
> **Datum:** ma **11.01.2027 om 08:30** (`DV1 - 02.54`).
> Maak deze volledige simulatie op papier met enkel het officiële formularium en wetenschappelijk rekentoestel.

---

## Vraag 1: Kinematica (Variabele Versnelling + Afhankelijke Beweging)
Een deeltje beweegt rechtlijnig met versnelling $a(v) = -0.02 v^2\text{ m/s}^2$. Op $t = 0$ is $s_0 = 0\text{ m}$ en $v_0 = 20\text{ m/s}$.
1. Bepaal de snelheid $v$ als functie van de afgelegde weg $s$.
2. Bereken na welke afstand $s$ de snelheid gehalveerd is tot $10\text{ m/s}$.

> [!success]- Oplossing ([[Chapter 2 - Variabele Versnelling]])
> - Gebruik $a\,ds = v\,dv$: $-0.02 v^2\,ds = v\,dv \implies -0.02\,ds = \frac{dv}{v}$.
> - Integreren van $0$ tot $s$ en $20$ tot $v$: $-0.02 s = \ln(v/20) \implies v(s) = 20 e^{-0.02s}$.
> - Voor $v = 10$: $s = \frac{\ln 2}{0.02} \approx 34.66\text{ m}$.

---

## Vraag 2: Kinetica ($t$-$n$ Stelsel + VLS)
Een wagentje ($m = 400\text{ kg}$) rijdt met constante snelheid $v = 15\text{ m/s}$ door het laagste punt van een cirkelvormig dal met kromtestraal $\rho = 30\text{ m}$.
1. Teken het **VLS** en **Kinetisch Schema** in het laagste punt.
2. Bereken de normaalkracht $N$ op de wielen.

> [!success]- Oplossing ([[Chapter 5 - Kinetica Newton t-n Stelsels]])
> - In het laagste punt wijst de normaal-as $n$ **omhoog** (naar het krommingsmiddelpunt!).
> - $\sum F_n = m a_n \implies N - mg = m \frac{v^2}{\rho}$.
> - $N = 400 \left(9.81 + \frac{15^2}{30}\right) = 400(9.81 + 7.50) = 6924\text{ N}$.

---

## Vraag 3: Arbeid, Energie & Stoot/Momentum (Gecombineerd!)
Een blok A ($m_A = 2\text{ kg}$) glijdt vanuit rust vanaf hoogte $h = 3.2\text{ m}$ langs een wrijvingsloze helling omlaag en botst centraal op stilstaand blok B ($m_B = 4\text{ kg}$) op een horizontaal vlak. De restitutiecoëfficiënt is $e = 0.8$. Na de botsing schuift blok B over een ruw horizontaal vlak ($\mu_k = 0.25$) tot stilstand.
Bereken de schuifafstand $d$ van blok B.

> [!success]- Oplossing ([[Chapter 7 - Behoud van Energie]] + [[Chapter 8 - Lineair Momentum en Stoot]])
> 1. **Behoud van energie (A glijdt omlaag):** $v_{A1} = \sqrt{2gh} = \sqrt{2(9.81)(3.2)} = 7.92\text{ m/s}$.
> 2. **Botsing A op B:**
>    - Behoud momentum: $2(7.92) + 0 = 2 v_{A2} + 4 v_{B2} \implies v_{A2} + 2 v_{B2} = 7.92$.
>    - Restitutie: $e = 0.8 = \frac{v_{B2} - v_{A2}}{7.92 - 0} \implies v_{B2} - v_{A2} = 6.34$.
>    - Optellen: $3 v_{B2} = 14.26 \implies v_{B2} = 4.75\text{ m/s}$.
> 3. **Arbeid & Energie (B remt af door wrijving):**
>    - $\frac{1}{2}m_B v_{B2}^2 - \mu_k m_B g d = 0 \implies d = \frac{v_{B2}^2}{2 \mu_k g} = \frac{4.75^2}{2(0.25)(9.81)} \approx 4.60\text{ m}$.
