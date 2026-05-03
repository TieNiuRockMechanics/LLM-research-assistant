---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2025-dargahizarandi-determination-of-3d-stress-state-using-a-novel-integrated-diametrical-core-d"
title: "Determination of 3D Stress State Using a Novel Integrated Diametrical Core Deformation and Ultrasonic Analysis."
status: "draft"
source_pdf: "data/papers/2025 - Determination of 3D Stress State Using a Novel Integrated Diametrical Core Deformation and Ultrasonic Analysis.pdf"
collections:
  - "zotero new"
citation: "Dargahizarandi, Atefeh, et al. \"Determination of 3D Stress State Using a Novel Integrated Diametrical Core Deformation and Ultrasonic Analysis.\" *Rock Mechanics and Rock Engineering*, vol. 58, 2025, pp. 4377–4401, doi:10.1007/s00603-025-04427-6. Accessed 2026."
indexed_texts: "14"
indexed_chars: "69367"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T15:02:48"
---

# Determination of 3D Stress State Using a Novel Integrated Diametrical Core Deformation and Ultrasonic Analysis.

## One-line Summary
该研究提出了一种结合直径岩芯变形分析与超声波成像的综合方法，从钻孔岩芯中测定完整的三维地应力状态（包括大小、方位角和倾角），并通过澳大利亚某地下金属矿的样本进行了验证 [Dargahizarandi 2025, pp. 1-2]。

## Research Question
如何克服现有岩芯法只能估算二维应力，或可靠性低、成本高的局限，从岩芯样本中可靠且经济地测定完整三维应力张量（应力大小、方位角和倾角）？[Dargahizarandi 2025, pp. 1-2, 3-4]

## Study Area / Data
研究使用了来自澳大利亚昆士兰州 Dugald River 地下金属矿的两个垂直钻孔的八块岩芯样本 [Dargahizarandi 2025, pp. 1-2, 8-9]。该矿是一个锌-铅-银（Zn–Pb–Ag）矿床，深度极大，地应力可达约70 MPa [Dargahizarandi 2025, pp. 2-3, 8-9]。未从索引片段中确认具体的钻孔位置坐标与采样深度等细节。

## Methods
该研究开发并验证了一套新的综合方法，流程如下：
1.  **应力方位角估算**：基于**岩芯直径变形分析（DCDA）** 原理。岩芯从地应力环境中取出后会发生膨胀，沿最大水平主应力方向的膨胀最大，形成椭圆形截面。通过激光扫描仪测量岩芯在不同方向的直径，最大和最小直径的方向即对应最大和最小水平主应力的方位角 [Dargahizarandi 2025, pp. 3-4]。
2.  **应力倾角测量**：基于**超声波速度各向异性**原理。沿已确定的水平主应力方向，在不同倾角钻取子样本，通过超声波脉冲传输测量纵波（P波）波速。对于最大主应力，在其真实倾角方向上，由于膨胀最大，波速最慢（到达时间最长）；对于最小主应力，在其真实倾角方向上，由于膨胀最小，波速最快（到达时间最短）[Dargahizarandi 2025, pp. 6-8]。
3.  **应力大小计算**：使用一个新的解析技术，基于测量的直径变化、岩芯的弹性模量和泊松比来计算主应力的大小。推导出的公式包含了垂直应力的影响，但在本研究中，由于主应力方向接近垂直，采用了忽略垂直应力影响的简化方程 [Dargahizarandi 2025, pp. 8-9]。未从索引片段中确认应力大小计算公式的完整推导。
4.  **验证与辅助测量**：
    *   **弹性参数测定**: 对岩芯样本进行单轴压缩试验，使用轴向应变片（TML, Model PFL-10-11-3LJCT-F）和环向引伸计（Epsilon Technology, Model 3544）测定杨氏模量和泊松比 [Dargahizarandi 2025, pp. 9-12]。
    *   **超声波结果验证**: 沿不同角度钻取样本进行弹性极限内的单轴压缩，测量杨氏模量，并将其方向性变化与超声波波速的方向性变化进行对比验证。波速最低的方向应对应杨氏模量最小的方向 [Dargahizarandi 2025, pp. 9-12]。
    *   **设备详情**: 激光扫描设备包含一个光学千分尺，该千分尺使用发光二极管发射均匀平行光。超声波测量使用了 Olympus 2022 示波器和 Olympus 5077PR 脉冲收发器 [Dargahizarandi 2025, pp. 9-12]。

## Key Findings
1.  提出的综合方法能够成功地从岩芯样本中测定完整的三维地应力状态，包括大小、方位角和倾角 [Dargahizarandi 2025, pp. 1-2]。
2.  该方法的经济性和可靠性通过对澳大利亚某地下金属矿的八块岩芯的分析，并与现场测量结果进行比较，得到了验证 [Dargahizarandi 2025, pp. 1-2]。未从索引片段中确认与现场测量对比的具体结果与误差分析。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| DCDA可测量岩心膨胀后直径变化，确定最大/最小水平主应力方位角。Dmax沿σH方向，Dmin沿σh方向。 | [Dargahizarandi 2025, pp. 4-6] | 假设岩心从受σH和σh压缩的岩体中钻取，发生弹性膨胀。 | 此为该方法的物理基础。 |
| 超声波纵波（P波）在各向异性介质中传播速度不同。在最大主应力方向，因微裂隙张开，波速最低；在最小主应力方向，波速最高。 | [Dargahizarandi 2025, pp. 6-8, 12-13] | 假设地应力释放产生的微裂隙是导致声波各向异性的主因；若P波速度变化模式不符合预期，则各向异性可能来自岩性变化等因素。 | 此为该方法的物理基础。 |
| 岩心直径测量使用了配备LED均匀平行光的光学千分尺。 | [Dargahizarandi 2025, pp. 12-13] | 实验室环境，用于扫描岩心圆周方向直径。 | 提供了方法实现的一个设备细节。 |
| 弹性模量和泊松比通过单轴压缩实验测定，使用了轴向应变片 (TML PFL-10-11-3LJCT-F) 和环向引伸计 (Epsilon 3544)。 | [Dargahizarandi 2025, pp. 9-12] | 在岩心均质部分进行，以获取局部准确应变。 | 实验参数部分来源于此。 |
| 研究地点为澳大利亚昆士兰州的Dugald River锌-铅-银矿。 | [Dargahizarandi 2025, pp. 8-9] | 验证数据来源于该矿的两个垂直钻孔。 | 明确了验证案例的位置与矿种。 |

## Limitations
*   原始的DCDA方法只能估算二维应力状态，无法直接得到全三维应力 [Dargahizarandi 2025, pp. 1-2]。
*   核心法（包括基于Kaiser效应的声发射法等）普遍被认为可靠性不足，因为将实验室数据与现场应力状态联系时存在高度不确定性，导致其得到的应力方向常与现场套芯法不一致 [Dargahizarandi 2025, pp. 3-4]。
*   未从索引片段中确认该新方法在不同岩性、深度或高应力各向异性条件下的适用性，也未提及方法的测量误差和不确定度量化。

## Assumptions / Conditions
*   **力学假设**：岩心从地应力环境中释放后的变形是线弹性的，符合胡克定律。计算过程中，由于研究中主应力方向近乎垂直，忽略了垂直应力对直径变化的贡献，直接使用了简化的二维公式 [Dargahizarandi 2025, pp. 8-9]。
*   **几何假设**：岩心样本被假设为均质、各向同性的材料，因此应变在整个样品中均匀分布 [Dargahizarandi 2025, pp. 9-12]。
*   **实验前提**：超声波测量中观察到的速度各向异性主要由地应力释放产生的微裂隙造成。如果结果不符合预期（即图3中的模式），则各向异性归因于岩性等其他未从索引片段中确认的参数 [Dargahizarandi 2025, pp. 12-13]。
*   **应力状态前提**：虽然提出了包含垂直应力影响的通用公式（公式5, 6, 7, 8），但在本验证案例中假设了其中一个主应力近似垂直，从而可以使用简化公式（公式2-4） [Dargahizarandi 2025, pp. 8-9]。

## Key Variables / Parameters
*   **σ_H, σ_h, σ_v**: 最大水平主应力，最小水平主应力，垂直主应力 [Dargahizarandi 2025, pp. 4-6, 8-9]。
*   **d_max, d_min, d_0**: 岩心最大膨胀直径，最小膨胀直径，岩心的原始未变形直径 [Dargahizarandi 2025, pp. 4-6, 8-9]。
*   **E, ν**: 杨氏模量，泊松比 [Dargahizarandi 2025, pp. 8-12]。
*   **P波到达时间/速度**: 超声波测量中的核心观测量，用于确定倾角 [Dargahizarandi 2025, pp. 6-8]。

## Reusable Claims
*   **Claim 1**: 根据DCDA原理，从深部地应力环境中取出的岩心，其截面会在最大水平主应力方向上发生更大的弹性膨胀，导致圆形截面变为椭圆形，因此测量各方向的直径可以确定水平主应力的方位 [Dargahizarandi 2025, pp. 4-6]。适用条件为岩心表现为弹性膨胀。
*   **Claim 2**: 超声波纵波穿过地应力释放后的岩心时会出现速度各向异性。对于最大主应力，由于其方向上膨胀最显著、微裂隙最发育，波速最慢（到达时间最长）；反之，对于最小主应力，波速最快（到达时间最短）。这一关系可用于确定主应力的倾角 [Dargahizarandi 2025, pp. 6-8]。该声学行为的适用性取决于地应力释放是产生波速各向异性的主导因素 [Dargahizarandi 2025, pp. 12-13]。

## Candidate Concepts
*   [[地应力场 (In-situ Stress Field)]]
*   [[岩芯法 (Core-based Stress Measurement)]]
*   [[直径变形分析 (Diametrical Core Deformation Analysis)]]
*   [[超声波应力测量 (Ultrasonic Stress Measurement)]]
*   [[三大主应力 (Principal Stresses S1 S2 S3)]]
*   [[应力各向异性 (Stress Anisotropy)]]
*   [[微裂隙 (Microcracks)]]
*   [[声波速度各向异性 (Acoustic Velocity Anisotropy)]]

## Candidate Methods
*   [[水压致裂法 (Hydraulic Fracturing)]]
*   [[套芯法 (Overcoring)]]
*   [[钻孔崩落分析 (Borehole Breakout Analysis)]]
*   [[声发射Kaiser效应法 (Acoustic Emission Kaiser Effect Method)]]
*   [[单轴抗压强度试验 (Uniaxial Compressive Strength Test)]]
*   [[弹性波理论 (Elastic Wave Theory)]]

## Connections To Other Work
*   该方法直接建立在Funato & Ito (2017) 提出的DCDA方法之上，旨在解决DCDA只能测二维应力的局限 [Dargahizarandi 2025, pp. 1-2]。
*   文中提到之前的岩心法（包括声发射法）结果与现场套芯法测量结果常不一致，指出岩心法普遍面临的可靠性挑战 [Dargahizarandi 2025, pp. 3-4]。
*   从主题上，该方法可连接到所有涉及通过岩芯应力释放效应（如应变恢复法、声学各向异性法）估算地应力的研究，但这些具体关联未从片段中得到确认。

## Open Questions
*   该方法在不同地质条件（如高度各向异性岩石、高地应力非弹性变形区）下的普适性如何？未从索引片段中确认。
*   与现场应力测量方法（如套芯法）进行对比验证的结果细节和量化误差是多少？索引片段只提到进行了比较，但未给出具体数据。
*   如果岩心膨胀不遵循线性弹性，或者初始截面并非理想圆形，该方法将如何修正？

## Source Coverage
本页内容基于提供的14个论文索引片段。片段覆盖了论文的摘要、引言、方法原理、样品制备、实验装置和部分分析过程。覆盖偏向于方法论和实验设计，对现场验证结果（片段仅在引言中提及，未展示具体对比图表和数据）和分析讨论（如新解析技术的详细推导和鲁棒性评估）部分覆盖不完整。研究区域的具体地质背景、所有核心样本的完整应力测量结果、误差分析以及更深入的讨论部分可能缺失。
