# 符号计算配方 (Optional Computation)

本模块是**可选**复核工具，不是主流程的一部分。主验证流程（F/D/B/C/L/E/I/J）由推理本身手算执行，任何环境下都可用。仅当**环境中存在 Python + SymPy/SciPy 且用户要求或手算验算不可行**时，才用下面的配方做机器复核。

纪律：
- 配方输出只是**交叉验证**，不能代替主流程的 PASS/FAIL 记录；答案正文仍须手写验算摘要。
- 不硬编码任何本机路径；脚本可直接复制到任意机器运行。
- 配方结果与手算不一致时，按回溯修正协议处理，不得单方面采信某一方。

## 配方 1：拉格朗日量 → 欧拉-拉格朗日方程

输入 $L(q,\dot q)$，输出 E-L 方程。用于验证手算的 E-L 推导。

```python
import sympy as sp

t = sp.symbols('t')
q = sp.Function('q')(t)
m, g, l = sp.symbols('m g l', positive=True)

L = sp.Rational(1,2)*m*l**2*q.diff(t)**2 + m*g*l*sp.cos(q)   # 单摆 L = T - V
dLdq    = sp.diff(L, q)
dLdqdot = sp.diff(L, q.diff(t))
EL = sp.simplify(sp.diff(dLdqdot, t) - dLdq)
print(sp.Eq(EL, 0))        # 期望: -m*l**2*Derivative(q(t), (t, 2)) - g*l*m*sin(q(t)) = 0
```

## 配方 2：运动方程数值解（scipy）

验证解析解与数值解的偏差。示例：非线性单摆 $\ddot\theta + (g/l)\sin\theta = 0$。

```python
import numpy as np
from scipy.integrate import solve_ivp

g, l = 9.8, 1.0
def f(t, y):
    th, w = y
    return [w, -(g/l)*np.sin(th)]

sol = solve_ivp(f, [0, 10], [0.1, 0.0], t_eval=np.linspace(0, 10, 200), rtol=1e-9)
w = np.sqrt(g/l)
err = np.max(np.abs(sol.y[0] - 0.1*np.cos(w*sol.t)))
print("max deviation:", err)   # 量级 ~1e-3（随振幅与时长变化），远小于 0.1
```

## 配方 3：矩阵/特征值复核（联动 Math.Skill 的矩阵能力）

小振动问题中 $\det(K - \omega^2 M)=0$ 的符号计算：

```python
import sympy as sp

w2 = sp.symbols('omega^2')
K = sp.Matrix([[2, -1], [-1, 2]])   # 刚度矩阵（示例：耦合振子）
M = sp.Matrix([[1, 0], [0, 1]])     # 质量矩阵
eigs = sp.solve(sp.Eq(sp.det(K - w2*M), 0), w2)
print(eigs)                          # 期望 [1, 3] -> omega = 1, sqrt(3)
```

## 配方 4：常数与单位（scipy.constants）

量纲/数值检查用标准常量，避免手抄错数值。

```python
from scipy import constants as c
print(c.hbar, c.e, c.m_e, c.c, c.k)   # 约化普朗克常数、元电荷、电子质量、光速、玻尔兹曼常数
```

## 配方 5：RC 电路复核

验证 RC 放电解析解与一阶 ODE 一致：

```python
import sympy as sp

t = sp.symbols('t')
V0, R, C = sp.symbols('V0 R C', positive=True)
V = sp.Function('V')(t)

ode = sp.Eq(V.diff(t) + V/(R*C), 0)
sol = sp.dsolve(ode, V, ics={V.subs(t, 0): V0})
print(sol)   # 期望: Eq(V(t), V0*exp(-t/(C*R)))
```

## 配方 6：回旋运动参数复核

验证回旋半径、角频率与周期：

```python
import sympy as sp

m, v, q, B = sp.symbols('m v q B', positive=True)
r = m*v/(q*B)
omega = q*B/m
T = 2*sp.pi/omega
print(r, omega, T)   # 期望: m*v/(B*q), B*q/m, 2*pi*m/(B*q)
```

## 配方 7：无限深势阱能级复核

验证一维无限深势阱能级公式：

```python
import sympy as sp

n, m, L, hbar = sp.symbols('n m L hbar', positive=True)
E = n**2 * sp.pi**2 * hbar**2 / (2*m*L**2)
print(sp.simplify(E))   # 期望: n**2*pi**2*hbar**2/(2*L**2*m)
```

## 配方 8：对易子复核

对任意可微试探函数验证 $[\hat x,\hat p]=i\hbar$：

```python
import sympy as sp

x = sp.symbols('x')
hbar = sp.symbols('hbar', positive=True)
f = sp.Function('f')(x)
comm = x*(-hbar*sp.I*sp.diff(f, x)) - (-hbar*sp.I)*sp.diff(x*f, x)
print(sp.simplify(comm))   # 期望: I*hbar*f(x)
```

## 何时不适用

- 环境无 Python/SymPy → 直接跳过，主流程不受影响。
- 纯概念/证明类问题（无计算量）→ 不需要。
- 用户明确要求只用手算 → 不使用。
