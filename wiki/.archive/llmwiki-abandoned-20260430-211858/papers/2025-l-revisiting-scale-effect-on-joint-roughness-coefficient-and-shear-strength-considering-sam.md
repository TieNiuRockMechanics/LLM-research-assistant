---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2025-l-revisiting-scale-effect-on-joint-roughness-coefficient-and-shear-strength-considering-sam"
title: "Revisiting Scale Effect on Joint Roughness Coefficient and Shear Strength Considering Sampling Methods and Geometric Characteristics."
status: "draft"
source_pdf: "data/papers/2025 - Revisiting scale effect on joint roughness coefficient and shear strength considering sampling methods and geometric characteristics.pdf"
collections:
  - "zotero new"
citation: "Lü, Qing, et al. \"Revisiting Scale Effect on Joint Roughness Coefficient and Shear Strength Considering Sampling Methods and Geometric Characteristics.\" *Journal of Rock Mechanics and Geotechnical Engineering*, 2025, doi:10.1016/j.jrmge.2024.05.045."
indexed_texts: "13"
indexed_chars: "61076"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T15:36:20"
---

# Revisiting Scale Effect on Joint Roughness Coefficient and Shear Strength Considering Sampling Methods and Geometric Characteristics.

## One-line Summary
本文旨在澄清节理粗糙度系数（JRC）与岩石节理剪切强度尺度效应机制的根本区别，指出JRC的尺度效应主要源于采样方法和几何特征，而剪切强度的尺度效应则主要受粗糙度中起伏度（waviness）分量的波长控制 [Qing 2025, pp. 1-1]。

## Research Question
- 岩石节理剪切强度的尺度效应是正、负还是不存在，学术界尚未达成共识，其机制仍不清晰 [Qing 2025, pp. 1-2]。
- JRC的尺度效应与剪切强度的尺度效应机制是否不同？ [Qing 2025, pp. 1-1, 2-4]
- 不同的采样方法以及节理粗糙度的几何特征（尤其是起伏度与不平整度分量）如何各自影响JRC与剪切强度的尺度效应？ [Qing 2025, pp. 1-1, 2-4]

## Study Area / Data
- **岩石样本**：取自中国浙江省杭州市转塘镇附近山区的三块花岗岩样本（样本A, B, C），岩石坚硬、完整、致密、微风化，表面相对粗糙 [Qing 2025, pp. 2-4]。
- **数据采集**：使用MetraSCAN 750 Elite 3D激光扫描仪采集岩石表面数据，最大扫描精度为0.025 mm [Qing 2025, pp. 2-4]。

## Methods
- **JRC表征**：选用四种代表性粗糙度参数来定量表征JRC，包括 $Z_2$、$R_p$、$\theta^*_{\max}/(C+1)$ 和 $\lambda$ [Qing 2025, pp. 4-4]。
- **传统窗口采样法**：评估其在表征JRC尺度效应时的局限性 [Qing 2025, pp. 4-6]。
- **全文数据采样法**：为消除岩石表面非均质性影响，提出了一种利用所有可能的测量窗口来计算粗糙度参数平均值的全文数据采样方法 [Qing 2025, pp. 4-6]。
- **高斯滤波分离**：利用高斯滤波技术将节理粗糙度分离为起伏度（waviness）和不平整度（unevenness）两个分量，以研究其几何特征 [Qing 2025, pp. 8-9]。
- **数值直剪试验**：设计三组人工岩石节理（分别研究起伏度、不平整度、复合粗糙度对尺度效应的影响），进行数值模拟直剪试验，以揭示剪切强度的尺度效应机制 [Qing 2025, pp. 9-10]。

## Key Findings
- **JRC尺度效应来源**：JRC的尺度效应主要来源于采样方法和粗糙度参数的几何特征。传统窗口采样法未考虑岩石表面整体的非均质性，具有显著局限性 [Qing 2025, pp. 1-1, 4-6]。
- **剪切强度尺度效应机制**：剪切强度的尺度效应主要源于起伏度分量，而非不平整度分量。起伏度分量因其长波长特性，在不同采样位置和尺寸下表现出显著的几何差异；而不平整度分量的几何特征（如平均倾角、平均高度）在不同采样条件下保持相对恒定 [Qing 2025, pp. 8-9, 1-1]。
- **数值模拟验证**：
    - 起伏度分量的剪切强度表现出显著的尺度效应（不同尺寸、位置样本的剪切强度差异很大） [Qing 2025, pp. 9-10]。
    - 不平整度分量的剪切强度在不同样本间几乎不表现出尺度效应 [未从索引片段中确认具体数据，结论基于片段中对机制的描述]。
    - 粗糙度参数 $\lambda$ 虽然能反映起伏度波长的影响，但由于缺乏内在物理机制，无法解释在等比例放大或重复拼接节理等特殊条件下剪切强度无尺度效应的现象 [Qing 2025, pp. 6-8]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| JRC尺度效应主要源于采样方法和参数的几何特征 | [Qing 2025, pp. 1-1] | 基于花岗岩样本的数字提取与对比分析 | 区别于剪切强度的尺度效应机制 |
| 传统窗口采样法因忽略表面非均质性，在小窗口下获取代表性参数存在显著局限 | [Qing 2025, pp. 4-6] | 将样本划分为49个50mm×50mm区域，计算$Z_2$值分布观察到的强非均质性 | |
| 全文数据采样法通过移动窗口扫描整个表面并取均值，可获得更具代表性的粗糙度参数 | [Qing 2025, pp. 4-6] | 移动步长0.25mm，单个样本可生成1201×1201个采样窗口 | |
| 分离出的起伏度与不平整度分量具有截然不同的几何特征：起伏度平均波长78.8mm，不平整度平均波长7.6mm，不平整度平均高度仅~0.2mm | [Qing 2025, pp. 8-9, Table 2] | 基于花岗岩样本剖面，沿两个方向分析 | 起伏度平均倾角5.8°/6.3°，不平整度8.6°/8.5° |
| 剪切强度尺度效应主要来自起伏度分量，而非不平整度分量 | [Qing 2025, pp. 8-9] | 因不平整度分量波长极短，其几何特征在不同采样位置/尺寸下保持恒定 | |
| 数值试验中，起伏度分量的剪切强度表现出显著差异(200mm长样本W1=24.5 MPa，其组成部分100mm样本W2=19.4 MPa，W3=31.3 MPa)，验证了其对尺度效应的控制作用 | [Qing 2025, pp. 9-10] | 法向应力30MPa，人工节理由两个100mm波长、6°和18°倾角的起伏波构成 | |
| Barton经验模型预测值与标准JRC剖面数值模拟结果接近，方差约4%，验证了数值方法可行性 | [Qing 2025, pp. 9-10] | 数值模型采用平滑-塑性接触模型校准，未考虑粗糙度退化效应 | Fig. 16 |

## Limitations
- 数值剪切试验未考虑粗糙度在剪切过程中的退化效应（asperity degradation） [Qing 2025, pp. 9-10]。
- 对尺度效应机制的讨论和验证主要基于特定的花岗岩样本和人工生成的理想化节理剖面，结果的泛化能力有待评估 [Qing 2025, pp. 2-4, 9-10]。
- 研究主要通过数值模拟来验证剪切强度机制，物理直剪试验的验证情况未从索引片段中确认。
- 对于剪切强度呈“无尺度效应”或“正尺度效应”的特殊条件，本文仅指出了参数$\lambda$的解释局限，并未提出一个能统一解释所有现象的普适参数 [Qing 2025, pp. 6-8]。

## Assumptions / Conditions
- **JRC与粗糙度参数关系**：采用文献中已建立的$Z_2$、$R_p$、$\theta^*_{\max}/(C+1)$和$\lambda$这四个参数与JRC的回归关系式，假定这些关系适用于本研究的样本 [Qing 2025, pp. 4-4]。
- **全文数据采样法假设**：假定对整个表面所有窗口的粗糙度参数取均值，能够有效消除非均质性的影响，从而得到代表整个节理的参数值 [Qing 2025, pp. 4-6]。
- **高斯滤波分离假设**：假定通过高斯滤波可以将节理粗糙度有效地分离为宏观起伏度和微观不平整度两个分量 [Qing 2025, pp. 8-9]。
- **数值模型假设**：数值直剪试验采用校准至Barton经验模型的平滑-塑性接触模型，假定该模型能复现剪切行为，且模拟中未考虑粗糙度退化 [Qing 2025, pp. 9-10]。
- **几何特征与力学机制关联假设**：假定起伏度分量的长波长是控制剪切强度尺度效应的关键几何因素 [Qing 2025, pp. 8-9, 1-1]。

## Key Variables / Parameters
- **粗糙度参数**：$Z_2$（一阶导数均方根），$R_p$（粗糙度轮廓指数），$\theta^*_{\max}/(C+1)$（剪切方向上的平均视倾角），$\lambda$（方向性粗糙度参数） [Qing 2025, pp. 4-4]。
- **几何特征参数**：起伏度与不平整度分量的平均倾角、平均高度、平均波长 [Qing 2025, pp. 8-9, Table 2]。
- **力学参数**：节理壁单轴抗压强度（UCS）、基本摩擦角（$\phi_r$，索引中提及为公式中的$\phi_r$），用于Barton经验模型的JRC、JCS [Qing 2025, pp. 2-4, 9-10]。
- **采样方法变量**：采样窗口尺寸（50mm至350mm） [Qing 2025, pp. 4-6]。
- **数值剪切试验变量**：法向应力（数值试验中设定为30 MPa） [Qing 2025, pp. 9-10]。

## Reusable Claims
- **传统窗口采样法在评估节理粗糙度JRC时的代表性问题**：基于花岗岩点云数据，传统窗口采样法仅使用节理面中心区域计算粗糙度参数，由于岩石表面存在强烈非均质性，该方法在小窗口下获得的参数值缺乏对整个节理面的代表性 [Qing 2025, pp. 4-6]。
- **全文数据采样法提高参数代表性**：提出了一种全文数据采样法，通过以固定步长（0.25mm）滑动采样窗口遍历整个节理面，并计算所有窗口参数的平均值作为代表值。该方法通过利用全部数据并取平均，旨在消除表面非均质性对参数取值的影响 [Qing 2025, pp. 4-6]。
- **剪切强度尺度效应主控因素**：通过高斯滤波将节理粗糙度分离为起伏度（长波长）和不平整度（短波长）分量后，数值剪切试验表明，剪切强度的尺度效应主要源自起伏度分量的几何差异，而不平整度分量由于其短波长特性（如平均波长7.6mm，高度0.2mm），其力学响应在不同尺度下几乎不变 [Qing 2025, pp. 8-9, 9-10]。该项结论基于未考虑粗糙度退化的数值模拟 [Qing 2025, pp. 9-10]。
- **参数$\lambda$解释尺度效应的局限性**：粗糙度参数$\lambda$虽考虑了起伏高度和波长，能部分反映起伏度的影响，但因缺乏内在物理机制（如无法解释等比例放大节理无尺度效应的现象），不能完全替代对起伏度/不平整度分量的力学分析来准确描述剪切强度尺度效应 [Qing 2025, pp. 6-8]。

## Candidate Concepts
- [[Scale Effect]] (尺度效应)
- [[Joint Roughness Coefficient (JRC)]]
- [[Rock Joint Shear Strength]]
- [[Joint Roughness Heterogeneity]] (节理粗糙度非均质性)
- [[Waviness and Unevenness]] (起伏度与不平整度)
- [[Fractal Geometry of Rock Joints]] (岩石节理的分形几何)
- [[Self-affine Fractal]] (自仿射分形)

## Candidate Methods
- [[Full Data Sampling Method]] (全文数据采样法)
- [[Gaussian Filtering for Roughness Decomposition]] (高斯滤波粗糙度分离)
- [[Numerical Direct Shear Test]] (数值直剪试验)
- [[3D Laser Scanning for Rock Surface]] (岩石表面三维激光扫描)
- [[Barton's Empirical Shear Strength Model]] (Barton经验剪切强度模型)

## Connections To Other Work
- 本文采用Barton (1973)和Barton & Choubey (1977)提出的JRC-JCS经验模型作为剪切强度估算和数值模型校准的基础 [Qing 2025, pp. 1-2]。
- 引用了Bandis et al. (1981)关于“尺度效应在粗糙、起伏节理中更显著，而在平直节理中几乎不存在”的发现 [Qing 2025, pp. 1-2]。
- 提到了Leal-Gomes (2003)认为节理的匹配或错配程度可能是尺度效应差异的原因之一 [Qing 2025, pp. 1-2]。
- 阐述了参数$\lambda$无法解释Ueng et al. (2010)等人发现的“等比例放大或重复拼接的节理表面无剪切强度尺度效应”的现象 [Qing 2025, pp. 6-8]。
- 采用的全文数据采样法与Yong et al. (2019)和Du et al. (2022)采用的方法类似 [Qing 2025, pp. 4-6]。

## Open Questions
- 是否存在一个能统一解释剪切强度正、负、无尺度效应的普适性力学参数或模型？本研究指出了$\lambda$的局限，但未提出最终解决方案 [Qing 2025, pp. 6-8]。
- 考虑粗糙度退化的、更真实的数值模型和物理试验能否进一步验证本文提出的“起伏度主控剪切强度尺度效应”的机制？ [Qing 2025, pp. 9-10]
- 本文提出的分离起伏度与不平整度的滤波方法和阈值，在面对不同岩性、更大尺度范围的节理时是否具有普适性？未从索引片段中确认。
- 如何将基于二维剖面的起伏度/不平整度分析及其尺度效应机制，扩展到真实的三维节理面上？未从索引片段中确认。

## Source Coverage
- 本页依据了论文的13个索引片段，覆盖了摘要、引言、方法、部分结果（采样方法影响和起伏度/不平整度几何特征分析）和部分讨论/结论（数值模拟验证尺度效应机制）。
- **覆盖侧重**：索引片段高度集中于文章的核心创新点，即区分JRC与剪切强度的尺度效应机制、提出全文数据采样法、以及使用高斯滤波分离起伏/不平整度分量并进行数值验证。
- **可能缺失信息**：索引片段未覆盖正式结论（第6节）、对全文数据采样法在不同窗口尺寸下所得参数变化趋势的详细结果、数值模型校准的详细过程（如参数取值）、以及对研究局限性的完整讨论。引言的完整综述和参考文献列表也基本缺失。
