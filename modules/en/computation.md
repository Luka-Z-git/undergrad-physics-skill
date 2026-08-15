# Symbolic Computation Recipes (Optional Computation)

This module provides **optional** cross-check recipes per the Level 1–4 tool gate: medium problems may run one symbolic cross-check, and complex problems auto-upgrade to one when available; L1 simple problems forbid tools, and tools are also disabled when the user asks for hand calculation only.

**Default discipline**: tool calls must actually run and be reported from real output; never claim "verified with SymPy" unless it ran. If Python/SymPy is unavailable, skip and keep the main flow unaffected.

**Rule**: output from these recipes is cross-check evidence only; it cannot replace the main flow's PASS/FAIL records. If it disagrees with a hand calculation, follow the Backtrack-and-Fix Protocol. Run at most one symbolic cross-check per problem unless the user asks for more.

## Recipe Overview

| # | Use case | Tool | Corresponding domain |
|---|---|---|---|
| 1 | Symbolic ODE solving (E-L / circuits) | SymPy dsolve/diff | Mechanics, Electromagnetism |
| 2 | Numerical ODE verification | SciPy solve_ivp | Mechanics (nonlinear) |
| 3 | Matrices / eigenvalues | SymPy Matrix | Small oscillations |
| 4 | Physical constants | scipy.constants | All domains |
| 5 | Algebraic simplification / dimensions | SymPy simplify | All domains |
| 6 | Commutator expansion | Sympy + test function | Quantum mechanics |

---

## Recipe 1: Symbolic ODE Solving (general)

Use this recipe for any ODE that can be checked with `dsolve` or by manual differentiation, including Lagrangian E–L equations and circuit transients.

**Example A — Pendulum E-L equation**:

```python
import sympy as sp

t = sp.symbols('t')
q = sp.Function('q')(t)
m, g, l = sp.symbols('m g l', positive=True)

L = sp.Rational(1,2)*m*l**2*q.diff(t)**2 + m*g*l*sp.cos(q)   # pendulum L
EL = sp.simplify(sp.diff(sp.diff(L, q.diff(t), t) - sp.diff(L, q)))
print(sp.Eq(EL, 0))
# → -m*l**2*Derivative(q(t),(t,2)) - g*l*m*sin(q(t)) = 0  OK
```

**Example B — RC discharge**:

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

## Recipe 2: Numerical ODE Deviation Detection (scipy)

Verifies the numerical accuracy of an analytic solution for a nonlinear system. Example: pendulum $\ddot\theta+(g/l)\sin\theta=0$:

```python
import numpy as np
from scipy.integrate import solve_ivp

g, l = 9.8, 1.0
sol = solve_ivp(lambda t,y: [y[1], -(g/l)*np.sin(y[0])],
                [0,10], [0.1, 0.0], t_eval=np.linspace(0,10,200), rtol=1e-9)
err = np.max(np.abs(sol.y[0] - 0.1*np.cos((g/l)**0.5 * sol.t)))
print("max deviation:", err)   # ~1e-3 order, far below the amplitude
```

---

## Recipe 3: Matrices / Eigenvalues (small oscillations)

Symbolic computation of $$\det(K-\omega^2 M)=0$$:

```python
import sympy as sp

w2 = sp.symbols('w2', positive=True)  # represents ω²
K = sp.Matrix([[2,-1],[-1,2]])        # stiffness matrix
M = sp.Matrix([[1,0],[0,1]])          # mass matrix
print(sp.solve(sp.Eq(sp.det(K-w2*M),0), w2))  # [1, 3]
```

---

## Recipes 4–6: Constants / Simplification / Commutators

```python
# Recipe 4: physical constants (avoid hand-copying errors)
from scipy import constants as c
print(c.hbar, c.e, c.m_e, c.c)  # ħ, e, mₑ, c

# Recipe 5: algebraic simplification and dimensional check
import sympy as sp
n,m,L,hbar = sp.symbols('n m L hbar', positive=True)
E = n**2 * sp.pi**2 * hbar**2 / (2*m*L**2)
print(sp.simplify(E))  # confirms the infinite square well energy formula

# Recipe 6: commutator expansion
x = sp.symbols('x')
hbar = sp.symbols('hbar', positive=True)
f = sp.Function('f')(x)
comm = x*(-hbar*sp.I*sp.diff(f,x)) - (-hbar*sp.I)*sp.diff(x*f, x)
print(sp.simplify(comm))  # I*ħ·f(x)  OK
```

---

## When Not Applicable

- L1 simple problems → tools are forbidden
- No Python/SymPy in the environment → skip; the main flow is unaffected
- Pure concept / proof problems → not needed
- User requests hand calculation only → do not use
