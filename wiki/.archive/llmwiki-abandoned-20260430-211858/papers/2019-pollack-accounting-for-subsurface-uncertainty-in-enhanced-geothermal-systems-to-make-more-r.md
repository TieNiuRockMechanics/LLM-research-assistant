---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2019-pollack-accounting-for-subsurface-uncertainty-in-enhanced-geothermal-systems-to-make-more-r"
title: "Accounting for Subsurface Uncertainty in Enhanced Geothermal Systems to Make More Robust Techno-Economic Decisions."
status: "draft"
source_pdf: "data/papers/2019 - Accounting for subsurface uncertainty in enhanced geothermal systems to make more robust techno-economic decisions.pdf"
collections:
citation: "Pollack, Ahinoam, and Tapan Mukerji. \"Accounting for Subsurface Uncertainty in Enhanced Geothermal Systems to Make More Robust Techno-Economic Decisions.\" *Applied Energy*, vol. 254, 2019, p. 113666. doi:10.1016/j.apenergy.2019.113666."
indexed_texts: "17"
indexed_chars: "80639"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T22:46:58"
---

# Accounting for Subsurface Uncertainty in Enhanced Geothermal Systems to Make More Robust Techno-Economic Decisions.

## One-line Summary
本研究比较了单模型优化（SM-Opt）与多模型优化（MM-Opt）两种工作流在增强型地热系统（EGS）工程决策中的应用，发现在考虑地下不确定性时，MM-Opt能提供更稳健的技术经济决策。[Pollack 2019, pp. 1-2]

## Research Question
在存在地下不确定性的情况下，使用基于单一代表性储层模型的优化（SM-Opt）与使用基于多个储层模型集合的优化（MM-Opt），哪种方法能为增强型地热系统（EGS）带来更稳健的技术经济决策？[Pollack 2019, pp. 3-4]

## Study Area / Data
*   **研究地点**：一个位于加州Coso地热田的假设EGS项目。该区域岩石温度可达270°C，但地层不透水。[Pollack 2019, pp. 5-6]
*   **储层模型特征**：数值模型包含一个注入井和两侧的两个生产井。注入井和生产井之间由长度、高度和开度各异的水力裂缝（通过微地震监测识别）和一条天然断层连接。[Pollack 2019, pp. 5-6]
*   **不确定的地下参数**：研究考虑了一系列不确定的地球参数，其取值范围基于Coso现场初步勘探后的不确定性水平。[Pollack 2019, pp. 5-6] 主要参数包括：
    *   **岩石特性**：热容、热导率。岩性主要为流纹岩、闪长岩和花岗岩。[Pollack 2019, pp. 5-6]
    *   **断层特性**：断层周围热晕宽度、天然断层渗透率、孔隙度、开度。[Pollack 2019, pp. 5-6]
    *   **基质特性**：基质孔隙度。[Pollack 2019, pp. 5-6]
    *   **水力裂缝特性**：裂缝半长、裂缝开度、纵横比（平均缝高/平均缝长）、裂缝向下与向上垂直延伸的比例。[Pollack 2019, pp. 6-8]
*   **不确定的工程决策参数**：被优化的工程决策变量包括最大井口压力、生产泵功率、井间距、裂缝簇间距、井筒长度、生产井和注入井直径，以及注入井相对于天然断层的位置。[Pollack 2019, pp. 6-8]

## Methods
本研究应用了两种优化工作流：[Pollack 2019, pp. 4-4]
1.  **单模型优化（Single-Model Optimization, SM-Opt）**：
    *   **步骤**：选择不确定地球参数的平均值，创建一个被认为最具代表性的单一储层模型。然后，使用粒子群优化算法在此恒定模型上进行优化，以最大化净现值（NPV）。[Pollack 2019, pp. 4-4]
2.  **多模型优化（Multiple-Model Optimization, MM-Opt）**：
    *   **步骤**：评估地下参数的不确定性范围，并创建一个能够代表这些不确定性的储层模型集合。在此模型集合上进行优化，寻找对多种可能的地下情景都稳健的工程决策。[Pollack 2019, pp. 3-4]
    *   **具体实现**：该研究通过对变化的地球参数进行蒙特卡洛优化（穷举暴力搜索抽样）来实现。[Pollack 2019, pp. 4-4]
*   **现金流模拟**：两种工作流均通过构建流动模拟模型来模拟EGS性能，并计算其净现值（NPV）。[Pollack 2019, pp. 4-4]

## Key Findings
*   使用单一储层模型进行优化（SM-Opt）会导致过于乐观的预测。[Pollack 2019, pp. 1-2]
*   使用储层模型集合进行优化（MM-Opt）能展示出现实的净现值（NPV）不确定性范围，从而确认了更稳健的工程决策。[Pollack 2019, pp. 1-2]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 单模型优化（SM-Opt）导致过于乐观的预测。 | [Pollack 2019, pp. 1-2] | 应用于具有地下不确定性的EGS项目。 | 未从索引片段中确认具体数值结果。 |
| 多模型优化（MM-Opt）通过展示现实的NPV不确定性范围，验证了更稳健的工程决策。 | [Pollack 2019, pp. 1-2] | 应用于具有地下不确定性的EGS项目。 | 未从索引片段中确认具体数值结果。 |

## Limitations
*   本研究未考虑天然断层的走向、倾角和倾伏的不确定性，也未考虑可能存在未被现有井筒交叉的附近大型断层。[Pollack 2019, pp. 6-8]
*   研究中水力裂缝的几何形状（长度、高度、开度）被预设为不确定属性，而没有模拟压裂增产过程本身对裂缝几何形状的影响。未来的工作将包含对增产过程的模拟。[Pollack 2019, pp. 5-6]

## Assumptions / Conditions
*   **应力场假设**：在设定水力裂缝纵横比和垂直延伸比例时，假设应力场和断裂韧性是各向同性的，且结晶岩中的层理作用很小。[Pollack 2019, pp. 6-8]
*   **地质假设**：Coso地热田的断层热晕被假定为来自断层中热水流动的热源。[Pollack 2019, pp. 5-6]
*   **裂缝网络假设**：增产裂缝受到未知天然参数的控制程度，高于受增产过程本身控制的程度。[Pollack 2019, pp. 5-6]

## Key Variables / Parameters
*   **不确定地球参数**：岩石热容 (kJ/(kg⋅K))、岩石热导率 (W/(m⋅k))、断层周围热晕宽度 (m)、基质孔隙度。[Pollack 2019, pp. 5-6]
*   **不确定裂缝参数**：裂缝半长 (m)、裂缝开度 (m)、纵横比、裂缝向下/向上垂直延伸比例。[Pollack 2019, pp. 6-8]
*   **不确定天然断层参数**：渗透率 (log(md))、孔隙度、开度 (m)。[Pollack 2019, pp. 6-8]
*   **工程决策参数**：最大井口压力 (kPa)、生产泵功率 (kW)、井间距 (m)、裂缝簇间距 (m)、井筒长度 (m)、井筒直径 (m)、注入井相对于天然断层的位置。[Pollack 2019, pp. 6-8]
*   **经济指标**：净现值 (NPV)。[Pollack 2019, pp. 3-4]
*   **控制方程参数**：井筒摩擦压降公式 (dp/dz = (f_F * q^2) / (2 * ρ_w * A^2 * d)) 中的质量流量 (q)、截面积 (A)、水密度 (ρ_w)、井直径 (d) 和穆迪摩擦系数 (f_F)。[Pollack 2019, pp. 6-8]

## Reusable Claims
*   **Claim 1 (优化方法对比)**：在EGS项目中，使用单模型优化（SM-Opt，使用平均值创建单一代表性模型）会忽略不确定性范围，从而导致过于乐观的净现值（NPV）预测；相比之下，多模型优化（MM-Opt，基于不确定性范围创建模型集合）能给出包含现实不确定性范围的NPV预估，并为工程决策提供更稳健的验证。[Pollack 2019, pp. 1-2] **条件**：这一结论基于对加州Coso地热田一个假设EGS的案例研究。**限制**：MM-Opt需要比SM-Opt庞大得多的模拟次数。[Pollack 2019, pp. 3-4]
*   **Claim 2 (决策制定的信息挑战)**：在EGS开发的早期决策阶段，关键参数（如温度的空间分布、断层性质和几何形状、增产成功率）大多未知且难以预测，这使得基于成本效益分析（如确定裂缝簇密度或井筒尺寸）的工程决策高度依赖未知的岩石特性和天然裂缝分布。[Pollack 2019, pp. 3-3] **证据**：基于Coso EGS项目案例的描述。**限制**：微地震云的范围可能远大于实际的增产裂缝体积，这使得仅依靠微地震监测来指导生产井放置存在不确定性。[Pollack 2019, pp. 3-3, 4-5]

## Candidate Concepts
*   [[Enhanced Geothermal System]]
*   [[Subsurface Uncertainty]]
*   [[Robust Decision Making]]
*   [[Techno-Economic Assessment]]
*   [[Monte Carlo Optimization]]
*   [[Net Present Value]]
*   [[Sensitivity Analysis]]

## Candidate Methods
*   [[Particle Swarm Optimization]]
*   [[Monte Carlo Optimization]]
*   [[Single-Model Optimization]]
*   [[Multiple-Model Optimization]]
*   [[Reservoir Simulation]]

## Connections To Other Work
*   该研究将之前的文献工作分为两类：一类专注于在单一储层模型下优化EGS的工程决策；另一类专注于量化和降低给定数据下的地下参数不确定性。[Pollack 2019, pp. 3-4] 索引片段未提供任何直接引用本研究的后续工作。
*   可从主题上连接到以下候选概念/方法：
    *   **与不确定性量化方法的联系**：研究中提到的[[Subsurface Uncertainty]]工作流，可以连接到历史匹配方法，如[[Ensemble Kalman Filter]]和[[Markov Chain Monte Carlo]]，这些方法曾在其他地热研究（如Soultz和Superstition Mountain场地）中用于校准储层模型。[Pollack 2019, pp. 4-4]
    *   **与压裂优化的联系**：关于[[Hydraulic Fracturing]]设计优化（如裂缝间距）的决策，可以连接到使用[[Numerical Modeling]]进行成本效益分析的研究。[Pollack 2019, pp. 3-3]

## Open Questions
*   MM-Opt与SM-Opt决策结果的稳健性差异，在多大程度上取决于特定的不确定参数范围及其分布假设？[从 [Pollack 2019, pp. 5-6] 关于“典型范围”的假设推断]
*   如果模拟更真实的压裂增产过程，而非预设不确定的裂缝几何形状，两种优化方法的表现差异会如何变化？[基于 [Pollack 2019, pp. 5-6, 6-8] 指出的研究限制]
*   除了净现值（NPV）外，其他技术经济指标（如平准化度电成本LCOE或内部收益率IRR）是否会对SM-Opt和MM-Opt的选择表现出不同的敏感性？[从 [Pollack 2019, pp. 4-4] 仅使用NPV作为目标函数的局限性推断]

## Source Coverage
本知识页面严格依据提供的17个索引片段（覆盖了论文的摘要、引言、方法论、参数表和结论部分）进行编写。这些片段详细描述了研究背景、目标、不确定参数来源与取值、两种优化工作流以及主要结论。然而，索引片段**缺失**了论文的主体部分，包括：
*   **具体结果分析**：未提供任何关于净现值（NPV）的数值结果、对比图表或统计分布。
*   **讨论部分**：未提供对结果更深入的解读和影响评估。
任何非片段内容的信息均被标注为“未从索引片段中确认”。
