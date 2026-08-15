# 符号计算配方 (Optional Computation)

本模块是**可选**复核工具，按工具门禁 L2–L3 使用：中等题允许一次符号复核，复杂题在环境可用时自动升级一次；L1 简单题禁止调用，用户要求只用手算时也禁止。

**默认纪律**：工具调用必须真实执行并以实际输出为据；未执行时禁止声称“已用 SymPy 验证”。环境无 Python/SymPy 时跳过，不影响主流程。

**规则**：配方输出只是交叉验证，不能代替主流程的 PASS/FAIL 记录；结果与手算不一致时按回溯修正协议处理。每次题目最多执行一次符号复核（用户另有要求除外）。

## 配方总览

| # | 用域 | 工具 | 对应领域 |
|---|---|---|---|
| 1 | ODE 符号求解（E-L / 电路） | SymPy dsolve/diff | 力学, 电磁学 |
| 2 | ODE 数值验证 | SciPy solve_ivp | 力学（非线性） |
| 3 | 矩阵/特征值 | SymPy Matrix | 小振动 |
| 4 | 物理常数 | scipy.constants | 全域 |
| 5 | 代数式化简/量纲 | SymPy simplify | 全域 |
| 6 | 对易子展开 | Sympy + 试探函数 | 量子力学 |

---

## 配方 1：ODE 符号求解（通用）

适用于拉格朗日→E-L 方程、电路暂态等一切可用 `dsolve` 或手动求导验证的 ODE。

**示例 A — 单摆 E-L 方程**：

```python
import sympy as sp

t = sp.symbols('t')
q = sp.Function('q')(t)
m, g, l = sp.symbols('m g l', positive=True)

L = sp.Rational(1,2)*m*l**2*q.diff(t)**2 + m*g*l*sp.cos(q)   # 单摆 L
EL = sp.simplify(sp.diff(sp.diff(L, q.diff(t), t) - sp.diff(L, q)))
print(sp.Eq(EL, 0))
# → -m*l**2*Derivative(q(t),(t,2)) - g*l*m*sin(q(t)) = 0  OK
```

**示例 B — RC 放电**：

```python
t = sp.symbols('t')
V0, R, C = sp.symbols('V0 R C', positive=True)
V = sp.Function('V')(t)
ode = sp.Eq(V.diff(t) + V/(R*C), 0)
sol = sp.dsolve(ode, V, ics={V.subs(t, 0): V0})
print(sol)
# → Eq(V(t), V0*exp(-t/(C*R)))  OK
```

---

## 配方 2：ODE 数值解偏差检测（scipy）

验证非线性系统解析解的数值精度。示例：单摆 $\ddot\theta+(g/l)\sin\theta=0$：

```python
import numpy as np
from scipy.integrate import solve_ivp

g, l = 9.8, 1.0
sol = solve_ivp(lambda t,y: [y[1], -(g/l)*np.sin(y[0])],
                [0,10], [0.1, 0.0], t_eval=np.linspace(0,10,200), rtol=1e-9)
err = np.max(np.abs(sol.y[0] - 0.1*np.cos((g/l)**0.5 * sol.t)))
print("max deviation:", err)   # ~1e-3 量级，远小于振幅
```

---

## 配方 3：矩阵/特征值（小振动）

$$\det(K-\omega^2 M)=0$$ 的符号计算：

```python
import sympy as sp

w2 = sp.symbols('w2', positive=True)  # 代表 ω²
K = sp.Matrix([[2,-1],[-1,2]])        # 刚度矩阵
M = sp.Matrix([[1,0],[0,1]])          # 质量矩阵
print(sp.solve(sp.Eq(sp.det(K-w2*M),0), w2))  # [1, 3]
```

---

## 配方 4–6：常数 / 化简 / 对易子

```python
# 配方 4：物理常数（避免手抄错）
from scipy import constants as c
print(c.hbar, c.e, c.m_e, c.c)  # ħ, e, mₑ, c

# 配方 5：代数式化简与量纲核对
import sympy as sp
n,m,L,hbar = sp.symbols('n m L hbar', positive=True)
E = n**2 * sp.pi**2 * hbar**2 / (2*m*L**2)
print(sp.simplify(E))  # 无限深势阱能级公式确认

# 配方 6：对易子展开
x = sp.symbols('x')
hbar = sp.symbols('hbar', positive=True)
f = sp.Function('f')(x)
comm = x*(-hbar*sp.I*sp.diff(f,x)) - (-hbar*sp.I)*sp.diff(x*f, x)
print(sp.simplify(comm))  # I*ħ·f(x)  OK
```

---

## 何时不适用

- L1 简单题 → 禁止调用
- 环境无 Python/SymPy → 跳过，主流程不受影响
- 纯概念/证明类问题 → 不需要
- 用户要求只用手算 → 不使用
