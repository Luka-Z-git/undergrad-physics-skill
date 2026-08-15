# Theoretical Mechanics Module

## Scope

**Theoretical Mechanics**: Newtonian mechanics, Lagrangian mechanics, Hamiltonian mechanics, conservation laws and symmetries, small oscillations and normal modes, rigid body basics, non-inertial frames.

Each subdomain follows the same structure: identifying features, modeling steps, a verification set, applicability conditions, and a common-errors table. Verification definitions are in `verification_engine.md`.

## 0. Method Selection Table

Choose the equation framework from the system's features. If several methods apply, use the one that gives the shortest derivation and the clearest verification, and state the choice in one sentence in the Modeling section.

| System Feature | Preferred Method | Reason for Choice | Domain-Specific Verification |
|---|---|---|---|
| Particle/system of particles, few constraints, forces known as functions, constraint reaction forces needed | Newtonian mechanics (§1) | Free-body diagrams give equations directly; reaction forces solved from constraint equations | D (friction/static friction conditions) |
| Many holonomic constraints, few degrees of freedom | Lagrangian mechanics (§2) | Generalized coordinates eliminate constraints; fewest equations | C strong conservation check |
| Need phase space, canonical equations, or conservation/Poisson bracket analysis | Hamiltonian mechanics (§3) | Second-order equations recast as first-order phase flow | J consistency |
| Small-amplitude motion near equilibrium, multi-DOF coupling | Small oscillations (§5) | Linearization yields normal modes and frequencies | J (M-orthogonality, eigenvalue substitution) |
| Rigid body planar motion, rolling without slipping, collisions | Rigid body basics (§6) | Center-of-mass theorem + rotation equations | B constraint back-substitution |
| Observer in an accelerating or rotating reference frame | Non-inertial frames (§7) | Explicitly add inertial force terms | I re-solve in the inertial frame |

## 1. Newtonian Mechanics

### Identifying Features

- Particle or system of particles, few constraints or constraints explicitly writable; forces (gravity, elastic force, tension, friction) are known functions.
- Quantities sought are accelerations, trajectories, or constraint reaction forces; handles both single- and multi-degree-of-freedom systems.
- The system moves in an inertial frame; see §7 for non-inertial-frame problems.

### Modeling Steps

1. Choose an inertial frame and coordinate system: Cartesian, polar, or natural coordinates (tangential/normal), and mark positive directions.
2. Isolate each body and draw a free-body diagram: draw only the real forces acting on that body; isolate bodies of a multi-body system one by one.
3. Resolve along coordinate directions and write component equations $m\ddot x = F_x$, $m\ddot y = F_y$.
4. Write the constraint equations (fixed rope length, contact, rolling without slipping) and solve them together with the equations of motion; reaction forces are obtained from the constraint equations.
5. Integrate to find $x(t)$, fixing the integration constants with initial conditions; check the domain and sign of the solution.

### Verification Set

Recommended verification set: F + B + D or L; add C only when a conservation law applies, and add I or E when the problem is high-risk.

### Applicability Conditions to Check

- Newton's second law holds only in inertial frames; for introductory problems, state explicitly when the Earth is being approximated as an inertial frame.
- Ropes, massless rods, and frictionless surfaces are idealized models; with friction present, a kinetic/static friction model must be introduced and the friction coefficient declared.
- Forces must be known functions; time-dependent, position-dependent, and velocity-dependent forces (damping) are handled separately.

### Common Errors

| Error | Correct |
|---|---|
| Writing $m\mathbf a=\mathbf F$ directly in a non-inertial frame | Add inertial forces $-m\mathbf a_0$, centrifugal force, and Coriolis force (see §7) |
| Drawing action and reaction forces on the same body | The free-body diagram shows only forces acting on that body |
| Writing kinetic energy as $mv^2$ | $T=\frac12 mv^2$; the 1/2 factor cannot be omitted |
| Writing polar acceleration as only $r\ddot\theta$ | $a_\theta = r\ddot\theta + 2\dot r\dot\theta$ |
| Assuming rope tension is equal everywhere | Holds only for massless ropes or frictionless pulleys |

## 2. Lagrangian Mechanics

### Identifying Features

- Many holonomic constraints and few degrees of freedom, so eliminating constraints with generalized coordinates is most efficient.
- Forces are conservative or can be absorbed into generalized forces; quantities sought are equations of motion, periods, and conserved quantities.
- Complex constrained systems: double pendulums, pulley systems, wheels rolling without slipping, beads on fixed curves.

### Modeling Steps

1. Determine the degrees of freedom $s = 3N - k$ (for a 3D system of particles, with $k$ the number of holonomic constraints; $2N - k$ for planar systems), and choose generalized coordinates $q_i$; the coordinate map must be one-to-one and invertible.
2. Write the kinetic energy $T$ and potential energy $V$ in terms of generalized velocities, and set $L = T - V$.
3. Classify the constraints: holonomic constraints are eliminated directly; non-holonomic constraints require Lagrange multipliers or d'Alembert's method.
4. Write non-conservative forces as generalized forces $Q_i = \sum_j \mathbf F_j\cdot\partial\mathbf r_j/\partial q_i$, and substitute into the Euler-Lagrange equation:

$$
\frac{d}{dt}\frac{\partial L}{\partial\dot q_i} - \frac{\partial L}{\partial q_i} = Q_i
$$

5. Solve the equations of motion, fixing constants with initial conditions; cross-check using conserved quantities.

### Verification Set

Recommended verification set: F + B + I or C; add E when numerical scale matters.

### Applicability Conditions to Check

- The Euler-Lagrange equation requires holonomic constraints; it cannot be applied directly to non-holonomic constraints.
- With friction/damping, $L=T-V$ does not fully describe the dynamics; generalized forces or a Rayleigh dissipation function must be added.
- Adding a total time derivative $dF(q,t)/dt$ to $L$ (where $F$ depends only on $q,t$) does not change the equations of motion (equivalent Lagrangians); if $F$ contains $\dot q$ the boundary term cannot be ignored; with non-holonomic constraints, the multiplier equations govern, and one cannot judge solely from the form of $L$.

### Common Errors

| Error | Correct |
|---|---|
| Missing the 1/2 or the mass factor in kinetic energy | Check each term against forms like $T=\frac12 m\dot x^2$ |
| Confusing $\partial L/\partial q$ with $\partial L/\partial\dot q$ | The first E-L term differentiates w.r.t. velocity, the second w.r.t. coordinate |
| Applying the E-L equation directly to non-holonomic constraints | Use Lagrange multipliers or rewrite as holonomic constraints |
| Friction with nowhere to go | Put it in generalized forces $Q_i$ or a Rayleigh dissipation function |
| Claiming $E$ is conserved just because $L$ has no explicit $t$ | Generalized energy equals mechanical energy only under time-independent constraints |

## 3. Hamiltonian Mechanics

### Identifying Features

- Need phase space $(q,p)$ description, canonical equations, Poisson brackets, or canonical transformations.
- Determining conserved quantities and integrals of motion; performing the Legendre transform from $L$.
- Classical correspondence with quantum mechanics, perturbation, or phase-flow analysis.

### Modeling Steps

1. Compute generalized momenta $p_i = \partial L/\partial\dot q_i$; verify that the Hessian matrix $\partial^2 L/\partial\dot q_i\partial\dot q_j$ is non-degenerate (invertible).
2. Solve for $\dot q_i(q,p,t)$ and perform the Legendre transform $H = \sum_i p_i\dot q_i - L$.
3. Write the canonical equations $\dot q_i = \partial H/\partial p_i$, $\dot p_i = -\partial H/\partial q_i$.
4. Criteria: $\partial H/\partial t = 0 \Rightarrow H$ is conserved; $H = E$ additionally requires time-independent constraints and $T$ quadratic homogeneous in $\dot q$.
5. Solve the equations or reduce the order using cyclic coordinates; verify with conserved quantities.

### Verification Set

Recommended verification set: F + B + J; J is mandatory for this domain. Add I or E when useful.

### Applicability Conditions to Check

- The Legendre transform must be invertible (non-singular Lagrangian); singular systems (gauge theories) are beyond undergraduate scope and must be declared.
- Cases where $H\neq T+V$: $H$ explicitly time-dependent, velocity-dependent potentials, time-dependent constraints.
- The canonical equations give conservation of $H$; energy conservation requires a separate criterion.

### Common Errors

| Error | Correct |
|---|---|
| Writing $H=T+V$ unconditionally | Perform the Legendre transform first, then check the expression for $H$ |
| Believing conservation of $H$ means energy conservation | $\partial H/\partial t=0$ only guarantees conservation of $H$; when $H\neq E$ the two differ |
| Sign error in canonical equations | $\dot p_i = -\partial H/\partial q_i$ |
| Residual $\dot q$ in $H$ | Eliminate $\dot q$ first using $p_i = \partial L/\partial\dot q_i$ |
| Cyclic coordinate present but momentum conservation not identified | $\partial H/\partial q_j = 0 \Rightarrow p_j$ is conserved |

## 4. Conservation Laws & Noether's Theorem

### Identifying Features

- Questions asking "which quantities are conserved", finding integrals of motion, or using conserved quantities to reduce the order of a solution.
- The system has translational, rotational, or time-translation symmetry.
- Using conserved quantities to cross-check numerical solutions (verification engine method C).

### Modeling Steps

1. Write down $L$ (or $H$) and explicitly list its dependent variables.
2. Cyclic coordinate criterion: $\partial L/\partial q_j = 0 \Rightarrow p_j$ is conserved.
3. $\partial L/\partial t = 0 \Rightarrow h = \sum_i p_i\dot q_i - L$ is conserved (the Noether charge of time-translation symmetry).
4. Spatial translation symmetry $\Rightarrow$ total momentum conservation; rotational symmetry $\Rightarrow$ angular momentum conservation (about a fixed point or the center of mass).
5. Use conserved quantities to reduce the order of the solution, and numerically sample to re-verify conservation.

### Verification Set

Recommended verification set: F + B + C; add I or E when an independent check is useful.

### Applicability Conditions to Check

- The symmetry must hold over the entire domain of motion; inhomogeneous external fields or boundaries break the symmetry.
- Mechanical energy is not conserved in dissipative systems; Noether's theorem requires the action to possess the corresponding continuous symmetry.
- Angular momentum conservation must be defined about a fixed point or the center of mass.

### Common Errors

| Error | Correct |
|---|---|
| Claiming a cyclic coordinate stays constant | A cyclic coordinate gives momentum conservation; the coordinate itself may vary with time |
| Using mechanical energy conservation despite friction | First compute the dissipated work $\Delta E = \int \mathbf F_f\cdot d\mathbf r$ |
| Choosing the angular momentum reference point arbitrarily | Fixed point or center of mass; changing the reference point requires conversion |
| Mistaking $p=\mathrm{const}$ for $p=0$ | A conserved quantity is an integration constant and may be nonzero |
| Assuming conservation although the symmetry is broken by an external field | First check whether external forces depend on the corresponding coordinate |

## 5. Small Oscillations & Normal Modes

### Identifying Features

- Small-amplitude motion near equilibrium; quantities sought are frequencies, normal modes, and normal coordinates.
- Multi-DOF coupled systems: coupled pendulums, double pendulums, molecular vibrations.

### Modeling Steps

1. Find the equilibrium configuration: $\partial V/\partial q_i\big|_0 = 0$ (conservative systems).
2. Expand about equilibrium to second order: $V = \frac12\sum_{ij} k_{ij}\xi_i\xi_j$, $T = \frac12\sum_{ij} m_{ij}\dot\xi_i\dot\xi_j$, with $K,M$ symmetric matrices.
3. Write the matrix equation of motion $M\ddot{\boldsymbol\xi} + K\boldsymbol\xi = 0$.
4. Set $\boldsymbol\xi = \mathbf A e^{i\omega t}$ to obtain the characteristic equation $\det(K - \omega^2 M) = 0$.
5. Solve for $\omega_\alpha^2$ and the eigenvectors, and construct normal coordinates $\eta_\alpha$ ($M$-orthonormal); $\omega^2>0$ indicates stable equilibrium.

### Verification Set

Recommended verification set: F + B + J; J is mandatory for this domain. Add E or D when useful.

### Applicability Conditions to Check

- Linearization requires small amplitudes; oscillation occurs only for $\omega^2>0$, while $\omega^2<0$ indicates unstable equilibrium and must be pointed out.
- Zero-frequency modes correspond to translation/rotation directions with no restoring force and must be identified separately.
- With damping or driving forces the frequencies change; the corresponding terms must be added to the matrix equation.

### Common Errors

| Error | Correct |
|---|---|
| Missing 1/2 in potential energy: writing $V=kx^2$ | $V=\frac12 kx^2=\frac12 m\omega^2 x^2$ |
| Using $\det(K-\omega^2 I)$ | Use $\det(K-\omega^2 M)=0$; the mass matrix cannot be omitted |
| Wrong equilibrium point (constraints not eliminated) | Eliminate constraints or use multipliers first, then solve $\partial V/\partial q_i=0$ |
| Taking frequency $f$ as angular frequency $\omega$ | $\omega = 2\pi f$; note the unit $\mathrm{rad/s}$ |
| Not checking $M$-orthogonality of eigenvectors | Verify $\mathbf A_\alpha^T M \mathbf A_\beta \propto \delta_{\alpha\beta}$ |

## 6. Rigid Body Basics

### Identifying Features

- Rigid body planar motion (translation + rotation), rolling without slipping, collision problems.
- Quantities sought are angular acceleration, center-of-mass acceleration, and constraint reaction forces.

### Modeling Steps

1. Choose a reference point (center of mass C or fixed point O); kinematics: $\mathbf v_P = \mathbf v_C + \boldsymbol\omega\times\mathbf r_{PC}$.
2. Compute moments of inertia: about the center-of-mass axis $I_C$; parallel axis theorem $I = I_C + md^2$.
3. Write $\sum\mathbf F = m\mathbf a_C$ and $\sum\boldsymbol\tau_C = I_C\dot{\boldsymbol\omega}$ about the center of mass.
4. Rolling-without-slipping condition $\dot x = R\dot\theta$ (no slipping); the direction of static friction is determined by the tendency of relative motion.
5. Energy method: $T = \frac12 mv_C^2 + \frac12 I_C\omega^2$; ideal constraints do no work.

### Verification Set

Recommended verification set: F + B + I or L; add E when numerical scale matters.

### Applicability Conditions to Check

- The rotation equation holds only about a fixed point or the center of mass; for a general point, an additional torque term involving the center-of-mass acceleration must be added.
- Rolling without slipping requires static friction below its limit: $f_s \le \mu_s N$; otherwise it transitions to sliding.
- Angular momentum is conserved only when the external torque is zero.

### Common Errors

| Error | Correct |
|---|---|
| Writing $\tau = I\alpha$ directly about a point that is neither the center of mass nor fixed | Write it only about a fixed point/the center of mass; for a general point add the extra torque term |
| Assuming $f = \mu_s N$ for rolling without slipping | $f$ is determined by the constraint; one must check $f \le \mu_s N$ |
| Missing $md^2$ in the parallel axis theorem | $I = I_C + md^2$ |
| Mistakenly using work done by kinetic friction in rolling without slipping | Rolling without slipping involves static friction, which does no work in the ideal case |
| Kinetic energy written with only the rotational term | $T = \frac12 mv_C^2 + \frac12 I_C\omega^2$ requires both terms |

## 7. Non-Inertial Frames

### Identifying Features

- The observer is in an accelerating or rotating reference frame: elevators, turntables, Earth's rotation, Foucault pendulum.
- Involves inertial forces, centrifugal force, Coriolis force, Euler force.

### Modeling Steps

1. Declare the inertial frame S and the moving frame S': relative translational acceleration $\mathbf a_0$ and angular velocity $\boldsymbol\Omega$.
2. Write the equation of motion in S':

$$
m\mathbf a' = \mathbf F - m\mathbf a_0 - m\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r') - 2m\boldsymbol\Omega\times\mathbf v' - m\dot{\boldsymbol\Omega}\times\mathbf r'
$$

3. Identify each term and label it as an inertial force (fictitious force); the Euler term vanishes when $\dot{\boldsymbol\Omega}=0$ (constant angular velocity), and is nonzero for rotation with varying speed about a fixed axis.
4. After solving, perform a limit check: $\mathbf a_0\to0$, $\boldsymbol\Omega\to0$ should recover the inertial-frame equation.
5. Recheck dimensions and directions (Coriolis force via the right-hand rule for cross products).

### Verification Set

Recommended verification set: F + B + I or L; add E when numerical scale matters.

### Applicability Conditions to Check

- Inertial forces appear only in non-inertial frames; explicitly declare the reference frame used when solving.
- The Coriolis force is velocity-dependent and cannot be absorbed into a potential; the centrifugal force can be absorbed into the potential $-\frac12 m\Omega^2 r'^2$ for rotation about a fixed axis ($r'$ is the perpendicular distance to the rotation axis).
- Earth's rotation $\Omega \approx 7.27\times10^{-5}\,\mathrm{rad/s}$; it is often negligible for low-speed, small-scale problems, and neglecting it must be declared.

### Common Errors

| Error | Correct |
|---|---|
| Missing the translational inertial force $-m\mathbf a_0$ | Must be added in an accelerating reference frame |
| Wrong direction of the Coriolis force | $-2m\boldsymbol\Omega\times\mathbf v'$ by the right-hand rule for cross products |
| Treating inertial forces as real forces | Label them as fictitious forces; they appear only in non-inertial frame equations |
| Introducing inertial forces in an inertial frame | Inertial forces are zero in an inertial frame |
| Absorbing the Coriolis force into a potential | Only the centrifugal force can be absorbed into a potential (fixed-axis case) |

## 8. Formulas & Traps

### Formula Quick Reference

Polar coordinates (plane):

$$
\mathbf v = \dot r\,\hat{\mathbf e}_r + r\dot\theta\,\hat{\mathbf e}_\theta, \qquad
\mathbf a = (\ddot r - r\dot\theta^2)\,\hat{\mathbf e}_r + (r\ddot\theta + 2\dot r\dot\theta)\,\hat{\mathbf e}_\theta
$$

Euler-Lagrange equation and generalized forces:

$$
\frac{d}{dt}\frac{\partial L}{\partial\dot q_i} - \frac{\partial L}{\partial q_i} = Q_i, \qquad
Q_i = \sum_j \mathbf F_j\cdot\frac{\partial\mathbf r_j}{\partial q_i}
$$

Hamiltonian and canonical equations:

$$
H = \sum_i p_i\dot q_i - L, \qquad
\dot q_i = \frac{\partial H}{\partial p_i},\quad \dot p_i = -\frac{\partial H}{\partial q_i}
$$

Small-oscillation characteristic equation:

$$
\det(K - \omega^2 M) = 0
$$

Non-inertial frame equation (S' moves relative to S with $\mathbf a_0$, $\boldsymbol\Omega$):

$$
m\mathbf a' = \mathbf F - m\mathbf a_0 - m\boldsymbol\Omega\times(\boldsymbol\Omega\times\mathbf r') - 2m\boldsymbol\Omega\times\mathbf v' - m\dot{\boldsymbol\Omega}\times\mathbf r'
$$

Moments of inertia (about center-of-mass axes): thin rod $I=mL^2/12$; disk $I=mR^2/2$; solid sphere $I=2mR^2/5$; spherical shell $I=2mR^2/3$; parallel axis $I = I_C + md^2$. Euler's equations for rotation about a fixed point (principal axes): $I_1\dot\omega_1 - (I_2-I_3)\omega_2\omega_3 = \tau_1$ (indices cyclic).

### Cross-Domain Traps

Cross-domain common traps (SI/CGS mixing, 1/2 factors, missing units, etc.) are covered in `error_prevention.md` §0–§2. Traps **specific** to this module are already listed in the Common Errors tables of each section and are not repeated here.
