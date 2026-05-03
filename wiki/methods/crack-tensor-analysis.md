---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "裂纹张量分析 (Crack Tensor Analysis)"
aliases:
  - "crack tensor"
  - "fabric tensor"
sources:
  - "2025-zhai-pfc-fdem-multi-scale-cross-platform-numerical-simulation-of-thermal-crack-network-evol"
---

# 裂纹张量分析 (Crack Tensor Analysis)

## Purpose

从裂纹网络中提取方向分布、密度和长度分布等统计特征，构建二阶裂纹张量以描述方向性和各向异性。
## Aliases

- crack tensor
- fabric tensor
## Workflow

对每个裂纹计算单位法向量，构建二阶裂纹张量，分析特征值和特征向量；可导出 Fisher 或 von Mises 分布参数。
## Inputs

- 裂纹位置和方向
## Outputs

- 裂纹密度方向分布
- 主导方向
- Fisher 密度指数 k
## Assumptions

- 裂纹网络可用二阶张量近似
- 方向分布服从特定分布族
## Strengths

- 适用于连续等效损伤描述
## Limitations

- 可能丢失高阶方向信息
## Related Concepts

- not-confirmed-from-current-pages
## Source Papers

- [2025-zhai-pfc-fdem-multi-scale-cross-platform-numerical-simulation-of-thermal-crack-network-evol](../papers/2025-zhai-pfc-fdem-multi-scale-cross-platform-numerical-simulation-of-thermal-crack-network-evol.md)
