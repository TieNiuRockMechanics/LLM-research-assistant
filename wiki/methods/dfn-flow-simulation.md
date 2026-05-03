---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "离散裂隙网络流动与传输模拟 (DFN Flow & Transport)"
aliases:
  - "DFN permeability simulation"
  - "3D DFN flow simulation"
  - "Mixed-Hybrid FEM for DFN"
  - "DFN modeling and upscaling"
sources:
  - "2012-de-dreuzy-influence-of-fracture-scale-heterogeneity-on-the-flow-properties-of-three-dimensi"
  - "2016-hyman-fracture-size-and-transmissivity-correlations-implications-for-transport-simulations"
  - "2016-maillot-connectivity-permeability-and-channeling-in-randomly-distributed-and-kinematically"
  - "2017-lei-the-use-of-discrete-fracture-networks-for-modelling-coupled-geomechanical-and-hydrologi"
  - "2019-hyman-linking-structural-and-transport-properties-in-three-dimensional-fracture-networks"
  - "2021-gottron-upscaling-of-fractured-rock-mass-properties-an-example-comparing-discrete-fracture"
  - "2023-yoon-effects-of-dead-end-fractures-on-non-fickian-transport-in-three-dimensional-discrete-f"
  - "2024-yin-p-clet-number-dependent-longitudinal-dispersion-in-discrete-fracture-networks"
---

# 离散裂隙网络流动与传输模拟 (DFN Flow & Transport)

## Purpose

在离散裂隙网络模型上求解渗流和溶质运移，计算等效渗透率、流场和突破曲线。
## Aliases

- DFN permeability simulation
- 3D DFN flow simulation
- Mixed-Hybrid FEM for DFN
- DFN modeling and upscaling
## Workflow

生成或导入 DFN 模型；施加渗透计式边界条件（一对对面定水头，其余面不透水）；对裂隙网络进行网格划分；使用有限元/有限体积/混合有限元法求解达西流或非达西流（包括 Forchheimer 修正）；通过达西定律计算等效渗透率张量；可结合粒子追踪法进行溶质运移模拟，得到浓度突破曲线。
## Inputs

- DFN 几何模型（裂隙位置、形状、尺寸、方向）
- 各裂隙导水系数 T 或隙宽 b
- 边界条件
## Outputs

- 等效渗透率张量 K_eq
- 压力场、流速场
- 溶质突破曲线
## Assumptions

- 岩石基质不透水或极低渗透
- 裂隙内流动为层流达西流（或立方定律）
- 单裂隙内导水性常假设均匀
## Strengths

- 显式表征裂隙网络的离散特征和三维连通性
- 可与粒子追踪模拟结合研究非反应性溶质传输
## Limitations

- 计算量大，特别是高密度网络
- 网格化难度大，尤其在 T 形相交处
- 标准模型中裂隙内孔径变化通常被简化
## Related Concepts

- discrete-fracture-network
- permeability-upscaling
- cubic-law
## Source Papers

- [2012-de-dreuzy-influence-of-fracture-scale-heterogeneity-on-the-flow-properties-of-three-dimensi](../papers/2012-de-dreuzy-influence-of-fracture-scale-heterogeneity-on-the-flow-properties-of-three-dimensi.md)
- [2016-hyman-fracture-size-and-transmissivity-correlations-implications-for-transport-simulations](../papers/2016-hyman-fracture-size-and-transmissivity-correlations-implications-for-transport-simulations.md)
- [2016-maillot-connectivity-permeability-and-channeling-in-randomly-distributed-and-kinematically](../papers/2016-maillot-connectivity-permeability-and-channeling-in-randomly-distributed-and-kinematically.md)
- [2017-lei-the-use-of-discrete-fracture-networks-for-modelling-coupled-geomechanical-and-hydrologi](../papers/2017-lei-the-use-of-discrete-fracture-networks-for-modelling-coupled-geomechanical-and-hydrologi.md)
- [2019-hyman-linking-structural-and-transport-properties-in-three-dimensional-fracture-networks](../papers/2019-hyman-linking-structural-and-transport-properties-in-three-dimensional-fracture-networks.md)
- [2021-gottron-upscaling-of-fractured-rock-mass-properties-an-example-comparing-discrete-fracture](../papers/2021-gottron-upscaling-of-fractured-rock-mass-properties-an-example-comparing-discrete-fracture.md)
- [2023-yoon-effects-of-dead-end-fractures-on-non-fickian-transport-in-three-dimensional-discrete-f](../papers/2023-yoon-effects-of-dead-end-fractures-on-non-fickian-transport-in-three-dimensional-discrete-f.md)
- [2024-yin-p-clet-number-dependent-longitudinal-dispersion-in-discrete-fracture-networks](../papers/2024-yin-p-clet-number-dependent-longitudinal-dispersion-in-discrete-fracture-networks.md)
