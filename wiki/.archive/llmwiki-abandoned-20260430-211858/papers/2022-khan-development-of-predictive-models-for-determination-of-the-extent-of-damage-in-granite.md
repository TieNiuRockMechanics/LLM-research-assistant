---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2022-khan-development-of-predictive-models-for-determination-of-the-extent-of-damage-in-granite"
title: "Development of Predictive Models for Determination of the Extent of Damage in Granite Caused by Thermal Treatment and Cooling Conditions Using Artificial Intelligence."
status: "draft"
source_pdf: "data/papers/2022 - Development of Predictive Models for Determination of the Extent of Damage in Granite Caused by Thermal Treatment and Cooling Conditions Using Artificial Intelligence.pdf"
collections:
  - "论文"
citation: "Khan, Naseer Muhammad, et al. “Development of Predictive Models for Determination of the Extent of Damage in Granite Caused by Thermal Treatment and Cooling Conditions Using Artificial Intelligence.” *Mathematics*, vol. 10, no. 16, 2022, Article 2883. doi:10.3390/math10162883."
indexed_texts: "17"
indexed_chars: "81145"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T04:05:02"
---

# Development of Predictive Models for Determination of the Extent of Damage in Granite Caused by Thermal Treatment and Cooling Conditions Using Artificial Intelligence.

## One-line Summary

本研究旨在利用多元线性回归、人工神经网络和自适应神经模糊推理系统，基于物理性质预测不同冷却条件下热损伤花岗岩的损伤程度，并通过多指标比较评估各模型的预测性能 [Khan 2022, pp. 3-4]。

## Research Question

现有研究在以下方面存在不足：基于孔隙率预测缓慢和快速冷却条件下损伤程度/损伤因子的研究，选择优化神经元以获得最佳结果的研究，人工智能中不同算法函数的比较分析，以及人工神经网络性能不佳的问题。因此，本研究的核心问题是针对非砂岩岩石，利用统计和人工智能方法预测热损伤程度，具体研究利用花岗岩的物理性质（孔隙率、密度、温度和P波速度）作为输入变量，通过MLR、ANN和ANFIS技术来预测热损伤因子（DT），并评估哪个模型最为有效 [Khan 2022, pp. 3-4]。

## Study Area / Data

**研究样本**：
- **岩石类型**：花岗岩，具体为寒武纪至奥陶纪的斯瓦特花岗片麻岩（Swat Granite Gneisses），属于变质沉积岩 [Khan 2022, pp. 4-5]。
- **样品来源**：来自巴基斯坦的斯瓦特地区，按分布区域包括由晚元古代至中晚中生代的地层及晚石炭纪至二叠纪的Ambela和Shewa火成岩杂岩体 [Khan 2022, pp. 4-5]。
- **样品形态**：使用了花岗岩卵石 [Khan 2022, pp. 4-5]。
- **实验流程**：对岩石样品进行热处理及后续冷却（缓慢冷却和快速冷却），并在处理前后测试其物理性质。每种物理性质（密度、孔隙率、P波和弹性模量）在热处理及后续冷却前后各进行了十次实验运行 [Khan 2022, pp. 4-5]。
- **数据特征**：研究结果中给出了热处理和不同冷却条件后花岗岩样本的密度、孔隙率和P波的平均值 [Khan 2022, pp. 4-5]。

## Methods

本研究采用了三种建模技术来预测热损伤因子：
1.  **多元线性回归**
    - 使用多个预测变量进行建模，其广义方程形式为：`W = C + b1z1 + b2z2 + b3z3 + ... + bnzn`，其中 `W` 是因变量，`C` 是常数，`z1` 到 `zn` 是自变量，`b1` 到 `bn` 是偏回归系数 [Khan 2022, pp. 5-7]。
2.  **人工神经网络**
    - **网络生成**：共生成了2000个网络，针对不同的训练算法，每种算法500个网络 [Khan 2022, pp. 8-10]。
    - **模型设计**：采用含有切线S型激活函数的前馈反向传播网络。测试了5种训练函数，神经元数量最多可达100个 [Khan 2022, pp. 8-10]。
    - **代码实现**：在MATLAB中编译了自定义代码，引入循环函数以运行指定数量的网络。在单次执行中代码运行了100个网络；每个网络中的神经元数量依次递增：网络1有1个神经元，网络2有2个神经元，以此类推。隐藏层和输出层使用相同的激活函数 [Khan 2022, pp. 8-10]。
    - **算法选择**：为选出最优训练函数，评估了五种不同的训练函数：BFG, RP, SCG, CGB, 和 LM [Khan 2022, pp. 10-12]。
3.  **自适应神经模糊推理系统**
    - **FIS类型**：采用Sugeno模糊推理系统，因其计算效率优于Mamdani型 [Khan 2022, pp. 7-8]。
    - **学习算法**：采用混合优化方法，因其具有较高的预测结果 [Khan 2022, pp. 7-8]。
    - **模型结构**：ANFIS模型由五层组成 [Khan 2022, pp. 7-8]。其模糊规则在训练过程中形成，形式为“如果S是J1且y是P1，则Z1 = D1x + F1y + Q1” [Khan 2022, pp. 7-8]。

模型的性能评估指标包括：
- 平均绝对百分比误差
- 决定系数
- A20指数
- 方差解释率
- 均方根误差 [Khan 2022, pp. 3-4]

## Key Findings

1.  **ANN算法性能比较**：在五种训练函数中，LM训练函数的整体效率非常高，其决定系数、均方根误差、神经元数量和执行时间均优于其他函数。LM函数的数据收敛速度更快 [Khan 2022, pp. 10-12]。
2.  **ANN预测效果**：对于DT的预测，LM函数基于孔隙率（在缓慢和快速冷却下）的效率（以RMSE衡量）优于基于弹性的效率 [Khan 2022, pp. 10-12]。
3.  **模型对比（基于已有文献）**：先前研究表明，ANFIS模型在预测热损伤程度（如从弹性模量预测）方面，比MLR和ANN模型更合适，性能更好 [Khan 2022, pp. 3-4]。此外，有研究指出ANFIS模型的预测效率高于人工神经网络 [Khan 2022, pp. 3-4]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| LM训练函数的整体效率（R2, RMSE, 神经元数量, 执行时间）优于BFG, RP, SCG, CGB。LM使数据收敛更快。 | [Khan 2022, pp. 10-12] | 用于预测花岗岩热损伤因子DT的ANN模型。模型为前馈反向传播网络，使用切线S型激活函数，最多100个神经元。 | 此比较是在ANN模型内部进行，以选择最佳训练函数。 |
| 对于基于孔隙率的DT预测，LM函数的RMSE表现优于基于弹性的DT预测，无论冷却方式快慢。 | [Khan 2022, pp. 10-12] | 花岗岩样本，在缓慢和快速冷却条件下。 | 表明基于孔隙率作为输入时，ANN的预测误差更小。 |
| 软计算方法比统计方法更准确地预测力学特性。ANFIS模型的预测效率高于ANN。 | [Khan 2022, pp. 3-4] | 此结论源自研究[66]，针对细粒印度砂岩，热处理温度最高至1000°C，缓慢冷却，使用孔隙率、波速等参数预测。 | 该结论并非本研究直接产生，而是作为本研究的基础和出发点。 |
| ANFIS模型在预测热损伤程度方面比MLR和ANN更合适。 | [Khan 2022, pp. 3-4] | 此结论源自研究[66]，针对细粒印度砂岩，预测从弹性模量推断的损伤程度。 | 该结论是引述的前人研究，为本研究的立题依据之一。 |

## Limitations

- **模型收敛速度**：尽管ANFIS模型性能优异，但其收敛速度可能因高“如果-且-或”关系而变慢 [Khan 2022, pp. 7-8]。
- **未从索引片段中确认**的研究局限性：索引片段未提供本研究自身的局限性讨论，例如样本的均一性、温度范围和冷却速率的普适性、模型外推至其他岩类的有效性、数据集大小是否足够等。

## Assumptions / Conditions

- **模型设计假设**：ANN模型设计基于前馈反向传播网络与切线S型激活函数的组合 [Khan 2022, pp. 8-10]。
- **ANFIS系统选择**：研究假设Sugeno型FIS比Mamdani型FIS在计算上更高效，因此选择了前者 [Khan 2022, pp. 7-8]。
- **实验条件**：岩石样本按照国际岩石力学学会的标准进行制备和测试 [Khan 2022, pp. 4-5]。实验涉及热处理和两种冷却条件：缓慢冷却和快速冷却 [Khan 2022, pp. 3-4]。
- **外部条件假设（来自文献）**：岩石在工程项目中（如地下煤气化、地热资源等）会长时间暴露于500至1500°C的高温环境 [Khan 2022, pp. 2-3]。

## Key Variables / Parameters

- **输入变量**：
    - 孔隙率）
    - 密度）
    - 温度
    - P波速度）[Khan 2022, pp. 3-4, 4-5]
- **输出/预测目标变量**：
    - 热损伤因子）
- **热损伤因子计算参数**：
    - `DTP`：基于孔隙率的损伤因子，公式为 `(1 - (1 - nT) / (1 - nT0)) × 100%`，其中 `nT` 是高温后孔隙率，`nT0` 是室温下孔隙率 [Khan 2022, pp. 5-7]。
    - `DTE`：基于弹性的损伤因子，公式为 `(1 - ET / E0) × 100%`（片段中公式未显示百分比），其中 `ET` 是高温下弹性，`E0` 是室温下弹性 [Khan 2022, pp. 5-7]。未从索引片段中确认百分比是否在公式中。
- **模型性能评估指标**：
    - 平均绝对百分比误差
    - 决定系数
    - A20指数
    - 方差解释率
    - 均方根误差 [Khan 2022, pp. 3-4, 8-10]
- **MLR模型参数**：
    - `W`：因变量
    - `z1` 到 `zn`：自变量
    - `b1` 到 `bn`：偏回归系数
    - `C`：常数 [Khan 2022, pp. 5-7]

## Reusable Claims

1.  **Claim**：在预测热损伤花岗岩的损伤因子时，使用LM算法的前馈反向传播人工神经网络，其收敛速度更快，整体性能（由决定系数、均方根误差、所需神经元数量和执行时间衡量）优于采用BFG、RP、SCG、CGB训练算法的同类网络。
    - **Conditions**：适用于花岗岩，使用物理性质（孔隙率等）作为输入，采用包含切线S型激活函数和最多100个神经元的前馈反向传播网络结构。索引片段中的性能比较基于特定的数据集和实验设置。
    - **Source**: [Khan 2022, pp. 10-12]
2.  **Claim**：对于同一ANN预测任务，使用孔隙率作为预测热损伤因子的指标时，模型的预测误差（以RMSE衡量）比使用弹性模量时更低。
    - **Conditions**：本结论基于LM训练函数的ANN模型，且同时适用于缓慢和快速冷却的花岗岩样本。
    - **Source**: [Khan 2022, pp. 10-12]
3.  **Claim**：在预测岩石热损伤的研究中，软计算方法（如ANFIS, ANN）比统计方法（如MLR）能提供更高的预测精度。
    - **Conditions**：此声明综合自该文引用的文献综述，已在细粒印度砂岩的热损伤预测中得到验证。本研究以此为研究前提。
    - **Source**: [Khan 2022, pp. 3-4]

## Candidate Concepts

- [[thermal damage factor]]
- [[granite damage]]
- [[cooling conditions]]
- [[porosity]]
- [[wave velocity]]
- [[rock mechanics]]

## Candidate Methods

- [[Multiple Linear Regression]]
- [[Artificial Neural Network]]
- [[Adaptive Neuro-Fuzzy Inference System]]
- [[Levenberg-Marquardt algorithm]]
- [[porosity-based damage prediction]]

## Connections To Other Work

- **文献[66]（Sirdesai等人）**：该研究利用MLR、ANN和ANFIS，以孔隙率、密度、热膨胀系数和波速为输入，预测了在缓慢冷却条件下、热处理至1000°C的细粒砂岩的弹性模量及热损伤程度。结论是ANFIS模型性能优于MLR和ANN。此结论是本研究的立论依据和比较基准 [Khan 2022, pp. 3-4]。
- **文献[39]（Placido）和[40]（Chew）**：这些早期研究通过热释光技术来量化混凝土样本在热处理（最高500°C）后的损伤程度。这些研究为评估热损伤提供了基础方法，但本研究转而使用人工智能方法进行预测 [Khan 2022, pp. 2-3]。

## Open Questions

- 未从索引片段中确认该研究模型对经历过更复杂温度路径或不同化学环境耦合作用的花岗岩的泛化能力。
- 未从索引片段中确认文中提出的最优模型（据推断为ANFIS）在独立验证集上的具体性能，以及其与最优ANN（即LM算法）的直接性能对比结果。
- 未从索引片段中确认快速冷却和缓慢冷却条件的具体技术细节，如冷却介质（水、空气等）和冷却速率。

## Source Coverage

本页面依据17个索引片段编写，覆盖了论文的摘要、引言、实验方法和部分结果与讨论部分。覆盖内容偏重**引言和方法**细节，其中详细描述了研究背景、问题陈述、样本来源、物理性质测试流程以及MLR、ANN、ANFIS三种模型的设计框架。对于**结果**的覆盖仅限于ANN部分的算法性能比较，而ANFIS模型在本研究中的具体表现、最终模型对比结论、以及MLR模型的详细结果均在索引片段中缺失。索引片段的页码分布从第1页至第12页，且存在较多图片和表格引用，但图片和表格的实质数据内容未被包含在片段中，可能遗漏了关键的定量结果。
