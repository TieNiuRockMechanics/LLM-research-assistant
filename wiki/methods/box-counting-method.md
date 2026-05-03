---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "盒计数法 (Box‑Counting)"
aliases:
  - "box-counting"
  - "capacity dimension"
  - "Db"
sources:
  - "1990-letters-to-nature-nature-letters-to-nature"
  - "1995-watanabe-fractal-geometry-characterization-of-geothermal-reservoir-fracture-networks"
  - "2001-bonnet-scaling-of-fracture-systems-in-geological-media"
  - "2013-kruhl-fractal-geometry-techniques-in-the-quantification-of-complex-rock-structures-a-specia"
  - "2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture"
  - "2015-liu-a-fractal-model-for-characterizing-fluid-flow-in-fractured-rock-masses-based-on-randoml"
  - "2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi"
  - "2025-zhao-characterizing-the-intrinsic-complexity-of-natural-fracture-networks-a-novel-fractal-b"
---

# 盒计数法 (Box‑Counting)

## Purpose

计算物体或点集的空间分形维数。
## Aliases

- box-counting
- capacity dimension
- Db
## Workflow

用不同尺度 ε 的网格覆盖目标，统计包含目标的盒子数 N(ε)，拟合 log(N(ε)) vs. log(1/ε) 的斜率得到分形维数 D0。
## Inputs

- 裂隙迹线图或点集
- 盒子尺寸序列
## Outputs

- 容量维数 D0
## Assumptions

- 目标在统计上自相似
- 盒子尺寸跨越足够的无标度区
## Strengths

- 数学简单，应用广泛
## Limitations

- 对有限尺寸效应和起始位置敏感
- 无法完全区分随机模式与分形模式
- 仅测部分维数
## Related Concepts

- fractal-dimension
## Source Papers

- [1990-letters-to-nature-nature-letters-to-nature](../papers/1990-letters-to-nature-nature-letters-to-nature.md)
- [1995-watanabe-fractal-geometry-characterization-of-geothermal-reservoir-fracture-networks](../papers/1995-watanabe-fractal-geometry-characterization-of-geothermal-reservoir-fracture-networks.md)
- [2001-bonnet-scaling-of-fracture-systems-in-geological-media](../papers/2001-bonnet-scaling-of-fracture-systems-in-geological-media.md)
- [2013-kruhl-fractal-geometry-techniques-in-the-quantification-of-complex-rock-structures-a-specia](../papers/2013-kruhl-fractal-geometry-techniques-in-the-quantification-of-complex-rock-structures-a-specia.md)
- [2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture](../papers/2015-li-relationship-between-joint-roughness-coefficient-and-fractal-dimension-of-rock-fracture.md)
- [2015-liu-a-fractal-model-for-characterizing-fluid-flow-in-fractured-rock-masses-based-on-randoml](../papers/2015-liu-a-fractal-model-for-characterizing-fluid-flow-in-fractured-rock-masses-based-on-randoml.md)
- [2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi](../papers/2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi.md)
- [2025-zhao-characterizing-the-intrinsic-complexity-of-natural-fracture-networks-a-novel-fractal-b](../papers/2025-zhao-characterizing-the-intrinsic-complexity-of-natural-fracture-networks-a-novel-fractal-b.md)
