---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2013-lang-fractured-reservoir-modeling-method-based-on-discrete-fracture-network-model"
title: "Fractured Reservoir Modeling Method Based on Discrete Fracture Network Model."
status: "draft"
source_pdf: "data/papers/2013 - 基于DFN离散裂缝网络模型的裂缝性储层建模方法.pdf"
collections:
  - "大论文-离散裂缝网络"
citation: "Lang, Xiaoling, and Zhaojie Guo. \"Fractured Reservoir Modeling Method Based on Discrete Fracture Network Model.\" *Acta Scientiarum Naturalium Universitatis Pekinensis*, vol. 49, no. 6, Nov. 2013, pp. 964-966. doi:10.13209/j.0479-8023.2013.128. Accessed 2026."
indexed_texts: "3"
indexed_chars: "14439"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T18:45:48"
---

# Fractured Reservoir Modeling Method Based on Discrete Fracture Network Model.

## One-line Summary
提出了一种分大尺度和中小尺度、结合确定性与随机建模方法的DFN离散裂缝网络模型，以建立Z地区裂缝性储层的三维空间分布及属性模型 [Lang 2013, pp. 1-3]。

## Research Question
如何解决裂缝性储层建模中存在的多尺度描述困难及井间裂缝预测的不确定性问题 [Lang 2013, pp. 1-3]。

## Study Area / Data
*   **研究区**：Z地区奥陶系潜山裂缝性储层 [Lang 2013, pp. 3-7]。
*   **数据基础**：
    *   **地震资料**：三维地震数据，用于确定大尺度裂缝分布和构建预测属性体 [Lang 2013, pp. 1-3]。
    *   **岩芯资料**：用于识别中小尺度裂缝的密度、长度、倾角、方位、开度等 [Lang 2013, pp. 1-7]。
    *   **测井资料**：包括常规测井（如CAL, AC, DEN, RXO, RT）、地层倾角测井和FMI成像测井，用于解释裂缝孔隙度与裂缝密度 [Lang 2013, pp. 1-7]。
    *   **生产动态数据**：用于模型验证，部分井的日产油量（如Z10井和Z2井）及压力数据符合率达到94%以上 [Lang 2013, pp. 7-9]。

## Methods
1.  **三维构造建模**：基于断层棒、断层中心线和井点断点数据建立断层模型，并对地震解释层面进行井点校正，建立储层空间格架，并划分三维网格（50m × 50m × 1m） [Lang 2013, pp. 3-7]。
2.  **分尺度DFN离散裂缝网络建模** [Lang 2013, pp. 1-3]：
    *   **大尺度裂缝建模**：采用**确定性建模方法**，利用地震资料（如高分辨率本征相干体和蚂蚁追踪技术）识别和提取大尺度裂缝 [Lang 2013, pp. 3-7]。
    *   **中小尺度裂缝建模**：采用**随机建模方法**，以岩芯观测和成像测井统计的裂缝属性（密度、长度、倾角、方位等）为基础，以地震裂缝预测属性体为约束，建立裂缝密度三维分布模型，并据此生成中小尺度裂缝网络模型 [Lang 2013, pp. 1-7]。
    *   **关键中间步骤**：通过建立成像测井的裂缝密度与常规测井的裂缝孔隙度之间的关系，获取缺失成像资料井点的裂缝密度值 [Lang 2013, pp. 7-9]。
3.  **模型整合与粗化**：整合大尺度和中小尺度DFN模型，形成综合离散裂缝网络模型，并粗化得到裂缝孔隙度、渗透率等属性模型 [Lang 2013, pp. 1-3]。

## Key Findings
1.  通过分大尺度和中小尺度两个层次建立的DFN离散裂缝网络模型，可以实现对多尺度裂缝的模拟 [Lang 2013, pp. 7-9]。
2.  该建模方法实现了井间裂缝密度的约束，能够展现连续和离散的裂缝信息空间分布 [Lang 2013, pp. 7-9]。
3.  模型结果与已有钻井的裂缝储层动态（如日产油量变化、井间压力系统一致性）比较吻合，油藏数值模拟验证的年平均日产油量符合率在94%以上，证明模型比较符合真实情况 [Lang 2013, pp. 7-9]。
4.  建立了成像测井裂缝密度与常规测井裂缝孔隙度的关系，为缺失成像测井资料的区域提供了一种建立DFN模型的方法 [Lang 2013, pp. 7-9]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 研究区构造特点是西高东低，中部为局部隆起带，区块内被多条断层切割；Z10-3井3840m处泥浆漏失并见油气显示，岩芯证实该段裂缝发育，证明裂缝受断层控制 [Lang 2013, pp. 3-7]。 | [Lang 2013, pp. 3-7] | Z地区奥陶系潜山裂缝性储层 | 证据来自研究区地质资料和钻井实例。 |
| 通过建立成像测井裂缝密度与常规测井裂缝孔隙度之间的关系，可推算缺乏成像资料井点的裂缝密度 [Lang 2013, pp. 7-9]。 | [Lang 2013, pp. 7-9] | Z地区具有成像测井和常规测井的井 | 为在数据不足区域开展DFN建模提供了关键数据内部链接。 |
| 利用数值模拟验证模型，模型计算的年平均日产油量与实际值的拟合精度非常高，符合率在94%以上；采用Z10井区的实测数据进行定压生产，计算压力曲线与油藏历史值比较接近 [Lang 2013, pp. 7-9]。 | [Lang 2013, pp. 7-9] | Z10井区油藏 | 证据基于生产动态和压力历史数据。 |

## Limitations
1.  裂缝性建模研究本身是世界性难题，DFN模型是建立在裂缝属性统计分布假设基础上的理想简化，由于裂缝属性具有极强的非均质性，该方法描述裂缝仍然存在不确定性 [Lang 2013, pp. 7-9]。
2.  模型精度受地震资料品质的直接影响，地震储层预测精度的不高会降低井间离散裂缝建模的可靠性 [Lang 2013, pp. 7-9]。
3. 论文索引片段未提供常规测井裂缝孔隙度与成像测井裂缝密度间关系的具体数学表达式或相关系数。

## Assumptions / Conditions
- **模型前提**：假设裂缝属性（如密度、长度、倾角等）可以进行统计分析，并用于随机模拟 [Lang 2013, pp. 1-9]。
- **构造控制**：假定研究区的大尺度裂缝发育主要受断层控制，且裂缝发育程度与距断层面距离呈负相关 [Lang 2013, pp. 3-7]。
- **尺度划分**：假设可以将裂缝系统有效划分为大尺度和中小尺度两种级别，分别采用不同方法进行建模 [Lang 2013, pp. 1-3]。
- **数据关联**：假设成像测井解释的裂缝密度与常规测井计算的裂缝孔隙度之间存在可建立的关系，可以用于估算缺失数据点 [Lang 2013, pp. 7-9]。

## Key Variables / Parameters
*   **裂缝属性**：裂缝密度、长度、开度、倾角 (Dip)、方位 (Azimuth) [Lang 2013, pp. 1-7]。
*   **地震属性体**：高分辨率本征相干体、蚂蚁追踪体、裂缝与断层距离分析属性体 [Lang 2013, pp. 3-7]。
*   **常规测井曲线**：井径曲线 (CAL)、声波曲线 (AC)、密度 (DEN)、深浅双侧向电阻率 (RXO, RT) [Lang 2013, pp. 3-7]。
*   **网格参数**：平面网格间距50m × 50m，纵向网格间距1m [Lang 2013, pp. 3-7]。
*   **输出属性模型**：裂缝孔隙度、裂缝渗透率 [Lang 2013, pp. 1-3]。

## Reusable Claims
- **Claim 1**：在裂缝性储层建模中，采用分尺度建模策略是有效的：大尺度裂缝通过三维地震资料的确定性解释（如相干体、蚂蚁追踪）直接获取；中小尺度裂缝则以地震预测属性体为趋势约束，基于井点统计信息进行随机模拟。此策略适用于具有多尺度裂缝特征且拥有较好地震和井点数据基础的潜山或类似构造油藏 [Lang 2013, pp. 1-7]。
- **Claim 2**：当研究区内部分井缺失成像测井资料时，可以利用已有的成像测井解释裂缝密度与常规测井计算裂缝孔隙度建立统计关系，来推算缺失井点的裂缝密度。这项技术的适用条件是研究区已有足够数量的井同时具备两种测井数据，且两者之间的相关性显著 [Lang 2013, pp. 7-9]。
- **Claim 3**：模型的准确度验证需结合静态与动态数据。文中使用生产动态数据和油藏数值模拟进行验证，通过对比模拟与实际生产的日产油量及压力历史数据，可以获得定量的可信度评价（如符合率94%以上），此方法可作为裂缝模型结果验证的有效实践 [Lang 2013, pp. 7-9]。

## Candidate Concepts
*   [[fractured reservoir]]
*   [[discrete fracture network (DFN)]]
*   [[fracture density]]
*   [[multi-scale fracture modeling]]
*   [[seismic attribute analysis]]
*   [[fracture identification from well logs]]
*   [[reservoir numerical simulation]]

## Candidate Methods
*   [[deterministic fracture modeling]]
*   [[stochastic fracture modeling]]
*   [[ant tracking]] / [[ant tracking technology]]
*   [[seismic coherence cube]]
*   [[3D structural modeling]]
*   [[fracture porosity and permeability calculation]]
*   [[history matching for model validation]]

## Connections To Other Work
- 论文引用了多种储层建模方法研究的进展，包括地质统计学方法在裂缝网络建模中的应用，如“储层建模方法研究进展”、“整合多尺度信息的裂缝性储层建模方法探讨”等文献 [Lang 2013, pp. 7-9]。
- 模型构建中应用的裂缝检测技术（如蚂蚁追踪、本征相干体）与断层距离分析方法，是连接地震裂缝预测和地质建模的关键技术 [Lang 2013, pp. 3-9]。
- 可从主题上连接到裂缝建模的其他相关方法研究，如基于连续裂缝模型的建模方法、裂缝与流体流动模拟的结合。

## Open Questions
- 研究中仅提到建立成像测井裂缝密度与常规测井裂缝孔隙度的关系，但未给出关系的具体形式和精度，该经验关系在不同地区或储层的通用性如何？[Lang 2013, pp. 7-9]
- 论文强调地震储层预测精度直接影响模型精度，但未具体探讨不同品质地震资料下的模型不确定性量化问题 [Lang 2013, pp. 7-9]。
- 文中提出分大尺度和中小尺度两种级别建模，但未明确指出划分两个尺度的定量标准或阈值。

## Source Coverage
本页基于论文的3个索引片段生成，覆盖了摘要（页1-3）、方法（页3-7）以及部分结果和结论（页7-9）。信息全面，包含了研究框架、关键建模步骤、主要结论和模型验证。但是，论文中间结果（如图3、4）、初步分析过程和部分背景介绍在片段中不完整或缺失。关于模型构建的核心参数（裂缝距离分析属性体具体计算方法、裂缝密度与孔隙度的具体关系等）缺乏详细的数学描述。
