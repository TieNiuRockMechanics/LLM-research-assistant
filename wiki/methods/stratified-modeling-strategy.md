---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "分层建模策略 (Stratified Modeling Strategy)"
aliases:
  - "stratified modeling"
  - "分层建模"
sources:
  - "2025-zhang-intelligent-construction-method-for-rock-slope-fracture-network-model-based-on-discre"
---

# 分层建模策略 (Stratified Modeling Strategy)

## Purpose

按岩性单元（或均质区）分别建立和反演裂缝模型以捕捉空间非均质性。
## Aliases

- stratified modeling
- 分层建模
## Workflow

划分岩性单元；每单元独立生成合成数据并训练专属神经网络；选择每单元最优模型参数；拼合总 DFN。
## Inputs

- 岩性边界
- 各单元裂缝统计
## Outputs

- 分单元 DFN 参数
## Assumptions

- 岩性界面为裂缝特征突变带
- 各层独立
## Strengths

- 显著降低反演误差（>18%）
## Limitations

- 层内均匀假设
- 需要足够合成数据
## Related Concepts

- not-confirmed-from-current-pages
## Source Papers

- [2025-zhang-intelligent-construction-method-for-rock-slope-fracture-network-model-based-on-discre](../papers/2025-zhang-intelligent-construction-method-for-rock-slope-fracture-network-model-based-on-discre.md)
