---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2007-an-three-dimensional-thermal-structure-of-the-chinese-continental-crust-and-upper-mantle"
title: "Three-Dimensional Thermal Structure of the Chinese Continental Crust and Upper Mantle."
status: "draft"
source_pdf: "data/papers/2007 - Three-dimensional thermal structure of the Chinese continental crust and upper mantle.pdf"
collections:
  - "山西断裂地质构造"
citation: "An, Meijian, and Yaolin Shi. \"Three-Dimensional Thermal Structure of the Chinese Continental Crust and Upper Mantle.\" *Science in China Series D: Earth Sciences*, vol. 50, no. 10, 2007, pp. 1441-51. doi:10.1007/s11430-007-0071-3."
indexed_texts: "10"
indexed_chars: "47943"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T12:38:21"
---

# Three-Dimensional Thermal Structure of the Chinese Continental Crust and Upper Mantle.

## One-line Summary
利用 S 波速度模型 CN03S 反演中国大陆上地幔温度，将 1300 °C 绝热线对应为地震低速带顶部，并以反演所得上地幔温度与地表温度为边界条件求解稳态热传导方程获得地壳温度，借此构建出地壳与上地幔的三维温度场，并通过与观测地表热流的比较检验模型可靠性 [An 2007, pp. 1-2]。

## Research Question
中国大陆地壳及上地幔（至约 240 km 深度）的三维温度结构是怎样的？从地震速度导出的温度分布与过去基于地表热流和稳态假设的岩石圈热模型有何差异 [An 2007, pp. 2-3]？

## Study Area / Data
- **研究区**：中国大陆（包括主要块体，如华北克拉通、鄂尔多斯盆地、四川盆地、塔里木克拉通、羌塘地体、青藏高原等）[An 2007, pp. 1-2][An 2007, pp. 4-6]。
- **地震速度数据**：3D S 波速度模型 CN03S，由面波层析成像获得（周期 10‑184 s，超过 4000 条射线路径，水平分辨率 4°‑6°）[An 2007, pp. 3-4]。使用深度范围 70‑240 km 的速度值。
- **地表热流数据**：用于模型检验（克里格插值获得区域热流分布，并附有观测质量评估）[An 2007, pp. 5-6][An 2007, pp. 8-9]。
- **地表温度**：作为地壳温度计算的顶部边界条件 [An 2007, pp. 1-2]。
- **矿物成分模型**：非克拉通成分（off-cratonic composition），具体为 68% 橄榄石、18% 斜方辉石、11% 单斜辉石、3% 石榴石，铁含量 0.1 [An 2007, pp. 3-4]。

## Methods
- **地震‑热转换**：基于 Goes et al. (2000) 提出的方法，根据实验室数据建立弹性参数和密度随温度、压力与成分的变化关系，从 CN03S 模型的 S 波速度直接反演上地幔温度。假定在 50‑250 km 深度范围内温度是控制地震速度的主导因素 [An 2007, pp. 2-3]。
- **地壳温度计算**：将反演得到的 80 km 深处温度与地表温度作为边界条件，求解稳态热传导方程，获得 80 km 以浅的地壳温度分布，并据此计算地表热流 [An 2007, pp. 1-2]。
- **模型评估**：比较计算地表热流与观测地表热流，计算偏差，作为模型的外部检验 [An 2007, pp. 5-6]。
- **流体效应处理**：由于缺乏深切部的流体分布模型，未考虑流体对速度的影响，因此反演温度为上限估计 [An 2007, pp. 3-4]。

## Key Findings
- **地壳温度分布**：深度 25 km 处，中国东部温度较高（500‑600 °C），西部普遍低于 500 °C，其中塔里木克拉通最低（约 460 °C）；西部地壳结构复杂，地壳温度可靠程度低于东部 [An 2007, pp. 1-2][An 2007, pp. 8-9]。
- **上地幔温度分布**  
  - 100 km 深度：东部和东南部温度高于 1300 °C 绝热线，西部则普遍低于绝热线；塔里木克拉通和四川盆地呈显著低温 [An 2007, pp. 1-2]。  
  - 150 km 深度：华南、扬子克拉通东部、华北克拉通和羌塘地体周围温度高于 1300 °C，四川盆地和印度‑欧亚碰撞带附近温度最低 [An 2007, pp. 1-2]。  
  - 200 km 深度：青藏高原南部及塔里木克拉通以南出现极低温度 [An 2007, pp. 1-2]。
- **与传统热模型的比较**：在华北克拉通、鄂尔多斯盆地和四川盆地，本模型与基于地表热流稳态假定的模型在 1300 °C 绝热线穿越深度上较为一致；但在塔里木克拉通和羌塘地体存在显著差异（如塔里木深部温度差异可达 260 °C），反映了稳态假设在这些区域的局限性 [An 2007, pp. 5-6][An 2007, pp. 6-8]。
- **模型检验结果**：大部分地区计算与观测地表热流的偏差小于 20%；青藏高原大量热流测量为 D 级质量，难以代表区域热状态，因此该区的大偏差不构成对模型的否定 [An 2007, pp. 8-9]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 东部 25 km 深度温度 500‑600 °C，西部 <500 °C，塔里木低至 ~460 °C | [An 2007, pp. 8-9] | 基于 S 波速度反演与稳态地壳热传导；西部可信度较低 | 静态稳态近似 |
| 100 km 深度东部和东南部温度高于 1300 °C 绝热线，西部低，塔里木、四川盆地低温 | [An 2007, pp. 1-2] | 非克拉通成分假设，忽略流体 | 1300 °C 绝热线作为热岩石圈底部参考温度 |
| 150 km 深度华南、扬子东部、华北、羌塘周围温度 >1300 °C，四川盆地和碰撞带最低 | [An 2007, pp. 1-2] | 同上 | |
| 200 km 深度青藏高原南部和塔里木南出现极低温度 | [An 2007, pp. 1-2] | 模型在该深度分辨率已降低（≥250 km 不可靠） | 可能受到物质不均一影响 |
| 四川盆地本模型与 Wang (1996) 的稳态模型在 1300 °C 绝热线穿越深度均约 180 km，但在 40‑100 km 深度差约 150 °C | [An 2007, pp. 5-6] | 四川盆地相对稳定 | 深部温度差异来自约束方式不同 |
| 塔里木克拉通本模型与 Wang 模型差异显著（~150 °C @40 km, ~260 °C @70 km），1300 °C 绝热线穿越深度相差约 85 km | [An 2007, pp. 6-8] | 复杂构造区 | 稳态假设失效可能性大 |
| 计算与观测地表热流偏差多数区域 <20% | [An 2007, pp. 8-9] | 密集且高质量热流测量的区域 | 作为模型有效性评估 |

## Limitations
- 速度模型 CN03S 在 ≥250 km 深度分辨率差，仅采用 70‑240 km 的速度 [An 2007, pp. 3-4]。
- 反演未考虑流体对地震速度的影响，导致温度为上限估计 [An 2007, pp. 3-4]。S 波速度的不确定性（<0.1 km/s）可引起温度变化 50‑250 °C [An 2007, pp. 3-4]。
- 地壳温度通过稳态热传导方程求取，对 80 km 以下仅为一级近似；西部地壳结构复杂，地壳温度可靠性较低 [An 2007, pp. 8-9][An 2007, pp. 9-10]。
- 在构造不稳定区（如青藏高原），实测热流的代表性差，检验能力有限 [An 2007, pp. 8-9]。
- 没有给出完整的矿物成分变化对温度影响的敏感性分析（仅采用单一非克拉通成分）[未从索引片段中确认]。

## Assumptions / Conditions
- 在 50‑250 km 深度，温度是影响地震速度的主导因素，成分和部分熔融的影响可暂不考虑 [An 2007, pp. 2-3]。
- 地壳温度计算假设稳态热传导，并使用统一的热导率等参数（来自 Artemieva & Mooney 2001）[An 2007, pp. 4-5]。
- 上地幔矿物组成按非克拉通成分计算，即 68% 橄榄石、18% 斜方辉石、11% 单斜辉石、3% 石榴石，铁含量 0.1 [An 2007, pp. 3-4]。
- 1300 °C 绝热线被视为热岩石圈底部温度的参考标志 [An 2007, pp. 1-2]。
- 流体效应可忽略或将其归入温度效应中 [An 2007, pp. 3-4]。
- 计算地表热流时，选用来自前人文献的热导率和生热率值，下地壳和上地幔的热导率为 2.5 W m⁻¹ K⁻¹ [An 2007, pp. 4-5]。

## Key Variables / Parameters
- S 波速度（来自 CN03S 模型）[An 2007, pp. 3-4]
- 上地幔温度及 1300 °C 绝热线深度 [An 2007, pp. 1-2]
- 地壳温度（25 km、80 km 等深度）[An 2007, pp. 8-9]
- 地表温度和地表热流 [An 2007, pp. 1-2]
- 热导率和生热率（取自文献）[An 2007, pp. 4-5]
- 矿物比例（橄榄石 68%，斜方辉石 18%，单斜辉石 11%，石榴石 3%）及铁含量 [An 2007, pp. 3-4]
- 岩石圈厚度（与 1300 °C 绝热线相交深度）[An 2007, pp. 1-2]

## Reusable Claims
- 利用三维 S 波速度场结合矿物物理实验室数据可以反演上地幔温度；当忽略流体对速度的影响时，所得温度为实际温度的上限估计 [An 2007, pp. 3-4]。
- 对于构造－热年龄较轻的区域，采用 off-cratonic 矿物成分（如 Ol 68% Opx 18% Cpx 11% Gt 3%）比克拉通成分更符合真实情况 [An 2007, pp. 3-4]。
- 以地震速度导出的上地幔温度和地表温度为边界条件，求解稳态热传导方程可给出地壳温度的一级近似，其可靠性取决于构造稳定性与参数约束 [An 2007, pp. 9-10]。
- 用计算地表热流与高质量观测热流的偏差作为温度模型的检验手段，在多数地区偏差小于 20% 可视为模型可靠 [An 2007, pp. 8-9]。
- 在构造活跃或深部过程复杂地区（如塔里木、羌塘），传统基于地表热流和稳态假设的温度剖面可能与实际差距较大，地震‑热方法可提供互补约束 [An 2007, pp. 6-8]。

## Candidate Concepts
- [[seismic velocity]]
- [[upper mantle temperature]]
- [[thermal lithosphere]]
- [[off-cratonic composition]]
- [[S-wave tomography]]
- [[steady-state thermal conduction]]
- [[surface heat flow]]
- [[1300 °C adiabat]]
- [[lithospheric thickness]]
- [[misfit between calculated and observed heat flow]]

## Candidate Methods
- [[seismic-thermal method]]
- [[3D S-wave velocity inversion]]
- [[steady-state heat conduction equation]]
- [[surface heat flow comparison]]
- [[fundamental-mode Rayleigh wave dispersion tomography]]

## Connections To Other Work
- 地震速度模型源自 Huang et al. (2003) 的 CN03S 面波层析成像 [An 2007, pp. 3-4]。
- 与传统基于地表热流稳态假定的模型进行了系统对比，涉及 Wang (1996) [3], Chi & Yan (1998) [28], Liu et al. (2000) [29] 等先前的热结构研究 [An 2007, pp. 4-6]。
- 热导率和生热率参数引用了 Artemieva & Mooney (2001) [1] [An 2007, pp. 4-5]。
- 地震‑热转换方法基于 Goes et al. (2000) [14] 的框架，并在欧洲和北美有过类似应用 [An 2007, pp. 2-3]。
- 本研究的结果可用于进一步约束 [[tectonic interactions between blocks]]、[[mantle convection]] 以及 [[Phanerozoic craton reworking]] 等动力学问题。

## Open Questions
- 流体在深部（>80 km）的分布及其对地震速度的影响尚未被纳入模型，这会对温度反演引入多大偏差？[An 2007, pp. 3-4]
- 塔里木克拉通等地区的上地幔可能已经受到强烈的改造，其成分是否偏离 off-cratonic 假设？[An 2007, pp. 2-3][An 2007, pp. 6-8]
- 青藏高原地表热流数据严重不足且质量偏低，如何获得该区域更可靠的深部热约束？[An 2007, pp. 8-9]
- 200 km 深度出现的极低温度是否指示了小尺度对流或板块俯冲残留？[An 2007, pp. 1-2]

## Source Coverage
本页面依据 10 个索引片段，覆盖了文章摘要、方法、部分结果（1‑D 温度剖面和不同深度的温度平面图）、与先前研究的对比及主要结论。索引片段包含了引言和讨论部分的关键论述。缺少完整的区域细节描述（如各块体的具体热导率、生热率表格）以及全部图件的详细说明。对青藏高原和塔里木以外的其他地区（如华南、扬子东部）的数据讨论可能不够充分。因此，某些定量细节（如所有对比模型的精确数值）仍需借助完整原文进一步确认。
