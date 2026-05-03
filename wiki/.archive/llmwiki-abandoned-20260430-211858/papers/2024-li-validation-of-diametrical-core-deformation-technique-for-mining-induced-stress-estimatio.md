---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2024-li-validation-of-diametrical-core-deformation-technique-for-mining-induced-stress-estimatio"
title: "Validation of Diametrical Core Deformation Technique for Mining-Induced Stress Estimation: A Case Study."
status: "draft"
source_pdf: "data/papers/2024 - Validation of Diametrical Core Deformation Technique for Mining-Induced Stress Estimation A Case Study.pdf"
collections:
  - "zotero new"
citation: "Li, Yizhuo, et al. “Validation of Diametrical Core Deformation Technique for Mining-Induced Stress Estimation: A Case Study.” *Rock Mechanics and Rock Engineering*, vol. 57, 2024, pp. 7643–52, doi:10.1007/s00603-024-03866-x."
indexed_texts: "7"
indexed_chars: "32195"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T14:40:39"
---

# Validation of Diametrical Core Deformation Technique for Mining-Induced Stress Estimation: A Case Study.

## One-line Summary
通过加拿大地下矿山的案例研究，验证了直径岩芯变形技术估算采矿诱导应力的有效性，其结果与校准后的FLAC3D数值模型吻合良好 [Li 2024, pp. 1-2] [Li 2024, pp. 9-10]。

## Research Question
直径岩芯变形技术能否在实际现场条件下有效估算采矿诱导应力的量值和方向？ [Li 2024, pp. 1-2]

## Study Area / Data
- **地点**：加拿大安大略省北部的 Young-Davidson 金矿，由 Alamos Gold Inc. 运营 [Li 2024, pp. 2-3]。
- **地质背景**：矿床位于 Kirkland-Larder Lake 金矿带内，横跨区域性的 Larder Lake-Cadillac 断裂带。矿体走向大致为东西向，开采深度超过1500米 [Li 2024, pp. 2-3]。
- **数据来源**：
    - **岩芯**：从该矿 9130 水平（地表以下1170米）的一条运输巷道的底板钻孔中提取了两段 NQ 规格（内径47.6毫米）的金刚石钻探岩芯，用于 DCDT 分析 [Li 2024, pp. 3-5] [Li 2024, pp. 5-7]。
    - **原位地应力数据**：基于先前研究中在该矿四个不同水平测量的地应力数据，用于建立数值模型和推导原位应力方程 [Li 2024, pp. 3-5]。

## Methods
1.  **直径岩芯变形技术**：
    - 从目标区域（运输巷道底板以下1.5米和3米处）定向提取岩芯，并标记北向 [Li 2024, pp. 3-5]。
    - 在实验室使用高精度激光设备测量岩芯直径的微小变化。每个岩芯样本旋转360度三次，并拟合最佳正弦曲线，以确定最大直径与最小直径及其方向 [Li 2024, pp. 5-7]。
    - 利用先前研究中开发的解析模型，结合岩石的弹性性质（E, ν），从直径变形数据反算岩芯所在平面的双轴应力状态（大小和方向） [Li 2024, pp. 1-2] [Li 2024, pp. 5-7]。

2.  **数值模拟验证**：
    - **模型**：使用 FLAC3D 代码开发了一个全矿区三维数值模型 [Li 2024, pp. 1-2]。
    - **模型简化与校准**：该模型是 Khalil (2023) 开发的综合模型的精简版，模拟了过去的采矿和充填序列。模型基于地质力学数据和原位应力状态，并使用 Hoek–Brown、Burst Potential Index 和 Brittle Shear Ratio 等多种岩爆准则，对照记录到的九次主要采矿诱发地震事件进行了校准 [Li 2024, pp. 1-2] [Li 2024, pp. 5-7]。
    - **应力对比**：在线弹性模式下运行模型至岩芯提取时的采动状态，计算岩芯所在位置的应力，并与 DCDT 的估算结果进行对比，以验证 DCDT [Li 2024, pp. 1-2] [Li 2024, pp. 7-9]。

## Key Findings
- **应力方向比较**：DCDT 估算的最大主应力方向平均为 N67°E，这与 McKinnon 和 Labrie (2006) 报告的区域主应力方向 N35°E 一致 [Li 2024, pp. 5-7] [Li 2024, pp. 7-9]。
- **应力量值比较**：DCDT 与 FLAC3D 模型在岩芯位置计算得到的最大、最小及差异主应力总体上具有良好的一致性。例如，在 A 点，两者的差异主应力差异为 8.7%；在 B 点，最小主应力差异仅为 0.3% [Li 2024, pp. 9-10]。
- **技术有效性**：对比结果显示合理的良好吻合，表明 DCDT 是一种适用于确定采掘面附近采矿诱导应力的方法，可作为岩层控制工具来帮助检测应力相关的地压问题 [Li 2024, pp. 1-2] [Li 2024, pp. 9-10]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| DCDT 在 A 点 (3m 深) 估算的最大主应力 (σH) 为 66.4 MPa，最小主应力 (σh) 为 17.9 MPa；FLAC3D 计算结果为 σL1 = 80.1 MPa, σL2 = 26.9 MPa，差异分别为 17.1% 和 33% | [Li 2024, pp. 9-10] Table 6 | NQ 规格岩芯，位置 9130 水平，岩石类型为 TSED，数据来自 DCDT 测量和线弹性 FLAC3D 模型 | DCDT 与数值模型在最大主应力的差异小于最小主应力。 |
| DCDT 在 B 点 (1.5m 深) 估算的最大主应力为 107.6 MPa，最小主应力为 29.1 MPa；FLAC3D 计算结果为 94.2 MPa 和 29.0 MPa | [Li 2024, pp. 9-10] Table 6 | NQ 规格岩芯，位置 9130 水平，岩石类型为 TSED | 在 B 点，最小主应力的差异仅为 0.3%，表现出了极好的一致性。 |
| DCDT 估算的最大主应力方向平均为 N67°E | [Li 2024, pp. 5-7] Section 3.2; Fig. 10 | 岩芯样本来自钻孔 YD-9130L-NQ-V1 和 V2 | 该结果与区域主应力方向 N35°E 可比 [Li 2024, pp. 7-9]。 |
| FLAC3D 模型计算的原位应力与通过线性回归测量值得到的式 (1) 一致性良好 | [Li 2024, pp. 7-9] Fig. 13 | 模型从模型底部到地表，初始应力与回归方程吻合 | 验证了 FLAC3D 模型初始应力场的模拟准确性。 |

## Limitations
- 案例研究仅基于加拿大 Young-Davidson 矿一个采场底板的两段岩芯，样本量有限 [Li 2024, pp. 3-5]。
- FLAC3D 模型运行在线弹性模式下，且是简化了采充历史的“精简版”，可能未完全反映所有复杂的地质和采矿因素 [Li 2024, pp. 5-7]。
- DCDT 测量结果本身存在变异性，如两个样本估测的主应力方向分别为 N45°E 和 N90°E，存在 45 度差异 [Li 2024, pp. 5-7]。
- 文中未讨论 DCDT 在不同岩性、不同深度或不同应力条件下的适用性限制。

## Assumptions / Conditions
- **原位应力场假设**：假设原位应力场随深度线性变化，并基于此拟合了地应力方程 [Li 2024, pp. 3-5]。
- **数值模型假设**：模型为线弹性模型，因此采动引起的应力不依赖于加载历史。这允许使用忽略详细采矿顺序的简化模型进行验证 [Li 2024, pp. 5-7] [Li 2024, pp. 7-9]。
- **DCDT 解析模型假设**：DCDT 的应用依赖于先前工作（Li and Mitri 2023）中开发和验证的解析模型，该模型将岩芯变形与应力状态联系起来。其假设条件（如岩石为各向同性线弹性）未在当前片段中详细说明 [Li 2024, pp. 1-2]。
- **岩性条件**：岩芯取自下盘围岩 Timiskaming sediments [Li 2024, pp. 2-3]。结论的适用性可能受岩性限制。

## Key Variables / Parameters
- **几何与位置变量**：岩芯提取位置（A点：底板下 3m，B点：底板下 1.5m）[Li 2024, pp. 5-7]。
- **材料属性**：岩石的弹性模量（E）和泊松比（ν），由单轴抗压强度测试确定 [Li 2024, pp. 5-7]。
- **测量变量**：岩芯直径最大值 (dmax) 和最小值 (dmin) [Li 2024, pp. 5-7]。
- **应力相关参数**：
    - 原位主应力 (σ1, σ2, σ3) 及其趋势/倾角 [Li 2024, pp. 3-5]。
    - 采矿诱导应力分量 (σx, σy, σz, τxy) [Li 2024, pp. 9-10]。
    - DCDT 估算的水平主应力 (σH, σh) 和方向 (θ) [Li 2024, pp. 9-10]。
    - 数值模型计算的局部主应力 (σL1, σL2) 和方向 (θL) [Li 2024, pp. 9-10]。
- **原位应力方程参数**：`σ1 = -0.065x + 677.84`, `σ2 = 0.0028x + 6.39`, `σ3 = 0.0072x - 47.72`，其中 x 为开采水平（米）[Li 2024, pp. 3-5]。

## Reusable Claims
- **CLAIM**: 在 Young-Davidson 矿 1170 米深处的运输巷道底板，直径岩芯变形技术估算的采矿诱导主应力与一个经地震事件校准的线弹性 FLAC3D 模型的计算结果吻合良好，其中最小主应力的差异可在 33% 以内，差异主应力的差异可在 20.3% 以内 [Li 2024, pp. 9-10]。**条件**: 该验证基于特定矿山的 Timiskaming sediments 岩性，使用了线弹性数值模型，且现场地应力数据存在测量变异性 [Li 2024, pp. 2-3] [Li 2024, pp. 3-5] [Li 2024, pp. 5-7]。
- **CLAIM**: DCDT 作为一种现场工具，能够用于快速估算采掘面附近的应力大小和方向，以帮助检测和诊断应力相关的岩层控制问题 [Li 2024, pp. 1-2] [Li 2024, pp. 9-10]。**条件**: 该方法需要定向取芯和高精度激光测量，并依赖于实验室标定的岩石弹性参数 [Li 2024, pp. 3-5] [Li 2024, pp. 5-7]。
- **CLAIM**: 在缺乏详细采动序列的情况下，一个简化的、达到初始平衡后仅模拟主要采充步骤的线弹性数值模型，可用于评估特定位置的采矿诱导应力 [Li 2024, pp. 5-7] [Li 2024, pp. 7-9]。**条件**: 前提是模型所采用的材料本构为线弹性，此时应力与加载路径无关。

## Candidate Concepts
- [[Diametrical Core Deformation Technique (DCDT)]]
- [[Mining-Induced Stress]]
- [[FLAC3D Numerical Modeling]]
- [[In-Situ Stress Measurement]]
- [[Stress Relief by Core Extraction]]
- [[Geomechanics Database]]
- [[Burst Potential Index (Mitri et al. 1999)]]
- [[Brittle Shear Ratio (Castro et al. 2012)]]
- [[Hoek–Brown Failure Criterion]]
- [[Linear Elastic Model]]
- [[Stress Transformation]]
- [[Principal Stress Orientation]]

## Candidate Methods
- [[Diametrical Core Deformation Technique (DCDT)]] 用于应力反演
- [[High-Precision Laser Measurement]] 用于测量岩芯直径变形
- [[FLAC3D Numerical Simulation]] 用于计算采矿诱导应力
- [[Linear Regression]] 用于建立原位地应力随深度的变化方程
- [[Stress Transformation from Cartesian to Principal Coordinates]] 用于对比不同坐标系下的应力结果

## Connections To Other Work
- **先前工作**: 本文直接验证了 Li 和 Mitri (2023) 开发的 DCDT 解析模型，将其从实验室验证扩展到现场验证 [Li 2024, pp. 1-2]。
- **地应力基础**: 案例研究依赖于 McKinnon 和 Labrie (2006) 在该矿区进行的地应力测量工作，并引用为原位应力方程和数据的基础 [Li 2024, pp. 2-3] [Li 2024, pp. 7-9]。
- **数值模型基础**: 文中所用 FLAC3D 模型是 Khalil (2023) 综合模型的精简版，Khalil 的模型使用多种岩爆准则和地震事件进行了校准 [Li 2024, pp. 1-2] [Li 2024, pp. 5-7]。
- **方法论连接**: DCDT 属于岩芯变形法的一种，可与其他应力估算方法（如 Ziegler and Valley 2021 研究的岩芯饼化分析）在主题上连接 [Li 2024, pp. 2-3]。
- **应力测量**: 本文的文献综述中提到了多种应力测量方法，可与 [[Borehole Breakout Analysis]]、[[Borehole Strain Change Back-Analysis]] 等相关主题产生联系 [Li 2024, pp. 10-10]。

## Open Questions
- DCDT 在不同岩石类型（如硬岩中的脆性岩石 vs. 软岩）中的适用性和准确性如何？ [Li 2024, pp. 2-3]
- 岩芯提取深度（距自由面的距离）对 DCDT 测量结果的敏感性如何？本研究中1.5米和3米深的两个样本在结果上表现出了差异 [Li 2024, pp. 5-7] [Li 2024, pp. 9-10]。
- 当应力状态更复杂（如三维应力接近自由面）时，DCDT 所基于的双轴应力假设会带来多大误差？
- 该技术能否以及如何应用于其他类型的矿山或地下工程（如隧道、洞室）的应力监测？

## Source Coverage
- **片段覆盖度**：此页面综合了全部 7 个片段，覆盖了从摘要、引言、方法、案例区数据、结果到结论和参考文献的完整内容。信息较为全面。
- **潜在缺失信息**：
    - DCDT 解析模型的具体数学公式未在片段中提供。
    - FLAC3D 模型的详细参数（如网格划分、边界条件、开挖步骤）仅部分说明。
    - 岩芯直径测量的原始数据点分布和正弦曲线拟合优度未详细展示。
    - 关于技术局限性的系统性讨论和未来研究方向的建议，在当前片段中较为简略。
