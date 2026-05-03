---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-waqas-investigation-of-strength-behavior-of-thermally-deteriorated-sedimentary-rocks-subjec"
title: "Investigation of Strength Behavior of Thermally Deteriorated Sedimentary Rocks Subjected to Dynamic Cyclic Loading."
status: "draft"
source_pdf: "data/papers/2022 - Investigation of strength behavior of thermally deteriorated sedimentary rocks subjected to dynamic cyclic loading.pdf"
collections:
  - "论文"
citation: "Waqas, Umer, and Muhammad Farooq Ahmed. “Investigation of Strength Behavior of Thermally Deteriorated Sedimentary Rocks Subjected to Dynamic Cyclic Loading.” *International Journal of Rock Mechanics & Mining Sciences*, vol. 158, 2022, 105201. doi:10.1016/j.ijrmms.2022.105201."
indexed_texts: "15"
indexed_chars: "74613"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "70669"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.947141"
coverage_status: "full-index"
source_signature: "40619ff02b67ee952b0cc6961c2d674ebbdc35ea"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T05:41:27"
---

# Investigation of Strength Behavior of Thermally Deteriorated Sedimentary Rocks Subjected to Dynamic Cyclic Loading.

## One-line Summary
热损伤沉积岩在 5 – 15 kHz 动态循环加载下发生裂纹闭合，刚度提升（强度改善因子 SIF 0 – 39%），ANFIS 预测模型（R=0.97）优于级联前馈神经网络（R=0.93），堆叠元分类器 MC 对 SIF 分类准确率达 100%。[Waqas 2022, pp. 1-2, 13-14]

## Research Question
1) 热损伤沉积岩在动态循环加载（共振效应）下的强度行为如何变化？  
2) 能否利用动态参数预测强度改善因子（SIF）并对岩石刚度进行可靠分类？[Waqas 2022, pp. 1-2, 13-14]

## Study Area / Data
- **采样地点**：巴基斯坦旁遮普省 Khewra 峡谷。 [Waqas 2022, pp. 2-3]  
- **岩石类型**：前寒武纪 Salt Range 泥灰岩；寒武纪 Khewra 组上、中、下砂岩，Kussak 砂岩，Jutana 白云岩；二叠纪 Tobra 砂岩；始新世 Namal 石灰岩，Sakesar 块状石灰岩和结核石灰岩。 [Waqas 2022, pp. 3-6, Table 1]  
- **样本制备**：NX 尺寸岩心，长径比 2.5 – 3，60 个样本，干燥器除湿 24 h。 [Waqas 2022, pp. 2-3]  
- **热循环处理**：以 1 – 5°C/min 升温，50℃ → 100℃ → 150℃ → 200℃ 逐级加热，每级后在干燥器中冷却至室温，产生热拉裂缝。 [Waqas 2022, pp. 2-3]  
- **实验数据**：在 5 – 15 kHz 激发频率下测得的动弹性模量 E、动剪切模量 G、泊松比 v、纵/扭共振频率 (Fr)L、(Fr)T、品质因子 QL、QT，以及单轴抗压强度 UCS。 [Waqas 2022, pp. 3-4, Table 1, pp. 10-13]

## Methods
- **动态测试**：按 ASTM C215 使用 Erudite 共振频率仪，在纵、扭模式下 5 – 15 kHz 非破坏性测量共振频率和品质因子，计算 E、G、v。 [Waqas 2022, pp. 3-4]  
- **强度测试**：按 ASTM D7012 用 200 t Shimadzu UTM，加载速率 0.5 – 1.0 MPa/s，测定 UCS。 [Waqas 2022, pp. 3-4]  
- **强度改善因子 SIF**：利用泊松比初/终值计算 SIF = (1 − v_i² / v_f²) × 100%，并按 0 – 10%（VLI）、11 – 40%（LI）等分级。 [Waqas 2022, pp. 3-4, 13-14]  
- **预测建模**：以 (Fr)L/(Fr)T 和 QL/QT 为自变量，SIF 为因变量，分别用级联前馈神经网络 CFNN（单隐藏层10神经元）和自适应神经模糊推理系统 ANFIS（4条模糊规则）建立预测模型，数据集70%训练/20%验证/10%测试。 [Waqas 2022, pp. 4-6, 13]  
- **分类器选择**：用 10 折交叉验证，比较 NB、LR、ANN-MLP、SVM、K-NN、RF 六种分类器，并堆叠构建元分类器 MC；以混淆矩阵、精准率、召回率、F 值、ROC/AUC、MCC 和错误率评价性能。 [Waqas 2022, pp. 6-14]

## Key Findings
1. **热损伤与共振效应**：200°C 循环加热后 UCS 普遍下降（硅酸盐砂岩 15 – 20%，泥灰岩 38%，白云岩 27%，Namal 石灰岩 10%），但在 5 – 15 kHz 共振下，因热裂纹弹性闭合，刚度提高，SIF 范围 0 – 39%（仅 VLI 与 LI 组）。 [Waqas 2022, pp. 10-11, 13-14]  
2. **动态参数线性增加**：(Fr)L 增加 1.5 – 2.2 kHz，(Fr)T 增加 1.0 – 1.8 kHz，QL 提高 16 – 30，QT 提高 9 – 20；动弹性模量 E 在硅酸盐岩中提高 9 – 20%（碳酸盐岩 4 – 7%），动剪切模量 G 硅酸盐岩提高 0 – 13%（碳酸盐岩 0 – 3%）。 [Waqas 2022, pp. 10-13]  
3. **预测模型性能**：ANFIS 模型（R = 0.97）优于 CFNN 模型（R = 0.93）；CFNN 的 MSE 在 epoch 17 达到最低，训练、验证、测试的 R 分别为 0.82、0.86、0.95。 [Waqas 2022, pp. 13-14]  
4. **分类性能排序**：堆叠元分类器 MC 的混淆矩阵显示 60/60 全部分类正确（F-measure = 1.000，AUC = 1.00，MCC = 1.00，错误率 0%），优于其他分类器；顺序为 MC > RF > NB > LR > ANN-MLP > K-NN > SVM。 [Waqas 2022, pp. 13-14]  
5. **分类器对比**：RF 分类准确率 98%，NB 93%，LR 91%，ANN-MLP 90%，K-NN 88%，SVM 85%。 [Waqas 2022, pp. 14]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| UCS 下降：硅酸盐砂岩 15–20%，泥灰岩 38%，白云岩 27%，Namal 灰岩 10% | [Waqas 2022, pp. 10-11] | 循环加热至 200°C，步长 50°C | 证实热裂纹产生 |
| 共振下 (Fr)L 增加 1.5–2.2 kHz，(Fr)T 增加 1.0–1.8 kHz | [Waqas 2022, pp. 10-11] | 5–15 kHz 激发频率，ASTM C215 | 线性增加趋势 |
| 共振下 E 增加（硅酸盐 9–20%，碳酸盐 4–7%），G 增加（硅酸盐 0–13%，碳酸盐 0–3%） | [Waqas 2022, pp. 12-13] | 同上 | 硅酸盐刚度提升更显著 |
| SIF 范围 0–39%，仅 VLI 和 LI 两组 | [Waqas 2022, pp. 13-14] | 基于泊松比变化 | 共振改善刚度有限 |
| ANFIS 模型 R=0.97 vs CFNN 模型 R=0.93 | [Waqas 2022, pp. 13-14] | 输入 (Fr)L/(Fr)T, QL/QT | ANFIS 性能更优 |
| MC 分类准确率 100%（60/60），F-measure=1.000，AUC=1.00，MCC=1.00 | [Waqas 2022, pp. 13-14] | 堆叠六种分类器 | 最佳分类器 |
| RF 分类准确率 98%，NB 93%，LR 91%，ANN-MLP 90%，K-NN 88%，SVM 85% | [Waqas 2022, pp. 13-14] | 相同测试集 | 分类器性能排序 |

## Limitations
- 加热上限仅 200°C，未涉及更高温度下的共振效应。 [Waqas 2022, pp. 1-2, 14]  
- 岩石类型限于所选沉积岩（硅酸盐和碳酸盐），未包括其他岩类。 [Waqas 2022, pp. 3-4, 6-7]  
- SIF 分类仅包含两个实际出现组（VLI、LI），未覆盖 MI、MHI、HI 组。 [Waqas 2022, pp. 13-14]  
- 共振试验在常温和干态下进行，未考虑湿度、围压等现场条件。 [Waqas 2022, pp. 2-3]  

## Assumptions / Conditions
- 热循环升温速率 1–5°C/min，逐级冷却至室温，保证热裂纹萌生。 [Waqas 2022, pp. 2-3]  
- 共振测试激发频率 5–15 kHz，最低输出电压 0.01 V，符合 ASTM C215。 [Waqas 2022, pp. 3-4]  
- 动态弹性参数由共振频率和样本尺寸、质量计算（D_cylinder = 520L/d²，B_cylinder = 400L/A）。 [Waqas 2022, pp. 3-4]  
- SIF 基于泊松比变化定义：SIF = (1 − v_i² / v_f²)×100%。 [Waqas 2022, pp. 3-4]  
- 预测建模中，训练集 70%，验证集 20%，测试集 10%。 [Waqas 2022, pp. 13]  
- 分类采用 10 折交叉验证，各类别权重均匀。 [Waqas 2022, pp. 13-14]

## Key Variables / Parameters
- **独立变量**：(Fr)L/(Fr)T 和 QL/QT（预测 SIF）；动态参数 (Fr)L, (Fr)T, QL, QT, E, G, v。  
- **因变量**：SIF（强度改善因子）。  
- **岩石属性**：岩性（碳酸盐/硅酸盐）、热历史（加热温度 200°C）、UCS 减退量。  
- **模型性能参数**：R、MSE、精准率、召回率、F 值、AUC、MCC、错误率。

## Reusable Claims
1. 热损伤沉积岩在 5–15 kHz 动态循环加载下因热裂纹弹性闭合而刚度提高，SIF 可达 39%（受限于 200°C 加热和该频率范围）。[Waqas 2022, pp. 13-14]  
2. 共振频率 (Fr)L、(Fr)T 和品质因子 QL、QT 均随激发频率增加而线性上升，可用于间接表征岩石致密化程度。[Waqas 2022, pp. 10-11]  
3. 使用共振频率比和品质因子比作为输入，ANFIS 模型能高精度预测 SIF（R=0.97），优于 CFNN 模型（R=0.93）。[Waqas 2022, pp. 13-14]  
4. 堆叠六种基分类器构建的元分类器 MC 在 SIF 二分类问题上性能最优，准确率 100%，可作为热损伤岩石刚度分级的最佳机器学习方案。[Waqas 2022, pp. 13-14]  
5. 在给定的动态数据集上，监督分类器的性能从高到低依次为：MC > RF > NB > LR > ANN-MLP > K-NN > SVM。[Waqas 2022, pp. 14]

## Candidate Concepts
- [[热损伤 rock]]  
- [[动态循环加载]]  
- [[共振刚度提升]]  
- [[裂纹闭合现象]]  
- [[强度改善因子 SIF]]  
- [[级联前馈神经网络 CFNN]]  
- [[自适应神经模糊推理系统 ANFIS]]  
- [[堆叠元分类器 MC]]  
- [[共振频率测试 ASTM C215]]  
- [[岩石动弹性模量]]  
- [[品质因子 Q]]  
- [[监督分类器性能比较]]  
- [[热循环处理]]  
- [[泊松比增加]]

## Candidate Methods
- [[Erudite 共振频率仪]]  
- [[ASTM C215 动态弹性模量测量]]  
- [[ASTM D7012 单轴压缩试验]]  
- [[CFNN 预测建模]]  
- [[ANFIS 模糊规则建模]]  
- [[10 折交叉验证]]  
- [[元分类器堆叠 ensemble]]  
- [[混淆矩阵评估]]  
- [[ROC/AUC 评估]]  
- [[Mathew 相关系数 MCC]]

## Connections To Other Work
- 前人已观察到热损伤岩石的动态响应下降（Zhang et al. 2001，Waqas & Ahmed 2020 等），但未深入共振效应。[Waqas 2022, pp. 1-2]  
- 线性-非线性和质量因子与谱宽的关系在常温共振棒实验中已有探讨（Johnson & Rasolofosaon 1996；Lyakhovsky et al. 2009），本研究将其扩展到热处理岩石。[Waqas 2022, pp. 2, 10-11]  
- 机器学习在岩体工程分类中已应用（Bishop 2006，Mohri et al. 2018），本研究提出的 MC 堆叠方法为热损伤岩石动态分类提供了新参考。[Waqas 2022, pp. 2-3, 14]  
- 本文引用的 Ahmed et al. (2018) 也研究了 Salt Range 岩石的动态性质，本研究在共振频率和 SIF 上做了深化。[Waqas 2022, pp. 14-15]

## Open Questions
- 更高温度（>200°C）或更宽频率范围下，共振导致的刚度提升是否持续，是否出现裂纹重启和非线性衰减？[Waqas 2022, pp. 1-2, 14]  
- 含水率、围压和各向异性对热损伤岩石共振行为的耦合影响尚未涉及。[Waqas 2022, pp. 2, 14]  
- SIF 仅在 VLI 和 LI 区间内观测，更高刚度等级（MI 以上）是否需要更强烈的共振或不同岩石类型？[Waqas 2022, pp. 13-14]  
- 元分类器 MC 的普适性是否可在其他岩石类型或现场声波数据中复现？[Waqas 2022, pp. 14]

## Source Coverage
本页所有非空索引片段（共 15 个，涵盖）[Waqas 2022, pp. 1-15]均已处理。按块覆盖率 100%（15/15），按字符覆盖率 94.7%（总索引字符 74613，编译字符 70669）。无遗漏碎片，未使用外部知识。编译策略：单遍 Markdown 直接组装。
