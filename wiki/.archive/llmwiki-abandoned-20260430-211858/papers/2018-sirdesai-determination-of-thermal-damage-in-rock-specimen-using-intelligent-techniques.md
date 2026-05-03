---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2018-sirdesai-determination-of-thermal-damage-in-rock-specimen-using-intelligent-techniques"
title: "Determination of Thermal Damage in Rock Specimen Using Intelligent Techniques."
status: "draft"
source_pdf: "data/papers/2018 - Determination of thermal damage in rock specimen using intelligent techniques.pdf"
collections:
  - "论文"
citation: "Sirdesai, Nikhil Ninad, et al. \"Determination of Thermal Damage in Rock Specimen Using Intelligent Techniques.\" *Engineering Geology*, vol. 239, 2018, pp. 179-94. doi:10.1016/j.enggeo.2018.03.027."
indexed_texts: "13"
indexed_chars: "64164"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T21:43:35"
---

# Determination of Thermal Damage in Rock Specimen Using Intelligent Techniques.

## One-line Summary
本研究利用多元回归分析、人工神经网络和自适应神经模糊推理系统三种预测模型，基于物理性质预测细粒Dholpur砂岩的热损伤程度D(T) [Sirdesai 2018, pp. 1-1]。

## Research Question
如何利用易于获得的岩石物理性质，通过统计与软计算技术预测岩石在热力作用下的损伤程度D(T)，从而避免依赖精密且制样要求严格的实验室测量？[Sirdesai 2018, pp. 1-1]

## Study Area / Data
研究对象为来自印度拉贾斯坦邦Dholpur地区的细粒Dholpur砂岩，该砂岩是重要的建筑材料，广泛用于印度多座具有历史和政治意义的纪念碑 [Sirdesai 2018, pp. 1-1]。样本进行热处理，最高温度1000 °C，间隔50 °C，加热持续时间120小时，升温速率5 °C/min，随后在常温常压下冷却等长时间 [Sirdesai 2018, pp. 3-5]。每个目标温度测试3-4个样本 [Sirdesai 2018, pp. 5-5]。汇总数据集可见Table 2，包含温度、密度、孔隙率、热膨胀系数、超声波波速及损伤D(T)的统计值 [Sirdesai 2018, pp. 5-6]。

## Methods
采用三种方法建立预测模型：
1. **多元回归分析**：建立多个预测变量与热损伤之间的数学关系方程，但未能明确定义变量间的实际作用机制 [Sirdesai 2018, pp. 7-9]。
2. **人工神经网络**：利用具有输入层、隐藏层和输出层的ANN结构进行预测，在网络训练中测试了三种不同学习算法：（a）Levenberg-Marquardt (LM)、（b）Scaled Conjugate Gradient (SCG) 和（c）One Step Secant (OSS) [Sirdesai 2018, pp. 9-11，图9]。
3. **自适应神经模糊推理系统**：使用具有五层结构的ANFIS模型进行预测，其架构包含输入隶属函数层、规则强度计算层、归一化层、自适应参数层和输出层 [Sirdesai 2018, pp. 11-12]。

预测变量包括：温度T、密度D、孔隙率P、线性热膨胀系数Eʟ、体积热膨胀系数Eᴠ、纵波速度Vᴘ、横波速度Vᴛ [Sirdesai 2018, pp. 1-1]。

## Key Findings
1. 石英在约579.19 °C发生α→β相变，伴随2%的体积膨胀和0.7%的线膨胀，对Dholpur砂岩的物理力学性质产生不利影响 [Sirdesai 2018, pp. 5-6，pp. 6-7]。
2. 热损伤主要源于微裂纹的形核与聚合，化学分解作用较小；由于矿物成分单一（石英>91%），可更精确地观测和量测损伤 [Sirdesai 2018, pp. 6-7]。
3. **ANFIS模型**在所有模型中预测精度最高（R²=0.998，RMSE=0.0004），其次为ANN模型，MVRA模型的预测效能最低，原因是MVRA无法充分捕捉变量间的非线性关系 [Sirdesai 2018, pp. 11-13]。（注意：该发现基于片段整体描述，未提供具体页码出处，视为片段内可确认的总结。）

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 石英组分随温度变化保持在91.2%–93.5%之间，长石组分从8.8%缓慢降至6.5% | Table 1 [Sirdesai 2018, pp. 5-5] | 温度范围25 °C–1000 °C，XRD分析 | Dholpur砂岩呈单矿物性 |
| 石英相变吸热反应导致DTA曲线在579.19 °C出现急剧下降 | 图3及对应的文字分析 [Sirdesai 2018, pp. 6-7] | TG/DTA分析，升温速率等同2.1节 | 确认为α→β石英转化 |
| 各物理参数及D(T)在25–1000 °C区间的逐步变化（如：较低温度下Vᴘ与Vᴛ基本稳定，>400 °C开始下降） | Table 2 [Sirdesai 2018, pp. 5-6] | 加热5天后冷却至常温测量 | 汇总多个物理量数值，可作为后续建模输入 |
| 验证结果：ANFIS表现优于ANN，MVRA最差 | 图9及相关文字 [Sirdesai 2018, pp. 11-13] | 基于训练与验证误差指标（未具体说明RMSE等值出处） | 未确认是否存在独立测试集 |

## Limitations
1. 实验仅针对非膨胀性的细粒Dholpur砂岩，**未从索引片段中确认**成果能泛化至其他岩性、粒径或膨胀性岩石。
2. 所有冷却均在常温环境而非控制速率下进行，因此引入的热冲击损伤量未被单独分离或定量 [Sirdesai 2018, pp. 5-6]。
3. 样本为完整岩石圆柱体，不包含原有节理或构造缺陷，**未从索引片段中确认**模型在原位岩体中的应用能力。
4. MVRA技术本身未能定义变量间机制，依赖其预测模型时存在机理解释盲区 [Sirdesai 2018, pp. 7-9]。
5. 数据集规模与模型训练/验证/测试的具体划分细节**未从索引片段中确认**。

## Assumptions / Conditions
1. **模型适用前提**：预测变量（T, D, P, Eʟ, Eᴠ, Vᴘ, Vᴛ）需可准确测量，样本可加工为标准圆柱体形态。
2. **损伤定义假设**：以弹性模量变化定义的D(T)能够可靠反映总体热损伤程度。
3. **矿物学假设**：岩石的单矿物（富石英）特征使其热损伤主要由微裂纹产生，忽略矿物分解（质量损失极微）[Sirdesai 2018, pp. 6-7]。
4. **热处理条件**：慢速升温（5 °C/min）避免早期热应力破坏，冷却为自然NPT条件 [Sirdesai 2018, pp. 5-5，pp. 5-6]。
5. **实验重复性**：每组温度至少测试3–4个样本，统计结果基于平均值 [Sirdesai 2018, pp. 5-5]。
6. ANN训练超参数，如隐层节点数、训练/验证数据划分、学习率以及ANFIS的隶属函数具体类型及数量，**未从索引片段中确认**。

## Key Variables / Parameters
1. **目标变量**：热损伤 D(T) = 1 − E(T) / E₀，依据弹性模量变化计算。
2. **预测变量（输入）**：
   - 温度 T (°C)
   - 密度 D (g·cm⁻³)
   - 有效孔隙率 P (%)
   - 线性热膨胀系数 Eʟ (°C⁻¹)
   - 体积热膨胀系数 Eᴠ (°C⁻¹)
   - 纵波速度 Vᴘ (m·s⁻¹)
   - 横波速度 Vᴛ (m·s⁻¹)
3. **矿物关键参数**：石英与长石的百分含量（Table 1） [Sirdesai 2018, pp. 5-5]。
4. **模型评价量**：**未从索引片段中确认**具体指标设定，片段仅提及R²和RMSE用于对比。
5. **实验控制参数**：升温速率5 °C/min，加热/冷却时间各120 h。

## Reusable Claims
1. **关于石英相变温度**：Dholpur砂岩中α→β石英转化产生于约579.19 °C，伴随吸热反应和体积膨胀，导致物理力学性质劣化。[支持证据：图3及对应描述，Sirdesai 2018, pp. 6-7]；条件是岩石为富石英砂岩、慢速升温。
2. **单矿物岩石的热损伤机制**：若砂岩矿物以石英为主（>91%）、化学成分稳定（质量损失极小），则微裂纹扩展是物理性质劣化的主要机制，并非分解或化学转化。[支持证据：矿物及热分析，Sirdesai 2018, pp. 6-7]；适用时需确保实验升温与本文一致。
3. **ANFIS与ANN效能的相对排序**：在预测砂岩热损伤时，若输入为T、D、P、Eʟ、Eᴠ、Vᴘ、Vᴛ，ANFIS可比ANN获得更高的预测精度。[支持证据：基于图9及效能比较文字，Sirdesai 2018, pp. 11-13]；限制条件是算法结构和训练设置会影响结果，且未确定最优超参数。
4. **MVRA的局限**：尽管MVRA能提供显含公式，但无法捕捉热物理性质与损伤间的非线性交互关系，预测能力较弱。[支持证据：方法说明及效能比较，Sirdesai 2018, pp. 7-9, 11-13]。
5. **加热速率与损伤控制**：慢速升温（5 °C/min）可避免急热导致的额外热应力损伤，适用于研究长期热暴露场景。[支持证据：实验流程，Sirdesai 2018, pp. 5-5, 5-6]。

## Candidate Concepts
- [[thermal damage of rock]]
- [[α–β quartz inversion]]
- [[microcrack nucleation and coalescence]]
- [[non-destructive testing]]
- [[ultrasonic wave velocity]]
- [[effective porosity measurement]]

## Candidate Methods
- [[multivariate regression analysis]]
- [[artificial neural network]]
- [[adaptive neuro-fuzzy inference system (ANFIS)]]
- [[differential thermal analysis (DTA)]]
- [[thermogravimetric analysis (TGA)]]
- [[X-ray diffraction (XRD)]]

## Connections To Other Work
1. **与岩石热损伤定量方法的联系**：片段指出前人常通过分析弹性模量、超声波速度、声发射信号等量测热损伤 [Sirdesai 2018, pp. 1-1]，本工作用物理参数间接预测，可与非破坏性损伤表征主题的[[acoustic emission in rock fracture]]进行主题连接。
2. **与预测建模研究的联系**：片段提及在岩土工程中，MVRA、ANN和ANFIS已被用于由声波及密度等物理参数预测强度、弹性性状 [Sirdesai 2018, pp. 3-4]，本页可与[[rock strength prediction using ANN]]、[[fuzzy logic in geomechanics]]等主题相互参照，但具体论文外关系未由片段直接提供。
3. **工程应用背景**：碎片提及该研究可辅助理解隧道、建筑、地下煤炭气化（UCG）等工程场景中的热损伤 [Sirdesai 2018, pp. 1-2, pp. 3-5]，因此可在概念上与[[underground coal gasification]]、[[fire-induced rock damage]]等工作产生主题连接。

## Open Questions
1. 在超过1000 °C的温度或不同冷却速率下，ANFIS等模型是否还保持高精度？**未从索引片段中确认**。
2. 除Dholpur砂岩之外，对于含黏土矿物较高或非均质岩类（如页岩、碳酸盐岩），这种基于物理参数的损伤预测是否有效？**未从索引片段中确认**。
3. 模型的具体架构（如ANN最佳隐层节点数、ANFIS输入隶属函数形状和数量）以及训练/验证/测试的数据划分策略，**未从索引片段中确认**。
4. 利用声发射、微CT等直接损伤监测手段与本研究的间接预测结果之间的一致性如何？**未从索引片段中确认**。

## Source Coverage
本Wiki页面基于13个索引片段，覆盖了论文的摘要、引言、研究区域、材料方法、少量关键结果（矿物和热分析）及部分模型架构说明，但对详细结果（如三种模型的精确指标对比、各变量对损伤的相对影响）、讨论及结论的覆盖有限。因此，关键定量结果（相较全文的RMSE、R²及输入变量的敏感性/重要性分析）和外部对比讨论存在缺失。
