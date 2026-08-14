# Independent Review Engine

This module is an **optional** post-hoc review protocol and does not run by default in the main flow. Purpose: after a standard solution is completed, independently audit the entire derivation, quickly locate suspect steps, and decide whether a full re-derivation is needed. Applies when the user demands high confidence, the problem is complex, or standard verification once FAILed before passing on re-verification.

Zero external dependencies: the review is performed by reasoning itself, with no scripts invoked; for optional symbolic review, see `computation.md`.

## 1. When to Use

- The user explicitly asks for "review / audit / double-check".
- The problem is complex, or standard verification once FAILed (even if it passed after a fix).
- The user provides an existing solution to be audited (Template C may first use this protocol to locate errors).

## 2. Pathology Filter

Check the entire derivation in order; any FAIL records a pathology:

| Code | Check | Pathology verdict |
|---|---|---|
| P1 | Dimension | Any intermediate or final expression whose dimension does not match the target physical quantity |
| P2 | Conservation | With no dissipation and valid symmetries, energy/momentum/angular momentum is not conserved, or the conserved expression drifts with time |
| P3 | Limit | Taking parameters to known limits ($\omega\to0$, $\hbar\to0$, $\theta\to0$, $m\to\infty$), the result does not reduce to the known form |
| P4 | Causality/direction | The result violates time ordering, reference-frame direction conventions, or the relationship between force and relative-motion direction |
| P5 | Domain | The result diverges at parameter boundaries, the squared frequency is negative, or the energy is negative without the applicability conditions being declared |

Each FAIL must record: **step where found + specific discrepancy + first suspect intermediate result**. Writing only "the result is wrong" is not allowed.

## 3. Blank-Paper Restart

When the Pathology Filter finds a FAIL:

1. Discard all work from the first suspect intermediate result onward; patching signs locally is forbidden.
2. Re-derive from the last complete intermediate result that passed checking (if none, return to modeling).
3. Re-derive along an independently verifiable path, or at least reorganize the derivation in a different way.
4. After re-deriving, re-run the standard four mandatory checks (F/L/B/C where applicable) and all of P1–P5.

If the re-derived result agrees with the first draft and all checks pass, record "review found no pathology"; do not force a disagreement.

## 4. Review Verdict Format

On pass:

```
复核：P1 量纲 PASS · P2 守恒 PASS · P3 极限 PASS · P4 因果 PASS · P5 定义域 PASS，FAIL 0 项
```
(English gloss: Review: P1 dimension PASS · P2 conservation PASS · P3 limit PASS · P4 causality PASS · P5 domain PASS, FAIL 0 items)

After a pathology is found and re-derived:

```
复核：P2 守恒 FAIL（第 N 步能量表达式随时间变化），已白纸重推，重推后 FAIL 0 项
```
(English gloss: Review: P2 conservation FAIL (energy expression at step N varies with time), Blank-Paper Restart performed, FAIL 0 items after re-derivation)

The review verdict is appended one line after the final answer.

## 5. Boundaries

- The review does not replace the PASS/FAIL records of the standard verification engine; both records are kept.
- When the review conflicts with the main flow's verdict, handle it per the Backtrack-and-Fix Protocol in `verification_engine.md`; neither side may be unilaterally trusted.
- This module only borrows the methodological ideas of pathology filtering and Blank-Paper Restart; its provisions are written independently and do not copy any external source text.
