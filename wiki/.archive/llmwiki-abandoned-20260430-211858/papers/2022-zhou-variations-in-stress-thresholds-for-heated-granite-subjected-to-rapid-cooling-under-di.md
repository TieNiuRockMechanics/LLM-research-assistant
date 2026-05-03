---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2022-zhou-variations-in-stress-thresholds-for-heated-granite-subjected-to-rapid-cooling-under-di"
title: "Variations in Stress Thresholds for Heated Granite Subjected to Rapid Cooling under Different Confining Pressures."
status: "draft"
source_pdf: "data/papers/2022 - Variations in Stress Thresholds for Heated Granite Subjected to Rapid Cooling under Different Confining Pressures.pdf"
collections:
  - "zotero new"
citation: "Zhou, Chunbo, et al. \"Variations in Stress Thresholds for Heated Granite Subjected to Rapid Cooling under Different Confining Pressures.\" *Natural Resources Research*, vol. 31, no. 5, 2022, pp. 2653-. doi:10.1007/s11053-022-10098-9."
indexed_texts: "11"
indexed_chars: "53668"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T11:31:06"
---

# Variations in Stress Thresholds for Heated Granite Subjected to Rapid Cooling under Different Confining Pressures.

## One-line Summary

研究在不同围压条件下经水冷和液氮冷快速冷却后的高温花岗岩的裂纹起始应力、裂纹损伤应力和峰值应力三个应力阈值的变化规律 [Zhou 2022, pp. 1-2]。

## Research Question

比较液氮冷却与传统水冷却对高温花岗岩力学性能劣化的影响，探究在不同围压（0–60 MPa）作用下三个应力阈值（σci、σcd、σp）的响应差异及内在机制 [Zhou 2022, pp. 1-3]。

## Study Area / Data

未从索引片段中确认研究区具体地理位置。实验材料为花岗岩，先加热至25℃、200℃和400℃，然后分别用水（25℃）和液氮（-196℃）快速冷却，最后在围压为0、20、40、50、60 MPa下进行三轴压缩试验 [Zhou 2022, pp. 3-5]。实验数据包括各条件下σci、σcd、σp以及推算的内摩擦角φ和内聚力c，详见Table 1 [Zhou 2022, pp. 6-9]。

## Methods

- 试样制备：花岗岩加热至目标温度后，分别用水和液氮快速冷却，恢复至室温后进行力学测试 [Zhou 2022, pp. 3-5]。
- 三轴压缩试验：使用TAW-2000岩石试验系统，围压容量80 MPa，加载速率0.05 MPa/s；轴向位移控制加载，速率0.2 mm/min，直至破坏 [Zhou 2022, pp. 3-5]。
- 应力阈值识别：根据体积应变法，裂纹起始应力σci由裂纹体积应变（εcV = εV - εeV）确定，裂纹损伤应力σcd由总体积应变（εV）确定，峰值应力σp即破坏强度 [Zhou 2022, pp. 3-5]；弹性体积应变按 εeV = (1-2ν)/E (σ1-σ3) 计算 [Zhou 2022, pp. 3-5]。
- 数据分析：σci、σcd、σp与围压的关系采用Hoek-Brown破坏准则拟合；温度敏感性用变异系数CV评估 [Zhou 2022, pp. 5-6]。
- 数值模拟：利用COMSOL软件建立二维轴对称均质和非均质模型，模拟水冷和液氮冷的传热过程，分析温度梯度与热膨胀非均质性对热损伤的贡献 [Zhou 2022, pp. 9-12]。模型参数见表3，热边界为第三类边界条件，水冷换热系数1000 W/(m²·K)，液氮冷换热系数100 W/(m²·K)（反映莱顿弗罗斯特效应） [Zhou 2022, pp. 12-13]。
- 围压效应分析：通过Hoek-Brown准则估算等效Mohr-Coulomb参数（内摩擦角φ和内聚力c），公式为 sinφ = mσc / [4(σ1-σ3) + mσc] [Zhou 2022, pp. 13-17]。

## Key Findings

- 两种冷却处理下，σci、σcd、σp与围压均呈凸非线性关系，可用Hoek-Brown方程良好拟合（R²为0.932–0.998） [Zhou 2022, pp. 5-6]。
- 温度对应力阈值的劣化作用被围压显著抑制：例如，从25℃到400℃，0 MPa围压下σci降幅超过50%，而60 MPa围压下仅降低约13%～23% [Zhou 2022, pp. 5-6]。σp的温度敏感性同样随围压升高而减弱 [Zhou 2022, pp. 6-9]。
- 低围压（<40 MPa）下，液氮冷却样品的三个应力阈值普遍高于水冷却样品；高围压（>40 MPa）下这一差异被抑制，并出现液氮冷却样品应力阈值低于水冷却的趋势 [Zhou 2022, pp. 1-2]。
- 液氮冷却在低围压下呈现更高的力学强度，归因于莱顿弗罗斯特效应对传热的限制和矿物体积收缩导致的裂纹闭合 [Zhou 2022, pp. 1-2, 13-17]。数值模拟证实：由于液氮换热系数较低，冷却初期和整体的温度梯度可能低于水冷 [Zhou 2022, pp. 12-13]。
- 在非均质模型中，矿物热膨胀非均质性越强，液氮冷却引起的热应力越大，诱导裂纹更复杂，损伤可能更严重 [Zhou 2022, pp. 13-17]。
- 围压效应方面，液氮冷却相对于水冷却的内摩擦角在围压<40 MPa时偏低（Δφ为负），>40 MPa时偏高；内聚力的变化趋势未从索引片段中完全确认，但摘要指出高围压下液氮冷却样品的应力阈值降低与内聚力有关 [Zhou 2022, pp. 13-17]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| σci、σcd、σp与围压呈凸非线性关系，可用Hoek-Brown方程拟合（R²≥0.932） | [Zhou 2022, pp. 5-6] | 花岗岩，加热25–400℃，水冷或液氮冷，围压0–60 MPa | 拟合参数见表2。 |
| 温度引起的σci劣化被围压抑制：0 MPa下400℃水冷σci降54.28%，60 MPa下降仅12.99% | [Zhou 2022, pp. 5-6] | 水冷，25℃至400℃ | 液氮冷类似趋势：降幅从50.36%降至23.16%。 |
| 低围压（<40 MPa）下液氮冷样品的σci、σcd、σp高于水冷样品 | [Zhou 2022, pp. 1-2] | 加热至200℃或400℃，围压0–40 MPa范围 | 数值见 Table 1。 |
| 高围压（>40 MPa）下液氮冷与水冷样品的应力阈值差异减小，甚至出现液氮冷更低 | [Zhou 2022, pp. 1-2, 13-17] | 围压50、60 MPa | 如400℃–60 MPa下液氮冷σci=417.60 MPa，水冷σci=454.50 MPa（Table 1）。 |
| 液氮冷却模型表面初始温度梯度低于水冷模型，由莱顿弗罗斯特效应所致 | [Zhou 2022, pp. 12-13] | COMSOL模拟，均质模型，换热系数液氮100 W/(m²·K)，水1000 W/(m²·K) | 大约60 s后水冷温度梯度衰减更快，液氮温度梯度持续时间更长。 |
| 热膨胀非均质性增强时，液氮冷却诱导的热应力更显著，裂纹复杂度增加 | [Zhou 2022, pp. 13-17] | 非均质模型，矿物热膨胀系数差异 | 石英、斜长石、钾长石的热膨胀系数取自Wu et al. 2019b。 |
| 等效内摩擦角φ和粘聚力c由Hoek-Brown准则估算，液氮冷与水冷的相对变化（Δφ）随围压增加由负转正 | [Zhou 2022, pp. 13-17] | 配合Table 1数据 | Δφ<0当围压<40 MPa，Δφ>0当围压>40 MPa。Δc变化不完全确认。 |

## Limitations

- 实验采用特定花岗岩，结论外推至其他岩性需谨慎 [未从索引片段中确认]。
- 液氮冷却的莱顿弗罗斯特效应在模拟中简化为固定换热系数，可能与实际复杂沸腾过程存在偏差 [Zhou 2022, pp. 12-13]。
- 围压局限于0–60 MPa，更深储层（>60 MPa）的行为未涉及。
- 仅研究了快速冷却后的静态强度，未考虑循环冷热冲击或长期效应。
- 数值模型假定弹性，未考虑裂纹萌生与扩展过程。

## Assumptions / Conditions

- 实验假定花岗岩均质、各向同性，试样无天然裂隙。
- 应力阈值确定基于Martin & Chandler (1994)的方法，要求裂纹体积应变曲线存在明确转折。
- 数值模拟中，水冷换热系数取1000 W/(m²·K)，液氮冷取100 W/(m²·K)，后者反映莱顿弗罗斯特效应抑制传热。
- Hoek-Brown准则适用于完整岩石的三轴压缩数据，参数m和s从拟合获得。
- 温度梯度和热膨胀非均质性是热损伤的主控因素，不考虑化学作用或相变。

## Key Variables / Parameters

- 岩石温度：25℃、200℃、400℃
- 冷却介质：水（25℃）、液氮（-196℃）
- 围压：σ3 = 0, 20, 40, 50, 60 MPa
- 应力阈值：σci（裂纹起始应力）、σcd（裂纹损伤应力）、σp（峰值应力），单位MPa
- 热力学与力学参数：弹性模量E、泊松比ν、导热系数、比热、热膨胀系数（均质和矿物值）
- Hoek-Brown参数：材料常数m、s，来自拟合
- Mohr-Coulomb参数：内摩擦角φ、内聚力c
- 变异系数CV，用于量化温度敏感性

## Reusable Claims

1. 对于经历热冲击的花岗岩，围压对温度引起的应力阈值劣化有显著抑制作用；例如，围压从0 MPa增至60 MPa，400℃水冷后σci的降幅由54.28%缩减至12.99% [Zhou 2022, pp. 5-6]。
2. 当换热系数因莱顿弗罗斯特效应而被压制时，液氮快速冷却对热应力的诱发可能弱于水冷，除非矿物热膨胀非均质性起主导作用 [Zhou 2022, pp. 13-17]。
3. 在低围压（<40 MPa）条件下，液氮冷却后花岗岩的强度（σci、σcd、σp）普遍高于水冷，这一现象可部分归因于体积收缩引起的裂纹闭合 [Zhou 2022, pp. 1-2, 13-17]。
4. 高围压（>40 MPa）下，冷却介质的影响反转，液氮冷却样品的强度可能低于水冷，与内聚力变化相关 [Zhou 2022, pp. 1-2, 13-17]。
5. Hoek-Brown破坏准则可有效描述加热急冷后花岗岩在不同围压下强度（σp）的非线性特征（R²>0.986），并能用于推算等效Mohr-Coulomb参数 [Zhou 2022, pp. 5-6, 13-17]。

## Candidate Concepts

- [[thermal damage]]
- [[Leidenfrost effect]]
- [[stress thresholds (σci, σcd, σp)]]
- [[Hoek-Brown failure criterion]]
- [[confining pressure effect]]
- [[temperature gradient]]
- [[thermal expansion heterogeneity]]
- [[crack closure]]
- [[internal friction angle and cohesion]]

## Candidate Methods

- [[triaxial compression test]]
- [[volumetric strain method for stress thresholds]]
- [[Hoek-Brown fitting]]
- [[COMSOL thermal-mechanical simulation]]
- [[coefficient of variation analysis]]

## Connections To Other Work

本页索引片段中未提及与其他具体论文的直接比较或引用。但从主题上，可与以下候选概念/方法关联：
- 不同冷却介质（液氮、水、空气）对热损伤的对比研究（如Wu et al. 2019a; Sha et al. 2020）。
- 莱顿弗罗斯特效应在岩石冷却中的影响（Cha et al. 2014; Tang et al. 2020）。
- 高温岩石力学性质劣化本构模型（Kumari et al. 2017b, 2018; Wang et al. 2021）。

## Open Questions

- 不同矿物组成和初始裂隙密度的花岗岩是否呈现相似的应力阈值变化规律？未从索引片段中确认。
- 循环冷热加载（多次急冷）下的损伤累积效应如何？当前研究仅单次冷却。
- 更高围压（>60 MPa）下冷却方式的差异是否持续反转？未涉及。
- 实际地热储层中，液氮注入与饱和流体的相互作用（如水蒸气爆炸）对热损伤的影响？未讨论。

## Source Coverage

本页基于提供的11个索引片段编写，覆盖论文的摘要、引言、方法、部分结果（σci和σcd的温度敏感性、围压关系、表1数据）以及讨论中的热损伤机理和围压效应分析。然而，对冷却处理的比较结果（如σcd、σp的具体差异数据、图8-10等）的定量细节缺失，仅根据片段中的摘要和表1进行推断。数值模拟的均质与非均质模型的具体应力分布图以及内聚力变化Δc的完整讨论仅部分呈现。此外，论文的结论和展望部分未在片段中体现。因此，本页对σcd和σp的详细影响以及内聚力的解释存在局限。
