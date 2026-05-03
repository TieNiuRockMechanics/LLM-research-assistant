---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "稳态气体渗透率测试 (Steady‑State Gas Permeability)"
aliases:
  - "steady-state method"
  - "Darcy permeability test"
sources:
  - "2020-yang-an-experimental-study-of-effect-of-high-temperature-on-the-permeability-evolution-and"
  - "2021-rong-effect-of-thermal-damage-on-mechanical-and-permeability-properties-of-sandstone"
---

# 稳态气体渗透率测试 (Steady‑State Gas Permeability)

## Purpose

在试样两端施加恒定气压差，记录稳定流量，依据达西定律计算岩石基质或裂隙的气体渗透率。
## Aliases

- steady-state method
- Darcy permeability test
## Workflow

对试件两端施加恒定气压差，测量稳定流量 Q，通过 k = QμL/(AΔP) 计算渗透率（需考虑气体压缩性和滑脱效应修正）。
## Inputs

- 试件截面积 A, 长度 L
- 上下游压力 P1,P2
- 气体粘度 μ
## Outputs

- 渗透率 k (m²)
## Assumptions

- 层流达西流
- 气体等温
- 稳态流动
## Strengths

- 直接测量
- 原理简单
## Limitations

- 低渗岩石测量时间长
- 滑脱效应需校正
## Related Concepts

- permeability-evolution
- gas-slippage
## Source Papers

- [2020-yang-an-experimental-study-of-effect-of-high-temperature-on-the-permeability-evolution-and](../papers/2020-yang-an-experimental-study-of-effect-of-high-temperature-on-the-permeability-evolution-and.md)
- [2021-rong-effect-of-thermal-damage-on-mechanical-and-permeability-properties-of-sandstone](../papers/2021-rong-effect-of-thermal-damage-on-mechanical-and-permeability-properties-of-sandstone.md)
