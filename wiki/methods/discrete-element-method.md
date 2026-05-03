---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "离散元法 (Distinct Element Method, DEM)"
aliases:
  - "DEM"
  - "Distinct Element Method"
  - "离散元"
  - "UDEC"
  - "3DEC"
  - "PFC"
  - "Particle Flow Code"
  - "颗粒流"
sources:
  - "2017-lei-the-use-of-discrete-fracture-networks-for-modelling-coupled-geomechanical-and-hydrologi"
  - "2019-lak-discrete-element-modeling-of-explosion-induced-fracture-extension-in-jointed-rock-masse"
  - "2022-feng-study-on-a-damage-model-and-uniaxial-compression-simulation-method-of-frozen-thawed-ro"
  - "2023-guo-impact-of-cooling-rate-on-mechanical-properties-and-failure-mechanism-of-sandstone-unde"
  - "2025-zhai-pfc-fdem-multi-scale-cross-platform-numerical-simulation-of-thermal-crack-network-evol"
---

# 离散元法 (Distinct Element Method, DEM)

## Purpose

模拟节理岩体或颗粒材料在准静态或动态载荷下的变形、破坏和裂隙扩展。包括块体离散元 (UDEC/3DEC) 和颗粒流 (PFC) 两种主要形式。
## Aliases

- DEM
- Distinct Element Method
- 离散元
- UDEC
- 3DEC
- PFC
- Particle Flow Code
- 颗粒流
## Workflow

定义块体/颗粒形状与接触力学定律；施加边界条件和载荷；通过显式时间步长求解运动方程；监测接触状态、裂纹萌生与扩展。在 PFC 中可结合平行粘结模型 (PBM) 和光滑节理模型 (SJM)。
## Inputs

- 节理/颗粒接触刚度、强度参数
- 块体密度
- 边界载荷或位移
## Outputs

- 应力分布、位移场
- 裂隙开度、块体运动
- 微裂纹数量、类型和空间分布
## Assumptions

- 块体可变形或刚性
- 接触遵守库仑摩擦等条件
## Strengths

- 能自然模拟大变形、块体旋转/滑动以及裂纹萌生、扩展
- 无需预设裂纹路径
## Limitations

- 计算量大
- 微观参数标定困难且非唯一
- 模型尺寸受限
## Related Concepts

- fractured-reservoir
- grain-based-model
## Source Papers

- [2017-lei-the-use-of-discrete-fracture-networks-for-modelling-coupled-geomechanical-and-hydrologi](../papers/2017-lei-the-use-of-discrete-fracture-networks-for-modelling-coupled-geomechanical-and-hydrologi.md)
- [2019-lak-discrete-element-modeling-of-explosion-induced-fracture-extension-in-jointed-rock-masse](../papers/2019-lak-discrete-element-modeling-of-explosion-induced-fracture-extension-in-jointed-rock-masse.md)
- [2022-feng-study-on-a-damage-model-and-uniaxial-compression-simulation-method-of-frozen-thawed-ro](../papers/2022-feng-study-on-a-damage-model-and-uniaxial-compression-simulation-method-of-frozen-thawed-ro.md)
- [2023-guo-impact-of-cooling-rate-on-mechanical-properties-and-failure-mechanism-of-sandstone-unde](../papers/2023-guo-impact-of-cooling-rate-on-mechanical-properties-and-failure-mechanism-of-sandstone-unde.md)
- [2025-zhai-pfc-fdem-multi-scale-cross-platform-numerical-simulation-of-thermal-crack-network-evol](../papers/2025-zhai-pfc-fdem-multi-scale-cross-platform-numerical-simulation-of-thermal-crack-network-evol.md)
