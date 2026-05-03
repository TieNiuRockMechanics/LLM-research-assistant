---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "运动学断裂生成模型 (Kinematic Fracture Model, KFM)"
aliases:
  - "KFM"
  - "kinematic fracture model"
sources:
  - "2013-davy-a-model-of-fracture-nucleation-growth-and-arrest-and-consequences-for-fracture-density"
  - "2016-maillot-connectivity-permeability-and-channeling-in-randomly-distributed-and-kinematically"
---

# 运动学断裂生成模型 (Kinematic Fracture Model, KFM)

## Purpose

基于简化运动学规则（成核、生长、停止）生成三维离散裂隙网络，模拟天然裂隙形成中的力学相互作用，生成比泊松模型更具空间相关性和 T 形交切的网络。
## Aliases

- KFM
- kinematic fracture model
## Workflow

设定断裂成核的分布和顺序（竞争或顺序）；各核遵循幂律生长规律（如 Charles 定律）向周围生长；当生长中的裂隙与更大的裂隙相交（T 形接触）时即停止生长；持续此过程直到达到指定密度或所有裂隙停止。
## Inputs

- 成核速率和分布
- 幂律生长指数 a
- 停止模式（一臂或两臂停止）
## Outputs

- 具有 T 形交切和空间聚集性的 DFN 模型
## Assumptions

- 裂隙生长可近似满足幂律关系
- 大裂隙对小裂隙存在绝对的力学抑制
- 裂隙被简化为圆盘，忽略各向异性生长效应
## Strengths

- 能生成与天然节理网络高度相似的 T 形交切和自相似长度分布
- 相比泊松模型有更强的空间相关性和更真实的渗流行为
## Limitations

- 模型参数众多（成核率、生长率、停止模式），标定困难
- 裂隙停止判据纯几何，缺少严格的能量平衡机制
## Related Concepts

- discrete-fracture-network
## Source Papers

- [2013-davy-a-model-of-fracture-nucleation-growth-and-arrest-and-consequences-for-fracture-density](../papers/2013-davy-a-model-of-fracture-nucleation-growth-and-arrest-and-consequences-for-fracture-density.md)
- [2016-maillot-connectivity-permeability-and-channeling-in-randomly-distributed-and-kinematically](../papers/2016-maillot-connectivity-permeability-and-channeling-in-randomly-distributed-and-kinematically.md)
