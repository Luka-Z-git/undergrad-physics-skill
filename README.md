# undergrad-physics-skill

![License](https://img.shields.io/badge/License-MIT%20%2B%20CC%20BY%204.0-orange)
![Examples](https://img.shields.io/badge/examples-20-blue)
![Tests](https://img.shields.io/badge/tests-18-blue)

面向大学本科物理习题的 Codex/Claude 推导型技能：**分步推导 + 内置验证 + 中文叙述 + LaTeX-ready 输出**。

English version: [README.en.md](README.en.md)

**快速上手**：`SKILL.md` 包含完整的定位、工作流、验证引擎摘要与模块索引。快速开始演示见 [docs/QUICKSTART_DEMO.md](docs/QUICKSTART_DEMO.md)。本文档仅补充安装、触发方式与项目元信息。

## 安装

- **Codex**：将本仓库内容放入 `~/.codex/skills/undergrad-physics-skill/`。
- **Claude Code**：放入 `~/.claude/skills/undergrad-physics-skill/`。
- **WorkBuddy**：放入技能目录或工作区 `.workbuddy/skills/`。

## 触发

直接提问物理习题即可自动触发：

- "用拉格朗日方法求双摆的运动微分方程"
- "推导带电粒子在均匀磁场中的回旋运动"
- "解一维无限深势阱的定态薛定谔方程并验证归一化"
- "帮我看看我写的这步对不对"（进入学生诊断模式）

矩阵/特征值子问题可联动 `math-skill`（可选；无则按 J 一致性手算）。

## 目录结构

```
undergrad-physics-skill/
├── SKILL.md                      # 主干：定位、工作流、验证摘要、模块索引
├── SKILL.en.md                   # English trunk
├── docs/                        # 快速开始演示
├── modules/
│   ├── mechanics.md              # 理论力学领域协议
│   ├── electromagnetism.md       # 电磁学领域协议
│   ├── quantum_basics.md         # 基础量子力学领域协议
│   ├── verification_engine.md    # 8 种验证方法 + 回溯协议（含 v0.5 成本止损）
│   ├── review_engine.md          # 可选独立复核
│   ├── tutoring_mode.md          # 可选学生诊断 + 确认题质量标准
│   ├── output_templates.md       # 输出模板 + v0.5 难度分级
│   ├── error_prevention.md       # 跨域错误预防清单
│   ├── computation.md            # 可选 SymPy/SciPy 复核配方
│   └── en/                       # 英文同步模块（发布时生成物，随中文版更新）
├── examples/                     # 完整带验证的例题（20 个）
├── tests/                        # 用例断言（TC-XXX-NNN，18 个）+ 结构校验器
├── .github/                      # CI（结构门禁）+ issue 模板
├── CONTRIBUTING.md               # 贡献与例题收录标准
├── CHANGELOG.md                  # 版本变更记录（Conventional Commits）
├── NOTICE                        # 许可与专利声明
├── LICENSE                       # MIT（脚本可选）
├── LICENSE-APACHE                # Apache-2.0（脚本可选，含专利条款）
└── LICENSE-CC-BY                 # CC BY 4.0（文本）
```

## 开发状态

- [x] v0.1–v0.3：三领域模块 + 验证引擎 + 输出模板 + 例题 + 测试
- [x] v0.4：学生诊断模式
- [x] v0.5：生产级加固——范围边界、难度分级、成本止损、确认题标准
- [x] v0.5.1：瘦身优化——跨域陷阱表去重、README/test_cases 精简
- [x] v0.5.2：评审修复——⑦J 编号、步骤引用、法拉第指针、范围对齐、结构校验器、版权核实、5 个缺域例题、CI、英文模块同步、双许可
- [x] v0.7：最小充分验算策略、顶层路由、LaTeX 文档模式、示例索引、对抗案例与抽查记录；含 v0.6 P0/P1 全部内容
- [ ] v1.0：正式发布

## 许可

双许可：脚本（如 `tests/validate_structure.py`）为 MIT OR Apache-2.0（见 [LICENSE](LICENSE) 与 [LICENSE-APACHE](LICENSE-APACHE)）；模块、例题与测试的文本为 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)（见 [LICENSE-CC-BY](LICENSE-CC-BY)）。详见 [NOTICE](NOTICE)。

商用说明：CC BY 4.0 允许商用，只需署名并提供许可链接；本项目选择 CC BY 4.0 以最大化传播。

许可与专利：本项目公开即构成 prior art；脚本按 Apache-2.0 使用时附带标准专利授权与终止条款（见 LICENSE-APACHE）；作者不主张本仓库方法的专利。

**如何署名**：复用或改编文本时使用：`文本内容：undergrad-physics-skill contributors，采用 CC BY 4.0 许可（https://creativecommons.org/licenses/by/4.0/）。如已修改，请注明修改。`

## 发现问题？

发现解题错误、验证被跳过或格式问题，请提交 Issue：

- [错题报告](.github/ISSUE_TEMPLATE/wrong_answer.md)：报告错误、伪造 PASS 或遗漏验证
- [新例题提案](.github/ISSUE_TEMPLATE/new_example.md)：提议补充缺失题型

提交前尽量附上题目、技能输出与你自己的推算，便于定位。

## 致谢 (Credits)

本技能的结构与验证方法受以下开源项目启发（均为独立实现，未复制原文；上游许可证已于 2026-08-14 核实，详见 [NOTICE](NOTICE)）：

- `math-skill` — 可选的数学推理协作技能；不可用时按 J 一致性手算
- [landau-mode](https://github.com/shaevitz/landau-mode) — 病理过滤与白纸重推的方法思路
- [ScienceClaw physics-solver](https://github.com/beita6969/ScienceClaw) — 符号计算配方思路
- [xiaozhi-skills](https://github.com/qizhitang/xiaozhi-skills) — 中文物理解题流程的图景建模思路
- [Agent Almanac](https://github.com/pjt222/agent-almanac) — 电磁感应与磁场分析的分步协议
- [Electromagnetism (LobeHub)](https://lobehub.com/skills/tibsfox-gsd-skill-creator-electromagnetism) — 公式与陷阱参考结构（上游为 BSL 1.1，仅参考结构，未并入任何文字）
