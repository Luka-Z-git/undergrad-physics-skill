# 例题：一维谐振子（哈密顿方法，模板 A 完整示范）

> 本例题展示哈密顿力学路径：Legendre 变换、正则方程与守恒量验证。所有公式可直接粘贴进 Overleaf 编译。

## 题意与图景

- **系统**：质量 $m$ 的质点在光滑水平面上受线性回复力 $F = -kx$，一维运动。
- **约束**：直线运动（完整、定常约束）；无耗散（理想弹簧）。自由度 $= 1$。
- **坐标**：广义坐标 $x$。单位制：SI。
- **已知**：$m$、$k$。**待求**：哈密顿量 $H$、正则方程、运动解与周期。

## 建模

- **方法选择**：约束定常且无耗散，用拉格朗日量做 Legendre 变换进入相空间 $(x,p)$，故用哈密顿方法。
- **拉格朗日量**：

$$
L = T - V = \frac{1}{2} m\dot x^2 - \frac{1}{2} kx^2
$$

- **广义动量与哈密顿量**：

$$
p = \frac{\partial L}{\partial\dot x} = m\dot x, \qquad
H = p\dot x - L = \frac{p^2}{2m} + \frac{1}{2} kx^2
$$

- **适用条件声明**：约束定常且 $T$ 为 $\dot x$ 的二次齐次式，故 $H = E$；无耗散，能量守恒可用。

## 推导

正则方程：

$$
\dot x = \frac{\partial H}{\partial p} = \frac{p}{m}, \qquad
\dot p = -\frac{\partial H}{\partial x} = -kx
$$

对第一式求导并代入第二式：

$$
m\ddot x = \dot p = -kx \quad\Longrightarrow\quad \ddot x + \frac{k}{m}x = 0
$$

令 $\omega = \sqrt{k/m}$，通解：

$$
x(t) = A\cos(\omega t + \varphi), \qquad
p(t) = -mA\omega\sin(\omega t + \varphi)
$$

周期：

$$
T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{m}{k}}
$$

## 验算

- **① F 量纲**：$[p^2/(2m)] = M^2L^2T^{-2}/M = ML^2T^{-2}$，$[\frac12 kx^2] = ML^2T^{-2}$，$H$ 量纲为能量；$[\omega] = [k/m]^{1/2} = T^{-1}$，$[2\pi\sqrt{m/k}] = T$。**PASS**。
- **② L 极限/特例**：$k \to 0$ 时 $H \to p^2/(2m)$（自由粒子），$\dot x = p/m$ 保持；$m \to \infty$ 时 $\omega \to 0$（惯性大、回复相对弱），极限合理。**PASS**。
- **③ B 回代**：将 $x(t)$ 代入 $m\ddot x + kx = 0$：$-m\omega^2 x + kx = 0$，用 $\omega^2 = k/m$ 得恒等；正则方程消去 $p$ 亦得同一式。**PASS**。
- **④ C 守恒量**：$H$ 不显含 $t$ 且无耗散，$E = H$ 守恒。取 $m = 1\,\mathrm{kg}$、$k = 1\,\mathrm{N/m}$，状态 $(x,p) = (1,0)$ 与 $(0,1)$，$H$ 均为 $0.5\,\mathrm{J}$。**PASS**。
- **⑤ E 数值抽样**（可选加分项）：$m = 1\,\mathrm{kg}$、$k = 1\,\mathrm{N/m}$ 时 $\omega = 1\,\mathrm{s^{-1}}$、$T = 2\pi\,\mathrm{s}$；$x(0)=1\,\mathrm{m}$、$p(0)=0$ 时 $E = 0.5\,\mathrm{J}$，与④一致。**PASS**。
- **⑥ I 独立方法**（可选加分项）：直接解牛顿方程 $m\ddot x = -kx$ 得同一角频率 $\omega = \sqrt{k/m}$ 与周期 $2\pi\sqrt{m/k}$。**PASS**。

验算摘要：`已通过 ①②③④，FAIL 0 项（⑤⑥ 已加做）`

## 答案

**哈密顿量 $H = \dfrac{p^2}{2m} + \dfrac{1}{2}kx^2$；正则方程 $\dot x = \dfrac{p}{m}$、$\dot p = -kx$；运动解 $x(t) = A\cos(\omega t + \varphi)$，角频率 $\omega = \sqrt{k/m}$，周期 $T = 2\pi\sqrt{m/k}$。**

适用条件：一维、定常完整约束、无耗散；$A$ 与 $\varphi$ 由初始条件确定。

## 易错点

1. $p$ 定义漏质量因子（$p = m\dot x$），或 $H$ 中残留 $\dot x$。
2. 正则方程符号写反（$\dot p = +kx$）。
3. 把 $H$ 守恒直接当机械能守恒：本例因约束定常且 $T$ 二次齐次成立，但须显式核对条件。
