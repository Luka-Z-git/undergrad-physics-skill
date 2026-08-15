# Output Templates

This module defines the output specification. Core principles: **clear structure, high information density, and a format matched to the delivery target**. Default output is Markdown with LaTeX formulae; switch to LaTeX document mode only when the user requests a compilable document.

## Template Selection

| User request | Template |
|---|---|
| Solve a problem / derive / find solution | A Standard Solution (default) |
| "Just the answer" / "give the result directly" | B Answer Only |
| "Check whether this step is right" / review an existing solution | C Solution Check |
| Concept/principle Q&A (no long derivation needed) | D Concept Q&A |
| "Diagnose" / "look at what I wrote" / "where did I go wrong" | E Student Diagnosis |

## Template A: Standard Solution

Output the following 6 sections in order, using the titles below verbatim; each section must stand alone. Do not merge 建模 with 推导, do not write 验算 as mixed prose, do not fold 易错点 into 答案. The structural gate below must be passed before output.

Fixed titles (use verbatim): `题意与图景`, `建模`, `推导`, `验算`, `答案`, `易错点`.

### 1. 题意与图景 (Problem Restatement)

- Restate the physical system in one sentence: objects, degrees of freedom, constraints, coordinate system, unit system, initial/boundary conditions. Do not copy the original problem text.
- One line listing: known quantities (symbol + value + unit) → quantities to find.

### 2. 建模 (Modeling)

- State the chosen equation framework (Newton / Lagrange / Hamilton / Maxwell / Schrödinger) and the reason for the choice (one clause, e.g., "constraints are holonomic and non-conservative forces can be absorbed into generalized forces, so Lagrangian mechanics is used").
- Write the explicit form of $L$, $H$, or the EOM.
- State the applicability conditions of every law invoked (inertial frame, no dissipation, potential field, stationary state, ...).

### 3. 推导 (Derivation)

- Step-by-step derivation, each step annotated with its justification ("by the E-L equation", "substituting the constraint").
- Symbols before numbers: carry the symbolic derivation through first; substitute numerical values only at the end.
- At each key intermediate result, approximation/representation change, and before the final result, run the most appropriate quick check and record it inline.
- When using `math-skill` for matrix / eigenvalue / matrix-power / recurrence subproblems, note which results were borrowed (e.g., "matrix part verified by math-skill").
- Write only necessary steps; do not output equivalent matrix forms or SymPy checks by default.

### 4. 验算 (Verification)

- List items as: **method name + what was actually executed + PASS/FAIL/N/A（原因）**.
- Every PASS must contain a re-checkable concrete check (expression / substituted values / limit); a purely conclusory PASS is incomplete and triggers backtracking.
- Select a minimum sufficient verification set: normally F dimensions and B back-substitution, plus at least one independent L limit/special case, C conservation, D domain, E numerical sampling, I independent-method, or J consistency check. Keep only applicable items.
- A J consistency check required by a domain module (small oscillations / normal modes, operators and commutation relations, matrices / eigenvalues / recurrences) is mandatory and cannot be replaced by another check.
- Put each item on its own numbered line; numbering reflects the actual selection and need not be consecutive. Every N/A states a physical reason. Mark a repaired failure as "修复后 PASS" (PASS after fix).

### 5. 答案 (Answer)

- The final result must be bolded in Markdown: wrap the complete conclusion (Chinese conclusion, formula, units) in `**...**`. `\boxed{}` may additionally be used inside the formula for emphasis, but `\boxed{}` does not count as explicit bolding; a 答案 section missing `**...**` is treated as FAIL.
- Append a one-line verification summary that lists the checks actually run, e.g. `验算：①F、②B、③L，FAIL 0 项`; for non-applicable items write `N/A（原因）`.

### 6. 易错点 (Common Pitfalls)

- List only 1–3 pitfalls that genuinely exist for this problem; if none, omit.

## Template A Structural Gate (check item by item before answering)

Before outputting the final answer, check each item; if any is unmet, restructure the output — do not answer directly:

- [ ] All six section titles present and in correct order: 题意与图景, 建模, 推导, 验算, 答案, 易错点
- [ ] Each section stands alone; 建模 and 推导 are not merged, 易错点 is not folded into 答案
- [ ] The 验算 section contains a minimum sufficient set: F, B (when applicable), and at least one independent check; any domain-mandatory J is included
- [ ] The 答案 section contains explicit `**...**` bolding; `\boxed{}` is not a substitute

## Template B: Answer Only

- Give the result directly (bold, with units).
- Must append a one-line verification summary — a bare answer with zero verification is not allowed.

## Template C: Solution Check

- Point out item by item: which step is correct (cite the step), which step is wrong (cite the step + the specific reason).
- For each error, give the corrected step.
- End with a one-line conclusion: `结论：解答正确/解答含 N 处错误，已修正` (Conclusion: solution correct / solution contains N errors, corrected).

## Template D: Concept Q&A

- Direct answer + one minimal illustrative example; no irrelevant elaboration.

## Template E: Student Diagnosis

Used to examine a student's attempt; do not expand into a full solution. Fixed fields and order:

1. **完整性结论** (Completeness verdict): `完整` or `不完整（缺：方法/方程/推导/答案）`
2. **核验结果** (Verification results): the minimum sufficient set from `verification_engine.md`, normally `①F ...`, `②B ...`, plus one independent check; include any domain-mandatory J check.
3. **问题定位** (Error location): `第 N 步 / 表达式 / 错因` (step N / expression / cause of error)
4. **概念误区** (Conceptual misconception): `对应的物理概念或适用条件` (the corresponding physical concept or applicability condition)
5. **修正建议** (Correction suggestion): `正确写法 + 为什么` (correct form + why)
6. **确认题** (Confirmation question): `一道需要学生回答的短问题` (one short question the student must answer)

Rules:

- When incomplete, directly point out the missing items and what specifically to write next; no hint-tiering.
- Do not automatically output a full Template A answer; switch back to the main flow only when the student explicitly asks for a complete answer.
- Every verification line must contain `PASS`/`FAIL`; when verification is impossible, write `N/A（原因）`.
- Every verification line must contain a re-checkable concrete check (expression / substituted values / limit); a purely conclusory PASS/FAIL counts as incomplete.

## Hard Formatting Rules

1. **Formulas**: standalone formulas always use `$$ ... $$`; inline `$...$` only for short symbols ($x$, $\theta$). Full-line formulas must not use single `$`.
2. **LaTeX compatibility**: use only syntax available in standard LaTeX packages (`\frac`, `\sqrt`, `\int`, `\sum`, `\mathrm`, `\begin{cases}`); do not output emoji, checkmark/cross, or other Unicode symbols; verification results use plain-text `PASS`/`FAIL`.
3. **Units**: carry units throughout; numerical problems must give numerical results with units.
4. **Language**: Chinese narration; physics terms keep their standard forms (Lagrangian, Hamiltonian, Schrödinger, etc. may remain in English or be given bilingually).
5. **Copy-paste readiness**: default Markdown output is readable and reuses its formulae directly; when a compilable document is requested, switch to the LaTeX document mode below. Do not treat Markdown markers as LaTeX.
6. **Length**: every derivation step independently verifiable, no skipped steps; be concise by default and delete all sentences irrelevant to solving the problem unless the user asks for detail.
7. **Structural gate**: Template A must satisfy all four: the six fixed section titles, standalone sections, a minimum sufficient verification set, and `**...**` bolding in 答案; restructure before answering if any is unmet.

## Counter-examples (forbidden output)

- "好的！让我们一步一步来分析吧～" (slogan-style opening)
- "因此，答案是 2，非常简单！" (conclusion without justification)
- "我相信这个结果是正确的" (belief substituted for verification)
- Treating Markdown markers as a directly compilable LaTeX document

## LaTeX Document Mode (only when a compilable document is requested)

Replace Markdown headings with `\section*{...}`, `**conclusions**` with `\textbf{conclusions}`, and circled verification marks with ordinary `1.`, `2.` numbering to avoid Unicode dependencies. For a complete document, use this minimal preamble:

```latex
\documentclass[UTF8]{ctexart}
\usepackage{amsmath,amssymb}
\begin{document}
% Write the six sections as \section*{题意与图景}, etc.
\end{document}
```

This mode uses no Markdown tables, `**...**`, or circled numbers; numerical values, formulae, and verification evidence remain identical to Markdown mode.

By default, output the LaTeX code block only and do not create or save a file; write a file only when the user explicitly asks. For simple problems use a compact structure: one-sentence problem statement, modeling, derivation, verification, answer; pitfalls are optional. Keep simple LaTeX documents within about 60 lines, with one line of compilation notes.

## Difficulty Grading and Output Granularity (executed in step 1 of the core workflow)

After the Parse phase completes and before modeling begins, assess problem complexity and adapt output granularity per the rules below. Every difficulty uses a minimum sufficient verification set; never add an inapplicable item merely to fill a checklist.

| Complexity | Criteria | Output granularity |
|---|---|---|
| **Simple** | Derivation ≤ 3 steps; single degree of freedom; standard problem types (constant-force motion, small-angle pendulum, RC discharge, infinite square well) | Keep Template A's six sections separate but make each concise; omit 易错点 if none |
| **Medium** | Derivation 4–10 steps; 1–2 degrees of freedom; involves choices/judgments (method selection, coordinate choice) | Standard Template A with all six sections |
| **Complex** | Derivation > 10 steps; coupled multi-DOF systems (double pendulum, coupled oscillators); or user demands high confidence | Standard Template A + optional review (`review_engine.md` P1–P5); review conclusion appended after the answer |

**Discipline**:
- Declare the complexity assessment in one sentence at the end of the Parse step, e.g., "本题评估为：中等（双自由度耦合，推导约 6 步）" (assessed as: medium — two coupled DOF, ~6 derivation steps).
- Be concise by default: simple problems use ≤3 checks and a few lines; medium ≤5; complex ≤5; do not add equivalent matrix forms or SymPy checks by default.
- The compact form for simple problems retains concrete evidence for every selected check and does not require inapplicable checks.
- When the user explicitly requests a "detailed solution" / "complete steps", ignore the automatic grading and always output to the complex-problem standard.
