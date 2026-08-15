---
name: undergrad-physics-skill
version: 0.6.0
description: Undergraduate physics (mechanics, electromagnetism, basic quantum mechanics): step-by-step derivations with mandatory F/L/B/C verification before final answers. Use when deriving equations of motion, solving field/circuit/Schrödinger problems, verifying a derivation, or diagnosing a student's attempted solution. 本科物理习题（理论力学/电磁学/基础量子力学）分步推导、验算、检查学生作答。
---

# undergrad-physics-skill

Undergraduate physics problem-solving skill: step-by-step derivation + built-in verification + Chinese narration + Overleaf-compilable output.

> English modules under `modules/en/` are synced artifacts of the Chinese originals. Edit the Chinese modules first; update the English copies during release.

## Positioning

A derivation-oriented skill for undergraduate physics problems (classical mechanics, electromagnetism, basic quantum mechanics). Every solution must follow **step-by-step derivation → multi-method independent verification → final answer only after verification passes**. When verification fails, roll back and fix; when verification is impossible, state so honestly — outputting an unverified "best guess" is forbidden.

This skill has zero external dependencies: the verification flow is executed by reasoning itself (hand calculation / symbolic substitution / numerical sampling), without relying on any script, environment, or plugin. Optionally, when Python/SymPy is available in the environment and the user requests it, symbolic computation can be used for cross-checking (see `modules/computation.md`), but the skill works fully without it.

## Scope

- **Classical mechanics**: Newtonian mechanics, Lagrangian mechanics, Hamiltonian mechanics, differential equations of motion, conserved quantities, small oscillations and normal modes, constrained systems, rigid-body basics (planar motion / rolling without slipping / collisions), non-inertial frames.
- **Electromagnetism**: electrostatics, magnetostatics (vacuum-focused; linear media only at the boundary-condition level, no polarization/magnetization derivations), vector calculus (gradient/divergence/curl), potential and field strength, capacitance/inductance, circuits (RC/RL/RLC), basic applications of Maxwell's equations.
- **Basic quantum mechanics**: time-independent Schrödinger equation, one-dimensional wells/barriers, harmonic oscillator, angular momentum and operators, commutation relations, introductory derivation of hydrogen energy levels.

## Out of Scope

- Other undergraduate areas: thermodynamics, optics, statistical physics, special relativity, etc. (this skill covers only classical mechanics, electromagnetism, and basic quantum mechanics).
- Graduate-level courses: quantum field theory, general relativity, group theory, many-body theory, cosmology, etc.
- Research workflows: paper reproduction, arXiv reading, multi-agent research pipelines.
- Pure lab-course content, computational physics programming tasks.
- Workflows that only review independently without solving or diagnosing are out of scope.

## Core Workflow

Execute the following steps in order for every problem; proceed to the next step only after the completion criterion of the current step is met.

1. **Parse**: extract the physical system — objects, degrees of freedom, constraints, coordinate system, unit system, initial/boundary conditions, known and unknown quantities; list implicit conditions (e.g., nonzero denominators, reality of energy, parameter ranges); if `examples/` contains a matching problem-type example, read its template structure and verification style first (format reference only — do not copy its answer). **When conditions are insufficient or the statement is ambiguous**: prefer asking the user to clarify missing key parameters; when reasonable assumptions can be made, state them explicitly and continue — fabricating numerical values not given in the problem is forbidden. Completion criterion: all the above items are explicitly listed, with no undeclared parameters or conditions.
2. **Model**: choose the equation framework (Newton / Lagrange / Hamilton / Maxwell / Schrödinger) and explain the choice; write the explicit form of the Lagrangian, Hamiltonian, or equation system; confirm the applicability conditions of every theorem/law invoked. Completion criterion: equation framework, explicit expressions, and applicability conditions all present.
3. **Derive**: step-by-step derivation, each step annotated with its justification; symbolic derivation first, numerical substitution last; at least once every 3–5 steps, run an F dimensional check or E numerical sampling and record the result inline; linear-algebra subproblems such as matrices, eigenvalues, matrix powers, and recurrences may be delegated to Math.Skill with a note of which results were borrowed (Math.Skill is an optional external skill — this skill does not depend on its existence); without Math.Skill, compute by hand per J consistency. Completion criterion: every step has a justification and is independently verifiable; symbolic derivation completed before numerical substitution.
4. **Verify**: a standard solution must check F dimensions, L limit/special case, B back-substitution, C conserved quantities (when applicable), plus optional bonus items per problem type; give PASS/FAIL item by item; on failure, enter the backtracking correction protocol. Completion criterion: the verification gate passes — all four mandatory checks PASS or N/A (with reason), FAIL 0 items.
5. **Review (optional)**: when the user demands high confidence or the problem is complex, run an independent review per `modules/review_engine.md` and append the review conclusion; skip when not requested. Completion criterion: when triggered, P1–P5 all PASS, or a clean-sheet re-derivation yields FAIL 0 items.
6. **Answer**: first execute the structural gate of the selected template (default Template A with six sections, see `modules/output_templates.md`); then give the final answer (bold, with units and applicability conditions) plus a one-line verification summary; list this problem's genuine pitfalls (omit if none). Completion criterion: the selected template's structural gate passes, and the answer bolding, verification summary, and formatting rules are all satisfied.

## Optional Mode: Student Diagnosis

The default main flow is full problem solving (Template A). When the user asks to check or diagnose their attempt, enter Student Diagnosis mode first; return to the main flow only after the diagnosis ends and the student explicitly asks for a complete solution.

- Mode routing: by default, solve from scratch (Template A); when the user submits an attempt for checking, enter Template C/E without automatically expanding a full answer; high-confidence review follows `modules/review_engine.md`.
- Trigger words and the diagnosis protocol are in `modules/tutoring_mode.md`; output uses Template E.
- Diagnosis mode points out missing items and errors directly — no hint-tiering, no automatic full-answer expansion.

## Verification Engine (Summary)

A standard solution must check **① F dimensions, ② L limit/special case, ③ B back-substitution, ④ C conserved quantities (when applicable)**; any FAIL rolls back to the last passed intermediate result and re-derives from that point; fabricating PASS is forbidden (PASS = an actually executed check + re-checkable steps). The full methods, problem-type selection table, and backtracking protocol are in `modules/verification_engine.md`.

## Output Rules

- Prefer `$$ ... $$` blocks for formulas; inline `$...$` only for short symbols.
- Chinese narration + standard LaTeX; strip emoji and any characters that would break Overleaf compilation; verification results use plain-text `PASS`/`FAIL`.
- Template A's six fixed section titles: 题意与图景 (Problem Restatement), 建模 (Modeling), 推导 (Derivation), 验算 (Verification), 答案 (Answer), 易错点 (Common Pitfalls); each section stands alone — no merging.
- Each line of the 验算 section starts with `①②③④` (optional `⑤⑥`, domain-mandatory `⑦J`); the 答案 section uses explicit Markdown `**...**` bolding — `\boxed{}` is not a substitute.
- The final answer must append a one-line verification summary, e.g.: `已通过 ①②③④，FAIL 0 项`.
- Output must be fully copy-pasteable into Overleaf for compilation.

## Honesty Principles

- Do not fabricate theorems, formulas, or "obviously true" derivation steps; mark uncertain intermediate steps explicitly.
- When verification fails and cannot be fixed, state so honestly — do not mask it with wording like "should pass verification".
- Physical quantities carry units throughout; declare the unit system (SI/CGS) explicitly in the Parse step.

## Module Index

| Module | File | Purpose |
|---|---|---|
| Verification Engine | `modules/verification_engine.md` | 8 verification methods, problem-type selection table, backtracking correction protocol, verification summary format |
| Independent Review | `modules/review_engine.md` | Optional post-hoc review: pathology filters P1–P5 and clean-sheet re-derivation |
| Student Diagnosis | `modules/tutoring_mode.md` | Optional branch: check student attempts, locate errors and conceptual misconceptions |
| Classical Mechanics | `modules/mechanics.md` | Domain protocols and common errors for Newton / Lagrange / Hamilton / small oscillations / conserved quantities / non-inertial frames |
| Electromagnetism | `modules/electromagnetism.md` | Electrostatics / magnetostatics / vector calculus / circuits / Maxwell basics |
| Quantum Basics | `modules/quantum_basics.md` | Time-independent Schrödinger / operators / commutators / one-dimensional systems |
| Error Prevention | `modules/error_prevention.md` | Cross-domain error checklist and pitfall tables |
| Output Templates | `modules/output_templates.md` | Standard solution / answer-only / solution-check templates and hard rules |
| Symbolic Computation | `modules/computation.md` | Optional SymPy/SciPy cross-check recipes (graceful degradation without dependencies) |
| Examples | `examples/` | Complete worked examples with verification |
| Tests | `tests/` | Test-case assertions (TC-XXX-NNN) |

In case of conflict, the module file takes precedence for its own domain.
