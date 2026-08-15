# 例题：旋转圆环上的珠子（非惯性系平衡，模板 A）

## 题意与图景

光滑圆环（半径 $R$）绕竖直直径以恒定角速度 $\omega$ 旋转，环上套一小珠（质量 $m$，可沿环自由滑动）。求珠子相对环的平衡角 $\theta$（自最低点起算）。已知量：$m,\ R,\ \omega,\ g$；待求量：平衡角 $\theta$。

## 建模

- 选方程体系：**非惯性系（随环旋转参考系）**——在旋转系中珠子静止，补惯性离心力后列平衡方程。理由：旋转系中珠子相对环静止，问题化为静力平衡。
- 适用条件：旋转参考系角速度恒定（$\dot{\boldsymbol\Omega}=0$，无欧拉力）；珠子在环上光滑滑动（无切向摩擦）；$\theta$ 自竖直向下方向（最低点）起算。

## 推导

1. 珠子到转轴（竖直直径）的垂直距离为 $R\sin\theta$，旋转系中的离心力大小为 $m\omega^2 R\sin\theta$，方向水平向外。

2. 珠子受重力 $mg$（竖直向下）、环的法向反力 $N$（沿径向）、离心力（水平向外）。切向（沿环方向）平衡：

$$
mg\sin\theta = m\omega^2 R\sin\theta\cos\theta
$$

3. 消去 $m\sin\theta$：

$$
\sin\theta\left(g-\omega^2 R\cos\theta\right)=0
$$

解为：$\sin\theta=0$（$\theta=0$，最低点，恒为平衡）或

$$
\cos\theta = \frac{g}{\omega^2 R}
$$

仅当 $\omega^2 R > g$ 时 $\cos\theta<1$，存在非平凡平衡角；此时珠子偏离最低点、向两侧升起。

## 验算

- **① F 量纲**：$\cos\theta=\dfrac{g}{\omega^2 R}$ 右侧 $\dfrac{LT^{-2}}{T^{-2}\cdot L}=1$ 无量纲。**PASS**。
- **② L 极限/特例**：$\omega\to0$（不旋转）时无离心力，仅 $\theta=0$ 平衡，珠子停在最低点 **PASS**；$\omega\to\infty$ 时 $\cos\theta\to0\Rightarrow\theta\to\tfrac\pi2$，珠子升至赤道平面。**PASS**。
- **③ B 回代**：把 $\cos\theta=g/(\omega^2 R)$ 代回切向平衡 $mg\sin\theta=m\omega^2R\sin\theta\cos\theta$，两边恒等。**PASS**。
- **④ C 守恒量**：N/A（静平衡，无运动；若讨论稳定性需二阶分析，此处不展开）。
- **⑤ E 数值抽样**：$R=1.0,\ \omega=4.0,\ g=9.8$ → $\cos\theta=9.8/16=0.6125$，$\theta\approx52.3^\circ$；介于 $0$ 与 $90^\circ$ 之间，合理。**PASS**。

验算：`①②③⑤，④ N/A（静平衡），FAIL 0 项`

## 答案

**平衡角满足 $\sin\theta=0$（最低点）或 $\cos\theta=\dfrac{g}{\omega^2 R}$（当 $\omega^2R>g$）；后者对应的稳定平衡角 $\theta=\arccos\dfrac{g}{\omega^2 R}$（无量纲，弧度）。**

适用条件：$\omega$ 恒定、环面光滑、$\theta$ 自最低点起算。

## 易错点

1. 把离心力当真实力：它只出现在旋转参考系中，大小为 $m\omega^2R\sin\theta$（到转轴距离为 $R\sin\theta$，不是 $R$）。
2. 漏掉 $\theta=0$ 这个恒成立的平衡解，或未指出 $\omega^2R>g$ 才有非平凡解。
