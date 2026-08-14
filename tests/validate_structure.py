#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""模板 A 结构门禁最小校验器（零依赖，stdlib only）。

对一份待发布的解答输出做结构断言，对应 modules/output_templates.md 的
"模板 A 结构门禁"与"格式硬规则"：

  1. 六节标题齐全且顺序正确：题意与图景、建模、推导、验算、答案、易错点
  2. 验算节每条以 ①②③④（可选 ⑤⑥、本域必做 ⑦J）开头，无混合散文
  3. 答案节含 **...** 显式加粗
  4. 含一行验算摘要：已通过 ①②③④，FAIL 0 项（允许 N/A 与附加明细）
  5. 无 emoji / 对勾叉号等 Overleaf 不兼容 Unicode 符号
  6. $$ 块配平

用法：
  python validate_structure.py <answer.md> [more.md ...]

退出码：0 = 全部通过；1 = 存在 FAIL。
"""
import re
import sys

REQUIRED_SECTIONS = ["题意与图景", "建模", "推导", "验算", "答案", "易错点"]

# Overleaf 不兼容符号（对勾/叉号/常见 emoji 区段）
BANNED_CHARS = "\u2713\u2714\u2717\u2718\u274c\u2b55\U0001f7e2\U0001f7e1\U0001f534"  # check/cross/status symbols
EMOJI_RE = re.compile(
    "[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF]"
)

NUM_MARKS = "①②③④⑤⑥⑦"


def extract_section(text, name, following):
    """取某一节正文（从 `## name` 到下一个节标题）。"""
    m = re.search(r"^#{1,4}\s*" + re.escape(name) + r"\s*$", text, re.M)
    if not m:
        return None
    start = m.end()
    nxt = re.search(r"^#{1,4}\s", text[start:], re.M)
    return text[start: start + nxt.start()] if nxt else text[start:]


def check_file(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    fails = []

    # 1. 六节标题与顺序
    pos = []
    for name in REQUIRED_SECTIONS:
        m = re.search(r"^#{1,4}\s*" + re.escape(name) + r"\s*$", text, re.M)
        pos.append(m.start() if m else None)
    missing = [n for n, p in zip(REQUIRED_SECTIONS, pos) if p is None]
    if missing:
        fails.append("缺节标题: " + ", ".join(missing))
    elif pos != sorted(pos):
        fails.append("节标题顺序错误，应为: " + " → ".join(REQUIRED_SECTIONS))

    # 2. 验算节逐条编号
    ver = extract_section(text, "验算", REQUIRED_SECTIONS)
    if ver is not None:
        for mark, label in zip("①②③④", ["F", "L", "B", "C"]):
            if mark not in ver:
                fails.append(f"验算节缺 {mark}（{label}）")
        bad_lines = [
            ln for ln in ver.splitlines()
            if ln.strip()
            and not ln.lstrip().startswith(tuple(NUM_MARKS))
            and not ln.lstrip().startswith(("#", "-", "|", "$", "验算摘要"))
            and "已通过" not in ln
        ]
        if bad_lines:
            fails.append(f"验算节存在无编号叙述行: {bad_lines[0].strip()[:40]}...")

    # 3. 答案节显式加粗
    ans = extract_section(text, "答案", REQUIRED_SECTIONS)
    if ans is not None and not re.search(r"\*\*.+?\*\*", ans, re.S):
        fails.append("答案节缺 **...** 显式加粗")

    # 4. 验算摘要行
    if "已通过" not in text or "FAIL 0 项" not in text:
        fails.append("缺验算摘要行（已通过 ①②③④，FAIL 0 项）")

    # 5. Overleaf 不兼容字符
    bad = [c for c in BANNED_CHARS if c in text]
    if bad:
        fails.append("含 Overleaf 不兼容符号: " + " ".join(bad))
    if EMOJI_RE.search(text):
        fails.append("含 emoji")

    # 6. $$ 配平
    if text.count("$$") % 2 != 0:
        fails.append("$$ 块未配平")

    return fails


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1
    ok = True
    for path in argv[1:]:
        fails = check_file(path)
        if fails:
            ok = False
            print(f"[FAIL] {path}")
            for f_ in fails:
                print(f"  - {f_}")
        else:
            print(f"[PASS] {path}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
