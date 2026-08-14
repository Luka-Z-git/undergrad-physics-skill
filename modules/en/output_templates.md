# Output Templates

This module defines the output specification. Core principles: **fixed structure, high information density, paste-ready into Overleaf for compilation**. No slogan-style encouragement, no boilerplate filler.

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
- Run a sanity check every 3–5 steps (substitute simple values or check dimensions).
- When delegating matrix / eigenvalue / matrix-power / recurrence subproblems to Math.Skill, note which results were borrowed (e.g., "matrix part verified by Math.Skill").

### 4. 验算 (Verification)

- Fixed format, item by item: **method name + what was actually executed + PASS/FAIL**.
- Every PASS must contain a re-checkable concrete check (expression / substituted values / limit); a purely conclusory PASS is treated as FAIL and triggers backtracking. Fabricating PASS is forbidden.
- Each item on its own line, starting with `①`, `②`, `③`, `④`; optional bonus items start with `⑤`, `⑥`; the domain-mandatory J consistency check starts with `⑦`. No unnumbered mixed narration.
- Mandatory checks: ① F dimensions ② L limit/special case ③ B back-substitution (substitute the solution back into the EOM / E-L / $H\psi=E\psi$) ④ C conserved quantities (when applicable).
- Optional bonus items: ⑤ E numerical sampling ⑥ I independent method.
- Domain-mandatory item: ⑦ J consistency — appears only when the domain module designates J as mandatory for that domain (small oscillations / normal modes, operators and commutation relations, matrices / eigenvalues / recurrences); same level as ①–④, must not be skipped; for other problem types do not write ⑦.
- When ④ is not applicable (no conserved quantity, dissipation, broken symmetry), write `N/A（原因）`; do not fabricate a PASS.
- Failed items must have been fixed via the backtracking protocol and annotated "修复后 PASS" (PASS after fix) on that item.

### 5. 答案 (Answer)

- The final result must be bolded in Markdown: wrap the complete conclusion (Chinese conclusion, formula, units) in `**...**`. `\boxed{}` may additionally be used inside the formula for emphasis, but `\boxed{}` does not count as explicit bolding; a 答案 section missing `**...**` is treated as FAIL.
- Append a one-line verification summary in the format: `已通过 ①②③④，FAIL 0 项`; for non-applicable items write `N/A（原因）`.

### 6. 易错点 (Common Pitfalls)

- List only 1–3 pitfalls that genuinely exist for this problem; if none, omit.

## Template A Structural Gate (check item by item before answering)

Before outputting the final answer, check each item; if any is unmet, restructure the output — do not answer directly:

- [ ] All six section titles present and in correct order: 题意与图景, 建模, 推导, 验算, 答案, 易错点
- [ ] Each section stands alone; 建模 and 推导 are not merged, 易错点 is not folded into 答案
- [ ] Every line of the 验算 section starts with ①②③④ (plus optional ⑤⑥, and domain-mandatory ⑦J); no mixed prose
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
2. **核验结果** (Verification results): item by item `①F ... PASS/FAIL/N/A（原因）`, `②L ...`, `③B ...`, `④C ...`
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
5. **Copy-paste readiness**: the output body (including all formulas) should paste directly into Overleaf and compile; do not use Overleaf-incompatible structures such as Markdown tables embedding formulas — use LaTeX `tabular` when a table is needed.
6. **Length**: every derivation step independently verifiable, no skipped steps; but delete all sentences irrelevant to solving the problem.
7. **Structural gate**: Template A must satisfy all four: the six fixed section titles, sections standing alone, 验算 numbered ①②③④ (domain-mandatory J numbered ⑦), and 答案 bolded with `**...**`; any failure is treated as FAIL and the final answer must not be released.

## Counter-examples (forbidden output)

- "好的！让我们一步一步来分析吧～" (slogan-style opening)
- "因此，答案是 2，非常简单！" (conclusion without justification)
- "我相信这个结果是正确的" (belief substituted for verification)
- Checkmark symbols or emoji in the output (Overleaf cannot compile them)

## Difficulty Grading and Output Granularity (executed in step 1 of the core workflow)

After the Parse phase completes and before modeling begins, assess problem complexity and adapt output granularity per the rules below. **The four mandatory checks (F/L/B/C) must never be omitted or downgraded at any difficulty level.**

| Complexity | Criteria | Output granularity |
|---|---|---|
| **Simple** | Derivation ≤ 3 steps; single degree of freedom; standard problem types (constant-force motion, small-angle pendulum, RC discharge, infinite square well) | Template A may be written compactly: the 推导 and 验算 sections may be merged into "推导与验算", but ①②③④ must still be listed item by item with concrete checks; omit 易错点 if none |
| **Medium** | Derivation 4–10 steps; 1–2 degrees of freedom; involves choices/judgments (method selection, coordinate choice) | Standard Template A with all six sections |
| **Complex** | Derivation > 10 steps; coupled multi-DOF systems (double pendulum, coupled oscillators); or user demands high confidence | Standard Template A + optional review (`review_engine.md` P1–P5); review conclusion appended after the answer |

**Discipline**:
- Declare the complexity assessment in one sentence at the end of the Parse step, e.g., "本题评估为：中等（双自由度耦合，推导约 6 步）" (assessed as: medium — two coupled DOF, ~6 derivation steps).
- The compact form for simple problems only permits merging the 推导 and 验算 sections structurally; it does not permit omitting any mandatory check or weakening the PASS criteria.
- When the user explicitly requests a "detailed solution" / "complete steps", ignore the automatic grading and always output to the complex-problem standard.
