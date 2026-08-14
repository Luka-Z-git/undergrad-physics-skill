# 测试用例 (Test Cases)

本文件定义 `undergrad-physics-skill` v0.4（理论力学 + 电磁学 + 基础量子力学 + 可选学生诊断模式）的行为断言。用例按 `TC-XXX-NNN` 格式编号，供人工评审或模型自检：把 Input 交给技能执行，按 Expected Behavior 逐项核对；Required Verification 列出该题必须出现的验证方法及可复算的具体数值；Failure Modes 列出技能若产生这些行为则判定 FAIL。

约定：验证结果必须为 `PASS`/`FAIL` 纯文本；输出不得含 emoji、对勾/叉号等 Overleaf 不兼容字符。

## 快速自检（冒烟）

修改 SKILL.md、输出模板或验证引擎后，至少重跑以下用例：

- TC-NEW-001：模板 A 六节 + 验算摘要
- TC-TUT-001：诊断模式分流，不展开完整答案
- TC-ELE-001：电磁学电路暂态
- TC-QNT-001：量子一维系统

逐项通过后再认为回归通过。

## 用例清单

| 编号 | 领域 | 题目 |
|---|---|---|
| TC-NEW-001 | 牛顿力学 | 恒力下物块直线运动 |
| TC-LAG-001 | 拉格朗日力学 | 双摆运动方程 |
| TC-HAM-001 | 哈密顿力学 | 一维谐振子正则方程 |
| TC-CON-001 | 守恒量 | 中心力场角动量守恒 |
| TC-SMO-001 | 小振动 | 耦合振子简正模式 |
| TC-NIF-001 | 非惯性系 | 加速车厢内悬挂小球平衡 |
| TC-VER-001 | 验证回溯 | 摩擦系统禁止裸用能量守恒 |
| TC-DOM-001 | 定义域 | 阻尼振荡三分区 |
| TC-ELE-001 | 电磁学-电路 | RC 电路放电暂态 |
| TC-ELE-002 | 电磁学-磁场 | 均匀磁场回旋运动 |
| TC-ELE-003 | 电磁学-静电场 | 均匀带电球壳电场 |
| TC-QNT-001 | 量子-一维系统 | 无限深势阱定态 |
| TC-QNT-002 | 量子-谐振子 | 升降算符能谱 |
| TC-QNT-003 | 量子-算符 | 对易关系与不确定度 |
| TC-TUT-001 | 学生诊断-分流 | 检查请求进入诊断模式 |
| TC-TUT-002 | 学生诊断-不完整 | 不完整作答直接指出缺项 |
| TC-TUT-003 | 学生诊断-有错 | 完整但错误作答直接定位 |
| TC-TUT-004 | 学生诊断-正确 | 完整且正确做概念确认 |

## TC-NEW-001

**Test ID:** TC-NEW-001

**Input:** "质量为 $m$ 的物块在光滑水平面上从静止开始受恒定水平力 $F$ 作用，求 $t$ 时刻的位移 $x(t)$ 与速度 $v(t)$。"

**Expected Classification:** 牛顿力学（恒力直线运动）

**Expected Behavior:** 声明惯性系与一维坐标；写 $m\ddot x = F$；积分得 $v(t) = Ft/m$、$x(t) = Ft^2/(2m)$；最终答案加粗并带单位。

**Required Verification:** ①F 量纲：$[F/m] = MLT^{-2}/M = LT^{-2}$，$[Ft^2/(2m)] = L$。②L 极限/特例：$F \to 0$ 时 $x(t) = 0$、$v(t) = 0$（静止特例）。③B 回代：$m\,d^2(Ft^2/(2m))/dt^2 = F$。④C 守恒量：外力做功，机械能不守恒，标 N/A（外力做功）。E 数值抽样（可选加分项）：取 $m = 2\,\mathrm{kg}$、$F = 10\,\mathrm{N}$、$t = 3\,\mathrm{s}$，得 $x = 22.5\,\mathrm{m}$、$v = 15\,\mathrm{m/s}$。

**Key Checks:** 初值 $x(0)=0$、$v(0)=0$ 必须用于定积分常数；单位制显式声明；$1/2$ 因子。

**Failure Modes:** 位移漏 $1/2$ 因子；忘记积分常数导致解族不唯一；力与位移方向不一致；未做量纲检查或伪造 PASS。

## TC-LAG-001

**Test ID:** TC-LAG-001

**Input:** "两个质量均为 $m$ 的质点用两根长度均为 $l$ 的无质量轻杆连接，上端固定，构成竖直平面内的双摆，求运动微分方程。"

**Expected Classification:** 拉格朗日力学（完整约束、双自由度）

**Expected Behavior:** 取广义坐标 $\theta_1,\theta_2$（相对竖直向下）；写

$$
T = ml^2\left[\dot\theta_1^2 + \tfrac12\dot\theta_2^2 + \dot\theta_1\dot\theta_2\cos(\theta_1-\theta_2)\right], \qquad
V = -mgl(2\cos\theta_1 + \cos\theta_2)
$$

由 E-L 方程得：

$$
2l\ddot\theta_1 + l\ddot\theta_2\cos(\theta_1-\theta_2) + l\dot\theta_2^2\sin(\theta_1-\theta_2) + 2g\sin\theta_1 = 0
$$

$$
l\ddot\theta_2 + l\ddot\theta_1\cos(\theta_1-\theta_2) - l\dot\theta_1^2\sin(\theta_1-\theta_2) + g\sin\theta_2 = 0
$$

**Required Verification:** ①F 量纲：两方程每项量纲均为 $LT^{-2}$。②L 极限/特例：令 $\theta_2 \equiv 0$、$\dot\theta_2 = 0$，第一式退化为 $2l\ddot\theta_1 + 2g\sin\theta_1 = 0$，即单摆方程。③B 回代：由 $L$ 逐项计算 $d(\partial L/\partial\dot\theta_i)/dt$ 与 $\partial L/\partial\theta_i$，核对两式与 E-L 方程恒等。④C 守恒量：$L$ 不显含 $t$、约束定常且无耗散，$E = T+V$ 守恒；小角下取同一能量面两组状态 $(\theta_1,\theta_2,\dot\theta_1,\dot\theta_2) = (0,0,\omega,\omega)$ 与 $(A,A,0,0)$，其中 $\omega^2 = 3gA^2/(5l)$，两态 $E$ 均为 $-3mgl + \frac52 ml^2\omega^2$，核对相等。

**Key Checks:** 动能交叉项 $2\dot\theta_1\dot\theta_2\cos(\theta_1-\theta_2)$ 的系数；势能符号（竖直向下为零势能参考时 $V$ 为负）；E-L 中 $\partial L/\partial q$ 与 $d(\partial L/\partial\dot q)/dt$ 不混淆；完整约束、无耗散适用条件声明。

**Failure Modes:** 漏交叉项或把 $\cos(\theta_1-\theta_2)$ 写成 1；势能符号写反；把 $\partial L/\partial q$ 当 $d(\partial L/\partial\dot q)/dt$ 求；用"显然"代替计算；未声明小角近似的能量核对适用区间。

## TC-HAM-001

**Test ID:** TC-HAM-001

**Input:** "一维谐振子 $L = \tfrac12 m\dot x^2 - \tfrac12 kx^2$，求哈密顿量与正则方程。"

**Expected Classification:** 哈密顿力学（Legendre 变换）

**Expected Behavior:** $p = \partial L/\partial\dot x = m\dot x$；$H = p\dot x - L = p^2/(2m) + \tfrac12 kx^2$；正则方程 $\dot x = p/m$、$\dot p = -kx$；$H$ 中不残留 $\dot x$。

**Required Verification:** ①F 量纲：$[p^2/(2m)] = ML^2T^{-2}$（能量），$[\dot x] = LT^{-1}$，$[kx] = MLT^{-2}$（力）。②L 极限/特例：$k \to 0$ 时 $H \to p^2/(2m)$（自由粒子）。③B 回代：由 $\dot x = p/m$ 与 $\dot p = -kx$ 合并得 $m\ddot x = -kx$，与牛顿方程一致。④C 守恒量：$H$ 不显含 $t$ 且无耗散，$E = H$ 守恒，$(x,p) = (1,0)$ 与 $(0,1)$ 两态 $H$ 均为 $0.5\,\mathrm{J}$。E 数值抽样（可选加分项）：取 $m = 1\,\mathrm{kg}$、$k = 1\,\mathrm{N/m}$，$\omega = 1\,\mathrm{s^{-1}}$、$T = 2\pi\,\mathrm{s}$。

**Key Checks:** $H$ 必须先消去 $\dot x$；正则方程 $\dot p = -\partial H/\partial x$ 的负号；$H$ 与机械能 $E$ 相等的条件（定常约束、$T$ 为 $\dot q$ 二次齐次式）。

**Failure Modes:** $H$ 中残留 $\dot x$；$p$ 定义符号错；$\dot p = +kx$；$k \to 0$ 极限缺失。

## TC-CON-001

**Test ID:** TC-CON-001

**Input:** "质点在中心力场 $V(r)$ 中运动，$L = \tfrac12 m(\dot r^2 + r^2\dot\theta^2) - V(r)$。指出守恒量并说明判据。"

**Expected Classification:** 守恒量与对称性（循环坐标 + 时间平移）

**Expected Behavior:** $\theta$ 为循环坐标，$p_\theta = \partial L/\partial\dot\theta = mr^2\dot\theta$ 守恒（相对固定点的角动量）；$L$ 不显含 $t$，$h = \tfrac12 m(\dot r^2 + r^2\dot\theta^2) + V(r) = E$ 守恒。

**Required Verification:** ①F 量纲：$[mr^2\dot\theta] = ML^2T^{-1}$（角动量）。②L 极限/特例：圆轨道 $r = a = \mathrm{const}$ 时 $\dot\theta = \mathrm{const}$，$p_\theta = ma^2\omega$。③B 回代：把 $p_\theta = mr^2\dot\theta$ 代回 $\theta$ 的 E-L 方程，得 $d(mr^2\dot\theta)/dt = 0$，恒等。④C 守恒量：取状态 $(r=a,\ \dot\theta=\omega_0)$ 与 $(r=b,\ \dot\theta=(a/b)^2\omega_0)$，$p_\theta = ma^2\omega_0 = mb^2(a/b)^2\omega_0$，两态相等。

**Key Checks:** 守恒的是广义动量 $p_\theta$ 而非坐标 $\theta$；角动量须相对固定点（或质心）定义；$V$ 只依赖 $r$ 才具有转动对称。

**Failure Modes:** 断言"$\theta$ 不变"；把守恒量误当 $p_\theta = 0$；外场破缺对称仍假设守恒；未声明无耗散。

## TC-SMO-001

**Test ID:** TC-SMO-001

**Input:** "两个质量均为 $m$ 的物块在水平光滑轨道上，中间用劲度系数 $k_c$ 的弹簧相连，两端再各用劲度系数 $k$ 的弹簧连接固定墙，求简正频率与简正模式。"

**Expected Classification:** 小振动与简正模式（耦合振子）

**Expected Behavior:** 以平衡位置为原点取位移 $\xi_1,\xi_2$，$T = \tfrac12 m(\dot\xi_1^2+\dot\xi_2^2)$，$V = \tfrac12 k\xi_1^2 + \tfrac12 k\xi_2^2 + \tfrac12 k_c(\xi_1-\xi_2)^2$；质量矩阵 $M = mI$，刚度矩阵

$$
K = \begin{pmatrix} k+k_c & -k_c \\ -k_c & k+k_c \end{pmatrix}
$$

由 $\det(K-\omega^2M)=0$ 得 $\omega_1^2 = k/m$、$\omega_2^2 = (k+2k_c)/m$；简正模式为同相 $(1,1)$ 与反相 $(1,-1)$。

**Required Verification:** ①F 量纲：$[k/m]$、$[(k+2k_c)/m]$ 均为 $T^{-2}$，$\omega$ 量纲 $T^{-1}$。②L 极限/特例：$k_c \to 0$ 时两频率均退化为 $\sqrt{k/m}$（两个独立振子）。③B 回代：把 $\omega_1^2 = k/m$、$\omega_2^2 = (k+2k_c)/m$ 代回特征方程，$\det(K-\omega_\alpha^2 M) = 0$ 成立。④C 守恒量：无耗散且 $K$ 定常，$E = T+V$ 守恒，数值抽样核对同相模式演化能量不变。J 一致性（本域必做）：特征向量 $(1,1)$、$(1,-1)$ 回代 $(K-\omega_\alpha^2 M)\mathbf A_\alpha = 0$ 且 $\mathbf A_1^T M \mathbf A_2 = 0$（M-正交）。

**Key Checks:** 用 $\det(K-\omega^2M)$ 而非 $\det(K-\omega^2I)$；刚度矩阵耦合元 $-k_c$ 的符号；简正模式须做 M-正交核对。

**Failure Modes:** 漏质量矩阵；耦合项符号写反；特征向量不正交仍宣称得到正常坐标；把角频率 $\omega$ 与频率 $f$ 混淆。

## TC-NIF-001

**Test ID:** TC-NIF-001

**Input:** "车厢在水平方向以恒定加速度 $a$ 加速，车厢内用轻绳悬挂质量为 $m$ 的小球，求小球相对车厢静止时悬线与竖直方向的夹角。"

**Expected Classification:** 非惯性系（平动惯性力）

**Expected Behavior:** 声明车厢系为非惯性系；平衡时惯性力 $-ma$ 与重力、张力三力平衡，得 $\tan\theta = a/g$，其中 $\theta$ 为悬线偏离竖直方向的角度，小球偏向加速度反方向。

**Required Verification:** ①F 量纲：$a/g$ 无量纲，$\theta$ 用弧度。②L 极限/特例：$a \to 0$ 时 $\theta \to 0$（车厢静止时悬线竖直）。③B 回代：把 $\tan\theta = a/g$ 代回 $T\sin\theta = ma$、$T\cos\theta = mg$，得 $\tan\theta = a/g$ 恒等。④C 守恒量：静平衡问题无守恒量可验，标 N/A（静平衡）。I 独立方法（可选加分项）：惯性系中 $T\sin\theta = ma$、$T\cos\theta = mg$，同样得 $\tan\theta = a/g$。

**Key Checks:** 惯性力方向与加速度相反；惯性力只在非惯性系出现，受力图须区分真实力与惯性力；加速度恒定（若变速转动另有欧拉项）。

**Failure Modes:** 漏惯性力；惯性力方向写反（小球偏向加速方向）；把惯性力当真实力；未声明所用参考系。

## TC-VER-001

**Test ID:** TC-VER-001

**Input:** "质量为 $m$ 的滑块在倾角 $\alpha$ 的粗糙斜面上从静止开始下滑，动摩擦系数为 $\mu$，沿斜面下滑距离 $s$，求末速度。"

**Expected Classification:** 验证回溯（耗散系统，禁止裸用能量守恒）

**Expected Behavior:** 先识别耗散：机械能不守恒，直接写 $E = \mathrm{const}$ 应为 FAIL；用功能原理 $E_2 - E_1 = W_f = -\mu mg\cos\alpha\, s$，取初始点为势能零点得 $\tfrac12 mv^2 - mgs\sin\alpha = -\mu mg\cos\alpha\, s$，故

$$
v = \sqrt{2gs(\sin\alpha - \mu\cos\alpha)}
$$

并声明下滑条件 $\sin\alpha > \mu\cos\alpha$（D）。

**Required Verification:** ①F 量纲：根号内量纲为 $L^2T^{-2}$，$v$ 量纲 $LT^{-1}$。②L 极限/特例：$\mu \to 0$ 时 $v \to \sqrt{2gs\sin\alpha}$（无摩擦能量守恒极限）。③B 回代：把 $v$ 代回功能原理方程 $\tfrac12mv^2 - mgs\sin\alpha = -\mu mg\cos\alpha\, s$，恒等。④C 守恒量：$\mu \neq 0$ 时 $E_2 \neq E_1$，正确行为是判 FAIL 后改用功能原理。I 独立方法（可选加分项）：牛顿第二定律沿斜面 $mg\sin\alpha - \mu mg\cos\alpha = ma$，$v = \sqrt{2as}$ 一致。

**Key Checks:** 摩擦功为负；下滑条件 $\sin\alpha > \mu\cos\alpha$；$\mu$ 未给出时不得编造数值。

**Failure Modes:** 无视摩擦直接写 $\tfrac12 mv^2 = mgs\sin\alpha$ 并伪称 PASS；摩擦功符号写反；$\mu$ 缺省时硬造数值；漏定义域检查。

## TC-DOM-001

**Test ID:** TC-DOM-001

**Input:** "阻尼振子 $m\ddot x + c\dot x + kx = 0$，记 $\beta = c/(2m)$、$\omega_0 = \sqrt{k/m}$。求临界阻尼 $\beta = \omega_0$ 的通解，并说明欠阻尼与过阻尼条件。"

**Expected Classification:** 定义域/参数域 + 线性二阶常微分方程

**Expected Behavior:** 特征方程 $\lambda^2 + 2\beta\lambda + \omega_0^2 = 0$；$\beta = \omega_0$ 时重根 $\lambda = -\beta$，通解 $x = (A + Bt)e^{-\beta t}$；欠阻尼 $\beta < \omega_0$ 时阻尼频率 $\omega_d = \sqrt{\omega_0^2 - \beta^2}$ 为实数，过阻尼 $\beta > \omega_0$ 时无振荡；声明参数域。

**Required Verification:** ①F 量纲：$[\beta] = [\omega_0] = [\omega_d] = T^{-1}$。②L 极限/特例：$\beta \to 0$ 退化为简谐振动；$t \to 0$ 时 $x(0) = A$。③B 回代：$x = (A+Bt)e^{-\beta t}$ 代入 $\ddot x + 2\beta\dot x + \omega_0^2 x = 0$，$\beta = \omega_0$ 时恒等。④C 守恒量：阻尼耗散系统机械能不守恒，标 N/A（耗散，$E$ 单调递减）。

**Key Checks:** $\omega_0^2 - \beta^2$ 的符号决定振荡与否；重根情形必须保留 $t$ 因子（$B$ 项）；把 $\omega_d$ 当 $\omega_0$ 是常见错误。

**Failure Modes:** 临界阻尼解漏 $(A+Bt)$ 形式；根号下为负时未按过阻尼处理；未声明参数域；特征根与角频率混淆。

## TC-ELE-001

**Test ID:** TC-ELE-001

**Input:** "电容 $C$ 初始电压 $V_0$，$t=0$ 时刻经电阻 $R$ 放电，求 $V_C(t)$、$I(t)$ 与时间常数。"

**Expected Classification:** 电磁学（电路暂态）

**Expected Behavior:** 声明集总线性电路与电流方向；KVL 得 $\dot V + V/(RC) = 0$；解 $V(t) = V_0 e^{-t/\tau}$、$I(t) = (V_0/R)e^{-t/\tau}$、$\tau = RC$；最终答案加粗带单位。

**Required Verification:** ①F 量纲：$[\tau] = [\Omega\cdot\mathrm{F}] = \mathrm{s}$，$[V_0/R] = \mathrm{A}$。②L 极限/特例：$t\to0$ 得 $V_0$、$V_0/R$；$t\to\infty$ 得 0。③B 回代：$\dot V + V/\tau = 0$ 恒等。④C 守恒量：$dU_C/dt = -I^2R$，能量守恒。E 数值抽样（可选加分项）：$R = 1\,\mathrm{k\Omega}$、$C = 100\,\mu\mathrm{F}$、$V_0 = 5\,\mathrm{V}$，$t = 0.1\,\mathrm{s}$ 时 $V \approx 1.84\,\mathrm{V}$、$I \approx 1.84\,\mathrm{mA}$。

**Key Checks:** 电流方向与 $I = -C\dot V$ 一致；$\tau = RC$ 而非 $1/(RC)$；用初始条件定常数。

**Failure Modes:** 时间常数写反；指数符号错导致增长解；符号约定不一致；未做 $t\to0,\infty$ 极限与能量复核。

## TC-ELE-002

**Test ID:** TC-ELE-002

**Input:** "质量为 $m$、电荷为 $q$ 的质点以速度 $v$ 垂直于均匀磁场 $\mathbf B$ 运动，求回旋半径、角频率与周期。"

**Expected Classification:** 电磁学（洛伦兹力）

**Expected Behavior:** 磁力不做功、速率恒定；由 $qvB = mv^2/r$ 得 $r = mv/(qB)$、$\omega = qB/m$、$T = 2\pi m/(qB)$；声明非相对论、$v\perp\mathbf B$。

**Required Verification:** ①F 量纲：$[mv/(qB)] = \mathrm{m}$，$[m/(qB)] = \mathrm{s}$。②L 极限/特例：$B\to0$ 时 $r\to\infty$、$\omega\to0$（直线）。③B 回代：$m v^2/r = qvB$ 得 $r = mv/(qB)$，恒等。④C 守恒量：磁力不做功，动能恒定。E 数值抽样（可选加分项）：质子 $B = 0.5\,\mathrm{T}$、$v = 3\times10^6\,\mathrm{m/s}$，$r \approx 0.0626\,\mathrm{m}$、$T \approx 1.31\times10^{-7}\,\mathrm{s}$。

**Key Checks:** $v$ 必须垂直于 $\mathbf B$ 才是纯圆轨道；$q<0$ 旋转方向相反；周期与速度无关。

**Failure Modes:** $r = qvB/m$ 写反；周期含 $v$；说磁力做功改变速率；未声明非相对论条件。

## TC-ELE-003

**Test ID:** TC-ELE-003

**Input:** "半径为 $R$ 的均匀带电球壳总电荷 $Q$，求球内与球外电场。"

**Expected Classification:** 电磁学（高斯定律）

**Expected Behavior:** 声明静电学与球对称；高斯面 $r<R$ 时 $Q_{\mathrm{enc}}=0$，$r>R$ 时 $Q_{\mathrm{enc}}=Q$；得 $\mathbf E=0$（$r<R$）、$\mathbf E = \dfrac{Q}{4\pi\varepsilon_0 r^2}\hat{\mathbf r}$（$r>R$）。

**Required Verification:** ①F 量纲：$[Q/(\varepsilon_0 r^2)] = \mathrm{V/m}$。②L 极限/特例：$r\to\infty$ 退化为点电荷场；$r\to R^+$ 得球面外边界值。③B 回代：$\oint\mathbf E\cdot d\mathbf A = Q_{\mathrm{enc}}/\varepsilon_0$ 在球内外均恒等。④C 守恒量：N/A（静电场，无时变守恒运动量）。D 定义域：球壳内 $E=0$，边界处 $E$ 不连续（面电荷），须声明。

**Key Checks:** 高斯面半径与 $Q_{\mathrm{enc}}$ 对应；球对称要求 $\mathbf E$ 径向且大小只依赖 $r$；均匀带电球壳与均匀带电球体区分。

**Failure Modes:** 球内场非零；$Q_{\mathrm{enc}}$ 取错；无对称性硬套高斯；把球壳当导体或球体处理；未做边界/极限检查。

## TC-QNT-001

**Test ID:** TC-QNT-001

**Input:** "质量为 $m$ 的粒子在 $0<x<L$ 的一维无限深势阱中，求定态波函数与能级。"

**Expected Classification:** 基础量子力学（一维定态）

**Expected Behavior:** 阱内解 $\psi=A\sin(kx)+B\cos(kx)$；由 $\psi(0)=\psi(L)=0$ 得 $k_n=n\pi/L$；归一化得 $\psi_n=\sqrt{2/L}\sin(n\pi x/L)$、$E_n=n^2\pi^2\hbar^2/(2mL^2)$。

**Required Verification:** ①F 量纲：$E_n$ 为能量、$\psi$ 满足 $\int|\psi|^2dx$ 无量纲。②L 极限/特例：$n=1$ 基态无节点；$L\to\infty$ 能级间距趋于零。③B 回代：$\psi_n''=-(n\pi/L)^2\psi_n$ 代入定态方程恒等。④C 守恒量：定态概率密度不显含时间、能量期望恒定。J 一致性（本域必做）：归一化与不同 $n$ 正交。E 数值抽样（可选加分项）：电子 $L=1\,\mathrm{nm}$ 时 $E_1\approx0.376\,\mathrm{eV}$。

**Key Checks:** 无限墙处 $\psi=0$ 而非 $\psi'$ 连续；归一化系数 $\sqrt{2/L}$；$n$ 从 1 开始。

**Failure Modes:** 边界条件用错；漏归一化；$n=0$ 作为零能解；能量公式漏 $\pi^2$ 或 2 因子；未做正交/归一化检查。

## TC-QNT-002

**Test ID:** TC-QNT-002

**Input:** "一维量子谐振子 $\hat H=\hat p^2/(2m)+\frac12 m\omega^2\hat x^2$，求能级并用升降算符求基态波函数。"

**Expected Classification:** 基础量子力学（谐振子）

**Expected Behavior:** $\hat a,\hat a^\dagger$ 满足 $[\hat a,\hat a^\dagger]=1$；$E_n=(n+1/2)\hbar\omega$；基态 $\hat a\psi_0=0$ 得 $\psi_0=(m\omega/\pi\hbar)^{1/4}e^{-m\omega x^2/(2\hbar)}$。

**Required Verification:** ①F 量纲：$\hbar\omega$ 为能量，$\psi_0$ 量纲 $L^{-1/2}$。②L 极限/特例：$n=0$ 零点能 $\hbar\omega/2$；$\omega\to0$ 时 $E_0\to0$。③B 回代：$\psi_0$ 代入 $\hat H\psi_0=E_0\psi_0$ 恒等。④C 守恒量：定态概率密度不显含时间。J 一致性（本域必做）：$[\hat a,\hat a^\dagger]=1$、$\int|\psi_0|^2dx=1$。I 独立方法（可选加分项）：Hermite 多项式级数截断得同一能谱。

**Key Checks:** 零点能不可漏；$\hat a$ 非厄米、不是可观测量的直接对应；高斯归一化完整。

**Failure Modes:** $E_0=0$；$[\hat a,\hat a^\dagger]=0$；归一化因子漏 $\pi^{1/4}$；把 $\hat a$ 当厄米算符；未回代定态方程。

## TC-QNT-003

**Test ID:** TC-QNT-003

**Input:** "证明 $[\hat x,\hat p]=i\hbar$，并写出对应的不确定性关系。"

**Expected Classification:** 基础量子力学（算符与对易关系）

**Expected Behavior:** 对任意可微试探函数 $f$：$[\hat x,\hat p]f = \hat x(-i\hbar f') - (-i\hbar)(xf)' = i\hbar f$；不确定性关系 $\Delta x\,\Delta p\ge\hbar/2$。

**Required Verification:** ①F 量纲：$[x][p]=ML^2T^{-1}$ 与 $[\hbar]$ 一致。②L 极限/特例：$\hbar\to0$ 时对易子趋于零，退化为经典可交换。③B 回代：把结果作用到试探函数逐项化简，得 $i\hbar f$。④C 守恒量：N/A（算符代数问题，无动力学守恒量）。J 一致性（本域必做）：$\hat x,\hat p$ 厄米、不确定性关系系数 $\ge1/2$。

**Key Checks:** $\hat p=-i\hbar d/dx$ 的符号；算符顺序保持；试探函数任意可微；不确定性不等号方向。

**Failure Modes:** $\hat p=+i\hbar\,d/dx$；交换算符顺序；直接断言 $[x,p]=i\hbar$ 而不展开；不确定性写成 $\le\hbar/2$ 或漏 $1/2$。

## TC-TUT-001

**Test ID:** TC-TUT-001

**Input:** "帮我看看我写的这步对不对：$L = T - V$ 这里为什么没有负号？"

**Expected Classification:** 学生诊断（触发分流）

**Expected Behavior:** 识别检查意图进入诊断模式；不输出模板 A 六节完整答案；按模板 E 字段输出完整性结论、核验结果、问题定位、概念误区、修正建议、确认题。

**Required Verification:** 本用例为流程断言：输出含模板 E 六字段；未收到"直接解答"意图时不展开完整答案。①F-④C 数值核验不适用，标 `N/A（流程用例）`。

**Key Checks:** 只发题目、无检查词时不进诊断模式；含检查词时进诊断模式；诊断结束前不展开完整解答。

**Failure Modes:** 无视检查意图直接给完整六节答案；重复询问用户意图；输出不含模板 E 六字段。

## TC-TUT-002

**Test ID:** TC-TUT-002

**Input:** "我写到一半卡住了，目前只写了：对单摆取广义坐标 $\theta$，写 $L = T - V$，后面不会了。"

**Expected Classification:** 学生诊断（不完整作答）

**Expected Behavior:** 完整性结论为不完整（缺：推导、答案）；直接指出缺项并给下一步具体写什么（写出 $T = \frac12 ml^2\dot\theta^2$、$V = mgl(1-\cos\theta)$，再代入 E-L 方程）；不展开完整解答；不做提示分级。

**Required Verification:** 本用例为流程断言：输出含缺项结论与可执行的具体下一步；无 H1-H4 式多级提示；无模板 A 完整答案。①F-④C 数值核验不适用，标 `N/A（流程用例）`。

**Key Checks:** 完整性四要素；下一步指令具体可执行；不替学生完成整题。

**Failure Modes:** 直接给出完整六节答案；只写"继续做"而没有具体下一步；引入多级提示。

## TC-TUT-003

**Test ID:** TC-TUT-003

**Input:** "RC 放电，我算得 $V(t) = V_0 e^{+t/\tau}$，哪里不对？"

**Expected Classification:** 学生诊断（完整但错误）

**Expected Behavior:** 完整性结论为完整；核验 ①F PASS、②L FAIL（$t\to\infty$ 时增长发散而非衰减到 0）、③B FAIL（$V_0e^{+t/\tau}$ 不满足 $\dot V + V/\tau = 0$）、④C FAIL（电容能量单调增加与电阻耗散矛盾）；定位第一个错误为指数符号；概念误区为电流方向约定 $I = -C\dot V$ 与 KVL 符号；修正建议为 $V = V_0e^{-t/\tau}$；给确认题。

**Required Verification:** ①F 量纲：$[V_0e^{\pm t/\tau}] = \mathrm{V}$ PASS。②L 极限/特例：$t\to\infty$ 增长解 FAIL。③B 回代：正号解不满足 $\dot V + V/\tau = 0$ FAIL。④C 守恒量：能量单调增加与电阻耗散矛盾 FAIL。

**Key Checks:** 指数符号；用极限与回代定位第一个错误；输出概念误区与确认题。

**Failure Modes:** 只判对错不定位第一步；未给出概念误区；未出确认题；直接重写整题。

## TC-TUT-004

**Test ID:** TC-TUT-004

**Input:** "无限深势阱我算到 $\psi_n = \sqrt{2/L}\sin(n\pi x/L)$、$E_n = n^2\pi^2\hbar^2/(2mL^2)$，对吗？"

**Expected Classification:** 学生诊断（完整且正确）

**Expected Behavior:** 完整性结论为完整；核验 ①F PASS、②L PASS（$L\to\infty$ 能级间距趋于零）、③B PASS（$\psi_n''$ 代回定态方程恒等）、④C PASS（定态概率密度不显含时间）；不只写 PASS，另给一道概念确认题（如"为什么 $n=0$ 不是允许的态？"）。

**Required Verification:** ①F 量纲：$E_n$ 量纲为能量 PASS。②L 极限/特例：$L\to\infty$ 时能级间距趋于零 PASS。③B 回代：$\psi_n''=-(n\pi/L)^2\psi_n$ 代入定态方程恒等 PASS。④C 守恒量：定态概率密度不显含时间 PASS。J 一致性（本域必做）：归一化与正交 PASS。

**Key Checks:** 正确作答也要做概念确认；确认题触及适用条件或边界条件；确认题不是附加答案。

**Failure Modes:** 只输出"正确"或 PASS 不提问；不执行核验；把确认题写成附加答案。
