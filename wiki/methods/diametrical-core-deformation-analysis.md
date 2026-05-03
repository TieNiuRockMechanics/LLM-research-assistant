---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "岩心直径变形分析"
aliases:
  - "DCDA"
  - "diametrical core deformation measurement"
sources:
  - "2022-li-determination-of-mining-induced-stresses-using-diametral-rock-core-deformations"
  - "2021-ziegler-evaluation-of-the-diametrical-core-deformation-and-discing-analyses-for-in-situ-str"
  - "2025-meng-evaluation-of-the-diametrical-core-deformation-analysis-dcda-and-fracture-surface-morp"
---

# 岩心直径变形分析

## Purpose

通过测量钻探岩心卸荷后的非弹性变形，反演深部原位差应力大小与方向。
## Aliases

- DCDA
- diametrical core deformation measurement
## Workflow

使用高分辨率激光扫描仪测量岩心圆柱面的直径变化，获取最大/最小直径及其方向；结合岩石弹性模量和泊松比，利用线弹性应力释放模型计算垂直于岩心轴平面上的差应力。
## Inputs

- 定向或非定向钻探岩心
- 高精度激光测微仪
- 岩石弹性模量E和泊松比ν
## Outputs

- 最大/最小直径差Δd
- 差应力大小σH-σh
- 主应力方向（若岩心已定向）
## Assumptions

- 岩石为均质、各向同性、完全线弹性
- 岩心变形完全由应力释放引起，无塑性变形或裂隙影响
## Strengths

- 无损岩心测试
- 可直接利用现有取芯
## Limitations

- 不适用于严重破裂或强各向异性岩石
- 仪器精度需求高（10⁻⁴ mm级）
- 仅能求取二维差应力
## Related Concepts

- in-situ-stress
- stress-release-method
## Source Papers

- [2022-li-determination-of-mining-induced-stresses-using-diametral-rock-core-deformations](../papers/2022-li-determination-of-mining-induced-stresses-using-diametral-rock-core-deformations.md)
- [2021-ziegler-evaluation-of-the-diametrical-core-deformation-and-discing-analyses-for-in-situ-str](../papers/2021-ziegler-evaluation-of-the-diametrical-core-deformation-and-discing-analyses-for-in-situ-str.md)
- [2025-meng-evaluation-of-the-diametrical-core-deformation-analysis-dcda-and-fracture-surface-morp](../papers/2025-meng-evaluation-of-the-diametrical-core-deformation-analysis-dcda-and-fracture-surface-morp.md)
