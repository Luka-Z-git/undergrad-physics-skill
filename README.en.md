# undergrad-physics-skill

[![validate](https://github.com/Luka-Z-git/undergrad-physics-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/Luka-Z-git/undergrad-physics-skill/actions/workflows/validate.yml)
![License](https://img.shields.io/badge/License-MIT%20%2B%20CC%20BY%204.0-orange)
![Examples](https://img.shields.io/badge/examples-20-blue)

> **Not another physics solver — a verification-and-repair layer for AI-generated undergraduate physics solutions.**

The most dangerous AI physics answers are not obvious nonsense. They are plausible derivations with a wrong sign, unit, boundary condition, limit, conservation law, or normalization. This skill requires Codex and Claude to provide re-checkable physical evidence before presenting a final answer.

[中文](README.md) · [Try it in 60 seconds](#try-it-in-60-seconds) · [Full demo](docs/QUICKSTART_DEMO.md) · [How it works](SKILL.en.md)

## Four reliability principles

- **No evidence, no PASS:** every PASS must sit next to a check the reader can reproduce.
- **Fail visibly, repair explicitly:** mark contradictions as FAIL, locate the error, return to the last reliable step, repair it, and verify again.
- **Tools must be real:** never claim a Python or SymPy check unless it actually ran; disclose a hand-check fallback when tools are unavailable.
- **Physics-aware verification:** select a minimum sufficient set of unit, substitution, boundary, limiting-case, conservation, or normalization checks for the problem at hand.

## See it catch an error

The following is a **worked demonstration of the backtrack protocol** from this repository. It shows the behavior the skill requires; it is not a model A/B benchmark.

A block of mass $m$ slides a distance $s$ down a rough incline. A plausible first attempt applies mechanical-energy conservation directly:

$$
\frac12mv^2=mgs\sin\alpha
\quad\Rightarrow\quad
v_{\rm wrong}=\sqrt{2gs\sin\alpha}.
$$

**Check → FAIL:** kinetic friction does work $W_f=-\mu mg\cos\alpha\,s\neq0$, so mechanical energy is not conserved. The derivation omitted dissipation and cannot pass the conservation check.

**Locate and repair:** return to the model and use the work-energy theorem:

$$
(mg\sin\alpha-\mu mg\cos\alpha)s=\frac12mv^2,
$$

which gives

$$
v=\sqrt{2gs(\sin\alpha-\mu\cos\alpha)}.
$$

**Re-check → PASS:** Newton's second law gives $a=g(\sin\alpha-\mu\cos\alpha)$, and $v^2=2as$ produces the same result. The expression also recovers the frictionless limit as $\mu\to0$.

[Read the complete FAIL → locate → repair → re-verify example](examples/backtrack_demonstration.md)

## Try it in 60 seconds

### 1. Install

Codex on PowerShell:

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
git clone https://github.com/Luka-Z-git/undergrad-physics-skill.git "$env:USERPROFILE\.codex\skills\undergrad-physics-skill"
```

Codex on macOS or Linux:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Luka-Z-git/undergrad-physics-skill.git ~/.codex/skills/undergrad-physics-skill
```

For Claude Code, use the same repository contents and change the target to `~/.claude/skills/undergrad-physics-skill/`. Codex is the primary verified platform. The file layout is compatible with Claude Code, but it has not received the same breadth of behavioral regression testing.

### 2. Ask

Copy this diagnostic prompt:

> For a block sliding down a rough incline, I wrote $\frac12mv^2=mgs\sin\alpha$. Check this step. Do not silently replace my answer; if a check fails, show the evidence, locate the error, repair it, and verify again.

Or try:

- “Derive the simple-pendulum equation with the Lagrangian method, then check units, substitute back into the Euler–Lagrange equation, and take the small-angle limit.”
- “Solve the one-dimensional infinite square well and verify both boundary conditions and normalization.”
- “Check my RC-discharge derivation. Identify only the first physical error instead of re-solving the entire problem.”

### 3. Know that it is working

You should see:

- an actual substitution, unit calculation, limit, or conservation relation—not merely “the result was verified”;
- evidence next to every PASS;
- an explicit “FAIL → locate → repair → re-verify” sequence when a check fails, rather than a silently replaced answer.

If you only receive a generic solution, name `undergrad-physics-skill` explicitly in your prompt and confirm that the repository's root `SKILL.md` is inside the skill directory shown above.

## Why it exists

| Common failure mode | What this skill does |
|---|---|
| A fluent derivation has a sign or dimensional error | Shows an actual dimensional check or substitution into the original equation |
| A solution satisfies the equation but ignores initial or boundary conditions | Verifies the problem constraints, not algebra alone |
| The answer says “verified” without showing a check | Refuses to mark PASS without re-checkable evidence |
| A contradiction is discovered and the answer is quietly replaced | Preserves the FAIL, locates the first bad step, repairs it, and verifies again |
| Python or SymPy is claimed without being run | Reports only real tool results; otherwise discloses a hand-check fallback |
| A student asks where one step went wrong and receives a full replacement solution | Enters diagnosis mode and identifies the first error and its underlying misconception |

## Current evidence and limitations

The repository currently provides **reviewable design constraints, worked demonstrations, and deterministic tests**:

- 20 verified worked examples, including boundary cases, degeneracies, student diagnosis, and a failure-repair demonstration;
- 12 adversarial behavior cases covering unsupported PASS claims, missed boundaries, false conservation in dissipative systems, and fabricated tool verification;
- zero-dependency structural gates, numerical regression, and size budgets in GitHub Actions;
- equivalent Chinese and English modules with explicit out-of-scope behavior.

**A model A/B benchmark is not yet complete.** Until same-model, same-problem, same-setting results are public, this project does not claim a measured accuracy improvement. The planned benchmark will report final-answer accuracy, key-derivation accuracy, undetected contradictions, unsupported PASS claims, and output-length/latency cost. See the [v1.0 improvement plan](docs/V1_IMPROVEMENT_PLAN.md).

## Scope

Currently covered:

- **Theoretical mechanics:** Newtonian, Lagrangian, and Hamiltonian mechanics; constraints; small oscillations; rigid-body basics; non-inertial frames.
- **Electromagnetism:** electrostatics, magnetostatics, circuits, basic Maxwell equations, and linear-media boundary conditions.
- **Basic quantum mechanics:** the stationary Schrödinger equation, one-dimensional systems, operators and commutators, introductory perturbation theory, and spin 1/2.

Currently out of scope: thermodynamics, statistical physics, optics/waves, special relativity, graduate courses, research workflows, laboratory-only work, and computational-physics programming. The skill declares these boundaries instead of pretending they are covered.

## How it works

A full solution follows `Parse → Model → Derive → Verify → optional Review → Answer`. Result-only requests, conceptual questions, and student diagnosis take shorter dedicated paths. A standard full solution normally checks dimensions and substitution plus one problem-specific independent test. Every non-applicable check requires a physical reason.

- [SKILL.en.md](SKILL.en.md): entry routing, core workflow, and module index;
- [Verification engine](modules/en/verification_engine.md): check selection, PASS/FAIL evidence, and backtracking;
- [Student diagnosis](modules/en/tutoring_mode.md): reviews student work without automatically revealing a full replacement solution;
- [Example index](examples/INDEX.md): routes problem types to complete examples;
- [Contributing guide](CONTRIBUTING.md): standards for new examples, modules, and tests.

## Release status

- [x] v0.1–v0.5.2: three domains, verification engine, diagnosis mode, examples, structural validation, and dual licensing;
- [x] v0.7: minimum sufficient verification, entry routing, LaTeX document mode, adversarial cases, and numerical regression;
- [x] v0.8: L1–L4 tool gate and undergraduate-coverage roadmap—**feature-complete; formal tag and GitHub Release pending**;
- [ ] v1.0: a public and reproducible physics-solving A/B benchmark.

## License and feedback

Scripts are licensed under MIT OR Apache-2.0. Module, example, and test prose is licensed under [CC BY 4.0](LICENSE-CC-BY), including commercial use with attribution and a license link. See [NOTICE](NOTICE) for details.

Found a problem? Open a:

- [Wrong-answer report](.github/ISSUE_TEMPLATE/wrong_answer.md) for incorrect solutions, unsupported PASS claims, missed verification, or tool-claim problems;
- [New-example proposal](.github/ISSUE_TEMPLATE/new_example.md) for uncovered problem types or real failures worth preserving as regressions.

If this skill catches a physics error you would otherwise have missed, consider starring the repository—or contribute the problem as a new regression case.

## Credits

This project is an independent implementation. Its structure and verification ideas were informed by `math-skill`, [landau-mode](https://github.com/shaevitz/landau-mode), [ScienceClaw physics-solver](https://github.com/beita6969/ScienceClaw), [xiaozhi-skills](https://github.com/qizhitang/xiaozhi-skills), [Agent Almanac](https://github.com/pjt222/agent-almanac), and [Electromagnetism (LobeHub)](https://lobehub.com/skills/tibsfox-gsd-skill-creator-electromagnetism). See [NOTICE](NOTICE) for upstream licensing and isolation notes.
