---
course: "Dynamica en energie (T1ADE1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.0
priority: medium
tags:
  - study-unit
---

# ❓ Active Recall Q&A: Hoofdstuk 4

> [!tip] Instructie
> Test je fundamentele VLS-vaardigheden en de toepassing van Newton's tweede wet.

---

### Vraag 4.1: Traagheidskracht op het VLS
**Vraag:** Mag de vector $m\mathbf{a}$ worden ingetekend op een Vrijlichaamschema (VLS)? Verklaar waarom dit al dan niet toegelaten is.

> [!success]- Toon Uitwerking & Verwijzing
> **Antwoord:** **Neen.** De term $m\mathbf{a}$ mag **nooit** op een VLS worden geplaatst.
> **Verklaring:** Een VLS toont uitsluitend reële fysieke interactiekrachten die door de omgeving op het lichaam worden uitgeoefend (gravitatie, normaalkracht, wrijving, kabelkrachten). De term $m\mathbf{a}$ is geen kracht, maar de kinematische respons van de massa op de resulterende kracht. Het intekenen van $m\mathbf{a}$ op het VLS leidt steevast tot dubbeltellingen of tekenfouten bij het projecteren van $\sum \mathbf{F} = m\mathbf{a}$.
> 👉 *Theorie review:* [[Chapter 4 - Kinetica Newton Rectangulair#2. VLS Methodologie (Vrij Lichaam Schema / Free Body Diagram)]].

---

### Vraag 4.2: Blok op Helling met Wrijving
**Vraag:** Een blok met massa $m = 10\text{ kg}$ glijdt langs een helling met hoek $\theta = 30^\circ$ naar beneden. De kinetische wrijvingscoëfficiënt is $\mu_k = 0{,}2$. Bereken de versnelling langs de helling.

> [!success]- Toon Uitwerking & Verwijzing
> **Antwoord:** $a_x = 3{,}21\text{ m/s}^2$ langs de helling omlaag.
> **Stapsgewijze berekening:**
> 1. Leg de $x$-as langs de helling omlaag, en de $y$-as loodrecht op de helling omhoog.
> 2. Evenwicht loodrecht op de helling ($a_y = 0$):
>    $$\sum F_y = 0 \implies N - mg\cos\theta = 0 \implies N = mg\cos 30^\circ = 10 \times 9{,}81 \times 0{,}866 = 84{,}96\text{ N}$$
> 3. Wrijvingskracht:
>    $$F_w = \mu_k N = 0{,}2 \times 84{,}96 = 16{,}99\text{ N}$$
> 4. Bewegingsvergelijking langs de helling:
>    $$\sum F_x = m a_x \implies mg\sin\theta - F_w = m a_x$$
>    $$10 \times 9{,}81 \times 0{,}5 - 16{,}99 = 10 a_x \implies 49{,}05 - 16{,}99 = 10 a_x \implies a_x = 3{,}21\text{ m/s}^2$$
> 👉 *Theorie review:* [[Chapter 4 - Kinetica Newton Rectangulair#3. Cartesische Projecties]].
