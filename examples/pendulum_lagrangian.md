# 例题：平面单摆（拉格朗日方法，模板 A 完整示范）

> 本例题展示标准解答模板（Template A）与验证引擎（F/D/B/C/L/E/I）的完整用法。所有公式可直接粘贴进 Overleaf 编译。

## 题意与图景

- **系统**：质量 $m$ 的质点，系于长度 $l$ 的无质量刚性轻杆一端；杆另一端固定于 $O$ 点，质点在竖直平面内摆动。
- **约束**：杆长固定（完整、定常约束）；无摩擦（理想约束）。自由度 $= 1$。
- **坐标**：取广义坐标 $\theta$，为杆与竖直向下方向的夹角。单位制：SI。
- **已知**：$m$、$l$、$g$。**待求**：小角度下的运动方程与摆动周期。

## 建模

- **方法选择**：约束完整且理想、非保守力不存在，故用拉格朗日方法（比牛顿方法少一个约束力变量）。
- **动能与势能**：

$$
T = \frac{1}{2} m l^2 \dot{\theta}^2, \qquad
V = mgl(1 - \cos\theta)
$$

（势能零点取最低点 $\theta=0$。）

- **拉格朗日量**：

$$
L = T - V = \frac{1}{2} m l^2 \dot{\theta}^2 - mgl(1 - \cos\theta)
$$

- **适用条件声明**：理想约束（无耗散）→ 能量守恒可用；约束定常 → 拉格朗日量不显含时间。

## 推导

由欧拉-拉格朗日方程：

$$
\frac{d}{dt}\frac{\partial L}{\partial \dot{\theta}} - \frac{\partial L}{\partial \theta} = 0
$$

计算各项：

$$
\frac{\partial L}{\partial \dot{\theta}} = m l^2 \dot{\theta}, \qquad
\frac{d}{dt}\frac{\partial L}{\partial \dot{\theta}} = m l^2 \ddot{\theta}
$$

$$
\frac{\partial L}{\partial \theta} = -mgl \sin\theta
$$

代入得：

$$
m l^2 \ddot{\theta} + mgl \sin\theta = 0
\quad\Longrightarrow\quad
\ddot{\theta} + \frac{g}{l} \sin\theta = 0
$$

**小角近似**（$\theta \ll 1$，弧度）：$\sin\theta \approx \theta$：

$$
\ddot{\theta} + \omega^2 \theta = 0, \qquad \omega = \sqrt{\frac{g}{l}}
$$

通解：

$$
\theta(t) = A\cos(\omega t + \varphi)
$$

周期：

$$
T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{l}{g}}
$$

## 验算

- **① F 量纲**：$[\omega] = [g/l]^{1/2} = (LT^{-2}/L)^{1/2} = T^{-1}$，角频率量纲正确；$[2\pi\sqrt{l/g}] = (L/(LT^{-2}))^{1/2} = T$，周期量纲正确。**PASS**。
- **② L 极限/特例**：$\theta \to 0$ 时 $\sin\theta \to \theta$，完整方程退化为线性谐振方程，与已知结果一致；$\omega \to 0$ 对应 $g \to 0$ 或 $l \to \infty$（无回复力/摆长无限），极限合理。**PASS**。
- **③ B 回代**：将 $\theta(t) = A\cos(\omega t + \varphi)$ 代入线性化方程：$\ddot{\theta} = -\omega^2 \theta$，得 $-\omega^2\theta + \omega^2\theta = 0$，恒等成立。**PASS**。
- **④ C 守恒量**：能量 $E = T + V = \frac{1}{2}ml^2\dot{\theta}^2 + mgl(1-\cos\theta)$。取两组不同时刻状态（如 $\theta = 0, \dot\theta = A\omega$ 与 $\theta = A, \dot\theta = 0$），$E$ 均为 $\frac{1}{2}ml^2 A^2 \omega^2 = \frac{1}{2}mgl A^2$（用 $\omega^2 = g/l$），守恒成立。**PASS**。
- **⑤ E 数值抽样**（可选加分项）：取 $m = 1\,\mathrm{kg}$，$l = 1\,\mathrm{m}$，$g = 9.8\,\mathrm{m/s^2}$：$\omega = \sqrt{9.8} \approx 3.13\,\mathrm{s^{-1}}$，$T \approx 2.01\,\mathrm{s}$；代入 $\ddot{\theta} + (g/l)\sin\theta = 0$ 数值两端一致（误差 $\sim 10^{-3}$ 量级，来自小角近似）。**PASS**。
- **⑥ I 独立方法**（可选加分项）：用能量守恒 $E = \frac{1}{2}ml^2\dot{\theta}^2 + mgl(1-\cos\theta)$ 求 $\dot\theta(\theta)$ 后对 $\theta$ 积分，小角下得同一周期 $2\pi\sqrt{l/g}$。**PASS**。

验算：`①②③④，FAIL 0 项（⑤⑥ 已加做）`

## 答案

**运动方程：$\ddot{\theta} + \dfrac{g}{l}\sin\theta = 0$；小角近似下 $\ddot{\theta} + \dfrac{g}{l}\theta = 0$，角频率 $\omega = \sqrt{\dfrac{g}{l}}$，周期 $T = 2\pi\sqrt{\dfrac{l}{g}}$。**

适用条件：$\theta \ll 1$（弧度）、理想定常约束、无耗散。

## 易错点

1. $L = T - V$ 符号写反（写成 $T + V$ 是最常见错误）；检查 $\partial L/\partial\dot\theta$ 应给出 $ml^2\dot\theta$ 而非 $-ml^2\dot\theta$。
2. 把角频率 $\omega$ 误当作角速度 $\dot\theta$：$\omega = \sqrt{g/l}$ 是常数，$\dot\theta$ 是运动学变量。
3. 势能零点可任意选择（E-L 方程不变），但须全文一致。
4. 大振幅时周期有修正 $T = 2\pi\sqrt{l/g}\,(1 + \theta_0^2/16 + \cdots)$，小角公式不可直接外推。
