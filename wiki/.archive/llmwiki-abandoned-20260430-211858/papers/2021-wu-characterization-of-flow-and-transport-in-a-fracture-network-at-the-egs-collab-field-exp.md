---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-wu-characterization-of-flow-and-transport-in-a-fracture-network-at-the-egs-collab-field-exp"
title: "Characterization of Flow and Transport in a Fracture Network at the EGS Collab Field Experiment through Stochastic Modeling of Tracer Recovery."
status: "draft"
source_pdf: "data/papers/2021 - Characterization of flow and transport in a fracture network at the EGS Collab field experiment through stochastic modeling of tracer recovery.pdf"
collections:
  - "part4-1"
citation: "Wu, Hui, et al. “Characterization of Flow and Transport in a Fracture Network at the EGS Collab Field Experiment through Stochastic Modeling of Tracer Recovery.” *eScholarship*, 1 Feb. 2021, doi:10.1016/j.jhydrol.2020.125888. Accessed 2026."
indexed_texts: "18"
indexed_chars: "85259"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T02:12:48"
---

# Characterization of Flow and Transport in a Fracture Network at the EGS Collab Field Experiment through Stochastic Modeling of Tracer Recovery.

## One-line Summary
本研究通过示踪剂回收的随机建模，表征了EGS Collab现场实验中由一条水力裂缝和一条天然裂缝耦合而成的裂隙网络内的流体流动与溶质运移特征 [Wu 2021, pp. 1-5]。

## Research Question
如何利用大量但存在不确定性的地质与地球物理测量数据，通过随机建模方法，有效表征增强型地热系统（EGS）中难以直接观察的裂隙网络的流动与溶质运移过程？[Wu 2021, pp. 1-5]

## Study Area / Data
- **实验地点**：实验1测试平台位于美国南达科他州的桑福德地下研究设施（SURF）内4850层西入口巷道西侧，深度约距地表1478米，岩性以千枚岩为主 [Wu 2021, pp. 7-11]。
- **井配置**：测试平台共钻有8口井，包括1口注入井（E1-I）、1口生产井（E1-P）和6口监测井 [Wu 2021, pp. 7-11]。
- **裂隙系统**：研究聚焦于E1-I井50米深度处刺激产生的水力裂缝，以及一条被称为“OT-P Connector”，连接监测井E1-OT和生产井E1-P的天然裂缝 [Wu 2021, pp. 11-13]。
- **刺激与测试数据**：2018年进行了多轮水力刺激。2018年10月24日至11月20日期间，以400 ml/min的速率进行了一次注水循环测试，并在此期间（10月26日至11月14日）进行了六次C-Dots示踪剂测试 [Wu 2021, pp. 11-13；Wu 2021, pp. 13-16]。生产井E1-P的两个产液点分别与水力裂缝和天然裂缝相交，记为E1-PHF和E1-PNF [Wu 2021, pp. 16-18]。
- **其他数据**：研究综合使用了岩心日志、井壁图像、水力刺激和注水循环测试期间的微震事件、监测井的分布式温度传感（DTS）测量、微生物/地球化学数据以及E1-P的井下摄像调查 [Wu 2021, pp. 13-16]。

## Methods
- **裂隙网络模型构建**：基于地质、地球物理和地球化学等综合数据，构建了一个包含一条椭圆形水力裂缝和一条平面状天然裂缝（OT-P Connector）的裂隙网络概念模型 [Wu 2021, pp. 13-16]。模型考虑了裂隙范围、汇的位置与大小、裂隙开度分布和弥散度等不确定性参数 [Wu 2021, pp. 18-21]。
- **流动与运移正演模拟**：采用劳伦斯利弗莫尔国家实验室开发的多物理场模拟平台GEOS进行流体流动和示踪剂运移的有限体积法（FVM）模拟 [Wu 2021, pp. 21-23]。裂隙采用等效多孔介质薄层表示，通过立方定律将裂隙开度转换为等效孔隙度和渗透率 [Wu 2021, pp. 21-23]。
- **裂隙耦合策略**：采用顺序耦合方式模拟水力裂缝和天然裂缝。首先确定水力裂缝与天然裂缝之间满足示踪剂突破曲线（BTCs）的泄露界面参数，然后将此作为已知边界条件施加给天然裂缝模型 [Wu 2021, pp. 16-18]。
- **随机建模框架**：通过生成大量随机实现来覆盖参数空间，寻找能够同时匹配E1-PHF、E1-PNF和E1-OT三口井示踪剂突破曲线的解，并从这些解的共性中提取流动和运移特征 [Wu 2021, pp. 5-7；Wu 2021, pp. 7-11]。

## Key Findings
- 通过随机建模方法，成功地同时拟合了E1-PHF、E1-PNF和E1-OT三处监测点的示踪剂突破曲线，这在之前类似研究中（如Soultz-sous-Forêts场地）是未能达成的目标 [Wu 2021, pp. 5-7]。
- 模拟结果揭示了示踪剂突破曲线随时间发生显著变化的原因是流动场的改变，这与注水循环测试期间的额外刺激活动以及E1-OT井的泄露有关 [Wu 2021, pp. 13-16]。
- 模型参数化研究表明，由于示踪剂注入持续时间短（5~7.6分钟）且基质孔隙度和渗透率极低，基质扩散对示踪剂运移过程的影响可以忽略不计 [Wu 2021, pp. 16-18]。
- 裂隙开度分布被假设为均匀或空间自相关的非均质分布，后者服从对数正态分布，并通过球状变差模型生成 [Wu 2021, pp. 18-21]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 研究通过随机建模成功同时拟合了E1-PHF， E1-PNF， E1-OT三口井的示踪剂突破曲线。 | [Wu 2021, pp. 5-7] | 模型涉及水力裂缝与天然裂缝的耦合，并使用了2018年10月-11月在EGS Collab Experiment 1的六次示踪剂测试数据。 | 这是衡量模型有效性的关键证据，指出了相较于 Soultz-sous-Forêts EGS场地研究的改进。 |
| 研究区域包含一条由刺激产生的水力裂缝和一条名为“OT-P Connector”的天然裂缝。 | [Wu 2021, pp. 11-13; Wu 2021, pp. 13-16] | 基于岩心日志、井壁图像、微震、DTS等数据解释。水力裂缝由E1-I井50米处刺激形成；天然裂缝连接E1-OT和E1-P。 | 裂隙网络模型的几何基础。 |
| 基质扩散对本次示踪剂实验的影响可忽略不计。 | [Wu 2021, pp. 16-18] | 基质孔隙度为0.01，渗透率为5 × 10-18 m²，示踪剂注入时长为5 ~ 7.6分钟。 | 该结论引用了Becker and Shapiro, 2003; White et al., 2018; Zhou et al., 2018。 |
| 模拟采用的裂隙开度符合对数正态分布或伽马分布，并且具有空间自相关性。 | [Wu 2021, pp. 18-21] | 基于岩心样本测量和测井观测。水力裂缝开度上限为几百微米，天然裂缝开度可达数毫米。 | 为开度参数范围的设定提供了依据，引用了Bianchi and Snow, 1968; Gale, 1987等。 |

## Limitations
- 基质扩散过程未被纳入模型，尽管研究论证了其在当前条件下影响甚微，但这是模型的一个简化 [Wu 2021, pp. 16-18]。
- 构建高保真且约束良好的模型具有挑战性，过度简化的模型可能无法捕捉现场的必要复杂性，而过度复杂的模型则容易导致过拟合 [Wu 2021, pp. 5-7]。
- 未从索引片段中确认模型在其他EGS场地或不同尺度下的可迁移性。
- 未从索引片段中确认具体的示踪剂拟合精度指标（如纳什效率系数 NSE）。
- 未从索引片段中确认对长期热采或化学-力学耦合效应的讨论。

## Assumptions / Conditions
- **模型结构假设**：裂隙网络可简化为一条水力裂缝和一条天然裂缝的耦合，其他天然裂缝的影响由模型外围的两个“汇”来概括 [Wu 2021, pp. 16-18]。
- **裂隙表征假设**：裂隙被等效为有一定厚度的多孔介质薄层，其水力学特性由立方定律描述 [Wu 2021, pp. 21-23]。
- **运移过程简化**：示踪剂运移主要由对流和物理弥散控制，模型使用的迎风差分格式引入的数值扩散可以忽略不计 [Wu 2021, pp. 21-23]。基质扩散效应可忽略 [Wu 2021, pp. 16-18]。
- **模型参数化假设**：
    - 裂隙开度分布考虑两种情景：均匀分布或服从对数正态分布且空间自相关的非均质分布 [Wu 2021, pp. 18-21]。
    - 横向弥散度 (αT) 被设定为小于纵向弥散度 (αL) [Wu 2021, pp. 18-21]。

## Key Variables / Parameters
- **裂隙几何参数**：水力裂缝和天然裂缝的范围 (a, b; a′, b′) [Wu 2021, pp. 18-21]。
- **汇参数**：表征模型边界流体损失的汇的位置 (θ, θ') 和长度 (L, L') [Wu 2021, pp. 18-21]。
- **裂隙开度参数**：均匀情景下的单一开度值 (w, w')；非均质情景下的平均开度 (𝑤"， 𝑤"′)、标准差 (σ, σ') 和相关长度 (CL, CL') [Wu 2021, pp. 18-21]。
- **运移参数**：纵向弥散度 (αL, αL′) 和横向弥散度 (αT, αT′) [Wu 2021, pp. 18-21]。
- **耦合参数**：水力裂缝与天然裂缝之间泄露界面的位置、长度和泄露速率 [Wu 2021, pp. 16-18]。
- **现场监测参数**：注入浓度 (C0)、流出速率、示踪剂突破曲线 (BTCs) [Wu 2021, pp. 13-16]。

## Reusable Claims
- **Claim 1**: 在裂缝性储层表征中，随机建模面临两大挑战：一是基于观测数据构建高保真度且适度复杂的模型；二是生成足够多的实现以覆盖高维参数空间 [Wu 2021, pp. 5-7]。该声明的证据来自对前人研究方法不足的总结，适用于类似场地的随机反演研究。
- **Claim 2**: 对于低孔隙度、短时示踪剂测试，基质扩散对示踪剂突破曲线的影响可以忽略不计，模型中可以简化此过程 [Wu 2021, pp. 16-18]。证据来自结合实验条件（基质孔隙度0.01，渗透率5e-18m²，脉冲5-7.6分钟）的分析及对先前研究的引用（Becker and Shapiro, 2003等）。限制条件是适用低渗基质和短脉冲测试。
- **Claim 3**: 基于现场多数据源（地质、地球物理、地球化学）约束裂隙网络模型结构，并采用顺序耦合策略处理水力裂缝与天然裂缝的交互作用，是一种有效的裂隙流表征方法 [Wu 2021, pp. 13-16; Wu 2021, pp. 16-18]。证据来自该方法在本研究中的成功应用，即成功拟合了多监测点的示踪剂BTCs。限制是该方法的有效性在其他场地的普适性未被证实。
- **Claim 4**: GEOS平台具备在复杂裂隙系统中模拟多物理场过程（包括流动和溶质运移）的能力，其通过立方定律将裂隙开度映射为等效孔隙度和渗透率 [Wu 2021, pp. 21-23]。证据来自对GEOS功能的描述和本研究的具体应用。

## Candidate Concepts
- [[fracture network]] (裂隙网络)
- [[stochastic modeling]] (随机建模)
- [[Enhanced Geothermal System (EGS)]] (增强型地热系统)
- [[tracer breakthrough curve]] (示踪剂突破曲线)
- [[cubic law]] (立方定律)
- [[fracture aperture distribution]] (裂隙开度分布)
- [[matrix diffusion]] (基质扩散)
- [[numerical dispersion]] (数值扩散)

## Candidate Methods
- [[GEOS simulator]] (GEOS 模拟器)
- [[Finite Volume Method (FVM)]] (有限体积法)
- [[spherical variogram model]] (球状变差模型)
- [[sequential coupling of fractures]] (裂隙顺序耦合方法)
- [[Monte Carlo approach]] (蒙特卡洛方法)
- [[equivalent porous media representation of fracture]] (裂隙的等效多孔介质表示)

## Connections To Other Work
- **与随机建模方法论的连接**：本研究建立在Cacas et al., 1990a; Geier et al., 2019; Moreno et al., 1988; Ptak et al., 2004; Tsang et al., 1996等关于随机建模在地下水资源分析中应用的工作之上 [Wu 2021, pp. 5-7]。
- **与先前场地研究的对比**：文中明确将本研究的成功与Vogt et al., (2012)在Soultz-sous-Forêts EGS场地的尝试进行了对比，后者用10，000个蒙特卡洛实现也未能同时匹配两条示踪剂突破曲线，指出本研究的改进在于纳入了更复杂的运移机制（如弥散度）[Wu 2021, pp. 5-7]。
- **与裂隙建模理论的连接**：研究采纳了关于裂隙开度空间自相关性与统计分布（如对数正态分布、伽马分布）的广泛文献共识，引用了Bianchi and Snow, 1968; Gale, 1987; Pyrak-Nolte and Morris, 2000; Tsang and Tsang, 1989等 [Wu 2021, pp. 18-21]。
- **与EGS场地研究的连接**：作为EGS Collab项目的一部分，本研究直接与该项目描述场地及实验的整体工作Kneafsey et al., 2019; White et al., 2019相连接 [Wu 2021, pp. 7-11]。
- **偏主题连接**：可从核心主题`fracture flow characterization`连接到更广泛的`subsurface reservoir engineering`、`geothermal energy recovery`及`uncertainty quantification`等领域。

## Open Questions
- 该随机建模方法在多大程度上依赖于所研究场地特定的、丰富的地质和地球物理数据？如果数据量减少，模型的约束效果和结论的稳健性会如何变化？[Wu 2021, pp. 5-7]
- 模型发现的流动与运移特征（如通过解的共同性归纳出的特征）对于预测未来长期的、具不同注入条件的循环测试表现如何？
- 未从索引片段中确认该方法在其他EGS实验阶段（Experiment 2， 3）或其他地热储层中的应用效力。
- 未从索引片段中确认如何定量权衡模型复杂度与过拟合风险。

## Source Coverage
本知识页基于论文的18个索引片段整理而成，覆盖了摘要、引言（研究背景与挑战）、研究区域描述、方法模型（裂隙网络构建、模拟技术、参数空间）和部分关键发现。片段主要集中在对论文研究框架、方法和基本结论的介绍上。由于缺少完整的结果、讨论和结论部分的细节，因此不确定具体的拟合优度、所有成功实现的数量、详细的参数敏感性分析、以及作者对该方法普适性和未来发展方向的更深入讨论。
