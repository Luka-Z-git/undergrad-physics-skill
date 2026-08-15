# 快速开始演示：RC 放电的六步流程

本文件用一道简单题展示 `undergrad-physics-skill` 的完整工作流，便于新用户快速理解技能会如何作答。

## 1. 解析（Parse）

用户输入："电容 C 初始电压 V0，t=0 经电阻 R 放电，求 V(t)、I(t)、tau。"

解析结果：对象为 RC 单回路；约束为集总线性电路、无外源；电流 I 从正极板经 R 流向负极板；单位制 SI；已知 V0、R、C，待求 V(t)、I(t)、tau。

## 2. 建模（Model）

选 KVL + 元件伏安关系：I = -C dV/dt，V = IR，得 dV/dt + V/(RC) = 0。

## 3. 推导（Derive）

分离变量积分并用 V(0)=V0 定常数：

$$
V(t)=V_0e^{-t/(RC)},\qquad I(t)=\frac{V_0}{R}e^{-t/(RC)},\qquad \tau=RC
$$

每 3-5 步做一次 F 量纲或 E 数值抽样并内联记录。

## 4. 验证（Verify）

- ①F 量纲：tau=RC 量纲为 s，V(t) 量纲为 V。PASS。
- ②L 极限：t 趋于 0 得 V0、V0/R；t 趋于无穷得 0。PASS。
- ③B 回代：dV/dt 代回 ODE 恒等。PASS。
- ④C 守恒：电容能量减少率等于电阻耗散功率。PASS。

## 5. 复核（Review，可选）

高置信度场景可再跑 `modules/review_engine.md` 的白纸重推；本例不需要。

## 6. 作答（Answer）

按模板 A 六节输出，答案加粗并带一行验算摘要：`已通过 ①②③④，FAIL 0 项`。

完整示范见 [examples/rc_discharge.md](../examples/rc_discharge.md)。
