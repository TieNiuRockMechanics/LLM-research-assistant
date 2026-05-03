---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-jiang-fracture-activation-and-induced-seismicity-during-long-term-heat-production-in-fractu"
title: "Fracture Activation and Induced Seismicity During Long-Term Heat Production in Fractured Geothermal Reservoirs."
status: "draft"
source_pdf: "data/papers/2022 - Fracture Activation and Induced Seismicity During Long-Term Heat Production in Fractured Geothermal Reservoirs.pdf"
collections:
  - "part5-3"
citation: "Jiang, Chuanyin, et al. \"Fracture Activation and Induced Seismicity During Long-Term Heat Production in Fractured Geothermal Reservoirs.\" *Rock Mechanics and Rock Engineering*, vol. 55, 2022, pp. 5235-5258. https://doi.org/10.1007/s00603-022-02882-z."
indexed_texts: "19"
indexed_chars: "91144"
nonempty_source_blocks: "19"
compiled_source_blocks: "19"
compiled_source_chars: "90330"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.991069"
coverage_status: "full-index"
source_signature: "50973583f5cb5b8378b45a3c136933c75468ee0a"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T05:30:32"
---

# Fracture Activation and Induced Seismicity During Long-Term Heat Production in Fractured Geothermal Reservoirs.

## One-line Summary
本研究通过基于离散裂缝网络的全耦合热-流-力模型，系统揭示了在长期热开采过程中，原位应力状态、注入压力与温度对裂缝性地热储层诱发地震活动的竞争性控制机制。[Jiang 2022, pp. 1-2]

## Research Question
在长期流体循环与热提取过程中，密集裂缝网络中的裂缝再激活动力学与地热生产诱发地震活动的时空演化规律是什么？原位应力、流体增压与热扰动如何交互作用，从而控制地震事件的触发时机、数量与震级？[Jiang 2022, pp. 1-3]

## Study Area / Data
研究采用一个二维通用离散裂缝网络模型，模拟深度约3000 m的裂缝性地热储层。模型域为600 m × 600 m的正方形，包含1200条符合对数正态长度分布的两组系统性裂缝（取向分别为30°与110°），网络生成受应力阴影原理约束以反映真实的裂缝空间组织。[Jiang 2022, pp. 4-5] 模型参数基于文献中的典型值，并非针对特定场地。[Jiang 2022, pp. 5-6] 材料属性包括：岩石基质杨氏模量30 GPa，泊松比0.25，渗透率1×10⁻¹⁸ m²；裂缝初始孔径0.6 mm，摩擦角31°等（完整参数见表1）。[Jiang 2022, pp. 6-7]

## Methods
- **离散裂缝网络（DFN）建模**：使用随机生成的二维DFN显式表征裂缝系统，其中基质渗透率远低于裂缝，流动结构由裂缝网络控制。[Jiang 2022, pp. 3-5]
- **全耦合THM模型**：基于有限元方法（COMSOL Multiphysics®）开发，耦合了地质力学变形（小应变热弹性、裂缝非线性法向变形与库仑摩擦滑动）、单相达西流（基质与裂缝域）以及考虑局部热平衡的传热过程。[Jiang 2022, pp. 3-5]
- **地震活动性评估**：通过监测每一条裂缝段的剪切滑动，基于地震矩M₀（与破裂面积、平均滑动距离和剪切模量相关）计算矩震级M_w，假设裂缝滑动沿走向方向发生且第三维尺寸等于储层厚度。[Jiang 2022, pp. 4-5]
- **模拟工况**：探索三个应力比（Sₓ = Sᵥ, 1.3Sᵥ, 1.6Sᵥ；S_y = 0.8Sᵥ），三个压力梯度（dp/dL_w = 10, 12.5, 15 kPa/m）和三个注入温差（ΔT = 0, 100, 200 °C）。[Jiang 2022, pp. 5-6] 生产阶段时间跨度达30年。[Jiang 2022, pp. 8]

## Key Findings
- **原地应力状态**为诱发地震活动提供基本背景控制：低应力比（Sₓ/S_y = 1/0.8）条件下，系统非常稳定，早期流体增压影响甚微；高应力比（1.6/0.8）条件下，裂缝接近临界应力状态，对微小应力扰动敏感。[Jiang 2022, pp. 6-7, 9-10]
- 流体增压与热扰动是**两个竞争性的触发因素**。在低应力比下，**晚期热衰减**主导裂缝激活，注入温度控制事件的时间、数量和震级。在高应力比下，**早期增压**效应占主导，部分临界应力裂缝可在流体压力扩散时激活；随后因热锋滞后，大量裂缝发生**二次剪切滑动**（即重复地震活动）。[Jiang 2022, pp. 12-14, 16-18]
- 诱发地震事件主要发生在注入井近场以及**流体流动的主通道沿线**，与强热对流（高Péclet数）区域高度对应。远离主流线的区域热传导速率低，能量释放缓慢，驱动剪切的能力较弱。[Jiang 2022, pp. 8-12]
- 在高应力比下，注入压力梯度的变化对裂缝激活比例影响显著，而注入温度主要影响**热诱发二次地震事件的震级**，对其发生时机与数量影响较小。[Jiang 2022, pp. 14, 16-19]
- 长期地热能量产出受裂缝地质力学变形的强烈影响：剪切膨胀可显著提高渗透率，但冷锋过早突破会加速产水温度下降，需在产量与地震风险之间做出权衡。[Jiang 2022, pp. 14-16, 18-19]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 在Sₓ=Sᵥ且S_y=0.8Sᵥ时，ΔT=100 °C几乎不引发M_w>0的事件；ΔT=200 °C时地震事件数量与震级显著增加。 | [Jiang 2022, pp. 9-10] | 低应力比条件 | 热应力不足以在低温差下触发明显地震。 |
| 在Sₓ=1.6Sᵥ且S_y=0.8Sᵥ时，等温（ΔT=0 °C）条件下单一增压即可触发震级高达M_w>1的事件，且事件传播极快（~300 m/10⁵ s）。 | [Jiang 2022, pp. 12] | 高应力比，等温注入 | 临界应力状态下，纯孔隙弹性效应即可诱发地震。 |
| 热衰减诱发的裂缝激活在低应力比下相对热锋有一定**延迟**；在高应力比下二次激活**无延迟**。 | [Jiang 2022, pp. 12-14] | ΔT=200 °C, p_in=35.6 MPa | 高应力比时裂缝更接近临界状态，微小的热应力即可立即触发。 |
| 当ΔT从100 °C升至200 °C时，在Sₓ=1.3Sᵥ条件下，二次激活事件的比例从34%增至69%；在Sₓ=1.6Sᵥ条件下，两次激活事件的总比例接近100%，且ΔT的变化对两激活机制比例影响甚微。 | [Jiang 2022, pp. 18] | 不同应力比和温差对比 | 低应力比时，温差增大强烈促进首次热激活；高应力比时所有裂缝都几乎会发生至少一次滑动。 |

## Limitations
- 研究基于**二维**通用DFN模型，无法完全捕捉三维裂缝网络的多轴应力依赖行为及三维流动路径。[Jiang 2022, pp. 19]
- 模型假设所有裂缝滑动均为**地震性**，未考虑无震滑动过程，而后者在注入体积较小时可能频繁出现。[Jiang 2022, pp. 18]
- 未考虑**化学溶解/沉淀**对裂缝长期力学与输运性质的影响。[Jiang 2022, pp. 19]
- 未纳入**应力驱动的裂缝扩展**，这对临界连通系统可能至关重要。[Jiang 2022, pp. 19]
- 所采用的模型为**通用性研究**，参数取文献典型值，并非针对特定场地验证。[Jiang 2022, pp. 5]

## Assumptions / Conditions
- 裂缝性地热储层为**基质-裂缝双组分系统**，基质渗透率远低于裂缝，流动由裂缝网络控制。[Jiang 2022, pp. 3]
- 初始储层**饱和同种水**，流动遵循**单相达西定律**。[Jiang 2022, pp. 3]
- 裂缝与基质间的热交换基于**局部热平衡**假设。[Jiang 2022, pp. 3]
- 岩石基质的变形为**小应变线热弹性**。[Jiang 2022, pp. 3]
- 裂缝法向变形遵循**双曲线模型**，剪切行为遵循**库仑摩擦定律**，且考虑了剪切诱导的不可逆膨胀。[Jiang 2022, pp. 3-4]
- 用于地震矩计算的破裂面积假设以**储层厚度**为第三维尺寸，滑移沿走向方向发生。[Jiang 2022, pp. 5]

## Key Variables / Parameters
- **原地应力比 (Sₓ/S_y)**：控制系统临界性的基础变量。[Jiang 2022, pp. 5-6]
- **宏观压力梯度 (dp/dL_w)**：10, 12.5, 15 kPa/m，控制早期增压效应和整体流速。[Jiang 2022, pp. 6]
- **注入温差 (ΔT = T₀ - T_in)**：0, 100, 200 °C，衡量热扰动强度。[Jiang 2022, pp. 6]
- **Péclet数 (Pe)**：量化主通道中热对流与基质热传导的竞争，控制热锋面推进的剧烈程度与裂缝激活的速率。[Jiang 2022, pp. 10-11]
- **岩石基质与裂缝力学/水力学参数**：包括杨氏模量、泊松比、渗透率、初始孔径、摩擦角、剪胀角、初始刚度等，见原文表1。[Jiang 2022, pp. 6-7]

## Reusable Claims
- 当处于**低原位应力比**的稳定应力状态时，长期热生产导致的**热衰减**是裂缝激活与诱发地震的主导机制。此时，**注入温度**显著控制地震事件发生的**时机、数量和最大震级**。[Jiang 2022, pp. 18-19, 22]
- 当处于**高原位应力比**的临界应力状态时，**早期流体增压**即可诱发大量地震活动。随后的**热锋面传播**会引发大规模的**二次裂缝再激活与重复地震活动**。此时，注入温度主要影响**事件震级**，而对二次热诱发事件的时机和数量影响不显著。[Jiang 2022, pp. 18-19, 22]
- 在长期热生产过程中，诱发地震活动在空间上可划分为不同模式：**注水井附近区域**（近场）易发**单次**大震级事件（压力与热效应叠加）；**生产井附近区域**因压力低，主要发生**单次**由热衰减引发的激活；**中间主通道区域**则易发生由压力和热分别触发的**双重激活**。[Jiang 2022, pp. 18-19]
- 裂缝地震滑动的空间范围与强度与**流体主通道高度相关**。仅在热对流强烈（高Pe数）的通道区域易发生快速热卸载和大震级事件；弱对流区域的热传导方式难以驱动裂缝快速失稳。[Jiang 2022, pp. 10-12, 18]

## Candidate Concepts
- [[Fracture activation and induced seismicity|裂缝激活与诱发地震活动]]
- [[Discrete fracture network (DFN)|离散裂缝网络（DFN）]]
- [[Poroelastic and thermoelastic stressing|孔隙弹性与热弹性应力]]
- [[Mohr-Coulomb failure criterion|Mohr-Coulomb 破坏准则]]
- [[Stress criticality margin|应力临界裕度]]
- [[Péclet number in fractured reservoirs|裂缝性储层中的Péclet数]]
- [[Recurrent seismicity|重复地震活动]]
- [[Flow channeling in fractured rock|裂缝性岩体中的流动沟道化]]

## Candidate Methods
- [[Fully coupled THM finite element model (COMSOL)|全耦合THM有限元模型（COMSOL）]]
- [[Stress-dependent aperture cubic law|应力依赖孔径的立方定律]]
- [[Seismic moment calculation from fracture slip|基于裂缝滑移的地震矩计算]]

## Connections To Other Work
- 与前人基于**单一断层**的长期热生产模拟结果一致——高应力比下，热效应主要影响量级而非时机（如Gan and Elsworth, 2014a）；本研究将其扩展至**复杂裂缝网络**，揭示了空间非均质性与重复激活模式的细节。[Jiang 2022, pp. 16, 22]
- 结果支持“热应力可通过降低有效正应力而促进断层/裂缝失稳”的经典Mohr-Coulomb解释框架，并进一步量化了**流体增压与热衰减两种机制在时空上的竞争与叠加**关系。[Jiang 2022, pp. 2]
- 生产诱发的裂缝变形直接影响**长期热提取效率**，这与Izadi and Elsworth (2015)及Zhang et al. (2021)等关于THMC耦合过程的结论相呼应。[Jiang 2022, pp. 14-16]

## Open Questions
- 在裂缝系统中，位于**主流线以外**区域的**无震滑动**过程如何影响整体的应力重分布与长期稳定性？[Jiang 2022, pp. 18]
- 若耦合**化学过程**（如矿物溶解/沉淀），地质力学与渗流特性的长期演化将如何改变地震活动模式与热产出？[Jiang 2022, pp. 19]
- 将研究扩展至具有**幂律长度标度**的更真实三维裂缝网络，并考虑**应力驱动的裂缝扩展**，会使关键发现产生怎样的修正？[Jiang 2022, pp. 19]

## Source Coverage
本文档严格基于提供的**全部19个索引片段**编译而成，未使用任何未提供的证据来源。经过逐字级联处理，所有非空来源块均已被处理，来源块覆盖率为**100%**，字符级覆盖率约为**99.1%**。
