---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2019-zhang-microbial-community-composition-in-deep-subsurface-reservoir-fluids-reveals-natural-i"
title: "Microbial Community Composition in Deep‐Subsurface Reservoir Fluids Reveals Natural Interwell Connectivity."
status: "draft"
source_pdf: "data/papers/2020 - Microbial Community Composition in Deep-Subsurface Reservoir Fluids Reveals Natural Interwell Connectivity.pdf"
collections:
  - "part4-1"
citation: "Zhang, Yuran, et al. \"Microbial Community Composition in Deep‐Subsurface Reservoir Fluids Reveals Natural Interwell Connectivity.\" *Water Resources Research*, 2019, doi:10.1029/2019WR025916. Accessed 2026."
indexed_texts: "22"
indexed_chars: "109508"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T01:08:39"
---

# Microbial Community Composition in Deep‐Subsurface Reservoir Fluids Reveals Natural Interwell Connectivity.

## One-line Summary
该研究通过深部储层流体中微生物群落组成的高通量测序，识别了由天然裂缝引起的井间连通性，并在一个中尺度增强地热系统（EGS）试验场得到验证 [Zhang 2019, pp. 1-1]。

## Research Question
该研究旨在回答以下六个核心问题：1）深部地下流体中是否存在微生物群落？2）这些微生物群落是否随空间位置变化，其数据是否对储层表征有信息价值？3）来自同一裂缝或储层分区的流体样本应预期具有何种程度的群落相似性？4）利用微生物群落数据，能在多大程度上区分地层水和注入的水力压裂液或钻井液？5）微生物群落组成数据在区分不同来源流体时是否比地球化学数据更具信息性？6）环境微生物学家常用的采样规范是否适用于储层工程师常遇到的深层地下环境？[Zhang 2019, pp. 4-4]

## Study Area / Data
研究地点位于美国南达科他州利德市桑福德地下研究设施（Sanford Underground Research Facility, SURF）地下4,850英尺（1,478米）水平的中尺度增强地热系统（EGS Collab Phase 1）试验场。该试验场处于前寒武纪Poorman组千枚岩区，基质渗透率极低（<~10 nD），天然裂缝和劈理普遍发育，其中有限数量的开敞天然裂缝是流体流动的通道。试验场共有8口新鲜钻孔（采样时已钻成2天至3周），其中OT和PST钻孔显示自发性出水。除了试验场内的流体样本，还采集了该层位其他位置（相距10米至1.9公里）的流体以及矿用工业水（用于钻井液）进行分析 [Zhang 2019, pp. 4-6]。

## Methods
研究方法主要包括以下几个步骤：
1. **流体采样**：于2017年11月至2018年1月的钻井阶段，从EGS Collab的钻孔中采集地层流体样本。对于自发流动的钻孔，直接收集井口流体；对于无流动迹象的钻孔，则使用惰性塑料提桶（bailer）从井底采集流体。所有样本使用0.2微米滤膜进行过滤，以捕获并浓缩微生物细胞 [Zhang 2019, pp. 6-7]。
2. **DNA提取和测序**：对捕获的微生物进行高通量16S rRNA基因扩增子测序，以获得微生物群落谱。方法使用了两种引物对，其中515F-Y/926R为主要分析引物，部分与历史数据对比时采用了515F-C/806R引物子采样 [Zhang 2019, pp. 7-8]。
3. **生物信息学分析**：通过质量过滤后的序列生成ASV（Amplicon Sequence Variant）表，并进行物种分类学鉴定（域、门、纲、目、科、属）。基于所有序列构建系统发育树，并结合相对丰度数据，计算样本对之间的**加权UniFrac距离**，以量化群落间的相似性/差异性。该距离不仅考虑物种相对丰度，还考虑了系统发育关系 [Zhang 2019, pp. 7-8]。
4. **地球化学分析**：对流体样本的化学组成进行了分析，使用离子色谱（IC）、电感耦合等离子体质谱（ICP-MS）或电感耦合等离子体发射光谱（ICP-OES）测量元素浓度，以与微生物数据进行对比 [Zhang 2019, pp. 8-10]。

## Key Findings
1. **微生物群落的空间异质性与相似性**：整个研究地点空间分布（相距10米至1.9公里）的样本，其微生物群落谱通常表现出显著的异质性。然而，EGS试验场内两口井（OT和PST）产生的流体显示出高度相似的微生物群落组成，暗示这两口井贯穿了同一条天然裂缝，揭示了它们之间的井间连通性 [Zhang 2019, pp. 1-1]。
2. **连通性证据的验证**：基于微生物群落推断OT和PST井的自然连通性，后来被岩芯测井分析和钻孔内下水道摄像调查所证实 [Zhang 2019, pp. 1-1]。
3. **微生物群落作为诊断工具的优越性**：研究表明，微生物群落组成能够比地球化学数据更好地确定储层流体的身份/来源，具备作为一种天然示踪剂来精确指出流体起源的潜力 [Zhang 2019, pp. 1-2] [Zhang 2019, pp. 1-1 端]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| OT 和 PST 两口井的产出流体具有高度相似的微生物群落组成 | [Zhang 2019, pp. 1-1] | EGS Collab试验场，4,850英尺深，千枚岩基质，低渗透率，采样时仅完成钻井，未进行任何储层开发活动 | 该微生物指示的连通性被岩芯测井和下水道摄像调查所证实 |
| 整个研究区域空间分布样本（相距10米至1.9公里）的微生物群落谱通常存在显著异质性 | [Zhang 2019, pp. 1-1] | SURF 4,850层位的多个采样点 | 该对比突显了OT和PST井相似性的异常，增强了将其作为连通性证据的置信度 |
| 微生物群落组成在确定储层流体来源时比地球化学数据具有更好的特异性 | [Zhang 2019, pp. 1-2] | 基于本研究的数据对比 | 片段未提供具体的地球化学对比图表，仅给出结论性陈述 |

## Limitations
1. 未从索引片段中确认该方法的普适性是否在其他地质环境或深度条件下得到验证。研究是在一个具体的千枚岩地热储层中进行的。
2. 未从索引片段中确认用于区分注入液和地层水的具体效果数据，仅提及了该应用潜力 [Zhang 2019, pp. 2-4]。
3. 使用不同引物对进行测序会导致部分序列分类学精度降低，但在本研究中未影响beta多样性分析 [Zhang 2019, pp. 8-10]。
4. 微生物群落作为诊断工具的适用范围和局限性的详细边界条件，例如在特定温度、压力或地球化学条件下的有效性，未从索引片段中完全确认。

## Assumptions / Conditions
1. **微生物群落结构的相对稳定性**：假设在适应了当地环境条件后，每个隔离的地下环境中的微生物会形成随时间相对稳定的群落结构 [Zhang 2019, pp. 1-2]。
2. **环境隔离假设**：水力隔离的储层区域具有不同的物理化学条件（温度、压力、水化学、氧化态等），这些因素塑造了独特的微生物群落，从而作为每个环境的天然签名 [Zhang 2019, pp. 1-2]。
3. **低基质渗透率**：试验场所在的Poorman组基质渗透率极低（<~10 nD），流体流动主要通过天然裂缝，这是将流体中的微生物群落相似性归因于裂缝连通性的关键前提 [Zhang 2019, pp. 4-6]。
4. **采样状态**：所有样本在储层开发活动（如水力压裂）之前采集，避免了人为活动对原始地层流体微生物群落的干扰 [Zhang 2019, pp. 4-6]。

## Key Variables / Parameters
- **加权UniFrac距离（Weighted UniFrac Distance）**：核心指标，用于量化样本间微生物群落的相似性/差异性，整合了物种相对丰度和系统发育关系 [Zhang 2019, pp. 7-8]。
- **ASV（Amplicon Sequence Variant）相对丰度矩阵**：基础的微生物群落组成数据，展示每个样本中各分类单元的占比 [Zhang 2019, pp. 7-8]。
- **地球化学参数**：流体中的离子和元素浓度，用于与微生物数据的特异性对比 [Zhang 2019, pp. 8-10]。
- **序列读取数（Sequencing Reads）**：每个样本通过质量过滤的序列数（10,976至76,471条），表征了分析的深度 [Zhang 2019, pp. 8-10]。

## Reusable Claims
- **Claim 1**：在极低基质渗透率（<~10 nD）的裂缝性储层中，如果两口新鲜钻孔自产出流体的微生物群落加权UniFrac距离极低（即群落组成高度相似），可以推断这两口井贯穿了同一条天然裂缝，并具有水力连通性。该连通性可通过岩芯分析和钻孔摄像等方式进行独立验证。[[fracture reservoir]] [Zhang 2019, pp. 1-1] [Zhang 2019, pp. 1-2]
- **Claim 2**：即使是在空间距离较近（10米量级）的井之间，其深层地下流体的微生物群落也可能表现出显著差异，这反映了深层地下环境的高度异质性和水力隔离性。因此，群落的高度相似性并非空间邻近性的必然结果，而是连通性的特定指示。[[subsurface connectivity]] [Zhang 2019, pp. 1-1]
- **Claim 3**：微生物群落组成数据可作为区分不同来源储层流体的工具，其特异性优于传统的流体地球化学数据。这意味着在地球化学性质难以区分的流体中，微生物数据可能提供更精确的“源”信息。 [[microbial tracer]] [Zhang 2019, pp. 1-2]
- **Claim 4**：钻井作业过程中使用的工业水（外部水源）可能携带与地层水截然不同的微生物群落，通过对比群落数据，可以在产出流体中区分“返排”的注入/钻井水和新产出的“地层”水。[[flowback fluid]] [Zhang 2019, pp. 2-4]

## Candidate Concepts
- [[fracture reservoir]]
- [[enhanced geothermal system]]
- [[microbial community composition]]
- [[16S rRNA gene amplicon sequencing]]
- [[beta diversity]]
- [[biosignature]]
- [[subsurface microbiology]]
- [[natural tracer]]
- [[interwell connectivity]]

## Candidate Methods
- [[Weighted UniFrac distance calculation]]
- [[High-throughput DNA sequencing]]
- [[ASV (Amplicon Sequence Variant) analysis]]
- [[ICP-MS / ICP-OES geochemistry analysis]]
- [[Ion chromatography]]
- [[core log analysis]]
- [[borehole camera survey]]

## Connections To Other Work
- **连接到储层工程领域的工作**：索引片段指出，识别天然裂缝及其连通的井是储层模型构建和水力裂缝扩展模拟的关键需求 [Zhang 2019, pp. 1-1]。这直接关联到 [[Juliusson & Horne 2013]] 关于裂缝性储层建模中数据源探索的讨论，片段中明确引用了该研究。也关乎到 [[EGS Collab project]] （Kneafsey et al., 2018; White et al., 2019）的现场实验设计，本研究正是依托于此项目。
- **连接到地下微生物学**：本研究确认了深层地下环境中存在大量微生物的估算 [Zhang 2019, pp. 1-2]，并引用了 [[Hinrichs & Inagaki, 2012]]、[[Magnabosco et al., 2018]] 和 [[McMahon & Parnell, 2014]]，建立了与全球地下生物圈研究的联系。
- **连接到DNA测序技术进展**：研究阐述了高通量测序技术的突破才使得分析复杂环境样本中的微生物群落变得经济可行 [Zhang 2019, pp. 2-4] [Zhang 2019, pp. 2-4]，可与 [[Shokralla et al., 2012]] 等关于环境DNA测序技术演变的综述工作联系起来。

## Open Questions
1. 该方法（微生物群落组成作为井间连通性指示）在其他地质背景（如碳酸盐岩、砂岩）或不同深度下的适用性如何？（未从索引片段中确认）
2. 微生物群落结构随时间（例如在储层开发的不同阶段、季节性变化）的稳定性如何，何时需要进行重复采样？（未从索引片段中确认）
3. 除了区分连通性和识别流体来源，微生物群落数据能否用于量化井间连通的程度（如传导率）？（片段中提及此是传统压力测试等方法的专长，但未明确微生物数据能否胜任）[Zhang 2019, pp. 2-4]

## Source Coverage
本页内容基于该论文的22个索引片段。片段覆盖了摘要、引言、研究地点描述、采样和测序方法、部分结果和讨论，信息较为全面，涵盖了研究动机、核心方法、关键发现和主要结论。然而，索引片段可能缺失了以下重要信息：详细的地球化学对比数据和图表、完整的系统发育树、具体的群落组成差异统计检验结果、以及更深入的方法局限性讨论。这些缺失可能导致对证据强度的描述不够充分。
