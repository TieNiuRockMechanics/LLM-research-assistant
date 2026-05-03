---
type: "claim"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
claim: "基于图的代理模拟器 (Graph-based emulator) 计算速度可比高保真 DFN 模型快 4 个数量级以上，同时保持可接受的精度，适用于大规模不确定性量化。"
confidence: "high"
claim_status: "supported"
sources:
  -
    paper_id: "2022-viswanathan-from-fluid-flow-to-coupled-processes-in-fractured-rock-recent-advances-and-new"
    locator: "pp. 46-46"
---

# Claim: 基于图的代理模拟器 (Graph-based emulator) 计算速度可比高保真 DFN 模型快 4 个数量级以上，同时保持可接受的精度，适用于大规模不确定性量化。

## Status

supported

## Confidence

high

## Evidence

一项权威综述研究将 DFN 简化为拓扑图，并通过机器学习修正保真度损失，成功实现了速度的指数级提升。
## Condition

需要高保真模型作为训练基础；计算精度取决于 DFN 到图映射的合理性及机器学习校正效果。
## Limitation

图模拟器在强耦合过程（如全 THMC 耦合）中的准确性有待验证，且在训练数据范围外的预测能力不确定。
## Supports

- not-confirmed-from-current-pages
## Contradicts

- not-confirmed-from-current-pages
## Source Papers

- [2022-viswanathan-from-fluid-flow-to-coupled-processes-in-fractured-rock-recent-advances-and-new](../papers/2022-viswanathan-from-fluid-flow-to-coupled-processes-in-fractured-rock-recent-advances-and-new.md) (pp. 46-46)
