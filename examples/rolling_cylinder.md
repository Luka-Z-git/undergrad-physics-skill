# 例题：刚体纯滚动圆柱下滑（模板 A）

## 题意与图景

实心圆柱（质量 $m$、半径 $R$，绕质心轴转动惯量 $I=\tfrac12 mR^2$）在倾角 $\theta$ 的斜面上从静止开始**纯滚动**下滑，下滑竖直高度 $h$。求质心加速度 $a_C$ 与末速度 $v_C$。已知量：$m,\ R,\ \theta,\ h,\ g$；待求量：$a_C,\ v_C$。

## 建模

- 选方程体系：**刚体平面运动**——质心平动方程 + 绕质心转动方程，配合纯滚动约束 $\dot x = R\dot\theta$（无滑动）。理由：需同时处理平动与转动，且约束为速度约束。
- 适用条件：斜面与圆柱间为**静摩擦**且未达上限（纯滚动成立）；接触点瞬时无相对滑动，静摩擦不做功，机械能守恒；斜面固定于惯性系。

## 推导

1. 沿斜面方向（取下滑为正）与垂直斜面方向受力，静摩擦力 $f$ 沿斜面向上。质心平动：

$$
m a_C = mg\sin\theta - f
$$

2. 绕质心转动方程（静摩擦为唯一力矩）：

$$
I\alpha = f R,\qquad I=\tfrac12 mR^2
$$

3. 纯滚动约束 $a_C = R\alpha$，代入消去 $f$ 与 $\alpha$：

$$
f = \frac{I a_C}{R^2}=\frac12 m a_C
\quad\Rightarrow\quad
m a_C = mg\sin\theta - \frac12 m a_C
\quad\Rightarrow\quad
a_C = \frac23 g\sin\theta
$$

4. 由能量守恒求末速度（静摩擦不做功，只有重力做功）：

$$
mgh = \frac12 mv_C^2 + \frac12 I\omega^2
= \frac12 mv_C^2 + \frac12\left(\tfrac12 mR^2\right)\left(\frac{v_C}{R}\right)^2
= \frac34 mv_C^2
$$

$$
v_C = \sqrt{\frac{4gh}{3}}
$$

## 验算

- **① F 量纲**：$a_C=\frac23 g\sin\theta$ 量纲 $LT^{-2}$ **PASS**；$v_C=\sqrt{4gh/3}$ 量纲 $(L\,T^{-2}\cdot L)^{1/2}=LT^{-1}$。**PASS**。
- **② L 极限/特例**：$I\to0$（质块无转动）时 $a_C\to g\sin\theta$、$v_C\to\sqrt{2gh}$，退化为质点沿光滑面下滑 **PASS**；$\theta\to0$ 时 $a_C\to0$。**PASS**。
- **③ B 回代**：把 $a_C=\frac23 g\sin\theta$ 代回 $ma_C=mg\sin\theta-f$ 与 $fR=I\alpha,\ a_C=R\alpha$ 得 $f=\frac13 mg\sin\theta$，三式自洽恒等。**PASS**。
- **④ C 守恒量**：纯滚动静摩擦不做功、重力保守，$E=T+V$ 守恒；末态 $E=\frac34 mv_C^2=mgh$ 与初态一致。**PASS**。
- **⑤ E 数值抽样**：$g=9.8,\ \theta=30^\circ,\ h=1.0$ → $a_C=3.27\ \mathrm{m/s^2}$，$v_C=\sqrt{4\cdot9.8/3}=3.61\ \mathrm{m/s}$，数量级合理。**PASS**。

验算：`①②③④⑤，FAIL 0 项`

## 答案

**质心加速度 $a_C = \dfrac23 g\sin\theta$；下滑高度 $h$ 后末速度 $v_C = \sqrt{\dfrac{4gh}{3}}$（单位为 $\mathrm{m/s^2}$、$\mathrm{m/s}$）。**

适用条件：纯滚动（$f\le\mu_s N$）、实心圆柱（$I=\tfrac12 mR^2$）、静止释放。

## 易错点

1. 动能漏转动项：$T$ 须含 $\tfrac12 I\omega^2$，否则得到 $v=\sqrt{2gh}$ 而非 $\sqrt{4gh/3}$。
2. 纯滚动默认 $f=\mu_s N$：静摩擦力由约束决定（此处 $f=\tfrac13 mg\sin\theta$），只需检验未超上限。
