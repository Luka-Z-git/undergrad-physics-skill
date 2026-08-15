# 例题：一维自由粒子散射态归一化（边界案例，模板 A）

## 题意与图景

- **系统**：一维自由粒子，定态波函数 $\psi_k(x)=A e^{ikx}$，$E=\hbar^2k^2/(2m)$。
- **约束**：非相对论、无外势、全空间 $x\in(-\infty,\infty)$；波函数为平面波（散射态/非束缚态）。
- **坐标**：一维 $x$；单位制：SI。
- **已知**：$m$、$k$。**待求**：$\psi_k$ 能否按 $\int|\psi|^2dx=1$ 归一化；不能时给出 $\delta$ 函数归一化并说明物理量。

## 建模

- **方法选择**：把平面波当作散射态处理，用连续谱归一化 $\langle\psi_k|\psi_{k'}\rangle=\delta(k-k')$；不用束缚态归一化。
- **适用条件声明**：非相对论、自由空间、定态；本案例刻意展示“无法按标准方式完成”时的诚实声明。

## 推导

对任意有限 $A$：

$$
\int_{-\infty}^{\infty}|\psi_k|^2\,dx=|A|^2\int_{-\infty}^{\infty}dx=\infty
$$

因此 $\int|\psi_k|^2dx=1$ 无解（除非 $A=0$，退化为零波函数）。改用 $\delta$ 函数归一化：

$$
\psi_k(x)=\frac{1}{\sqrt{2\pi}}e^{ikx}
$$

利用

$$
\int_{-\infty}^{\infty}e^{i(k'-k)x}\,dx=2\pi\,\delta(k'-k)
$$

得

$$
\langle\psi_k|\psi_{k'}\rangle=\frac{1}{2\pi}\int e^{i(k'-k)x}\,dx=\delta(k'-k)
$$

物理量取概率流密度：

$$
j=\frac{\hbar}{m}\mathrm{Im}\left(\psi^*\frac{\partial\psi}{\partial x}\right)=\frac{\hbar k}{m}
$$

它描述粒子通量，不要求总概率等于 1。

## 验算

- **① F 量纲**：$dx$ 量纲 $L$，$e^{ikx}$ 无量纲，$\delta(k'-k)$ 量纲 $[k]^{-1}=L$，两边一致；$[j]=[\hbar k/m]=LT^{-1}$。**PASS**。
- **② L 极限/特例**：$k\to0$ 时 $\psi$ 趋于常数，仍不可归一化；波包 $\psi_a(x)=(2\pi a^2)^{-1/4}e^{-x^2/(4a^2)}e^{ikx}$ 在 $a\to\infty$ 时趋于平面波极限。**PASS**。
- **③ B 回代**：$\psi_k$ 代入定态方程 $-\hbar^2\psi''/(2m)=E\psi$，$E=\hbar^2k^2/(2m)$ 恒等；把 $\langle\psi_k|\psi_{k'}\rangle=\delta(k-k')$ 代回正交积分公式，两边一致。**PASS**。
- **④ C 守恒量**：自由粒子动量与能量守恒；概率流密度 $j=\hbar k/m$ 为常数，无源。**PASS**。

验算摘要：`已通过 ①②③④，FAIL 0 项（附加说明：散射态不归一化为 1）`

## 答案

**平面波散射态不能按 $\int|\psi|^2dx=1$ 归一化；改用 $\delta$ 函数归一化 $\langle\psi_k|\psi_{k'}\rangle=\delta(k-k')$，取 $\psi_k=\dfrac{1}{\sqrt{2\pi}}e^{ikx}$，物理量由概率流密度 $j=\dfrac{\hbar k}{m}$ 描述。**

适用条件：一维自由粒子、非相对论、连续谱散射态；束缚态仍使用 $\int|\psi|^2dx=1$。

## 易错点

1. 强行令 $\int|\psi|^2dx=1$ 会得到 $A=0$ 的伪解，掩盖“散射态不可归一化”的物理事实。
2. 把 $\delta$ 函数归一化直接当作概率密度：散射态给出的是概率流，不是局域概率。
3. 混淆束缚态与散射态的量纲和归一化约定。
