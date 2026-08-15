#!/usr/bin/env python3
"""Size budget checks (stdlib only). v1.0 hard constraints.

SKILL.md <= 150 lines; modules (zh and en) <= 400 lines each;
single Template A example <= 120 lines; tutoring_diagnosis <= 200 lines.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAILURES = []


def lines(p):
    with open(p, "rb") as f:
        return f.read().decode("utf-8").count("\n") + 1


def check(name, got, limit):
    ok = got <= limit
    print(("PASS" if ok else "FAIL") + f" {name}: {got} <= {limit}")
    if not ok:
        FAILURES.append(name)


check("SKILL.md", lines(os.path.join(ROOT, "SKILL.md")), 150)

for sub in ("modules", "modules/en"):
    d = os.path.join(ROOT, sub)
    if not os.path.isdir(d):
        continue
    for fn in sorted(os.listdir(d)):
        if fn.endswith(".md"):
            check(f"{sub}/{fn}", lines(os.path.join(d, fn)), 400)

for fn in sorted(os.listdir(os.path.join(ROOT, "examples"))):
    if not fn.endswith(".md"):
        continue
    limit = 200 if fn == "tutoring_diagnosis.md" else 120
    check(f"examples/{fn}", lines(os.path.join(ROOT, "examples", fn)), limit)

if FAILURES:
    print("FAILED:", ", ".join(FAILURES))
    sys.exit(1)
print("ALL PASS")
