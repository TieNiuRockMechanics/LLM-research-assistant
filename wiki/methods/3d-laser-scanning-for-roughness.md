---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "三维激光扫描断面粗糙度分析"
aliases:
  - "3D morphology scanning"
  - "3D轮廓仪"
  - "激光断面扫描"
sources:
  - "2025-gu-effects-of-high-temperature-and-thermal-cycles-on-fracture-surface-s-roughness-of-granit"
  - "2025-l-revisiting-scale-effect-on-joint-roughness-coefficient-and-shear-strength-considering-sam"
  - "2023-deng-study-on-fracture-surface-damage-and-fluid-flow-characteristics-of-hot-dry-rock-with-d"
---

# 三维激光扫描断面粗糙度分析

## Purpose

获取岩石断裂面或结构面的高分辨率三维点云，用于计算 JRC、三维粗糙度参数、分形维数及各向异性。
## Aliases

- 3D morphology scanning
- 3D轮廓仪
- 激光断面扫描
## Workflow

激光扫描仪采集表面点云，经去噪、网格化，提取剖面或计算 Z₂、θ*max/(C+1)、高度参数等。
## Inputs

- 岩石断裂面
- 三维激光扫描仪
## Outputs

- 三维点云/网格
- 粗糙度参数（JRC、Z₂、三维参数）
- 分形维数
## Assumptions

- 采样间距足以捕捉粗糙度
- 基准面选取合理
## Strengths

- 高精度、全表面信息
## Limitations

- 深凹处可能遮挡
- 不同扫描仪精度差异
## Related Concepts

- joint-roughness-coefficient
- fractal-dimension
## Source Papers

- [2025-gu-effects-of-high-temperature-and-thermal-cycles-on-fracture-surface-s-roughness-of-granit](../papers/2025-gu-effects-of-high-temperature-and-thermal-cycles-on-fracture-surface-s-roughness-of-granit.md)
- [2025-l-revisiting-scale-effect-on-joint-roughness-coefficient-and-shear-strength-considering-sam](../papers/2025-l-revisiting-scale-effect-on-joint-roughness-coefficient-and-shear-strength-considering-sam.md)
- [2023-deng-study-on-fracture-surface-damage-and-fluid-flow-characteristics-of-hot-dry-rock-with-d](../papers/2023-deng-study-on-fracture-surface-damage-and-fluid-flow-characteristics-of-hot-dry-rock-with-d.md)
