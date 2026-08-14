# 例题：氢原子能级（玻尔模型入门推导，模板 A）

## 题意与图景

电子（电荷 $-e$、质量 $m_e$）绕质子做圆周运动，用玻尔量子化条件求氢原子能级 $E_n$、玻尔半径 $a_0$ 与基态能量。已知量：$e,\ m_e,\ \varepsilon_0,\ \hbar$；待求量：$r_n,\ E_n,\ a_0$。

## 建模

- 选方程体系：**半经典玻尔模型**——库仑力提供向心力 + 角动量量子化条件 $m_e v r=n\hbar$。理由：入门推导，回避径向薛定谔方程而给出正确能级；结果与严格量子解一致。
- 适用条件：非相对论（$v\ll c$）、单电子（类氢）、忽略精细结构/自旋-轨道耦合/兰姆位移；$n=1,2,\ldots$ 为正整数。

## 推导

1. 库仑力提供向心力：

$$
\frac{e^2}{4\pi\varepsilon_0 r^2}=\frac{m_e v^2}{r}
$$

2. 玻尔角动量量子化：

$$
m_e v r = n\hbar
$$

3. 两式联立消去 $v$：由第 2 式 $v=\dfrac{n\hbar}{m_e r}$ 代入第 1 式：

$$
\frac{e^2}{4\pi\varepsilon_0 r^2}=\frac{m_e}{r}\left(\frac{n\hbar}{m_e r}\right)^2
=\frac{n^2\hbar^2}{m_e r^3}
$$

解得轨道半径

$$
r_n = \frac{4\pi\varepsilon_0\hbar^2}{m_e e^2}\, n^2 = a_0 n^2,\qquad
a_0=\frac{4\pi\varepsilon_0\hbar^2}{m_e e^2}\approx0.529\,\mathrm{\AA}
$$

4. 能量 $E_n=T+V=\dfrac12 m_e v^2-\dfrac{e^2}{4\pi\varepsilon_0 r}$。用向心力式 $m_e v^2=\dfrac{e^2}{4\pi\varepsilon_0 r}$ 得 $T=\dfrac{e^2}{8\pi\varepsilon_0 r}$，故

$$
E_n = -\frac{e^2}{8\pi\varepsilon_0 r_n}
= -\frac{m_e e^4}{2(4\pi\varepsilon_0)^2\hbar^2}\frac{1}{n^2}
= -\frac{13.6\,\mathrm{eV}}{n^2}
$$

## 验算

- **① F 量纲**：$a_0$ 量纲为长度（$\mathrm{\AA}$ 级）；$E_n$ 量纲为能量，$13.6\ \mathrm{eV}$ 数值合理。**PASS**。
- **② L 极限/特例**：$n\to\infty$ 时 $E_n\to0^-$（电离限），能级趋于连续 **PASS**；$n=1$ 得基态 $-13.6\ \mathrm{eV}$，与实验电离能一致。**PASS**。
- **③ B 回代**：$r_n$、$v_n=\dfrac{n\hbar}{m_e r_n}$ 代回库仑力与量子化两式，均恒等。**PASS**。
- **④ C 守恒量**：中心库仑力场中角动量守恒，与 $m_e v r=n\hbar$ 的角动量量子化一致。**PASS**。
- **⑦ J 一致性**：能级公式 $E_n\propto -1/n^2$；$n=1$ 代入 $-13.6\ \mathrm{eV}$，$n=2$ 代入 $-3.4\ \mathrm{eV}$，比值 $4:1$ 自洽。**PASS**。

验算摘要：`已通过 ①②③④⑦，FAIL 0 项`

## 答案

**氢原子轨道半径 $r_n = a_0 n^2$，玻尔半径 $a_0=\dfrac{4\pi\varepsilon_0\hbar^2}{m_e e^2}\approx0.529\ \mathrm{\AA}$；能级 $E_n=-\dfrac{13.6\ \mathrm{eV}}{n^2}$（$n=1,2,\ldots$）。**

适用条件：非相对论单电子、忽略精细结构；此为半经典推导，结果与严格量子解一致。

## 易错点

1. 能量是动能与势能之和且势能为负：漏掉 $V=-e^2/(4\pi\varepsilon_0 r)$ 的负号或忘 $T=\tfrac12 mv^2$ 都会错。
2. 把 $a_0$ 直接当 $r_n$：$r_n=a_0 n^2$，含 $n^2$ 因子。
