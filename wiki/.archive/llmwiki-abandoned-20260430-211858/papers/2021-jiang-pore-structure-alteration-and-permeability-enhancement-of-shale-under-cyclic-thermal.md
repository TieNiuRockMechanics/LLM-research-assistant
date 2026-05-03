---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-jiang-pore-structure-alteration-and-permeability-enhancement-of-shale-under-cyclic-thermal"
title: "Pore Structure Alteration and Permeability Enhancement of Shale under Cyclic Thermal Impacts."
status: "draft"
source_pdf: "data/papers/2022 - Pore structure alteration and permeability enhancement of shale under cyclic thermal impacts.pdf"
collections:
  - "论文"
citation: "Jiang, Changbao, et al. \"Pore Structure Alteration and Permeability Enhancement of Shale under Cyclic Thermal Impacts.\" 2021."
indexed_texts: "9"
indexed_chars: "43716"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T11:12:49"
---

# Pore Structure Alteration and Permeability Enhancement of Shale under Cyclic Thermal Impacts.

## One-line Summary
在300°C的循环热冲击下，页岩内部孔隙持续生成和扩张，其累积孔隙率和渗透率随热冲击次数呈对数函数增长，验证了多次热冲击对于改善页岩储层渗透性的重要性 [Jiang 2021, pp. 1-1, 8-9]。

## Research Question
循环热冲击（cyclic thermal impacts）技术如何改变页岩的孔隙结构并提高其渗透率？ [Jiang 2021, pp. 1-1]

## Study Area / Data
实验样本为从同一完整天然页岩块沿平行层理方向钻取的、无明显裂纹的标准页岩试样（直径25 mm × 50 mm）[Jiang 2021, pp. 2-4]。样本的超声速度范围为3.79–3.91 km/s [Jiang 2021, pp. 2-4]。具体页岩产地或层位未从索引片段中确认。

## Methods
- **热处理**：使用马弗炉进行循环热冲击。将样本放入已从室温预热至设定温度的马弗炉中，加热特定时间直到样本核心温度达到预设温度的90%以上，然后取出在炉中冷却至室温，此全过程定义为一次热冲击 [Jiang 2021, pp. 2-4]。热冲击温度选定为300°C [Jiang 2021, pp. 2-4]。
- **孔隙结构分析**：使用ASAP2010比表面积与孔隙度分析仪和MacroMR12-150H-I核磁共振（NMR）测试系统，对比热冲击前后的孔隙结构变化 [Jiang 2021, pp. 2-4, 5-7]。
- **渗透率测试**：使用脉冲孔隙度测试仪，测量范围10^-5–10^3 mD [Jiang 2021, pp. 2-4]。
- **数据分析**：
    - **累积孔隙率增加量 (λc)**：定义为热冲击后与热冲击前累积孔隙率的差值与冲击前累积孔隙率的百分比。公式：`λc = (φa - φb) / φb * 100%` [Jiang 2021, pp. 5-7]。
    - **绝对渗透率增加量 (λa)**：定义为第i次热冲击后渗透率与初始渗透率的差值与初始渗透率的百分比。公式：`λa = (ki - k0) / k0 * 100%` [Jiang 2021, pp. 7-8]。
    - **相对渗透率增加量 (λr)**：定义为相邻两次（i和i-2次）热冲击间渗透率的差值与（i-2）次后渗透率的百分比（首次冲击时`i=1`，与初始值比较）。公式：`λr = (ki - ki-2) / ki-2 * 100%`，`λr = (ki - k0) / k0 * 100% (i=1)` [Jiang 2021, pp. 7-8]。

## Key Findings
1.  根据IUPAC分类，页岩的氮气吸附-脱附回滞环属于H3型并兼具H2型特征，表明其内部以开放孔（如平行板孔和两端开口的圆柱孔）为主，伴生少量“墨水瓶”孔 [Jiang 2021, pp. 4-5]。原始页岩样品的平均比表面积为31.680 m²/g，平均孔容为0.0285 cm³/g，平均孔径为7.209 nm [Jiang 2021, pp. 4-5]。
2.  在300°C热冲击下，页岩中的孔隙持续生成和扩大。随着热冲击次数增加，页岩的累积孔隙率逐渐增加，其增长趋势是热冲击次数的对数函数 [Jiang 2021, pp. 1-1, 8-9]。
3.  与单次热冲击相比，多次热冲击的效果成倍增加 [Jiang 2021, pp. 8-9]。
4.  循环热冲击可有效提高页岩渗透率，且渗透率随热冲击次数的对数增加 [Jiang 2021, pp. 8-9]。渗透率增加量随热冲击次数的增加而减小 [Jiang 2021, pp. 7-8]。
5.  多次热冲击下的渗透率增量效果相比单次冲击呈指数级提升 [Jiang 2021, pp. 8-9]。例如，经过7次热冲击，试样B1的渗透率增加了58.2%，B2的渗透率增加了35.9% [Jiang 2021, pp. 7-8]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 累积孔隙率随热冲击次数呈对数函数增长 | [Jiang 2021, pp. 1-1, 8-9] | 温度：300°C | 多次冲击效果相比单次成倍增加。 |
| 渗透率随热冲击次数呈对数增长 | [Jiang 2021, pp. 8-9] | 温度：300°C | 多次冲击效果相比单次呈指数级提升。 |
| 首次热冲击的相对渗透率增加量为28.02%，随后增量下降 | [Jiang 2021, pp. 7-8] | 试样B1，300°C | 后续的渗透率增量随着冲击次数的增加而减小。 |
| 七次热冲击后，两试样的渗透率分别增加了58.2%和35.9% | [Jiang 2021, pp. 7-8] | 试样B1、B2，300°C | B1: 4.816 × 10^-18 m² 增至 7.620 × 10^-18 m²；B2: 5.296 × 10^-18 m² 增至 7.195 × 10^-18 m²。 |
| 原始页岩平均比表面积为31.680 m²/g，平均孔容0.0285 cm³/g，平均孔径7.209 nm | [Jiang 2021, pp. 4-5] | 试样C1-C3的氮气吸附-脱附测试 | |
| 原始页岩以开放孔为主，孔隙类型主要为平行板和墨水瓶状 | [Jiang 2021, pp. 4-5] | 根据H3/H2型回滞环判断 | |

## Limitations
- 实验是在实验室特定条件下（300°C）进行的，其结果外推至其他温度和实际现场条件时存在不确定性。
- 未从索引片段中确认样本数量及其离散性对结论统计显著性的影响。
- 未从索引片段中确认实验是否考虑了其他地质因素（如围压、流体饱和度）的影响。
- 未从索引片段中确认该技术在长期或更大尺度上的效果和潜在负面效应（如诱导的地质力学失稳）。

## Assumptions / Conditions
- 该研究基于实验室规模的标准页岩试样，并假定对均质、无显著裂纹的初始试样进行处理 [Jiang 2021, pp. 2-4]。
- 热冲击实验的条件是温度从室温突变至300°C并冷却 [Jiang 2021, pp. 2-4]。
- 孔隙率和渗透率的变化模型（对数增长）适用于该温度-材料组合所经历的循环次数范围。
- 渗透率增加量的计算基于定义的公式 (6)、(7)、(8) [Jiang 2021, pp. 7-8]。

## Key Variables / Parameters
-   `λc`： 累积孔隙率增加量 (%) [Jiang 2021, pp. 5-7]
-   `λa`： 绝对渗透率增加量 (%) [Jiang 2021, pp. 7-8]
-   `λr`： 相对渗透率增加量 (%) [Jiang 2021, pp. 7-8]
-   **热冲击温度** (300°C) [Jiang 2021, pp. 1-1]
-   **热冲击次数** [Jiang 2021, pp. 1-1]
-   **渗透率** (m²) [Jiang 2021, pp. 7-8]
-   **孔隙类型** (比表面积、孔容、孔径) [Jiang 2021, pp. 4-5]
-   **吸附孔、滑移孔** [Jiang 2021, pp. 5-7]

## Reusable Claims
1.  **Claim**：在300°C条件下对页岩进行循环热冲击，其累积孔隙率和渗透率的增长趋势是热冲击次数的对数函数。**Conditions**: 实验室无围压条件，室温至300°C循环，均质页岩试样。**Evidence**: 实验结果和结论 [Jiang 2021, pp. 1-1, 8-9]。**Limitations**: 仅适用于该温度，未确认对其他页岩类型的普适性。
2.  **Claim**：利用核磁共振(NMR)技术可观测到，多次热冲击（尤其是5次以上）能显著增加页岩中的滑移孔数量，并促使部分滑移孔扩张。**Conditions**: 300°C热冲击，NMR分析。**Evidence**: NMR T2谱和孔径分布变化 [Jiang 2021, pp. 5-7]。**Limitations**: 观测基于特定实验装置和试样。
3.  **Claim**：多次循环热冲击在提升页岩渗透率方面的效果显著优于单次冲击，其渗透率增量可以是指数级的。**Conditions**: 基于定义的绝对和相对渗透率增加量指标进行对比。**Evidence**: 多次冲击效果成倍或指数级增加的结论 [Jiang 2021, pp. 8-9]。**Limitations**: 结论基于300°C下的实验室数据。

## Candidate Concepts
- [[cyclic thermal impact]]
- [[shale reservoir]]
- [[permeability enhancement]]
- [[pore structure alteration]]
- [[nuclear magnetic resonance (NMR)]]
- [[adsorption-desorption hysteresis loop]]
- [[water phase trap]]
- [[formation heat treatment (FHT)]]

## Candidate Methods
- [[Nuclear Magnetic Resonance (NMR) pore size analysis]]
- [[Nitrogen adsorption-desorption (BET/BJH analysis)]]
- [[Pulse decay permeability measurement]]
- [[Muffle furnace thermal treatment]]
- [[IUPAC hysteresis loop classification]]

## Connections To Other Work
- 该方法与页岩气增产改造技术存在关联，例如 [[formation heat treatment (FHT)]] [Jiang 2021, pp. 9-9]，以及微波辐射 [Jiang 2021, pp. 1-2]、注水蒸汽热解 [Jiang 2021, pp. 1-2] 等其他热激发手段。
- 研究延续了对岩石热冲击效应的关注，前人已在煤样上进行了冷热冲击研究，并观察到对渗透率的显著增强效果 [Jiang 2021, pp. 1-2]。
- 研究参考了温度对页岩物理性质影响的文献 [Jiang 2021, pp. 2-4]，将研究焦点从传统的缓慢变温影响转向温度突变造成的热冲击效应 [Jiang 2021, pp. 1-2]。

## Open Questions
- 对于不同矿物组成和有机质丰度的页岩，其孔隙率和渗透率的对数增长规律是否具有普适性？
- 最佳的循环热冲击温度、升温/冷却速率、单次作用时间和循环次数组合是什么，以平衡增产效果和能耗/安全？
- 在有真实应力约束的地下条件中，热冲击产生的微裂缝网络和渗透率提升效果会如何变化？
- 多次循环热冲击是否会诱发宏观破裂，从而影响井筒稳定性或导致储层出砂？
- 除了消除水相圈闭，热冲击通过何种具体机制改变了气体在纳米孔中的吸附-解吸行为？

## Source Coverage
本页面仅基于提供的9个索引片段构建，主要涵盖论文的摘要（pp. 1-1）、引言（pp. 1-2）、实验材料与方法（pp. 2-4）、部分结果与分析（氮气吸附 pp. 4-5, NMR pp. 5-7, 渗透率 pp. 7-8）以及结论（pp. 8-9）。内容侧重于方法和主要发现，但缺失了对结果更详细的讨论、与其他研究的具体量化对比、所有图表数据以及完整的参考文献列表。因此，关于实验的细节、具体数值的统计特性、讨论部分的深入解释等信息可能存在缺失。
