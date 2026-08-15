---
name: undergrad-physics-skill
version: 0.7.0
description: Undergraduate physics (mechanics, electromagnetism, basic quantum mechanics): derivations with a minimum sufficient verification set before final answers. Use for equations of motion, field/circuit/Schrödinger problems, derivation checks, or student-answer diagnosis. 本科物理习题（理论力学/电磁学/基础量子力学）分步推导、验算、检查学生作答。
---

# undergrad-physics-skill

Undergraduate physics problem-solving skill: step-by-step derivation + built-in verification + Chinese narration + LaTeX-ready output.

> English modules under `modules/en/` are synced artifacts of the Chinese originals. Edit the Chinese modules first; update the English copies during release.

## Positioning

A derivation-oriented skill for undergraduate physics problems (classical mechanics, electromagnetism, basic quantum mechanics). Every solution follows **step-by-step derivation → minimum sufficient verification → final answer only after verification passes**. When verification cannot be completed, state the uncertainty, missing conditions, and next information needed.

This skill has zero external dependencies: the verification flow is executed by reasoning itself (hand calculation / symbolic substitution / numerical sampling), without relying on any script, environment, or plugin. Python/SymPy symbolic cross-checks are used only when the user explicitly asks, and only once; no external tools are invoked automatically by default (see `modules/computation.md`).

**Tool gate**: this skill is hand-computed by default; without an explicit user request, do not invoke Python/SymPy, math-skill, numerical-integration scripts, or other external tools, and do not claim they verified the answer.

## Scope

- **Classical mechanics**: Newtonian mechanics, Lagrangian mechanics, Hamiltonian mechanics, differential equations of motion, conserved quantities, small oscillations and normal modes, constrained systems, rigid-body basics (planar motion / rolling without slipping / collisions), non-inertial frames.
- **Electromagnetism**: electrostatics, magnetostatics (vacuum-focused; linear media only at the boundary-condition level, no polarization/magnetization derivations), vector calculus (gradient/divergence/curl), potential and field strength, capacitance/inductance, circuits (RC/RL/RLC), basic applications of Maxwell's equations.
- **Basic quantum mechanics**: time-independent Schrödinger equation, one-dimensional wells/barriers, harmonic oscillator, angular momentum and operators, commutation relations, introductory derivation of hydrogen energy levels, non-degenerate perturbation theory and spin-1/2 basics.

## Out of Scope

- Other undergraduate areas: thermodynamics, optics, statistical physics, special relativity, etc. (this skill covers only classical mechanics, electromagnetism, and basic quantum mechanics).
- Graduate-level courses: quantum field theory, general relativity, group theory, many-body theory, cosmology, etc.
- Research workflows: paper reproduction, arXiv reading, multi-agent research pipelines.
- Pure lab-course content, computational physics programming tasks.
- Workflows that only review independently without solving or diagnosing are out of scope.

## Entry Routing

| User intent | Entry |
|---|---|
| Full solution / derivation | Template A + core workflow |
| Result only | Template B + minimum necessary verification |
| Concept question | Template D + minimal example |
| Check / diagnose an attempt | Template C/E + Student Diagnosis mode |
| Compilable Overleaf document | Switch to LaTeX document mode on the entry above |

Per-template execution scope:

- Template A: full six-step workflow (review optional).
- Template B: only minimal necessary verification (F/B or one independent check), then answer; no six sections.
- Template D: direct answer plus one minimal example; no derivation workflow.
- Template C/E: locate errors per the diagnosis protocol; do not solve from scratch.
- LaTeX document mode: switch the output format on the selected entry; verification scope is unchanged.

Full template definitions live in `modules/output_templates.md`.

## Core Workflow

By default Template A runs the full six-step workflow; Templates B/D and C/E use their minimal paths (see Entry Routing) — do not run unnecessary derivation or verification. Proceed to the next step only after the completion criterion of the current step is met.

1. **Parse**: extract the physical system — objects, degrees of freedom, constraints, coordinate system, unit system, initial/boundary conditions, known and unknown quantities; list implicit conditions (e.g., nonzero denominators, reality of energy, parameter ranges). For a complex or high-risk problem, or when the user requests high confidence, use `examples/INDEX.md` to read **one** matching example for structure and verification style only. When conditions are insufficient, ask the key clarifying question; when a reasonable assumption is available, state it before continuing. Completion criterion: all the above items are explicitly listed, with no undeclared parameters or conditions.
2. **Model**: choose the equation framework (Newton / Lagrange / Hamilton / Maxwell / Schrödinger) and explain the choice; write the explicit form of the Lagrangian, Hamiltonian, or equation system; confirm the applicability conditions of every theorem/law invoked. Completion criterion: equation framework, explicit expressions, and applicability conditions all present.
3. **Derive**: step-by-step derivation, each step annotated with its justification; symbolic derivation first, numerical substitution last. At each key intermediate result, approximation/representation change, and before the final result, run the most appropriate quick check and record it inline. Linear-algebra subproblems may use `math-skill` only when the user asks, with a note of borrowed results; otherwise compute by hand per J consistency. External tools are not invoked automatically. Completion criterion: every step has a justification and is independently verifiable; symbolic derivation completed before numerical substitution.
4. **Verify**: select a minimum sufficient verification set from `modules/verification_engine.md`: normally F and B, plus one independent L/C/D/E/I/J check; default total is 3, at most 5 when the user asks for high confidence; record a physical reason for every N/A. Numerical sampling (E) uses only small hand-checkable samples; do not automatically run scripted integration. A J check required by a domain module cannot be replaced. Give PASS/FAIL item by item; on failure, enter the backtracking correction protocol. Completion criterion: every selected check PASS, every N/A justified, FAIL 0 items.
5. **Review (optional)**: when the user demands high confidence or the problem is complex, run an independent review per `modules/review_engine.md` and append a P1–P5 summary; blank-paper restart runs only when the user asks or a pathology is found. Skip when not requested. Completion criterion: when triggered, P1–P5 all PASS, or a clean-sheet re-derivation yields FAIL 0 items.
6. **Answer**: first execute the structural gate of the selected template (default Template A with six sections, see `modules/output_templates.md`); then give the final answer (bold, with units and applicability conditions) plus a one-line verification summary; list this problem's genuine pitfalls (omit if none). Completion criterion: the selected template's structural gate passes, and the answer bolding, verification summary, and formatting rules are all satisfied.

## Optional Mode: Student Diagnosis

The default main flow is full problem solving (Template A). When the user asks to check or diagnose their attempt, enter Student Diagnosis mode first; return to the main flow only after the diagnosis ends and the student explicitly asks for a complete solution.

- Mode routing: by default, solve from scratch (Template A); when the user submits an attempt for checking, enter Template C/E without automatically expanding a full answer; high-confidence review follows `modules/review_engine.md`.
- Trigger words and the diagnosis protocol are in `modules/tutoring_mode.md`; output uses Template E.
- Diagnosis mode points out missing items and errors directly — no hint-tiering, no automatic full-answer expansion.

## Verification Engine (Summary)

A standard solution uses a **minimum sufficient verification set**: normally F and B plus one independent L/C/D/E/I/J check; add J whenever its domain requires it. Any FAIL rolls back to the last passed intermediate result and re-derives from that point; a PASS contains an actually executed, re-checkable step. The full methods, problem-type selection table, and backtracking protocol are in `modules/verification_engine.md`.

## Output Rules

- Use Chinese Markdown with standard LaTeX formulae by default; template selection, structural gates, and verification-summary formats are in `modules/output_templates.md`.
- When the user requests a compilable document, use that module's LaTeX document mode; by default output the code directly without writing a file, and keep simple problems compact; do not mix Markdown markers with LaTeX-document markup.
- Without an explicit user request, do not invoke external tools or claim that SymPy/Python verified the answer.
- **Output stop-loss**: split complex or multi-part problems into sections, giving each part's final result and one-line verification first; never return an empty answer.

## Honesty Principles

- Mark uncertain theorems, formulae, or intermediate steps explicitly and say how to re-check them.
- When verification cannot be completed or fixed, state the evidence, missing conditions, and a feasible next step.
- Physical quantities carry units throughout; declare the unit system (SI/CGS) explicitly in the Parse step.

## Module Index

| Module | File | Purpose |
|---|---|---|
| Verification Engine | `modules/verification_engine.md` | 8 verification methods, problem-type selection table, backtracking correction protocol, verification summary format |
| Independent Review | `modules/review_engine.md` | Optional post-hoc review: pathology filters P1–P5 and clean-sheet re-derivation |
| Student Diagnosis | `modules/tutoring_mode.md` | Optional branch: check student attempts, locate errors and conceptual misconceptions |
| Classical Mechanics | `modules/mechanics.md` | Domain protocols and common errors for Newton / Lagrange / Hamilton / small oscillations / conserved quantities / non-inertial frames |
| Electromagnetism | `modules/electromagnetism.md` | Electrostatics / magnetostatics / vector calculus / circuits / Maxwell basics |
| Quantum Basics | `modules/quantum_basics.md` | Time-independent Schrödinger / operators / commutators / one-dimensional systems / perturbation and spin basics |
| Error Prevention | `modules/error_prevention.md` | Cross-domain error checklist and pitfall tables |
| Output Templates | `modules/output_templates.md` | Template selection, structural gates, Markdown and LaTeX document modes |
| Symbolic Computation | `modules/computation.md` | Optional SymPy/SciPy cross-check recipes (graceful degradation without dependencies) |
| Example Index | `examples/INDEX.md` | Pick one example by problem type for complex/high-risk work |
| Examples | `examples/` | Complete worked examples with verification |
| Tests | `tests/` | Test-case assertions (TC-XXX-NNN) |

In case of conflict, the module file takes precedence for its own domain.
