# 例题：粗糙斜面下滑（能量守恒误用与回溯修正，模板 A）

## 题意与图景

- **系统**：质量 $m$ 的物块从粗糙斜面上端由静止开始沿斜面下滑距离 $s$；倾角 $\alpha$，动摩擦因数 $\mu$。
- **约束**：斜面固定、物块沿斜面一维运动；摩擦为耗散力。
- **坐标**：沿斜面向下为正；单位制：SI。
- **已知**：$m$、$\alpha$、$\mu$、$s$、$g$。**待求**：末速度 $v$。

## 建模

- **方法选择**：系统有摩擦耗散，机械能不守恒，故用功能原理（外力做功等于动能增量），并用牛顿第二定律作独立复核。
- **功能原理**：

$$
(mg\sin\alpha-\mu mg\cos\alpha)\,s=\frac12 mv^2
$$

- **适用条件声明**：无粘滞、摩擦做功全程存在；能量守恒仅在无耗散时适用，本系统不满足。

## 推导

**第一次尝试（错误）**：误用机械能守恒

$$
\frac12mv^2=mgs\sin\alpha\quad\Rightarrow\quad v_{\rm wrong}=\sqrt{2gs\sin\alpha}
$$

**验算发现 FAIL**：摩擦力做功 $-fs$，机械能减少，C 守恒量检查不通过。

**回溯**：回到建模，诊断错误为“忽略耗散项”；修正为功能原理：

$$
(mg\sin\alpha-\mu mg\cos\alpha)s=\frac12mv^2
$$

解得：

$$
v=\sqrt{2gs(\sin\alpha-\mu\cos\alpha)}
$$

**重验**：将 $v$ 代回功能原理、用牛顿第二定律复核 $a=g(\sin\alpha-\mu\cos\alpha)$，$v^2=2as$ 一致；$\mu\to0$ 还原无摩擦结果。**修复后 PASS**。

## 验算

- **① F 量纲**：$[2gs(\sin\alpha-\mu\cos\alpha)]^{1/2}=LT^{-1}$，速度量纲正确。**PASS**。
- **② L 极限/特例**：$\mu\to0$ 时 $v=\sqrt{2gs\sin\alpha}$（无摩擦极限）；$\mu=\tan\alpha$ 时 $v=0$（临界静止）。**PASS**。
- **③ B 回代**：把 $v=\sqrt{2gs(\sin\alpha-\mu\cos\alpha)}$ 代回功能原理，两边恒等；由 $a=g(\sin\alpha-\mu\cos\alpha)$ 与 $v^2=2as$ 重推得同一结果。**PASS**。
- **④ C 守恒量**：初始 FAIL——裸用能量守恒得出错误速度；修正后能量关系为 $\Delta K=W_g+W_f$，机械能变化恰等于摩擦功 $-fs$，复核 PASS。**PASS**。

验算：`①②③④，FAIL 0 项（含一次修复后 PASS）`

## 答案

**末速度 $v=\sqrt{2gs(\sin\alpha-\mu\cos\alpha)}$；无摩擦极限 $v\to\sqrt{2gs\sin\alpha}$。**

适用条件：物块沿斜面下滑全程、$\mu<\tan\alpha$（否则不能加速下滑）、斜面固定。

## 易错点

1. 有摩擦时直接写机械能守恒：$W_f\neq0$，必须用功能原理。
2. 摩擦功符号：$W_f=-fs$，漏负号会得到虚数速度。
3. 极限 $\mu\to0$ 只是数值还原，不代表“能量守恒在此题可用”。
