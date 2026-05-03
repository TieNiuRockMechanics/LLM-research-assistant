---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2009-iassonov-segmentation-of-x-ray-computed-tomography-images-of-porous-materials-a-crucial-ste"
title: "Segmentation of X-Ray Computed Tomography Images of Porous Materials: A Crucial Step for Characterization and Quantitative Analysis of Pore Structures."
status: "draft"
source_pdf: "data/papers/2009 - Segmentation of X-ray computed tomography images of porous materials A crucial step for characterization and quantitative analysis of pore structures.pdf"
collections:
  - "论文"
citation: "Iassonov, Pavel, et al. “Segmentation of X-Ray Computed Tomography Images of Porous Materials: A Crucial Step for Characterization and Quantitative Analysis of Pore Structures.” *Water Resources Research*, vol. 45, 2009, W09415, doi:10.1029/2009WR008087. Accessed 15 Sept. 2026."
indexed_texts: "17"
indexed_chars: "81537"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T13:05:11"
---

# Segmentation of X-Ray Computed Tomography Images of Porous Materials: A Crucial Step for Characterization and Quantitative Analysis of Pore Structures.

## One-line Summary

本文系统评估了多种全局与局部自适应图像分割方法在工业与同步辐射X射线CT孔隙介质图像中的适用性，并证实分割步骤是孔隙结构定量表征与流体动力学建模中最关键却相对滞后的环节。[Iassonov 2009, pp. 1-2]

## Research Question

如何选择和评估适用于天然及人造多孔材料X射线CT图像的图像分割（二值化）方法，以便为孔隙空间的定量表征与流体模拟提供可靠的离散化数据？[Iassonov 2009, pp. 1-2]

## Study Area / Data

研究涉及三类多孔材料样品，并使用两种不同源的X射线CT系统：
- **工业CT图像**：
  - 玻璃珠（Glass beads，3.5 mm粒径）：通过HYTEC FLASHCT系统扫描，8-bit灰度体积，体素分辨率110微米，尺寸820×820×1480体素。[Iassonov 2009, pp. 5-6]
  - 膨润土-砂混合物（Bentonite-sand mixtures，用于研究脱湿裂隙）：具体参数未从索引片段中确认。
  - 大孔隙壤土（Macroporous loam soil）：具体参数未从索引片段中确认。
- **同步辐射CT图像**：
  - 均匀玻璃珠样品（直径6.35 mm，高5.67 mm）：由Oregon State University的Dorthe Wildenschild提供。扫描分辨率5.9微米，能量水平33.3 keV，体积尺寸1300×1300×1300体素，其孔隙度通过计数、比重和精密玻璃珠质量独立测定。[Iassonov 2009, pp. 5-6]

## Methods

为评估不同分割算法的效果，研究采用了直接比较法，即将不同分割方法计算得到的图像衍生孔隙度（Image-derived Porosities）在彼此之间进行对比，并在可行时与物理实验直接测量的孔隙度（Directly Measured Porosities）进行对比。使用简单的体素计数算法来估计离散化三维样品体积的孔隙度（孔隙体素总数除以圆柱体三维样品体积的总体素数）。[Iassonov 2009, pp. 4-5]

测试的分割算法分为两大类：[Iassonov 2009, pp. 6-7]
1.  **全局阈值法 (Global Thresholding)**
    基于Sezgin与Sankur [2004]的综述进行选择。所有方法均产生一个“硬”阈值，用于分割整个X射线CT体积，其运算基于图像直方图分析。具体方法包括：
    - 手动全局阈值法 (Manual Global Thresholding)：基于二值图像与原始灰度图像二维切片间的主观视觉相似性来选择阈值。
    - 其他基于直方图的自动全局阈值技术：具体名称未从索引片段中确认，但指出其基于对图像直方图的分析。

2.  **局部自适应分割法 (Locally Adaptive Segmentation)**
    这类方法为每个体素独立做出分割决策，利用局部信息以提供更好的分割质量并校正部分图像伪影（如射束硬化、高频噪声），但计算需求更高。
    - **LA-Kriging**：由Oh和Lindquist [1999]开发的二阶段算法。第一阶段选定两个全局阈值（T0, T1）以划分明确的背景与前景体素；第二阶段，对灰度值介于T0和T1之间的未分类体素，利用以该体素为中心的小邻域（“克里金窗口”）内的平稳空间协方差，为每个体素独立计算最大似然估计，以完成分类。[Iassonov 2009, pp. 6-7]
    - 未从索引片段中确认其他局部自适应方法的具体名称。

## Key Findings

- **分割步骤至关重要**：图像分割是将灰度CT体积转换为离散形式以供后续定量分析（如孔隙度、比表面积、曲折度、网络结构）和流体分布、流动模拟的关键步骤，但其发展滞后于CT技术与模拟技术的发展。[Iassonov 2009, pp. 1-2]
- **不同方法导致巨大差异**：应用不同分割方法及相关的操作者偏差会导致孔隙度等结构特性计算结果差异巨大，这凸显了分割环节的重要性。[Iassonov 2009, pp. 1-2]
- **局部信息方法更优**：利用空间相关性等局部图像信息，以及应用局部自适应技术，能产生显著更优的分割结果。[Iassonov 2009, pp. 1-2]
- **手动分割不切实际**：对于具有复杂内部结构的天然多孔材料的CT图像，手动分割（“painting”）不切实际且极度耗时。即使是手动阈值法或简单的监督分割，也始终存在操作者偏差，且偏差与误差难以预测和校正。[Iassonov 2009, pp. 3-4]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 应用不同分割方法及操作者偏差得到的结果差异巨大，直接测量孔隙度与图像衍生孔隙度的对比证明了这一点。 | [Iassonov 2009, pp. 1-2] | 适用于工业与同步辐射X射线CT下的天然及人造多孔材料。 | 该证据奠定了全文的研究动机，即分割方法的选择对结果有决定性影响。 |
| 利用局部图像信息（如空间相关性）及局部自适应技术能产生显著更优的分割结果。 | [Iassonov 2009, pp. 1-2] | 适用于多种测试材料与CT系统。 | 相比于全局阈值法，局部方法在处理CT图像固有伪影和噪声方面具有优势。 |
| 手动分割（手动描绘）对于具有复杂内部结构的典型天然多孔材料不切实际，不可行。 | [Iassonov 2009, pp. 3-4] | 适用于包含高分辨率、典型天然多孔材料（CT体积可达10^10体素）复杂内部结构的情况。 | 这强调了开发无监督或最少监督分割算法的必要性。 |

## Limitations

- 尽管评估了多种分割算法，但本研究仅用“体素计数法估算的孔隙度”作为唯一的评价指标来比较各方法性能。对于其他重要孔隙结构参数（如比表面积、曲折度、孔径分布）的影响未从索引片段中确认。
- 测试的样品类型（玻璃珠、膨润土-砂混合物、大孔隙壤土）虽然具有代表性，但可能无法覆盖所有天然多孔介质的复杂性（例如含大量黏土矿物或有机物）。
- CT重建过程中本身可能存在误差和畸变，尤其是使用宽锥束几何的工业扫描仪产生的射束硬化效应，这些上游问题会影响所有下游分割方法的最终效果，但本分割研究对此的校正能力有限。[Iassonov 2009, pp. 2-2]
- 由于索引片段限制，未能确认所测试的全部局部自适应和全局阈值方法的完整列表及其各自的具体表现。

## Assumptions / Conditions

- **工作流假设**：假定从CT重建到定量分析的流程中，图像分割（二值化）是独立且最关键的步骤。所有的孔隙尺度参数计算和流体模拟都高度依赖于此步骤的输出质量。[Iassonov 2009, pp. 2-2]
- **评价标准假设**：假定物理实验直接测量的孔隙度是“金标准”，并将其作为评价图像分割方法性能的基准。[Iassonov 2009, pp. 4-5]
- **数据条件**：研究基于8-bit和未明确bit数（同步辐射）的灰度CT图像，图像中体素灰度值是区分固相与孔隙相的唯一信息源。[Iassonov 2009, pp. 5-6]
- **分割目标**：研究的核心目标是实现天然的、具有复杂结构的多孔材料图像分割自动化，并最大限度减少人工控制或监督。[Iassonov 2009, pp. 5-6]

## Key Variables / Parameters

- **图像衍生孔隙度 (Image-derived Porosity)**：通过体素计数法计算（孔隙体素数 / 总体素数），是评价分割效果的核心因变量。[Iassonov 2009, pp. 4-5]
- **直接测量孔隙度 (Directly Measured Porosity)**：作为基准值（Ground Truth），通过物理测量（计数、比重、质量）和几何测量（从垂直射线照片截面确定容器尺寸）得到。[Iassonov 2009, pp. 5-6]
- **灰度值 (Gray Scale Values)**：X射线CT图像的基本数据单元，是分割算法的唯一直接输入。
- **分割阈值 (Threshold Values)**：全局阈值法的核心控制参数。LA-Kriging方法中细化为T0和T1两个全局阈值，用于界定明确和未分类体素。[Iassonov 2009, pp. 6-7]
- **局部空间协方差 (Stationary Spatial Covariance)**：LA-Kriging方法中，用于对未分类体素进行最大似然估计的关键局部特征。[Iassonov 2009, pp. 6-7]
- **图像来源与分辨率**：作为潜在的影响变量被研究，包括工业CT（110微米）与同步辐射CT（5.9微米）。[Iassonov 2009, pp. 5-6]

## Reusable Claims

1.  在基于X射线CT的孔隙介质研究中，图像分割是将灰度图像转换为可用于定量表征与建模的离散相（二值）图像的**最关键步骤**。后续所有孔隙尺度参数（如孔隙度、比表面积、曲折度）的计算及流体动力学模拟均对其高度敏感。**适用条件**：该结论适用于需要从CT体数据中提取可量化孔隙结构的场景。**证据与限制**：不同分割方法得到的结果差异巨大 [Iassonov 2009, pp. 1-2]。该结论基于孔隙度这一指标的对比得出，是否对所有结构参数有同等程度的影响需进一步验证。
2.  **利用局部图像信息（如空间相关性）的局部自适应分割方法，在处理X射线CT图像时，其性能优于仅基于全局直方图分析的全局阈值法**。**适用条件**：尤其适用于需要考虑图像伪影（如射束硬化、高噪声）的天然多孔介质CT图像。**证据**：研究表明局部自适应技术产生了“显著更优的结果”（significantly better results）[Iassonov 2009, pp. 1-2]。**限制**：“显著更优”在此语境下主要以孔隙度估算准确度为基准，其计算成本远高于全局阈值法。
3.  **手动操作（无论是完全手绘还是手动选择阈值）是不一致、不可预测且带有操作者偏差的，不适用于复杂孔隙结构的可重复定量分析**。**适用条件**：任何需要客观、可重复性的科学或工程研究。**证据**：手动分割“总是有偏差”（always operator-biased），“偏差和可能的误差难以预测和校正”（difficult to predict and correct for）[Iassonov 2009, pp. 3-4]。

## Candidate Concepts

- [[Porous Media]] / [[X-ray Computed Tomography (X-ray CT)]]
- [[Image Segmentation]] / [[Binarization]] / [[Image Thresholding]]
- [[Pore Structure Characterization]] / [[Porosity]]
- [[Global Thresholding]] / [[Locally Adaptive Segmentation]] / [[LA-Kriging]]
- [[Operator Bias]] / [[Unsupervised Segmentation]]
- [[Beam Hardening]] / [[CT Image Artifacts]]
- [[Fluid Dynamics Modeling]] at pore scale

## Candidate Methods

- [[Local Adaptive Kriging (LA-Kriging) Segmentation]]
- [[Manual Global Thresholding]]
- [[Voxel Counting Method]] for porosity estimation
- [[Histogram-based Binarization]]
- [[Region Growing Methods]]（文中提及但为非重点评估方法）
- [[Deformable Surfaces / Level Set Methods]]（文中提及因计算量大、参数多而不太适合高分辨率天然介质CT）
- [[Image Preprocessing with Smoothing Filters]] / [[Postprocessing with Morphological Operations (Erosion/Dilation)]]

## Connections To Other Work

- **连接到图像分割综述**：本研究在选择全局阈值法时，直接参考了Sezgin和Sankur [2004]的综述。[Iassonov 2009, pp. 6-7]
- **连接到CT图像预处理**：文中提到CT图像分割前常用平滑滤波等预处理降噪，并引用了Kaestner等人 [2008] 的综述；同时指出不恰当的前后处理会降低分割质量。[Iassonov 2009, pp. 3-4]
- **连接到多相流研究**：文中指出图像二值化比对不同饱和度或不同能级下扫描图像的配准和相减分析至关重要，这与Wildenschild等人 [2002] 和 Schnaar与Brusseau [2005, 2006] 的研究相关。[Iassonov 2009, pp. 2-2]
- **连接到专用软件工具**：提及了数个应用于地质材料的图像分析软件及其内置的分割方法，包括 [[3DMA-Rock]]（具备手动阈值和两种局部自适应方法）、[[Blob3D]]（具备自适应区域生长算法）和 [[Mango]]。[Iassonov 2009, pp. 4-4]
- **连接到CT技术问题**：指出CT重建中的误差和畸变（尤其是工业扫描仪宽锥束几何导致的射束硬化）是普遍问题，关联到如Ketcham和Carlson [2001]的综述。[Iassonov 2009, pp. 2-2]

## Open Questions

- 如何发展计算效率高且完全无需人为监督的分割算法，以处理天然多孔材料日益增大的数据集？[Iassonov 2009, pp. 3-4]
- 除了孔隙度之外，分割方法的选择对于其他关键孔隙结构参数（如比表面积、曲折度、孔径分布）的具体量化影响有多大？这个问题未从索引片段中确认。
- 针对强烈受CT伪影（如射束硬化）影响的图像，开发能有效消除或校正这些伪影的集成化分割方案是否可能？[Iassonov 2009, pp. 2-2]
- 在LA-Kriging等利用空间相关性的方法之外，是否还能开发出更稳健地利用三维空间邻域信息的局部自适应方法？未从索引片段中确认。

## Source Coverage

本知识页基于该论文提供的17个索引片段编译而成。这些片段主要覆盖了论文的**引言 (Introduction)**、**方法概述 (Methods Overview)** 和**部分材料描述 (Materials)**。

- **覆盖部分**：研究动机与背景、分割重要性的论述、测试方法的分类与原则性介绍（全局阈值与局部自适应）、LA-Kriging方法的描述、实验样品与CT系统参数、以及用于评估的孔隙度比较策略。
- **潜在缺失信息**：
    - **结果 (Results)** 部分：所有全局与局部自适应方法的定量比较结果、图表数据未包含在片段中。
    - **讨论 (Discussion)** 部分：对导致方法性能差异的原因的深入分析未包含在内。
    - **结论 (Conclusions)** 部分：论文最终推荐的具体方法或算法，以及未来研究的明确指向可能不完整。
    - **完整方法列表**：除“LA-Kriging”和“手动全局阈值”外，其他所有被测试的全局和局部自适应方法的具体名称和原理细节在提供的片段中缺失。
