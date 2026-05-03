---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "水力层析成像 (Hydraulic Tomography, HT)"
aliases:
  - "HT"
  - "Hydraulic Tomography"
sources:
  - "2019-dong-equivalence-of-discrete-fracture-network-and-porous-media-models-by-hydraulic-tomograp"
---

# 水力层析成像 (Hydraulic Tomography, HT)

## Purpose

通过多井顺序注水/抽水的水头响应反演裂隙岩体导水率和储水率空间分布。
## Aliases

- HT
- Hydraulic Tomography
## Workflow

实施交叉孔注水试验；用连续线性估计器 (SimSLE) 或类似反演算法，结合顺序抽水/观测压力响应，反演得到导水率 (K) 和储水率 (Ss) 的空间分布。
## Inputs

- 注水/抽水速率
- 多井观测水头时间序列
## Outputs

- 导水率分布 K
- 储水率分布 Ss
- 等效渗透率场
## Assumptions

- 等效多孔介质模型成立
- 达西流
## Strengths

- 无需预先知道 DFN 几何
## Limitations

- 在无 REV 时仅能识别主导裂隙
## Related Concepts

- equivalent-porous-media
## Source Papers

- [2019-dong-equivalence-of-discrete-fracture-network-and-porous-media-models-by-hydraulic-tomograp](../papers/2019-dong-equivalence-of-discrete-fracture-network-and-porous-media-models-by-hydraulic-tomograp.md)
