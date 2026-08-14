# Error Prevention

This module defines the error-prevention rules that must be observed during derivation, the common-pitfall tables for each domain, and the pre-submission checklist. The rules remain in effect continuously during the derivation step (step 3 of the core workflow); the checklist is executed once in full before answering (step 6 of the core workflow).

## 0. General Discipline

1. **No fabrication**: do not invent theorems, formulas, or "obviously true" steps. Mark uncertain intermediate steps explicitly; do not mask them with vague wording.
2. **Carry units throughout**: every physical quantity carries units; intermediate results must be dimensionally consistent with the context; declare the unit system (SI/CGS) explicitly in the Parse step and never mix systems during derivation.
3. **Write out all steps**: write every algebraic transformation explicitly; no mental-math skipping; run a sanity check with simple values or dimensions every 3–5 steps.
4. **Preconditions before theorems**: before invoking any law/theorem, verify that its applicability conditions hold (inertial frame, no dissipation, potential field, stationary state, small angle, etc.) and state them in the text.

## 1. Common Algebra and Calculus Errors in Physics

| Pitfall | Wrong | Correct |
|---|---|---|
| Dropping the $1/2$ | Kinetic energy written as $mv^2$ | $T=\frac{1}{2}mv^2$ |
| Square-root sign | $\sqrt{x^2}=x$ | $\sqrt{x^2}=\|x\|$ |
| Chain rule | $\frac{d}{dt}V(q(t))=\frac{dV}{dq}$ | $\frac{d}{dt}V(q)=\frac{dV}{dq}\dot q$ |
| Integration constants / initial values | Solving an ODE without writing integration constants | Determine constants from initial conditions; missing initial values leave a non-unique family of solutions |
| Mixing dimensions | Mixing SI and CGS | Declare the unit system in the Parse step and keep it consistent throughout |

## 2. Mechanics

### 2.1 Modeling Stage

- **Coordinate system and inertial frames**: Newton's second law holds only in inertial frames; in non-inertial frames, inertial forces (transport, Coriolis, centrifugal) must be added explicitly and the reference frame declared.
- **Constraint classification**: before using Lagrangian mechanics, confirm the constraints are holonomic and ideal; non-holonomic constraints or frictional systems require generalized forces or Lagrange multipliers instead, with the reason stated.
- **Generalized coordinates**: degrees of freedom = number of independent coordinates; choosing too few or too many coordinates leads to the wrong number of equations.
- **Zero of potential energy**: adding a constant to the potential does not affect the equations of motion; once chosen, keep it consistent throughout.

### 2.2 Lagrangian Mechanics

- **Sign of $L = T - V$**: writing $T+V$ is the most common error; check that $\partial L/\partial \dot q$ applied to the kinetic term gives $m\dot q$, not $-m\dot q$.
- **E-L equation structure**: $\frac{d}{dt}\frac{\partial L}{\partial \dot q_i} - \frac{\partial L}{\partial q_i} = 0$; the sign of $\partial L/\partial q_i$ (from the minus sign in $V$) is a high-frequency error point.
- **Cyclic coordinates and conservation**: $L$ not containing $q_i$ → generalized momentum $p_i = \partial L/\partial \dot q_i$ is conserved; $L$ not explicitly time-dependent → the generalized energy (Jacobi integral) $h = \sum p_i\dot q_i - L$ is conserved, and $h$ equals the mechanical energy $T+V$ only when the constraints are scleronomic. The criterion is the explicit dependence of $L$, not "what it looks like".
- **Energy and the Hamiltonian**: $H = \sum p_i \dot q_i - L$; only when the constraints are scleronomic (not explicitly time-dependent) does $H = E$, and only then does $E$ equal $T+V$.

### 2.3 Small Oscillations and Normal Modes

- **Equilibrium points**: first solve $\partial V/\partial q_i = 0$ to find equilibrium configurations; $\omega^2 < 0$ indicates an unstable equilibrium (exponential growth), not oscillation.
- **Small-angle / small-displacement approximation**: $\sin\theta \approx \theta$ holds only for $\theta \ll 1$ (radians); after approximating, state the range of validity — large amplitudes need higher-order corrections.
- **Normal coordinates**: frequencies are given by $\det(K - \omega^2 M) = 0$; $K$ is the stiffness matrix and $M$ the mass matrix — writing matrix elements in the wrong order is a common error.

### 2.4 Pitfall Table

| Pitfall | Wrong | Correct |
|---|---|---|
| Misusing inertial frames | Applying Newton's second law in an accelerating train car without adding inertial forces | Declare the non-inertial frame and add inertial-force terms |
| E-L signs | $L = T + V$ or wrong sign in $\frac{\partial L}{\partial q}$ | $L=T-V$; check signs term by term |
| Misusing energy conservation | Using $E=\text{const}$ despite dissipation (friction/damping) | First verify no dissipation, or account for it explicitly |
| Small-angle overreach | Using $\sin\theta\approx\theta$ for large amplitudes | State $\theta\ll1$; otherwise use elliptic integrals |
| $\omega$ confusion | Treating angular frequency $\omega$ as angular velocity $\dot\theta$ | $\omega=\sqrt{k/m}$ is a constant; $\dot\theta$ is a variable |

## 3. Electromagnetism and Quantum Mechanics (Cross-Domain Checks)

This table lists only cross-domain common checks; for electromagnetism and quantum specifics see `electromagnetism.md` and `quantum_basics.md` respectively.

- **Electromagnetism**: rules for vector operators (gradient/divergence/curl) acting on scalars/vectors; applicability boundaries of integral vs. differential forms; continuity of boundary conditions at interfaces.
- **Quantum mechanics**: operator ordering (non-commuting operators cannot be swapped); wavefunction normalization $\int|\psi|^2\,dx = 1$; eigenvalues of Hermitian operators are real.

## 4. Pre-Submission Checklist (execute in full before answering)

- [ ] Unit system declared and consistent throughout; final result's dimensions match the target physical quantity (F)
- [ ] Applicability conditions of all invoked theorems/laws stated and satisfied
- [ ] Template A mandatory checks executed with item-by-item PASS/FAIL: ①F dimensions ②L limit/special case ③B back-substitution ④C conserved quantities (when applicable); FAIL 0 items
- [ ] Template A six section titles complete and in correct order: 题意与图景 (Problem Restatement), 建模 (Modeling), 推导 (Derivation), 验算 (Verification), 答案 (Answer), 易错点 (Common Pitfalls); each section independent, no merging
- [ ] Each 验算 line starts with ①②③④ (plus optional ⑤⑥, and domain-mandatory ⑦J); the 答案 section contains explicit `**...**` bolding (`\boxed{}` is not a substitute)
- [ ] Final answer includes units and parameter validity ranges (e.g., $\theta\ll1$, $v\ll c$)
- [ ] Output contains no emoji, checkmark/cross, or other Unicode symbols; formulas use `$$ ... $$` blocks, paste-ready for Overleaf compilation
- [ ] No wording such as "believe", "obviously", or "should pass verification" used in place of actual verification
