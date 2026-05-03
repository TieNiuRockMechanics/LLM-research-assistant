---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2019-sirdesai-development-of-novel-methods-to-predict-the-strength-properties-of-thermally-treat"
title: "Development of Novel Methods to Predict the Strength Properties of Thermally Treated Sandstone Using Statistical and Soft-Computing Approach."
status: "draft"
source_pdf: "data/papers/2019 - Development of novel methods to predict the strength properties of thermally treated sandstone using statistical and soft-computing approach.pdf"
collections:
  - "论文"
citation: "Sirdesai, Nikhil Ninad, et al. \"Development of Novel Methods to Predict the Strength Properties of Thermally Treated Sandstone Using Statistical and Soft-Computing Approach.\" *Neural Computing and Applications*, vol. 31, 2019, pp. 2841-67. doi:10.1007/s00521-017-3233-z."
indexed_texts: "12"
indexed_chars: "58906"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T22:53:50"
---

# Development of Novel Methods to Predict the Strength Properties of Thermally Treated Sandstone Using Statistical and Soft-Computing Approach.

## One-line Summary
本研究基于统计与软计算方法，通过物理性质预测热改性砂岩的单轴抗压强度和抗拉强度，发现自适应神经模糊推理系统（ANFIS）优于多元回归分析（MVRA）[Sirdesai 2019, pp. 1-2]。

## Research Question
能否根据室温下或热改性后砂岩的物理性质，开发出精确的经验模型来预测其力学强度？[Sirdesai 2019, pp. 1-2]

## Study Area / Data
研究材料为印度细粒砂岩“Dholpur sandstone”，属于Vindhyan超群Bhander群。该砂岩被广泛用作印度标志性建筑（如总统府、议会大厦、红堡等）的建筑材料 [Sirdesai 2019, pp. 3-4]。样本取自完整的砂岩块体，为富含石英和长石的单矿碎屑岩，颜色呈灰色。通过金刚石钻头垂直于层理方向取芯，分别制备直径40 mm和50 mm的圆柱形样品用于抗压和抗拉强度试验 [Sirdesai 2019, pp. 3-4]。样品在50°C间隔、最高1000°C的条件下进行了热处理，并在试验前让其缓慢冷却至室温，这一过程持续了5天（120小时）[Sirdesai 2019, pp. 6-8]。数据集包含未冷却（NC）和热改性后冷却（WC）的样品，每个测试点包含3到4个样品 [Sirdesai 2019, pp. 4-6]。

## Methods
研究采用了三种预测方法，将物理性质作为输入来预测力学强度 [Sirdesai 2019, pp. 8-12]：
1.  **[[多元回归分析]] (MVRA)**：用于建立多个预测变量与单一响应变量之间关系，其局限性在于无法描述建立关系的真实机制 [Sirdesai 2019, pp. 8-12]。
2.  **[[人工神经网络]] (ANN)**：受生物神经网络启发的数学模型，能够对含噪声数据进行分类和过滤以建立潜在关系。研究测试了三种训练算法：Levenberg-Marquardt (LM)、Scaled Conjugate Gradient (SCG) 和 One Step Secant (OSS) [Sirdesai 2019, pp. 8-12]。
3.  **[[自适应神经模糊推理系统]] (ANFIS)**：由Jang引入，该方法结合模糊推理系统和神经网络学习算法，使用反向传播算法进行训练 [Sirdesai 2019, pp. 12-18]。ANFIS模型的各种参数被记录在案 [Sirdesai 2019, pp. 18-22]。

## Key Findings
*   **ANFIS模型的性能相对更优**：根据决定系数（R²）、平均绝对百分比误差、均方根误差和方差解释比等性能指标的比较，结论是ANFIS的预测比MVRA更接近真实值 [Sirdesai 2019, pp. 1-2]。
*   **MVRA预测方程已建立**：研究得出了使用物理性质（孔隙率P、密度D、温度T、线性和体积热膨胀系数EL、EV，以及对于WC样品的波速VP和VS）预测未冷却（NC）和冷却（WC）样品UCS和TS的多元回归方程 [Sirdesai 2019, pp. 18-22]。
    *   `UCS_NC = 37.61 + 10.13(P) - 6.42(D) - 21.32(T) - 0.12(EL) + 0.97(EV)` [Sirdesai 2019, pp. 18-22]
    *   `TS_NC = 3.51 - 0.14(P) + 0.08(D) - 0.27(T) - 0.09(EL) - 0.32(EV)` [Sirdesai 2019, pp. 18-22]
    *   `UCS_WC = 30.48 + 3.5(P) + 7.51(D) - 3.78(T) + 7.07(EL) - 5.52(EV) - 20.58(VP) + 22.31(VS)` [Sirdesai 2019, pp. 18-22]
    *   `TS_WC = 2.98 - 0.21(P) + 0.12(D) - 0.19(T) - 0.24(EL) - 0.29(EV) + 1.99(VP) - 2.18(VS)` [Sirdesai 2019, pp. 18-22]
*   **数据集和模型训练**：ANFIS模型的训练使用了45个数据集，其余数据用于模型的检验和测试 [Sirdesai 2019, pp. 8-12]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| ANFIS提供了比MVRA更接近的估计 | [Sirdesai 2019, pp. 1-2] | 基于R²、MAPE、RMSE和VAF等性能指标的比较研究 | 此结论为摘要中的核心声明 |
| 得出NC和WC样品UCS、TS的MVRA方程及相关系数 | [Sirdesai 2019, pp. 18-22] | 方程由指定物理变量构建，在相应页面上展示了方程16-19 | 方程的具体形式和各项系数已明确列出 |
| Dholpur砂岩在热处理后，其波速（VP，VS）被测量并作为WC样品的输入参数 | [Sirdesai 2019, pp. 4-6] | 300-800°C的WC样品波速数据记录在数据表中 | 这表明高温处理后岩石的物理结构发生了变化 |
| 使用ISRM推荐的浮力与饱和技术测量有效孔隙率 | [Sirdesai 2019, pp. 6-8] | 适用于完整和非膨胀性岩石 | 公式为`UE = ((M_SAT - M_S) / (M_SAT - M_SUB)) * 100` |

## Limitations
*   **信息不足**：所有MVRA、ANN和ANFIS模型的具体性能指标（如R²、RMSE的数值）和详细的比较结果未从索引片段中确认。
*   **ANN模型详情缺失**：对于ANN模型的架构（如层数、神经元数）、具体参数设置和最终选用的训练算法结果，未从索引片段中确认。
*   **ANFIS结果缺失**：ANFIS模型最终的性能数据和具体推理机理未被提供。
*   **普适性限制**：所有模型仅基于单一类型砂岩（Dholpur sandstone）的数据建立，其泛化到其他岩类的能力未知 [Sirdesai 2019, pp. 3-4]。
*   **回归方法的固有局限**：MVRA本身的局限性在于不能定义变量间关系的真实物理机制 [Sirdesai 2019, pp. 8-12]。

## Assumptions / Conditions
1.  **数据生成假设**：用于预测的物理性质（如孔隙率、密度、波速）是在样品经过热处理并冷却至室温后测量的。对于NC样品，未测量其波速，因此波速仅作为WC样品的预测变量。
2.  **实验条件**：样品在高达1000°C的温度下以50°C为间隔进行处理，并经历了一个长达5天（120小时）的缓慢冷却过程。
3.  **模型训练条件**：ANFIS模型使用45个数据集进行训练，其余用于测试 [Sirdesai 2019, pp. 8-12]。
4.  **应用场景**：该研究结果旨在服务于地下煤炭气化、深部地质处置库中的放射性废物处置、火灾受损结构修复等高温工程场景 [Sirdesai 2019, pp. 1-2]。

## Key Variables / Parameters
*   **自变量（物理性质）**：温度 (T)、密度 (D)、孔隙率 (P)、线性热膨胀系数 (EL)、体积热膨胀系数 (EV)，以及仅用于WC样品的P波速度 (VP) 和 S波速度 (VS) [Sirdesai 2019, pp. 1-2]。
*   **因变量（力学性质）**：[[单轴抗压强度]] (UCS)、[[抗拉强度]] (TS) [Sirdesai 2019, pp. 1-2]。
*   **模型性能指标**：决定系数/相关系数 (R²)、[[平均绝对百分比误差]]、[[均方根误差]]、[[方差解释比]] [Sirdesai 2019, pp. 1-2]。
*   **ANFIS模型训练参数**：误差函数 E [Sirdesai 2019, pp. 18-22]。
*   **MVRA方程参数**：回归系数、常数项 [Sirdesai 2019, pp. 18-22]。

## Reusable Claims
1.  [[自适应神经模糊推理系统]] (ANFIS) 在预测热改性砂岩力学强度方面的性能优于 [[多元回归分析]] (MVRA)，此结论基于多种性能指标的比较得出 [Sirdesai 2019, pp. 1-2]。**条件限制**：结论仅在对一种细粒印度砂岩的研究中证实。
2.  火成或热改性砂岩的力学强度（UCS， TS）可以通过其物理性质（如温度、密度、孔隙率、热膨胀系数和超声波波速）使用MVRA建立数学关系进行预测。例如，本研究为特定砂岩推导的方程16-19 [Sirdesai 2019, pp. 18-22]。**条件限制**：建立的MVRA方程是经验性的，其系数和形式对所用数据集有极强的依赖性，不能直接外推。
3.  对岩石进行高温处理时，采用缓慢冷却步骤（本研究中为5天，120小时）是可操作的实验方法 [Sirdesai 2019, pp. 6-8]。**条件限制**：冷却制度对热裂纹的生成和力学性质有直接影响，是实验设计的关键环节。

## Candidate Concepts
*   [[热改性 (Thermal modification)]]
*   [[单轴抗压强度 (UCS)]]
*   [[抗拉强度]]
*   [[砂岩]]
*   [[热膨胀]]
*   [[孔隙率]]
*   [[超声波波速]]
*   [[地下煤炭气化 (UCG)]]
*   [[放射性废物深部地质处置]]

## Candidate Methods
*   [[多元回归分析 (MVRA)]]
*   [[人工神经网络 (ANN)]]
*   [[自适应神经模糊推理系统 (ANFIS)]]
*   [[Levenberg-Marquardt算法 (LM)]]
*   [[Scaled Conjugate Gradient算法 (SCG)]]
*   [[One Step Secant算法 (OSS)]]
*   [[ISRM岩石力学测试建议方法]]

## Connections To Other Work
*   从主题上，本研究与利用 [[机器学习]] 和 [[统计方法]] 预测岩石力学性质的研究相关。
*   方法论上与使用 [[ANFIS]]、[[ANN]] 进行地质工程参数预测的工作有关。
*   应用背景上与所有涉及高温岩石力学的问题（如 [[地热开发]]、[[隧道火灾后评估]]）相联系。

## Open Questions
*   ANFIS模型的性能具体比MVRA提高了多少？其在测试集上的泛化误差是多少？
*   ANN和ANFIS模型的详细架构（网络层数、神经元数量）和关键超参数设置是什么？
*   研究结论是否可信，模型的可解释性如何体现？
*   是否能将所提出的建模方法推广到其他类型的岩石，尤其是页岩、碳酸盐岩等文中提及难以制备样品的岩石？[Sirdesai 2019, pp. 2-3]

## Source Coverage
本页依据12个索引片段撰写。覆盖内容主要来自论文的摘要、引言、方法概述、部分数据集和结果分析的开头部分。由于片段缺失了结果分析的主体、讨论和结论部分，重要信息如模型的详细性能指标、对比分析数据、讨论部分的深入解释以及最终结论均未从索引片段中确认。
