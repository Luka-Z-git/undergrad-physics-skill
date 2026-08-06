# 理论力学模块 (Theoretical Mechanics)

## 适用范围

本模块覆盖中文本科《理论力学》课程：牛顿力学（质点系、惯性系、受力分析）、拉格朗日力学（广义坐标、完整/非完整约束、E-L 方程、广义力）、哈密顿力学（正则方程、能量守恒判据）、守恒量与对称性（循环坐标、Noether 定理）、小振动与简正模式、刚体基础（平面运动、转动惯量、纯滚动）、非惯性系（惯性力、离心力、科里奥利力）。每个子域给出：识别特征、建模步骤、验证组合（F/D/B/C/L/E/I/J，定义见 `verification_engine.md`）、必须检查的适用条件、常见错误表。引用任何定律时先声明其适用条件；验证未通过不得输出最终答案。

## 0. 方法选择表

按系统特征选方程体系；方法不唯一时，选推导最短、验证最直接者，并在建模节用一句话说明理由。

| 系统特征 | 首选方法 | 选择理由 | 本域特化验证 |
|---|---|---|---|
| 质点/质点系，约束少，力为已知函数，需约束反力 | 牛顿力学（§1） | 受力图直接列方程，反力由约束方程解出 | D（摩擦/静摩擦条件） |
| 完整约束多、自由度少 | 拉格朗日力学（§2） | 广义坐标消去约束，方程数最少 | C 守恒量强校验 |
| 需相空间、正则方程或守恒/泊松括号分析 | 哈密顿力学（§3） | 二阶方程化为一阶相流 | J 一致性 |
| 平衡点附近小幅运动、多自由度耦合 | 小振动（§5） | 线性化后求简正模式与频率 | J（M-正交、特征值回代） |
| 刚体平面运动、纯滚动、碰撞 | 刚体基础（§6） | 质心定理 + 转动方程 | B 回代约束条件 |
| 观察者在加速或旋转参考系 | 非惯性系（§7） | 显式补惯性力项 | I 惯性系重解 |

## 1. 牛顿力学 (Newtonian Mechanics)

### 识别特征

- 质点或质点系，约束少或约束可显式写出；力（重力、弹性力、张力、摩擦力）为已知函数。
- 待求量为加速度、轨道或约束反力；可处理单自由度与多自由度。
- 系统在惯性系内运动；非惯性系问题见 §7。

### 建模步骤

1. 选惯性系与坐标系：笛卡尔、极坐标或自然坐标（切向/法向），标注正方向。
2. 隔离物体画受力图：只画作用在该物体上的真实力；多体系统逐个隔离。
3. 沿坐标方向分解，写分量方程 $m\ddot x = F_x$、$m\ddot y = F_y$。
4. 写出约束方程（绳长不变、接触、纯滚动），与运动方程联立；反力由约束方程解出。
5. 积分求 $x(t)$，用初始条件定积分常数；检查解的定义域与符号。

### 验证组合

必查 F, L, B（C 适用时）；建议加做 D, E, I。

### 必须检查的适用条件

- 牛顿第二定律只在惯性系成立；地表问题将地球近似为惯性系须声明。
- 绳、轻杆、光滑面为理想化模型；有摩擦时须引入动/静摩擦模型并声明摩擦系数。
- 力须为已知函数；含时力、位置相关力、速度相关力（阻尼）分别处理。

### 常见错误

| 错误 | 正确 |
|---|---|
| 非惯性系中直接写 $m\mathbf a=\mathbf F$ | 补惯性力 $-m\mathbf a_0$、离心力与科里奥利力（见 §7） |
| 把作用力与反作用力画在同一物体上 | 隔离体受力图只画该物体所受的力 |
| 动能写成 $mv^2$ | $T=\frac12 mv^2$，1/2 因子不可省 |
| 极坐标加速度只写 $r\ddot\theta$ | $a_\theta = r\ddot\theta + 2\dot r\dot\theta$ |
| 绳张力默认处处相等 | 仅轻绳或无摩擦滑轮才成立 |

## 2. 拉格朗日力学 (Lagrangian Mechanics)

### 识别特征

- 完整约束多、自由度少，用广义坐标消去约束最省力。
- 力为保守力或可并入广义力；待求运动方程、周期、守恒量。
- 复杂约束系统：双摆、滑轮组、轮滚不滑、珠子沿固定曲线。

### 建模步骤

1. 求自由度 $s = 3N - k$（质点系三维情形，$k$ 为完整约束数；平面系统为 $2N - k$），选广义坐标 $q_i$，坐标映射须一一可逆。
2. 用广义速度写出动能 $T$，势能 $V$，令 $L = T - V$。
3. 判别约束类型：完整约束直接消元；非完整约束用拉格朗日乘子或 d'Alembert 方法。
4. 非保守力写广义力 $Q_i = \sum_j \mathbf F_j\cdot\partial\mathbf r_j/\partial q_i$，代入 E-L 方程：

$$
\frac{d}{dt}\frac{\partial L}{\partial\dot q_i} - \frac{\partial L}{\partial q_i} = Q_i
$$

5. 解运动方程，用初始条件定常数；用守恒量复核。

### 验证组合

必查 F, L, B（C 适用时）；建议加做 I, E。

### 必须检查的适用条件

- E-L 方程要求完整约束；非完整约束不可直接套用。
- 存在摩擦/阻尼时 $L=T-V$ 不完整描述动力学，须加广义力或 Rayleigh 耗散函数。
- $L$ 加全导数 $dF(q,t)/dt$（$F$ 仅依赖 $q,t$）不改变运动方程（等价拉格朗日量）；$F$ 含 $\dot q$ 时边界项不可忽略；含非完整约束时以乘子方程为准，不能只凭 $L$ 形式判断。

### 常见错误

| 错误 | 正确 |
|---|---|
| 动能中漏 1/2 或漏质量因子 | 逐项核对 $T=\frac12 m\dot x^2$ 等形式 |
| 混淆 $\partial L/\partial q$ 与 $\partial L/\partial\dot q$ | E-L 第一项对坐标求偏导，第二项对速度求偏导 |
| 对非完整约束直接用 E-L 方程 | 用拉格朗日乘子法或改写成完整约束 |
| 摩擦无处安放 | 写入广义力 $Q_i$ 或 Rayleigh 耗散函数 |
| 因 $L$ 不显含 $t$ 就断言 $E$ 守恒 | 定常约束下广义能量才等于机械能 |

## 3. 哈密顿力学 (Hamiltonian Mechanics)

### 识别特征

- 需相空间 $(q,p)$ 描述、正则方程、泊松括号或正则变换。
- 判断守恒量与运动积分；从 $L$ 做 Legendre 变换。
- 与量子力学的经典对应、微扰或相流分析。

### 建模步骤

1. 求广义动量 $p_i = \partial L/\partial\dot q_i$；验证 Hessian 矩阵 $\partial^2 L/\partial\dot q_i\partial\dot q_j$ 非退化（可逆）。
2. 解出 $\dot q_i(q,p,t)$，做 Legendre 变换 $H = \sum_i p_i\dot q_i - L$。
3. 写正则方程 $\dot q_i = \partial H/\partial p_i$、$\dot p_i = -\partial H/\partial q_i$。
4. 判据：$\partial H/\partial t = 0 \Rightarrow H$ 守恒；$H = E$ 还需约束定常且 $T$ 为 $\dot q$ 的二次齐次式。
5. 解方程或找循环坐标降阶；用守恒量验证。

### 验证组合

必查 F, L, B（C 适用时）；J 为本域必做；建议加做 I, E。

### 必须检查的适用条件

- Legendre 变换须可逆（非奇异拉格朗日量）；奇异系统（规范理论）超出本科范围，须声明。
- $H\neq T+V$ 的情形：$H$ 显含时间、速度相关势、非定常约束。
- 正则方程给出的是 $H$ 守恒；能量守恒需单独判据。

### 常见错误

| 错误 | 正确 |
|---|---|
| 无条件写 $H=T+V$ | 先做 Legendre 变换，再核对 $H$ 表达式 |
| 认为 $H$ 守恒即能量守恒 | $\partial H/\partial t=0$ 只保证 $H$ 守恒；$H\neq E$ 时两者不同 |
| 正则方程符号写反 | $\dot p_i = -\partial H/\partial q_i$ |
| $H$ 中残留 $\dot q$ | 先用 $p_i = \partial L/\partial\dot q_i$ 消去 $\dot q$ |
| 有循环坐标却不判动量守恒 | $\partial H/\partial q_j = 0 \Rightarrow p_j$ 守恒 |

## 4. 守恒量与对称性 (Conservation Laws & Noether)

### 识别特征

- 问"哪些量守恒"、求运动积分，或利用守恒量降阶求解。
- 系统具有平移、转动或时间平移对称性。
- 用守恒量复核数值解（验证引擎方法 C）。

### 建模步骤

1. 写出 $L$（或 $H$），显式列出其依赖变量。
2. 循环坐标判据：$\partial L/\partial q_j = 0 \Rightarrow p_j$ 守恒。
3. $\partial L/\partial t = 0 \Rightarrow h = \sum_i p_i\dot q_i - L$ 守恒（时间平移对称的 Noether 荷）。
4. 空间平移对称 $\Rightarrow$ 总动量守恒；转动对称 $\Rightarrow$ 角动量守恒（相对固定点或质心）。
5. 用守恒量降阶求解，并数值抽样复核守恒性。

### 验证组合

必查 F, L, B, C（守恒量即本题目标，必须验证）；建议加做 I, E。

### 必须检查的适用条件

- 对称性须在整个运动域成立；外场不均匀或存在边界会破缺对称性。
- 耗散系统机械能不守恒；Noether 定理要求作用量具有相应连续对称性。
- 角动量守恒须相对固定点或质心定义。

### 常见错误

| 错误 | 正确 |
|---|---|
| 有循环坐标却断言该坐标不变 | 循环坐标给出动量守恒，坐标本身可随时间变化 |
| 有摩擦仍用机械能守恒 | 先算耗散功 $\Delta E = \int \mathbf F_f\cdot d\mathbf r$ |
| 角动量参考点随意选择 | 固定点或质心；换参考点须换算 |
| 把 $p=\mathrm{const}$ 误当 $p=0$ | 守恒量为积分常数，可非零 |
| 对称性被外场破坏仍假设守恒 | 先检查外力是否依赖对应坐标 |

## 5. 小振动与简正模式 (Small Oscillations & Normal Modes)

### 识别特征

- 平衡点附近小幅运动；待求频率、简正模式、正常坐标。
- 多自由度耦合系统：耦合摆、双摆、分子振动。

### 建模步骤

1. 求平衡构型：$\partial V/\partial q_i\big|_0 = 0$（保守系统）。
2. 在平衡点展开到二阶：$V = \frac12\sum_{ij} k_{ij}\xi_i\xi_j$、$T = \frac12\sum_{ij} m_{ij}\dot\xi_i\dot\xi_j$，$K,M$ 为对称矩阵。
3. 写矩阵运动方程 $M\ddot{\boldsymbol\xi} + K\boldsymbol\xi = 0$。
4. 令 $\boldsymbol\xi = \mathbf A e^{i\omega t}$，得特征方程 $\det(K - \omega^2 M) = 0$。
5. 解 $\omega_\alpha^2$ 与特征向量，构造正常坐标 $\eta_\alpha$（$M$-正交归一）；$\omega^2>0$ 为稳定平衡。

### 验证组合

必查 F, L, B（C 适用时）；J 为本域必做；建议加做 E, D。

### 必须检查的适用条件

- 线性化要求振幅小；$\omega^2>0$ 才振荡，$\omega^2<0$ 为不稳定平衡，须指出。
- 零频模式对应无回复力的平动/转动方向，须单独识别。
- 有阻尼或驱动力时频率改变，须在矩阵方程中补相应项。

### 常见错误

| 错误 | 正确 |
|---|---|
| 势能漏 1/2：写成 $V=kx^2$ | $V=\frac12 kx^2=\frac12 m\omega^2 x^2$ |
| 用 $\det(K-\omega^2 I)$ | 用 $\det(K-\omega^2 M)=0$，质量矩阵不可省 |
| 平衡点求错（未消约束） | 先消约束或用乘子法，再求 $\partial V/\partial q_i=0$ |
| 把频率 $f$ 当角频率 $\omega$ | $\omega = 2\pi f$；注明单位 $\mathrm{rad/s}$ |
| 特征向量不做 $M$-正交核对 | 验证 $\mathbf A_\alpha^T M \mathbf A_\beta \propto \delta_{\alpha\beta}$ |

## 6. 刚体基础 (Rigid Body Basics)

### 识别特征

- 刚体平面运动（平动 + 转动）、纯滚动、碰撞问题。
- 待求角加速度、质心加速度、约束反力。

### 建模步骤

1. 选参考点（质心 C 或固定点 O）；运动学 $\mathbf v_P = \mathbf v_C + \boldsymbol\omega\times\mathbf r_{PC}$。
2. 计算转动惯量：质心轴 $I_C$，平行轴定理 $I = I_C + md^2$。
3. 对质心写 $\sum\mathbf F = m\mathbf a_C$ 与 $\sum\boldsymbol\tau_C = I_C\dot{\boldsymbol\omega}$。
4. 纯滚动条件 $\dot x = R\dot\theta$（无滑动）；静摩擦方向按相对运动趋势判定。
5. 能量法：$T = \frac12 mv_C^2 + \frac12 I_C\omega^2$；理想约束不做功。

### 验证组合

必查 F, L, B（C 适用时）；建议加做 I, E。

### 必须检查的适用条件

- 转动方程只对固定点或质心成立；对一般点须补含质心加速度的附加力矩项。
- 纯滚动要求静摩擦未达上限：$f_s \le \mu_s N$；否则转为滑动。
- 角动量守恒仅当外力矩为零。

### 常见错误

| 错误 | 正确 |
|---|---|
| 对非质心、非固定点直接写 $\tau = I\alpha$ | 只对固定点/质心写；一般点补附加力矩项 |
| 纯滚动默认 $f = \mu_s N$ | $f$ 由约束决定，须检验 $f \le \mu_s N$ |
| 平行轴定理漏 $md^2$ | $I = I_C + md^2$ |
| 纯滚动误用动摩擦做功 | 纯滚动为静摩擦，理想情形不做功 |
| 动能只写转动项 | $T = \frac12 mv_C^2 + \frac12 I_C\omega^2$ 两项齐备 |

## 7. 非惯性系 (Non-Inertial Frames)

### 识别特征

- 观察者位于加速或旋转参考系：电梯、转盘、地球自转、傅科摆。
- 涉及惯性力、离心力、科里奥利力、欧拉力。

### 建模步骤

1. 声明惯性系 S 与动系 S'：相对平动加速度 $\mathbf a_0$、角速度 $\boldsymbol\Omega$。
2. 在 S' 中写运动方程：

$$
m\mathbf a' = \mathbf F - m\mathbf a_0 - m\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r') - 2m\boldsymbol\Omega\times\mathbf v' - m\dot{\boldsymbol\Omega}\times\mathbf r'
$$

3. 识别各项并标注为惯性力（虚构力）；$\dot{\boldsymbol\Omega}=0$（角速度恒定）时欧拉项为零，定轴变速转动时欧拉项不为零。
4. 求解后做极限检查：$\mathbf a_0\to0$、$\boldsymbol\Omega\to0$ 还原惯性系方程。
5. 复核量纲与方向（科里奥利力用叉积右手定则）。

### 验证组合

必查 F, L, B（C 适用时）；建议加做 I, E。

### 必须检查的适用条件

- 惯性力只在非惯性系出现；解题时显式声明所用参考系。
- 科里奥利力与速度相关，不可并入势能；离心力可并入定轴旋转势能 $-\frac12 m\Omega^2 r'^2$（$r'$ 为到转轴的垂直距离）。
- 地球自转 $\Omega \approx 7.27\times10^{-5}\,\mathrm{rad/s}$；低速小尺度问题常可忽略，忽略时须声明。

### 常见错误

| 错误 | 正确 |
|---|---|
| 漏平动惯性力 $-m\mathbf a_0$ | 加速参考系必须补 |
| 科里奥利力方向用错 | $-2m\boldsymbol\Omega\times\mathbf v'$ 按叉积右手定则 |
| 把惯性力当真实力 | 标注为虚构力，只出现在非惯性系方程中 |
| 惯性系中引入惯性力 | 惯性系中惯性力为零 |
| 把科里奥利力并入势能 | 仅离心力可并入势能（定轴情形） |

## 8. 常用公式与陷阱 (Formulas & Traps)

### 公式速查

极坐标（平面）：

$$
\mathbf v = \dot r\,\hat{\mathbf e}_r + r\dot\theta\,\hat{\mathbf e}_\theta, \qquad
\mathbf a = (\ddot r - r\dot\theta^2)\,\hat{\mathbf e}_r + (r\ddot\theta + 2\dot r\dot\theta)\,\hat{\mathbf e}_\theta
$$

E-L 方程与广义力：

$$
\frac{d}{dt}\frac{\partial L}{\partial\dot q_i} - \frac{\partial L}{\partial q_i} = Q_i, \qquad
Q_i = \sum_j \mathbf F_j\cdot\frac{\partial\mathbf r_j}{\partial q_i}
$$

哈密顿量与正则方程：

$$
H = \sum_i p_i\dot q_i - L, \qquad
\dot q_i = \frac{\partial H}{\partial p_i},\quad \dot p_i = -\frac{\partial H}{\partial q_i}
$$

小振动特征方程：

$$
\det(K - \omega^2 M) = 0
$$

非惯性系方程（S' 相对 S 以 $\mathbf a_0$、$\boldsymbol\Omega$ 运动）：

$$
m\mathbf a' = \mathbf F - m\mathbf a_0 - m\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r') - 2m\boldsymbol\Omega\times\mathbf v' - m\dot{\boldsymbol\Omega}\times\mathbf r'
$$

转动惯量（质心轴）：细杆 $I=mL^2/12$；圆盘 $I=mR^2/2$；实心球 $I=2mR^2/5$；球壳 $I=2mR^2/3$；平行轴 $I = I_C + md^2$。定点转动欧拉方程（主轴系）：$I_1\dot\omega_1 - (I_2-I_3)\omega_2\omega_3 = \tau_1$（下标循环）。

### 跨域陷阱总表

| 错误 | 正确 |
|---|---|
| SI 与 CGS 混用（kg 配 cm、g 配 N） | 全程单一单位制，数值代入前完成换算 |
| 动能/势能漏 1/2 因子 | $T=\frac12 mv^2$、$\frac12 I\omega^2$、$V=\frac12 kx^2=\frac12 m\omega^2 x^2$ |
| 坐标正方向选择导致符号错误 | 受力图标注正方向，加速度与力同号核对 |
| 非惯性系不用惯性力 | 补 $-m\mathbf a_0$、离心力、科里奥利力 |
| 默认能量守恒 | $\partial H/\partial t=0$ 且无耗散才成立 |
| 小振动漏 $\frac12 m\omega^2 x^2$ 的 1/2 | 势能二阶展开保留 1/2 因子 |
| 数值结果不写单位 | 数值答案一律带单位 |

本模块与 `output_templates.md` 配合：解答按模板 A 五节结构输出；验证逐条给出 PASS/FAIL，摘要格式见 `verification_engine.md`。
