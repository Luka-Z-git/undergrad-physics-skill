# 例题：耦合振子的简正模式（模板 A 完整示范 + J 一致性必做）

> 本例题展示小振动领域的标准解答流程，重点演示 J 一致性检查（特征值回代、M-正交）在本域的必做用法。所有公式可直接粘贴进 Overleaf 编译。

## 题意与图景

- **系统**：两个质量均为 $m$ 的物块在水平光滑轨道上振动；中间用劲度系数 $k_c$ 的弹簧相连，两端再各用劲度系数 $k$ 的弹簧连接固定墙。
- **约束**：轨道光滑（无摩擦）；弹簧为轻弹簧（质量不计）；运动沿直线（一维）。自由度 $= 2$。
- **坐标**：以两物块平衡位置为原点，取位移 $\xi_1, \xi_2$（向右为正）。单位制：SI。
- **已知**：$m$、$k$、$k_c$。**待求**：简正频率 $\omega_1, \omega_2$ 与简正模式。

## 建模

- **方法选择**：平衡点附近小幅运动，多自由度耦合系统，故用小振动线性化方法（§5）。
- **动能与势能**：

$$
T = \frac{1}{2}m(\dot\xi_1^2 + \dot\xi_2^2), \qquad
V = \frac{1}{2}k\xi_1^2 + \frac{1}{2}k\xi_2^2 + \frac{1}{2}k_c(\xi_1 - \xi_2)^2
$$

- **质量矩阵与刚度矩阵**：

$$
M = m\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \qquad
K = \begin{pmatrix} k+k_c & -k_c \\ -k_c & k+k_c \end{pmatrix}
$$

- **适用条件声明**：小幅运动（线性化有效）；弹簧服从胡克定律；无耗散 → 能量守恒可用。

## 推导

矩阵运动方程 $M\ddot{\boldsymbol\xi} + K\boldsymbol\xi = 0$。令 $\boldsymbol\xi = \mathbf A e^{i\omega t}$，得特征方程：

$$
\det(K - \omega^2 M) = \det\begin{pmatrix} k+k_c - m\omega^2 & -k_c \\ -k_c & k+k_c - m\omega^2 \end{pmatrix} = 0
$$

展开：

$$
(k+k_c - m\omega^2)^2 - k_c^2 = 0 \quad\Longrightarrow\quad k+k_c - m\omega^2 = \pm k_c
$$

两支解：

$$
\omega_1^2 = \frac{k}{m}, \qquad \omega_2^2 = \frac{k + 2k_c}{m}
$$

$\omega^2 > 0$（稳定平衡）。对应特征向量（取首元归一）：

- $\omega_1$：$(K - \omega_1^2 M)\mathbf A_1 = \begin{pmatrix} k_c & -k_c \\ -k_c & k_c \end{pmatrix}\begin{pmatrix} 1 \\ a \end{pmatrix} = 0$ → $a = 1$ → **同相模式** $\mathbf A_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$
- $\omega_2$：$(K - \omega_2^2 M)\mathbf A_2 = \begin{pmatrix} -k_c & -k_c \\ -k_c & -k_c \end{pmatrix}\begin{pmatrix} 1 \\ b \end{pmatrix} = 0$ → $b = -1$ → **反相模式** $\mathbf A_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$

正常坐标（$M$-正交归一，$M=mI$ 时即普通正交归一）：

$$
\eta_1 = \frac{\xi_1 + \xi_2}{\sqrt{2}}, \qquad \eta_2 = \frac{\xi_1 - \xi_2}{\sqrt{2}}
$$

通解：

$$
\begin{pmatrix} \xi_1(t) \\ \xi_2(t) \end{pmatrix} = C_1\begin{pmatrix} 1 \\ 1 \end{pmatrix}\cos(\omega_1 t + \varphi_1) + C_2\begin{pmatrix} 1 \\ -1 \end{pmatrix}\cos(\omega_2 t + \varphi_2)
$$

## 验算

- **① F 量纲**：$[k/m] = [k_c/m] = MT^{-2}/M = T^{-2}$，$\omega$ 量纲 $T^{-1}$ 正确。**PASS**。
- **② L 极限/特例**：$k_c \to 0$ 时 $\omega_1^2 = \omega_2^2 = k/m$，退化为两个独立振子（耦合弹簧消失），符合物理直觉。$k \to 0$ 时 $\omega_1 \to 0$（整体平动零频模式）、$\omega_2^2 = 2k_c/m$（相对振动），合理。**PASS**。
- **③ B 回代**：将 $\omega_1^2 = k/m$ 代回 $\det(K-\omega^2 M)=0$：$(k+k_c-k)(k+k_c-k)-k_c^2 = k_c^2-k_c^2=0$；$\omega_2^2=(k+2k_c)/m$ 代回：$(k+k_c-k-2k_c)(k+k_c-k-2k_c)-k_c^2 = (-k_c)^2-k_c^2=0$。均恒等。**PASS**。
- **④ C 守恒量**：无耗散且 $K$ 定常，$E=T+V$ 守恒。取同相模式初态 $(\xi_1,\xi_2)=(A,A), (\dot\xi_1,\dot\xi_2)=(0,0)$：$E = 0 + \frac12(2kA^2) = kA^2$。四分之一周期后 $(\xi_1,\xi_2)=(0,0), (\dot\xi_1,\dot\xi_2)=(-\omega_1 A,-\omega_1 A)$：$E = \frac12(2m\omega_1^2 A^2) + 0 = m(k/m)A^2 = kA^2$。守恒成立。**PASS**。
- **⑦ J 一致性（本域必做）**：
  - 特征值回代：$(K-\omega_1^2 M)\mathbf A_1 = \begin{pmatrix} k_c & -k_c \\ -k_c & k_c \end{pmatrix}\begin{pmatrix} 1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$，成立；$(K-\omega_2^2 M)\mathbf A_2 = \begin{pmatrix} -k_c & -k_c \\ -k_c & -k_c \end{pmatrix}\begin{pmatrix} 1 \\ -1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$，成立。**PASS**。
  - M-正交：$\mathbf A_1^T M \mathbf A_2 = m(1\cdot 1 + 1\cdot(-1)) = 0$，两简正模式 $M$-正交。**PASS**。

验算：`①②③④⑦，FAIL 0 项`

## 答案

**简正频率：$\omega_1 = \sqrt{\dfrac{k}{m}}$（同相模式），$\omega_2 = \sqrt{\dfrac{k+2k_c}{m}}$（反相模式）；简正模式：同相 $(1,1)$、反相 $(1,-1)$，$M$-正交归一正常坐标 $\eta_1 = (\xi_1+\xi_2)/\sqrt{2},\ \eta_2 = (\xi_1-\xi_2)/\sqrt{2}$。**

适用条件：小幅运动（线性化）、无耗散、弹簧服从胡克定律。

## 易错点

1. 特征方程用 $\det(K-\omega^2 I)$ 而非 $\det(K-\omega^2 M)$（漏质量矩阵，当 $m\neq 1$ 时结果错误）。
2. 刚度矩阵耦合元符号写错（应为 $-k_c$；写成 $+k_c$ 导致特征值错误）。
3. 把角频率 $\omega$ 与频率 $f$ 混淆（$\omega = 2\pi f$，答案中注明单位 $\mathrm{rad/s}$）。
4. 简正模式未做 $M$-正交核对（本域 J 必查项，遗漏按未完成处理）。
