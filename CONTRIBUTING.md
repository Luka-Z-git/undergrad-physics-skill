# 贡献指南 (Contributing)

感谢关注 `undergrad-physics-skill`。本技能的核心纪律是**验证门禁**——没有经过 F/L/B/C 验证的答案不会被输出。贡献（尤其是例题）必须遵守同一纪律。

## 收录标准（例题必须全部满足）

新例题提交前逐项自查，任何一项不满足即退回：

1. **模板 A 六节完整且顺序正确**：`题意与图景`、`建模`、`推导`、`验算`、`答案`、`易错点`，每节独立成节。
2. **验算节逐条编号**：以 `①②③④`（可选 `⑤⑥`，本域必做 `⑦J`）开头，每条含可复核的具体检查（表达式/代入值/极限），并以 `PASS`/`FAIL` 纯文本收尾。
3. **答案节显式加粗**：用 Markdown `**...**` 包裹完整结论（含单位与适用条件）；`\boxed{}` 不替代加粗。
4. **附验算摘要行**：`已通过 ①②③④，FAIL 0 项`（不适用项写 `N/A（原因）`）。
5. **无 Overleaf 不兼容字符**：不含 emoji、对勾/叉号等 Unicode 符号；公式用 `$$ ... $$` 块。
6. **物理正确性**：F 量纲、L 极限/特例、B 回代、C 守恒量（适用时）四项实际执行，禁止伪造 PASS。

## 提交前跑一遍结构校验

```bash
python tests/validate_structure.py <你的例题>.md
```

CI 会对 `examples/*.md`（模板 A 例题）自动执行同一校验，PR 必过。

## 提交流程

1. Fork 并新建分支。
2. 新例题放入 `examples/`，命名用 `snake_case.md`（如 `rolling_cylinder.md`）。
3. 若属于本域必做 J 的题型（小振动/算符对易/矩阵线代），验算节须含 `⑦ J` 条目。
4. 若新增题型覆盖现有测试缺口，欢迎同时在 `tests/test_cases.md` 补一条 `TC-XXX-NNN` 断言。
5. 提交 PR，说明题目来源与验证思路。

## 题目措辞

例题请使用自拟措辞的教科书通用问题（双摆、无限深势阱、RC 放电等），**不要整段搬运** Griffiths、Landau 等教材的题面原文。

## 许可

脚本（如 `tests/validate_structure.py`）按 [MIT](LICENSE) 授权；模块、例题与测试的文本按 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授权。详见 [NOTICE](NOTICE)。
