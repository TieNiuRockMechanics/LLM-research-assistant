---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2020-egert-implications-on-large-scale-flow-of-the-fractured-egs-reservoir-soultz-inferred-from"
title: "Implications on Large-Scale Flow of the Fractured EGS Reservoir Soultz Inferred from Hydraulic Data and Tracer Experiments."
status: "draft"
source_pdf: "data/papers/2020 - Implications on large-scale flow of the fractured EGS reservoir Soultz inferred from hydraulic data and tracer experiments.pdf"
collections:
  - "part4-1"
citation: "Egert, Robert, et al. \"Implications on Large-Scale Flow of the Fractured EGS Reservoir Soultz Inferred from Hydraulic Data and Tracer Experiments.\""
indexed_texts: "15"
indexed_chars: "74042"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T00:54:59"
---

# Implications on Large-Scale Flow of the Fractured EGS Reservoir Soultz Inferred from Hydraulic Data and Tracer Experiments.

## One-line Summary
研究通过构建包含13条主要水力活跃断层的瞬态三维有限元模型，模拟Soultz增强型地热系统储层中的水力与溶质运移，揭示其大规模流动机制，并强调了水力分离储层南北两部分的关键裂缝带作用 [Egert unknown-year, pp. 1-3]。

## Research Question
核心问题是，如何综合利用水力数据与示踪实验数据，克服空间信息缺失、数据孤立和模型简化等局限，来更好地表征和量化Soultz裂缝型EGS储层内部的大规模流体流动路径、井间连接和热交换器的流动场，特别是揭示潜在的、将储层分割为南北两个水力区域的关键裂缝带 [Egert unknown-year, pp. 1-3, 3-4, 14-17]。

## Study Area / Data
- **研究区**：法国Soultz-sous-Forêts的增强型地热系统，位于上莱茵地堑（URG）中部，储层为断层和裂隙控制的低渗透性结晶基底花岗岩 [Egert unknown-year, pp. 4-6, 1-3]。
- **钻井数据**：模型包含深部储层中的GPK1至GPK4四口井，及其裸眼段和套管泄漏信息 [Egert unknown-year, pp. 1-3]。
- **水力/地球物理数据**：基于地球物理、地质和水力数据，特别是用于反演裂隙网络参数的长期井间循环测试数据 [Egert unknown-year, pp. 1-3, 4-6]。其中，2011年初的一次循环测试（平均流量9-20 L/s）用于校准连接GPK1, GPK2, GPK3三口井的裂缝导水系数 [Egert unknown-year, pp. 10-12]。
- **示踪实验数据**：2005年7月至12月在GPK2-GPK4井间进行的持续145天的示踪测试，荧光素钠从GPK3注入，从GPK2和GPK4采出 [Egert unknown-year, pp. 12-14]。GPK2和GPK3之间存在两种水力连接：一个水力短路和一个更长路径，而GPK3与GPK4之间连接较差 [Egert unknown-year, pp. 6-8]。

## Methods
- **数值模拟工具**：采用基于MOOSE框架的开源有限元应用TIGER（THC sImulator for GEoscience Research），该工具可处理地热储层中的热-水-溶质运移问题 [Egert unknown-year, pp. 6-8]。
- **控制方程**：水力场通过结合质量/动量守恒和达西定律求解孔隙压力；溶质运移由对流-扩散-弥散方程控制。裂缝被处理为离散二维单元，井的裸眼段被离散为一维单元，与三维基质连续体共享节点 [Egert unknown-year, pp. 6-8]。
- **模型构建与校准**：
    - 模型域为13x11x5 km，包含13条主要的水力活跃断层和裂缝 [Egert unknown-year, pp. 1-3]。
    - 利用长期井间循环测试数据正向反演裂隙网络的水力参数，并进一步通过重现2005年井间示踪实验来重新校准水力模型 [Egert unknown-year, pp. 4-6]。
    - 模型假设基质渗透率为正交各向异性，N-S向更高 [Egert unknown-year, pp. 8-10]。
    - 对GPK3-FZ4770主裂缝在GPK2和GPK3附近进行了网格细分，以考虑水力或化学增产效果并最小化网格依赖性 [Egert unknown-year, pp. 8-10]。

## Key Findings
- **模型确认了储层的强非均质性**，并**揭示了一条潜在的重要裂缝带的存在**，该裂缝带将储层水力学分隔为包含GPK1-GPK3的北部区域和包含GPK4的南部区域，并倾向于将储层与主断层系统连接起来 [Egert unknown-year, pp. 1-3]。
- **GPK2与GPK3的真实连接距离被修正**。模型显示，连接两口井的主裂缝GPK3-FZ4770是倾斜的，井在不同储层深度与之相交，其真实距离为840米，而非通常基于纯水平距离估算的650米 [Egert unknown-year, pp. 8-10]。
- **成功模拟示踪突破曲线**。模型拟合了GPK2和GPK4两口井的荧光素钠浓度突破曲线（BTC），并识别出了GPK2处的双峰或三水力路径特征 [Egert unknown-year, pp. 12-14]。GPK2的突破曲线表现出强烈拖尾，可能是不同裂隙组相互连接所致 [Egert unknown-year, pp. 12-14]。
- **识别出储层中的“分离裂缝”**。一条走向WNW-ESE方向的裂缝（Separation fracture）作为一个异常带，通过创造沿自身的优势通道和排水作用，水力学上解耦了储层的南部（GPK4）与北部（GPK1-GPK3）[Egert unknown-year, pp. 14-17]。
- **量化了示踪剂回注和背景流的影响**。示踪剂回注导致GPK2在实验末期的示踪剂浓度增加了20%，GPK4增加了6% [Egert unknown-year, pp. 14-17]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 一条潜在的裂缝带将储层水力学分隔为北部(GPK1-GPK3)和南部(GPK4) | [Egert unknown-year, pp. 1-3] | 基于包含13条主要断裂的有限元模型对2005年示踪实验的模拟结果 | 该裂缝带（Separation fracture）走向WNW-ESE，充当了优势通道并水力学解耦了两个区域 [Egert unknown-year, pp. 14-17]。 |
| GPK2和GPK3之间的真实连接距离为840米 | [Egert unknown-year, pp. 8-10] | 模型考虑了GPK3-FZ4770裂缝的倾斜以及井在不同储层深度与裂缝相交的情况 | 通常使用的纯水平距离为650米。 |
| 示踪剂回注导致实验末期GPK2的示踪剂浓度增加了20%，GPK4增加了6% | [Egert unknown-year, pp. 14-17] | 在对2005年示踪实验进行长期数值模拟和评估时，对比了考虑与忽略示踪剂回注的情况 | |
| 套管泄漏影响了GPK2的压力响应测量 | [Egert unknown-year, pp. 10-12] | 在2011年初的循环测试进行到第47天后，GPK2报告了套管泄漏 | 泄漏导致流体回流至储层，泵流量对应的测量压力变化低于理论值。该泄漏未纳入本次研究的模型。 |
| GPK2示踪突破曲线显示存在2到3条不同的水力通道 | [Egert unknown-year, pp. 12-14] | 对GPK2的2005年示踪试验突破曲线进行分析和模型拟合 | 拖尾现象支持该结论，可能是由不同的裂隙组连接两口井所导致。 |

## Limitations
- 模型仅关注主要的裂缝带（13条），可能忽略了许多次要裂缝和基质中的小尺度非均质性，这些可能影响细节流动 [Egert unknown-year, pp. 1-3]。
- 模型校准偏向长期稳态数据，对于短期瞬态行为（如GPK3在实验初期5-15天的压力变化）拟合不佳，原因可能是未考虑的井筒效应、表皮效应、小裂缝开闭或流动状态变化等 [Egert unknown-year, pp. 10-12]。
- GPK2在2011年循环测试中的套管泄漏未纳入模型，这使该段时间的压力拟合存在偏差 [Egert unknown-year, pp. 10-12]。
- 对示踪突破曲线最大值附近的混合模拟，是通过调整纵向和横向弥散度及裂缝开度的变化来实现的，存在参数非唯一性问题 [Egert unknown-year, pp. 12-14]。

## Assumptions / Conditions
- **表征单元体假设**：模型假设多孔介质存在表征单元体（REV），使得耦合过程间的相互作用可在此尺度上发生 [Egert unknown-year, pp. 6-8]。
- **裂缝为离散二维单元**：主要的导水断层和裂缝被简化为离散的二维界面，其内流体流动遵循特定的方程 [Egert unknown-year, pp. 6-8]。
- **统计均匀系统假设**：当运移维度远大于裂缝内通道间距，且运移距离足够大时，使用统计均匀系统（如用于开度、渗透率）是合适的 [Egert unknown-year, pp. 8-10]。
- **静水压力初始与边界条件**：整个储层的初始孔隙压力被设定为静水压力，且顶部和底部边界条件与之相符[Egert unknown-year, pp. 8-10]。
- **各向异性渗透率**：假设基质渗透率为正交各向异性，且在南北方向上更高 [Egert unknown-year, pp. 8-10]。

## Key Variables / Parameters
- `P`：孔隙压力
- `t`：时间
- `S_m`：液相与固相的混合比储水系数
- `Q`：源汇项（注采）
- `k`：渗透率张量
- `μ`：流体动力粘度
- `ρ_l`：流体密度
- `g`：重力加速度矢量
- `q`：达西速度矢量
- `b`：尺度因子（用于考虑裂缝开度和井的面积）
- `C`：溶质浓度
- `D_m`：溶质弥散张量
- **裂缝导水系数 (transmissivity)**：通过水力测试进行校准 [Egert unknown-year, pp. 10-12]。
- **裂缝渗透率 (permeability)**：通过拟合示踪实验的运移时间和流体速度进行校准 [Egert unknown-year, pp. 12-14]。
- **纵向/横向弥散度 (longitudinal/transversal dispersivity)**：用于拟合示踪突破曲线的最大值附近的混合 [Egert unknown-year, pp. 12-14]。
- **裂缝开度 (aperture)**：用于拟合示踪突破曲线的混合 [Egert unknown-year, pp. 12-14]。

## Reusable Claims
- **Claim 1**: 对于裂缝型EGS储层，综合利用长期循环测试和示踪实验数据进行多步骤校准（先用循环测试反演水力参数，再用示踪数据校准运移参数），可以有效构建能重现储层非均质性和井间复杂连接的离散裂隙网络模型 [Egert unknown-year, pp. 4-6]。
    - **条件**: 需要有高质量的长期井间循环测试和示踪实验数据，且模型空间尺度远大于局部非均质性。
    - **证据**: 该方法应用于Soultz储层，模型成功校准了13条主要裂缝的导水系数，并模拟了示踪突破曲线，识别出储层的水力学分割和GPK2的多通道连接 [Egert unknown-year, pp. 10-12, 12-14]。
- **Claim 2**: 在裂缝性储层中，连接井间的关键裂缝若与井筒倾斜相交，其真实连接距离可能显著大于纯水平距离（两点间直线距离），错误估计会影响对流体运移时间和储层体积的计算 [Egert unknown-year, pp. 8-10]。
    - **条件**: 裂缝倾角非垂直，且与井筒相交于不同深度。
    - **证据**: Soultz储层中，连接GPK2和GPK3的GPK3-FZ4770裂缝真实距离为840米，而通常假设的水平距离为650米 [Egert unknown-year, pp. 8-10]。
- **Claim 3**: 示踪剂回注（即采出的、富含示踪剂的流体被重新注入储层）会对长期示踪剂浓度分布产生显著影响，在评价示踪实验时需要纳入模型，否则会导致对储层连接性和运移路径的评估偏差 [Egert unknown-year, pp. 14-17]。
    - **条件**: 试验属于闭路循环，且采出流体被重新注入储层。
    - **证据**: Soultz试验中，忽略示踪剂回注导致GPK2在试验末期浓度被低估20%，GPK4被低估6% [Egert unknown-year, pp. 14-17]。

## Candidate Concepts
- [[离散裂隙网络模型]]
- [[增强型地热系统]]
- [[表征单元体]]
- [[达西定律]]
- [[对流-弥散方程]]
- [[示踪突破曲线]]
- [[水力层析成像]]
- [[裂隙储层]]
- [[井间循环测试]]

## Candidate Methods
- [[有限元模拟]]
- [[TIGER 模拟器]]
- [[MOOSE 框架]]
- [[多步骤模型校准]]
- [[水力示踪联合反演]]
- [[示踪实验]]
- [[水力层析扫描]]

## Connections To Other Work
- **直接继承与发展**：本研究模型对 Held et al. (2014) 的早期方法进行了重大扩展，加入了花岗岩基底和多条水力活跃断裂[Egert unknown-year, pp. 4-6]。模拟所用的示踪数据来自 Sanjuan et al. (2006) 的实验 [Egert unknown-year, pp. 6-8]。
- **背景研究**：Soultz储层的自然对流过程（Bächler et al., 2003; Guillou-Frottier et al., 2013；Kohl et al., 2000；Vallier et al., 2019）和机械增产效果（Baujard and Bruel, 2006；Kohl et al., 2006；Kohl and Mégel, 2007）已有多项数值研究。过去的井间示踪模拟多采用简化模型，如连接两井的单一平面结构或理想裂隙网络，并使用解析或简化数值解 [Egert unknown-year, pp. 3-4]，本工作则在复杂三维离散裂隙网络上进行了更全面的模拟。
- **可连接的主题**：本工作通过示踪实验研究裂隙储层流动路径，在方法学上与以下领域相关：
    - 裂隙介质中的溶质运移理论，如通道化流动与弥散效应（[[Becker and Shapiro, 2000]]）[Egert unknown-year, pp. 12-14]。
    - 裂隙统计均匀化假设的适用性研究（[[Tsang et al., 1988]]）[Egert unknown-year, pp. 8-10]。
    - 地热储层数值模拟的一般方法论（[[O'Sullivan et al., 2001]]）[Egert unknown-year, pp. 3-4]。

## Open Questions
- 储层中识别出的“分离裂缝”的具体三维几何形态、水力属性（如导水系数、开度的空间分布）及其与其他裂缝网络的连接细节是什么？在索引片段中未明确给出。
- 模型拟合示踪突破曲线时，纵向和横向弥散度以及裂缝开度的具体校准值是多少？这些参数的敏感性和唯一性如何？未从索引片段中确认。
- 储层南部的GPK4井的未来井位部署或储层改造策略，根据本研究揭示的分离裂缝带应如何调整？未从索引片段中确认。
- 除了示踪剂回注和背景流，还有哪些长期运行因素（如热-水-力-化学多场耦合效应）会影响该储层的大规模流动路径？该研究未涉及。

## Source Coverage
本页内容基于15个索引片段，主要覆盖了论文的背景、方法、核心结果和部分讨论部分。片段详细描述了模型构建方法、校准流程、关键发现（如分离裂缝）以及示踪剂回注等影响因素的量化。然而，索引片段明显偏向结果的图形解读和部分数值，对于完整的讨论、结论、具体的参数表（如最终校准的裂缝导水系数、渗透率值）、引言部分的全面综述以及全部参考文献列表可能覆盖不全。
