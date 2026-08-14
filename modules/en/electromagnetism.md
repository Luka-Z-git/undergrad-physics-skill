# Electromagnetism Module

## Scope

**Electromagnetism**: electrostatics, magnetostatics, vector analysis, capacitance/inductance, circuit transients (RC/RL/RLC), foundations of Maxwell's equations. **Media are treated primarily as vacuum**; linear media are covered only at the level of boundary conditions (see the scope statement in SKILL.md).

(Standard subdomain structure as in mechanics.md)

## 0. Method Selection Table

Select the method according to the system's features; when multiple methods apply, choose the one with the shortest derivation and the most direct verification, and state the reason in one sentence in the modeling section.

| System Feature | Preferred Method | Reason for Choice | Domain-Specific Verification |
|---|---|---|---|
| Static charge distribution, find $E$ or $V$, high symmetry (sphere/cylinder/plane) | Gauss's law (§1) | Flux integral reduces to algebra | J (boundary conditions), I (comparison with Coulomb integral) |
| Static charge distribution, find $E$ or $V$, insufficient symmetry | Coulomb's law integration + superposition (§1) | Element-by-element integration works for any distribution | E (numerical integration), L (far-field point-charge limit) |
| Current distribution, find $B$, high symmetry (infinite straight wire/solenoid/toroid) | Ampère's circuital law (§2) | Loop integral reduces to algebra | L (known near-field/on-axis results) |
| Current distribution, find $B$, general geometry | Biot-Savart law (§2) | Integrates over arbitrary current paths | J ($\nabla\cdot\mathbf B=0$, comparison with $\oint\mathbf B\cdot d\mathbf l$) |
| Motion of charged particles in electromagnetic fields | Lorentz force equation (§2) | Equations of motion written directly | B (back-substitution into equations of motion), C (speed/energy) |
| Lumped-circuit transients with $R$/$C$/$L$ | KCL/KVL + differential equations (§3) | Lumped-parameter model | B (solution back-substituted into ODE), L ($t\to0,\infty$), C (energy) |
| Time-varying magnetic flux, moving conductors | Faraday's law + Lenz's law (§3) | Unified treatment of induced and motional EMF | I (induced vs motional derivations), L ($\dot{\mathbf B}\to0$, $v\to0$) |
| Vector identities, field-theory proofs | Component expansion (§4) | Direct term-by-term comparison | J (expand both sides of the identity), E (spot-check with special fields) |

## 1. Electrostatics

### Identifying Features

- Charges at rest or charge distributions constant in time; the medium can be treated as vacuum, linear media, or conductor boundaries.
- Quantities sought are field strength $\mathbf E$, potential $V$, electric force, capacitance, and energy.
- The system obeys the superposition principle; conductors are in electrostatic equilibrium.

### Modeling Steps

1. Declare the unit system (SI/CGS) and the type of charge distribution (point/line/surface/volume).
2. Perform a symmetry check: spherical, infinite cylindrical, or infinite planar symmetry → Gauss's law; otherwise use Coulomb integration.
3. Gauss method: choose a Gaussian surface, use symmetry to pull $\mathbf E$ out of the integral, and write

$$
\oint_S \mathbf E\cdot d\mathbf A = \frac{Q_{\mathrm{enc}}}{\varepsilon_0}
$$

4. Coulomb method: integrate over charge elements, or superpose point charges:

$$
\mathbf E(\mathbf r) = \frac{1}{4\pi\varepsilon_0}\int \frac{\rho(\mathbf r')(\mathbf r-\mathbf r')}{|\mathbf r-\mathbf r'|^3}\,dV'
$$

5. Potential: $V(\mathbf r) = \frac{1}{4\pi\varepsilon_0}\int \frac{\rho(\mathbf r')}{|\mathbf r-\mathbf r'|}\,dV'$ (when infinity is taken as the zero reference); cross-check via $E = -\nabla V$.
6. Conductor boundaries: in electrostatic equilibrium $\mathbf E=0$ inside a conductor and charge resides on the surface; write the interface boundary conditions.

### Verification Set

Required: F, L, B (C when applicable); recommended additional: D, E, I, J.

### Applicability Conditions to Check

- Electrostatics requires $\partial\mathbf E/\partial t = 0$; in time-varying electromagnetic fields $\mathbf E$ is no longer determined by $\rho$ alone.
- Gauss's law holds for any closed surface, but $\mathbf E$ can be pulled out of the integral and solved directly only when the charge distribution has sufficient symmetry.
- The potential is single-valued only in electrostatic fields; the Faraday induced electric field is non-conservative and admits no global potential.
- The superposition principle requires linear field equations; strongly nonlinear media require separate treatment.
- Taking infinity as the zero-potential reference applies only to finite charge distributions; for an infinite charged line a finite reference point must be used instead.

### Common Errors

| Error | Correct |
|---|---|
| Superposing potential as a vector | $V$ is a scalar, added algebraically; only $\mathbf E$ is added as a vector by components |
| Writing $\mathbf E=+\nabla V$ | $\mathbf E=-\nabla V$ |
| Gaussian surface mismatched with the symmetry | On the Gaussian surface, $\mathbf E$ must be constant in magnitude or perpendicular/parallel to the surface element |
| $\mathbf E\neq0$ inside a conductor | In electrostatic equilibrium $\mathbf E=0$; net charge resides on the surface |
| Taking infinity as zero potential for an infinite distribution | Use a finite reference point, otherwise the integral diverges |
| Writing $\mathbf D=\varepsilon_0\mathbf E$ in a medium | In linear media $\mathbf D=\varepsilon\mathbf E$; write the boundary conditions separately |

## 2. Magnetostatics & Vector Analysis

### Identifying Features

- Steady currents ($\nabla\cdot\mathbf J=0$) producing magnetic fields; or forces on charged particles/current elements in a known magnetic field.
- Quantities sought are $\mathbf B$, magnetic forces, magnetic flux, inductance, and magnetic-field energy.
- Vector identities or boundary conditions are needed to check field solutions.

### Modeling Steps

1. Declare the current type (line current $I$, surface current $\mathbf K$, volume current $\mathbf J$) and the coordinate system.
2. Symmetry analysis: infinite straight wire (cylindrical symmetry) → Ampère's circuital law:

$$
\oint_C \mathbf B\cdot d\mathbf l = \mu_0 I_{\mathrm{enc}}
$$

3. General geometry → Biot-Savart law:

$$
d\mathbf B = \frac{\mu_0}{4\pi}\frac{I\,d\mathbf l'\times(\mathbf r-\mathbf r')}{|\mathbf r-\mathbf r'|^3}
$$

4. Lorentz force: $\mathbf F = q(\mathbf E + \mathbf v\times\mathbf B)$; for a current element $\mathbf F = I\,d\mathbf l\times\mathbf B$.
5. Cross-check with vector identities and boundary conditions: $\nabla\cdot\mathbf B=0$, $\nabla\times\mathbf B = \mu_0\mathbf J$ (magnetostatics), $B_{1n}=B_{2n}$, $H_{1t}-H_{2t}=K_{\mathrm{free}}$.
6. Magnetic-field energy: $U = \frac{1}{2}LI^2 = \int \frac{B^2}{2\mu_0}\,dV$ (linear, lossless media).

### Verification Set

Required: F, L, B (C when applicable); recommended additional: I, E, J.

### Applicability Conditions to Check

- Magnetostatics requires steady currents ($\nabla\cdot\mathbf J=0$); when displacement current is present, the Maxwell-Ampère equation must be used.
- Ampère's circuital law always holds, but $\mathbf B$ can be pulled out of the integral only for highly symmetric current distributions.
- Magnetic forces do no work: $q\mathbf v\times\mathbf B$ is perpendicular to the velocity, so the speed is unchanged; energy changes can come only from electric fields or non-electromagnetic forces.
- In linear media $\mathbf B=\mu\mathbf H$; ferromagnetic materials are nonlinear and not covered.
- Biot-Savart cross-product direction: $d\mathbf l'\times(\mathbf r-\mathbf r')$; reversing the order flips the direction.

### Common Errors

| Error | Correct |
|---|---|
| Lorentz magnetic force doing work and changing the speed | Magnetic forces do no work; they only change the direction |
| Cross-product order reversed | Check Biot-Savart and $\mathbf v\times\mathbf B$ term by term with the right-hand rule |
| Forcing Ampère's law without symmetry | Ampère's law always holds but is not solvable there; switch to Biot-Savart |
| Mixing up $\mathbf B$ and $\mathbf H$ | In vacuum $\mathbf B=\mu_0\mathbf H$; media and boundary conditions are handled separately |
| Missing displacement current beyond magnetostatics | For time-varying fields use $\nabla\times\mathbf B = \mu_0\mathbf J + \mu_0\varepsilon_0\partial\mathbf E/\partial t$ |
| Drawing magnetic field lines starting/ending at sources | $\nabla\cdot\mathbf B=0$; magnetic field lines are closed |

## 3. Circuit Transients (RC/RL/RLC Circuits)

### Identifying Features

- Lumped circuits: resistors, capacitors, inductors with DC/sinusoidal sources; circuit dimensions much smaller than the wavelength (quasi-static).
- Quantities sought are currents, voltages, time constants, energies, and transient solutions.

### Modeling Steps

1. Mark current directions and loop orientations; write KCL (charge conservation) and KVL (energy conservation).
2. Use the capacitor/inductor element relations: $I=C\,dV/dt$ (with a stated charging-direction convention), $V_L = L\,dI/dt$.
3. RC discharge:

$$
\frac{dV}{dt} + \frac{1}{RC}V = 0, \qquad V(t)=V_0 e^{-t/\tau},\ \tau=RC
$$

4. RL discharge:

$$
L\frac{dI}{dt} + RI = 0, \qquad I(t)=I_0 e^{-t/\tau},\ \tau=L/R
$$

5. Series RLC: $L\ddot q + R\dot q + q/C = 0$; classify underdamped/critical/overdamped, and write $\omega_0 = 1/\sqrt{LC}$, $\alpha=R/(2L)$, $\omega_d=\sqrt{\omega_0^2-\alpha^2}$.
6. Energy cross-check: $U_C = \frac12 CV^2$, $U_L=\frac12 LI^2$, dissipated power $P_R=I^2R$.

### Verification Set

Required: F, L, B (C when applicable); recommended additional: E, D.

### Applicability Conditions to Check

- Lumped circuits require dimensions much smaller than the electromagnetic wavelength; high-frequency/long-line problems require distributed-parameter models.
- Capacitors and inductors are linear elements; nonlinear elements require their own I-V characteristics.
- Energy conservation holds only with no external injection or with source power properly accounted for; for RC discharge verify $P_R=-dU_C/dt$ directly.
- $t\to\infty$ steady state: capacitors act as open circuits, inductors as short circuits (DC).

### Common Errors

| Error | Correct |
|---|---|
| Time constant written as the reciprocal of $RC$ | RC discharge: $\tau=RC$; RL discharge: $\tau=L/R$ |
| Exponential sign reversed | Discharge: $e^{-t/\tau}$; charging: $1-e^{-t/\tau}$ |
| Current-direction convention inconsistent with $I=C\,dV/dt$ | Fix the loop orientation first, then write element relations with consistent signs throughout |
| Mixing capacitor/inductor series-parallel rules with resistor rules | Capacitors add in parallel, combine by reciprocals in series; resistors are the opposite |
| Judging RLC underdamping from $R$ alone | Compare $R^2$ with $4L/C$ |
| Ignoring initial capacitor voltage/inductor current | First-order transients require initial conditions to fix the constants |

### Electromagnetic Induction (Faraday's Law and Motional EMF)

Problems of the "time-varying magnetic flux, moving conductors" type in the method selection table are modeled as follows:

1. Induced EMF (fixed loop, time-varying magnetic field): $\mathcal{E}=-\dfrac{d}{dt}\displaystyle\int_S\mathbf B\cdot d\mathbf A$; the induced electric field is non-conservative and admits no global potential.
2. Motional EMF (conductor moving in a magnetic field): $\mathcal{E}=\oint(\mathbf v\times\mathbf B)\cdot d\mathbf l$; the result must agree with the induced-EMF route (I independent-method strong check).
3. Direction determined by Lenz's law: the induced effect opposes the change in flux; the minus sign cannot be omitted.
4. Verification: in addition to the required F/L/B, the limits $\dot{\mathbf B}\to0$ or $v\to0$ should give $\mathcal E\to0$; the dimension is volts.

| Error | Correct |
|---|---|
| Double-counting induced and motional EMF | The same flux change is counted once; the two routes cross-check each other |
| Direction not checked with Lenz's law | The effect of the induced current opposes the change in flux |
| Wrong area for the flux | $S$ is the area enclosed by the loop, not the conductor's cross-sectional area |

## 4. Basic Applications of Maxwell's Equations

### Identifying Features

- Time-varying electromagnetic fields, electromagnetic waves, displacement current, Poynting vector.
- Quantities sought are field equations, wave speed, and energy flow of fields and waves.

### Modeling Steps

1. Write the differential forms:

$$
\nabla\cdot\mathbf E = \frac{\rho}{\varepsilon_0}, \qquad
\nabla\cdot\mathbf B = 0
$$

$$
\nabla\times\mathbf E = -\frac{\partial\mathbf B}{\partial t}, \qquad
\nabla\times\mathbf B = \mu_0\mathbf J + \mu_0\varepsilon_0\frac{\partial\mathbf E}{\partial t}
$$

2. In free space ($\rho=0,\mathbf J=0$), take the curl to obtain the wave equation:

$$
\nabla^2\mathbf E = \mu_0\varepsilon_0\frac{\partial^2\mathbf E}{\partial t^2}, \qquad c=\frac{1}{\sqrt{\mu_0\varepsilon_0}}
$$

3. Plane waves: $\mathbf E\perp\mathbf B\perp$ propagation direction, $|\mathbf E|=c|\mathbf B|$.
4. Energy flow: Poynting vector $\mathbf S = \frac{1}{\mu_0}\mathbf E\times\mathbf B$; energy density $u=\frac12\varepsilon_0E^2+\frac{1}{2\mu_0}B^2$.
5. Interface boundary conditions: $D_{1n}-D_{2n}=\sigma_{\mathrm{free}}$, $E_{1t}=E_{2t}$, $B_{1n}=B_{2n}$, $H_{1t}-H_{2t}=K_{\mathrm{free}}$.

### Verification Set

Required: F, L, B (C when applicable); recommended additional: J, E, D.

### Applicability Conditions to Check

- Classical electromagnetism, no relativistic field transformations; high-speed frame transformations are beyond scope.
- The displacement current cannot be omitted: removing it contradicts charge conservation.
- Plane-wave solutions apply only in free space far from sources; near conductors/boundaries the boundary conditions must be satisfied.
- Static limit: as $\partial/\partial t\to0$, the equations should reduce to Gauss's law and Ampère's circuital law respectively.

### Common Errors

| Error | Correct |
|---|---|
| Missing minus sign in Faraday's law | $\nabla\times\mathbf E=-\partial\mathbf B/\partial t$ |
| Missing displacement current in the Maxwell-Ampère equation | Add $\mu_0\varepsilon_0\partial\mathbf E/\partial t$ |
| $\mathbf E$ parallel to $\mathbf B$ in a plane wave | They are mutually perpendicular and both perpendicular to the propagation direction |
| Applying $|\mathbf E|=c|\mathbf B|$ in a conducting medium | Holds only in free space; wave speed and impedance change in media |
| Listing boundary conditions for $E$ only or $B$ only | List all four normal/tangential conditions separately for each interface |

## 5. Formulas & Traps

### Formula Quick Reference

Coulomb's law and Gauss's law:

$$
\mathbf F = \frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r^2}\hat{\mathbf r}, \qquad
\oint_S \mathbf E\cdot d\mathbf A = \frac{Q_{\mathrm{enc}}}{\varepsilon_0}
$$

Potential and field strength:

$$
V(\mathbf r)=\frac{1}{4\pi\varepsilon_0}\frac{Q}{r}, \qquad
\mathbf E = -\nabla V
$$

Capacitance/inductance:

$$
C=\frac{Q}{V}=\varepsilon_0\frac{A}{d}, \qquad
L=\frac{N\Phi}{I}, \qquad
U_C=\frac12 CV^2,\quad U_L=\frac12 LI^2
$$

Circuit time constants and RLC:

$$
\tau_{RC}=RC, \qquad \tau_{RL}=\frac{L}{R}, \qquad
\omega_0=\frac{1}{\sqrt{LC}}, \qquad \alpha=\frac{R}{2L}
$$

Lorentz force, Biot-Savart, Ampère's circuital law:

$$
\mathbf F=q(\mathbf E+\mathbf v\times\mathbf B), \qquad
d\mathbf B=\frac{\mu_0}{4\pi}\frac{I\,d\mathbf l'\times(\mathbf r-\mathbf r')}{|\mathbf r-\mathbf r'|^3}, \qquad
\oint_C \mathbf B\cdot d\mathbf l=\mu_0 I_{\mathrm{enc}}
$$

Faraday's law:

$$
\mathcal{E}=-\frac{d\Phi_B}{dt}, \qquad
\Phi_B=\int_S \mathbf B\cdot d\mathbf A
$$

Vector identities:

$$
\nabla\times(\nabla\varphi)=0, \qquad
\nabla\cdot(\nabla\times\mathbf A)=0, \qquad
\nabla\times(\nabla\times\mathbf A)=\nabla(\nabla\cdot\mathbf A)-\nabla^2\mathbf A
$$

### Cross-Domain Traps

Cross-domain common traps (SI/CGS mixing, missing units, etc.) are covered in `error_prevention.md` §0–§3. Traps **specific** to this module (adding potential as a vector, forcing Gauss's law without symmetry, missing displacement current, etc.) are already listed in the Common Errors tables of each section and are not repeated here.
