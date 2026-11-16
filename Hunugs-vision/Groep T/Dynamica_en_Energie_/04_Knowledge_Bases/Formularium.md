# 📐 Master Formularium — Dynamica en Energie

> [!info] Usage
> Every formula in this reference table links directly to its theoretical formulation and practical context in the chapter notes.

---

## 1. Kinematica van een Puntmassa (Rectilineair & Curvilineair)

| Concept | Formule | Verwijzing |
| :--- | :--- | :--- |
| **Snelheid (definitie)** | $$v = \frac{ds}{dt} = \dot{s}$$ | [[Chapter 2 - Variabele Versnelling#Differentiële Grondrelaties]] |
| **Versnelling (definitie)** | $$a = \frac{dv}{dt} = \frac{d^2s}{dt^2} = \dot{v} = \ddot{s}$$ | [[Chapter 2 - Variabele Versnelling#Differentiële Grondrelaties]] |
| **Tijdsonafhankelijke relatie** | $$a\,ds = v\,dv$$ | [[Chapter 2 - Variabele Versnelling#Differentiële Grondrelaties]] |
| **Constante versnelling: snelheid** | $$v(t) = v_0 + a_c t$$ | [[Chapter 1 - Constante Versnelling en Cirkelbeweging#Bewegingsvergelijkingen Constante Versnelling]] |
| **Constante versnelling: positie** | $$s(t) = s_0 + v_0 t + \frac{1}{2} a_c t^2$$ | [[Chapter 1 - Constante Versnelling en Cirkelbeweging#Bewegingsvergelijkingen Constante Versnelling]] |
| **Constante versnelling: kwadratisch**| $$v^2 = v_0^2 + 2 a_c (s - s_0)$$ | [[Chapter 1 - Constante Versnelling en Cirkelbeweging#Bewegingsvergelijkingen Constante Versnelling]] |
| **Projectielbeweging ($x, y$)** | $$\mathbf{r}(t) = \mathbf{r}_0 + \mathbf{v}_0 t + \frac{1}{2} \mathbf{g} t^2$$ | [[Chapter 1 - Constante Versnelling en Cirkelbeweging#Projectielbeweging 2D]] |
| **Tangentiële versnelling** | $$a_t = \frac{dv}{dt} = \dot{v}$$ | [[Chapter 1 - Constante Versnelling en Cirkelbeweging#Cirkelbeweging en t-n Coördinaten]] |
| **Normale versnelling** | $$a_n = \frac{v^2}{\rho}$$ | [[Chapter 1 - Constante Versnelling en Cirkelbeweging#Cirkelbeweging en t-n Coördinaten]] |
| **Totale curvilineaire versnelling** | $$a = \sqrt{a_t^2 + a_n^2}$$ | [[Chapter 2 - Variabele Versnelling#Curvilineaire Ontbinding]] |
| **Kromtestraal (cartesisch pad)** | $$\rho = \frac{\left[1 + \left(\frac{dy}{dx}\right)^2\right]^{3/2}}{\left|\frac{d^2y}{dx^2}\right|}$$ | [[Chapter 2 - Variabele Versnelling#Kromtestraal van een Pad]] |
| **Relatieve positie / snelheid** | $$\mathbf{r}_B = \mathbf{r}_A + \mathbf{r}_{B/A}, \quad \mathbf{v}_B = \mathbf{v}_A + \mathbf{v}_{B/A}$$ | [[Chapter 3 - Afhankelijke en Relatieve Beweging#Relatieve Beweging]] |
| **Afhankelijke kabelbeweging** | $$L = \sum s_i = \text{const} \implies \sum \dot{s}_i = 0, \quad \sum \ddot{s}_i = 0$$ | [[Chapter 3 - Afhankelijke en Relatieve Beweging#Katrolsystemen en Kinematische Koppelingen]] |

---

## 2. Kinetica van een Puntmassa (Newton & Bewegingsvergelijkingen)

| Concept | Formule | Verwijzing |
| :--- | :--- | :--- |
| **2e Wet van Newton (Vectorieel)** | $$\sum \mathbf{F} = m \mathbf{a}$$ | [[Chapter 4 - Kinetica Newton Rectangulair#Wetten van Newton]] |
| **Cartesische ontbinding** | $$\sum F_x = m a_x, \quad \sum F_y = m a_y, \quad \sum F_z = m a_z$$ | [[Chapter 4 - Kinetica Newton Rectangulair#Cartesische Projecties]] |
| **Normaal-tangentieel stelsel** | $$\sum F_t = m a_t, \quad \sum F_n = m \frac{v^2}{\rho}, \quad \sum F_b = 0$$ | [[Chapter 5 - Kinetica Newton t-n Stelsels#Bewegingsvergelijkingen in t-n-b]] |
| **Wrijvingskracht (kinetisch)** | $$F_w = \mu_k N$$ | [[Chapter 4 - Kinetica Newton Rectangulair#Contactkrachten en Wrijving]] |
| **Veerkracht (Wet van Hooke)** | $$F_v = k (l - l_0) = k s$$ | [[Chapter 4 - Kinetica Newton Rectangulair#Elastische Krachten]] |

---

## 3. Arbeid, Energie en Behoudswetten

| Concept | Formule | Verwijzing |
| :--- | :--- | :--- |
| **Arbeid van een kracht (integraal)**| $$U_{1-2} = \int_{\mathbf{r}_1}^{\mathbf{r}_2} \mathbf{F} \cdot d\mathbf{r} = \int_{s_1}^{s_2} F \cos\theta \, ds$$ | [[Chapter 6 - Arbeid en Energie#Definitie van Arbeid]] |
| **Arbeid constante kracht** | $$U_{1-2} = F_c \cos\theta \, (s_2 - s_1)$$ | [[Chapter 6 - Arbeid en Energie#Constante Krachten]] |
| **Arbeid van de zwaartekracht** | $$U_{1-2} = -W\,\Delta y = -mg\,(y_2 - y_1)$$ | [[Chapter 6 - Arbeid en Energie#Zwaartekrachtarbeid]] |
| **Arbeid van een lineaire veer** | $$U_{1-2} = -\left(\frac{1}{2} k s_2^2 - \frac{1}{2} k s_1^2\right)$$ | [[Chapter 6 - Arbeid en Energie#Veerarbeid]] |
| **Kinetische energie** | $$T = \frac{1}{2} m v^2$$ | [[Chapter 6 - Arbeid en Energie#Kinetische Energie]] |
| **Principe van Arbeid en Energie** | $$T_1 + \sum U_{1-2} = T_2$$ | [[Chapter 6 - Arbeid en Energie#Principe van Arbeid en Energie]] |
| **Mechanisch Vermogen** | $$P = \frac{dU}{dt} = \mathbf{F} \cdot \mathbf{v}$$ | [[Chapter 6 - Arbeid en Energie#Vermogen en Rendement]] |
| **Potentiële zwaartekrachtenergie**| $$V_g = mg y$$ | [[Chapter 7 - Behoud van Energie#Potentiële Energie]] |
| **Potentiële elastische energie** | $$V_e = \frac{1}{2} k s^2$$ | [[Chapter 7 - Behoud van Energie#Potentiële Energie]] |
| **Behoud van Mechanische Energie**| $$T_1 + V_1 = T_2 + V_2 \iff T_1 + V_{g,1} + V_{e,1} = T_2 + V_{g,2} + V_{e,2}$$ | [[Chapter 7 - Behoud van Energie#Behoudswet]] |

---

## 4. Impuls en Lineair Momentum

| Concept | Formule | Verwijzing |
| :--- | :--- | :--- |
| **Lineair Momentum** | $$\mathbf{L} = m\mathbf{v}$$ | [[Chapter 8 - Lineair Momentum en Stoot#Lineair Momentum]] |
| **Lineaire Impuls (Stoot)** | $$\mathbf{I} = \int_{t_1}^{t_2} \mathbf{F}\,dt$$ | [[Chapter 8 - Lineair Momentum en Stoot#Principe van Impuls en Momentum]] |
| **Principe van Impuls en Momentum** | $$m\mathbf{v}_1 + \sum \int_{t_1}^{t_2} \mathbf{F}\,dt = m\mathbf{v}_2$$ | [[Chapter 8 - Lineair Momentum en Stoot#Principe van Impuls en Momentum]] |
| **Behoud van Lineair Momentum** | $$\sum m_i \mathbf{v}_{i,1} = \sum m_i \mathbf{v}_{i,2}$$ | [[Chapter 8 - Lineair Momentum en Stoot#Behoud van Momentum]] |
| **Restitutiecoëfficiënt (Botsing)** | $$e = \frac{(v_B)_2 - (v_A)_2}{(v_A)_1 - (v_B)_1}$$ | [[Chapter 8 - Lineair Momentum en Stoot#Botsingen en Restitutie]] |
