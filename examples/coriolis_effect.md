# 例题：匀角速度转盘上的径向运动（科里奥利力，模板 A）

## 题意与图景

- **系统**：水平圆盘以恒定角速度 $\omega$ 绕竖直轴旋转；质量 $m$ 的质点在盘面上以相对速度 $v$ 沿半径向外匀速运动，忽略摩擦。
- **约束**：非惯性参考系（随盘旋转）；$\omega$ 恒定；质点相对盘面沿径向。
- **坐标**：柱坐标 $(\rho,\varphi)$ 固定在盘上，$\hat{\boldsymbol\rho}$ 沿径向向外；单位制：SI。
- **已知**：$m$、$\omega$、$v$。**待求**：科里奥利力 $\mathbf F_C$ 的大小与方向、横向加速度与 $t$ 时刻横向位移。

## 建模

- **方法选择**：在旋转参考系中，相对运动方程除真实力外还须加入惯性力；科里奥利力项为 $-2m\boldsymbol\omega\times\mathbf v$。
- **运动方程**（无摩擦、真实力只有约束力时）：

$$
m\mathbf a' = -2m\boldsymbol\omega\times\mathbf v + m\omega^2\boldsymbol\rho
$$

- **适用条件声明**：非惯性系、$\boldsymbol\omega$ 恒定、质点相对盘面运动、忽略摩擦；$v\ll c$。

## 推导

取 $\boldsymbol\omega=\omega\hat{\mathbf z}$、$\mathbf v=v\hat{\boldsymbol\rho}$：

$$
\boldsymbol\omega\times\mathbf v = \omega v\,(\hat{\mathbf z}\times\hat{\boldsymbol\rho}) = \omega v\,\hat{\boldsymbol\varphi}
$$

因此

$$
\mathbf F_C = -2m\boldsymbol\omega\times\mathbf v = -2m\omega v\,\hat{\boldsymbol\varphi}
$$

大小 $F_C=2m\omega v$，方向沿 $-\hat{\boldsymbol\varphi}$（与旋转方向相反）。横向加速度：

$$
a_\varphi = \frac{F_C}{m} = 2\omega v
$$

从 $t=0$ 开始（初始横向速度为零），横向位移：

$$
y(t)=\frac12 a_\varphi t^2=\omega v t^2
$$

离心力 $m\omega^2\rho$ 沿径向向外，不改变横向运动。

## 验算

- **① F 量纲**：$[a_\varphi]=[\omega v]=T^{-1}\cdot LT^{-1}=LT^{-2}$；$[F_C]=MLT^{-2}$；$[y]=[\omega vt^2]=L$。**PASS**。
- **② L 极限/特例**：$\omega\to0$ 或 $v\to0$ 时科里奥利力为零；$\omega$ 反向时横向偏转方向反转。**PASS**。
- **③ B 回代**：把 $y(t)=\omega v t^2$ 求二阶导得 $\ddot y=2\omega v=a_\varphi$，与 $a_\varphi=F_C/m$ 恒等；把 $F_C=2m\omega v$ 代回 $-2m\boldsymbol\omega\times\mathbf v$ 取模，结果一致。**PASS**。
- **④ C 守恒量**：N/A（非惯性系中科里奥利力垂直于相对速度、不做功；动能守恒与否由约束决定，本域不构成简单守恒量判据）。
- **⑤ E 数值抽样**：$m=1\,\mathrm{kg}$、$\omega=0.5\,\mathrm{s^{-1}}$、$v=2\,\mathrm{m/s}$：$F_C=2\,\mathrm{N}$、$a_\varphi=2\,\mathrm{m/s^2}$、$t=3\,\mathrm{s}$ 时 $y=9\,\mathrm{m}$；数值代入恒等。**PASS**。

验算摘要：`已通过 ①②③④，FAIL 0 项（⑤ 已加做）`

## 答案

**$\mathbf F_C=-2m\boldsymbol\omega\times\mathbf v$，大小 $F_C=2m\omega v$，方向垂直于 $\boldsymbol\omega$ 与 $\mathbf v$ 所在平面；横向加速度 $a_\varphi=2\omega v$，$t$ 时刻横向位移 $y(t)=\omega v t^2$。**

适用条件：匀角速度非惯性系、忽略摩擦、质点相对盘面运动。

## 易错点

1. 科里奥利力方向写反：$\mathbf F_C=-2m\boldsymbol\omega\times\mathbf v$，叉积顺序决定符号。
2. 把科里奥利力与离心力混淆：离心力沿径向向外，科里奥利力在横向。
3. 科里奥利力垂直于相对速度，不做功；它改变运动方向，不改变相对速率。
