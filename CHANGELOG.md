# Changelog

本项目提交信息遵循 [Conventional Commits](https://www.conventionalcommits.org/) 风格（feat/fix/docs/refactor/chore），本文件由人工维护。

## v0.7.0 (unreleased)

### Added

- 例题扩至 20 道：法拉第、介质边界、科里奥利、4 道边界/退化案例（不稳定平衡、零频模式、散射态归一化、回溯修正）
- 学生诊断示例扩展至 7 个场景（新增 E-L 符号、量纲、归一化诊断）
- 确定性数值回归 `tests/numeric_regression.py`，接入 CI
- 体积预算 `tests/size_budget.py`，接入 CI
- 快速开始演示 `docs/QUICKSTART_DEMO.md`
- README 反馈闭环（错题/新例题 Issue 模板）
- 量子模块：非简并微扰论与自旋 1/2 入门
- 电磁模块：宏观 D/H 形式与线性介质范围声明
- CHANGELOG 与 PR 模板
- 顶层入口路由（SKILL.md）与示例索引 `examples/INDEX.md`
- LaTeX 文档模式
- 对抗行为案例 10 个与抽查记录

### Changed

- 验算政策收敛为最小充分验算集：通常 F + B + 一项独立检查，领域必做 J；验证引擎为唯一来源
- 英文模块完成母语化润色，并与中文模块同步验算策略、示例索引与 LaTeX 文档模式
- 许可文档与 NOTICE/README 对齐（MIT + CC BY 4.0），记录许可决策
- `error_prevention.md` 增加跨域陷阱映射表，sanity check 绑定 F/E
- CONTRIBUTING 细化：例题 PR 模板、风格指南、新增模块流程、TC 命名规范
- README、CONTRIBUTING 与测试说明同步新的验算门禁
- 脚本许可双许可为 MIT OR Apache-2.0；新增 LICENSE-APACHE、NOTICE 专利声明与贡献者 DCO
- 默认简洁路径：按模板最小化执行范围，简单题收紧输出预算；符号复核默认关闭（仅用户要求时一次），默认验算 3 项、最多 5 项；LaTeX 模式默认不写文件、简单题 ≤60 行；未获要求禁止调用/声称 SymPy；复核默认 P1-P5 摘要、白纸重推默认不做；新增输出止损（禁止空答）与禁止自动数值积分

## v0.5.2 - 2026-08-14

- 一致性修复：⑦J 编号、步骤引用、法拉第指针、范围对齐
- 新增 5 个缺域例题（刚体、非惯性系、平面波、氢原子、势垒）
- 结构校验器 `tests/validate_structure.py` 与 GitHub Actions CI
- 英文模块完整同步，NOTICE 上游许可证核查与双许可声明
- 新增 CONTRIBUTING 与 Issue 模板

## v0.5.1

- 瘦身优化：跨域陷阱表去重、README/test_cases 精简、computation 配方合并

## v0.5.0

- 范围边界明确化：介质与量子非相对论近似声明
- F 量纲检查对纯数学中间步骤的适用性微调
- 难度分级与输出粒度自适应
- 耦合振子示例与诊断确认题质量校准
- 回溯协议成本止损机制

## v0.4.0

- 可选学生诊断模式（模板 E），不展开完整答案

## v0.3.0 / v0.2.0 / v0.1.0

- v0.3：基础量子力学模块（定态薛定谔/谐振子/算符/对易/氢原子入门）
- v0.2：电磁学模块（静电场/静磁场/电路/麦克斯韦基础）
- v0.1：理论力学模块、验证引擎、输出模板、错误预防、示例与测试
