---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi"
title: "Mining-Induced Fracture Network Reconstruction and Anisotropic Mining-Enhanced Permeability Evaluation Using Fractal Theory."
status: "draft"
source_pdf: "data/papers/2025 - Mining-induced fracture network reconstruction and anisotropic mining-enhanced permeability evaluation using fractal theory.pdf"
collections:
  - "zotero new"
citation: "Zhu, Zeyu, et al. \"Mining-Induced Fracture Network Reconstruction and Anisotropic Mining-Enhanced Permeability Evaluation Using Fractal Theory.\" *Journal of Rock Mechanics and Geotechnical Engineering*, vol. 17, 2025, pp. 2256-75, https://doi.org/10.1016/j.jrmge.2024.05.039."
indexed_texts: "18"
indexed_chars: "87528"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T15:27:10"
---

# Mining-Induced Fracture Network Reconstruction and Anisotropic Mining-Enhanced Permeability Evaluation Using Fractal Theory.

## One-line Summary

本研究提出了一套从三维角度重建采动裂隙网络并基于分形理论评估各向异性采动增透率的方法，用于解决煤与瓦斯共采中的渗透性评价挑战。

## Research Question

如何从三维（3D）视角表示采动裂隙网络，并建立一个综合模型来评估各向异性的采动增透特性？[Zhu 2025, pp. 1-2]

## Study Area / Data

- **研究区域**：中国平顶山煤业集团十矿的 Ji14-31050 工作面。 [Zhu 2025, pp. 3-3]
- **数据来源**：在工作面前方煤层中进行的钻孔窥视现场实验，系统监测钻孔裂隙的演化。 [Zhu 2025, pp. 1-2] 测试数据包括了裂隙的产状（倾向、倾角）和间距等定量参数。 [Zhu 2025, pp. 3-3] 钻孔 C3, C4, C5, C7, C8 用于分析裂隙分形维度和连通性的演化。 [Zhu 2025, pp. 7-7]
- **仪器限制**：研究主要关注毫米级以上的宏观裂隙，忽略了微米级裂隙对气体流动的影响，因为钻孔成像仪仅能有效捕捉毫米级裂隙。 [Zhu 2025, pp. 5-5]

## Methods

1.  **现场监测与数据处理**：通过钻孔成像仪获取孔壁视频图像数据，导入 AutoCAD 软件进行矢量化，为后续定量分析奠定基础。 [Zhu 2025, pp. 3-3]
2.  **断裂特征定量分析**：
    *   利用**计盒维数法**（box-counting method）计算断裂的分形维数 (Fractal dimension, $D_B$)。 [Zhu 2025, pp. 5-7]
    *   利用沿钻孔深度方向投影的方法计算一维连通性 (1D connectivity, $\chi$)。 [Zhu 2025, pp. 5-7]
3.  **工程尺度三维裂隙网络重建**：
    *   处理流程：将裂隙产状数据导入 Dips 软件，基于极点聚类确定优势产状组和 Fisher 浓度参数。 [Zhu 2025, pp. 9-9]
    *   重建工具：利用基于 MATLAB 和蒙特卡洛方法的 **RJNS3D** (Rock Mass Joint Network Simulation 3D) 工具箱，生成工程尺度的三维裂隙网络。该技术基于相似椭圆法扩展。 [Zhu 2025, pp. 7-7][Zhu 2025, pp. 7-9]
4.  **渗透率增强评估模型**：基于分形理论，建立了采动引起的**渗透率增强率** (Permeability enhancement rate, PER) 评价模型。 [Zhu 2025, pp. 1-2]

## Key Findings

- **裂隙演化的分区特征**：随着工作面的推进，钻孔裂隙的分形维度和一维连通性呈现出三个典型的演化区。当工作面距监测钻孔超过 70 m 时，监测结果显示分形维度和连通性在特定演化规律内变化。 [Zhu 2025, pp. 7-7]
- **裂隙形态转变**：在采动影响下，采动裂隙经历从随机裂隙到离层裂隙，最终形成破碎区的渐进式转变。 [Zhu 2025, pp. 5-5]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 随着工作面推进，钻孔裂隙的分形维度和 ID 连通性呈现三个典型演化区。 | [Zhu 2025, pp. 7-7] | 数据来自钻孔 C3, C4, C5, C7, C8；当距工作面 >70 m 时，参数变化遵循特定模式。 | 该发现基于现场实验的定量监测数据。 |
| 采动裂隙在形态上呈现从随机裂隙 -> 离层裂隙 -> 破碎区的转化规律。 | [Zhu 2025, pp. 5-5] | 通过现场钻孔窥视图像分析得出。 | 揭示了采动应力作用下煤体破裂的宏观演化路径。 |

## Limitations

- **裂隙观测尺度**：用于数据采集的钻孔窥视仪器仅能捕捉到毫米级裂隙，因此研究忽略了微米级裂隙对气体流动的贡献。 [Zhu 2025, pp. 5-5]
- **数据基础**：每个钻孔内的裂隙数量有限，无法对裂隙间距的分布函数进行统计分析。 [Zhu 2025, pp. 9-9]
- **建模假设**：裂隙网络重建过程中，假设裂隙岩体属于均质区。 [Zhu 2025, pp. 9-9]

## Assumptions / Conditions

- **均质区假设**：为简化数据处理流程，在重建工程尺度三维裂隙网络时，假设裂隙岩体属于一个均质区 (homogeneous zone)。 [Zhu 2025, pp. 9-9]
- **裂隙分组**：根据裂隙极点聚类，将所有裂隙处理为一个优势组。 [Zhu 2025, pp. 9-9]
- **裂隙规模贡献**：模型建立在对毫米级宏观裂隙的分析之上，认为采矿活动导致的宏观裂隙是气体流动的主要通道，忽略了微米级裂隙的影响。 [Zhu 2025, pp. 5-5]

## Key Variables / Parameters

- **分形维数 (Fractal Dimension, $D_B$)**：通过计盒维数法计算，用于定量表征裂隙网络的复杂程度。 [Zhu 2025, pp. 5-7]
- **一维连通性 (1D Connectivity, $\chi$)**：通过投影法计算，用于评估裂隙在钻孔深度方向上的连通程度。 [Zhu 2025, pp. 5-7]
- **渗透率增强率 (Permeability Enhancement Rate, PER)**：本研究构建的核心评价模型，用于评估采动引起的各向异性渗透特性变化。 [Zhu 2025, pp. 1-2]
- **优势产状 (Dominant Orientation) 与 Fisher 浓度参数**：用于构建三维裂隙网络的统计参数，通过 Dips 软件分析获取。 [Zhu 2025, pp. 9-9]
- **裂隙间距 (Fracture Spacing)**：用于估算裂隙密度的关键参数。 [Zhu 2025, pp. 9-9]

## Reusable Claims

- **Claim 1**：采动煤体的宏观裂隙网络随工作面临近，其形态遵循“随机裂隙 → 离层裂隙 → 破碎区”的演化序列。此规律适用于强采动影响的煤岩体，但限于毫米尺度的宏观裂隙观测。 [Zhu 2025, pp. 5-5]
- **Claim 2**：通过对钻孔裂隙图像进行矢量化处理，并利用计盒维数法和投影法计算的分形维数 ($D_B$) 与一维连通性 ($\chi$)，可作为量化裂隙网络演化的有效指标。该方法的适用条件是可获取高分辨率钻孔孔壁图像。 [Zhu 2025, pp. 3-3][Zhu 2025, pp. 5-7]
- **Claim 3**：基于蒙特卡洛方法的 RJNS3D 工具箱，可以利用钻孔裂隙的统计参数（优势产状、密度等）重建工程尺度的三维非连续裂隙网络，前提是假设岩体为均质区且裂隙服从设定的统计分布。 [Zhu 2025, pp. 7-7][Zhu 2025, pp. 9-9]

## Candidate Concepts

- [[Fracture network reconstruction]]
- [[Anisotropic permeability]]
- [[Fractal Dimension]]
- [[Mining-induced fractures]]
- [[Rock mass joint networks]]
- [[3D DFN (Discrete Fracture Network)]]
- [[Coal seam gas extraction]]
- [[Borehole televiewer / imaging]]

## Candidate Methods

- [[Box-counting method]]
- [[Monte Carlo simulation]]
- [[RJNS3D (Rock Mass Joint Network Simulation 3D)]]
- [[Dips software for structural geology]]
- [[Fracture network connectivity calculation]]
- [[Borehole image vectorization]]

## Connections To Other Work

- **主题连接**：本研究与大量关于采动裂隙网络演化特性的研究紧密相连，引用如 Close (1993), Mathur et al. (2023), Lei et al. (2017) 等关于裂隙系统或开挖损伤区演化的描述。 [Zhu 2025, pp. 2-2]
- **渗透率模型连接**：研究提及前人关于煤岩渗透率模型的工作，如 Jia and Zou (2021) 的考虑应力状态和路径的模型，Li et al. (2022) 的煤渗透率模型，以及 Xie et al. (2020) 推导的多种增渗模型。 [Zhu 2025, pp. 2-3]
- **数值模拟连接**：研究建立在数值模拟评估裂隙网络渗透特性的基础上，引用如 Baghbanan and Jing (2008) 对 2D 裂隙网络各向异性渗透率的研究，以及 Miao et al. (2015a) 和 Liu et al. (2016) 利用分形理论对裂隙网络流量的评估。 [Zhu 2025, pp. 3-3]
- **具体技术连接**：使用的三维裂隙网络重建方法直接继承自张 (2011a, 2011b, 2011c) 提出的 RJNS3D 工具箱和 Jin (2014) 基于相似椭圆的扩展技术。 [Zhu 2025, pp. 7-7]

## Open Questions

- 未从索引片段中确认。
- （开放问题可从片段局限性推导：如何有效整合微米级裂隙对渗透率的贡献？如何在裂隙间距数据有限的情况下提高三维网络重建的准确性？）

## Source Coverage

本页面基于提供的 18 个索引片段编译而成。片段摘录覆盖了从摘要、引言、方法（现场测试、裂隙表征与网络重建）到部分结果的论文前半部分内容。片段对于**核心模型（渗透率增强率 PER 模型）的具体构建细节、验证过程、以及论文的完整讨论和结论部分覆盖较少**。关于“各向异性”评价是如何在 PER 模型中实现的，以及模型与应用效果相关的完整 Key Findings，在现有片段中无法充分确认。
