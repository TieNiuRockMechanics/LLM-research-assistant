---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "有限元-离散元耦合方法 (FDEM)"
aliases:
  - "FDEM"
  - "Finite-Discrete Element Method"
  - "内聚力单元法"
sources:
  - "2025-zhai-pfc-fdem-multi-scale-cross-platform-numerical-simulation-of-thermal-crack-network-evol"
---

# 有限元-离散元耦合方法 (FDEM)

## Purpose

结合有限元和离散元，在宏观尺度上模拟岩石裂纹的萌生、扩展和破坏过程，尤其适用于动态断裂问题。
## Aliases

- FDEM
- Finite-Discrete Element Method
- 内聚力单元法
## Workflow

在有限元网格中插入零厚度内聚力单元（cohesive zone elements），定义牵引-分离法则；当应力达到强度阈值时内聚力单元失效，形成新的不连续面；可进行动态显式求解。
## Inputs

- 裂纹网络几何（可来自 PFC 映射）
- 内聚力断裂能 G_f
- 材料强度阈值
- 载荷/冲击速度
## Outputs

- 动态应力-应变
- 裂纹扩展路径和速度
- 能量分配（弹性、断裂、动能）
## Assumptions

- 平面应力或平面应变
- 裂纹按 Griffith 能量平衡扩展
## Strengths

- 能显式模拟裂纹动态扩展和多重破裂
- 可与微观 DEM 模型跨尺度耦合
## Limitations

- 网格依赖性
- 二维模型计算仍较昂贵
- 未考虑疲劳效应
## Related Concepts

- cohesive-zone-model
- multi-scale-cross-platform-coupling
## Source Papers

- [2025-zhai-pfc-fdem-multi-scale-cross-platform-numerical-simulation-of-thermal-crack-network-evol](../papers/2025-zhai-pfc-fdem-multi-scale-cross-platform-numerical-simulation-of-thermal-crack-network-evol.md)
