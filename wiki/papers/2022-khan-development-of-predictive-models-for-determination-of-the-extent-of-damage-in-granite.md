---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-khan-development-of-predictive-models-for-determination-of-the-extent-of-damage-in-granite"
title: "Development of Predictive Models for Determination of the Extent of Damage in Granite Caused by Thermal Treatment and Cooling Conditions Using Artificial Intelligence."
status: "draft"
source_pdf: "data/papers/2022 - Development of Predictive Models for Determination of the Extent of Damage in Granite Caused by Thermal Treatment and Cooling Conditions Using Artificial Intelligence.pdf"
collections:
  - "论文"
citation: "Khan, Naseer Muhammad, et al. “Development of Predictive Models for Determination of the Extent of Damage in Granite Caused by Thermal Treatment and Cooling Conditions Using Artificial Intelligence.” *Mathematics*, vol. 10, no. 16, 2022, Article 2883. doi:10.3390/math10162883."
indexed_texts: "17"
indexed_chars: "81145"
nonempty_source_blocks: "17"
compiled_source_blocks: "17"
compiled_source_chars: "81118"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.999667"
coverage_status: "full-index"
source_signature: "576aebd471e64f8902ea98d063939d2e47a5c105"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T05:12:31"
---

# Development of Predictive Models for Determination of the Extent of Damage in Granite Caused by Thermal Treatment and Cooling Conditions Using Artificial Intelligence.

## One-line Summary
本研究针对热处理和冷却条件引起的花岗岩损伤，以温度、密度、孔隙率和P波速度为输入，开发了MLR、ANN和ANFIS三种预测模型，其中基于孔隙率的LM‑ANN模型预测损伤因子的效果最优（慢冷R² 0.99，RMSE 0.01；快冷R² 0.99，RMSE 0.02）。

## Research Question
如何利用易于获取的物理特性（温度、密度、孔隙率、P波速度）和人工智能方法，快速、准确地量化热处理后慢速冷却与快速冷却条件下花岗岩的损伤程度（热损伤因子），以避免传统实验室方法的耗时与高成本？[Khan 2022, pp. 1-2]

## Study Area / Data
- 岩样采集自巴基斯坦Khyber Pakhtunkhwa省Buner区Baba G Kandaw采石场，属Swat花岗岩片麻岩区的花岗岩体 [Khan 2022, pp. 3-4]。
- 岩性组成（平均）：钾长石47.29%、石英25.18%、斜长石24.38%、黑云母32.03%、白云母0.15%、其他0.97% [Khan 2022, pp. 4-5]。
- 圆柱形岩芯尺寸54×108 mm，按ISRM标准制备 [Khan 2022, pp. 3-4]。
- 样品分组：An（参考，25°C）、Bn/Cn/Dn（慢冷：300/600/900°C）、En/Fn/Gn（快冷：300/600/900°C） [Khan 2022, pp. 4-5]。
- 测试数据见表1，包括温度、孔隙率、密度、P波速度和弹性模量，以及据此计算的两种热损伤因子DTρ和DTE [Khan 2022, pp. 4-5]。
- 数据集共40个点，划分为训练（75%）、测试（15%）和验证（15%） [Khan 2022, pp. 10-12]。

## Methods
- 热损伤因子计算：DTρ = (1 - (1 - n_T)/(1 - n_T0)) × 100%；DTE = 1 - E_T / E_0 [Khan 2022, pp. 5-7]。
- **多元线性回归（MLR）**：针对四种情况（慢冷/快冷 × 基于孔隙率/弹性）分别建立线性方程，输入变量为T、ρ、φ、V_P [Khan 2022, pp. 7-8]。
- **人工神经网络（ANN）**：采用前馈反向传播网络，隐藏层使用正切Sigmoid激活函数；测试了五种训练算法：BFG、RP、SCG、CGB和LM；通过自编译MATLAB代码生成2000个网络（每种算法500个），对最多100个神经元进行循环优化，以R²、a20指数、RMSE、MAPE和VAF评价性能 [Khan 2022, pp. 8-12]。
- **自适应神经模糊推理系统（ANFIS）**：使用减法聚类（sub‑clustering）生成FIS，输入隶属函数为高斯型，输出为线性，混合训练算法，50个epoch [Khan 2022, pp. 15-17]。
- 模型间比较基于R²、a20指数、RMSE、MAPE、VAF等指标，最优模型为LM算法的ANN [Khan 2022, pp. 17-19]。

## Key Findings
- 花岗岩的损伤程度随温度升高而增大，且快冷造成的损伤高于慢冷 [Khan 2022, pp. 19-20]。
- 在五种训练函数（BFG、RP、SCG、CGB、LM）中，LM算法在R²、RMSE、收敛速度和所需神经元数方面综合最优 [Khan 2022, pp. 10-12]。
- ANN模型的预测精度显著优于MLR和ANFIS：慢冷条件下基于孔隙率的ANN预测DT，R²=0.99，a20=0.99，RMSE=0.01，MAPE=0.14%，VAF=100%；快冷条件下R²=0.99，a20=0.99，RMSE=0.02，MAPE=0.36%，VAF=99.99% [Khan 2022, pp. 17-19]。
- 基于孔隙率的损伤因子预测优于基于弹性模量的预测：无论在慢冷还是快冷条件，孔隙率型ANN模型的RMSE更低（慢冷0.01 vs. 0.07；快冷0.02 vs. 0.09） [Khan 2022, pp. 13-15]。
- ANFIS模型虽性能优于MLR，但其训练时间过长（随输入和epoch增加尤为显著），限制了其实用性 [Khan 2022, pp. 17-19]。
- 所有模型在低温（<200°C）和高温（>600°C）下预测精度较高，中温区因热致损伤的非线性增加导致偏差略大 [Khan 2022, pp. 17-19]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 基于LM算法的ANN模型预测慢冷孔隙率型DT：R²=0.99，a20=0.99，RMSE=0.01，MAPE=0.14%，VAF=100% | [Khan 2022, pp. 17-19], Table 4 | 缓慢冷却，输入T, ρ, φ, V_P，40个数据点，LM训练，80个神经元 | 最优模型 |
| ANN预测快冷孔隙率型DT：R²=0.99，a20=0.99，RMSE=0.02，MAPE=0.36%，VAF=99.99% | [Khan 2022, pp. 17-19], Table 4 | 快速冷却，LM训练，18个神经元 | 次优，但远优于MLR和ANFIS |
| MLR模型慢冷孔隙率型DT：R²=0.97，RMSE=0.061 | [Khan 2022, pp. 7-8], Figure 3 | 缓慢冷却，多元线性回归 | 精度较低 |
| ANFIS模型慢冷孔隙率型DT：R²=0.98，RMSE=0.07 | [Khan 2022, pp. 15-17], Figure 11 | 缓慢冷却，减法聚类+Sugeno FIS | 训练耗时 |
| LM算法在R²、RMSE、神经元数和执行时间上均优于BFG、RP、SCG、CGB | [Khan 2022, pp. 10-12], Table 2 | 5种算法对比 | LM收敛更快 |
| 快冷条件下样品Gn (900°C)的孔隙率从1.33%升至13.53%，DTρ高达0.90 | [Khan 2022, pp. 4-5], Table 1 | 快速冷却，900°C | 最大损伤值 |
| ANN模型基于孔隙率在慢冷下最佳神经元数为80，快冷下为18 | [Khan 2022, pp. 12-13], Figure 7 | LM算法 | 神经元优化结果 |
| MLR方程式(11)‑(14)，如DTER = 50.6946 + 0.0005T - 0.0032ρ - 0.0185φ - 0.0002PV | [Khan 2022, pp. 7-8] | 快速冷却，基于弹性 | 具体系数可复现 |

## Limitations
- 研究仅针对巴基斯坦特定区域的花岗岩，岩性单一；岩石行为具有地域差异性，结论的外推需谨慎 [Khan 2022, pp. 17-19]。
- 数据集仅40个点，训练样本量偏小，可能限制模型的泛化能力 [Khan 2022, pp. 17-19]。
- ANFIS模型的训练耗时随输入维度和epoch增加而急剧增长，限制了其实时应用的潜力 [Khan 2022, pp. 17-19]。
- 文中仅比较了MLR、ANN和ANFIS，未涵盖决策树、随机森林等其他常见机器学习方法 [Khan 2022, pp. 17-19]。

## Assumptions / Conditions
- 损伤因子仅通过孔隙率下降（DTρ）和弹性模量下降（DTE）间接表征，未考虑裂纹密度、声发射等其他直接指标 [Khan 2022, pp. 1-2]。
- 热处理速率固定为5°C/min，冷却方式简化为“暴露于空气中”的慢冷和“浸入水中”的快冷，未考虑中等冷却速率 [Khan 2022, pp. 3-4]。
- 输入的物理参数（T, ρ, φ, V_P）和输出DT均在实验温度范围（25‑900°C）和本文所研究的特定岩性内有效 [Khan 2022, pp. 17-19]。
- ANN模型采用正切Sigmoid激活函数和LM训练算法，其他激活函数或梯度下降变体可能产生不同结果 [Khan 2022, pp. 8-12]。
- 所有模型的评价指标基于同一数据集划分（75/15/15）的单次实验，未提及交叉验证 [Khan 2022, pp. 10-12]。

## Key Variables / Parameters
- **输入变量**：温度（T）、孔隙率（φ）、密度（ρ）、P波速度（V_P） [Khan 2022, pp. 1-2]。
- **输出（目标）变量**：基于孔隙率的热损伤因子（DTρ）和基于弹性模量的热损伤因子（DTE） [Khan 2022, pp. 5-7]。
- **ANN训练参数**：正切Sigmoid激活函数；五种训练算法（LM, BFG, RP, SCG, CGB）；神经元数1‑100 [Khan 2022, pp. 8-12]。
- **ANFIS参数**：减法聚类生成FIS，影响范围0.5，挤压因子1.25，接受率0.5，拒绝率0.15；256条模糊规则；50个epoch [Khan 2022, pp. 15-17]。
- **模型评价指标**：决定系数（R²）、a20指数、均方根误差（RMSE）、平均绝对百分比误差（MAPE）、方差解释率（VAF） [Khan 2022, pp. 17-19]。

## Reusable Claims
1. 对于热‑冷联合作用下的花岗岩，基于孔隙率变化计算的[[热损伤因子]]，比基于弹性模量变化的损伤因子更适合作为[[机器学习]]预测的目标变量，其预测误差更低（慢冷RMSE 0.01 vs. 0.07，快冷0.02 vs. 0.09）[Khan 2022, pp. 13-15, 17-19]。  
   *条件*：在25‑900°C的热处理范围内，采用-5°C/min升温和空气慢冷/水淬快冷方式，对高钾长石花岗岩有效。  

2. 采用Levenberg‑Marquardt (LM) 算法的[[前馈神经网络]]，在预测热损伤因子时，比BFG、RP、SCG、CGB等算法具有更快的收敛速度和更低的RMSE，同时所需神经元数量更少 [Khan 2022, pp. 10-12]。  
   *条件*：网络结构为4输入1输出，隐藏层使用正切Sigmoid激活，数据集40个点，最大迭代次数和训练参数为本研究默认设置。  

3. 基于孔隙率的LM‑ANN模型在缓慢冷却下的性能指标为R²=0.99、a20=0.99、RMSE=0.01、MAPE=0.14%，在快速冷却下为R²=0.99、a20=0.99、RMSE=0.02、MAPE=0.36%，可作为未来[[地热工程]]、[[核废料处置]]等高温岩石力学环境中快速评估热损伤的基准模型 [Khan 2022, pp. 17-19]。  
   *条件*：模型输入参数必须处于本文所用的数据范围内（T: 25‑900°C; ρ: 2670‑2682 kg/m³; φ: 1.33‑13.53%; V_P: 3210‑4099 m/s），且岩石类型为相似矿物组成的花岗岩。  

4. 在输入数据范围相似的情况下，MLR模型虽解释性较强，但相比ANN和ANFIS其精度不足（慢冷孔隙率DT的MLR R²=0.97，RMSE=0.061），不适用于需要高精度损伤量化的场景 [Khan 2022, pp. 17-19]。  

5. 快速冷却（水冷）比缓慢冷却（空气冷）在相同温度下引起更严重的损伤：例如900°C时，慢冷DTρ=0.86，快冷DTρ=0.90 [Khan 2022, pp. 4-5]。  
   *条件*：冷却方式的定义为“浸入水中”与“暴露在空气中”，对于其他冷却介质（如油冷或喷雾冷却）需另外验证。

## Candidate Concepts
- [[热损伤因子 (Themal Damage Factor)]]  
- [[孔隙率损伤因子 (Porosity-based Damage Factor)]]  
- [[弹性损伤因子 (Elasticity-based Damage Factor)]]  
- [[慢速冷却 (Slow Cooling)]]  
- [[快速冷却 (Rapid Cooling)]]  
- [[热处理 (Thermal Treatment)]]  
- [[花岗岩高温劣化]]  
- [[Levenberg-Marquardt算法]]  
- [[正切Sigmoid激活函数]]  
- [[前馈反向传播神经网络]]  
- [[自适应神经模糊推理系统 (ANFIS)]]  
- [[减法聚类 (Sub-clustering)]]  
- [[超声波P波速度]]  
- [[岩石孔隙率演化]]  
- [[多模型比较评价指标 (R², RMSE, MAPE, VAF, a20)]]  

## Candidate Methods
- [[多元线性回归 (MLR)]]  
- [[人工神经网络 (ANN)]]  
- [[LM训练算法 (trainlm)]]  
- [[BFGS准牛顿算法 (trainbfg)]]  
- [[弹性反向传播 (trainrp)]]  
- [[标度共轭梯度 (trainscg)]]  
- [[Powell-Beale重启动共轭梯度 (traincgb)]]  
- [[ANFIS混合训练]]  
- [[Sugeno型模糊推理系统]]  
- [[数据归一化 (min-max normalization)]]  
- [[前馈神经网络结构优化（循环生成网络）]]  

## Connections To Other Work
- 本研究直接借鉴了Sirdesai等人 (2018) 的工作，该工作使用MLR、ANN和ANFIS预测印度细粒砂岩的热损伤，并提出ANFIS优于ANN；而本研究发现对于花岗岩，LM‑ANN表现更佳，完善了AI技术在热损伤预测中的适用性讨论 [Khan 2022, pp. 2-4]。
- 文中引用了大量关于热处理下岩石力学性质变化的基础研究（如Chen et al., 2017；Zhao, 2016；Kumari et al., 2017等），为损伤因子的选择和实验设计提供了依据 [Khan 2022, pp. 19-21]。
- 在预测岩石强度与变形参数方面，前人多采用ANN、ANFIS或混合模型（如Armaghani et al., 2016；Singh et al., 2012），本文将其扩展至热损伤因子的预测，并与传统统计方法进行了系统比较 [Khan 2022, pp. 2-3]。
- 作者团队的前期工作（如Khan et al., 2021, 2022）探讨了利用红外辐射和机器学习预测砂岩破坏，本工作进一步将预测对象延伸至花岗岩的热损伤因子 [Khan 2022, pp. 21-22]。

## Open Questions
- 在其他火成岩或变质岩类型（如玄武岩、片麻岩）中，基于孔隙率的热损伤因子预测是否仍保持高精度？[Khan 2022, pp. 17-19]（文中提到需考虑多种岩石以泛化模型）
- 若将冷却速率、矿物晶体大小、微裂纹形态等作为额外输入，能否进一步提升ANN模型的预测能力？[Khan 2022, pp. 17-19]（文中未涉及）
- ANFIS训练耗时长的问题能否通过特征选择或简化规则库得到缓解，从而使其在实际工程中更具竞争力？[Khan 2022, pp. 17-19]（文中指出ANFIS局限但未提出解决方案）
- 结合声发射和红外热成像等实时监测手段，能否开发出实时的损伤因子预测模型，以服务于高温岩石工程的动态安全评估？[Khan 2022, pp. 19-20]（作者在结论中提出未来方向）
- 对于中等冷却速率或循环热‑冷情况，本研究所建立的模型是否依然有效？[Khan 2022, pp. 17-19]（文中仅涉及极端的慢冷与快冷）

## Source Coverage
All 17 non‑empty indexed source blocks have been processed. The coverage by source blocks is 100%, and by characters is approximately 99.97% (81,118 of 81,145 characters), corresponding to a full-index compile. No fragments were omitted.
