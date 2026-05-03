---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "基于统计分布的离散裂隙网络随机生成 (Statistical DFN Generation)"
aliases:
  - "stochastic DFN"
  - "Monte Carlo DFN generation"
  - "HatchFrac"
  - "FracMan"
  - "3DEC"
  - "RJNS3D"
  - "fractal DFN generation"
sources:
  - "2009-kim-estimation-of-fracture-porosity-of-naturally-fractured-reservoirs-with-no-matrix-porosi"
  - "2015-liu-a-fractal-model-for-characterizing-fluid-flow-in-fractured-rock-masses-based-on-randoml"
  - "2016-liu-a-fractal-model-based-on-a-new-governing-equation-of-fluid-flow-in-fractures-for-charac"
  - "2020-chen-equivalent-permeability-distribution-for-fractured-porous-rocks-correlating-fracture-a"
  - "2022-zhu-hatchfrac-a-fast-open-source-dfn-modeling-software"
  - "2022-zhu-enhancing-fracture-network-characterization-a-data-driven-outcrop-based-analysis"
  - "2025-zhang-intelligent-construction-method-for-rock-slope-fracture-network-model-based-on-discre"
  - "2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi"
---

# 基于统计分布的离散裂隙网络随机生成 (Statistical DFN Generation)

## Purpose

根据裂隙产状、尺寸、密度的统计分布，通过蒙特卡洛方法生成二维或三维离散裂隙网络，用于后续渗流/输运模拟。
## Aliases

- stochastic DFN
- Monte Carlo DFN generation
- HatchFrac
- FracMan
- 3DEC
- RJNS3D
- fractal DFN generation
## Workflow

定义裂隙统计参数（Fisher 分布方向、幂律/对数正态长度、泊松位置、开度模型）；从相应分布中随机抽样生成裂隙圆盘/直线；检查交切和连通性；实现可从简单几何抽样到分形级联、乘法级联等不同算法。常用软件包括 FracMan、HatchFrac、3DEC、RJNS3D 等。
## Inputs

- 裂隙产状分布参数
- 长度分布参数（幂律指数、上下限）
- 密度指标（如 P32）
- 裂缝开度模型
## Outputs

- 符合指定统计的离散裂隙网络（几何、拓扑）
## Assumptions

- 裂隙为平面圆盘或直线
- 基质不可渗透
- 统计分布参数相互独立
## Strengths

- 可高效生成大量实现，便于不确定性量化
- 可匹配多种野外统计特征
## Limitations

- 默认空间泊松分布可能忽略天然裂隙的丛集性
- 高密度 3D 网络计算成本极高
- 未考虑力学成因关联
## Related Concepts

- discrete-fracture-network
- power-law-length-distribution
- fractal-dimension
## Source Papers

- [2009-kim-estimation-of-fracture-porosity-of-naturally-fractured-reservoirs-with-no-matrix-porosi](../papers/2009-kim-estimation-of-fracture-porosity-of-naturally-fractured-reservoirs-with-no-matrix-porosi.md)
- [2015-liu-a-fractal-model-for-characterizing-fluid-flow-in-fractured-rock-masses-based-on-randoml](../papers/2015-liu-a-fractal-model-for-characterizing-fluid-flow-in-fractured-rock-masses-based-on-randoml.md)
- [2016-liu-a-fractal-model-based-on-a-new-governing-equation-of-fluid-flow-in-fractures-for-charac](../papers/2016-liu-a-fractal-model-based-on-a-new-governing-equation-of-fluid-flow-in-fractures-for-charac.md)
- [2020-chen-equivalent-permeability-distribution-for-fractured-porous-rocks-correlating-fracture-a](../papers/2020-chen-equivalent-permeability-distribution-for-fractured-porous-rocks-correlating-fracture-a.md)
- [2022-zhu-hatchfrac-a-fast-open-source-dfn-modeling-software](../papers/2022-zhu-hatchfrac-a-fast-open-source-dfn-modeling-software.md)
- [2022-zhu-enhancing-fracture-network-characterization-a-data-driven-outcrop-based-analysis](../papers/2022-zhu-enhancing-fracture-network-characterization-a-data-driven-outcrop-based-analysis.md)
- [2025-zhang-intelligent-construction-method-for-rock-slope-fracture-network-model-based-on-discre](../papers/2025-zhang-intelligent-construction-method-for-rock-slope-fracture-network-model-based-on-discre.md)
- [2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi](../papers/2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi.md)
