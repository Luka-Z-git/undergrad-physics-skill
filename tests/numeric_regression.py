#!/usr/bin/env python3
"""Deterministic numeric regression checks for worked examples (stdlib only).

Each check reproduces a concrete numeric claim from examples/ or tests/.
Exit code 0 means all checks PASS; 1 means at least one FAIL.
"""
import math
import sys

FAILURES = []


def check(name, got, expected, tol=1e-3):
    ok = abs(got - expected) <= tol * max(1.0, abs(expected))
    status = "PASS" if ok else "FAIL"
    print(f"{status} {name}: got={got:.6g}, expected={expected:.6g}")
    if not ok:
        FAILURES.append(name)


# RC discharge: R=1k, C=100uF, V0=5V, t=0.1s
R, C, V0, t = 1e3, 100e-6, 5.0, 0.1
tau = R * C
check("RC tau", tau, 0.1)
check("RC V(t)", V0 * math.exp(-t / tau), 1.839397205857)
check("RC I(t) mA", V0 / R * math.exp(-t / tau) * 1e3, 1.839397205857)

# Cyclotron: proton, B=0.5T, v=3e6 m/s
mp, qp, Bp, vp = 1.67e-27, 1.6e-19, 0.5, 3e6
check("cyclotron r", mp * vp / (qp * Bp), 0.062625)
check("cyclotron T", 2 * math.pi * mp / (qp * Bp), 1.3116e-7)

# Infinite square well: electron, L=1nm
hbar = 1.054571817e-34
me = 9.1093837015e-31
Lw = 1e-9
E1 = math.pi**2 * hbar**2 / (2 * me * Lw**2)
check("well E1 eV", E1 / 1.602176634e-19, 0.376014)
n = 100000
norm = sum((2.0 / Lw) * math.sin(math.pi * (i + 0.5) / n) ** 2 for i in range(n)) * (Lw / n)
check("well normalization", norm, 1.0)

# Faraday sliding rod
Bf, lf, vf, Rf = 0.5, 0.2, 2.0, 2.0
Ef = Bf * lf * vf
If = Ef / Rf
Ff = If * lf * Bf
check("faraday emf", Ef, 0.2)
check("faraday I", If, 0.1)
check("faraday F", Ff, 0.01)
check("faraday P = I^2R", Ff * vf, If * If * Rf)

# Dielectric boundary
e1, e2, th1 = 1.0, 4.0, math.radians(30.0)
th2 = math.atan(e2 / e1 * math.tan(th1))
E1f = 1.0
E2f = E1f * math.sin(th1) / math.sin(th2)
check("dielectric theta2 deg", math.degrees(th2), 66.5868)
check("dielectric D-normal", e1 * E1f * math.cos(th1), e2 * E2f * math.cos(th2), tol=1e-6)

# Coriolis on rotating disk
w, vr, tm, mm = 0.5, 2.0, 3.0, 1.0
check("coriolis F", 2 * mm * w * vr, 2.0)
check("coriolis y", w * vr * tm * tm, 9.0)

# Incline with friction (backtrack demonstration)
g, s, alpha, mu = 9.8, 1.0, math.radians(30.0), 0.2
vv = math.sqrt(2 * g * s * (math.sin(alpha) - mu * math.cos(alpha)))
a = g * (math.sin(alpha) - mu * math.cos(alpha))
check("backtrack v", vv, 2.5308)
check("backtrack v^2=2as", vv * vv, 2 * a * s, tol=1e-9)

# Zero-frequency mode: det(K - lambda*I) roots at 0, 1, 3
def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
            - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def detKminus(l):
    return det3([[1 - l, -1, 0], [-1, 2 - l, -1], [0, -1, 1 - l]])


for lam in (0.0, 1.0, 3.0):
    check(f"zero-mode det at {lam:g}", detKminus(lam), 0.0, tol=1e-9)

if FAILURES:
    print("FAILED:", ", ".join(FAILURES))
    sys.exit(1)
print("ALL PASS")
