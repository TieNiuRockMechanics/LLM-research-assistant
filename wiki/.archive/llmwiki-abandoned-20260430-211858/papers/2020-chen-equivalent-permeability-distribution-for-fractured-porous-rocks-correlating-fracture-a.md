---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2020-chen-equivalent-permeability-distribution-for-fractured-porous-rocks-correlating-fracture-a"
title: "Equivalent Permeability Distribution for Fractured Porous Rocks: Correlating Fracture Aperture and Length."
status: "draft"
source_pdf: "data/papers/2020 - Equivalent Permeability Distribution for Fractured Porous Rocks Correlating Fracture Aperture and Length.pdf"
collections:
citation: "Chen, Tao. \"Equivalent Permeability Distribution for Fractured Porous Rocks: Correlating Fracture Aperture and Length.\" *Geofluids*, vol. 2020, 2020, article 8834666, 12 pp., doi:10.1155/2020/8834666."
indexed_texts: "11"
indexed_chars: "54860"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T00:25:17"
---

# Equivalent Permeability Distribution for Fractured Porous Rocks: Correlating Fracture Aperture and Length.

## One-line Summary

本研究定量分析了裂缝开度与长度相关关系（以相关指数 D 表征）对二维裂缝性多孔岩石等效渗透率空间分布的影响，发现该分布随 D 与裂缝几何参数发生规律性演变，并建立了平均无量纲渗透率与 D 之间的指数关系模型 [Chen 2020, pp. 1-2, pp. 5-7]。

## Research Question

如何定量描述裂缝开度-长度相关模型（由相关指数 D 控制）对裂缝性多孔岩石等效渗透率空间分布的影响？ [Chen 2020, pp. 1-2]

## Study Area / Data

本研究基于二维离散裂缝模型进行数值实验，不存在特定实地研究区。模型中的基质渗透率根据裂缝性油气藏的实际数据假定为 $k_m = 9.87 \times 10^{-16} \text{ m}^2$ (1 md) [Chen 2020, pp. 3-5]。裂缝开度 (w) 与长度 (l) 之间的幂律关系 $w = \gamma l^D$ 中的相关指数 D 在 0.5 至 1.0 之间变化，该关系广泛应用于现场尺度并被线性弹性断裂力学所推导 [Chen 2020, pp. 2-3]。研究考虑了不同的最小裂缝长度 (lmin) 和裂缝数量 (N) [Chen 2020, pp. 5-5]。

## Methods

研究采用了两步法 [Chen 2020, pp. 2-3]：
1.  **离散裂缝模型生成**：基于幂律关系 $w = \gamma l^D$ 生成具有不同相关指数 D（范围从0.5到1.0，步长为0.1）的二维离散裂缝模型。D=1.0 代表线性相关（如孤立脉体、恒定驱动应力），D=0.5 代表亚线性相关（如恒定断裂韧度）[Chen 2020, pp. 2-3]。
2.  **等效渗透率升尺度**：采用多重边界升尺度法计算网格块的等效渗透率张量。该方法通过应用多边界条件，根据达西定律反算渗透率张量分量 $k_{xx}, k_{yy}, k_{xy}$ [Chen 2020, pp. 3-5]。使用 MRST 代码求解裂缝和基质中的流动问题，流动基于质量守恒和达西定律，通过多相流逼近在裂缝-基质界面上耦合，并使用二维三角形网格(0.2 m)和一维线网格(0.1 m)进行离散化 [Chen 2020, pp. 3-5]。

## Key Findings

1.  **渗透率分布形态演变**：对角分量 $k_{xx}, k_{yy}$ 的分布形态随着相关指数 D、最小裂缝长度 lmin 和裂缝数量 N 的增加，从幂律分布，经过对数正态分布，最终演变为正态分布。这种转变部分归因于网格块内裂缝连通性的增加 [Chen 2020, pp. 5-5]。非对角分量 $k_{xy}$ 始终趋向于正态分布 [Chen 2020, pp. 5-5]。D 的增加会减慢这种从幂律到正态分布的演变过程 [Chen 2020, pp. 1-2]。
2.  **平均渗透率与 D 的关系**：等效裂缝模型的平均无量纲渗透率 $\bar{k}'$ 与相关指数 D 之间遵循指数关系：$\bar{k}' = A \cdot 10^{B \cdot D}$。其中，无量纲系数 A 和 B 分别处于 $10^{1.4}$ 至 $10^{2.4}$ 和 3.4 至 4.3 的范围内 [Chen 2020, pp. 5-7]。该指数模型也适用于非对角分量的绝对值 $|k_{xy}|$ [Chen 2020, pp. 5-7]。
3.  **系数 B 的依赖性**：指数关系式中的系数 B 会随着最小裂缝长度 lmin 和裂缝数量 N 的增加而增大，而系数 A 没有表现出明显的变化规律 [Chen 2020, pp. 5-7]。
4.  **渗透率各向异性**：当 D 从 0.5 增加到 1.0 时，网格块的渗透率各向异性（由渗透率椭圆的长短轴之比 $k_{\text{max}}/k_{\text{min}}$ 表示）普遍增强 [Chen 2020, pp. 9-10]。
5.  **与先前研究一致**：该研究结果支持了前人关于不同开度模型对等效渗透率有重要影响的结论 [Chen 2020, pp. 7-9]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 对角等效渗透率分量 $k_{xx}, k_{yy}$ 分布随 D、lmin 和 N 的增加，从幂律分布演变为对数正态分布，最终趋于正态分布。 | [Chen 2020, pp. 5-5] | 二维离散裂缝模型，D=0.5~1.0，基质渗透率 $k_m = 1 \text{ md}$。 | 这一演变过程部分由裂缝连通性增强导致；D 的增加会使演变减速。 |
| 平均无量纲等效渗透率 $\bar{k}'$ 与相关指数 D 呈指数关系：$\bar{k}' = A \cdot 10^{B \cdot D}$。 | [Chen 2020, pp. 5-7] | 二维等效裂缝模型，多重边界升尺度法。 | 系数 A 在 $10^{1.4}$ 至 $10^{2.4}$ 之间，B 在 3.4 至 4.3 之间；此关系同样适用于非对角分量的绝对值。 |
| 指数模型中的系数 B 随 lmin 和 N 的增大而增大，而系数 A 变化不明显。 | [Chen 2020, pp. 5-7] | 二维等效裂缝模型，指数关系模型。 | 表明大规模和高密度的裂缝增加了渗透性和连通性。 |
| D 从 0.5 增至 1.0 时，各网格块的各向异性比 $k_{\text{max}}/k_{\text{min}}$ 总体增大。 | [Chen 2020, pp. 9-10] | 二维网格块，渗透率椭圆分析。 | 表明裂缝长度与开度相关性越强，等效渗透率各向异性越显著。 |

## Limitations

*   本研究基于二维离散裂缝模型，这是对真实三维情况的简化 [Chen 2020, pp. 9-10]。
*   裂缝开度不受力学性质和周围应力场的影响（未考虑本构模型），而实际中裂缝开度会因此变化 [Chen 2020, pp. 9-10]。研究未从索引片段中确认是否考虑了由于岩石基质渗透性导致的具体限制。
*   具体的离散裂缝模型实现次数未从索引片段中确认，但有提到“所有十次实现”用于生成某些统计曲线 [Chen 2020, pp. 5-5]。

## Assumptions / Conditions

*   **裂缝开度-长度关系**：假设裂缝开度与长度遵循幂律关系 $w = \gamma l^D$，该关系由线性弹性断裂力学推导并广泛应用于现场尺度 [Chen 2020, pp. 2-3]。
*   **基质渗透率**：岩石基质渗透率假设为恒定值 $k_m = 9.87 \times 10^{-16} \text{ m}^2$ (1 md)，该值参考了裂缝性油气藏的实际数据 [Chen 2020, pp. 3-5]。
*   **裂缝渗透率**：裂缝渗透率通过立方定律 $k_f = w^2/12$ 根据其开度计算得出 [Chen 2020, pp. 3-5]。
*   **升尺度方法**：采用多重边界升尺度法计算等效渗透率张量，并对非对角分量进行平均以获得对称渗透率张量 [Chen 2020, pp. 3-5]。

## Key Variables / Parameters

*   `D`：裂缝开度-长度相关指数，取值范围 0.5~1.0，代表岩石的不同地质力学性质 [Chen 2020, pp. 1-2, pp. 2-3]。
*   `w`：裂缝开度 [Chen 2020, pp. 2-3]。
*   `l`：裂缝长度 [Chen 2020, pp. 2-3]。
*   `lmin`：最小裂缝长度 [Chen 2020, pp. 1-2, pp. 5-5]。
*   `N`：裂缝数量 [Chen 2020, pp. 1-2, pp. 5-5]。
*   `k_{xx}, k_{yy}, k_{xy}`：二维等效渗透率张量的分量 [Chen 2020, pp. 3-5, pp. 5-5]。
*   `k'`：无量纲平均等效渗透率 [Chen 2020, pp. 5-7]。
*   `A`, `B`：描述 $\bar{k}'$ 与 `D` 指数关系的系数 [Chen 2020, pp. 5-7]。

## Reusable Claims

*   Claim 1：在对裂缝性多孔岩石进行升尺度时，其网格块的等效渗透率张量对角分量 $(k_{xx}, k_{yy})$ 的统计分布形态会随着裂缝长度-开度相关指数 $(D)$ 的增大，从幂律型向对数正态型再向正态型演变，且该演变过程会因 D 的增大而减缓。[Chen 2020, pp. 1-2, pp. 5-5] (条件：二维离散裂缝网络模型，D 在 0.5 至 1.0 之间，基质渗透率为 1 md)
*   Claim 2：存在一个指数模型 $\bar{k}' = A \cdot 10^{B \cdot D}$ 可以有效描述等效裂缝模型的平均无量纲等效渗透率 $(\bar{k}')$ 与裂缝开度-长度相关指数 $(D)$ 之间的关系。[Chen 2020, pp. 5-7] (条件：二维等效裂缝模型，多重边界升尺度法，D 范围 0.5-1.0)
*   Claim 3：对于使用幂律开度-长度关系的裂缝网络，裂缝长度-开度相关性越强（即 D 值越大），生成的等效渗透率场的各向异性程度越高。[Chen 2020, pp. 9-10] (条件：对比 D 从 0.5 到 1.0 的情况)
*   Claim 4：平均无量纲等效渗透率公式 $\bar{k}' = A \cdot 10^{B \cdot D}$ 中的系数 B 会随裂缝几何参数（如最小裂缝长度、裂缝数量）的增大而增大，而系数 A 对此不敏感。[Chen 2020, pp. 5-7] (局限性：这一趋势是基于观察，其通用性未从索引片段中确认)

## Candidate Concepts

*   [[equivalent permeability]]
*   [[fracture aperture]]
*   [[fracture length]]
*   [[correlation exponent]]
*   [[power law model]]
*   [[fractured porous rock]]
*   [[anisotropy ratio]]

## Candidate Methods

*   [[discrete fracture model]]
*   [[multiple boundary upscaling method]]
*   [[histogram fitting method]]
*   [[Spearman rank correlation]]
*   [[dimensionless analysis]]
*   [[MRST simulator]]

## Connections To Other Work

*   研究结果支持了 **Klimczak 等人 [27]**、**Leung 和 Zimmerman [28]** 以及 **Bisdom 等人 [35]** 的观点，他们都强调了不同开度模型（尤其是相关长度-开度关系）对等效渗透率有重要影响 [Chen 2020, pp. 7-9]。
*   与主要比较恒定开度和变化开度模型对单个网格块影响的 **Bisdom 等人 [35]** 工作不同，本研究重点在于相关开度-长度模型对整个模型区域等效渗透率**分布**的影响 [Chen 2020, pp. 9-10]。
*   渗透率对角分量呈幂律分布的发现，与三维低裂缝连通性裂缝性多孔岩石中的结果相似 [Chen 2020, pp. 5-5]。具体文献为 [54]，但其详细信息未从索引片段中确认。
*   研究中假设的对数正态渗透率分布常被用于实际油藏模型 [Chen 2020, pp. 5-5]，相关文献为 [55, 56]，但其详细信息未从索引片段中确认。

## Open Questions

*   在考虑裂缝开度受控于力学性质的本构模型（而非简单的幂律关系）时，等效渗透率分布将如何变化？[Chen 2020, pp. 9-10]
*   本研究的发现和方法在扩展到三维离散裂缝模型时是否依然成立？[Chen 2020, pp. 9-10] 对于三维模型，需要真实的裂缝几何数据和更高的计算能力。[Chen 2020, pp. 9-10]
*   裂缝之间具体的力学相互作用如何通过 D 值来定量表征，以及如何从实验室或现场数据中直接约束 D 值？[Chen 2020, pp. 2-3]

## Source Coverage

本知识页基于提供的 11 个索引片段构建。这些片段来自论文的引言（pp. 1-2）、方法（pp. 2-5）、结果（pp. 5-7, pp. 7-9）和讨论/结论（pp. 9-10）部分，覆盖了研究的核心内容。未覆盖的部分可能包括：更详细的文献综述、方法的具体数学推导、所有案例研究的完整数据集、对幂律模型系数更深入的物理解释讨论，以及结论部分未提供的部分。
