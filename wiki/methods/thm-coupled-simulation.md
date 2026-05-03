---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "热-水-力耦合数值模拟 (THM Coupling)"
aliases:
  - "THM FEM"
  - "Thermal-Hydraulic-Mechanical coupling simulation"
  - "热-流-固耦合模拟"
sources:
  - "2017-sun-numerical-simulation-of-the-heat-extraction-in-egs-with-thermal-hydraulic-mechanical-co"
  - "2018-salimzadeh-a-three-dimensional-coupled-thermo-hydro-mechanical-model-for-deformable-fractur"
  - "2023-xue-effect-of-water-cooling-shock-on-fracture-initiation-and-morphology-of-high-temperature"
  - "2024-suo-experimental-and-numerical-simulation-research-on-hot-dry-rock-wellbore-stability-under"
---

# 热-水-力耦合数值模拟 (THM Coupling)

## Purpose

求解温度、流体流动和岩石变形相互作用的偏微分方程组，用于预测地热储层注采过程中的温度场、压力场、应力场和裂隙开度演化。
## Aliases

- THM FEM
- Thermal-Hydraulic-Mechanical coupling simulation
- 热-流-固耦合模拟
## Workflow

建立包含基质和裂隙的几何模型，定义达西流、能量平衡、线弹性（或更复杂本构）控制方程；可采用等效连续介质或离散裂隙模型；通过有限元/有限体积法离散，进行顺序或全耦合迭代求解。
## Inputs

- 材料热物性和力学参数
- 初始地应力场
- 注入/生产温度、压力制度
## Outputs

- 温度场、压力场
- 应力/应变和破坏区
- 裂隙开度演化
## Assumptions

- 局部热平衡或非平衡可选
- 单相流
- 忽略化学反应（纯 THM）
## Strengths

- 可同时预测流动通道化、热突破和力学稳定性
## Limitations

- 大尺度 DFN 全耦合计算成本极高
- 参数不易准确获取
## Related Concepts

- fractured-reservoir
- local-thermal-non-equilibrium
- thermo-hydro-mechanical-coupling
## Source Papers

- [2017-sun-numerical-simulation-of-the-heat-extraction-in-egs-with-thermal-hydraulic-mechanical-co](../papers/2017-sun-numerical-simulation-of-the-heat-extraction-in-egs-with-thermal-hydraulic-mechanical-co.md)
- [2018-salimzadeh-a-three-dimensional-coupled-thermo-hydro-mechanical-model-for-deformable-fractur](../papers/2018-salimzadeh-a-three-dimensional-coupled-thermo-hydro-mechanical-model-for-deformable-fractur.md)
- [2023-xue-effect-of-water-cooling-shock-on-fracture-initiation-and-morphology-of-high-temperature](../papers/2023-xue-effect-of-water-cooling-shock-on-fracture-initiation-and-morphology-of-high-temperature.md)
- [2024-suo-experimental-and-numerical-simulation-research-on-hot-dry-rock-wellbore-stability-under](../papers/2024-suo-experimental-and-numerical-simulation-research-on-hot-dry-rock-wellbore-stability-under.md)
