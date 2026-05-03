---
type: "claim"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
claim: "通用裂隙模型（UFM）预测，在密集裂隙网络中，长度分布自然趋于自相似且满足 a=D+1，密度项接近常数，网络处于临界逾渗状态。"
confidence: "high"
claim_status: "supported"
sources:
  -
    paper_id: "2010-davy-a-likely-universal-model-of-fracture-scaling-and-its-consequence-for-crustal-hydromech"
    locator: "pp. 2-3, 4-5"
---

# Claim: 通用裂隙模型（UFM）预测，在密集裂隙网络中，长度分布自然趋于自相似且满足 a=D+1，密度项接近常数，网络处于临界逾渗状态。

## Status

supported

## Confidence

high

## Evidence

推导得 n(l,L)=Dγ^D L^D l^{-(D+1)}，用 Hornelen、San Andreas 等数据验证。
## Condition

裂隙生长受更大裂隙的交切抑制，无外部力学长度尺度控制。
## Limitation

基于统计规则，非完全力学模型；用于断层时拟合区间很窄。
## Supports

- hornelen-joint-first-order-model
## Contradicts

- scaling-law-x-equals-a-minus-1-over-D
## Source Papers

- [2010-davy-a-likely-universal-model-of-fracture-scaling-and-its-consequence-for-crustal-hydromech](../papers/2010-davy-a-likely-universal-model-of-fracture-scaling-and-its-consequence-for-crustal-hydromech.md) (pp. 2-3, 4-5)
