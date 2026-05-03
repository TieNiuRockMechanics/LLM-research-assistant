---
type: "synthesis"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
title: "基于岩心的地应力测量方法比较"
sources:
  - "2025-meng-evaluation-of-the-diametrical-core-deformation-analysis-dcda-and-fracture-surface-morp"
  - "2023-li-methodology-for-the-estimation-of-mining-face-stresses-using-rock-core-diametrical-defor"
  - "2025-dargahizarandi-determination-of-3d-stress-state-using-a-novel-integrated-diametrical-core-d"
---

# 基于岩心的地应力测量方法比较

## Central Question

各种基于岩心的地应力估算方法（DCDA、ASR、DSCA、AE）的准确性与适用性如何？
## Synthesis

岩心直径变形分析（DCDA）是近年快速发展的方法，通过高精度直径测量和弹性解算二维差分应力，并经多种现场验证有效。相较于声发射凯瑟效应、差应变曲线分析等方法，DCDA 的物理基础更清晰且无需复杂的加载历史，但要求岩石近似各向同性且具备微米级测量能力。联合破裂面形貌各向异性可进一步指示应力方向。
## Evidence Chain

- Meng (2025) 在隧道花岗岩中对比了 DCDA 和水压致裂结果，应力方向偏差 <15°，大小吻合。
- Li (2023) 建立了体积应变方程解决 DCDA 中原始直径未知的问题。
- Dargahizarandi (2025) 集成了超声波速度映射，实现三维应力张量估算。
## Disagreements / Tensions

- DCDA 获得的应力数值与套芯法或水压致裂仍存在 15–20% 的差异，弹性参数和各向异性是主要误差源。
- 对于高度各向异性的页岩或片麻岩，DCDA 表现不佳，而 ASR 或 DSCA 可能更适用。
## Boundary Conditions

- 适合深部均质花岗岩等火成岩；钻孔轴需与一个主应力平行。
## Writing Uses

- 在无法开展水压致裂的场合，推荐 DCDA 作为替代。
- 阐明现有岩心应力测试方法的优缺点，引导方法选择。
## Source Papers

- [2025-meng-evaluation-of-the-diametrical-core-deformation-analysis-dcda-and-fracture-surface-morp](../papers/2025-meng-evaluation-of-the-diametrical-core-deformation-analysis-dcda-and-fracture-surface-morp.md)
- [2023-li-methodology-for-the-estimation-of-mining-face-stresses-using-rock-core-diametrical-defor](../papers/2023-li-methodology-for-the-estimation-of-mining-face-stresses-using-rock-core-diametrical-defor.md)
- [2025-dargahizarandi-determination-of-3d-stress-state-using-a-novel-integrated-diametrical-core-d](../papers/2025-dargahizarandi-determination-of-3d-stress-state-using-a-novel-integrated-diametrical-core-d.md)
