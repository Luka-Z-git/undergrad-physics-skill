# 例题：自由空间电磁平面波（麦克斯韦方程，模板 A）

## 题意与图景

真空（$\rho=0,\ \mathbf J=0$）中，由麦克斯韦方程组推导电磁波波动方程，证明平面波解中 $\mathbf E\perp\mathbf B\perp\mathbf k$ 且 $|\mathbf E|=c|\mathbf B|$，并给出波速 $c$。已知量：$\mu_0,\ \varepsilon_0$；待求量：波动方程、$c$、横波性与幅度关系。

## 建模

- 选方程体系：**麦克斯韦方程组（真空微分形式）**，对旋度再取旋度得波动方程。理由：自由空间无源，取旋度可直接消去混合场分量。
- 适用条件：经典电磁学、线性真空介质、自由空间远场（无边界与导体）；平面波为简谐解 $e^{i(\mathbf k\cdot\mathbf r-\omega t)}$。

## 推导

1. 真空麦克斯韦方程：

$$
\nabla\cdot\mathbf E=0,\qquad \nabla\cdot\mathbf B=0,\qquad
\nabla\times\mathbf E=-\frac{\partial\mathbf B}{\partial t},\qquad
\nabla\times\mathbf B=\mu_0\varepsilon_0\frac{\partial\mathbf E}{\partial t}
$$

2. 对法拉第定律取旋度：

$$
\nabla\times(\nabla\times\mathbf E)=-\frac{\partial}{\partial t}(\nabla\times\mathbf B)
=-\mu_0\varepsilon_0\frac{\partial^2\mathbf E}{\partial t^2}
$$

3. 用恒等式 $\nabla\times(\nabla\times\mathbf E)=\nabla(\nabla\cdot\mathbf E)-\nabla^2\mathbf E$，并代入 $\nabla\cdot\mathbf E=0$：

$$
\nabla^2\mathbf E=\mu_0\varepsilon_0\frac{\partial^2\mathbf E}{\partial t^2}
$$

波速

$$
c=\frac{1}{\sqrt{\mu_0\varepsilon_0}}
$$

4. 平面波 $\mathbf E=\mathbf E_0 e^{i(\mathbf k\cdot\mathbf r-\omega t)}$，$\mathbf B=\mathbf B_0 e^{i(\mathbf k\cdot\mathbf r-\omega t)}$。由 $\nabla\cdot\mathbf E=0$：

$$
\mathbf k\cdot\mathbf E_0=0\quad\Rightarrow\quad \mathbf E\perp\mathbf k
$$

由法拉第定律 $\nabla\times\mathbf E=-\partial\mathbf B/\partial t$ 得 $i\mathbf k\times\mathbf E_0=i\omega\mathbf B_0$，即

$$
\mathbf B_0=\frac{\mathbf k\times\mathbf E_0}{\omega}
\quad\Rightarrow\quad \mathbf B\perp\mathbf k,\ \mathbf B\perp\mathbf E
$$

且取模（用 $\omega=ck$）：

$$
|\mathbf B_0|=\frac{k}{\omega}|\mathbf E_0|=\frac{|\mathbf E_0|}{c}
\quad\Rightarrow\quad |\mathbf E|=c|\mathbf B|
$$

## 验算

- **① F 量纲**：$c=\dfrac1{\sqrt{\mu_0\varepsilon_0}}$ 量纲 $\left(\dfrac{H}{m}\cdot\dfrac{F}{m}\right)^{-1/2}=LT^{-1}$。**PASS**。
- **② L 极限/特例**：静场极限 $\partial/\partial t\to0$ 时波动方程退化为无源拉普拉斯方程 $\nabla^2\mathbf E=0$ **PASS**；$\mathbf k=0$（均匀时变场）时波解退化，不再满足传播条件。**PASS**。
- **③ B 回代**：平面波代入 $\nabla\cdot\mathbf E=0$ 得 $\mathbf k\cdot\mathbf E_0=0$，代入法拉第定律得 $\mathbf B_0=\mathbf k\times\mathbf E_0/\omega$，两式与解的构造一致。**PASS**。
- **④ C 守恒量**：N/A（无机械守恒量；能量守恒由坡印廷定理 $\partial u/\partial t+\nabla\cdot\mathbf S=0$ 保证，另见 ⑦）。
- **⑦ J 一致性**：横波性双垂直 $\mathbf E\perp\mathbf k$ 且 $\mathbf E\perp\mathbf B$ 由两式独立推出，自洽；$|\mathbf E|=c|\mathbf B|$ 与 $\mathbf B_0=\mathbf k\times\mathbf E_0/\omega$ 取模结果一致。**PASS**。
- **⑤ E 数值抽样**：$\mu_0=4\pi\times10^{-7},\ \varepsilon_0=8.854\times10^{-12}$ → $c\approx2.998\times10^8\ \mathrm{m/s}$，与真空中光速一致。**PASS**。

验算摘要：`已通过 ①②③⑤⑦，④ N/A（坡印廷定理），FAIL 0 项`

## 答案

**真空电磁波满足 $\nabla^2\mathbf E=\mu_0\varepsilon_0\dfrac{\partial^2\mathbf E}{\partial t^2}$，波速 $c=\dfrac{1}{\sqrt{\mu_0\varepsilon_0}}\approx3\times10^8\ \mathrm{m/s}$；平面波中 $\mathbf E$、$\mathbf B$、$\mathbf k$ 两两垂直，且 $|\mathbf E|=c|\mathbf B|$。**

适用条件：真空、自由空间远场、简谐平面波近似。

## 易错点

1. 横波性符号：$\mathbf k\cdot\mathbf E_0=0$ 与 $\mathbf B_0=\mathbf k\times\mathbf E_0/\omega$ 的叉积顺序决定 $\mathbf B$ 方向，写反则右手系不自洽。
2. 把 $|\mathbf E|=c|\mathbf B|$ 用到介质或导电环境：仅在自由空间真空成立。
