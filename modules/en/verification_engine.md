# Verification Engine

This module defines 8 verification methods (F/D/B/C/L/E/I/J), a problem-type selection table, the Backtrack-and-Fix Protocol, and the verification summary format. Every solution must pass this engine before a final answer is given.

## Method Overview

| Code | Name | What it does | Verdict |
|---|---|---|---|
| F | Dimensional check | Carry units throughout the derivation; the dimension of the final expression must match the target physical quantity | Dimension mismatch → FAIL |
| D | Domain/parameter domain | Physical domain of the solution: parameter ranges, non-zero denominators, reality of square roots, non-negative squared frequencies, real energies | Out of range/undeclared → FAIL |
| B | Back-substitution | Substitute the solution back into the original equation (EOM, E–L equation, $H\psi=E\psi$, circuit equations) to verify identity | Not identical upon substitution → FAIL |
| C | Conserved quantities | Conservation of energy/momentum/angular momentum (when the system is dissipation-free and symmetries hold); verify $T+V=\text{const}$ | Not conserved under numerical evolution → FAIL |
| L | Limits/special cases | Taking parameters to known limits ($\omega\to0$, $\hbar\to0$, $m\to\infty$, $\theta\to0$) should recover known results | Limit inconsistent → FAIL |
| E | Numerical sampling | Plug concrete numbers into intermediate and final expressions, compare both sides of the equation, and check orders of magnitude | Numerically unequal or implausible order of magnitude → FAIL |
| I | Independent method | Re-solve using another framework (Newton vs Lagrange; energy method vs force method; another gauge) | Results disagree → FAIL |
| J | Consistency | Matrix/linear algebra: trace, determinant, back-substitution $A\mathbf{v}=\lambda\mathbf{v}$, reconstruction $PDP^{-1}=A$; quantum: normalization $\int|\psi|^2=1$, $\sum|c_n|^2=1$, commutation relations | Not satisfied → FAIL |

## PASS Criteria

Each PASS must be accompanied by a concrete, auditable check: dimensional substitution, a limit expression, back-substitution identity, conserved-quantity values, or numerical sampling; a purely conclusory PASS (e.g., merely writing "dimension correct") counts as incomplete and is treated as FAIL, triggering the Backtrack-and-Fix Protocol. Fabricating PASS is forbidden.

## Method Details

### F Dimensional check (mandatory, every problem)

1. The analysis step declares the unit system (SI/CGS) and base dimensions $[M],[L],[T],[Q]$.
2. **The final expression and every physically meaningful intermediate result must carry units**; purely mathematical stages (matrix inversion / eigenvalue computation / integration tricks / algebraic simplification) may have dimensionless intermediate steps, but units must be restored and the dimensions checked immediately once physical meaning is re-assigned.
3. The dimension of the final expression = the dimension of the target physical quantity. Example: simple-harmonic angular frequency $\omega=\sqrt{k/m}$, $[\omega]=[k/m]^{1/2}=[\mathrm{N/(kg\cdot m)}]^{1/2}=\mathrm{s^{-1}}$.
4. Common dimensions to remember: $[E]=ML^2T^{-2}$, $[\hbar]=ML^2T^{-1}$, $[\mathrm{electric\ field}]=MLT^{-3}I^{-1}$.

### D Domain/parameter-domain check

- Whether non-negativity/non-zero conditions on quantities in denominators, logarithms, and under square roots have been declared.
- A frequency with $\omega^2>0$ represents oscillation; $\omega^2<0$ indicates exponential growth (near an unstable equilibrium) and must be pointed out.
- The applicable range of the solution (e.g., small-angle approximation $\theta \ll 1$, non-relativistic $v\ll c$, weak field) must be consistent with the assumptions of the derivation.

### B Back-substitution check

Substitute the final solution $x(t)$, $\theta(t)$, $\psi(x)$ back into the original equation, simplify term by term; the two sides must be identical. Example: after obtaining $\theta(t)$, substitute into $\ddot\theta+\omega^2\theta=0$ to verify.

### C Conserved-quantity check

- Lagrangian independent of a coordinate → the corresponding generalized momentum is conserved (Noether); Hamiltonian time-independent → energy is conserved.
- Verification method: take two states at different times, compute $E=T+V$ or $p$; they must be equal.

### L Limit/special-case check

- Take parameters to known limits; the result must reduce to a familiar expression. Example: a bead on a rotating hoop with $\omega\to0$ should reduce to a simple pendulum $\Omega^2=g/R$; quantum results with $\hbar\to0$ should approach the classical limit.

### E Numerical-sampling check

- Take simple numbers (e.g., $m=1,\ k=1,\ g=9.8$), substitute into both sides of the equation separately, and compute each term to several decimal places.
- For trigonometric/exponential functions, substitute special angles or values ($\theta=0,\pi/2$) to verify identities.
- Check that the order of magnitude matches physical common sense: macroscopic speeds far below $c$, forces in typical ranges, non-negative energies, etc.; an implausible order of magnitude is an immediate FAIL.

### I Independent-method check

- Re-solve the same problem with a different method and compare: Newton's second law vs Lagrange; energy conservation vs direct integration; Cartesian vs polar coordinates.
- Applies to hard problems, after a verification failure, or when the user demands high confidence.

### J Consistency check

- Matrix problems: $\mathrm{tr}(A)=\sum\lambda$, $\det(A)=\prod\lambda$, eigenvector back-substitution $A\mathbf{v}=\lambda\mathbf{v}$, reconstruction $PDP^{-1}=A$.
- Quantum problems: wavefunction normalization, probability sum $\sum|c_n|^2=1$, commutation relations such as $[\hat x,\hat p]=i\hbar$.
- Recurrence/matrix-power problems: hand-check $A^2,A^3$ for small $n$ before generalizing.

## Problem Type → Verification Combination Selection Table

The mandatory checks for Template A (standard solution) are fixed as: ① F dimension ② L limit/special case ③ B back-substitution ④ C conserved quantity (when applicable), defined in `output_templates.md`. J consistency, when marked mandatory by a domain module, is presented in the verification section with the number ⑦, at the same level as ①–④ and must not be skipped. The table below supplements optional bonus items and domain emphasis for each problem type.

| Problem type | Optional bonus items | Domain emphasis |
|---|---|---|
| Newtonian mechanics / force analysis | D, E, I | Domain (friction/static-friction conditions); B back-substitution for solutions of equations of motion |
| Lagrangian/Hamiltonian derivations | I, E | Independent method (Newton re-solve) and numerical sampling are strong checks |
| Small oscillations / normal modes | J, E, D | J mandatory in this domain: eigenvalue back-substitution, M-orthogonality |
| Conserved-quantity problems | I, E | Independent-method re-solve to cross-check conserved quantities |
| Electrostatic field / potential | D, E, I | Boundary-condition back-substitution and superposition |
| Circuits RC/RL/RLC | E, D | Time-constant dimensions and $t\to0,\infty$ behavior |
| Maxwell / vector analysis | J, E, D | Expand and compare both sides of identities |
| Stationary Schrödinger / 1D potentials | J, E | J normalization; B back-substitution already mandatory |
| Operators / commutation relations | J, E, D | J mandatory in this domain: verify by direct expansion |
| Matrices / eigenvalues / recurrences | J, E, I | J mandatory in this domain: trace/determinant/back-substitution/reconstruction |

## Backtrack-and-Fix Protocol

When verification FAILs:

1. **Record the failure**: which method, which step, the specific discrepancy.
2. **Backtrack**: locate the last intermediate result that passed; all work after it is considered suspect.
3. **Diagnose**: error category — algebraic error, sign error, dimensional error, theorem applicability conditions not met, lost solution, omitted boundary condition.
4. **Fix**: re-derive from the backtrack point and propagate forward.
5. **Re-verify**: use the original method + at least one additional method (preferably I independent method).
6. **Two failed fixes** → switch to an independent solution route; if that still fails, explicitly declare that no verified answer can be given and report the verified intermediate results. Fabricating PASS is forbidden.

### Cost Stop-Loss Mechanism (new in v0.5)

To prevent uncontrolled token consumption from backtracking on complex problems (double pendulum, coupled oscillators, etc.), the following stop-loss rules are introduced:

#### 6a. Lightweight back-substitution option

When the FAIL occurs only in the last 1–2 steps of the derivation (e.g., a sign error in the final expression, an arithmetic mistake in numerical substitution), and all preceding intermediate results have passed independent verification, a **local fix** is allowed instead of a full backtrack:

- Redo only the FAILing steps and their direct predecessors;
- Keep all previously passed intermediate results; do not mark them as "suspect";
- After the local fix, the full set of four mandatory checks (F/L/B/C) must still be executed on the final answer.

**Trigger conditions, all required simultaneously**: (a) the FAIL occurs in steps beyond 80% of the derivation; (b) all preceding intermediate results have passed at least two independent verifications.

#### 6b. Cost stop-loss point

When the number of operation steps on the re-derivation path exceeds **150%** of the first draft, stop same-path fixes and switch directly to **independent method I** (Newton vs Lagrange, energy method vs force method, matrix method vs algebraic method). Do not attempt a third same-path fix.

#### 6c. Complex-problem tagging

The following problem types are automatically tagged as "complex"; at step 6 of the Backtrack-and-Fix Protocol they **skip the second same-path fix** and go directly to the independent-method switch:
- Double pendulum and coupled systems with more degrees of freedom
- Lagrangian problems involving full constraint elimination + generalized-coordinate selection
- Quantum problems requiring separation of variables + special functions (hydrogen-atom radial equation)
- Electromagnetism problems requiring vector integrals + symmetry analysis (non-highly-symmetric)

**The complex-problem tag should be declared at the end of the analysis phase, together with the difficulty grading.**

#### Stop-loss record format

When lightweight back-substitution or the cost stop-loss is triggered, note it in the verification summary:

```
已通过 ①②③④，FAIL 0 项（⑥ 成本止损：重推路径超 150%，切换至 I 独立方法后 PASS）
```
(English gloss: Passed ①②③④, FAIL 0 items (⑥ cost stop-loss: re-derivation path exceeded 150%, PASS after switching to independent method I))

Or:

```
已通过 ①②③④，FAIL 0 项（⑥a 轻量回代：仅修正第 N 步符号错误）
```
(English gloss: Passed ①②③④, FAIL 0 items (⑥a lightweight back-substitution: only fixed the sign error in step N))

## Verification Summary Format

A one-line summary must be appended at the end of the final answer, in the format:

```
已通过 ①②③④，FAIL 0 项
```
(English gloss: Passed ①②③④, FAIL 0 items)

Details may be included, e.g.: `已通过 ①F 量纲 ②L 极限(ω→0 退化为单摆) ③B 回代 ④C 守恒，FAIL 0 项` (English gloss: Passed ①F dimension ②L limit (reduces to simple pendulum as ω→0) ③B back-substitution ④C conservation, FAIL 0 items). If an item FAILed and was then fixed, write `修复后 PASS` (fixed, then PASS); when ④ is not applicable (no conserved quantity, dissipation, broken symmetry), write `④ N/A（原因）` (④ N/A (reason)).
