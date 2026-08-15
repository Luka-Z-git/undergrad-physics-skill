# 例题：两种线性电介质分界面的电场折射（边界条件，模板 A）

## 题意与图景

- **系统**：两种线性、各向同性电介质（介电常数 $\varepsilon_1,\varepsilon_2$）的平面分界面，无自由面电荷。
- **约束**：静电场、无自由面电荷、界面无限大；场线在界面两侧分别与法线成 $\theta_1,\theta_2$。
- **坐标**：取界面法线 $\hat{\mathbf n}$ 从介质 1 指向介质 2；单位制：SI。
- **已知**：$\varepsilon_1,\varepsilon_2,\theta_1,E_1$。**待求**：$\theta_2$ 与 $E_2$ 的大小。

## 建模

- **方法选择**：用电场边界条件——切向 $\mathbf E$ 连续、无自由面电荷时法向 $\mathbf D$ 连续。
- **边界条件**：

$$
E_1\sin\theta_1 = E_2\sin\theta_2,\qquad
\varepsilon_1 E_1\cos\theta_1 = \varepsilon_2 E_2\cos\theta_2
$$

- **适用条件声明**：线性各向同性介质、静电场、分界面无自由面电荷；铁磁材料与非线性介质不在本技能范围。

## 推导

两式相除：

$$
\frac{\tan\theta_2}{\varepsilon_2} = \frac{\tan\theta_1}{\varepsilon_1}
\quad\Longrightarrow\quad
\tan\theta_2 = \frac{\varepsilon_2}{\varepsilon_1}\tan\theta_1
$$

由切向条件：

$$
E_2 = E_1\frac{\sin\theta_1}{\sin\theta_2}
$$

（法向条件给出同一结果。）

## 验算

- **① F 量纲**：$\tan\theta$ 无量纲；$\varepsilon_2/\varepsilon_1$ 无量纲；$E_2$ 与 $E_1$ 同量纲 $\mathrm{V/m}$。**PASS**。
- **② L 极限/特例**：$\varepsilon_2=\varepsilon_1$ 时 $\theta_2=\theta_1$、$E_2=E_1$（均匀介质）；$\theta_1=0$（垂直入射）时 $\theta_2=0$；$\varepsilon_2\to\infty$ 时 $\theta_2\to90^\circ$，场在介质 2 中趋于平行界面（导体极限）。**PASS**。
- **③ B 回代**：把 $\tan\theta_2=(\varepsilon_2/\varepsilon_1)\tan\theta_1$ 与 $E_2=E_1\sin\theta_1/\sin\theta_2$ 代回两条边界条件，两边恒等。**PASS**。
- **④ C 守恒量**：N/A（静电场边界问题，无机械守恒量；能量密度 $u=\frac12\varepsilon E^2$ 可作交叉核对，本域非必查）。
- **⑤ E 数值抽样**：$\varepsilon_1=\varepsilon_0$、$\varepsilon_2=4\varepsilon_0$、$\theta_1=30^\circ$：$\tan\theta_2=4\tan30^\circ\approx2.309$，$\theta_2\approx66.6^\circ$；代回 $E_1\sin\theta_1=E_2\sin\theta_2$ 与 $\varepsilon_1E_1\cos\theta_1=\varepsilon_2E_2\cos\theta_2$，两式数值一致。**PASS**。

验算摘要：`已通过 ①②③④，FAIL 0 项（⑤ 已加做）`

## 答案

**$\tan\theta_2=\dfrac{\varepsilon_2}{\varepsilon_1}\tan\theta_1$，$E_2=E_1\dfrac{\sin\theta_1}{\sin\theta_2}$；无自由面电荷时分界面两侧切向 $\mathbf E$ 连续、法向 $\mathbf D$ 连续。**

适用条件：线性各向同性介质、静电场、分界面无自由面电荷。

## 易错点

1. 法向连续的是 $\mathbf D$ 而不是 $\mathbf E$；不能把 $\varepsilon_1E_{1\perp}=\varepsilon_2E_{2\perp}$ 误写成 $E$ 连续。
2. 有自由面电荷 $\sigma$ 时法向条件为 $D_{2\perp}-D_{1\perp}=\sigma$，本题结论不能直接外推。
3. 角度必须相对法线定义；相对界面定义会改变公式形式。
