---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-viswanathan-from-fluid-flow-to-coupled-processes-in-fractured-rock-recent-advances-and-new"
title: "From Fluid Flow to Coupled Processes in Fractured Rock: Recent Advances and New Frontiers."
status: "draft"
source_pdf: "data/papers/2022 - From Fluid Flow to Coupled Processes in Fractured Rock Recent Advances and New Frontiers.pdf"
collections:
citation: "Viswanathan, H. S., et al. \"From Fluid Flow to Coupled Processes in Fractured Rock: Recent Advances and New Frontiers.\" *Reviews of Geophysics*, vol. 60, no. 4, 2022."
indexed_texts: "84"
indexed_chars: "417765"
nonempty_source_blocks: "84"
compiled_source_blocks: "84"
compiled_source_chars: "417059"
compiled_stage_count: "1"
single_pass_char_budget: "800000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.99831"
coverage_status: "full-index"
source_signature: "f5a74073f9511ed4bd1294e159a15214d3dfdd44"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T09:23:19"
---

# From Fluid Flow to Coupled Processes in Fractured Rock: Recent Advances and New Frontiers.

## One-line Summary

这篇综述文章系统回顾了裂隙岩石中流体流动到耦合过程的研究进展，强调整合现场与实验室实验、物理模拟及不确定性量化。

## Research Question

深层裂隙岩石中，热-水-力-化学(T-H-M-C)耦合过程对流动和传输的控制机制、预测模型的不确定性量化以及多尺度观测与模拟的集成方法。

## Study Area / Data

本综述涵盖全球多个裂隙岩石研究场地和实验室数据，具体案例包括：
- 美国南达科他州Sanford地下研究设施（SURF）的[[Enhanced Geothermal Systems]] Collab项目，深约1.5 km的结晶岩体。
- 瑞士Mont Terri岩石实验室的断层滑动（Fault Slip）实验，涉及低渗透性泥页岩断层带。
- 瑞典Stripa矿场和Äspö硬岩实验室，早期花岗岩中核废料处置研究。
- 美国德克萨斯州Midland盆地的水力压裂测试场（HFTS），关注非常规油气储层。
- 犹他州FORGE（Frontier Observatory for Research in Geothermal Energy）地热研究场地。
- 实验室数据涵盖多种岩石类型（花岗岩、页岩、石灰岩、砂岩等），实验类型包括人工断裂（锯切面）、诱导拉伸/剪切断裂、天然断裂及合成材料等，使用高分辨率轮廓测量、X射线CT、透明类似物/微流控和弹性波等方法获得[Viswanathan 2022, pp. 7-9] [Viswanathan 2022, pp. 13-14] [Viswanathan 2022, pp. 18-19]。

## Methods

综述关注的集成方法包括：

1. **动态监测技术**：分布式光纤传感(Distributed Fiber-Optic Sensing, DFOS)用于温度(DTS)、应变(DSS)和声学(DAS)信号的高分辨率时空监测；三维井中探头（如EMI、FMI、声波扫描、FDTD雷达）进行近井裂隙成像；可实现局部裂隙张开度和剪切位移测量的水力力学井中测试探头（如SIMFIP）[Viswanathan 2022, pp. 5-6]。
2. **数据分析与反演方法**：统计方法（聚类、多变量分析、人工智能算法）用于测井图像中裂隙检测；全波形反演(FWI)和逆时偏移(RTM)进行高分辨率弹性特性成像；应力层析成像和联合反演约束离散裂隙网络(DFN)几何模型；基于机器学习的初至拾取辅助微震事件定位[Viswanathan 2022, pp. 6-7]。
3. **实验室实验技术**：高分辨率轮廓测量（激光、白光）表征裂隙表面粗糙度；X射线CT（工业、微焦点、同步辐射）原位观察裂隙几何演化；透明类似物和微流控系统可视化多相流、化学反应和流场；弹性波（超声相控阵、可传输微型源）探测裂隙比刚度和连通性[Viswanathan 2022, pp. 14-16]。
4. **物理基数值模拟**：
   - 连续介质方法：等效多孔介质模型(EPM)、随机连续介质(SC)、双重连续介质(DCM)。
   - 离散模型：离散裂隙网络(DFN)、离散裂隙-基质(DFM)、通道/管道网络(CN)，以及混合离散-连续介质方法。
   - 本构关系：正应力相依的Bandis-Barton模型、基于Mohr-Coulomb准则的剪切扩容模型、矿物溶解/沉淀的动力学反应速率方程。
   - 力学计算：有限元或离散元方法，有时与有限体积法进行双网格耦合[Viswanathan 2022, pp. 27-35]。
5. **不确定性量化(UQ)与替代模型**：
   - 简化随机模型：用于计算置信区间。
   - 基于图和机器学习的模拟器（图模拟器）：将DFN映射为图(graph)，再使用机器学习修正，速度提高三到四个数量级。
   - 多保真度蒙特卡罗、多项式混沌展开(PCE)等UQ方法[Viswanathan 2022, pp. 40-42] [Viswanathan 2022, pp. 45-46]。

## Key Findings

### 现场观测与技术突破
- 分布式光纤传感(DAS/DSS)能够以极高灵敏度探测跨越流动裂隙的纳米级应变振荡，识别裂隙网络中的活跃裂隙及其热-水-力耦合相互作用[Viswanathan 2022, pp. 10-11]。
- 水力力学井中测试证实，在现场尺度下，单裂隙的孔弹性响应同时受其固有属性（刚度、水力开度）和周围环境的剪切应变分布控制，呈现明显非线性[Viswanathan 2022, pp. 10-10]。
- 在Mont Terri断层活化实验中发现，断层渗透性变化主要由张开度(opening)而非剪切位移主导，大部分断层破裂和相关流体泄漏是**无震(aseismic)的**，仅依靠微震监测无法完全捕获。因此，理解水力-力学耦合对约束断层破裂扩展和止裂至关重要[Viswanathan 2022, pp. 10-10]。
- 多模式监测、联合反演和综合正演模拟的协同应用（如EGS Collab项目），成功三维重建了被激活的裂隙网络。具体利用DSS(每米)和DTS(每0.25m)识别水泥环井中激活裂隙交叉点产生的温度异常(Joule-Thompson效应)或应变信号；较远处的定位微震事件则对齐于特定平面[Viswanathan 2022, pp. 11-11]。

### 实验室研究核心发现
- **渗透率控制因素复杂**：裂隙渗透率受粗糙度、开度(aperture)和接触面积(contact area)分布共同控制，每个因素均存在尺度效应，且动态受应力与位移影响。目前依然缺乏同时高精度测量这三者的实验，局部立方定律(local cubic law)的有效性尚未得到决定性验证[Viswanathan 2022, pp. 16-18]。
- **应力-流动普适标度**：数值研究发现了裂隙流体流动与裂隙比刚度(fracture-specific stiffness)之间存在准普适标度关系，但该关系代表蒙特卡罗模拟的集合平均行为，且实验室加载条件的影响需仔细甄别[Viswanathan 2022, pp. 20-20]。
- **剪切位移对渗透率的双重影响**：在较低正应力和脆性岩石中，剪切位移导致扩容(dilation)，渗透率增加；随位移增大，断层泥(gouge)累积可降低或止住渗透率增长；高正应力或强亲水性矿物(如黏土)含量高时，位移也可能导致渗透率下降[Viswanathan 2022, pp. 20-21]。
- **化学过程影响复杂多变**：
  - 溶解反应可通过增加孔隙度提升渗透率，也可能因溶解弱化粗糙触点而降低渗透率；流动速率增加常导致不稳定溶解指进和通道化流[Viswanathan 2022, pp. 21-21]。
  - 竞争性溶解-沉淀反应可导致渗透率变化甚微，或加剧非均质性（沉淀在狭窄区域和碎屑材料中富集）[Viswanathan 2022, pp. 21-22]。
  - 基质近裂缝区域的化学反应会改变岩石强度，形成影响断裂水-力行为的“反应晕(reaction halo)”[Viswanathan 2022, pp. 22-22]。
- **胶体运输新现象**：纳米至微米级颗粒能形成**群(swarms)**，产生相干运动，其重力沉降速度是单颗粒的10至1000倍，并能变形通过狭窄孔喉，可能显著加速污染物迁移[Viswanathan 2022, pp. 23-23]。

### 数值模型先进成果
- **网络结构的主导性**：大型离散模型（DFN/DFM）研究表明，**裂隙网络结构(connectivity, topology)** 常常是控制流动和传输行为的主导因素，超过了单裂隙尺度开度变化的相对重要性[Viswanathan 2022, pp. 36-36]。
- **热-水-力耦合通道效应**：EGS二维/三维模型成功再现了因冷却岩体热收缩导致的**显著流动通道化(flow channeling)** 和“应力笼(stress-cage)”效应，即冷却区外形成压应力，这与实地观测到的热短路现象相符[Viswanathan 2022, pp. 36-36]。
- **新型网络生成方法**：“运动学(kinematic)” DFN通过模拟裂隙成核、生长和止裂的简化规则，生成具有T型交叉、幂律长度分布等更接近物理现实的网络，其拓扑和水文性质与纯随机网络不同，呈现更强的流动通道化[Viswanathan 2022, pp. 36-37]。

### 不确定性量化与机器学习赋能
- **显著加速模拟**：基于图的模拟器（graph-based emulator）可将流固耦合DFN模型的计算速度提升**4个数量级以上**，结合机器学习对保真度损失进行校正，使运行海量蒙特卡罗实现成为可能[Viswanathan 2022, pp. 46-46]。
- **有效路径识别**：利用图论和机器学习，可精确识别DFN中贡献主要流量的骨干(backbone)子网络，其流量和传输计算仅需完整DFN**50%** 的时间，结果依然准确[Viswanathan 2022, pp. 41-42]。
- **核心不确定性认识**：蒙特卡罗模拟表明，相较于参数不确定性，模型不确定性（如选择随机连续介质还是DFN）对预测积分量（如首次抵达时间）的影响相对次要[Viswanathan 2022, pp. 45-45]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|:---|:---|:---|:---|
| 裂隙渗透率呈对数-正态或双峰分布，最大开度位于裂隙中部并向尖端减小 | Viswanathan 2022, pp. 17-18 | 基于小尺度实验室X射线CT测量 | 与现场卡尺测量揭示的开度随裂隙长度线性标度结果形成对比 |
| 裂隙流体流动与裂隙比刚度之间存在准普适标度关系 | Viswanathan 2022, pp. 20-20 | 基于数千次数值蒙特卡罗研究的集合行为 | 单一实验室测量值可能偏离该平均行为；加载条件对能否发展该标度关系影响显著 [Petrovitch 2014] |
| 颗粒群(swarms)的沉降速度是单颗粒的10–1000倍，并能自适应变形通过窄喉道 | Viswanathan 2022, pp. 23-23 | 实验室实验 | 该特性可能导致污染物以远高于预期的浓度和距离传输 |
| Mont Terri断层的渗透率变化主要由张开(open)主导，大部分破裂为无震滑移(aseismic) | Viswanathan 2022, pp. 10-10 | 低渗透性泥页岩断层，通过流体注入激活 | 仅依赖微震监测将严重低估泄漏风险 |
| 基于图的模拟器比高保真度DFN模型快超过4个数量级 | Viswanathan 2022, pp. 46-46 | 单相稳态流；通过与高保真度模拟比较 | 引入ML进行精度校正；用于快速不确定性量化 |
| 网络结构(structure)控制流动，而非单裂隙开度变化，这是大规模DFN仿真的主要发现 | Viswanathan 2022, pp. 36-36 | 基于千米尺度包含数万条裂隙的DFN模拟 | 指导未来建模：耦合T-H-M-C的DFM模型可能无需显式解析单裂隙尺度的开度变化 |

## Limitations

- **现场技术局限**：分布式光纤传感(DAS/DSS)目前多为单分量测量，对平行于井轴的准静态剪切灵敏度较弱；完全三维应变张量的监测尚未在作业中实现。缺乏原位分布式化学光纤传感器(DCS)来远距离监测裂隙中的化学变化。现有仪器在深部高温(>200°C)和侵蚀性化学环境的长期（数十年）耐久性依然不足。
- **实验室挑战**：模拟完全真实的裂隙网络（考虑交叉点作用、3D拓扑等）的实验极为稀少。几乎所有研究都聚焦于单裂隙或简单平行裂隙组，缺乏验证数值网络模型所需的、控制条件下的网络实验数据，特别是关于裂隙交叉点(intersections)的开度、水力分配和混合机制。
- **模型构成本构关系的经验性**：大多数模拟依赖现象学模型（如Bandis-Barton模型, Mohr-Coulomb准则）来描述裂隙的法向和剪切变形，这些模型的核心参数（如节理粗糙度系数JRC、膨胀角）难以直接测量和尺度升级。
- **计算与不确定性量化瓶颈**：完全的3D热-水-力-化学(THMC)耦合离散裂隙-基质(DFM)模型由于计算成本和网格复杂性，仍限于相对简单几何体。将基于图的模拟器或机器学习替代模型扩展到涵盖**全T-H-M-C过程**仍处于起步阶段。机器学习模型在推断训练数据范围之外的场景时预测不可靠。
- **长时序行为认知的缺乏**：对裂隙闭合/愈合/封闭(closure/healing/sealing)的长周期（数十年到世纪）演化、无震变形、慢滑移和蠕动的直接现场观测极度匮乏，限制了对相关过程（如断层封盖层完整性、长期核素迁移）的预测能力[Viswanathan 2022, pp. 12-13]。

## Assumptions / Conditions

- **立方定律(local cubic law)应用假设**：假设流动为二维、平面层流，且粗糙度变化幅度远小于粗糙度特征波长，雷诺数远小于1。在多数真实粗糙裂隙中，这些条件难以严格满足。
- **离散断裂模型的基本设定**：在离散断裂网络(DFN)和离散裂隙-基质(DFM)模型中，裂隙被简化为开放的空隙空间，不考虑多孔介质属性的裂隙充填。背景基质的非均质性常通过随机场表示。除运动学DFN外，网络拓扑和几何通常通过随机方法生成，假设裂隙位置、产状、长度等服从特定概率分布。
- **耦合模拟默认前提**：流体-力学耦合分析通常假设裂隙为静态、无扩展、预存在(pre-existing)的结构，不适用裂缝尖端扩展问题。化学过程（溶解/沉淀）对渗透率的反馈通常采用**延迟或顺序耦合**(lagged/sequential coupling)方式，以节省计算资源，默认反应相对于流动和力学过程足够缓慢。
- **等效连续体(ECM)的上尺度化前提**：假定存在**表征单元体(REV)**，能够将裂隙和基质的属性均质化为有效张量。当裂隙网络连通性差、裂隙尺寸与网格尺度相当时，REV的存在性存疑，可能导致虚假的流动连接或高估/低估渗透率各向异性。

## Key Variables / Parameters

- **裂隙几何参数**: 表面粗糙度(surface roughness，通常表现为自仿射分形)、水力开度(hydraulic aperture, b)、力学开度(mechanical aperture)、接触面积(contact area)。
- **裂隙力学参数**: 裂隙比刚度(fracture-specific stiffness, κ)、法向刚度、剪切刚度(K_s)、摩擦系数(μ)、膨胀角(ϕ_d)、内聚力(c)。
- **水力参数**: 渗透率(k)、传导系数(T)、储存系数(S)。
- **应力状态**: 有效正应力(σ'_n = σ_n - p)、剪切应力(τ)。
- **热参数**: 温度(T)、热传导系数、热膨胀系数。
- **化学参数**: 反应速率常数(k(T))、比表面积(specific surface area, A)、平衡常数(K(T))、离子浓度(C)。
- **网络描述符**: 裂隙密度(P30/P32)、连通性、拓扑结构（如度分布）、长度与开度分布幂律指数。
- **传输特征量**: 溶质首次抵达时间(first passage time)或突破时间(breakthrough time)、佩克莱数(Péclet, Pe)。
- **分布式传感记录量**: 分布式温度(DTS)、分布式应变(DSS, 纳应变级)、分布式声学(DAS)信号的频率-振幅-相位。

## Reusable Claims

- 裂隙网络的结构（拓扑和连通性）在大多数情况下是控制流动和溶质传输的首要因素，其影响通常超过单裂隙尺度内部开度变化。（来自数值模拟综合结论）[Viswanathan 2022, pp. 36-36]。
- 如果网格分辨率过大，等效连续体模型(EPM)中的单个网格可能形成“虚假连接”，导致模拟的溶质突破时间远早于离散裂隙网络（DFN）模型的预测结果。因此，当网络连通性关键时，DFN/DFM模型更为可靠[Viswanathan 2022, pp. 29-30]。
- 在低渗透性页岩中断层活化的现场实验显示，断层渗透性演化主要由无震(asiesmic)张开主导，微震活动只是总变形的一部分，预测泄漏风险必须考虑这种无震机制[Viswanathan 2022, pp. 10-10]。
- 将离散裂隙网络模型映射为图(graph)并利用机器学习修正的模拟方法，可以实现比原物理模型快4个数量级以上的运算速度，同时保有合理的预测精度，对于需要大量实现次数的蒙特卡罗不确定性量化是可行的加速策略[Viswanathan 2022, pp. 46-46]。
- 剪切位移对裂隙渗透率的影响非单调：在适当条件下可因扩容而增加（尤其低应力、脆性岩石），但在大位移、高应力或高黏土矿物含量条件下，可因断层泥形成而降低[Viswanathan 2022, pp. 20-21]。
- 实验室实验中观察到的颗粒群(particle swarms)现象，其迁移速度可达单颗粒的10-1000倍，对胶体/污染物在裂隙中的远距离快速运输具有重大潜在意义[Viswanathan 2022, pp. 23-23]。

## Candidate Concepts

- [[Fractured rock]]
- [[Coupled Thermo-Hydro-Mechanical-Chemical (THMC) Processes]]
- [[Discrete Fracture Network (DFN)]]
- [[Discrete Fracture-Matrix (DFM) model]]
- [[Fracture-specific stiffness]]
- [[Local cubic law]]
- [[Flow channeling]]
- [[Aseismic slip]]
- [[Distributed Fiber Optic Sensing (DFOS)]]
- [[Distributed Acoustic Sensing (DAS)]]
- [[Particle swarms]]
- [[Reactive transport modeling]]
- [[Uncertainty quantification (UQ)]]
- [[Graph-based emulator]]
- [[Multifidelity Monte Carlo]]
- [[Representative Elementary Volume (REV)]]
- [[Enhanced Geothermal Systems (EGS)]]
- [[Hydraulic fracturing]]
- [[Kinematic DFN]]
- [[Fault reactivation]]

## Candidate Methods

- [[Full waveform inversion (FWI)]]
- [[Microseismic monitoring]]
- [[Stress-based tomography]]
- [[X-ray computed tomography (CT) for fractures]]
- [[Microfluidics for geoscience]]
- [[Elastic wave characterization of fractures]]
- [[Graph theory for flow networks]]
- [[Machine learning emulators for subsurface flow]]
- [[Polynomial Chaos Expansion (PCE)]]
- [[Monte Carlo simulation]]

## Connections To Other Work

- 本综述指明了裂隙-基质相互作用的重要性，这与Berkowitz (2002)关于裂隙介质表征的综述及Berre等人(2019)关于离散与连续介质模型对比的论述一脉相承。
- 现场实验部分强调了DECOVALEX国际合作项目[Viswanathan 2022, pp. 48-48]的价值，该项目整合了现场实验、高保真度模拟与多团队对比，是验证和提升耦合过程模型的国际标杆。
- 对于耦合过程的数值模拟，内容直接继承并扩展了诸如Tsang (1991)和Rutqvist & Tsang (2012)所讨论的裂隙中热-水-力耦合的核心问题。
- 在不确定性量化方面，引用了Selroos等人(2002)和Finsterle (2000)的研究来佐证对于积分量（如突破时间）预测，连续介质与离散模型间的模型不确定性可能小于参数不确定性的观点。
- 裂隙流动的最基本描述，即“立方定律”，其有效性和局限性直接关联至经典的Witherspoon, Wang等人(1980)实验工作，以及后续诸多关于粗糙度、惯性效应对其修正的论述[Viswanathan 2022, pp. 17-17]。

## Open Questions

- 如何开发并现场部署能够长期（数年-数十年）耐高温、耐化学腐蚀的高灵敏度综合传感器（特别是分布式化学传感器DCS）？
- 现场尺度上，断层和裂隙长期演化的化学-力学耦合（如反应晕的形成和影响）如何有效测量与建模？
- 从单裂隙行为到包含交叉点的简单网络，再到复杂的千米尺度3D网络，流体和溶质的混合、分配、以及流动-比刚度标度关系如何过渡？是否存在一个“代表网络体积(REV) for network”？[Viswanathan 2022, pp. 24-24]
- 如何将基于图和机器学习的成功加速方法扩展到包含完整T-H-M-C耦合的模拟器中，建立一个能高效运行不确定性量化的全耦合计算框架？[Viswanathan 2022, pp. 42-46]
- 能否开发一个普适的、基于几何与岩石物性的裂隙渗透率预测框架，以解决当前不同岩石类型和实验条件下渗透率测量值无法统一对比的困境？[Viswanathan 2022, pp. 18-19]

## Source Coverage

所有84个提供的非空索引片段均已纳入处理，基于这些片段构建了本页面。源文本覆盖率（按块计）为100% (84/84)，按字符计约为99.8% (417,059/417,765)。所有主张均源自所给材料并保留来源标签。
