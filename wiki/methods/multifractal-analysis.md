---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "多重分形分析 (Multifractal Analysis)"
aliases:
sources:
  - "2013-kruhl-fractal-geometry-techniques-in-the-quantification-of-complex-rock-structures-a-specia"
---

# 多重分形分析 (Multifractal Analysis)

## Purpose

通过一系列广义分形维数谱 D(q) 量化不能用单一分形维数完整描述的复杂空间模式（如裂隙网络、矿石品位等）的异质性。
## Aliases

- not-confirmed-from-current-pages
## Workflow

将研究区划分为尺度 ε 的盒子，计算每个盒子的概率质量 Pi(ε)；计算 q 阶矩的配分函数 Z(q,ε)=Σ Pi^q；在对数图上对每个 q 拟合斜率得到 D(q)。
## Inputs

- 空间分布模式数据（二值或灰度图）
## Outputs

- 广义分形维数谱 D(q)
## Assumptions

- 现象在其测量尺度范围内具有尺度不变性或长程相关性
- 数据足够密集
## Strengths

- 比单分形维数提供更丰富的空间聚集模式信息
## Limitations

- 计算复杂，对数据质量和规模要求高
- 对噪声和采样方案敏感
## Related Concepts

- not-confirmed-from-current-pages
## Source Papers

- [2013-kruhl-fractal-geometry-techniques-in-the-quantification-of-complex-rock-structures-a-specia](../papers/2013-kruhl-fractal-geometry-techniques-in-the-quantification-of-complex-rock-structures-a-specia.md)
