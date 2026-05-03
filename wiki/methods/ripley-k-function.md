---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "基于 Ripley K 函数的空间聚集性分析"
aliases:
  - "Ripley K"
  - "空间点模式分析"
sources:
  - "2025-zhai-pfc-fdem-multi-scale-cross-platform-numerical-simulation-of-thermal-crack-network-evol"
---

# 基于 Ripley K 函数的空间聚集性分析

## Purpose

评估裂纹中心点在空间上的聚集或分散程度，探测多尺度聚集模式。
## Aliases

- Ripley K
- 空间点模式分析
## Workflow

计算不同距离环内点数量的期望值，与泊松过程理论值比较，对距离做包络测试。
## Inputs

- 裂纹中点坐标
## Outputs

- K(r) 曲线
- 空间聚集尺度
## Assumptions

- 研究区为规则窗口
- 边界效应需校正
## Strengths

- 可探测多尺度聚集模式
## Limitations

- 对窗口形状敏感
## Related Concepts

- not-confirmed-from-current-pages
## Source Papers

- [2025-zhai-pfc-fdem-multi-scale-cross-platform-numerical-simulation-of-thermal-crack-network-evol](../papers/2025-zhai-pfc-fdem-multi-scale-cross-platform-numerical-simulation-of-thermal-crack-network-evol.md)
