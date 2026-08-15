# undergrad-physics-skill

![License](https://img.shields.io/badge/License-MIT%20%2B%20CC%20BY%204.0-orange)
![Examples](https://img.shields.io/badge/examples-20-blue)
![Tests](https://img.shields.io/badge/tests-18-blue)

A Codex/Claude skill for solving undergraduate physics problems with
step-by-step derivations, built-in verification, Chinese explanations, and
LaTeX-ready output.

Covers: theoretical mechanics, electromagnetism, and basic quantum
mechanics (v0.7.0).

A quick-start demo is available in [docs/QUICKSTART_DEMO.md](docs/QUICKSTART_DEMO.md).

## Features

- **Zero hard dependencies**: pure Markdown skill; verification is executed
  by reasoning, not by scripts.
- **Step-by-step workflow**: Parse -> Model -> Derive -> Verify -> Review
  (optional) -> Answer.
- **Built-in verification**: 8 methods (F dimensional analysis / D domain /
  B back-substitution / C conservation / L limiting cases / E numerical
  sampling / I independent method / J consistency). Template A normally uses
  F + B plus one independent check; domain-mandatory J checks cannot be
  skipped. Each PASS must include a re-checkable step; failures trigger the
  backtrack protocol.
- **Chinese + LaTeX**: display formulas use `$$ ... $$`; request LaTeX
  document mode when a compilable Overleaf document is needed.
- **Optional enhancements**: `math-skill` for linear algebra, and
  Python/SymPy/SciPy recipes for machine cross-checks. Neither is required.
- **Optional review engine**: pathology filter and blank-paper restart for
  high-confidence requests.
- **Optional student diagnosis mode**: checks a student's work, directly
  points out missing pieces and errors, maps them to physics
  misconceptions, and asks a confirmation question. It never expands to a
  full Template A answer on its own.

## Install

- **Codex**: copy the repository to
  `~/.codex/skills/undergrad-physics-skill/`.
- **Claude Code**: copy the repository to
  `~/.claude/skills/undergrad-physics-skill/`.

## Triggers

Ask a physics problem directly, for example:

- "Use the Lagrangian method to derive the equations of motion of a double pendulum."
- "Derive the cyclotron motion of a charged particle in a uniform magnetic field."
- "Solve the stationary Schrödinger equation for a one-dimensional infinite square well and verify normalization."
- "Check my work: is this step correct?" (enters student diagnosis mode)

Matrix, eigenvalue, matrix-power, and recurrence subproblems may optionally
use `math-skill`; without it, use the J consistency checks by hand.

## Scope

**Covers**: theoretical mechanics (Newtonian/Lagrangian/Hamiltonian, small
oscillations, rigid bodies, non-inertial frames), electromagnetism
(electrostatics, magnetostatics, circuits, Maxwell basics, linear-media
boundary conditions), and basic quantum mechanics (stationary Schrodinger
equation, operators, commutators, one-dimensional systems,
non-degenerate perturbation theory and spin-1/2 basics).

**Out of scope**: other undergraduate topics (thermodynamics, optics,
statistical physics, special relativity), graduate courses, research
workflows, lab-only content, and computational physics programming.

## Verification Engine (Summary)

| Code | Method | Purpose |
|---|---|---|
| F | Dimensional analysis | Always check units and final dimensions |
| D | Domain/parameter domain | Physical ranges, denominators, real roots |
| B | Back-substitution | Substitute the solution back into the original equation |
| C | Conservation law | Energy/momentum/angular momentum when applicable |
| L | Limiting case | Parameter limits must reproduce known results |
| E | Numerical sampling | Substitute concrete values and compare both sides |
| I | Independent method | Re-solve with a second framework |
| J | Consistency | Matrix identities, normalization, commutators |

Hard rules: Template A uses a minimum sufficient verification set—normally
F + B plus one independent check—and every N/A must have a physical reason.
Any FAIL triggers the backtrack protocol; after two failed corrections,
switch to an independent route or explicitly state that no verified answer
can be given. The authoritative definitions live in
`modules/verification_engine.md`.

## Repository Layout

```
undergrad-physics-skill/
|-- SKILL.md
|-- modules/
|   |-- mechanics.md
|   |-- electromagnetism.md
|   |-- quantum_basics.md
|   |-- verification_engine.md
|   |-- review_engine.md
|   |-- tutoring_mode.md
|   |-- output_templates.md
|   |-- error_prevention.md
|   |-- computation.md
|   `-- en/
|-- docs/
|-- examples/
|-- tests/
|-- CONTRIBUTING.md
|-- CHANGELOG.md
|-- NOTICE
|-- LICENSE
|-- LICENSE-APACHE
`-- LICENSE-CC-BY
```

## Development Status

- [x] v0.1: theoretical mechanics
- [x] v0.2: electromagnetism
- [x] v0.3: basic quantum mechanics
- [x] v0.4: optional student diagnosis mode (non-primary)
- [x] v0.5: production hardening — scope boundaries, difficulty grading,
  cost stop-loss in the backtrack protocol, confirmation-question standards
- [x] v0.5.1: slimming — cross-domain trap-table dedup, README/test-case
  compaction
- [x] v0.5.2: review fixes — J numbering as ⑦, step references, Faraday
  pointer, scope alignment, structural validator, license verification
- [x] v0.7: minimum sufficient verification, entry routing, LaTeX document mode, example index, adversarial cases and spot-check; includes all v0.6 P0/P1 work
- [ ] v1.0: formal release

## License

Dual-licensed: scripts (e.g. `tests/validate_structure.py`) are MIT OR
Apache-2.0 (see [LICENSE](LICENSE) and [LICENSE-APACHE](LICENSE-APACHE));
module text, examples, and tests are
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (see
[LICENSE-CC-BY](LICENSE-CC-BY)). See [NOTICE](NOTICE).

Commercial use is allowed under CC BY 4.0 with attribution; this choice
maximizes reuse. Publishing this repository constitutes public disclosure
(prior art); scripts used under Apache-2.0 carry the standard patent grant
and termination clause; the authors do not assert patents over the methods
described here.

## Reporting Issues

Found a wrong answer, skipped verification, or a formatting problem? Open an issue:

- [Wrong answer report](.github/ISSUE_TEMPLATE/wrong_answer.md): report errors, fake PASS, or missing checks
- [New example proposal](.github/ISSUE_TEMPLATE/new_example.md): propose examples for uncovered topics

Include the problem statement, the skill output, and your own derivation when possible.

## Originality

The text, examples, and tests in this repository are original. The project
only borrows methodology and structure from the projects listed in NOTICE,
without copying their source text.

## Credits

- `math-skill` - optional mathematical-reasoning collaboration skill; use J
  consistency checks by hand when it is unavailable
- [landau-mode](https://github.com/shaevitz/landau-mode) - pathology filter
  and blank-paper restart methodology
- [ScienceClaw physics-solver](https://github.com/beita6969/ScienceClaw) -
  symbolic computation recipe ideas
- [xiaozhi-skills](https://github.com/qizhitang/xiaozhi-skills) - Chinese
  physics problem-solving picture/modeling ideas
- [Agent Almanac](https://github.com/pjt222/agent-almanac) - stepwise
  protocols for electromagnetic induction and magnetic field analysis
- [Electromagnetism (LobeHub)](https://lobehub.com/skills/tibsfox-gsd-skill-creator-electromagnetism) -
  formula and pitfall reference structure
