---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2019-sui-the-fractal-description-model-of-rock-fracture-networks-characterization"
title: "The Fractal Description Model of Rock Fracture Networks Characterization."
status: "draft"
source_pdf: "data/papers/2019 - The fractal description model of rock fracture networks characterization.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Sui, Lili, et al. \"The Fractal Description Model of Rock Fracture Networks Characterization.\" *Chaos, Solitons and Fractals*, vol. 129, 2019, pp. 71-76."
indexed_texts: "8"
indexed_chars: "37813"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T23:45:56"
---

# The Fractal Description Model of Rock Fracture Networks Characterization.

## One-line Summary
提出一种结合分形自相似性与头尾分割法（Head/Tail Break）的新型量化方法（SFI），以更准确、简便地表征岩石裂隙网络的复杂性和不规则性，并利用两个二维煤裂隙样本进行验证 [Sui 2019, pp. 1-2]。

## Research Question
如何克服传统几何学方法和现有分形方法（如计盒维数）在量化岩石裂隙网络时的局限性（如计算不稳定、依赖最小二乘回归带来的偏差），并提出一种能更准确、高效且简便地表征裂隙网络复杂性的新分形描述模型 [Sui 2019, pp. 1-2]？

## Study Area / Data
用于验证新方法的样本是两幅真实的二维煤裂隙图像 [Sui 2019, pp. 1-2]。未从索引片段中确认样本的具体地质来源或地理位置。

## Methods
1.  **传统方法评估**：系统回顾并分析了传统几何学方法 [Sui 2019, pp. 1-2]、分形几何方法以及图论方法在裂隙网络表征中的优缺点 [Sui 2019, pp. 1-2]。
2.  **新方法提出 (SFI)**：基于分形自相似性和头尾分割法（Head/Tail Break），提出一种新的分形量化指标 SFI（具体公式为 SFI = ln(N)/ln(r)，其中 N 和 r 基于头尾分割法对裂隙长度的分级计算得出）[Sui 2019, pp. 4-5]。该方法的核心是将研究对象（裂隙网络）按照头尾分割法进行分层，并保留“尾”部（即大量细小裂隙）进行分析，以代表整体特征并简化计算步骤 [Sui 2019, pp. 3-4]。
3.  **数据预处理**：使用嵌入在 ArcGIS 10.0 中的 Axwoman 程序对裂隙图像进行识别和长度分级。识别规则包括：优先识别更长的、更直接的裂隙（如将夹角小于45°的连接裂隙视为一条长裂隙）[Sui 2019, pp. 4-5]。

## Key Findings
1.  传统的单一几何参数不足以量化裂隙网络，分形维数被作为一种综合量化指标 [Sui 2019, pp. 2-3]。
2.  传统分形维数计算中，使用不同尺寸比例（ratio gaps）会导致结果不稳定，从而在工程应用中引入误差 [Sui 2019, pp. 1-2]。此外，最小二乘法的回归步骤存在偏差 [Sui 2019, pp. 3-4]。
3.  二维与三维分形维数之间的关系（如 Dd-1 = Dd - 1 或 Dd-1 = d - 1）具有不稳定性，且二维裂隙信息与三维裂隙信息之间的复杂关系仍有待验证 [Sui 2019, pp. 3-3]。
4.  仅有单一分形维数不足以描述裂隙网络的不同分形行为特性 [Sui 2019, pp. 3-3]。
5.  本文提出的基于头尾分割法的 SFI 方法避免了传统分形计算中的最小二乘回归步骤，能够提高计算精度，且与原始分形数学定义更为一致 [Sui 2019, pp. 3-4]。
6.  在两个二维煤裂隙样本上进行验证：图 (a) 的 SFI 值为 1.59，图 (b) 的 SFI 值为 1.60，SFI 的增大与其更复杂的分形特征相符，验证了方法的有效性、准确性和简便性 [Sui 2019, pp. 4-5]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 传统分形维数计算不稳定，使用不同尺寸比例（ratio gaps）结果差异大 | [Sui 2019, pp. 1-2] | 使用传统分形维数计算方法时 | 该不稳定性限制了其在工程预测和评估模型中的可靠应用。 |
| 二维与三维裂隙分形维数关系（Dd-1）不稳定，有时等于 Dd-1，有时等于 d-1 | [Sui 2019, pp. 3-3] | 依赖于长度分布指数 a | 这意味着通过二维剖面信息推测三维裂隙网络结构存在困难。 |
| 最小二乘法评估分形布朗运动的维数时存在局限性 | [Sui 2019, pp. 3-4] (引用自 Qiao et al., 2015 [13]) | 在回归计算求极限步骤中 | 这是本文提出新计算方法以避免回归步骤的依据之一。 |
| 提出了新量化指标 SFI，公式为 SFI = ln(N)/ln(r) | [Sui 2019, pp. 4-5] | 基于头尾分割法对裂隙长度进行分级后计算 | 该方法被证明更精确、简便。 |
| 样本图 (a) 的 SFI 值为 1.59，(b) 为 1.60 | [Sui 2019, pp. 4-5] | 裂隙在 ArcGIS 中的识别遵循特定规则（如优先识别长裂隙、裂隙夹角小于45°时视为连接） | 结果证实 SFI 值越大，裂隙网络越复杂。 |

## Limitations
1.  未从索引片段中确认该新方法在不同类型岩石、不同尺度或三维裂隙网络中的普适性。
2.  索引片段仅提及该方法避免了最小二乘回归的偏差，但未与其他分形维数计算方法（如计盒维数、频谱法）在其他复杂网络上的定量对比结果。
3.  方法验证仅基于两个二维煤裂隙样本，样本量有限 [Sui 2019, pp. 1-2]。
4.  二维裂隙信息与三维裂隙信息之间的复杂关系仍未解决，这限制了通过地表或剖面数据理解三维网络的能力 [Sui 2019, pp. 3-3]。

## Assumptions / Conditions
1.  岩石裂隙网络本身具有分形特征，即自相似性 [Sui 2019, pp. 2-3]。
2.  应用头尾分割法假设裂隙网络中，大量“尾部”的细小裂隙能够代表整体特征 [Sui 2019, pp. 3-4]。
3.  裂隙网络的识别依赖于 ArcGIS 和 Axwoman 程序的自动识别规则，例如，优先识别较长的直接裂隙，将小于45度夹角的连接裂隙视为同一条裂隙 [Sui 2019, pp. 4-5]。这些规则会影响后续的长度分级和 SFI 计算。
4.  SFI 计算中，对象“由一个无限数量（或大量）不同长度的部分组成” [Sui 2019, pp. 3-4] 时，符合该方法的特性。

## Key Variables / Parameters
*   **SFI**：新提出的分形量化指标，基于头尾分割法计算 [Sui 2019, pp. 4-5]。
*   **N 和 r**：在 SFI 计算（SFI = ln(N)/ln(r)）中，由头尾分割法得出的分级计数与长度比。例如，对图(a)，`N = 3020.36 / 21.99 / 44 = 3.12`，`r = 45.08 / 21.99 = 2.05` [Sui 2019, pp. 4-5]。
*   **头尾指数 (ht-index)**：头尾分割法迭代分割的次数，反映了数据空间层级结构的深度 [Sui 2019, pp. 3-4]。
*   **分形维数 (Fractal Dimension, D)**：传统方法中的核心量化指标，用于描述裂隙网络的复杂性 [Sui 2019, pp. 1-2]。
*   **裂隙几何参数**：如裂隙方位 (orientation)、倾斜角 (inclination angle)、长度 (length)、宽度 (width)、密度 (density) 等 [Sui 2019, pp. 2-3]。
*   **长度分布指数 (a)**：影响 2D-3D 分形维数关系的不稳定性 [Sui 2019, pp. 3-3]。

## Reusable Claims
*   **Claim 1**: 岩石裂隙网络具有不规则和碎片化的特征，传统欧几里得几何学难以描述，而分形几何学是一个有用的补充工具 [Sui 2019, pp. 2-3]。
*   **Claim 2**: 使用不同尺寸比例（ratio gaps）计算传统分形维数会导致结果不稳定，从而限制了其在工程实践中的可靠应用 [Sui 2019, pp. 1-2]。
*   **Claim 3**: 通过最小二乘回归求极限来计算分形维数会引入偏差 [Sui 2019, pp. 3-4]。
*   **Claim 4**: 二维裂隙信息（如露头或剖面）与三维裂隙网络结构之间存在复杂关系，目前尚未被完全探明，因此不能简单地通过一个固定函数关系由 2D 信息推断 3D 信息 [Sui 2019, pp. 3-3]。
*   **Claim 5**: 本文提出的方法通过保留头尾分割法中的“尾”部（即大量细小裂隙）进行分析，可以提高计算精度并简化步骤，使其更符合分形的原始数学定义 [Sui 2019, pp. 3-4]。

## Candidate Concepts
*   [[Fractal fracture networks]]
*   [[Fractal dimension]]
*   [[Head/Tail Break]]
*   [[Self-similarity]]
*   [[Rock fracture characterization]]
*   [[2D-3D fractal relationship]]
*   [[Box-counting method]]

## Candidate Methods
*   [[Head/Tail Break]]
*   [[ArcGIS with Axwoman]]
*   [[Fractal geometry methods]]
*   [[Traditional geometry methods for fractures]]
*   [[Multivariable regression analysis for fracture permeability]] [Sui 2019, pp. 3-3]

## Connections To Other Work
*   **传统几何学方法**：论文总结了传统几何学方法是描述裂隙网络特征的基础技术，任何其他量化方法都基于它们。单一的传统几何参数不足以用于裂隙量化 [Sui 2019, pp. 2-3]。
*   **分形几何学**：该工作建立在分形几何学在岩石裂隙表征的已有研究之上，引用了 Mandelbrot (1967) [30] 的开创性工作和 Barton [32] 关于二维天然裂隙分形测量的研究成果 [Sui 2019, pp. 2-3]。指出单一分形维数的不足，这与 Miller [46] 关于岩石裂隙表面不同分形维数值及其趋势变化的研究相关联 [Sui 2019, pp. 3-3]。
*   **2D-3D 分形关系**：讨论了 Darcel 等 [44] 和 Davy 等 [45] 关于分形裂隙网络的体视学分析，并指出 2D 与 3D 分形维数关系存在不稳定性，该复杂性关系“still to be identified” [Sui 2019, pp. 3-3]。
*   **裂隙网络综合量化**：连接到 Jafari 和 Babadagli [48] 的工作，他们使用非线性多变量回归分析（包含计盒维数、水力传导率等参数）来估算等效裂隙网络渗透率 [Sui 2019, pp. 3-3]。
*   **头尾分割法**：本研究的核心方法直接继承自 Jiang [51, 52] 的研究工作，该工作已成功应用了 ht-index [Sui 2019, pp. 3-4]。

## Open Questions
1.  这种基于头尾分割法的 SFI 新方法在三维天然裂隙网络中的适用性和准确性如何？
2.  二维裂隙分布信息与三维裂隙网络结构之间的定量关系究竟为何 [Sui 2019, pp. 3-3]？
3.  该新方法对于评估或预测裂隙岩石的物理力学性质（如渗透率、弹性模量）的有效性如何，能否建立类似 Jafari 和 Babadagli [48] 的预测方程 [Sui 2019, pp. 3-3]？
4.  未从索引片段中确认该方法与其他分形描述方法（如质量维数、扫描线维数）的定量比较研究。

## Source Coverage
本页面基于提供的 8 个索引片段编写，覆盖了该论文的摘要（Abstract）、引言（Introduction）、第 2-3 节的方法综述、第 4 节提出的新方法、第 5 节的部分案例应用以及结论。覆盖侧重于研究动机、方法原理对比和新方法的公式与计算步骤。然而，片段覆盖可能存在以下缺失：
*   **第 5 节案例应用**：对两幅煤裂隙图像的详细描述、更多验证细节和数据可能不完整。
*   **讨论部分**：可能存在的对方法更深入的讨论、与其他工作的对比分析未被收录。
*   **参考文献细节**：无法提供除片段中出现的作者和年份外的更多引用信息。
*   **图例和表格**：除 Fig. 4, 5 和 Table 2 的部分数据外，其他图表信息缺失。
