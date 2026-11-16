---
course: "SGDM (T1ASD1)"
unit_type: qa
status: todo
completed: false
est_hours: 1.0
priority: medium
tags:
  - study-unit
---

# 💡 Oefenvragenbank: Kristallen, Defecten en Plasticiteit
#oefenvragen #meerkeuze #kristallografie #dislocaties #schmid #antwoorden

Koppeling naar theorie:
* [[04_Theory_Notes/H07_Kristallijne_Structuren_en_Miller_Indices]]
* [[04_Theory_Notes/H10_Plasticiteit_en_Trekproef]]
* [[04_Theory_Notes/H11_Roosterdefecten_en_Verstevigingsmechanismen]]

---

### Vraag 1
Waarom is korrelgrensversteviging (Hall-Petch) uniek in vergelijking met de andere drie verstevigingsmechanismen (koudvervorming, oplossingsharding, precipitatieharding)?
* A: Het verlaagt de vloeigrens maar verhoogt de E-modulus.
* B: Het verhoogt de vloeigrens zonder verlies aan taaiheid en verlaagt zelfs de ductiel-brosse overgangstemperatuur (DBTT).
* C: Het werkt uitsluitend bij temperaturen boven $0.5 T_m$.
* D: Het elimineert alle dislocaties uit het kristalrooster.

> [!success]- Toon Oplossing & Uitleg
> **Correct Antwoord: B**
> **Uitleg**: Bij de meeste verstevigingsmechanismen (zoals cold work of precipitaten) stijgt de sterkte ten koste van ductiliteit en taaiheid. Korrelverfijning dwingt scheuren echter om voortdurend van richting te veranderen aan korrelgrenzen, waardoor zowel de sterkte ($\sigma_y \propto d^{-1/2}$) als de kerftaaiheid toenemen.
> *Zie theorie*: [[04_Theory_Notes/H11_Roosterdefecten_en_Verstevigingsmechanismen#3-de-4-fundamentele-verstevigingsmechanismen]]

---

### Vraag 2
Wat veroorzaakt het optreden van Lüdersbanden bij de trekproef op zacht ongelegeerd staal?
* A: Het plotseling smelten van korrelgrenzen door wrijvingswarmte.
* B: Het losbreken van dislocaties die door interstitiële koolstofatomen (Cottrell-wolken) verankerd waren.
* C: De plotse transformatie van ferriet naar martensiet onder spanning.
* D: Het ontstaan van holtes en insnoering in het midden van het proefstuk.

> [!success]- Toon Oplossing & Uitleg
> **Correct Antwoord: B**
> **Uitleg**: Kleine C-atomen diffunderen naar de rekzones onder randdislocaties (Cottrell-wolk). Zodra de spanning de bovenste vloeigrens $R_{eH}$ bereikt, breken de dislocaties collectief los en kunnen ze bij een lagere spanning ($R_{eL}$) propageren, wat zich macroscopisch toont als Lüdersbanden.
> *Zie theorie*: [[04_Theory_Notes/H10_Plasticiteit_en_Trekproef#2-vloeigebied-lüdersbanden--cottrell-wolken]]

---

### Vraag 3
In een eenkristal onder uniaxiale trekspanning $\sigma$ treedt glijding op langs een glijstelsel waarvan het glijvlak een hoek $\phi$ maakt met de trek-as en de glijrichting een hoek $\lambda$. Bij welke hoekencombinatie is de benodigde trekspanning om vloeiing te starten minimaal?
* A: $\phi = 0^\circ, \lambda = 90^\circ$
* B: $\phi = 45^\circ, \lambda = 45^\circ$
* C: $\phi = 90^\circ, \lambda = 0^\circ$
* D: $\phi = 30^\circ, \lambda = 60^\circ$

> [!success]- Toon Oplossing & Uitleg
> **Correct Antwoord: B**
> **Uitleg**: Volgens de wet van Schmid is $\tau = \sigma \cos\phi \cos\lambda$. De Schmid-factor $m = \cos\phi \cos\lambda$ bereikt haar wiskundig maximum van $0.5$ wanneer $\phi = \lambda = 45^\circ$. Omdat $\sigma_y = \tau_{\text{CRSS}} / m$, is de benodigde vloeispanning $\sigma_y$ dan minimaal ($\sigma_y = 2\tau_{\text{CRSS}}$).
> *Zie theorie*: [[04_Theory_Notes/H11_Roosterdefecten_en_Verstevigingsmechanismen#2-dislocatiebeweging--de-wet-van-schmid]]
