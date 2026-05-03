---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2019-sirdesai-development-of-novel-methods-to-predict-the-strength-properties-of-thermally-treat"
title: "Development of Novel Methods to Predict the Strength Properties of Thermally Treated Sandstone Using Statistical and Soft-Computing Approach."
status: "draft"
source_pdf: "data/papers/2019 - Development of novel methods to predict the strength properties of thermally treated sandstone using statistical and soft-computing approach.pdf"
collections:
  - "论文"
citation: "Sirdesai, Nikhil Ninad, et al. \"Development of Novel Methods to Predict the Strength Properties of Thermally Treated Sandstone Using Statistical and Soft-Computing Approach.\" *Neural Computing and Applications*, vol. 31, 2019, pp. 2841-67. doi:10.1007/s00521-017-3233-z."
indexed_texts: "12"
indexed_chars: "58906"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "59214"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005229"
coverage_status: "full-index"
source_signature: "7b190de64165ee44ce00ed6f54f68b4652399de1"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T22:51:01"
---

# Development of Novel Methods to Predict the Strength Properties of Thermally Treated Sandstone Using Statistical and Soft-Computing Approach.

## One-line Summary
本研究利用多元回归分析（MVRA）、人工神经网络（ANN）和自适应神经模糊推理系统（ANFIS），开发了基于物理性质（温度、密度、孔隙度、热膨胀系数、超声波波速）预测热处理的细粒印度砂岩在未冷却（NC）和冷却后（WC）条件下单轴抗压强度（UCS）和抗拉强度（TS）的新模型，并通过性能指标比较得出ANFIS具有最高的预测精度。

## Research Question
由于缺乏经验方程来从室温强度推断热改性岩石的强度，且高温力学测试设备不易获得、成本高，本研究试图回答：能否利用相对容易测定的物理性质，通过统计和软计算方法来准确预测热处理砂岩在高温下的强度性质？

## Study Area / Data
- **岩石类型与来源**：细粒Dholpur砂岩，采集自印度拉贾斯坦邦Dholpur地区，属于温德亚超群（Vindhyan Supergroup）的上Bhander群。该砂岩是印度标志性建筑（如总统府、议会、红堡等）的主要建筑材料，且该区域计划开展地下煤气化（UCG），煤系上覆地层与Dholpur砂岩地质相似 [Sirdesai 2019, pp. 2-3]。
- **样品制备**：沿垂直于层理方向钻取直径40 mm和50 mm的圆柱形样品，分别用于压缩和抗拉测试，并加工至标准长径比 [Sirdesai 2019, pp. 3-4]。
- **热处理制度**：样品以5°C/min的恒定速率加热至1000°C，间隔50°C，每个目标温度均热120小时。测试分为两组：未冷却（NC，热状态下测试）和冷却后（WC，冷却120小时后测试） [Sirdesai 2019, pp. 3-4]。
- **数据集**：共63组数据集（Table 1），涵盖25–1000°C的物理和力学性质。45组用于训练ANFIS模型，其余用于检验；ANN模型使用前47组训练和验证，后16组测试 [Sirdesai 2019, pp. 4-8] [Sirdesai 2019, pp. 22-23]。

## Methods
- **多元回归分析（MVRA）**：建立强度（UCS, TS）与多个独立变量（NC样本：P, D, T, EL, EV；WC样本增加VP, VS）之间的线性方程，回归系数通过最小二乘法确定 [Sirdesai 2019, pp. 8-9] [Sirdesai 2019, pp. 18-19]。
- **人工神经网络（ANN）**：使用MATLAB的前馈反向传播网络，数据经归一化处理。比较了三种训练算法：Levenberg-Marquardt (LM)、比例共轭梯度 (SCG) 和一步正割 (OSS)。网络结构：NC样本5个输入、WC样本7个输入；隐藏层含10个神经元，使用对数S型传递函数；输出层使用正切S型传递函数；训练500个epoch [Sirdesai 2019, pp. 9-12] [Sirdesai 2019, pp. 22-23]。
- **自适应神经模糊推理系统（ANFIS）**：采用Sugeno型模糊推理，75%数据训练，25%检验。NC样本使用网格划分（grid partition），WC样本使用子聚类（sub-clustering）；隶属函数为高斯型（gaussmf）；训练50个epoch [Sirdesai 2019, pp. 12-18] [Sirdesai 2019, pp. 22-23]。
- **性能评价指标**：相关系数（R²）、平均绝对百分比误差（MAPE）、均方根误差（RMSE）和方差解释率（VAF） [Sirdesai 2019, pp. 22-25]。

## Key Findings
- MVRA建立了预测UCS和TS的线性方程（Eqs. 16–19），但R²值最低（NC: UCS R²=0.4868, TS R²=0.568; WC: UCS R²=0.4486, TS R²=0.5343） [Sirdesai 2019, pp. 18-19] [Sirdesai 2019, pp. 25-26]。
- 在ANN的三种算法中，SCG算法对NC样品强度预测具有最高的R²（UCS: 0.744; TS: 0.716），对WC样品的UCS预测（R²=0.839）也最高，而WC样品的TS预测则以LM算法最佳（R²=0.765） [Sirdesai 2019, pp. 22-25]。
- ANFIS在所有情况下均表现出最高的预测精度，R²值分别为：NC组UCS 0.9662、TS 0.9851；WC组UCS 0.9105、TS 0.9622；其RMSE和MAPE均显著低于MVRA和ANN [Sirdesai 2019, pp. 25-26]。
- 综合性能比较表明，ANFIS对热改性砂岩强度的预测能力优于ANN和MVRA，残差偏差最小 [Sirdesai 2019, pp. 25-26]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| MVRA预测NC组UCS的R²=0.4868, RMSE=13.42 MPa, MAPE=14.71% | [Sirdesai 2019, pp. 18-19] [Sirdesai 2019, pp. 25-26] | 5个输入：P, D, T, EL, EV；Eq. 16 | 回归方程无法揭示内在机制 |
| MVRA预测NC组TS的R²=0.568, RMSE=12.97 MPa, MAPE=13.27% | [Sirdesai 2019, pp. 18-19] [Sirdesai 2019, pp. 25-26] | 5个输入：P, D, T, EL, EV；Eq. 17 | 同上 |
| MVRA预测WC组UCS的R²=0.4486, RMSE=10.18 MPa | [Sirdesai 2019, pp. 18-19] [Sirdesai 2019, pp. 25-26] | 7个输入：P, D, T, EL, EV, VP, VS；Eq. 18 | 同上 |
| MVRA预测WC组TS的R²=0.5343, RMSE=11.73 MPa | [Sirdesai 2019, pp. 18-19] [Sirdesai 2019, pp. 25-26] | 7个输入：P, D, T, EL, EV, VP, VS；Eq. 19 | 同上 |
| ANN-SCG预测NC组UCS的R²=0.746, RMSE=7.21 MPa, MAPE=8.77% | [Sirdesai 2019, pp. 22-25] | 隐藏层10个神经元，logsig/tansig传递函数，500 epochs | SCG算法在NC强度预测中最优 |
| ANN-SCG预测NC组TS的R²=0.7159, RMSE=4.58 MPa | [Sirdesai 2019, pp. 22-25] | 同上 | 同上 |
| ANN-SCG预测WC组UCS的R²=0.8388, RMSE=6.03 MPa | [Sirdesai 2019, pp. 22-25] | 7个输入 | SCG算法在WC组UCS预测中最优 |
| ANN-LM预测WC组TS的R²=0.7645, RMSE=7.47 MPa | [Sirdesai 2019, pp. 22-25] | 7个输入 | LM算法在WC组TS预测中最优 |
| ANFIS预测NC组UCS的R²=0.9662, RMSE=1.73 MPa, MAPE=2.48% | [Sirdesai 2019, pp. 22-26] | 网格划分，50 epochs，243条模糊规则 | 精度显著高于其他模型 |
| ANFIS预测NC组TS的R²=0.9851, RMSE=0.67 MPa, MAPE=3.55% | [Sirdesai 2019, pp. 22-26] | 同上 | 同上 |
| ANFIS预测WC组UCS的R²=0.9105, RMSE=4.32 MPa, MAPE=5.76% | [Sirdesai 2019, pp. 22-26] | 子聚类，50 epochs，18条模糊规则 | 精度最高 |
| ANFIS预测WC组TS的R²=0.9622, RMSE=2.65 MPa, MAPE=2.63% | [Sirdesai 2019, pp. 22-26] | 同上 | 精度最高 |

## Limitations
- 回归技术（MVRA）无法定义建立关系的实际机制 [Sirdesai 2019, pp. 8-9]。
- 数据集仅来自一种细粒印度砂岩，模型可能不适用于其他岩类或不同矿物组成的砂岩 [Sirdesai 2019, pp. 2-3]。
- 所有结论基于特定的热处理制度（5°C/min升温，120 h均热），不同升温速率或均热时间下的适用性未验证 [Sirdesai 2019, pp. 3-4]。
- 高温下NC样品的波速（VP, VS）数据缺失，可能导致模型信息不全 [Sirdesai 2019, pp. 4-8] （Table 1）。
- 样本制备过程中，水敏性岩石可能受损，但本研究中Dholpur砂岩未因此产生问题，此局限并非直接针对本研究 [Sirdesai 2019, pp. 2-3]。

## Assumptions / Conditions
- 假设慢速升温（5°C/min）可避免热应力造成的额外损伤 [Sirdesai 2019, pp. 3-4]。
- 假设120 h的均热时间足以使样品达到热平衡和充分的热蚀变 [Sirdesai 2019, pp. 3-4]。
- 物理性质（P, D, EL, EV, VP, VS）与强度之间存在非线性映射关系，可通过软计算方法捕捉 [Sirdesai 2019, pp. 1-2]。
- 采用的MVRA、ANN和ANFIS模型能够合理泛化未见的温度-强度数据，前提是热处理条件与研究一致 [Sirdesai 2019, pp. 25-26]。

## Key Variables / Parameters
**自变量（输入）**：
- 温度 T (°C)
- 有效孔隙度 P (%)
- 体密度 D (g/cm³)
- 线膨胀系数 EL (°C⁻¹)
- 体膨胀系数 EV (°C⁻¹)
- 超声纵波速度 VP (m/s) —— 仅用于WC样品
- 超声横波速度 VS (m/s) —— 仅用于WC样品

**因变量（输出）**：
- 单轴抗压强度 UCS (MPa)
- 抗拉强度 TS (MPa)

**模型参数**：
- MVRA回归系数 [Sirdesai 2019, pp. 18-19]
- ANN：连接权重与偏差，隐层节点数=10，传递函数类型 [Sirdesai 2019, pp. 9-12]
- ANFIS：前提参数与结论参数，NC模型243条规则（网格划分），WC模型18条规则（子聚类），高斯隶属函数，训练50 epochs [Sirdesai 2019, pp. 22-23]

## Reusable Claims
- **ANFIS优势断言**：对于热处理细粒砂岩的UCS和TS预测，ANFIS模型的精度显著高于MVRA和ANN，可用于需要高精度估计的场景，但应用前必须核实热处理参数（升温速率、均热时间）与本研究的相似性 [Sirdesai 2019, pp. 25-26]。
- **ANN算法选择**：若采用ANN预测热处理砂岩强度，对于NC组推荐SCG算法（UCS R²=0.746，TS R²=0.716），对于WC组UCS推荐SCG算法（R²=0.839），对于WC组TS推荐LM算法（R²=0.765） [Sirdesai 2019, pp. 22-25]。
- **MVRA预测方程**：式16–19提供的线性回归方程可用于快速估计Dholpur砂岩热改性强度，但需注意其较低的泛化能力和R²值 [Sirdesai 2019, pp. 18-19]。
- **物理性质的重要性**：孔隙度（P）、密度（D）、热膨胀系数（EL, EV）和波速（VP, VS）是预测热处理砂岩强度的有效输入变量，其中波速对WC样品尤其重要 [Sirdesai 2019, pp. 1-2] [Sirdesai 2019, pp. 18-19]。

## Candidate Concepts
- [[热损伤 sandstone]] [[热处理岩石强度预测]] [[地下煤气化岩石力学]] [[核废料处置围岩稳定性]] [[火灾后结构评估]] [[热膨胀系数]] [[超声脉冲速度与强度相关]] [[有效孔隙度]]

## Candidate Methods
- [[MVRA (Multivariate Regression Analysis)]] [[ANN (Artificial Neural Network)]] [[ANFIS (Adaptive Neuro-Fuzzy Inference System)]] [[Levenberg-Marquardt算法]] [[比例共轭梯度 (SCG)]] [[一步正割 (OSS)]] [[Sugeno模糊推理系统]] [[网格划分模糊推理]] [[减聚类模糊推理]] [[高斯隶属函数]] [[性能指标 (R², RMSE, MAPE, VAF)]]

## Connections To Other Work
- 前人研究已使用统计和软计算技术预测室温下岩石的UCS，例如通过矿物颗粒特性 [20–24]、密度 [25–31]、孔隙度 [32–37]、波速 [37–40] 和吸水率 [41] 建立关系 [Sirdesai 2019, pp. 2-3]。
- 已有研究证实ANFIS在室温下预测岩土力学性质具有最高的精度，本研究将该结论扩展至高温条件 [Sirdesai 2019, pp. 2-3]。
- 仅有少数初步研究考虑了热处理对强度预测的影响 [27, 43]；本研究是首次将预测温度范围扩展到1000°C [Sirdesai 2019, pp. 2-3]。
- 引用的相关实验研究包括：热处理对红砂岩抗拉强度的影响 [8]；温度对砂岩矿物学和物理性质的影响 [9-11]；粘土岩热-力学行为 [12]；以及Dholpur砂岩的热-孔隙力学特性 [13] [Sirdesai 2019, pp. 25-26]。

## Open Questions
- 所建模型对其他岩石类型（如碳酸盐岩、花岗岩、粘土岩）的适用性未经验证 [Sirdesai 2019, pp. 2-3]。
- 不同升温速率或非恒定温度路径下的预测能力未知。
- WC模型需波速数据，但NC样品未提供波速，是否能统一输入集有待探讨。
- 特征选择（如仅用P, D, T）是否能维持预测精度未做分析。
- 模型在多次热循环或长时间高温暴露下的表现尚未研究。

## Source Coverage
本页面基于论文《Development of novel methods to predict the strength properties of thermally treated sandstone using statistical and soft-computing approach》的全部12个非空索引文本片段编制。所有片段均已被处理并整合，总计59214字符（覆盖比率1.0）。来源签名为7b190de64165ee44ce00ed6f54f68b4652399de1。
