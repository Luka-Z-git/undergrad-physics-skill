# undergrad-physics-skill

面向大学本科物理习题的 Codex/Claude 推导型技能：**分步推导 + 内置验证 + 中文叙述 + Overleaf 可编译输出**。

English version: [README.en.md](README.en.md)

覆盖：理论力学、电磁学、基础量子力学（v0.4 三个领域模块 + 可选学生诊断模式）。

## 特性

- **零外部依赖**：纯 Markdown 技能，复制到技能目录即可用；验证流程由推理本身手算执行。
- **分步推导**：解析 → 建模 → 推导 → 验证 → 复核（可选）→ 作答，每步可独立核验。
- **内置验证引擎**：8 种验证方法（F 量纲 / D 定义域 / B 回代 / C 守恒量 / L 极限特例 / E 数值抽样 / I 独立方法 / J 一致性）。标准解答必查：量纲、极限/特例、回代、守恒量（适用时）；验证失败自动回溯修正，无法验证时如实声明。
- **中文 + LaTeX**：中文解题叙述，公式用 `$$ ... $$` 块，输出可完整粘贴进 Overleaf 编译；无 emoji、无 Overleaf 不兼容字符。
- **可选联动**：Math.Skill（线性代数）与 Python/SymPy/SciPy（符号/数值复核）均为可选增强；未安装时分别降级为 J 一致性手算与纯手算。
- **可选独立复核**：作答前可按 `modules/review_engine.md` 做病理过滤与白纸重推（用户要求或高置信度场景）。
- **可选学生诊断模式**：检查学生作答时直接指出缺项与错误，定位概念误区并出确认题，不展开完整解答（非主体功能）。

## 安装

- **Codex**：将本仓库内容放入 `~/.codex/skills/undergrad-physics-skill/`。
- **Claude Code**：放入 `~/.claude/skills/undergrad-physics-skill/`。

## 触发

直接提问物理习题即可自动触发，例如：

- "用拉格朗日方法求双摆的运动微分方程"
- "推导带电粒子在均匀磁场中的回旋运动"
- "解一维无限深势阱的定态薛定谔方程并验证归一化"
- "帮我看看我写的这步对不对"（进入学生诊断模式）

矩阵、特征值、矩阵幂、递推等线性代数子问题可联动 Math.Skill 处理（可选；无 Math.Skill 时按 J 一致性手算）。

## 范围

**覆盖**：理论力学（牛顿/拉格朗日/哈密顿/小振动/非惯性系）、电磁学（静电场/静磁场/电路/矢量分析）、基础量子力学（定态薛定谔/算符/对易/一维系统）。

**不覆盖**（Out of Scope）：本科其他方向（热学、光学、统计物理、狭义相对论等）、研究生方向课（量子场论、广义相对论、群论、多体理论等）、科研工作流（论文复现、arXiv 阅读、多智能体研究流水线）、纯实验课与计算物理编程任务。

## 验证引擎（摘要）

| 代号 | 方法 | 说明 |
|---|---|---|
| F | 量纲检查 | 必做：推导全程携带单位，最终量纲与目标物理量一致 |
| D | 定义域/参数域 | 参数范围、分母非零、频率平方非负等 |
| B | 回代 | 解代回 EOM / E-L / $H\psi=E\psi$ 验证恒等 |
| C | 守恒量 | 能量/动量/角动量守恒（无耗散、对称性成立时） |
| L | 极限/特例 | $\omega\to0$、$\hbar\to0$、$\theta\to0$ 应还原已知结果 |
| E | 数值抽样 | 代入具体数值比较等式两端并核对数量级 |
| I | 独立方法 | 牛顿 vs 拉格朗日、能量法 vs 力法 |
| J | 一致性 | 矩阵迹/行列式/特征值回代、归一化、对易关系 |

硬性规则：标准解答必查 F 量纲、L 极限/特例、B 回代、C 守恒量（适用时）；任何 FAIL 回溯修正；禁止伪造验证通过；两次修正仍失败则换独立方法，仍失败则明确声明无法给出已验证答案。

## 目录结构

```
undergrad-physics-skill/
├── SKILL.md                      # 主干：定位、工作流、验证摘要、模块索引
├── modules/
│   ├── mechanics.md              # 理论力学领域协议（v0.1）
│   ├── electromagnetism.md       # 电磁学领域协议（v0.2）
│   ├── quantum_basics.md         # 基础量子力学领域协议（v0.3）
│   ├── verification_engine.md    # 8 种验证方法、题型选择表、回溯协议
│   ├── review_engine.md          # 可选独立复核：病理过滤与白纸重推
│   ├── tutoring_mode.md          # 可选学生诊断：检查作答、定位错误与概念误区
│   ├── output_templates.md       # 输出模板与格式硬规则
│   ├── error_prevention.md       # 错误预防与交卷前检查清单
│   └── computation.md            # 可选 SymPy/SciPy 复核配方
├── examples/                     # 完整带验证的例题
├── tests/                        # 用例断言（TC-XXX-NNN）
├── NOTICE                        # 原创声明与借鉴来源
└── LICENSE                       # MIT
```

## 开发状态

- [x] v0.1：理论力学（SKILL.md 主干 + mechanics 模块 + 验证引擎 + 输出模板 + 错误预防 + 例题 + 测试）
- [x] v0.2：电磁学模块（静电场/静磁场/电路暂态/麦克斯韦基础 + 例题 + 测试）
- [x] v0.3：基础量子力学模块（定态薛定谔/谐振子/算符/角动量/氢原子入门 + 例题 + 测试）
- [x] v0.4：可选学生诊断模式（检查作答、直接定位错误与概念误区，非主体）
- [ ] v1.0：README 双语完善、正式发布

## 许可

MIT License。参见 [LICENSE](LICENSE)。

## 原创声明

本项目由 AI 辅助编写与审查；正文、示例与测试均为原创实现，只借鉴参考项目的方法与结构，未复制其原文或代码，借鉴来源见 Credits。若未来引入任何第三方代码片段，将保留其原始版权声明。

## 致谢 (Credits)

本技能的结构与验证方法受以下开源项目启发（均为独立实现，未复制原文）：

- [Math.Skill](https://github.com/Wholiver/Math.Skill) — 数学推理技能架构、验证引擎思路
- [landau-mode](https://github.com/shaevitz/landau-mode) — 病理过滤与白纸重推的方法思路（独立实现，未复制原文）
- [ScienceClaw physics-solver](https://github.com/beita6969/ScienceClaw) — 符号计算配方思路
- [xiaozhi-skills](https://github.com/qizhitang/xiaozhi-skills) — 中文物理解题流程的图景建模思路
- [Agent Almanac](https://github.com/pjt222/agent-almanac) — 电磁感应/磁场分析的分步协议思路
- [Electromagnetism (LobeHub)](https://lobehub.com/skills/tibsfox-gsd-skill-creator-electromagnetism) — 电磁学公式与陷阱对照思路
