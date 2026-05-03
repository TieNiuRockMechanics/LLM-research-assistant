---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2025-meng-evaluation-of-the-diametrical-core-deformation-analysis-dcda-and-fracture-surface-morp"
title: "Evaluation of the Diametrical Core Deformation Analysis (DCDA) and Fracture Surface Morphology for In-Situ Stress Estimation."
status: "draft"
source_pdf: "data/papers/2025 - Evaluation of the Diametrical Core Deformation Analysis (DCDA) and Fracture Surface Morphology for In-Situ Stress Estimation.pdf"
collections:
  - "zotero new"
citation: "Meng, Qingsen, et al. “Evaluation of the Diametrical Core Deformation Analysis (DCDA) and Fracture Surface Morphology for In-Situ Stress Estimation.” *Rock Mechanics and Rock Engineering*, vol. 58, 2025, pp. 7363–76. doi:10.1007/s00603-025-04512-w. Accessed 2026."
indexed_texts: "12"
indexed_chars: "55641"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T15:12:05"
---

# Evaluation of the Diametrical Core Deformation Analysis (DCDA) and Fracture Surface Morphology for In-Situ Stress Estimation.

## One-line Summary

Meng et al. (2025) 评估了利用岩心直径变形分析 (DCDA) 与断裂面形貌来估算500米深处独居花岗岩原位应力的方法，发现DCDA估算的应力大小与水力压裂结果吻合，且断裂面的各向异性形态可推断应力方向。

## Research Question

如何通过高分辨率测量岩心样品的直径变形（DCDA）和定量表征断裂面形貌，来准确有效地估算深部钻孔中的原位应力大小和方向？ [Meng 2025, pp. 1-2]

## Study Area / Data

- **研究地点**: 中国新疆北天山地区的独居花岗岩（monzonitic granite），深度为500米。 [Meng 2025, pp. 1-2]
- **数据来源**:
    - **DYL-1号钻孔**: 获取了总长9.5米、直径54毫米的岩心。岩心连续取芯，但在三个层段不连续地采集了20个岩心样品用于分析，大部分样品呈现饼化（discing）现象，厚度在2到4厘米之间。 [Meng 2025, pp. 5]
    - **水力压裂法现场实测数据**: 用于对比验证原位应力的大小和方向。 [Meng 2025, pp. 7]
    - **岩石力学参数**: 从室内单轴抗压强度（UCS）等试验中获得，其变化范围很大。例如，密度范围为2.62–2.69 g/cm³，杨氏模量范围为20.2–43.5 GPa，泊松比范围为0.22–0.30，UCS范围为50.7–98.5 MPa。 [Meng 2025, pp. 5]

## Methods

1.  **岩心直径变形分析 (DCDA)**:
    - **测量工具**: 使用蔡司（ZEISS）Spectrum 7106三坐标测量机（CMM），最大分辨率为1.2 μm，在恒温室（23℃）中对20个岩心样品的直径进行测量。 [Meng 2025, pp. 7]
    - **理论模型**: 基于广义胡克定律，假设材料为各向同性、线弹性且发生小变形，利用岩心应力释放后最大直径（dmax）和最小直径（dmin）的差异来计算垂直于钻孔平面上的差应力，并确定其方向。 [Meng 2025, pp. 3-4]
    - **d₀估算**: 原始岩心直径d₀无法直接测量，研究中给出了基于变形后体积变化等参数推算d₀的更严谨计算公式（Eq. 11）。 [Meng 2025, pp. 4]

2.  **断裂面形貌定量表征**:
    - **三维激光扫描**: 使用三维激光扫描仪获取岩心断裂面的高分辨率数字高程模型（DEM）。 [Meng 2025, pp. 7]
    - **数据处理**: 将扫描数据在Rhino软件中处理生成三角网格模型后，导入ArcGIS软件生成栅格表面。利用ArcGIS的“空间分析-表面分析”工具，提取断裂面的基本形态参数，如外围高度分布和坡向（aspect）分布，以捕捉断裂面的各向异性。 [Meng 2025, pp. 7-8]

## Key Findings

1.  **应力大小验证**: DCDA方法估算的差应力大小与水力压裂法的现场实测结果具有良好的一致性。 [Meng 2025, pp. 1-2] 当采用平均参数（E=30 GPa, ν=0.26）时，估算的最大与最小主应力均值（29.03 MPa和8.94 MPa）与水力压裂法实测值（26.05 MPa和15.01 MPa）存在差异。 [Meng 2025, pp. 8]
2.  **应力方向验证**: 通过DCDA估算得到的最小主应力方向，与观测到的饼化断裂面形貌特征推断的方向一致。 [Meng 2025, pp. 1-2]
3.  **断裂面形貌的指示作用**: 断裂面外围高度分布呈正弦曲线模式，周期为180°，其高点和低点的方向近乎正交。这表明断裂面的形态各向异性可用于推断垂直于钻孔平面的原位应力方向。 [Meng 2025, pp. 8]
4.  **参数敏感性与误差来源**: 可靠的应力估算不仅需要高分辨率数据集，还依赖于对局部岩石力学参数（如杨氏模量E和泊松比ν）及其潜在各向异性的准确评估。岩石力学参数的变异性会导致应力估算结果的显著变化。 [Meng 2025, pp. 8,11-12]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| DCDA估算的原位应力大小与水力压裂法结果吻合良好。 | [Meng 2025, pp. 1-2] | 深度500米处的独居花岗岩。 | 与实测值对比显示了良好的一致性，但使用平均参数估算的主应力均值与实测值存在差异。 |
| 最小主应力方向由DCDA估算，并与饼化断裂形态的各向异性推断方向一致。 | [Meng 2025, pp. 1-2] | 该方法适用于垂直于钻孔平面的应力状态推断。 | 方向的一致性通过断裂面外围高度分布的正弦曲线特征和高低点正交性得到验证。 |
| 断裂面包含大量穿晶裂纹，形态呈现马鞍状，表现出典型的各向异性。 | [Meng 2025, pp. 2,8] | 高应力条件下导致岩心饼化。 | 饼化断裂面的形态是由应力条件和岩体完整性共同作用的结果。 |
| 岩石力学参数（如表1中E、ν）的高度变异性是应力估算的主要潜在误差来源。 | [Meng 2025, pp. 11-12] | 由于岩石各向异性或取芯过程中产生的微裂纹导致。 | 研究认为力学性质的各向异性是导致岩石力学参数大幅度变化的主要因素。 |

## Limitations

1.  **岩石各向异性假设**: DCDA方法基于岩心各向同性、线弹性及小变形假设。而深部钻孔岩心常因应力诱导产生垂直于轴向的微裂纹，导致力学性质呈现各向异性，这与假设不符，可能带来显著的应力估算误差。 [Meng 2025, pp. 11-12]
2.  **Sn 忽略假设**: 本研究为二维案例分析，假设了钻孔轴向的应变可忽略且平行于钻孔轴向的应力 Sz ≈ 0。此条件仅在特定工程场景（如靠近开挖面垂直钻孔取样）下成立。 [Meng 2025, pp. 4]
3.  **岩心定向问题**: 岩心样品在钻取时未使用定向工具，其参考线不指示地理方位，因此仅能确定应力的相对方向。 [Meng 2025, pp. 7]
4.  **数据质量依赖**: 可靠的应力估算高度依赖于高分辨率数据集和局部岩石力学参数的准确性。 [Meng 2025, pp. 1-2]

## Assumptions / Conditions

1.  **材料模型假设**: 岩心被假定为各向同性、线弹性材料，且发生小变形。 [Meng 2025, pp. 3-4]
2.  **应力状态简化**: 本研究聚焦于二维情况，假设钻孔垂直于开挖面且靠近开挖面取样，此时平行于钻孔轴向的应力 Sz 可忽略不计。 [Meng 2025, pp. 4]
3.  **d₀ 替代与修正**: 由于 d₀ 约比变形量大三个数量级，在 DCDA 的差应力解析解（Eq. 3）中，可用 d_min 近似替代 d₀ 进行计算。 [Meng 2025, pp. 3-4]
4.  **测量控制**: 样品在测量前需在控温室中放置48小时以保持恒温（23℃），且扫描过程中保持恒定的接触力（0.5 N）和速度（5 mm/s）。 [Meng 2025, pp. 7]

## Key Variables / Parameters

- **测量变量**: 最大直径（d_max），最小直径（d_min），直径差（Δd = d_max - d_min），原始直径（d₀），岩心长度（L₀, L₁）。 [Meng 2025, pp. 3-4,8]
- **应力与应变**: 最大主应力（S_max），最小主应力（S_min），差应力（S_max - S_min）；最大张应变（ε_max）和最小张应变（ε_min）。 [Meng 2025, pp. 3-4,8]
- **岩石力学参数**: 杨氏模量（E），泊松比（ν），单轴抗压强度（UCS），抗拉强度。 [Meng 2025, pp. 3-4,5]
- **形貌参数**: 断裂面外围高度分布，坡向分布。 [Meng 2025, pp. 8]

## Reusable Claims

1.  “DCDA方法可有效估算原位应力大小，其结果与水力压裂法结果吻合良好，但准确性高度依赖于局部岩石力学参数（E, ν）的准确获取。” [Meng 2025, pp. 1-2,8,11-12]（适用条件：需要超高分辨率（微米级）的直径测量设备；限制：要求岩石近似各向同性弹性体，在存在明显应力诱导微裂纹的情况下可能产生误差。）
2.  “饼化岩心断裂面的形态具有各向异性，其外围高度呈180°周期的正弦分布，高低点方向近乎正交，可用于推断垂直于钻孔平面的最小主应力方向。” [Meng 2025, pp. 8]（适用条件：岩心发生典型的拉伸破坏应力饼化，形成如马鞍状的断裂面；限制：需要三维激光扫描等精确的形态定量表征工具，且推断的是应力在平面内的相对方向。）
3.  “利用三坐标测量机（CMM）可实现对岩心直径变形的连续、精确测量（分辨率达1.2μm），为DCDA应力估算提供了比传统光学方法更精确和便捷的测量基础。” [Meng 2025, pp. 11]

## Candidate Concepts

- [[in-situ stress estimation]]
- [[core discing]]
- [[diametrical core deformation analysis (DCDA)]]
- [[fracture surface morphology]]
- [[hydraulic fracturing method]]
- [[stress-induced microcracks]]
- [[anisotropy of rock mechanical properties]]

## Candidate Methods

- [[Diametrical Core Deformation Analysis (DCDA)]]
- [[coordinate measuring machine (CMM)]]
- [[3D laser scanning]] for [[fracture surface characterization]]
- [[ArcGIS spatial analysis]] for morphological parameter extraction
- [[hydraulic fracturing in-situ stress measurement]]
- [[least square regression fitting]] for diameter data

## Connections To Other Work

- 该研究引用了将岩心饼化视为拉伸破坏机制的普遍观点，该观点被有限元数值模拟和实验室研究所支持 [Meng 2025, pp. 2]。例如，当最大主应力约为岩石抗拉强度6.5倍时，岩心饼化开始发生，这来自连接至 [[Lim and Martin 2010]] 的工作 [Meng 2025, pp. 2-3]。
- 研究在方法上参考并改进了前人工作：与 [[Ito et al. 2013]] 提出的 DCDA 理论分析模型及光学测微计测量，以及 [[Ziegler and Valley 2021]] 的摄影测量技术相比，本文采用的CMM技术提升了精度和便利性 [Meng 2025, pp. 3,11]。
- 该研究的核心主题可从概念上连接到关于深部钻孔损伤的 [[Martin and Stimpson 1994]] 和 [[Lim et al. 2012]] 的工作，以及关于岩心饼化与应力状态关系的 [[Matsuki et al. 2004]] 和 [[Funato and Ito 2017]] 的工作 [Meng 2025, pp. 2-4]。

## Open Questions

1.  如何定量评估和校正由应力诱导的微裂纹引起的各向异性对岩心变形的影响，以修正 DCDA 方法的系统性误差？ [Meng 2025, pp. 11-12]
2.  未从索引片段中确认文中提及的“三轴应力状态下通过三个互相垂直方向钻孔的岩心进行DCDA分析”的全三维应用效果与局限。
3.  未从索引片段中确认对于非马鞍形（例如平坦、杯状）的饼化断裂面，其形貌与应力方向的定量关系是否仍然成立。

## Source Coverage

- 本页面基于论文的12个索引片段生成，覆盖了摘要、引言、方法论、实验程序、部分结果和讨论章节。
- 覆盖内容侧重于研究方法（DCDA与断裂面形貌测量）、主要发现（大小和方向一致性验证）以及核心局限性（各向异性假设）。
- **信息缺失**: 测量结果中特定样品的d_max、d_min、Δd等完整数值表格（仅部分内容在片段中呈现）、与水力压裂结果的具体对比图表（图8）、详细的敏感性分析结果（图7）、以及讨论部分5.2节关于应力方向的全部内容缺失。对于应力测量的一个潜在偏差来源——温度影响的分析可能不完整。
