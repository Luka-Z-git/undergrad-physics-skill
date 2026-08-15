# 测试用例 (Test Cases)

本文件定义 `undergrad-physics-skill` v0.8.0 的行为断言。用例按 `TC-XXX-NNN` 格式编号。

约定：验证结果必须为 `PASS`/`FAIL` 纯文本；输出不得含 emoji、Overleaf 不兼容字符。

结构门禁可用脚本自动校验（六节标题/验算编号/加粗/禁用符号/`$$` 配平）：

```
python tests/validate_structure.py <answer.md>
```

## 快速冒烟（修改后必跑）

TC-NEW-001 · TC-TUT-001 · TC-ELE-001 · TC-QNT-001

核心流程或验证引擎变更后，另运行 `adversarial_cases.md` 的 TC-ADV-001 至 TC-ADV-012；这些用例检验错误能否被实际验算捕获，而不只检查输出结构。

## 用例清单

| 编号 | 领域 | 复杂度 | 题目 |
|---|---|---|---|
| TC-NEW-001 | 牛顿力学 | 简单 | 恒力下物块直线运动 |
| TC-LAG-001 | 拉格朗日 | 复杂 | 双摆运动方程 |
| TC-HAM-001 | 哈密顿 | 简单 | 一维谐振子正则方程 |
| TC-CON-001 | 守恒量 | 简单 | 中心力场角动量守恒 |
| TC-SMO-001 | 小振动 | 复杂 | 耦合振子简正模式 |
| TC-NIF-001 | 非惯性系 | 简单 | 加速车厢悬挂小球 |
| TC-VER-001 | 验证回溯 | 中等 | 摩擦斜面（耗散系统） |
| TC-DOM-001 | 定义域 | 中等 | 阻尼振子三分区 |
| TC-ELE-001 | 电磁学-电路 | 简单 | RC 放电暂态 |
| TC-ELE-002 | 电磁学-磁场 | 简单 | 均匀磁场回旋运动 |
| TC-ELE-003 | 电磁学-静电 | 中等 | 均匀带电球壳电场 |
| TC-QNT-001 | 量子-一维 | 简单 | 无限深势阱定态 |
| TC-QNT-002 | 量子-谐振子 | 中等 | 升降算符能谱 |
| TC-QNT-003 | 量子-算符 | 简单 | 对易关系与不确定度 |
| TC-TUT-001 | 诊断-分流 | 简单 | 检查请求进入诊断模式 |
| TC-TUT-002 | 诊断-不完整 | 简单 | 不完整作答指出缺项 |
| TC-TUT-003 | 诊断-有错 | 简单 | 错误作答定位与确认题 |
| TC-TUT-004 | 诊断-正确 | 简单 | 正确作答概念确认 |

---

## 简单测试（紧凑格式）

以下 TC 的 Expected Behavior 为标准答案摘要，Required Verification 仅列关键检查点。完整输出规范见 `modules/output_templates.md`。

### TC-NEW-001（牛顿/恒力直线）

**Input:** 质量为 $m$ 的物块在光滑水平面上从静止开始受恒定水平力 $F$ 作用，求 $x(t)$ 与 $v(t)$。

**答案:** $v(t)=Ft/m$, $x(t)=Ft^2/(2m)$；加粗带单位。

**验算要点:**
- ①F: $[Ft^2/(2m)]=L$ PASS | ②L: $F\to0 \Rightarrow x=0$ PASS | ③B: $m\ddot x=F$ PASS | ④C: N/A（外力做功）
- 数值: $m=2,F=10,t=3 \Rightarrow x=22.5\,\mathrm{m}, v=15\,\mathrm{m/s}$

**Key Checks:** 初值定常数；1/2 因子。

**Failure Modes:** 漏 1/2；忘积分常数；方向不一致。

---

### TC-HAM-001（哈密顿/谐振子）

**Input:** $L = \tfrac12 m\dot x^2 - \tfrac12 kx^2$，求 $H$ 与正则方程。

**答案:** $p=m\dot x$, $H=p^2/(2m)+\tfrac12 kx^2$, $\dot x=p/m$, $\dot p=-kx$。

**验算要点:**
- ①F: $[p^2/(2m)]=$能量 PASS | ②L: $k\to0 \Rightarrow$自由粒子 PASS | ③B: 合并正则方程得 $m\ddot x=-kx$ PASS | ④C: $H$ 守恒 PASS

**Key Checks:** $H$ 不残留 $\dot x$；$\dot p$ 负号。

**Failure Modes:** $H$ 含 $\dot x$；$p$ 符号错；$\dot p=+kx$。

---

### TC-CON-001（守恒量/中心力场）

**Input:** $L = \tfrac12 m(\dot r^2 + r^2\dot\theta^2) - V(r)$，指出守恒量。

**答案:** $\theta$ 循环 → $p_\theta=mr^2\dot\theta$ 守恒（角动量）；$L$ 不显含 $t$ → $E$ 守恒。

**验算要点:**
- ①F: $[mr^2\dot\theta]=ML^2T^{-1}$ PASS | ②L: 圆轨道 $r=a \Rightarrow p_\theta=ma^2\omega$ PASS | ③B: 代回 θ 的 E-L 方程恒等 PASS | ④C: 两态 $p_\theta$ 相等 PASS

**Key Checks:** 守恒的是 $p_\theta$ 非 $\theta$；角动量相对固定点。

**Failure Modes:** 断言"$\theta$ 不变"；$p_\theta=0$；外场破缺对称仍假设守恒。

---

### TC-NIF-001（非惯性系/加速车厢）

**Input:** 车厢以恒定加速度 $a$ 加速，内悬小球，求平衡时夹角。

**答案:** $\tan\theta = a/g$，小球偏向加速度反方向。

**验算要点:**
- ①F: $a/g$ 无量纲 PASS | ②L: $a\to0 \Rightarrow \theta\to0$ PASS | ③B: $T\sin\theta=ma, T\cos\theta=mg$ 恒等 PASS | ④C: N/A（静平衡）
- I（可选）: 惯性系推导结果一致

**Key Checks:** 惯性力方向与加速度相反；声明非惯性系。

**Failure Modes:** 漏惯性力；方向写反；把惯性力当真实力。

---

### TC-ELE-001（电磁学/RC放电）

**Input:** 电容 $C$ 初始电压 $V_0$，$t=0$ 经电阻 $R$ 放电，求 $V_C(t), I(t), \tau$。

**答案:** $V(t)=V_0e^{-t/\tau}$, $I(t)=(V_0/R)e^{-t/\tau}$, $\tau=RC$。

**验算要点:**
- ①F: $[\tau]=\mathrm{s}$ PASS | ②L: $t\to0 \Rightarrow V_0, V_0/R$; $t\to\infty \Rightarrow 0$ PASS | ③B: $\dot V+V/\tau=0$ 恒等 PASS | ④C: $dU_C/dt=-I^2R$ PASS
- 数值: $R=1\,\mathrm{k\Omega}, C=100\,\mu\mathrm{F}, t=0.1 \Rightarrow V\approx1.84\,\mathrm{V}$

**Key Checks:** $\tau=RC$（非倒数）；指数负号；初始条件定常数。

**Failure Modes:** 时间常数写反；指数增长解；符号不一致。

---

### TC-ELE-002（电磁学/回旋运动）

**Input:** 质量 $m$、电荷 $q$、速度 $v \perp B$，求 $r, \omega, T$。

**答案:** $r=mv/(qB)$, $\omega=qB/m$, $T=2\pi m/(qB)$。

**验算要点:**
- ①F: $[mv/(qB)]=\mathrm{m}$ PASS | ②L: $B\to0 \Rightarrow r\to\infty$（直线）PASS | ③B: $qvB=mv^2/r$ 恒等 PASS | ④C: 动能恒定（磁力不做功）PASS

**Key Checks:** $v\perp B$ 才是纯圆轨道；周期不含 $v$。

**Failure Modes:** $r=qvB/m$ 写反；周期含 $v$；说磁力做功。

---

### TC-ELE-003（电磁学/高斯定律）

**Input:** 半径 $R$ 均匀带电球壳总电荷 $Q$，求内外电场。

**答案:** $E=0$ ($r<R$); $E=\dfrac{Q}{4\pi\varepsilon_0 r^2}\hat{\mathbf r}$ ($r>R$)。

**验算要点:**
- ①F: $[Q/(\varepsilon_0 r^2)]=\mathrm{V/m}$ PASS | ②L: $r\to\infty$ 退化为点电荷 PASS | ③B: 高斯定律在球内外均成立 PASS | ④C: N/A | D: $r=R$ 处 $E$ 不连续（面电荷），须声明

**Key Checks:** 球对称；$Q_{\mathrm{enc}}$ 对应半径；球壳≠球体。

**Failure Modes:** 球内非零；无对称硬套高斯；边界未声明。

---

### TC-QNT-001（量子/无限深势阱）

**Input:** $0<x<L$ 一维无限深势阱，求 $\psi_n, E_n$。

**答案:** $\psi_n=\sqrt{2/L}\sin(n\pi x/L)$, $E_n=n^2\pi^2\hbar^2/(2mL^2)$, $n=1,2,\ldots$

**验算要点:**
- ①F: $E_n$ 为能量 PASS | ②L: $L\to\infty$ 能级间距→0 PASS | ③B: $\psi_n''$ 代回定态方程恒等 PASS | ④C: 定态概率密度不显含时间 PASS | ⑦J: 归一化+正交 PASS
- 数值: 电子 $L=1\,\mathrm{nm} \Rightarrow E_1\approx0.376\,\mathrm{eV}$

**Key Checks:** 无限墙处 $\psi=0$（非 $\psi'$）；归一化系数；$n$ 从 1 开始。

**Failure Modes:** 边界条件错；漏归一化；$n=0$ 作为零能解。

---

### TC-QNT-003（量子/对易关系）

**Input:** 证明 $[\hat x,\hat p]=i\hbar$，写出不确定性关系。

**答案:** 对任意可微 $f$：$[\hat x,\hat p]f=i\hbar f$; $\Delta x\,\Delta p\ge\hbar/2$。

**验算要点:**
- ①F: $[x][p]=ML^2T^{-1}=[\hbar]$ PASS | ②L: $\hbar\to0$ 退化为经典可交换 PASS | ③B: 作用到试探函数逐项化简得 $i\hbar f$ PASS | ④C: N/A | ⑦J: $\hat x,\hat p$ 厄米 PASS

**Key Checks:** $\hat p=-i\hbar d/dx$ 符号；算符顺序保持；试探函数任意可微。

**Failure Modes:** $\hat p=+i\hbar d/dx$；交换顺序；不展开直接断言。

---

### TC-TUT-001 ~ TC-TUT-004（学生诊断——流程断言）

**TC-TUT-001（分流）**: Input 含"检查/对吗/诊断"→ 进入模板 E，不展开模板 A。Failure: 直接给六节答案。

**TC-TUT-002（不完整）**: "写到一半卡住了" → 结论"不完整（缺：推导、答案）"，给出具体下一步，不展开解答。Failure: 直接给完整答案或只说"继续"。

**TC-TUT-003（有错）**: "RC放电我算得 $V=V_0e^{+t/\tau}$" → ②L FAIL($t\to\infty$发散) + ③B FAIL(不满足ODE) + ④C FAIL(能量单调增)；定位：指数符号；出确认题。Failure: 只判对错不定位。

**TC-TUT-004（正确）**: 无限深势阱答案正确 → 四项 PASS + ⑦J PASS；**必须**出概念确认题（如"为什么 $n=0$ 不允许？"）。Failure: 只输出"正确"不提问。

---

## 中等/复杂测试（完整格式）

以下 TC 保留完整的 Expected Behavior 与 Required Verification，作为复杂题输出的参考标准。

### TC-VER-001（验证回溯/摩擦斜面）

**Test ID:** TC-VER-001

**Input:** 质量 $m$ 的滑块在倾角 $\alpha$ 的粗糙斜面下滑距离 $s$，动摩擦系数 $\mu$，求末速度。

**Expected Classification:** 验证回溯（耗散系统，禁止裸用能量守恒）

**Expected Behavior:** 先识别耗散 → $E=\text{const}$ 应为 FAIL → 用功能原理：

$$
v = \sqrt{2gs(\sin\alpha - \mu\cos\alpha)}
$$

声明下滑条件 $\sin\alpha > \mu\cos\alpha$（D）。

**Required Verification:**
- ①F: 根号内 $L^2T^{-2}$, $v$ 为 $LT^{-1}$ PASS
- ②L: $\mu\to0 \Rightarrow v=\sqrt{2gs\sin\alpha}$（能量守恒极限）PASS
- ③B: 代回功能原理方程恒等 PASS
- ④C: $\mu\neq0$ 时 $E_2\neq E_1$，正确判 FAIL 后改用功能原理 PASS
- I（可选）: 牛顿第二定律结果一致

**Key Checks:** 摩擦功为负；下滑条件；$\mu$ 缺省时不编造数值。

**Failure Modes:** 无视摩擦直接写 $\frac12 mv^2=mgs\sin\alpha$ 并伪称 PASS；摩擦功符号写反。

---

### TC-DOM-001（定义域/阻尼振子）

**Test ID:** TC-DOM-001

**Input:** 阻尼振子 $m\ddot x + c\dot x + kx = 0$，$\beta=c/(2m)$, $\omega_0=\sqrt{k/m}$。求临界阻尼通解与欠/过阻尼条件。

**Expected Behavior:** 特征方程 $\lambda^2+2\beta\lambda+\omega_0^2=0$；临界 $\beta=\omega_0$ → $x=(A+Bt)e^{-\beta t}$；欠阻尼 $\beta<\omega_0$；过阻尼 $\beta>\omega_0$。

**Required Verification:**
- ①F: $[\beta]=[\omega_0]=T^{-1}$ PASS
- ②L: $\beta\to0$ 退化为简谐振动；$t\to0 \Rightarrow x(0)=A$ PASS
- ③B: 临界解代入 ODE 恒等 PASS
- ④C: N/A（耗散）

**Key Checks:** 重根保留 $t$ 因子；$\omega_d$ vs $\omega_0$ 不混淆。

**Failure Modes:** 临界解漏 $(A+Bt)$；根号下为负未处理。

---

### TC-QNT-002（量子/升降算符）

**Test ID:** TC-QNT-002

**Input:** $\hat H=\hat p^2/(2m)+\frac12 m\omega^2\hat x^2$，求能级并用升降算符求基态。

**Expected Behavior:** $[\hat a,\hat a^\dagger]=1$; $E_n=(n+\frac12)\hbar\omega$; 基态 $\hat a\psi_0=0$ → $\psi_0=(m\omega/\pi\hbar)^{1/4}e^{-m\omega x^2/(2\hbar)}$。

**Required Verification:**
- ①F: $\hbar\omega$ 为能量, $\psi_0$ 量纲 $L^{-1/2}$ PASS
- ②L: $n=0$ 零点能 $\hbar\omega/2$; $\omega\to0 \Rightarrow E_0\to0$ PASS
- ③B: $\psi_0$ 代入 $\hat H\psi_0=E_0\psi_0$ 恒等 PASS
- ④C: 定态概率密度不显含时间 PASS | ⑦J: $[\hat a,\hat a^\dagger]=1$ + 归一化 PASS
- I（可选）: Hermite 多项式截断得同一能谱

**Key Checks:** 零点能不可漏；$\hat a$ 非厄米；高斯归一化完整。

**Failure Modes:** $E_0=0$; $[\hat a,\hat a^\dagger]=0$; 归一化漏 $\pi^{1/4}$。

---

### TC-LAG-001（拉格朗日/双摆）复杂题参考标准

**Test ID:** TC-LAG-001

**Input:** 双摆（两质点 $m$，两杆 $l$），求运动微分方程。

**Expected Behavior:**

$$
T = ml^2\left[\dot\theta_1^2 + \tfrac12\dot\theta_2^2 + \dot\theta_1\dot\theta_2\cos(\theta_1-\theta_2)\right], \quad
V = -mgl(2\cos\theta_1 + \cos\theta_2)
$$

由 E-L 方程得耦合方程组（见 `examples/pendulum_lagrangian.md` 格式）。

**Required Verification:**
- ①F: 两方程每项均为 $LT^{-2}$ PASS
- ②L: $\theta_2\equiv0$ → 第一式退化为单摆 PASS
- ③B: 由 $L$ 逐项计算 E-L 方程，核对恒等 PASS
- ④C: $E=T+V$ 守恒（两组状态数值核对）PASS | ⑦J 不适用（非矩阵问题）

**Key Checks:** 动能交叉项系数；势能符号；E-L 偏导不混淆。

**Failure Modes:** 漏交叉项；势能符号反；用"显然"代替计算。

---

### TC-SMO-001（小振动/耦合振子）复杂题参考标准

**Test ID:** TC-SMO-001

**Input:** 两物块 $m$，弹簧 $k$（两端）+ $k_c$（中间），求简正频率与模式。

**Expected Behavior:** 完整解答见 `examples/coupled_oscillators.md`（模板 A + J 一致性必做示范）。

**Required Verification:**
- ①F: $[k/m]=T^{-2}$ PASS | ②L: $k_c\to0$ 退化为两个独立振子 PASS
- ③B: $\omega_\alpha^2$ 代回特征方程 = 0 PASS | ④C: $E=T+V$ 守恒 PASS
- **⑦J（本域必做）**: 特征向量回代 $(K-\omega_\alpha^2 M)\mathbf A_\alpha=0$ PASS + M-正交 $\mathbf A_1^T M \mathbf A_2=0$ PASS

**Key Checks:** 用 $\det(K-\omega^2 M)$（非 $I$）；耦合元 $-k_c$ 符号；M-正交。

**Failure Modes:** 漏质量矩阵；耦合元符号反；特征向量不正交。
