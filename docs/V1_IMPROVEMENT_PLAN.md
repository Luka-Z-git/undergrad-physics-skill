# V1.0 改进计划

状态：`v0.8.0` 功能已完成，正式 tag / GitHub Release 待发布；本文档是 v1.0 的路线与验收依据。

## 目标

证明“使用本 skill 后模型解题能力提升”，而不是只证明结构严谨。v1.0 的完成判据：物理解题 benchmark 报告发布、README 加入 A/B 对比表、覆盖路线图明确。

## 已完成（v0.8.0）

- L1–L4 工具门禁：简单题禁止工具；中等题允许一次符号复核；复杂题环境可用时自动升级；L4 独立复核 P1–P5
- 覆盖路线图：热学、统计物理、光学/波动、狭义相对论
- TC-ADV-012：复杂题自动升级工具门禁对抗用例
- 版本号升至 0.8.0，中英文模块与 CHANGELOG 同步

## 待办 1：物理解题能力 Benchmark（最高优先级）

### 规模与题库

- 起步 100 题：力学 35 / 电磁 35 / 量子 30（当前覆盖域内）
- 难度分布：简单 40 / 中等 40 / 复杂 20
- 每题包含：题目、标准答案、关键推导步骤、评分规则、可复现的数值/极限检查
- 来源：公开教材例题或自编，逐题标注来源；避免直接复制受版权限制的整题

### A/B 协议

- 同一模型、同一 prompt、同一 temperature（建议 0）
- 每道题跑两次：不用 skill vs 用 skill
- 每种组合至少跑 1 次；预算允许时跑 3 次取中位数
- 统计指标：最终答案正确率、关键推导步骤正确率、hallucination rate（伪造 PASS/声称工具验证）、token、延迟

### 评分

- 结构分：自动复用现有 `validate_structure.py` 等测试
- 物理正确性：LLM-as-judge + 人工抽检 20–30 题校准
- Hallucination 专查：PASS 无具体检查、声称已用 SymPy/Python 但未执行
- 数值题给容差；符号题给代数等价性判据

### 输出物

- `benchmarks/problem_bank/`：题目 JSON/MD + 答案 + rubric
- `benchmarks/results/`：每次运行的原始结果与汇总表
- `benchmarks/README.md`：运行方式与复现说明
- README 增加 A/B 对比表：no-skill vs skill

### 完成判据

- 100 题全部跑完，人工抽检通过
- 报告公开四项数字：答案正确率、推导正确率、hallucination rate、token/延迟
- 至少一个领域显示提升；任何领域不得明显倒退
- 原始数据与评分脚本可复现

## 待办 2：覆盖扩展（benchmark 之后）

顺序建议：热学 → 统计物理 → 光学/波动 → 狭义相对论。

每个领域按现有流程补齐：module + examples + tests + adversarial cases + 英文同步。

## 待办 3：v1.0 发布

- 版本号升至 1.0.0（`SKILL.md` / `SKILL.en.md` / `tests/test_cases.md` / README）
- CHANGELOG 标记 `v1.0.0` released
- 打 tag 并创建 GitHub Release
- README 的 v1.0 checkbox 勾选

## 不做的边界

- 不把 benchmark 混入 CI（成本高、依赖外部模型与评分）
- 不承诺“用了就一定对”，报告如实呈现
- 不把研究生课程纳入本科范围
