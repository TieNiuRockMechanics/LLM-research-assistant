---
type: "claim"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
claim: "二维离散裂隙网络（DFN）流动从线性（达西）向非线性（Forchheimer）转变所需的临界水力梯度 Jc，最主要的控制因子是机械隙宽，其次才是裂隙交点数 (Ni) 和表面粗糙度 (JRC)。"
confidence: "high"
claim_status: "supported"
sources:
  -
    paper_id: "2016-liu-critical-hydraulic-gradient-for-nonlinear-flow-through-rock-fracture-networks-the-roles"
    locator: "pp. 7-8"
---

# Claim: 二维离散裂隙网络（DFN）流动从线性（达西）向非线性（Forchheimer）转变所需的临界水力梯度 Jc，最主要的控制因子是机械隙宽，其次才是裂隙交点数 (Ni) 和表面粗糙度 (JRC)。

## Status

supported

## Confidence

high

## Evidence

参数化数值模拟表明，隙宽从 0.5 mm 变为 10 mm，Jc 变化跨越约 5 个数量级；而 JRC 从 0 增到 20 或 Ni 从 1 增到 12 只引起数倍变化。
## Condition

二维 DFN，低 Re (<~100)，满足层流但惯性项不可忽略的“弱惯性流”区。
## Limitation

基于固定边界二维模型，所有交叉角均为 60°；对真实三维网络需校正。
## Supports

- not-confirmed-from-current-pages
## Contradicts

- not-confirmed-from-current-pages
## Source Papers

- [2016-liu-critical-hydraulic-gradient-for-nonlinear-flow-through-rock-fracture-networks-the-roles](../papers/2016-liu-critical-hydraulic-gradient-for-nonlinear-flow-through-rock-fracture-networks-the-roles.md) (pp. 7-8)
