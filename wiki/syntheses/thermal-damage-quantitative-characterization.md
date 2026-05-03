---
type: "synthesis"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
title: "岩石热损伤的多尺度表征与定量无损评价"
sources:
  - "2024-xi-experimental-study-on-pore-characteristics-evolution-and-rock-damage-mechanism-of-therma"
  - "2024-bu-deterioration-of-equivalent-thermal-conductivity-of-granite-subjected-to-heating-cooling"
  - "2024-yang-multiscale-damage-and-thermal-stress-evolution-characteristics-of-rocks-with-thermal-s"
  - "2021-li-thermal-damage-effect-on-the-thermal-conductivity-inhomogeneity-of-granite"
  - "2020-li-effect-of-mechanical-damage-on-the-thermal-conductivity-of-granite"
  - "2021-verma-prediction-of-thermal-conductivity-and-damage-in-indian-jalore-granite-for-design-of"
---

# 岩石热损伤的多尺度表征与定量无损评价

## Central Question

如何利用XRD、SEM、NMR、CT、超声和热导率等多尺度手段，建立热损伤的定量指标，并实现基于波速等无损参数的损伤评估？
## Synthesis

热处理（尤其 >400 °C）显著改变花岗岩微观孔裂隙结构。XRD、SEM、NMR等揭示矿物相变和微裂纹演化，CT和超声可量化裂纹密度和分布。热导率随损伤线性下降，且与P波速度、孔隙度呈强线性相关。通过基于波速定义的损伤变量，可统一不同冷却方式下的劣化趋势，实现了从微观到宏观的无损定量表征，为深部地热和核废料处置工程提供关键物性参数。
## Evidence Chain

- Xi (2024) 用 NMR 孔隙率损伤和波速损伤拟合出 R²>0.97 的相关曲线。
- Bu (2024) 发现热导率也与微裂纹密度呈线性负相关，并可统一到损伤框架。
- Yang (2024) 的颗粒基模型模拟了加热‑冷却全过程微裂纹的萌生和扩展，验证了晶间裂纹的主导地位。
- Li (2021) 热处理（尤其 >400 °C）显著降低花岗岩热导率，降幅可达 50% 以上；水冷比空气冷却降幅更大。
- Li (2020) 发现热导率与 P 波速度呈强线性正相关，与孔隙度呈强线性负相关。
- Verma (2021) AI 预测模型验证了热导率与损伤关系。
## Disagreements / Tensions

- 不同岩石类型（砂岩、花岗岩、灰岩）的损伤演变批次存在差异，尤其是沉积岩的烧结和方解石分解使损伤趋势更复杂。
- 孔隙度—强度关系在某些砂岩中并非单调。
- 水冷增加热导率非均匀度的原因：是宏观裂纹集聚还是石英相变导致的局部弱化，不同作者侧重不同。
## Boundary Conditions

- 适用于结晶岩，尤其是含石英花岗岩；干燥条件；常压室温测量
- 热导率变化以基质热传导为主，忽略对流辐射
## Writing Uses

- 支持利用地球物理测井（声波）推演深部岩体热物性
- 为设计增强型地热系统的换热功率提供输入参数
- 构建高温岩石本构模型时，可以将孔隙率或波速作为内变量
## Source Papers

- [2024-xi-experimental-study-on-pore-characteristics-evolution-and-rock-damage-mechanism-of-therma](../papers/2024-xi-experimental-study-on-pore-characteristics-evolution-and-rock-damage-mechanism-of-therma.md)
- [2024-bu-deterioration-of-equivalent-thermal-conductivity-of-granite-subjected-to-heating-cooling](../papers/2024-bu-deterioration-of-equivalent-thermal-conductivity-of-granite-subjected-to-heating-cooling.md)
- [2024-yang-multiscale-damage-and-thermal-stress-evolution-characteristics-of-rocks-with-thermal-s](../papers/2024-yang-multiscale-damage-and-thermal-stress-evolution-characteristics-of-rocks-with-thermal-s.md)
- [2021-li-thermal-damage-effect-on-the-thermal-conductivity-inhomogeneity-of-granite](../papers/2021-li-thermal-damage-effect-on-the-thermal-conductivity-inhomogeneity-of-granite.md)
- [2020-li-effect-of-mechanical-damage-on-the-thermal-conductivity-of-granite](../papers/2020-li-effect-of-mechanical-damage-on-the-thermal-conductivity-of-granite.md)
- [2021-verma-prediction-of-thermal-conductivity-and-damage-in-indian-jalore-granite-for-design-of](../papers/2021-verma-prediction-of-thermal-conductivity-and-damage-in-indian-jalore-granite-for-design-of.md)
