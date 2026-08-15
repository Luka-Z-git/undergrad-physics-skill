# 基础量子力学模块 (Basic Quantum Mechanics)

## 适用范围

**基础量子力学**：波函数与概率诠释、定态薛定谔方程、一维势阱/势垒、谐振子、算符与对易关系、角动量、氢原子能级入门、非简并微扰论入门与自旋 1/2 基础（**非相对论近似，忽略精细结构**；简并微扰/相对论量子力学不在范围）。

（子域标准结构同 mechanics.md）

## 0. 方法选择表

按系统特征选方法；方法不唯一时，选推导最短、验证最直接者，并在建模节用一句话说明理由。

| 系统特征 | 首选方法 | 选择理由 | 本域特化验证 |
|---|---|---|---|
| 一维定态势（阱/垒/谐振子） | 解定态薛定谔方程（§1） | 直接求本征函数与本征值 | B（$H\psi=E\psi$）、J（归一化/正交） |
| 谐振子能级与态 | 升降算符（§2） | 代数法免解微分方程 | J（$[a,a^\dagger]=1$、归一化） |
| 算符顺序/可观测性 | 对易子展开（§2） | 逐项作用到试探函数 | J（厄米性、对易结果） |
| 角动量本征值问题 | 本征方程（§3） | 已知 $L^2,L_z$ 谱 | J（$m$ 范围、归一化） |
| 氢原子/类氢原子能级 | 球坐标分离变量（§3） | 标准教材解法 | L（$n\to\infty$、$n=1$ 基态）、J（归一化） |
| 弱微扰下的能级修正 | 非简并微扰论（§4） | 已知 H0 谱且所考虑能级非简并 | I（直接对角化/数值对照）、L（微扰→0） |
| 自旋 1/2 可观测量 | 泡利矩阵（§5） | 代数法直接构造 | J（对易/厄米/σ²=I） |

## 1. 定态薛定谔方程与一维系统

### 识别特征

- 势能不含时，求束缚态能量、波函数、透射/反射系数。
- 一维无限深势阱、有限势阱、势垒、谐振子。
- 需要归一化、边界条件、节点数或简并度判断。

### 建模步骤

1. 声明单位制、单粒子、非相对论；写出定态方程：

$$
\left[-\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)\right]\psi(x) = E\psi(x)
$$

2. 按势能分区求解；在势跳跃处用边界条件：$\psi$ 连续，$V$ 有限时 $\psi'$ 连续；无限高墙处 $\psi=0$。
3. 由边界条件得量子化条件；束缚态要求 $E<V(\infty)$，散射态 $E>V(\infty)$ 为连续谱。
4. 归一化：$\int_{-\infty}^{+\infty}|\psi|^2\,dx = 1$；多态还核对正交性。
5. 概率诠释：$|\psi(x)|^2$ 为概率密度；定态概率密度不显含时间。

### 验证组合

推荐最小充分组合：F + B + J；J 为本域必做；按需再加 E 或 D。

### 必须检查的适用条件

- 非相对论单粒子；$V$ 与时间无关才可分离出定态 $\psi(x)e^{-iEt/\hbar}$。
- 束缚态波函数平方可积；散射态用概率流而非归一化到 1。
- 哈密顿量为厄米算符，本征值为实数；不同本征值的本征函数正交。
- 一维束缚态无简并（忽略自旋）；节点定理：第 $n$ 个激发态有 $n$ 个节点。

### 常见错误

| 错误 | 正确 |
|---|---|
| 无限深势阱边界只写 $\psi'$ 连续 | 无限墙处 $\psi=0$，$\psi'$ 不连续 |
| 忘归一化 | 束缚态必须 $\int|\psi|^2=1$ |
| 把 $\psi$ 本身当概率 | 概率密度是 $|\psi|^2$ |
| 把能量 $E$ 与角频率混淆 | $E=\hbar\omega$；对周期过程才用 $\omega$ |
| 有限势垒边界少写透射/反射系数 | 保留入射/反射/透射三个分区并核对概率流守恒 |
| 混用 $E=h\nu$ 与 $E=\hbar\omega$ | $\hbar\omega=h\nu$，二者同一能量 |

## 2. 算符与对易关系

### 识别特征

- 问可观测量的算符、对易关系、不确定性关系、厄米性。
- 升降算符构造谐振子谱。

### 建模步骤

1. 写出位置、动量算符：$\hat x=x$，$\hat p=-i\hbar\frac{d}{dx}$。
2. 对任意可微试探函数 $f$ 展开对易子：

$$
[\hat x,\hat p]f = \hat x\hat p f - \hat p\hat x f = i\hbar f
$$

3. 核对厄米性：$\langle\psi|\hat A\phi\rangle=\langle\hat A\psi|\phi\rangle$；本征值为实、不同本征值本征态正交。
4. 不确定性关系：

$$
\Delta A\,\Delta B \ge \frac{1}{2}\left|\langle[\hat A,\hat B]\rangle\right|
$$

5. 谐振子升降算符：

$$
\hat a=\sqrt{\frac{m\omega}{2\hbar}}\left(\hat x+\frac{i\hat p}{m\omega}\right), \qquad
[\hat a,\hat a^\dagger]=1, \qquad
\hat H=\hbar\omega\left(\hat a^\dagger\hat a+\frac12\right)
$$

### 验证组合

推荐最小充分组合：F + B + J；J 为本域必做；按需再加 E 或 D。

### 必须检查的适用条件

- 可观测量对应厄米算符；非厄米算符（如 $\hat a$）不是可观测量的直接对应。
- 算符顺序不可交换；展开对易子必须保留作用顺序。
- 不确定性关系适用于任意两可观测量；等号只在相干态等特定态达到。

### 常见错误

| 错误 | 正确 |
|---|---|
| $\hat p=+i\hbar\,d/dx$ | $\hat p=-i\hbar\,d/dx$ |
| 交换算符顺序 | 展开 $[\hat A,\hat B]$ 时逐项保持顺序 |
| 把非厄米算符当可观测量 | 先核对厄米性 |
| $[\hat a,\hat a^\dagger]=0$ | $=1$ |
| 直接写 $[\hat x,\hat p]$ 等于某数而不作用到函数 | 对任意试探函数展开证明 |

## 3. 角动量与氢原子

### 识别特征

- 球对称势、角动量本征值、磁量子数、氢原子/类氢原子能级。

### 建模步骤

1. 角动量本征方程：

$$
\hat L^2 Y_{lm}=\hbar^2 l(l+1)Y_{lm}, \qquad
\hat L_z Y_{lm}=m\hbar Y_{lm}, \qquad m=-l,\ldots,l
$$

2. 球对称势分离变量：$\psi=R_{nl}(r)Y_{lm}(\theta,\phi)$。
3. 径向方程解氢原子能级：

$$
E_n=-\frac{\mu e^4}{2(4\pi\varepsilon_0)^2\hbar^2}\frac{1}{n^2}=-\frac{13.6\,\mathrm{eV}}{n^2}
$$

4. 玻尔半径 $a_0=\frac{4\pi\varepsilon_0\hbar^2}{m_e e^2}=0.529\,\mathrm{\AA}$。
5. 简并度：给定 $n$ 有 $n^2$ 个态（忽略自旋；计入自旋为 $2n^2$）。

### 验证组合

推荐最小充分组合：F + B + J；J 为本域必做；按需再加 E 或 D。

### 必须检查的适用条件

- 非相对论、无自旋-轨道耦合、无外场；**本模块氢原子结果均为非相对论近似，忽略精细结构、超精细结构与兰姆位移**；精细结构与塞曼效应不在本模块范围。
- 氢原子公式中 $\mu$ 为约化质量；对电子绕质子 $\mu\approx m_e$。
- 束缚态要求 $E<0$；$n=1$ 为基态。

### 常见错误

| 错误 | 正确 |
|---|---|
| 用电子质量代替约化质量且不说明 | 写约化质量 $\mu$；无限核近似时声明 |
| 忘记 $n^2$ 简并 | 忽略自旋时 $n^2$，计入自旋 $2n^2$ |
| 把 $E_n\propto -1/n$ | $-1/n^2$ |
| 磁量子数超出 $[-l,l]$ | $m=-l,\ldots,l$ 共 $2l+1$ 个 |
| 忽略波函数归一化/角向归一化 | $Y_{lm}$ 与 $R_{nl}$ 分别归一 |

## 4. 非简并微扰论入门

### 识别特征

- 哈密顿量 $H=H_0+\lambda V'$，$H_0$ 谱已知且所考虑能级非简并；$\lambda V'$ 为小扰动。
- 待求量：能级与态的一级/二级修正。

### 建模步骤

1. 写出 $H_0$ 的本征方程 $H_0|n^{(0)}\rangle=E_n^{(0)}|n^{(0)}\rangle$；确认 $|n^{(0)}\rangle$ 非简并，并声明微扰小（$|\langle m^{(0)}|V'|n^{(0)}\rangle|$ 远小于能级间距）。
2. 一级能量修正：

$$
E_n^{(1)}=\langle n^{(0)}|V'|n^{(0)}\rangle
$$

3. 二级能量修正：

$$
E_n^{(2)}=\sum_{m\neq n}\frac{|\langle m^{(0)}|V'|n^{(0)}\rangle|^2}{E_n^{(0)}-E_m^{(0)}}
$$

4. 一级态修正：

$$
|n^{(1)}\rangle=\sum_{m\neq n}\frac{\langle m^{(0)}|V'|n^{(0)}\rangle}{E_n^{(0)}-E_m^{(0)}}|m^{(0)}\rangle
$$

### 验证组合

推荐最小充分组合：F + B + J；按需再加 E 或 I。

### 必须检查的适用条件

- 所考虑能级非简并；简并微扰需另建简并子空间对角化，不在本模块范围。
- 微扰矩阵元有限，分母 $E_n^{(0)}-E_m^{(0)}\neq0$。
- 收敛条件 $|\langle m^{(0)}|V'|n^{(0)}\rangle|\ll|E_n^{(0)}-E_m^{(0)}|$；不满足时如实声明微扰论不适用。
- $H_0$ 与 $V'$ 均为厄米算符，能量修正为实数。

### 常见错误

| 错误 | 正确 |
|---|---|
| 简并能级直接套非简并公式 | 先建简并子空间再对角化 |
| 分母为零仍硬算 | 检查 $E_n^{(0)}\neq E_m^{(0)}$ |
| 二级修正漏平方绝对值 | 用 $|\langle m^{(0)}|V'|n^{(0)}\rangle|^2$ |
| 加态修正后忘记整体归一化 | 修正后重新归一化 |

## 5. 自旋 1/2 入门

### 识别特征

- 含自旋的可观测量：$S^2$、$S_z$、泡利矩阵；自旋单态/三重态组合。
- 电子自旋 1/2，$S_z$ 本征值为 $+\hbar/2$ 与 $-\hbar/2$。

### 建模步骤

1. 自旋算符 $\mathbf S=\frac{\hbar}{2}\boldsymbol\sigma$，泡利矩阵：

$$
\sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
\sigma_y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\qquad
\sigma_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}
$$

2. 本征态：$S_z|\uparrow\rangle=+\frac{\hbar}{2}|\uparrow\rangle$、$S_z|\downarrow\rangle=-\frac{\hbar}{2}|\downarrow\rangle$；$S^2=s(s+1)\hbar^2$，$s=1/2$。
3. 对易与恒等式：$[S_x,S_y]=i\hbar S_z$（循环）；$\sigma_i^2=I$；$i\neq j$ 时 $\{\sigma_i,\sigma_j\}=0$。
4. 两粒子自旋组合：单态 $|00\rangle=\frac{1}{\sqrt2}(|\uparrow\downarrow\rangle-|\downarrow\uparrow\rangle)$（$S=0$）；三重态 $|11\rangle=|\uparrow\uparrow\rangle$ 等（$S=1$）。

### 验证组合

推荐最小充分组合：F + B + J；按需再加 E。

### 必须检查的适用条件

- 非相对论；自旋轨道耦合、精细结构不在本模块范围。
- 泡利矩阵作用于自旋空间，与轨道角动量算符属于不同子空间。
- 单态/三重态分解时用 $\mathbf S=\mathbf S_1+\mathbf S_2$ 与耦合系数核对。

### 常见错误

| 错误 | 正确 |
|---|---|
| 把自旋角动量当轨道角动量 | 自旋是内禀自由度，$S^2=s(s+1)\hbar^2$ |
| 泡利矩阵迹/行列式记错 | $\mathrm{tr}\,\sigma_i=0$、$\det\sigma_i=-1$、$\sigma_i^2=I$ |
| 自旋对易符号写反 | $[S_x,S_y]=i\hbar S_z$ 循环 |
| 单态与三重态混淆 | 单态反对称、三重态对称 |

## 6. 常用公式与陷阱 (Formulas & Traps)

### 公式速查

定态薛定谔方程：

$$
\hat H\psi=E\psi, \qquad
\hat H=-\frac{\hbar^2}{2m}\nabla^2+V
$$

对易与不确定关系：

$$
[\hat x,\hat p]=i\hbar, \qquad
\Delta x\,\Delta p\ge\frac{\hbar}{2}
$$

一维无限深势阱（$0<x<L$）：

$$
\psi_n=\sqrt{\frac{2}{L}}\sin\frac{n\pi x}{L}, \qquad
E_n=\frac{n^2\pi^2\hbar^2}{2mL^2}
$$

谐振子：

$$
E_n=\left(n+\frac12\right)\hbar\omega, \qquad
\psi_0=\left(\frac{m\omega}{\pi\hbar}\right)^{1/4}e^{-m\omega x^2/(2\hbar)}
$$

角动量与氢原子：

$$
\hat L^2|l,m\rangle=\hbar^2 l(l+1)|l,m\rangle, \qquad
E_n=-\frac{13.6\,\mathrm{eV}}{n^2}
$$

微扰论（非简并）：

$$
E_n^{(1)}=\langle n^{(0)}|V'|n^{(0)}\rangle, \qquad
E_n^{(2)}=\sum_{m\neq n}\frac{|\langle m^{(0)}|V'|n^{(0)}\rangle|^2}{E_n^{(0)}-E_m^{(0)}}
$$

自旋 1/2：

$$
\mathbf S=\frac{\hbar}{2}\boldsymbol\sigma, \qquad
[S_x,S_y]=i\hbar S_z, \qquad
S_z|\uparrow\rangle=\frac{\hbar}{2}|\uparrow\rangle
$$


### 跨域陷阱

跨域共性陷阱（单位遗漏等）见 `error_prevention.md` §0–§3。本模块**特有**陷阱（$\hat p$ 符号、算符顺序、归一化、$h\nu$ vs $\hbar\omega$、微扰收敛性、自旋与轨道区分）已列入各节常见错误表，此处不重复。
