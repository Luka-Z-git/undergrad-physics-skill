# 例题：一维量子谐振子（模板 A 完整示范）

> 本例题展示升降算符方法的模板 A 用法：代数求谱、基态构造、归一化与回代验证。所有公式可直接粘贴进 Overleaf 编译。

## 题意与图景

- **系统**：质量为 $m$ 的粒子在势 $V(x)=\frac12 m\omega^2 x^2$ 中做一维量子运动。
- **约束**：非相对论单粒子；势能定常，求束缚态能谱与基态波函数。
- **坐标**：一维 $x$，单位制：SI。
- **已知**：$m$、$\omega$。**待求**：能级 $E_n$、基态波函数 $\psi_0(x)$。

## 建模

- **方法选择**：谐振子势具有升降算符代数结构，用 $\hat a,\hat a^\dagger$ 免解微分方程。
- **哈密顿量**：

$$
\hat H=\frac{\hat p^2}{2m}+\frac12 m\omega^2\hat x^2
$$

- **升降算符**：

$$
\hat a=\sqrt{\frac{m\omega}{2\hbar}}\left(\hat x+\frac{i\hat p}{m\omega}\right), \qquad
[\hat a,\hat a^\dagger]=1
$$

$$
\hat H=\hbar\omega\left(\hat a^\dagger\hat a+\frac12\right)
$$

- **适用条件声明**：非相对论、无耗散、势能定常。

## 推导

令 $\hat N=\hat a^\dagger\hat a$，本征方程 $\hat N|n\rangle=n|n\rangle$，$n=0,1,2,\ldots$。因此：

$$
E_n=\hbar\omega\left(n+\frac12\right)
$$

基态满足 $\hat a\psi_0=0$：

$$
\left(x+\frac{\hbar}{m\omega}\frac{d}{dx}\right)\psi_0=0
$$

解得：

$$
\psi_0(x)=A e^{-m\omega x^2/(2\hbar)}
$$

归一化：

$$
1=|A|^2\int_{-\infty}^{+\infty}e^{-m\omega x^2/\hbar}\,dx=|A|^2\sqrt{\frac{\pi\hbar}{m\omega}}
$$

取正实数相位：

$$
\psi_0(x)=\left(\frac{m\omega}{\pi\hbar}\right)^{1/4}e^{-m\omega x^2/(2\hbar)}
$$

## 验算

- **① F 量纲**：$[\hbar\omega]=ML^2T^{-2}$（能量）；$[\sqrt{m\omega/\hbar}]=L^{-1}$，$[\psi_0]=L^{-1/2}$。**PASS**。
- **② L 极限/特例**：$n=0$ 得零点能 $\hbar\omega/2$；$\omega\to0$ 时 $E_0\to0$（势阱变平）。**PASS**。
- **③ B 回代**：$\psi_0'=-(m\omega x/\hbar)\psi_0$，$\psi_0''=[(m\omega x/\hbar)^2-m\omega/\hbar]\psi_0$；代入 $\hat H\psi_0$ 后动能与势能项抵消，得 $E_0=\hbar\omega/2$，恒等。**PASS**。
- **④ C 守恒量**：定态概率密度不显含时间，能量期望值恒定。**PASS**。
- **⑤ E 数值抽样**（可选加分项）：$\int_{-\infty}^{+\infty}|\psi_0|^2dx=1$ 由高斯积分核对；$E_0=\hbar\omega/2$。**PASS**。
- **⑥ I 独立方法**（可选加分项）：直接解定态方程的 Hermite 多项式级数截断条件，得同一能谱 $(n+1/2)\hbar\omega$。**PASS**。

验算：`①②③④，FAIL 0 项（⑤⑥ 已加做）`

## 答案

**能级 $E_n=\left(n+\dfrac12\right)\hbar\omega$；基态波函数 $\psi_0(x)=\left(\dfrac{m\omega}{\pi\hbar}\right)^{1/4}\exp\left(-\dfrac{m\omega x^2}{2\hbar}\right)$。**

适用条件：非相对论、无自旋、势能定常；升降算符方法要求势为二次型。

## 易错点

1. 零点能是 $\hbar\omega/2$，不是 0。
2. $\hat a,\hat a^\dagger$ 不是厄米算符，不能直接当可观测量的测量算符。
3. 基态归一化因子易漏 $\pi^{1/4}$；高斯积分须完整写出。
