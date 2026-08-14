# 例题：一维矩形势垒隧穿（势垒散射，模板 A）

## 题意与图景

质量为 $m$ 的粒子以能量 $E<V_0$ 从左向右入射高度 $V_0$、宽度 $a$ 的一维矩形势垒，求透射系数 $T$。已知量：$m,\ E,\ V_0,\ a,\ \hbar$；待求量：透射系数 $T$。

## 建模

- 选方程体系：**定态薛定谔方程**，三区（左入射区 $x<0$、垒区 $0<x<a$、右透射区 $x>a$）分区求解并匹配边界条件。理由：势垒分段常数，逐区指数解即可。
- 适用条件：非相对论单粒子、$E<V_0$（隧穿区）；波函数与 $\psi'$ 在势的有限跳变处连续；用概率流定义透射系数。

## 推导

1. 令 $\kappa=\dfrac{\sqrt{2m(V_0-E)}}{\hbar}$，$k=\dfrac{\sqrt{2mE}}{\hbar}$。三区波函数：

$$
\psi(x)=\begin{cases}
e^{ikx}+R e^{-ikx}, & x<0\\[2pt]
A e^{\kappa x}+B e^{-\kappa x}, & 0<x<a\\[2pt]
t\,e^{ikx}, & x>a
\end{cases}
$$

2. 在 $x=0$、$x=a$ 处匹配 $\psi$ 与 $\psi'$ 连续，四个方程消去 $A,B,R$，得透射幅 $t$。

3. 透射系数 $T=|t|^2$ 的标准结果为：

$$
T = \left[1+\frac{V_0^2}{4E(V_0-E)}\sinh^2(\kappa a)\right]^{-1}
$$

4. 厚垒或高垒极限 $\kappa a\gg1$ 时 $\sinh(\kappa a)\approx\tfrac12 e^{\kappa a}$：

$$
T \approx \frac{16E(V_0-E)}{V_0^2}\, e^{-2\kappa a}
$$

表现为指数抑制（隧穿）。

## 验算

- **① F 量纲**：$\kappa=\dfrac{\sqrt{2m(V_0-E)}}{\hbar}$ 量纲 $L^{-1}$，故 $\kappa a$ 无量纲、$T$ 无量纲。**PASS**。
- **② L 极限/特例**：$V_0\to\infty$ 或 $a\to\infty$ 时 $T\to0$（垒不可穿越）；$V_0\to E$ 时 $\kappa\to0$、$\sinh(\kappa a)\to\kappa a$，$T\to\left[1+\dfrac{mV_0 a^2}{2\hbar^2}\right]^{-1}$，与 $E>V_0$ 情形的 $T$ 在阈限处连续。**PASS**。
- **③ B 回代**：三区波函数分别代入各自定态方程，均满足 $\psi''+\dfrac{2m(E-V)}{\hbar^2}\psi=0$。**PASS**。
- **④ C 守恒量**：定态下概率流守恒，$J_{\text{in}}=J_{\text{trans}}+J_{\text{ref}}$，即 $1=|R|^2+|t|^2$，与 $T=|t|^2$ 定义一致。**PASS**。
- **⑤ E 数值抽样**：电子 $m=9.11\times10^{-31}$，$V_0-E=1\ \mathrm{eV}$，$a=0.5\ \mathrm{nm}$ → $\kappa a\approx3.6$，$T\approx e^{-7.2}\sim10^{-3}$，呈指数小量，符合隧穿直觉。**PASS**。

验算摘要：`已通过 ①②③④⑤，FAIL 0 项`

## 答案

**透射系数 $T=\left[1+\dfrac{V_0^2}{4E(V_0-E)}\sinh^2(\kappa a)\right]^{-1}$，其中 $\kappa=\dfrac{\sqrt{2m(V_0-E)}}{\hbar}$；厚垒极限 $T\approx\dfrac{16E(V_0-E)}{V_0^2}e^{-2\kappa a}$（无量纲）。**

适用条件：$E<V_0$、单粒子非相对论、一维矩形势垒。

## 易错点

1. 垒区用 $\sin$ 而非 $\sinh$：$E<V_0$ 时垒区是实指数衰减，波矢为虚数，对应 $\kappa$（双曲函数），不是振荡的 $k$。
2. 忘记匹配 $\psi'$：有限跳变处 $\psi$ 与 $\psi'$ 都要连续，漏匹配会导致系数少一个方程。
