---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-verma-prediction-of-thermal-conductivity-and-damage-in-indian-jalore-granite-for-design-of"
title: "Prediction of Thermal Conductivity and Damage in Indian Jalore Granite for Design of Underground Research Laboratory."
status: "draft"
source_pdf: "data/papers/2021 - Prediction of thermal conductivity and damage in Indian Jalore granite for design of underground research laboratory.pdf"
collections:
  - "论文"
citation: "Verma, A. K., et al. “Prediction of Thermal Conductivity and Damage in Indian Jalore Granite for Design of Underground Research Laboratory.” *Neural Computing and Applications*, vol. 33, 2021, pp. 13183–92. doi:10.1007/s00521-021-05944-5."
indexed_texts: "8"
indexed_chars: "36263"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T03:04:59"
---

# Prediction of Thermal Conductivity and Damage in Indian Jalore Granite for Design of Underground Research Laboratory.

## One-line Summary
基于印度Jalore花岗岩的物理性质数据，应用人工神经网络（ANN）、决策树回归器（DTR）等AI技术建立其热导率与损伤阈值的预测模型，以支持地下研究实验室的设计 [Verma 2021, pp. 1-2]。

## Research Question
如何利用AI技术更快速、准确地预测印度Jalore花岗岩的热导率和损伤阈值，以替代耗时且需精密仪器的实验测量，并评估各模型的有效性 [Verma 2021, pp. 1-2]。

## Study Area / Data
- **地点**: 印度拉贾斯坦邦Jalore地区，位于北纬24°37'至25°49'，东经71°11'至73°05'之间 [Verma 2021, pp. 3-3]。
- **数据来源**: 数据集来源于Gautam et al. 2019 (参考编号17) 和另一2019年研究（参考编号18）的测量分析，旨在评估Jalore花岗岩作为核废料处置库的潜力 [Verma 2021, pp. 3-3]。
- **样本与处理**: 岩样被分为13组，以5°C/min的恒定速率加热至不同目标温度，并在达到目标温度后保持12小时 [Verma 2021, pp. 3-3]。
- **数据规模**: 数据集包含约100组数据 [Verma 2021, pp. 3-3]。
- **数据集划分**: 训练集（60组）、测试集（20组）、预测集（20组），比例为3:1:1 [Verma 2021, pp. 3-3]。

## Methods
- **输入变量**: 温度、质量损失、P波速度、S波速度、密度和孔隙度 [Verma 2021, pp. 3-3]。
- **预测目标**: 热系数和损伤阈值 [Verma 2021, pp. 3-3]。
- **评估指标**: R² Score, MAE, MSE [Verma 2021, pp. 3-3]。
- **模型与配置**:
    - **人工神经网络 (ANNs)**:
        - 尝试了多种网络结构（如6-10-1, 8-15-7-1等）和优化器（如Adam, Rmsprop, Nadam等） [Verma 2021, pp. 7-9]。
        - 激活函数包括：Softmax [Verma 2021, pp. 1-2]。
        - 训练原理基于最小化误差函数（如总均方误差或平均绝对误差）来调整权重 [Verma 2021, pp. 5-7]。
    - **决策树回归器 (DTRs)**:
        - 关键超参数为子树数量 `n_estimators`，取值包括100, 1000, 10000 [Verma 2021, pp. 1-2]。
    - **支持向量回归器 (SVRs)**:
        - 采用了Linear和Robust两种核函数 [Verma 2021, pp. 1-2]。
    - **线性回归 (Linear Regression)** [Verma 2021, pp. 1-2]。

## Key Findings
- **最优模型**: 对于预测热导率和损伤阈值，采用8个输入节点、两个隐藏层（节点数分别为15和7）的ANN模型取得了最优性能 [Verma 2021, pp. 1-2]。
- **最优模型性能**:
    - 预测热系数时的MAE为0.0033671, MSE为1.84E-05 [Verma 2021, pp. 1-2]。
    - 预测损伤阈值时的MAE为0.0016141, MSE为3.89E-06 [Verma 2021, pp. 1-2]。
- **其他模型性能比较**:
    - DTRs在预测热导率（`n_estimators`=1000时MSE=6.81E-05）和损伤阈值（`n_estimators`=100时MSE=2.84E-05）时表现相对较好 [Verma 2021, pp. 1-2]。
    - 线性回归和SVRs模型在数据趋势发生突变或转折的点上表现出一定的偏差 [Verma 2021, pp. 1-2]。
- **物理机制关系**: 研究确认，热损伤与热导率呈反比关系，且热损伤可通过P波速度测量进行量化 [Verma 2021, pp. 2-3]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| ANN (结构8-15-7-1, 优化器Nadam) 预测热系数的MSE为1.84E-05。 | [Verma 2021, pp. 7-9] | 数据集：Jalore花岗岩的约100组数据；输入特征：温度、质量损失、P/S波速度、密度、孔隙度；训练集/测试集/预测集=60/20/20。 | 最优模型。Softmax激活函数。 |
| ANN (结构8-15-7-1, 优化器Nadam) 预测损伤阈值的MSE为3.89E-06。 | [Verma 2021, pp. 7-9] | 数据集：Jalore花岗岩的约100组数据；输入特征：温度、质量损失、P/S波速度、密度、孔隙度；训练集/测试集/预测集=60/20/20。 | 最优模型。Softmax激活函数。 |
| DTR (`n_estimators`=1000) 预测热导率的MSE为6.81E-05。 | [Verma 2021, pp. 5-7] | 数据集：Jalore花岗岩的约100组数据；模型：决策树回归器。 | 同类型中最优配置。 |
| DTR (`n_estimators`=100) 预测损伤阈值的MSE为2.86E-05。 | [Verma 2021, pp. 5-7] | 数据集：Jalore花岗岩的约100组数据；模型：决策树回归器。 | 同类型中最优配置。 |
| 热损伤与热导率存在反比关系。 | [Verma 2021, pp. 2-3] | 基于对花岗岩的实验研究。 | 物理机制。热损伤可通过P波速度量化。 |

## Limitations
- 提出的经验方程适用性有限，不能推广 [Verma 2021, pp. 3-5]。
- AI模型的训练和验证依赖于Gautam et al. (2019)等的特定实验数据集，其泛化到其他岩石类型或地区的能力未从索引片段中确认。
- 尽管ANN模型取得了高精度，但研究未提及是否对模型进行了过拟合检验。
- 研究结论基于实验室数据，其在原位岩体中的直接适用性未从索引片段中确认。

## Assumptions / Conditions
- **模型假设**: ANN模型通过最小化误差函数（如MSE, MAE）来学习输入与输出之间的映射关系，假设训练集能代表整体数据分布 [Verma 2021, pp. 5-7]。
- **实验条件**: 样本是在标准实验室条件下制备和测试的；温度以5°C/min的稳态速率升高，并恒温12小时，以模拟特定热工况下的岩石响应 [Verma 2021, pp. 3-3]。
- **物理假设**: 热导率的变化主要由温度引起的微观结构损伤（微裂纹的形核与扩展）所导致 [Verma 2021, pp. 2-3]。
- **数据条件**: 数据集规模较小（约100组），且被划分为60组用于训练，各20组用于测试和预测 [Verma 2021, pp. 3-3]。

## Key Variables / Parameters
- **输入变量**: 温度，质量损失 (Mass Loss), P波速度 (P-wave velocity), S波速度 (S-wave velocity), 密度 (Density), 孔隙度 (Porosity) [Verma 2021, pp. 3-3]。
- **输出变量**: 热系数，损伤阈值 [Verma 2021, pp. 3-3]。
- **模型超参数**: ANN隐含层数与节点数、优化器（如Adam, Nadam）、DTR的 `n_estimators`、SVR的核函数 (Linear, Robust) [Verma 2021, pp. 1-2]。
- **性能评估参数**: R² Score, MAE, MSE [Verma 2021, pp. 3-3]。

## Reusable Claims
- **Claim 1**: 对于印度Jalore花岗岩的热导率预测，一个具有8个输入节点、两个隐藏层（分别含15和7个节点）并使用Nadam优化器和Softmax激活函数的ANN模型，能够达到MSE为1.84E-05的高预测精度 [Verma 2021, pp. 7-9]。其适用条件为数据集包含温度及多项物理性质（P/S波速度、孔隙度、密度等），且数据量级约为100组。
- **Claim 2**: 在预测岩石的热物理行为时，当数据趋势出现突变点时，树基模型（如DTRs）比线性模型（线性回归、线性核SVR）表现出更低的偏差，表明其在捕捉非线性关系上更具优势 [Verma 2021, pp. 1-2]。
- **Claim 3**: 岩石的热损伤程度与P波速度的变化相关，且与热导率呈反比关系，因此P波速度可以作为表征热损伤和预测热导率变化的一个有效间接指标 [Verma 2021, pp. 2-3]。

## Candidate Concepts
- [[thermal conductivity prediction]]
- [[rock thermal damage]]
- [[nuclear waste repository]]
- [[P-wave velocity]]
- [[microcrack nucleation]]
- [[Jalore granite]]

## Candidate Methods
- [[Artificial Neural Networks]]
- [[Decision Tree Regressor]]
- [[Support Vector Regressor]]
- [[Linear Regression]]

## Connections To Other Work
- **已确认的连接**: 本研究直接基于Gautam et al. 2019（参考文献17, 18）的实验测量数据 [Verma 2021, pp. 3-3]。引用了关于高温对花岗岩热性质和力学性质影响的文献 [参考文献8, 9, 12, 16，见 Verma 2021, pp. 9-10]。也引用了先前关于使用AI技术预测岩石热导率和热损伤的研究 [参考文献2, 6, 7，见 Verma 2021, pp. 9-10]。
- **主题连接**: 本研究中使用的AI预测方法可以从主题上连接到其他地质材料性质预测的广泛研究，例如砂岩、页岩的热导率建模 [参考文献4, 6, 11，见 Verma 2021, pp. 9-10]，以及使用智能技术进行岩体工程分类或参数反演。

## Open Questions
- 此最优ANN模型结构对除Jalore花岗岩以外的其他花岗岩或岩石类型的泛化能力如何？
- 在更大、更多样化的数据集上，模型的稳定性及是否会出现过拟合？
- 研究中未从索引片段中确认是否进行了特征重要性分析，以确定哪个物理性质（如P波速度或孔隙度）对预测结果的贡献最大。
- 能否将这种数据驱动模型与物理模型（如基于微观结构的均质化理论）相结合，以提高其可解释性和外推能力？
- 原位应力环境对热导率-损伤关系的影响未在实验中得到体现，其影响如何？

## Source Coverage
- 本页内容基于从论文《Prediction of Thermal Conductivity and Damage in Indian Jalore Granite for Design of Underground Research Laboratory》中提取的8个索引片段 [Verma 2021, pp. 1-10]。
- 覆盖范围包括摘要、研究区域与数据描述、方法（ANN, DTR, SVR）、关键发现（模型性能比较与最优模型参数）和参考文献列表。
- **可能的信息缺失**: 索引片段主要覆盖了摘要、导论、方法、结果和参考文献部分。论文的详细讨论、研究局限性的深入分析、结论部分、以及对图表（如DTR树结构图、SVR算法图、真值与预测值对比图）的详细解释可能未被完全收录。此外，关于地质背景和实验装置细节的完整描述可能不在此次提供的片段中。
