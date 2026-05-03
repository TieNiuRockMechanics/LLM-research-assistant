---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-guo-mechanical-properties-and-crack-propagation-behavior-of-granite-after-high-temperature"
title: "Mechanical Properties and Crack Propagation Behavior of Granite After High Temperature Treatment Based on a Thermo-Mechanical Grain-Based Model."
status: "draft"
source_pdf: "data/papers/2023 - Mechanical Properties and Crack Propagation Behavior of Granite After High Temperature Treatment Based on a Thermo-Mechanical Grain-Based Model.pdf"
collections:
  - "zotero new"
citation: "Guo, Pingye, et al. \"Mechanical Properties and Crack Propagation Behavior of Granite After High Temperature Treatment Based on a Thermo-Mechanical Grain-Based Model.\" *Rock Mechanics and Rock Engineering*, vol. 56, 2023, pp. 6411-6435. https://doi.org/10.1007/s00603-023-03408-x."
indexed_texts: "17"
indexed_chars: "80288"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T12:55:00"
---

# Mechanical Properties and Crack Propagation Behavior of Granite After High Temperature Treatment Based on a Thermo-Mechanical Grain-Based Model.

## One-line Summary

Guo 等人 (2023) 通过实验与考虑真实矿物分布的热-力颗粒模型 (TM-GBM) 模拟，揭示了花岗岩在高温处理后的力学性质劣化与裂纹扩展行为，并确定 450°C 为热损伤阈值 [Guo 2023, pp. 1-2]。

## Research Question

高温如何影响花岗岩的力学性质，特别是其内部热诱导微裂纹的萌生与扩展机制？能否建立一个考虑真实矿物分布的数值模型来重现这一过程，并确定其热损伤阈值？[Guo 2023, pp. 1-2]

## Study Area / Data

未从索引片段中确认实验材料的具体地质产区。研究采用的花岗岩主要矿物为长石 (65.22%)、石英 (32.45%) 与云母 (2.33%)，平均颗粒粒径约为 0.16 mm [Guo 2023, pp. 4-6]。实验采用尺寸为 Φ10 mm × 20 mm 的小型圆柱试样，通过 CT 扫描与光学显微镜观测高温处理后的内部结构 [Guo 2023, pp. 4-6]，并测量了不同温度后的 P 波速度、应力-应变曲线、峰值应力、峰值应变和弹性模量 [Guo 2023, pp. 6-7]。

## Methods

1.  **实验室实验**：将花岗岩试样分为五组，每组三个，加热至 150°C、300°C、450°C、600°C 和 750°C 等目标温度 [Guo 2023, pp. 6-7]。测量了高温处理前后的 P 波速度、单轴压缩下的应力-应变曲线、峰值应力、峰值应变和弹性模量。利用 CT 扫描系统和先进光学显微技术观测热诱导微裂纹的分布与形态 [Guo 2023, pp. 7-10]。
2.  **热-力颗粒模型 (TM-GBM)**：
    *   **模型生成**：结合 CT 技术和 GBM 建模方法，提出了一种反映矿物颗粒真实形状与分布特征的二维 TM-GBM [Guo 2023, pp. 10-11]。生成过程包括对 CT 重建图像进行矿物分割、边界矢量化，并将其导入颗粒流程序 (PFC) 以生成颗粒模型和 Voronoi 多边形，最终划分出代表不同矿物的区域 [Guo 2023, pp. 11-13]。模型总颗粒数为 27742 个 [Guo 2023, pp. 11-13]。
    *   **接触模型**：模型中同一矿物内部的接触采用线性平行黏结模型 (Pb)，而不同矿物之间以及同一矿物不同颗粒间的接触采用光滑节理模型 (Sj) [Guo 2023, pp. 11-13]。通过引入热力学计算来模拟热应力的产生与微裂纹的扩展。
3.  **热损伤评估**：基于弹性应变理论，定义了与弹性模量相关的热损伤因子 \( D_E = 1 - E_T/E_0 \) 和与 P 波速度相关的热损伤因子 \( D_V = 1 - (V_{PT}/V_{P0})^2 \)，用于定量评估损伤程度 [Guo 2023, pp. 10-11]。

## Key Findings

1.  **热损伤阈值**：450°C 是本研究花岗岩的热损伤阈值。当温度 \( T \leq 450\)°C 时，热诱导微裂纹发展不显著，P 波速度与力学性质劣化不明显；当 \( T > 450\)°C 时，微裂纹快速扩展，P 波速度与力学性质显著劣化 [Guo 2023, pp. 1-2]。
2.  **力学性质变化规律**：随热处理温度升高，峰值应力和弹性模量总体呈下降趋势，而峰值应变增加 [Guo 2023, pp. 7-10]。具体表现为：从室温至 450°C，力学性质仅轻微劣化（例如 450°C 时平均峰值应力相比室温下降 13.73% [Guo 2023, pp. 7-10]；而在 450°C 至 600°C 之间，力学性质急剧下降，例如 600°C 时平均峰值应力相比室温下降约 40% [Guo 2023, pp. 6-7]）。
3.  **热损伤因子**：由弹性模量和 P 波速度定义的热损伤因子 (\( D_E \), \( D_V \)) 均随温度升高而增加，其变化在 450°C 至 600°C 间最为显著 [Guo 2023, pp. 10-11]。
4.  **微裂纹演化机制**：热诱导微裂纹主要是在矿物边界处产生的拉伸裂纹，矿物颗粒间的热应力集中是其主要成因 [Guo 2023, pp. 1-2]。实验观察显示，450°C 时以石英-长石晶间开裂为主，这与石英较高的热膨胀系数导致边界处产生较大的局部热应力有关 [Guo 2023, pp. 7-10]。数值模拟也证实了热诱导微裂纹数量与温度呈正相关 [Guo 2023, pp. 1-2]。
5.  **模型有效性**：TM-GBM 能有效重现高温后花岗岩的力学行为、裂纹扩展过程及破坏模式，其合理性已通过实验验证 [Guo 2023, pp. 1-2]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 450°C 被确定为热损伤阈值 (\( T \leq 450\)°C 劣化不显著，\( T > 450\)°C 显著劣化) | [Guo 2023, pp. 1-2] | 研究对象为含特定矿物比例的花岗岩；Φ10mm × 20mm 试样 | |
| 450°C 后，P 波速度从 3556.67 m/s 急剧降至 600°C 时的 1448.33 m/s | [Guo 2023, pp. 6-7] | 基于 P 波速度测量 | 原文有前后文关联，需确认 3556.67 m/s 是否为室温初始值。 |
| 450°C 处理后的试样，平均峰值应力相比室温下降 13.73% | [Guo 2023, pp. 7-10] | 单轴压缩实验数据 | 室温参考峰值应力为 236.92 MPa |
| 600°C 和 750°C 处理后的试样，其弹性模量分别降至 12.79 GPa 和 9.38 GPa | [Guo 2023, pp. 7-10] | 单轴压缩实验数据 | 未从索引片段中确认室温弹性模量具体值 |
| 热损伤因子 \( D_E \) 和 \( D_V \) 的变化可用二次多项式拟合，相关系数 \( R^2 \) 分别为 0.84 和 0.92 | [Guo 2023, pp. 10-11] | 拟合公式参见原文 Eq.(3) 和 Eq.(4) | |
| 热诱导微裂纹主要为拉伸裂纹，主要位于矿物边界 | [Guo 2023, pp. 1-2] | 基于 TM-GBM 模拟结果 | |
| CT 图像显示，750°C 时局部形成贯穿整个切片的裂缝网络和断裂带 | [Guo 2023, pp. 7-10] | CT 扫描观测结果 | | 

## Limitations

*   数值模拟的 TM-GBM 模型为二维模型，可能无法完全捕捉真实三维空间中裂纹的复杂扩展路径 [Guo 2023, pp. 10-11]。
*   TM-GBM 模型的矿物含量与 CT 切片相比存在微小差异 [Guo 2023, pp. 11-13]。
*   实验采用小尺寸试样 (Φ10mm × 20mm)，其结果对更大尺度岩体的代表性可能存在局限。
*   索引片段未详细说明热处理的具体升降温速率及保温时间，这些因素可能影响热损伤结果。

## Assumptions / Conditions

*   **模型基本假设**: 岩石可被视为由不同矿物颗粒组成的离散集合体，其宏观力学响应由颗粒间接触的破坏决定。
*   **模型方法**: 采用线性平行黏结模型 (Pb) 模拟矿物内部的断裂，光滑节理模型 (Sj) 模拟晶界行为 [Guo 2023, pp. 11-13]。
*   **实验条件**: 加热实验在集成马弗炉中进行，目标温度分别为 150°C, 300°C, 450°C, 600°C, 750°C [Guo 2023, pp. 6-7]。CT 扫描分辨率为 5.65 µm [Guo 2023, pp. 4-6]。
*   **试样**: 试样矿物成分均匀，粒径 (0.16 mm) 远小于试样直径 (10 mm)，以保证代表性 [Guo 2023, pp. 4-6]。
*   **损伤理论**: 热损伤因子基于弹性应变理论定义，视弹性模量和 P 波速度的变化为材料内部损伤的直接表征 [Guo 2023, pp. 10-11]。

## Key Variables / Parameters

*   **独立变量**: 热处理温度 \( T \) (°C) [Guo 2023, pp. 6-7]。
*   **材料物理参数**: P 波速度 \( V_P \) (m/s) [Guo 2023, pp. 6-7], 密度 (未从索引片段中确认具体数值)
*   **力学参数**: 单轴抗压峰值应力 \( \sigma_c \) (MPa)，峰值应变 \( \varepsilon \)，弹性模量 \( E \) (GPa) [Guo 2023, pp. 7-10]。
*   **损伤参数**: 基于弹性模量的热损伤因子 \( D_E \)，基于 P 波速度的热损伤因子 \( D_V \) [Guo 2023, pp. 10-11]。
*   **模型参数**: 平行黏结模型 (Pb) 参数、光滑节理模型 (Sj) 参数、颗粒半径 (最小 0.2 mm，最大最小比 1.6)，矿物热力学参数 [Guo 2023, pp. 11-13]。
*   **微观参数**: 热诱导微裂纹数量、类型、位置 [Guo 2023, pp. 1-2]。

## Reusable Claims

*   **Claim 1**: 对于花岗岩这类由多种热膨胀系数不同的矿物组成的岩石，其在热处理温度低于某个阈值时，热诱导微裂纹发展不显著，力学性质变化不明显；但当超过该阈值（本文定为 450°C）后，微裂纹会快速扩展，导致 P 波速度和力学性质的急剧劣化 [Guo 2023, pp. 1-2]。**条件**: 矿物组成相似的花岗岩。**证据**: P 波速度、峰值应力、弹性模量在 450°C 前后的变化速率有显著差异。**限制**: 阈值温度依赖于具体的矿物成分和结构。
*   **Claim 2**: 高温下花岗岩的热损伤主要源于矿物颗粒间的非协调热膨胀。晶间热应力集中是形成以拉伸型为主的微裂纹的主要原因，尤其是在石英-长石边界 [Guo 2023, pp. 1-2, 7-10]。**条件**: 矿物颗粒间胶结良好。**证据**: 光学显微和 CT 观测结果显示裂纹优先在矿物边界萌生。
*   **Claim 3**: 利用 CT 扫描获取真实矿物图像并结合 GBM 方法建立的 TM-GBM，能够有效模拟高温后花岗岩的力学行为和热致裂纹的起裂与扩展过程 [Guo 2023, pp. 1-2, 10-11]。**条件**: 模型需根据实验数据进行标定。**证据**: 模拟结果与实验结果在力学性质和裂纹模式上有较好的一致性。

## Candidate Concepts

*   [[Thermal damage threshold]]
*   [[Thermally-induced microcrack]]
*   [[Grain-based model (GBM)]]
*   [[Thermo-mechanical grain-based model (TM-GBM)]]
*   [[P-wave velocity]]
*   [[Thermal damage factor]]
*   [[Intergranular cracking]]
*   [[Granite]]
*   [[Computed tomography (CT)]]
*   [[Smooth joint model]]
*   [[Linear parallel bond model]]
*   [[Thermal stress concentration]]

## Candidate Methods

*   [[Grain-based model in PFC]] [Guo 2023, pp. 11-13]
*   [[Computed tomography (CT) for mineral segmentation]] [Guo 2023, pp. 10-11]
*   [[P-wave velocity measurement for damage assessment]] [Guo 2023, pp. 6-7]
*   [[Uniaxial compression test after temperature treatment]] [Guo 2023, pp. 6-7]
*   [[Optical microscope observation of microcracks]] [Guo 2023, pp. 7-10]
*   [[Thermal damage variables defined by elastic modulus and P-wave velocity]] [Guo 2023, pp. 10-11]

## Connections To Other Work

*   本研究引用了前人关于高温花岗岩物理力学性质（如抗压强度、弹性模量）变化的实验研究 [Guo 2023, pp. 2-2]。
*   在数值模拟方面，本研究建立在先前使用 GBM 方法研究高温下岩石力学行为的工作基础之上，特别是针对热致裂纹的萌生与扩展 [Guo 2023, pp. 2-4]。与基于统计或 Voronoi 镶嵌法的 GBM 不同，本研究通过引入 CT 图像，实现了考虑真实矿物分布的建模方法 [Guo 2023, pp. 2-4]。
*   对于力学性质在 200°C 左右时增时降的矛盾现象，本文引用了 Isaka 等 (2019) 和 Shao 等 (2015) 的观点，认为这取决于矿物学、颗粒方向和纹理等 [Guo 2023, pp. 2-2]。

## Open Questions

*   二维 TM-GBM 模型能否可靠地推广到三维情况，以更精确地捕捉裂纹的扩展和贯通机制？
*   升降温速率和加熱程序（路径）对热损伤阈值和裂纹模式的具体影响是什么？
*   所确定的 450°C 阈值是否具有普适性，还是高度依赖于本研究中花岗岩的特定矿物组成和颗粒大小？
*   高温下的水-热-力多场耦合作用对裂纹扩展行为的影响有待研究。

## Source Coverage

本页内容基于论文提供的 17 个索引片段生成。索引片段覆盖了摘要、引言、实验方法、实验结果、数值模型构建等主要章节。其中，摘要 [Guo 2023, pp. 1-2]、部分引言 [Guo 2023, pp. 2-2, 2-4]、实验设计 [Guo 2023, pp. 4-6]、P 波速度与应力-应变曲线分析 [Guo 2023, pp. 6-7, 7-10]、热损伤评价 [Guo 2023, pp. 10-11] 以及 TM-GBM 模型生成细节 [Guo 2023, pp. 11-13] 均有涉及。但关于 **数值模型的参数标定过程、完整的模拟结果分析、讨论部分的详细内容** 以及**结论**的全面总结等信息，未从现有索引片段中确认。片段主要侧重于方法提出和实验结果验证。
