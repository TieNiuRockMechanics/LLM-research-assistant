---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2015-lei-a-new-approach-to-upscaling-fracture-network-models-while-preserving-geostatistical-and"
title: "A New Approach to Upscaling Fracture Network Models While Preserving Geostatistical and Geomechanical Characteristics."
status: "draft"
source_pdf: "data/papers/2015 - A new approach to upscaling fracture network models while preserving geostatistical and geomechanical characteristics.pdf"
collections:
citation: "Lei, Qinghua, et al. \"A New Approach to Upscaling Fracture Network Models While Preserving Geostatistical and Geomechanical Characteristics.\" *Journal of Geophysical Research: Solid Earth*, vol. 120, 2015, pp. 4784–, doi:10.1002/2014JB011736."
indexed_texts: "22"
indexed_chars: "107132"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T19:13:15"
---

# A New Approach to Upscaling Fracture Network Models While Preserving Geostatistical and Geomechanical Characteristics.

## One-line Summary

提出一种新型裂缝网络升级方法，通过在递归自引用晶格中进行离散时间随机游走，将小尺度裂缝模式放大至更大规模，同时保留其地质统计与地质力学特征 [Lei 2015, pp. 1-1]。

## Research Question

如何将小尺度裂缝网络模型升级至更大尺度（1–100 m），同时保留裂缝模式的地质统计特征（如空间分布、长度、连通性）以及受地应力控制的地质力学特征（如法向与剪切位移、变孔径），并探究在此过程中渗透率的尺度变化规律与流态转变机制 [Lei 2015, pp. 1-2]？

## Study Area / Data

研究基于一个由石灰岩与几乎不透水页岩互层中的裂缝系统，该露头图像来源于构造伸展作用下形成的两套主要垂直方解石充填节理组（走向约100°和140°），受层理限制，并以非邻接关系相交 [Lei 2015, pp. 2-4]。分析区域为从露头图中提取的6 m × 6 m方形子区域，包含约1000条裂缝，同时选用一个2 m × 2 m的子域作为地质力学建模和升级的源区 [Lei 2015, pp. 4-5]。

## Methods

- **尺度特征表征**：利用分形几何（关联维数 \(D_c\)）评估裂缝空间分布，并采用幂律模型拟合裂缝长度分布和密度，校正截断与审查偏差 [Lei 2015, pp. 4-5]。
- **地质力学建模**：使用组合有限-离散单元法模型，对尺寸 \(L = 2\) m 的含裂缝岩石样本在原位应力下的响应进行模拟，以获取裂缝张开度和剪切位移的现实分布，并推导位移-长度相关性的应力依赖标度指数 [Lei 2015, pp. 6-7]。
- **升级算法开发**：提出一种离散时间随机游走方案，在递归自引用晶格中成核与传播裂缝。该方法通过优先度、弯曲度、拐点数量和片段数等统计量，复制源裂缝模式的地质统计和地质力学属性至最大54 m × 54 m 的大域 [Lei 2015, pp. 7-9]。
- **水力行为模拟**：对不同升级实现进行单相流模拟，以分析网络尺度增加时的渗透率标度趋势和流态从极管道化到弥散化的转变 [Lei 2015, pp. 1-1]。

## Key Findings

- 源裂缝模式显现非分形特征，分形维数 \(D \approx 2.0\)，表明其裂缝重心在二维空间均匀填充，但其长度分布遵循幂律，指数 \(a\) 在2到3之间，估算值约为2.37–2.45 [Lei 2015, pp. 4-5]。
- 裂缝连通性由幂律长度指数 \(a\) 和分形维数 \(D\) 的关系主导。当 \(a < D+1\) 且最小裂缝长度充分小时，系统连通性对最小长度不敏感，计算出的临界系统尺寸 \(L_c\) 约为0.80 m [Lei 2015, pp. 5-6]。
- 通过地质力学模拟，裂缝位移（张开度和剪切位移）与长度之间的标度关系受应力条件控制，而非仅遵循纯弹性的平方根规律 [Lei 2015, pp. 6-7]。
- 升级后的多尺度网络模型在液压模拟中展现出渗透率随尺度变化的不同趋势（增加、稳定或不增），并识别出一个过渡带，在此带内流态从极度沟道化向弥散流转变 [Lei 2015, pp. 1-1]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| \(D \approx 2.0\)，网络非分形 | [Lei 2015, pp. 4-5] | 基于6 m × 6 m露头模式的关联维数分析 | 重心在2D空间均匀填充 |
| 长度指数 \(a \approx 2.37\)–\(2.45\) | [Lei 2015, pp. 5-6] | 经过审查效应校正和系统尺寸校正的累积与密度分布 | 2 < a < 3 |
| 临界系统尺寸 \(L_c \approx 0.80\) m | [Lei 2015, pp. 5-6] | a>1, a≠D+1, 且最小裂缝长度充分小的条件下 | 基于逾渗理论计算 |
| 地质力学控制位移-长度标度关系 | [Lei 2015, pp. 6-7] | 在施加原位应力场的FEMDEM模型结果中 | 标度指数偏离0.5的弹性预测值 |
| 升级网络渗透率呈应力依赖的多趋势标度 | [Lei 2015, pp. 1-1] | 对不同地质力学场景的多尺度实现进行单相流模拟观察 | 趋势可增、稳、或降 |
| 存在流态过渡带 | [Lei 2015, pp. 1-1] | 随网络尺度增加，由液压模拟观察 | 从极管道化向弥散流转变 |

## Limitations

- 所用分析为二维，二维方法可能忽略重要的三维效应。论文在第6节讨论了潜在的3D影响，但未从索引片段中确认其具体分析结论 [Lei 2015, pp. 2-4]。
- 由于计算能力的限制，地质力学建模的源区尺寸较小（\(L = 2\) m），其代表性可能影响升级结果。未从索引片段中确认大尺寸模型的验证细节 [Lei 2015, pp. 4-5]。
- 所研究露头的裂缝是方解石充填的脉体，但本研究的裂缝张开度推导并未使用脉厚度，而是通过地质力学响应计算，这可能与实际导水裂缝不同 [Lei 2015, pp. 2-4]。
- 渗透率趋势可能与区域尺度（>100m）的复杂因素有关，但本研究范围限定于1–100 m尺度，无法外推 [Lei 2015, pp. 1-2]。

## Assumptions / Conditions

- **模型设定**：分析限定于原地尺度（1–100 m），流体运移由裂缝主导，特别适用于结晶岩 [Lei 2015, pp. 1-2]。
- **地质力学条件**：裂缝初始无剪切，其初始张开度先验地依据线性弹性断裂力学（LEFM）推导的平方根标度律分配，随后在原位应力作用下计算闭合、张开、剪切及剪胀效应 [Lei 2015, pp. 6-7]。
- **统计前提**：用于升级的随机游走过程假设源模式的统计特征（如间距分布、弯曲度）具有代表性，并可通过非参数Kolmogorov-Smirnov检验量化的概率密度函数进行复制 [Lei 2015, pp. 7-9]。

## Key Variables / Parameters

- **分形维数与幂律指数**：关联维数 \(D_c\)（及由此推定的分形维数 \(D\)），幂律长度指数 \(a\)，密度项 \(\alpha\)，用于表征源模式的几何和尺度特征 [Lei 2015, pp. 4-5]。
- **连通性参数**：裂缝密度 \(P_{21}\)，逾渗临界尺寸 \(L_c\)，用于评估网络连接程度 [Lei 2015, pp. 5-6]。
- **地质力学参数**：模式I断裂韧性 \(K_{Ic}\)，杨氏模量 \(E\)，泊松比 \(\upsilon\)，以及能量释放率 \(G\)，用于初始张开度模型。原位应力的大小和方向是控制位移分布的关键变量 [Lei 2015, pp. 6-7]。
- **升级算法变量**：优先度（由裂缝长度与源区尺寸之比定义），片段数，拐点数（ñ），曲率条件分布的标准差，这些是控制裂缝形态复制的关键统计量 [Lei 2015, pp. 7-9]。

## Reusable Claims

- **声明1**: 对于非分形（\(D \approx 2.0\)）但长度遵循幂律分布（\(2 < a < 3\)）的二维裂缝网络，若 \(a < D+1\) 且最小裂缝长度充分小，系统连通性对最小裂缝长度的敏感性低，此时逾渗阈值的临界系统尺寸 \(L_c\) 可由 \(a, D\) 和密度项 \(\alpha\) 确定。 [Lei 2015, pp. 5-6]
- **声明2**: 升级裂缝网络并模拟其液压行为时，仅使用几何统计或恒定/随机孔径不足以再现真实渗透率趋势，必须纳入基于地质力学模拟的、与应力和尺度相关的变孔径和位移分布，才能观察到渗透率随尺度增加、稳定或降低的多种可能趋势。 [Lei 2015, pp. 1-1, 6-7]
- **声明3**: 在结合地质力学约束进行网络升级时，基于线性弹性断裂力学的平方根位移-长度标度律（\(b_{max} \propto l^{0.5}\)）可作为初始条件，但网络在不同应力状态下的响应将使得最终位移-长度相关性偏离该理论值，因此升级算法需动态生成受应力影响的裂缝属性。 [Lei 2015, pp. 6-7]
- **声明4**: 采用递归自引用晶格中的离散时间随机游走方案，是一种可行的技术路径，可将小尺寸源模式中的裂缝非平面性、长裂缝贯穿机制、变孔径及应力依赖的位移-长度相关性保真地放大到大尺寸域中。 [Lei 2015, pp. 1-1, 7-9]

## Candidate Concepts

- [[Fracture Network Upscaling]]
- [[Discrete Fracture Network Flow Simulation]]
- [[Geostatistics of Fractures]]
- [[Fractal Geometry in Fracture Networks]]
- [[Percolation Threshold in Fractured Media]]
- [[Geomechanical Controls on Fracture Aperture]]
- [[Channeling vs. Distributed Flow]]

## Candidate Methods

- [[Correlation Dimension Analysis]]
- [[Power Law Fitting for Fracture Length Distribution]]
- [[Kaplan-Meier Censoring Correction]]
- [[Finite-Discrete Element Method for Fractured Rocks]]
- [[Discrete-Time Random Walk in Recursive Lattices]]
- [[Point Packing Process for Spatial Replication]]
- [[Bootstrapping Statistical Replication]]

## Connections To Other Work

未从索引片段中确认与其他已编号文献的直接对比或继承关系。本研究的背景讨论和引述中包含了可与以下主题连接的相关研究：
- 关于渗透率随尺度变化趋势的争论（增加、稳定、降低）直接引用了 Brace [1980， 1984]、Neuman [1994]、Clauser [1992]、Renshaw [1998] 等的研究，建立了问题设置的对比基础 [Lei 2015, pp. 1-2]。
- 本研究挑战了仅使用随机分形DFN且不考虑地力学约束的做法，引用了 de Dreuzy 等人 [2001a, 2001b, 2002]、Klimczak 等人 [2010]、Leung 和 Zimmerman [2012] 等的工作作为传统方法的参照 [Lei 2015, pp. 1-2]。
- 裂缝张开度的平方根模型与 Olson [2003]、Schultz 等人 [2008] 等的工作一致，但本工作强调了地应力对此关系的修正 [Lei 2015, pp. 6-7]。

## Open Questions

- 二维升级方法在三维裂缝网络中如何实现和验证？其三维几何和连通性效应如何影响渗透率标度？ [Lei 2015, pp. 2-4]
- 更大的计算能力是否允许更大的源区尺寸？源区尺寸的选择对该方法的升级保真度有何定量影响？未从索引片段中确认。
- 所识别的流态从沟道化到弥散化的过渡带，其具体控制参数和临界条件是什么？未从索引片段中确认。

## Source Coverage

本页依据22个索引片段生成。片段主要覆盖了论文的摘要、引言、研究区域与数据描述、方法详述（尺度表征、地质力学模型设置、升级算法核心逻辑）以及部分关键结果的定性描述。覆盖集中在前半部分的理论方法和技术实现，但对结果部分（特别是渗透率标度趋势和流态过渡的定量证据）、讨论部分和结论部分的信息缺失较多。因此，定量发现、模型验证和论文自我局限性的深层讨论可能不完整，仅能基于已有片段进行陈述。
