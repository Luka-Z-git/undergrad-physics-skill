# undergrad-physics-skill

[![validate](https://github.com/Luka-Z-git/undergrad-physics-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/Luka-Z-git/undergrad-physics-skill/actions/workflows/validate.yml)
![License](https://img.shields.io/badge/License-MIT%20%2B%20CC%20BY%204.0-orange)
![Examples](https://img.shields.io/badge/examples-20-blue)

> **不是另一个物理解题器，而是 AI 本科物理解答的验证与修复层。**

AI 物理解答最危险的不是明显胡说，而是符号、边界条件、量纲、极限、守恒律或归一化已经出错，答案仍然看起来合理。本 skill 要求 Codex / Claude 在提交最终答案前给出可复核的物理验算证据。

[English](README.en.md) · [60 秒试用](#60-秒试用) · [完整演示](docs/QUICKSTART_DEMO.md) · [工作原理](SKILL.md)

## 四条可靠性原则

- **No evidence, no PASS**：每个 PASS 必须紧邻一项实际执行、可由读者复核的检查。
- **Fail visibly, repair explicitly**：发现矛盾后显式标记 FAIL，定位错误，回到最后一个可靠步骤，修正后重新验算。
- **Tools must be real**：没有真实运行 Python / SymPy，就不声称做过工具验证；工具不可用时明确披露手算降级。
- **Physics-aware verification**：根据题型选择量纲、回代、边界、极限、守恒、归一化等最小充分检查，不为凑数机械套模板。

## 看它怎样抓住一个错误

下面是仓库中的**回退协议演示例题**，用于展示 skill 应有的行为；它不是尚未完成的模型 A/B benchmark。

质量为 $m$ 的物块从粗糙斜面下滑距离 $s$。一个看似熟悉的第一次推导直接套用机械能守恒：

$$
\frac12mv^2=mgs\sin\alpha
\quad\Rightarrow\quad
v_{\rm wrong}=\sqrt{2gs\sin\alpha}.
$$

**检查 → FAIL：** 动摩擦力做功 $W_f=-\mu mg\cos\alpha\,s\neq0$，机械能并不守恒。上式漏掉耗散项，因此不能通过守恒量检查。

**定位与修复：** 回到建模步骤，改用功能原理：

$$
(mg\sin\alpha-\mu mg\cos\alpha)s=\frac12mv^2,
$$

得到

$$
v=\sqrt{2gs(\sin\alpha-\mu\cos\alpha)}.
$$

**重新验算 → PASS：** 用牛顿第二定律得到 $a=g(\sin\alpha-\mu\cos\alpha)$，再由 $v^2=2as$ 得到同一结果；当 $\mu\to0$ 时也还原无摩擦极限。

[查看完整的 FAIL → 定位 → 修复 → 重验过程](examples/backtrack_demonstration.md)

## 60 秒试用

### 1. 安装

Codex（PowerShell）：

```powershell
New-Item -ItemType Directory -Force "$env:USERPROFILE\.codex\skills" | Out-Null
git clone https://github.com/Luka-Z-git/undergrad-physics-skill.git "$env:USERPROFILE\.codex\skills\undergrad-physics-skill"
```

Codex（macOS / Linux）：

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/Luka-Z-git/undergrad-physics-skill.git ~/.codex/skills/undergrad-physics-skill
```

Claude Code 使用相同仓库内容，将目标目录换成 `~/.claude/skills/undergrad-physics-skill/`。Codex 是当前主要验证平台；Claude Code 的文件布局兼容，但尚未完成与 Codex 同等规模的行为回归。

### 2. 提问

复制下面这道诊断题：

> 带动摩擦的斜面下滑，我直接写 $\frac12mv^2=mgs\sin\alpha$。请检查这一步；不要静默替换答案，若检查失败，请指出失败证据、定位错误并在修正后重新验算。

也可以直接求解：

- “用拉格朗日方法推导单摆方程，并检查量纲、回代与小角度极限。”
- “解一维无限深势阱，并验证边界条件与归一化。”
- “检查我的 RC 放电推导，只指出第一处物理错误，不要重做整题。”

### 3. 判断是否生效

你应该看到：

- 具体的代入式、量纲式、极限或守恒关系，而不只是“经验证正确”；
- 每个 PASS 与它的证据放在一起；
- 如果检查失败，明确出现“FAIL → 定位 → 修复 → 重新验算”，而不是悄悄覆盖原答案。

如果只得到普通解答，可在问题中显式写出 skill 名称 `undergrad-physics-skill`，并确认仓库根目录的 `SKILL.md` 位于上述技能目录中。

## 为什么需要它

| 常见失败模式 | 本 skill 的响应 |
|---|---|
| 推导流畅，但符号或量纲错误 | 展示量纲检查或回代原方程的实际计算 |
| 解满足方程，却漏掉初始/边界条件 | 将题目约束纳入验证，而不只检查代数 |
| 最后写“经验证正确”，却没有过程 | 没有可复核证据就不允许标记 PASS |
| 发现矛盾后直接换一个答案 | 保留 FAIL，定位首个错误步骤，修复后重验 |
| 声称用过 Python / SymPy，实际未运行 | 只报告真实工具结果；否则声明手算降级 |
| 学生问“这一步哪里错了”，AI 却重做整题 | 进入学生诊断模式，定位第一处错误及对应概念误区 |

## 当前证据与限制

当前仓库提供的是**可审阅的设计约束、演示例题和确定性测试**：

- 20 个带验证的例题，其中包括边界、退化、学生诊断和失败回溯案例；
- 12 个对抗性行为用例，约束伪 PASS、漏边界、耗散系统误用守恒、虚构工具验证等行为；
- 零依赖的结构门禁、数值回归和体积预算，通过 GitHub Actions 运行；
- 中英文模块与明确的范围外声明。

**模型 A/B benchmark 尚未完成。** 在公开同模型、同题目、同设置的对照结果前，本项目不声称已经测得正确率提升。计划中的 benchmark 将同时报告最终答案、关键推导、未发现矛盾、无证据 PASS，以及输出长度/延迟成本，详见 [v1.0 改进计划](docs/V1_IMPROVEMENT_PLAN.md)。

## 覆盖范围

当前覆盖：

- **理论力学**：牛顿、拉格朗日、哈密顿、小振动、约束、刚体基础与非惯性系；
- **电磁学**：静电、静磁、电路、麦克斯韦方程基础与线性介质边界条件；
- **基础量子力学**：定态薛定谔方程、一维系统、算符与对易、微扰论和自旋 1/2 入门。

当前范围外：热学、统计物理、光学/波动、狭义相对论、研究生方向课、科研工作流、实验课与计算物理编程。遇到范围外题目时，skill 会先声明，而不是假装已经覆盖。

## 工作方式

完整求解走 `解析 → 建模 → 推导 → 验证 → 可选复核 → 作答`；只要结果、概念问答和学生诊断会走更短的专用路径。标准完整解通常使用量纲与回代，再加一项题型相关的独立检查；任何不适用项都必须给出物理理由。

- [SKILL.md](SKILL.md)：入口路由、核心流程与模块索引；
- [验证引擎](modules/verification_engine.md)：检查选择、PASS/FAIL 证据和回退协议；
- [学生诊断](modules/tutoring_mode.md)：检查学生作答而不自动泄漏完整答案；
- [示例索引](examples/INDEX.md)：按题型选择完整例题；
- [贡献指南](CONTRIBUTING.md)：新增例题、模块与测试的标准。

## 版本状态

- [x] v0.1–v0.5.2：三领域、验证引擎、学生诊断、示例、结构校验与双许可；
- [x] v0.7：最小充分验算、入口路由、LaTeX 文档模式、对抗案例与数值回归；
- [x] v0.8：L1–L4 工具门禁与本科领域覆盖路线图——**功能已完成，正式 tag / GitHub Release 待发布**；
- [ ] v1.0：公开可复现的物理解题 A/B benchmark。

## 许可与反馈

脚本采用 MIT OR Apache-2.0；模块、例题与测试文本采用 [CC BY 4.0](LICENSE-CC-BY)，允许在署名并提供许可链接后商用。完整说明见 [NOTICE](NOTICE)。

发现错误时，请提交：

- [错题报告](.github/ISSUE_TEMPLATE/wrong_answer.md)：错误答案、伪 PASS、漏验证或工具声明问题；
- [新例题提案](.github/ISSUE_TEMPLATE/new_example.md)：缺失题型或值得加入回归的真实失败案例。

如果本 skill 帮你发现过一次原本没注意到的物理错误，欢迎点一个 Star，或把那道题提交为新的回归案例。

## 致谢

本项目为独立实现；结构与验证思路受到 `math-skill`、[landau-mode](https://github.com/shaevitz/landau-mode)、[ScienceClaw physics-solver](https://github.com/beita6969/ScienceClaw)、[xiaozhi-skills](https://github.com/qizhitang/xiaozhi-skills)、[Agent Almanac](https://github.com/pjt222/agent-almanac) 与 [Electromagnetism (LobeHub)](https://lobehub.com/skills/tibsfox-gsd-skill-creator-electromagnetism) 启发。上游许可证与隔离说明见 [NOTICE](NOTICE)。
