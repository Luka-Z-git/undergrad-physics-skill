# Basic Quantum Mechanics Module

## Scope

**Basic quantum mechanics**: wavefunctions and the probability interpretation, the time-independent Schrödinger equation, one-dimensional wells/barriers, the harmonic oscillator, operators and commutators, angular momentum, and an introductory treatment of hydrogen-atom energy levels (**non-relativistic, fine structure ignored**).

(Standard sub-domain structure is the same as `mechanics.md`.)

## 0. Method Selection Table

Select the equation framework by system features; when multiple methods work, choose the shortest derivation with the most direct verification and state the reason in one sentence in the Modeling section.

| System features | Preferred method | Reason | Domain-specific verification |
|---|---|---|---|
| 1D time-independent potential (well/barrier/oscillator) | Solve the time-independent Schrödinger equation (§1) | Directly obtain eigenfunctions and eigenvalues | B ($H\psi=E\psi$), J (normalization/orthogonality) |
| Harmonic-oscillator levels and states | Ladder operators (§2) | Algebraic method avoids solving the ODE | J ($[a,a^\dagger]=1$, normalization) |
| Operator ordering / observability | Commutator expansion (§2) | Apply term-by-term to a test function | J (Hermiticity, commutator result) |
| Angular-momentum eigenvalue problem | Eigenvalue equation (§3) | Known $L^2,L_z$ spectra | J ($m$ range, normalization) |
| Hydrogen / hydrogen-like energy levels | Spherical separation of variables (§3) | Standard textbook solution | L ($n\to\infty$, $n=1$ ground state), J (normalization) |

## 1. The Time-Independent Schrödinger Equation and 1D Systems

### Identifying Features

- Time-independent potential; solve for bound-state energies, wavefunctions, transmission/reflection coefficients.
- 1D infinite well, finite well, barrier, harmonic oscillator.
- Requires normalization, boundary conditions, node count, or degeneracy checks.

### Modeling Steps

1. State units, single particle, non-relativistic; write the time-independent equation:

$$
\left[-\frac{\hbar^2}{2m}\frac{d^2}{dx^2} + V(x)\right]\psi(x) = E\psi(x)
$$

2. Solve region by region; at potential jumps use the boundary conditions: $\psi$ continuous, and $\psi'$ continuous when $V$ is finite; at an infinite wall $\psi=0$.
3. Boundary conditions yield the quantization condition; bound states require $E<V(\infty)$, scattering states $E>V(\infty)$ form a continuous spectrum.
4. Normalize: $\int_{-\infty}^{+\infty}|\psi|^2\,dx = 1$; for multiple states also check orthogonality.
5. Probability interpretation: $|\psi(x)|^2$ is the probability density; stationary-state densities do not depend on time.

### Verification Set

Mandatory F, L, B (C when applicable); recommended J, E, D.

### Applicability Conditions to Check

- Non-relativistic single particle; $V$ must be time-independent to separate $\psi(x)e^{-iEt/\hbar}$.
- Bound-state wavefunctions are square-integrable; scattering states use probability current rather than normalizing to 1.
- The Hamiltonian is Hermitian with real eigenvalues; eigenfunctions of distinct eigenvalues are orthogonal.
- 1D bound states are non-degenerate (spin ignored); node theorem: the $n$-th excited state has $n$ nodes.

### Common Errors

| Error | Correct |
|---|---|
| At an infinite well, imposing only $\psi'$ continuity | At an infinite wall $\psi=0$, $\psi'$ is discontinuous |
| Forgetting normalization | Bound states require $\int|\psi|^2=1$ |
| Treating $\psi$ itself as probability | Probability density is $|\psi|^2$ |
| Confusing energy $E$ with angular frequency | $E=\hbar\omega$; $\omega$ applies only to periodic processes |
| Finite barrier: missing transmission/reflection coefficients | Keep incident/reflected/transmitted regions and check probability-current conservation |
| Mixing $E=h\nu$ with $E=\hbar\omega$ | $\hbar\omega=h\nu$, both equal the same energy |

## 2. Operators and Commutators

### Identifying Features

- Questions about observable operators, commutators, uncertainty relations, Hermiticity.
- Constructing the harmonic-oscillator spectrum with ladder operators.

### Modeling Steps

1. Write the position and momentum operators: $\hat x=x$, $\hat p=-i\hbar\frac{d}{dx}$.
2. Expand the commutator on an arbitrary differentiable test function $f$:

$$
[\hat x,\hat p]f = \hat x\hat p f - \hat p\hat x f = i\hbar f
$$

3. Check Hermiticity: $\langle\psi|\hat A\phi\rangle=\langle\hat A\psi|\phi\rangle$; eigenvalues real, eigenstates of distinct eigenvalues orthogonal.
4. Uncertainty relation:

$$
\Delta A\,\Delta B \ge \frac{1}{2}\left|\langle[\hat A,\hat B]\rangle\right|
$$

5. Harmonic-oscillator ladder operators:

$$
\hat a=\sqrt{\frac{m\omega}{2\hbar}}\left(\hat x+\frac{i\hat p}{m\omega}\right), \qquad
[\hat a,\hat a^\dagger]=1, \qquad
\hat H=\hbar\omega\left(\hat a^\dagger\hat a+\frac12\right)
$$

### Verification Set

Mandatory F, L, B (C when applicable); recommended J, E, D.

### Applicability Conditions to Check

- Observables correspond to Hermitian operators; non-Hermitian operators (e.g. $\hat a$) are not direct observables.
- Operator order is not commutative; keep the order when expanding a commutator.
- The uncertainty relation applies to any two observables; equality holds only for special states such as coherent states.

### Common Errors

| Error | Correct |
|---|---|
| $\hat p=+i\hbar\,d/dx$ | $\hat p=-i\hbar\,d/dx$ |
| Swapping operator order | Keep the order when expanding $[\hat A,\hat B]$ |
| Treating a non-Hermitian operator as observable | Check Hermiticity first |
| $[\hat a,\hat a^\dagger]=0$ | $=1$ |
| Writing $[\hat x,\hat p]$ as a bare number without acting on a function | Expand on an arbitrary test function |

## 3. Angular Momentum and the Hydrogen Atom

### Identifying Features

- Spherically symmetric potentials, angular-momentum eigenvalues, magnetic quantum numbers, hydrogen / hydrogen-like energy levels.

### Modeling Steps

1. Angular-momentum eigenvalue equations:

$$
\hat L^2 Y_{lm}=\hbar^2 l(l+1)Y_{lm}, \qquad
\hat L_z Y_{lm}=m\hbar Y_{lm}, \qquad m=-l,\ldots,l
$$

2. Separate variables in a spherically symmetric potential: $\psi=R_{nl}(r)Y_{lm}(\theta,\phi)$.
3. Solve the radial equation for the hydrogen energy levels:

$$
E_n=-\frac{\mu e^4}{2(4\pi\varepsilon_0)^2\hbar^2}\frac{1}{n^2}=-\frac{13.6\,\mathrm{eV}}{n^2}
$$

4. Bohr radius $a_0=\frac{4\pi\varepsilon_0\hbar^2}{m_e e^2}=0.529\,\mathrm{\AA}$.
5. Degeneracy: given $n$ there are $n^2$ states (spin ignored; $2n^2$ with spin).

### Verification Set

Mandatory F, L, B (C when applicable); recommended J, E, D.

### Applicability Conditions to Check

- Non-relativistic, no spin-orbit coupling, no external field; **all hydrogen-atom results in this module are non-relativistic and ignore fine structure, hyperfine structure, and the Lamb shift**; fine structure and the Zeeman effect are out of scope.
- In the hydrogen formula $\mu$ is the reduced mass; for an electron around a proton $\mu\approx m_e$.
- Bound states require $E<0$; $n=1$ is the ground state.

### Common Errors

| Error | Correct |
|---|---|
| Using electron mass instead of reduced mass without stating it | Write reduced mass $\mu$; state the infinite-nucleus approximation |
| Forgetting the $n^2$ degeneracy | $n^2$ without spin, $2n^2$ with spin |
| $E_n\propto -1/n$ | $-1/n^2$ |
| Magnetic quantum number outside $[-l,l]$ | $m=-l,\ldots,l$, $2l+1$ values |
| Ignoring wavefunction / angular normalization | Normalize $Y_{lm}$ and $R_{nl}$ separately |

## 4. Formula Reference and Traps

### Formula Reference

Time-independent Schrödinger equation:

$$
\hat H\psi=E\psi, \qquad
\hat H=-\frac{\hbar^2}{2m}\nabla^2+V
$$

Commutator and uncertainty:

$$
[\hat x,\hat p]=i\hbar, \qquad
\Delta x\,\Delta p\ge\frac{\hbar}{2}
$$

1D infinite well ($0<x<L$):

$$
\psi_n=\sqrt{\frac{2}{L}}\sin\frac{n\pi x}{L}, \qquad
E_n=\frac{n^2\pi^2\hbar^2}{2mL^2}
$$

Harmonic oscillator:

$$
E_n=\left(n+\frac12\right)\hbar\omega, \qquad
\psi_0=\left(\frac{m\omega}{\pi\hbar}\right)^{1/4}e^{-m\omega x^2/(2\hbar)}
$$

Angular momentum and hydrogen:

$$
\hat L^2|l,m\rangle=\hbar^2 l(l+1)|l,m\rangle, \qquad
E_n=-\frac{13.6\,\mathrm{eV}}{n^2}
$$

### Cross-Domain Traps

For shared traps (missing units, etc.) see `error_prevention.md` §0–§3. Domain-specific traps ($\hat p$ sign, operator ordering, normalization, $h\nu$ vs $\hbar\omega$) are listed in the common-error tables above.
