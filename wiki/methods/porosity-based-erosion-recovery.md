---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "地层剥蚀厚度恢复 (孔隙度法)"
aliases:
  - "porosity-based erosion recovery method"
sources:
  - "2011-ni-tectonics-and-mechanisms-of-uplift-in-the-central-uplift-belt-of-the-huimin-depression"
---

# 地层剥蚀厚度恢复 (孔隙度法)

## Purpose

利用泥岩声波时差或孔隙度随深度呈指数衰减的规律，通过迭代求解恢复盆地的剥蚀厚度。
## Aliases

- porosity-based erosion recovery method
## Workflow

建立正常压实趋势下的孔隙度-深度关系 φ(z)=φ0 exp(-cZ)；根据实测孔隙度/声波时差数据，采用二元迭代法不断调整剥蚀厚度 He，直到模型计算的孔隙度与实测值达到最佳拟合。
## Inputs

- 钻井实测泥岩声波时差或孔隙度数据
- 正常压实段的孔隙度-深度趋势线
- 初始孔隙度 φ0 和压实系数 c
## Outputs

- 剥蚀厚度 He
## Assumptions

- 剥蚀前地层已历正常最大埋深压实，孔隙度-深度符合指数衰减
- 后期构造反转对现今孔隙度的叠加影响可忽略
- 压实系数 c 在地质历史时期保持恒定
## Strengths

- 物理基础明确，所需数据是盆地常规勘探数据
- 可量化连续的地层剥蚀量
## Limitations

- 在埋深 >4000 m 或发育异常高压带时模型不成立
- 存在大量不整合面或岩性变化剧烈时误差较大
- 主要适用于碎屑岩，碳酸盐岩需更复杂假设
## Related Concepts

- not-confirmed-from-current-pages
## Source Papers

- [2011-ni-tectonics-and-mechanisms-of-uplift-in-the-central-uplift-belt-of-the-huimin-depression](../papers/2011-ni-tectonics-and-mechanisms-of-uplift-in-the-central-uplift-belt-of-the-huimin-depression.md)
