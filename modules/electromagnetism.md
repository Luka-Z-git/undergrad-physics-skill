# 电磁学模块 (Electromagnetism)

## 适用范围

本模块覆盖本科《电磁学》课程：静电场（库仑定律、高斯定律、叠加原理、电势）、静磁场（洛伦兹力、安培环路定理、毕奥-萨伐尔定律、磁场能量）、矢量分析（梯度/散度/旋度、常用恒等式、边界条件）、电容与电感、电路暂态（RC/RL/RLC）、麦克斯韦方程组的基础应用（积分/微分形式、电磁波、坡印廷矢量）。每个子域给出：识别特征、建模步骤、验证组合（F/D/B/C/L/E/I/J，定义见 `verification_engine.md`）、必须检查的适用条件、常见错误表。引用任何定律时先声明其适用条件；验证未通过不得输出最终答案。

## 0. 方法选择表

按系统特征选方法；方法不唯一时，选推导最短、验证最直接者，并在建模节用一句话说明理由。

| 系统特征 | 首选方法 | 选择理由 | 本域特化验证 |
|---|---|---|---|
| 静电荷分布求 $E$ 或 $V$，高对称（球/柱/平面） | 高斯定律（§1） | 通量积分化为代数 | J（边界条件）、I（库仑积分对照） |
| 静电荷分布求 $E$ 或 $V$，无足够对称性 | 库仑定律积分 + 叠加（§1） | 逐元积分适用任意分布 | E（数值积分）、L（远场点电荷极限） |
| 电流分布求 $B$，高对称（无限长直导线/螺线管/环） | 安培环路定理（§2） | 环路积分化为代数 | L（近场/轴上场已知结果） |
| 电流分布求 $B$，一般几何 | 毕奥-萨伐尔定律（§2） | 对任意电流路径积分 | J（$\nabla\cdot\mathbf B=0$、$\oint\mathbf B\cdot d\mathbf l$ 对照） |
| 带电粒子在电磁场中的运动 | 洛伦兹力方程（§2） | 直接写运动方程 | B（回代运动方程）、C（速率/能量） |
| 含 $R$/$C$/$L$ 的集总电路暂态 | KCL/KVL + 微分方程（§3） | 集总参数模型 | B（解回代 ODE）、L（$t\to0,\infty$）、C（能量） |
| 时变磁通、运动导体 | 法拉第定律 + 楞次定律（§3） | 统一处理感生与动生电动势 | I（感生 vs 动生两种推导）、L（$\dot{\mathbf B}\to0$、$v\to0$） |
| 矢量恒等式、场论证明 | 分量展开（§4） | 直接逐项比较 | J（恒等式两侧展开）、E（特殊场抽查） |

## 1. 静电场与电势 (Electrostatics)

### 识别特征

- 电荷静止或电荷分布不随时间变化；介质可视为真空、线性介质或导体边界。
- 待求量为场强 $\mathbf E$、电势 $V$、电场力、电容、能量。
- 系统满足叠加原理；导体处于静电平衡。

### 建模步骤

1. 声明单位制（SI/CGS）与电荷分布类型（点电荷/线/面/体分布）。
2. 做对称性检查：球对称、无限长柱对称、无限大平面对称 → 高斯定律；否则库仑积分。
3. 高斯法：选高斯面，利用对称性把 $\mathbf E$ 从积分中提出，写

$$
\oint_S \mathbf E\cdot d\mathbf A = \frac{Q_{\mathrm{enc}}}{\varepsilon_0}
$$

4. 库仑法：对电荷元积分，或点电荷叠加：

$$
\mathbf E(\mathbf r) = \frac{1}{4\pi\varepsilon_0}\int \frac{\rho(\mathbf r')(\mathbf r-\mathbf r')}{|\mathbf r-\mathbf r'|^3}\,dV'
$$

5. 电势：$V(\mathbf r) = \frac{1}{4\pi\varepsilon_0}\int \frac{\rho(\mathbf r')}{|\mathbf r-\mathbf r'|}\,dV'$（取无穷远为零势参考时）；由 $E = -\nabla V$ 复核。
6. 导体边界：静电平衡时导体内部 $\mathbf E=0$、电荷分布在表面；写出界面边界条件。

### 验证组合

必查 F, L, B（C 适用时）；建议加做 D, E, I, J。

### 必须检查的适用条件

- 静电场要求 $\partial\mathbf E/\partial t = 0$；时变电磁场中 $\mathbf E$ 不再由 $\rho$ 单独决定。
- 高斯定律对任意闭合面恒成立，但只有电荷分布具备足够对称性时才可直接解出 $\mathbf E$。
- 电势在静电场中才有单值定义；法拉第感应电场非保守，不能定义全局电势。
- 叠加原理成立要求场方程线性；强场非线性介质需另作处理。
- 取无穷远为零势参考只适用于有限电荷分布；无限长带电直线须改用有限参考点。

### 常见错误

| 错误 | 正确 |
|---|---|
| 电势按矢量叠加 | $V$ 是标量，代数相加；$\mathbf E$ 才按分量矢量相加 |
| 写 $\mathbf E=+\nabla V$ | $\mathbf E=-\nabla V$ |
| 高斯面与对称性不匹配 | 高斯面上 $\mathbf E$ 须大小恒定或垂直/平行于面元 |
| 导体内部 $\mathbf E\neq0$ | 静电平衡时 $\mathbf E=0$，净电荷在表面 |
| 用无限长分布时仍取无穷远为零势 | 有限参考点，否则积分发散 |
| 把介质中 $\mathbf D=\varepsilon_0\mathbf E$ | 线性介质中 $\mathbf D=\varepsilon\mathbf E$，边界条件分开写 |

## 2. 静磁场与矢量分析 (Magnetostatics & Vector Analysis)

### 识别特征

- 稳定电流（$\nabla\cdot\mathbf J=0$）产生磁场；或带电粒子/电流元在已知磁场中受力。
- 待求量为 $\mathbf B$、磁场力、磁通、电感、磁场能量。
- 需要矢量恒等式或边界条件检验场解。

### 建模步骤

1. 声明电流类型（线电流 $I$、面电流 $\mathbf K$、体电流 $\mathbf J$）与坐标系。
2. 对称性分析：无限长直导线（柱对称）用安培环路：

$$
\oint_C \mathbf B\cdot d\mathbf l = \mu_0 I_{\mathrm{enc}}
$$

3. 一般几何用毕奥-萨伐尔：

$$
d\mathbf B = \frac{\mu_0}{4\pi}\frac{I\,d\mathbf l'\times(\mathbf r-\mathbf r')}{|\mathbf r-\mathbf r'|^3}
$$

4. 洛伦兹力：$\mathbf F = q(\mathbf E + \mathbf v\times\mathbf B)$；对电流元 $\mathbf F = I\,d\mathbf l\times\mathbf B$。
5. 用矢量恒等式与边界条件核对：$\nabla\cdot\mathbf B=0$，$\nabla\times\mathbf B = \mu_0\mathbf J$（静磁），$B_{1n}=B_{2n}$，$H_{1t}-H_{2t}=K_{\mathrm{free}}$。
6. 磁场能量：$U = \frac{1}{2}LI^2 = \int \frac{B^2}{2\mu_0}\,dV$（线性无耗散介质）。

### 验证组合

必查 F, L, B（C 适用时）；建议加做 I, E, J。

### 必须检查的适用条件

- 静磁学要求电流稳定（$\nabla\cdot\mathbf J=0$）；含位移电流时须用麦克斯韦-安培方程。
- 安培环路定理恒成立，但只有高对称电流分布时才可把 $\mathbf B$ 从积分提出。
- 磁力不做功：$q\mathbf v\times\mathbf B$ 垂直于速度，速率不变；能量变化只能来自电场或非电磁力。
- 线性介质中 $\mathbf B=\mu\mathbf H$；铁磁材料非线性不适用。
- 毕奥-萨伐尔叉积方向：$d\mathbf l'\times(\mathbf r-\mathbf r')$，顺序写反方向翻转。

### 常见错误

| 错误 | 正确 |
|---|---|
| 洛伦兹磁力做功改变速率 | 磁力不做功，只改变方向 |
| 叉积顺序写反 | 毕奥-萨伐尔与 $\mathbf v\times\mathbf B$ 按右手定则逐项核对 |
| 无对称性仍用安培环路硬解 | 安培定律恒成立但不可解；改用毕奥-萨伐尔 |
| 把 $\mathbf B$ 与 $\mathbf H$ 混用 | 真空 $\mathbf B=\mu_0\mathbf H$；介质与边界条件分别处理 |
| 静磁时漏掉位移电流 | 时变场须用 $\nabla\times\mathbf B = \mu_0\mathbf J + \mu_0\varepsilon_0\partial\mathbf E/\partial t$ |
| 磁场线画成起止于源 | $\nabla\cdot\mathbf B=0$，磁力线闭合 |

## 3. 电路暂态 (RC/RL/RLC Circuits)

### 识别特征

- 集总电路：电阻、电容、电感与直流/简谐电源；电路尺寸远小于波长（准静态）。
- 待求量为电流、电压、时间常数、能量、暂态解。

### 建模步骤

1. 标注电流方向与回路方向；写 KCL（电荷守恒）与 KVL（能量守恒）。
2. 用电容/电感元件关系：$I=C\,dV/dt$（充电方向约定）、$V_L = L\,dI/dt$。
3. RC 放电：

$$
\frac{dV}{dt} + \frac{1}{RC}V = 0, \qquad V(t)=V_0 e^{-t/\tau},\ \tau=RC
$$

4. RL 放电：

$$
L\frac{dI}{dt} + RI = 0, \qquad I(t)=I_0 e^{-t/\tau},\ \tau=L/R
$$

5. RLC 串联：$L\ddot q + R\dot q + q/C = 0$；判别欠阻尼/临界/过阻尼，写 $\omega_0 = 1/\sqrt{LC}$、$\alpha=R/(2L)$、$\omega_d=\sqrt{\omega_0^2-\alpha^2}$。
6. 能量复核：$U_C = \frac12 CV^2$、$U_L=\frac12 LI^2$、耗散功率 $P_R=I^2R$。

### 验证组合

必查 F, L, B（C 适用时）；建议加做 E, D。

### 必须检查的适用条件

- 集总电路要求尺寸远小于电磁波长；高频/长线须用分布参数模型。
- 电容、电感为线性元件；非线性元件需另写伏安特性。
- 能量守恒只在无外部注入或正确计入电源功率时成立；RC 放电直接验证 $P_R=-dU_C/dt$。
- $t\to\infty$ 稳态：电容开路、电感短路（直流）。

### 常见错误

| 错误 | 正确 |
|---|---|
| 时间常数写成 $RC$ 的倒数 | RC 放电 $\tau=RC$，RL 放电 $\tau=L/R$ |
| 指数符号写反 | 放电 $e^{-t/\tau}$，充电 $1-e^{-t/\tau}$ |
| 电流方向约定与 $I=C\,dV/dt$ 不一致 | 先定回路方向再写元件关系，符号全程一致 |
| 把电容/电感串并联规则与电阻混用 | 电容并联相加、串联倒数；电阻相反 |
| RLC 欠阻尼判别只看 $R$ | 判别 $R^2$ 与 $4L/C$ 的大小 |
| 忽略电容初始电压/电感初始电流 | 一阶暂态必须用初始条件定常数 |

## 4. 麦克斯韦方程组基础应用 (Maxwell's Equations)

### 识别特征

- 时变电磁场、电磁波、位移电流、坡印廷矢量。
- 待求量为场方程、波速、场与波的能量流。

### 建模步骤

1. 写出微分形式：

$$
\nabla\cdot\mathbf E = \frac{\rho}{\varepsilon_0}, \qquad
\nabla\cdot\mathbf B = 0
$$

$$
\nabla\times\mathbf E = -\frac{\partial\mathbf B}{\partial t}, \qquad
\nabla\times\mathbf B = \mu_0\mathbf J + \mu_0\varepsilon_0\frac{\partial\mathbf E}{\partial t}
$$

2. 自由空间（$\rho=0,\mathbf J=0$）取旋度得波动方程：

$$
\nabla^2\mathbf E = \mu_0\varepsilon_0\frac{\partial^2\mathbf E}{\partial t^2}, \qquad c=\frac{1}{\sqrt{\mu_0\varepsilon_0}}
$$

3. 平面波：$\mathbf E\perp\mathbf B\perp$ 传播方向，$|\mathbf E|=c|\mathbf B|$。
4. 能量流：坡印廷矢量 $\mathbf S = \frac{1}{\mu_0}\mathbf E\times\mathbf B$；能量密度 $u=\frac12\varepsilon_0E^2+\frac{1}{2\mu_0}B^2$。
5. 界面边界条件：$D_{1n}-D_{2n}=\sigma_{\mathrm{free}}$、$E_{1t}=E_{2t}$、$B_{1n}=B_{2n}$、$H_{1t}-H_{2t}=K_{\mathrm{free}}$。

### 验证组合

必查 F, L, B（C 适用时）；建议加做 J, E, D。

### 必须检查的适用条件

- 经典电磁学，非相对论场变换；高速参考系变换超出范围。
- 位移电流不可省：去掉后与电荷守恒矛盾。
- 平面波解只适用于自由空间远场；导体/边界附近须满足边界条件。
- 静场极限：$\partial/\partial t\to0$ 应分别退化为高斯定律、安培环路定律。

### 常见错误

| 错误 | 正确 |
|---|---|
| 法拉第定律缺负号 | $\nabla\times\mathbf E=-\partial\mathbf B/\partial t$ |
| 麦克斯韦-安培方程漏位移电流 | 补 $\mu_0\varepsilon_0\partial\mathbf E/\partial t$ |
| 平面波中 $\mathbf E$ 与 $\mathbf B$ 平行 | 互相垂直且垂直于传播方向 |
| 把 $|\mathbf E|=c|\mathbf B|$ 用在导电介质 | 自由空间才成立；介质中波速与阻抗改变 |
| 边界条件只列 $E$ 或只列 $B$ | 法向/切向四式按界面分别列出 |

## 5. 常用公式与陷阱 (Formulas & Traps)

### 公式速查

库仑定律与高斯定律：

$$
\mathbf F = \frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r^2}\hat{\mathbf r}, \qquad
\oint_S \mathbf E\cdot d\mathbf A = \frac{Q_{\mathrm{enc}}}{\varepsilon_0}
$$

电势与场强：

$$
V(\mathbf r)=\frac{1}{4\pi\varepsilon_0}\frac{Q}{r}, \qquad
\mathbf E = -\nabla V
$$

电容/电感：

$$
C=\frac{Q}{V}=\varepsilon_0\frac{A}{d}, \qquad
L=\frac{N\Phi}{I}, \qquad
U_C=\frac12 CV^2,\quad U_L=\frac12 LI^2
$$

电路时间常数与 RLC：

$$
\tau_{RC}=RC, \qquad \tau_{RL}=\frac{L}{R}, \qquad
\omega_0=\frac{1}{\sqrt{LC}}, \qquad \alpha=\frac{R}{2L}
$$

洛伦兹力、毕奥-萨伐尔、安培环路：

$$
\mathbf F=q(\mathbf E+\mathbf v\times\mathbf B), \qquad
d\mathbf B=\frac{\mu_0}{4\pi}\frac{I\,d\mathbf l'\times(\mathbf r-\mathbf r')}{|\mathbf r-\mathbf r'|^3}, \qquad
\oint_C \mathbf B\cdot d\mathbf l=\mu_0 I_{\mathrm{enc}}
$$

法拉第定律：

$$
\mathcal{E}=-\frac{d\Phi_B}{dt}, \qquad
\Phi_B=\int_S \mathbf B\cdot d\mathbf A
$$

矢量恒等式：

$$
\nabla\times(\nabla\varphi)=0, \qquad
\nabla\cdot(\nabla\times\mathbf A)=0, \qquad
\nabla\times(\nabla\times\mathbf A)=\nabla(\nabla\cdot\mathbf A)-\nabla^2\mathbf A
$$

### 跨域陷阱总表

| 错误 | 正确 |
|---|---|
| SI 与 CGS 混用（$k=1$ 与 $1/4\pi\varepsilon_0$ 混用） | 全程单一单位制，常数换算一致 |
| 电势按矢量相加 | 标量代数相加 |
| 高斯/安培无对称硬套 | 先做对称性分析，再决定是否可提取场 |
| 漏位移电流 | 时变场必须补 |
| 磁力做功 | 磁力不做功，能量变化找电场/外力 |
| 时间常数与指数符号错 | $\tau=RC$、$\tau=L/R$，放电用 $e^{-t/\tau}$ |
| 数值结果不写单位 | 数值答案一律带单位 |

本模块与 `output_templates.md` 配合：解答按模板 A 六节结构输出；验证逐条给出 PASS/FAIL，摘要格式见 `verification_engine.md`。
