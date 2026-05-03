---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-verma-prediction-of-thermal-conductivity-and-damage-in-indian-jalore-granite-for-design-of"
title: "Prediction of Thermal Conductivity and Damage in Indian Jalore Granite for Design of Underground Research Laboratory."
status: "draft"
source_pdf: "data/papers/2021 - Prediction of thermal conductivity and damage in Indian Jalore granite for design of underground research laboratory.pdf"
collections:
  - "论文"
citation: "Verma, A. K., et al. “Prediction of Thermal Conductivity and Damage in Indian Jalore Granite for Design of Underground Research Laboratory.” *Neural Computing and Applications*, vol. 33, 2021, pp. 13183-92. doi:10.1007/s00521-021-05944-5."
indexed_texts: "8"
indexed_chars: "36263"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "36437"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004798"
coverage_status: "full-index"
source_signature: "a9c9705082b1689f683a8af7f3403093b50d36b8"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T04:35:34"
---

# Prediction of Thermal Conductivity and Damage in Indian Jalore Granite for Design of Underground Research Laboratory.

## One-line Summary
利用人工神经网络（ANN）、支持向量回归（SVR）和决策树回归（DTR）等人工智能技术，基于温度、质量损失、P波速度、S波速度、密度和孔隙度六个物理参数，预测印度Jalore花岗岩的热导率与热损伤阈值，ANN‑8‑15‑7‑1结构精度最高（热导率 MSE = 1.84×10⁻⁵，损伤阈值 MSE = 3.89×10⁻⁶）。

## Research Question
如何利用易测量的物理性质（温度、质量损失、P波速度、S波速度、密度、孔隙度）构建可靠的人工智能预测模型，以替代耗时且需精密仪器的花岗岩热导率与热损伤阈值实验测量？

## Study Area / Data
- **研究区域**：印度拉贾斯坦邦Jalore地区（纬度24°37′–25°49′，经度71°11′–73°05′）[Verma 2021, pp. 3-3]。
- **数据来源**：基于Gautam等（2018, 2019）对Jalore花岗岩用于核废料处置潜力的实验测量与热分析[Verma 2021, pp. 3-3]。
- **样本处理**：样本分为13组，以5 °C/分钟的速率匀速加热至不同目标温度，并在目标温度保持12小时[Verma 2021, pp. 3-3]。
- **数据集**：约100组数据，包含六个输入参数（温度、质量损失、P波速度、S波速度、密度、孔隙度）和两个目标参数（热导率、损伤阈值）；按3 : 4比例划分为训练集60组、测试集20组、预测集20组[Verma 2021, pp. 3-3]。

## Methods
- **多元线性回归（Multiple Linear Regression）**：建立热导率（TC）和损伤阈值（DT）与六个物理参数的线性方程，以最小化误差函数，获得回归系数与R²、MAE、MSE指标[Verma 2021, pp. 3-3]。
- **决策树回归（Decision Tree Regressor, DTR）**：构建树状结构，通过调整决策树节点数（估计器数量 n = 100, 1000, 10000）避免欠拟合或过拟合，实现全局最优[Verma 2021, pp. 3-5]。
- **支持向量回归（Support Vector Regressor, SVR）**：采用线性核与稳健核，引入ε容忍误差，最大化间隔，对数据进行归一化、优化和反归一化处理[Verma 2021, pp. 5-5]。
- **人工神经网络（ANN）**：构建多层前馈网络，隐藏层采用Softmax激活函数，利用多种优化器（Adam, Rmsprop, Nadam, Adamax, Adadelta）对权重进行训练，以均方误差损失函数最小化为目标；通过调整输入节点数（6–10）、隐藏层层数和节点数进行微调[Verma 2021, pp. 5-7]。

## Key Findings
1.  **最佳ANN结构**：输入层8节点，两个隐藏层分别含15和7节点，Softmax激活，采用Nadam优化器，预测热导率时MSE = 1.84×10⁻⁵，预测损伤阈值时MSE = 3.89×10⁻⁶，R²均超过0.99996[Verma 2021, pp. 7-7][Verma 2021, pp. 1-2]。
2.  **DTR性能**：估计器数量 n = 1000 时预测热导率最优（MSE = 6.81×10⁻⁵），n = 100 时预测损伤阈值最优（MSE = 2.84×10⁻⁵）[Verma 2021, pp. 1-2][Verma 2021, pp. 7-9]。
3.  **回归模型局限**：线性回归和SVR（线性核、稳健核）在趋势出现突变或扭折的位置与实测值存在明显偏差[Verma 2021, pp. 1-2][Verma 2021, pp. 7-9]。
4.  **参数敏感性**：孔隙度对热导率变化影响最大，其次为P波速度和S波速度；温度是第二重要影响参数。损伤阈值对孔隙度、P波速度敏感，质量损失和温度亦有显著影响[Verma 2021, pp. 9-9]。
5.  **相关方向**：热导率与密度、S波速度、P波速度呈高度正相关；损伤阈值与温度、质量损失、孔隙度呈高度正相关，与其余参数呈强负相关[Verma 2021, pp. 10-10]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 多元线性回归方程（Eq. 2, 3）拟合度：热导率 R² = 0.9888, MAE = 0.0534, MSE = 0.00541；损伤阈值 R² = 0.9944, MAE = 0.0221, MSE = 7.73×10⁻⁴ | [Verma 2021, pp. 3-3] | Jalore花岗岩实验数据，60组训练 | 线性相关可解释，但不可推广到其他岩类 |
| DTR 热导率最优：n = 1000，R² = 0.99985, MAE = 0.00386, MSE = 6.81×10⁻⁵ | [Verma 2021, pp. 5-5] | Jalore花岗岩数据，60组训练，树模型 | 避免过拟合和欠拟合 |
| DTR 损伤阈值最优：n = 100，R² = 0.99979, MAE = 0.00266, MSE = 2.86×10⁻⁵（文中另一处记为2.84×10⁻⁵） | [Verma 2021, pp. 5-5][Verma 2021, pp. 7-9] | Jalore花岗岩数据，60组训练 | 表述存在微小差异，以Table 3为准 |
| SVR 热导率：线性核 R² = 0.9871, MSE = 0.00630；稳健核 R² = 0.9917, MSE = 0.00424 | [Verma 2021, pp. 5-5] | 归一化后训练，反归一化预测 | 在曲率突变处有偏差 |
| SVR 损伤阈值：线性核 R² = 0.9689, MSE = 0.00362；稳健核 R² = 0.9689, MSE = 0.00362 | [Verma 2021, pp. 5-5] | 同上 | 两核表现几近相同 |
| ANN最佳结构（8‑15‑7‑1, Softmax, Nadam）热导率：MAE = 0.00337, MSE = 1.84×10⁻⁵, R² = 0.99996 | [Verma 2021, pp. 7-7] | 60组训练，20组测试，20组预测 | 输入层包含6个实际输入+2个哑节点 |
| ANN最佳结构（同上）损伤阈值：MAE = 0.00161, MSE = 3.89×10⁻⁶, R² = 0.99997 | [Verma 2021, pp. 7-7] | 同上 | 训练采用均方误差损失函数 |
| 参数敏感性：孔隙度与热导率的相关性≈‑0.984，与损伤阈值的相关性≈‑0.987；P波速度与热导率相关性≈0.984，与损伤阈值相关性≈‑0.987 | [Verma 2021, pp. 9-9] | 基于模型分析 | 相关性数值为图中近似值，具体见图9、图10 |
| 线性回归方程仅适用于Jalore花岗岩，不可泛化到其他岩类 | [Verma 2021, pp. 3-3] | 受岩石高度非均质性限制 | 不同矿物组成和孔隙结构导致不可迁移 |

## Limitations
- 多元线性回归方程（Eq. 2, 3）仅对Jalore花岗岩有效，不能推广至其他岩石类型，因其矿物组成、孔隙度和微裂隙差异显著[Verma 2021, pp. 3-3]。
- 线性回归与SVR模型在实验趋势出现突变点或扭折时与观测值偏差较大，处理强非线性关系能力受限[Verma 2021, pp. 1-2]。
- 实验数据基于特定的升温速率（5 °C/min）和恒温时间（12 h），其他热历史下的适用性未验证[Verma 2021, pp. 3-3]。
- 文中未能给出预测模型对不同温度范围、不同压力条件的泛化能力评价。

## Assumptions / Conditions
- 岩石样本均匀且各向同性（用于均质化模型假设）[Verma 2021, pp. 3-3]（注：实际花岗岩为非均质，文中未明确验证）。
- 升温过程中微裂隙发育主要由温度引起，忽略应力等其他因素耦合[Verma 2021, pp. 2-2]。
- 热损伤可通过P波速度相对于室温时的变化进行量化[Verma 2021, pp. 2-2]。
- 训练数据集能代表Jalore花岗岩在该温区内的整个性质变化范围。
- ANN模型使用Softmax激活函数，假设各神经元输出满足该函数的非线性变换要求。

## Key Variables / Parameters
- **输入变量（预测因子）**：温度（T），质量损失（ML），密度（D），孔隙度（P），P波速度（Pv），S波速度（Sv）[Verma 2021, pp. 3-3]。
- **输出变量（预测目标）**：热导率（TC, W/mK），损伤阈值（DT，由P波速度比归一化表示）[Verma 2021, pp. 3-3]。
- **模型超参数**：ANN隐藏层层数、各层节点数、激活函数、优化器；DTR估计器数量（n）；SVR核函数与ε容忍度[Verma 2021, pp. 5-7]。

## Reusable Claims
- **Claim 1**：对于印度Jalore花岗岩，含8个输入节点、两个隐藏层（15和7节点）并使用Softmax激活和Nadam优化器的ANN，能以MSE ≤ 2×10⁻⁵的误差同时预测热导率和损伤阈值。[Verma 2021, pp. 7-7]
- **Claim 2**：DTR在该花岗岩数据上，n = 1000时热导率预测MSE = 6.81×10⁻⁵，n = 100时损伤阈值预测MSE ≈ 2.84×10⁻⁵，优于线性回归和SVR。[Verma 2021, pp. 7-9]
- **Claim 3**：孔隙度和P波速度是控制热导率与热损伤预测的最关键物理参数，其与目标变量的相关性绝对值均大于0.98。[Verma 2021, pp. 9-9]
- **Claim 4**：基于多元线性回归的式(2)和式(3)仅在Jalore花岗岩上成立，不可外推至其他岩石类型。[Verma 2021, pp. 3-3]
- **Claim 5**：温度、质量损失和孔隙度与损伤阈值呈高度正相关，而密度和波速呈高度负相关，可为简化的经验关联提供方向。[Verma 2021, pp. 10-10]

## Candidate Concepts
- [[thermal conductivity prediction in granite]] using [[artificial neural networks]]
- [[thermal damage threshold]] defined via P-wave velocity ratio
- [[decision tree regressor]] for [[rock thermal properties]]
- [[support vector regressor]] with linear and robust kernels for [[granite thermal damage]]
- [[porosity‑thermal conductivity correlation]] in crystalline rock
- [[laboratory heating protocol]] (5 °C/min, 12 h hold) for [[thermal property measurement]]
- [[Jalore granite]] as a potential [[underground research laboratory]] host rock

## Candidate Methods
- [[ANN with Softmax and Nadam optimizer]]
- [[Decision Tree Regressor with tuned n_estimators]]
- [[Support Vector Regressor (linear and robust kernels)]]
- [[Multiple Linear Regression for thermal properties]]
- [[Data splitting (60:20:20) for training, testing, prediction]]

## Connections To Other Work
- 研究引用了多篇关于高温下岩石热导率、热损伤演化的实验与模型工作，如花岗岩、页岩和砂岩在温度作用下的性质变化[Verma 2021, pp. 9-10]。
- 本文的损伤阈值定义与Liu & Xu (2014)、Verma et al. (2016)等基于P波速度的量化方法一致[Verma 2021, pp. 2-2]。
- 在预测方法上，与前人使用ANN（如Vaferi et al., 2014; Singh et al., 2007）或SVM（Rostami et al., 2016）进行热导率建模的思路相延续[Verma 2021, pp. 9-10]。
- 数据直接来自Gautam et al. (2018, 2019)对Jalore花岗岩用于核废料处置库的实验研究[Verma 2021, pp. 3-3]。

## Open Questions
- 所建ANN和DTR模型能否推广到其他花岗岩类或不同热加载历史（如不同升温速率、循环热冲击）的预测？目前无实验验证。
- 在大尺度原位条件（高应力、高孔隙水压）下，本文基于实验室干燥样本的预测模型是否需要耦合力学‑热‑水力参数？
- 损伤阈值量化仅依赖P波速度比，是否需引入微观裂隙密度或声发射等更直接的损伤指标以提高预测精度？
- 其余AI模型（如XGBoost、随机森林）与当前最优DTR/ANN的对比未开展，是否可获得更低误差？

## Source Coverage
所有提供的非空索引片段均已处理。共8个片段，总计36,263个索引字符，编译后字符数36,437，覆盖率为1.0（按片段数），字符覆盖率约1.005。签名：a9c9705082b1689f683a8af7f3403093b50d36b8。
