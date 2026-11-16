# 🎯 Exam Preparation, Methodology & Pitfalls

> [!warning] Exam Architecture (100% Written Evaluation)
> - **Format:** Written problem-solving exam (3 hours).
> - **Allowed Aids:** Official formula sheet (Formularium) and approved scientific calculator.
> - **Prerequisite Competence:** Mastery of the Free Body Diagram (VLS / FBD). Failure to draw an accurate VLS will invalidate subsequent equations of motion.

---

## 🧠 Algemeen Oplossingsstappenplan (Universal Problem Heuristic)

```
[Lees Opgave & Identificeer Geometrie]
               │
               ▼
   [Bepaal het Type Probleem]
   ├── Kinematica: Snelheden, posities, versnellingen zónder krachten?
   │     ├── Constante versnelling? ──> Analytische formules
   │     └── Variabele versnelling? ──> Differentiaalrelaties integreren
   │
   └── Kinetica: Krachten, massa's, versnellingen of energieën betrokken?
         ├── Positie/Snelheid gekoppeld aan krachten? ──> Arbeid & Energie
         ├── Krachten & ogenblikkelijke versnellingen? ──> Newton (F = m a)
         └── Tijd & botstijd/krachtstoot? ────────────> Impuls & Momentum
```

---

## ⚠️ Top 5 Valkuilen op het Examen (Critical Traps)

### 1. Foutieve VLS / FBD Constructie
- **Fout:** Traagheidskrachten ($m \mathbf{a}$) intekenen op het VLS als ware het fysieke krachten.
- **Correcte Aanpak:** Het VLS bevat *uitsluitend* echte interactiekrachten (contactkrachten, normaalkracht, wrijving, kabelkracht, gravitatie). De term $m \mathbf{a}$ hoort thuis in het *kinetische schema* aan de rechterkant van $\sum \mathbf{F} = m \mathbf{a}$.

### 2. Formules voor Constante Versnelling toepassen bij Variabele Versnelling
- **Fout:** Gebruik van $v = v_0 + at$ of $s = s_0 + v_0t + \frac{1}{2}at^2$ wanneer de versnelling afhangt van tijd $a(t)$, positie $a(s)$ of snelheid $a(v)$.
- **Correcte Aanpak:** Integreer altijd direct vanuit de basisdefinities:
  $$a = \frac{dv}{dt} \implies \int dv = \int a\,dt, \qquad v = \frac{ds}{dt} \implies \int ds = \int v\,dt, \qquad a\,ds = v\,dv \implies \int a\,ds = \int v\,dv$$.

### 3. Wrijvingsrichting bij Bewegende Referentiekaders
- **Fout:** Wrijving tekenen tegengesteld aan de absolute snelheid $\mathbf{v}$ in plaats van tegengesteld aan de *relatieve glijsnelheid* $\mathbf{v}_{\text{rel}}$ ten opzichte van het contactoppervlak.
- **Correcte Aanpak:** Bepaal eerst $\mathbf{v}_{B/A} = \mathbf{v}_B - \mathbf{v}_A$. De wrijvingskracht op $B$ door $A$ werkt parallel aan het contactvlak en strikt tegengesteld aan $\mathbf{v}_{B/A}$.

### 4. Tekenfout bij Arbeid van Veren
- **Fout:** Verkeerde toestandstermen in de veerarbeid: $U_{\text{veer}} \neq \frac{1}{2}k(s_2 - s_1)^2$.
- **Correcte Aanpak:** De rek $s$ moet afzonderlijk gekwadrateerd worden:
  $$U_{1-2} = -\left[\frac{1}{2}k s_2^2 - \frac{1}{2}k s_1^2\right] = \frac{1}{2}k (s_1^2 - s_2^2)$$
  waarbij $s = l - l_0$ de uitrekking ten opzichte van de *ongespannen rustlengte* $l_0$ is.

### 5. Niet-constante Krachthoek bij Arbeidsintegralen
- **Fout:** $U = F \Delta s \cos\theta$ toepassen terwijl de hoek $\theta$ verandert tijdens het traject (zoals bij een bobslee getrokken door een vaste katrol op hoogte).
- **Correcte Aanpak:** Pas de kettingregel/verplaatsing van het touwuiteinde toe: bereken de effectieve verkorting van de kabel $\Delta L_{\text{kabel}}$ zodat $U = F \cdot \Delta L_{\text{kabel}}$.

---

## 📁 Archief Oude Examens & Proeftoetsen
- `[[Retake test Hertest FBD 2627.pdf]]` — *Hertest VLS: dubbele blokken op helling met veer en wrijving*.
- `[[Test_4p.pdf]]` — *Tussentijdse formatieve toetsing*.
