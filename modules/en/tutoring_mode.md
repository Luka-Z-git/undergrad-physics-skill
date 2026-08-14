# Optional Mode: Student Diagnosis (Tutoring Mode)

This mode is an optional branch, entered only when the user explicitly asks to check or diagnose their own work; the default main flow remains Template A full problem-solving.

## Trigger

Enter this mode when the user's message contains one of the following intents:

- "诊断" ("diagnose")
- "看看我写的" ("look at what I wrote")
- "帮我检查" ("check it for me")
- "我哪里错了" ("where did I go wrong")
- "这步对吗" ("is this step correct")
- "看我卡在哪" ("see where I'm stuck")

If the user only sends a problem with no intent to have their work checked, do not enter this mode; follow the SKILL.md main flow.

## Flow

1. **Get progress**: if the student has not pasted their work, ask in one sentence: "贴出你目前的作答，至少包含你已写出的方法/方程/推导/答案，并说明卡在哪一步（可选）。" (English gloss: Paste your current work, including at least the method/equations/derivation/answer you have written so far, and state which step you are stuck on (optional).)
2. **Completeness check**: the four elements are method, equations, derivation, answer.
   - Incomplete: directly state which element is missing and give the specific next thing to write (one sentence, without expanding into a full solution).
   - Complete: proceed to verification.
3. **Verify and locate**: verify the student's results item by item using F dimension / L limit-special case / B back-substitution / C conserved quantity (where applicable); locate the first error (step + expression + cause); map it to the corresponding conceptual misconception (may cite `modules/error_prevention.md`); give the correct form and the reason.
4. **Confirm understanding**: give one short question for the student to answer, confirming they understand rather than copy.
5. **Loop**: the student revises and sends again; repeat steps 2–4; if still FAIL after two consecutive rounds, suggest switching back to Template A full solution or to independent review per `modules/review_engine.md`.

## Output Template (Template E)

Output strictly follows the six fields and their order in Template E of `modules/output_templates.md`; field definitions are not repeated here.

## Discipline

- Point out missing elements and errors directly; no hint-tiering.
- Diagnosis mode does not automatically expand into a Template A full answer; switch back to the main flow only when the student explicitly asks for a full answer.
- Do not quote full worked examples from `examples/` as a substitute answer.
- Verification discipline follows `modules/verification_engine.md`.
- For out-of-scope problems (thermodynamics, optics, statistical physics, graduate-level content), state honestly that they are not covered; do not force a solution.

## Confirmation Question Quality Standards

The confirmation question is the core teaching tool of diagnosis mode — a good confirmation question tests whether the student truly understands the concept rather than merely remembering the conclusion. **Question-design principles**:

1. It must be answerable in 1–3 sentences, but the answer must **require reasoning** (cannot be copied directly from the original problem's answer).
2. Prefer having the student **look at the same physics from a different angle** (counterfactual, limit, comparison, generalization).
3. Avoid yes/no questions ("对吗？" / "Is that right?") and pure recall questions ("记住 X=Y" / "remember X=Y").

A good/bad comparison table and scenario-based examples can be found in the "确认题质量校准参考" ("Confirmation Question Quality Calibration Reference") table at the end of `examples/tutoring_diagnosis.md`.
