---
title: "Mock Exam 3 - Oplossingen en Zelfevaluatie Rubric"
course: "Wiskundige basistechnieken (T1AWB1)"
unit_type: exam
status: todo
completed: false
est_hours: 1.5
priority: high
tags:
  - study-unit
  - wiskunde
  - mock-exam
---

# ✅ Mock Exam Oplossingen & Zelfevaluatie Rubric

> Gebruik deze uitwerkingen pas nadat je [[Mock Exam 1 - Proefexamen Halverwege Semester (Kennismakingsexamen)]] of [[Mock Exam 2 - Volledig Proefexamen Deel 1, 2 en 3]] onder echte examentijd hebt gemaakt!

---

## 📘 Beknopte Oplossingssleutel — Mock Exam 1
1. **Bewijs 02:** Zie [[Bewijs 02 - Afstand tussen Punt en Rechte in R2]].
2. **Rechtenbundel:** $(2x - y + 3) + \lambda(x + 3y - 2) = 0 \implies (2+\lambda)x + (3\lambda - 1)y + (3 - 2\lambda) = 0$. Normaalvector $\mathbf{n} = [2+\lambda, 3\lambda-1]^T \perp \mathbf{n}_3 = [4, -1]^T \implies 4(2+\lambda) - (3\lambda-1) = 0 \implies \lambda = -9$. Invullen: $-7x - 28y + 21 = 0 \iff x + 4y - 3 = 0$.
3. **Kruisende rechten:** $\mathbf{d}_1 = [1, -1, 3]^T$, $\mathbf{d}_2 = [2, 1, -1]^T \implies \mathbf{n} = \mathbf{d}_1 \times \mathbf{d}_2 = [-2, 7, 3]^T$. Vector tussen $P_1(1,2,0)$ en $P_2(0,1,1)$: $\overrightarrow{P_1 P_2} = [-1, -1, 1]^T$. Afstand $d = \frac{|\overrightarrow{P_1 P_2} \cdot \mathbf{n}|}{\|\mathbf{n}\|} = \frac{|2 - 7 + 3|}{\sqrt{4+49+9}} = \frac{2}{\sqrt{62}}$.
4. **Parameterstelsel:** $\det(A) = (a-1)^2(a+2)$.
   - $a \neq 1$ en $a \neq -2$: **1 unieke oplossing**.
   - $a = 1$: alle rijen identiek $[1\; 1\; 1 \mid 1] \implies$ **$\infty^2$ oplossingen**.
   - $a = -2$: strijdig stelsel ($0 = 6$ in laatste rij) $\implies$ **0 oplossingen**.
5. **Inverse:** $\det(A) = 1$, $A^{-1} = \begin{bmatrix} -3 & -2 & 2 \\ 2 & 1 & -1 \\ -2 & 0 & 1 \end{bmatrix}$.

---

## 📗 Beknopte Oplossingssleutel — Mock Exam 2
- **5. Complexe getallen:** $w = -8 + 8\sqrt{3}\,i = 16\,\text{cis}(\frac{2\pi}{3}) \implies z_k = 2\,\text{cis}\left(\frac{\pi}{6} + k\frac{\pi}{2}\right)$ voor $k=0,1,2,3$: $\pm(\sqrt{3}+i)$ en $\pm(-1+\sqrt{3}i)$.
- **6. Gram-Schmidt:** $\mathbf{u}_1 = \frac{1}{\sqrt{2}}[1,1,0]^T$, $\mathbf{u}_2 = \frac{1}{\sqrt{6}}[1,-1,2]^T$. Projectie: $(v\cdot u_1)u_1 + (v\cdot u_2)u_2 = \frac{3}{2}[1,1,0]^T + \frac{5}{6}[1,-1,2]^T = \left[\frac{7}{3}, \frac{2}{3}, \frac{5}{3}\right]^T$.
- **7a. Limiet:** $\ln y = \sin x \ln x \to 0$ (l'Hôpital op $\frac{\ln x}{1/\sin x}$) $\implies \lim = e^0 = 1$.
- **7b. Reeks:** $\lim a_n = 0$ en dalend $\implies$ **convergent** via Leibniz. Echter $\sum \frac{n}{n^2+1} \sim \sum \frac{1}{n}$ divergeert $\implies$ **voorwaardelijk (relatief) convergent**.
- **8a. Integraal:** Veeltermdeling eerst! $\frac{2x^3+x+1}{x^2+1} = 2x + \frac{-x+1}{x^2+1} \implies x^2 - \frac{1}{2}\ln(x^2+1) + \arctan x + C$.
- **8b. Integraal:** Partieel met $u = \arctan x, dv = x\,dx \implies \left[\frac{x^2}{2}\arctan x\right]_0^1 - \frac{1}{2}\int_0^1 \frac{x^2}{1+x^2}\,dx = \frac{\pi}{8} - \frac{1}{2}\left(1 - \frac{\pi}{4}\right) = \frac{\pi}{4} - \frac{1}{2}$.
- **9a. Cardioïde:** $A = \frac{1}{2}\int_0^{2\pi} (1+\cos\theta)^2\,d\theta = \frac{3\pi}{2}$.
- **9b. Machtreeks:** $R = 3$, centrum $x_0 = 2 \implies (-1, 5)$. Bij $x=-1$: $\sum \frac{(-1)^n}{n}$ (Leibniz: **conv.**); bij $x=5$: $\sum \frac{1}{n}$ (harmonisch: **div.**). Interval: **$[-1, 5)$**.

---

## 📊 Zelfevaluatie Rubric (Doel: $\ge 12/20$)
| Onderdeel | Max | Mijn Score | Actie bij $< 60\%$ |
| :--- | :---: | :---: | :--- |
| **Bewijzen (Deel A)** | 20 | `/20` | Herhaal [[00 - Index der Bewijzen]] blind op wit blad |
| **Oefeningen (Deel B)** | 20 | `/20` | Werk zwakke sessies opnieuw door in [[Exercise Session Tracker]] |
| **TOTAAL** | **40** | **`/40`** | ($\ge 24/40 = 12/20$ veilig geslaagd!) |
