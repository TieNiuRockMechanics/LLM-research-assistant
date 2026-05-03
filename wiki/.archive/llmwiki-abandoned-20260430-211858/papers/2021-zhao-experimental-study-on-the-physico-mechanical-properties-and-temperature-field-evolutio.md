---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-zhao-experimental-study-on-the-physico-mechanical-properties-and-temperature-field-evolutio"
title: "Experimental Study on the Physico-Mechanical Properties and Temperature Field Evolution of Granite Subjected to Different Heating–Cooling Treatments."
status: "draft"
source_pdf: "data/papers/2021 - Experimental study on the physico-mechanical properties and temperature field evolution of granite subjected to different heating–cooling treatments.pdf"
collections:
  - "靳一作以外的"
citation: "Zhao, Zhongrui, et al. “Experimental Study on the Physico-Mechanical Properties and Temperature Field Evolution of Granite Subjected to Different Heating–Cooling Treatments.” *Bulletin of Engineering Geology and the Environment*, vol. 80, 2021, pp. 8745–8763. DOI: 10.1007/s10064-021-02466-1. Accessed 2026."
indexed_texts: "11"
indexed_chars: "53769"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T02:42:47"
---

# Experimental Study on the Physico-Mechanical Properties and Temperature Field Evolution of Granite Subjected to Different Heating–Cooling Treatments.

## One-line Summary
本研究通过实验探讨了花岗岩在加热至100～300℃后经不同温度水（0～60℃）快速冷却的物理力学性能劣化规律及内部温度场的时空演化特征。

## Research Question
不同加热温度和冷却水温差的组合如何影响花岗岩的渗透率、P波速度、单轴抗压强度、拉伸强度等物理力学指标，以及试样内部的温度、冷却速率和温度梯度的动态演化模式？ [Zhao 2021, pp. 1-2]

## Study Area / Data
实验基于实验室制备的花岗岩标准试样。力学测试采用Φ50mm × 100mm圆柱体（单轴压缩）和Φ50mm × 25mm圆盘（巴西劈裂）。天然状态下的基本物理力学参数见Table 1。温度场测试使用特制圆柱试样，其内部钻有7个孔以埋入温度传感器，传感器布置用于监测径向与轴向的温度分布。 [Zhao 2021, pp. 3-4]

**Table 1 天然花岗岩物理力学性质**
| 性质 | 值 |
|------|-----|
| 渗透率 (×10⁻¹⁸ m²) | 2.76 ± 0.21 |
| 密度 (g/cm³) | 2.60 ± 0.01 |
| P波速度 (m/s) | 4369.60 ± 48.83 |
| 单轴抗压强度 UCS (MPa) | 197.13 ± 3.02 |
| 杨氏模量 (GPa) | 35.14 ± 2.96 |
| 巴西劈裂抗拉强度 BTS (MPa) | 8.51 ± 0.92 |

[Zhao 2021, pp. 3-4]

## Methods
- **热处理与冷却方案**：加热温度为100、200、300℃，冷却水温为0、20、60℃，组成“加热温度–冷却水温”的不同处理组合。 [Zhao 2021, pp. 1-2]
- **物理力学测试**：
  - 渗透率：采用压力脉冲衰减法，使用氮气作为渗透介质，通过监测上下游压力衰减计算。 [Zhao 2021, pp. 4-6]
  - P波速度：使用NM-4B非金属超声波检测分析仪，传感器端面涂抹凡士林并施加0.2 MPa恒定压力。 [Zhao 2021, pp. 4-6]
  - 力学强度：采用300kN电液伺服试验机，以0.002 mm/s速率进行单轴压缩和巴西劈裂试验，应变通过粘贴的应变片测量。 [Zhao 2021, pp. 4-6]
- **温度场测试**：将内置热电偶的试样加热后在指定水温下快速冷却，使用Asmik R200D无纸记录仪实时采集8通道温度数据。 [Zhao 2021, pp. 4-6]
- **数值验证**：使用COMSOL Multiphysics有限元软件，对带孔装配试样与无孔完整试样的热循环过程进行模拟，以评估钻孔和填充水泥对热传导的影响。 [Zhao 2021, pp. 13-16]

## Key Findings
- 冷却水温降低会加剧花岗岩物理力学性能的热劣化：渗透率增大，P波速度、单轴抗压强度（UCS）、杨氏模量和巴西劈裂抗拉强度均呈下降趋势。 [Zhao 2021, pp. 1-2, 6-11]
- 高温花岗岩在快速冷却过程中的热传递机制为非稳态导热。 [Zhao 2021, pp. 1-2]
- 试样内部温度、冷却速率和温度梯度随时间的变化可划分为三个阶段：
  1. 前200s：快速冷却阶段；
  2. 200s～400s：缓慢冷却阶段；
  3. 400s～600s：温度基本恒定阶段。 [Zhao 2021, pp. 1-2]
- 冷却速率和温度梯度的演化趋势一致，均表现为先急剧增大后缓慢减小。 [Zhao 2021, pp. 1-2]
- 最大冷却速率和最大温度梯度始终出现在最靠近固-液换热界面的外表面区域（如监测点D处）。例如，在100℃温差范围内，最大温度梯度从100–60℃的1.75 ℃/mm增至100–0℃的4.6 ℃/mm。 [Zhao 2021, pp. 11-13, 13-16]
- 数值模拟结果证实，试样内钻孔及填充水泥对温度分布的影响可以忽略，温度场测试方案可靠。 [Zhao 2021, pp. 13-16]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 冷却水温降低，花岗岩渗透率增加、P波速度及力学强度下降。 | [Zhao 2021, pp. 1-2] | 加热100–300℃，冷却水0–60℃快速冷却。 | 物理力学性能整体劣化。 |
| 加热温度越高，快速冷却后P波速度越低；相同加热温度下，冷却水温越低，P波速度越低。 | [Zhao 2021, pp. 6-8] | 冷却水温0℃下的P波速度显著低于60℃下的值。 | 见表2具体数据。 |
| UCS随加热温度升高和冷却水温降低而减小。 | [Zhao 2021, pp. 8-11] | 300–0℃时平均UCS降至137.30 MPa。 | 室温下平均UCS为197.13 MPa。 |
| 温度场演化分快速、缓慢、恒定三阶段。 | [Zhao 2021, pp. 1-2] | 以300–0℃为例，阶段划分基于温度衰减量。 | 时间划分可能随工况略有变化。 |
| 冷却速率与温度梯度变化趋势一致，最大值在外表面附近。 | [Zhao 2021, pp. 11-16] | 径向监测点D处出现最大冷却速率；温度梯度随温差增大。 | 数值模拟验证了测试可靠性。 |

## Limitations
未从索引片段中确认。

## Assumptions / Conditions
- 试样视为均质材料，并通过剔除P波速度明显偏离平均值的试样来降低离散性影响。 [Zhao 2021, pp. 3-4]
- 快速冷却过程为自然对流冷却，冷却水温假设恒定。
- 热传递以非稳态导热为核心机制。 [Zhao 2021, pp. 1-2]
- 温度场测试中，钻孔和填充水泥对热传导的干扰经数值验证可忽略。 [Zhao 2021, pp. 13-16]

## Key Variables / Parameters
- **自变量**：加热温度 (100, 200, 300℃)；冷却水温 (0, 20, 60℃)。
- **因变量**：渗透率 (k, ×10⁻¹⁸ m²)；P波速度 (m/s)；单轴抗压强度 UCS (MPa)；杨氏模量 E (GPa)；巴西劈裂抗拉强度 BTS (MPa)；试样内部各点温度 (°C)；冷却速率 dT/dt (°C/s)；温度梯度 (°C/mm)。
- **控制因素**：试样尺寸 (Φ50mm×100mm, Φ50mm×25mm)；加载速率 (0.002 mm/s)；时间阶段划分 (0-200s, 200-400s, 400-600s)。 [Zhao 2021, pp. 3-4, 11-13]

## Reusable Claims
- 当冷却水温从60℃降至0℃，高温花岗岩快速冷却后的物理力学劣化效应显著增强，表现为渗透率增大、P波速度与强度指标下降。此结论适用于100-300℃加热、0-60℃水冷的实验条件，且试样越接近固-液界面，损伤越重。 [Zhao 2021, pp. 1-2, 6-11]
- 快速冷却过程中的内部温度场演化呈典型三阶段特征：0-200s降温剧烈，200-400s降温趋缓，400s后接近平衡。应用于非稳态导热分析时，可据此划分热应力主导时段。 [Zhao 2021, pp. 1-2]
- 冷却速率和温度梯度的时空分布高度同步，均在外表面附近先急升后缓降。此规律可为地热井筒或储层热冲击中的裂纹萌生位置预测提供依据。 [Zhao 2021, pp. 11-13]
- 在试样内部埋设温度传感器并辅以数值模型验证，是一种可行的花岗岩内部温度场测试方法，前提是钻孔直径小且填充物导热特性与岩石接近。 [Zhao 2021, pp. 13-16]

## Candidate Concepts
- [[thermal shock cracking]]
- [[geothermal wellbore stability]]
- [[unsteady heat conduction]]
- [[temperature gradient in rock]]
- [[granite thermal treatment]]
- [[P-wave velocity decay]]
- [[permeability enhancement by cooling]]
- [[rapid cooling stage]]
- [[solid-liquid heat transfer interface]]

## Candidate Methods
- [[pressure pulse decay permeability test]]
- [[ultrasonic P-wave velocity measurement]]
- [[uniaxial compression test with strain gauges]]
- [[Brazilian disc tensile test]]
- [[embedded thermocouple temperature monitoring]]
- [[COMSOL finite element thermal simulation]]
- [[natural convection cooling experiment]]

## Connections To Other Work
未从索引片段中确认直接的文献对比或连接关系。从主题上，本研究可与[[thermal stimulation in geothermal reservoirs]]、[[cooling-induced microcracks]]、[[heating-cooling cyclic degradation of rock]]等概念领域相关联，后续可重点比对液态氮激冷等极端冷却研究。

## Open Questions
未从索引片段中确认。可能包括：长时间循环下的累积损伤规律；冷却水温低于0℃（如冰水或液态氮）的影响；微观裂纹定量表征与宏观力学参数变化的关联等。

## Source Coverage
本页依据11个索引片段编写，覆盖论文摘要、实验方法、部分结果、温度场分析及讨论。片段的覆盖面偏向结果与温度场演化，对完整的讨论、结论、致谢及可能存在的机理分析细节覆盖不足。
