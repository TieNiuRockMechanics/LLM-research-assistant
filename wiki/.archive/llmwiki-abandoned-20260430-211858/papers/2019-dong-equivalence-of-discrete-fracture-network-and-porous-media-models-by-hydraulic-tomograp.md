---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2019-dong-equivalence-of-discrete-fracture-network-and-porous-media-models-by-hydraulic-tomograp"
title: "Equivalence of Discrete Fracture Network and Porous Media Models by Hydraulic Tomography."
status: "draft"
source_pdf: "data/papers/2019 - Equivalence of Discrete Fracture Network and Porous Media Models by Hydraulic Tomography.pdf"
collections:
citation: "Dong, Yanhui, et al. \"Equivalence of Discrete Fracture Network and Porous Media Models by Hydraulic Tomography.\" *Water Resources Research*, 2019. doi:10.1029/2018WR024290."
indexed_texts: "14"
indexed_chars: "65786"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T23:00:55"
---

# Equivalence of Discrete Fracture Network and Porous Media Models by Hydraulic Tomography.

## One-line Summary
本研究通过合成水力层析实验证明，当离散裂隙网络存在空间表征单元体时，基于等效多孔介质模型的层析成像可以准确预测独立水流场；当不存在该表征单元体时，该模型仍能捕捉大尺度连通裂隙。 [Dong 2019, pp. 1-2]

## Research Question
水力层析成像（HT）通常在等效多孔介质（EPM）模型框架下进行反演，这一做法可能会高估HT在真实离散裂隙介质中的表现。因此，本研究要回答的核心问题是：在何种条件下，基于EPM模型的水力层析成像能够有效刻画离散裂隙网络中的水流行为？ [Dong 2019, pp. 1-1]

## Study Area / Data
本研究为二维合成数值实验。数据由FracMan软件生成，模拟区域尺寸为1000 m × 1000 m × 1 m。研究设计了三个裂隙密度递增的离散裂隙网络模型（Model A, B, C），用于生成虚拟的注水试验数据。 [Dong 2019, pp. 3-4]

## Methods
研究分为四步：
1.  **裂隙网络建模**：利用FracMan软件生成包含两组小裂隙和两条大断层、但具有不同裂隙密度的离散裂隙网络模型。裂隙生成采用Enhanced Baecher Model，其中心位置基于泊松过程。 [Dong 2019, pp. 3-4]
2.  **水流模拟与数据生成**：使用MAFIC程序（Miller et al., 2001）在上述DFN中模拟水流，并将裂隙划分为三角形单元。研究为合成层析成像生成了虚拟的注水试验数据。 [Dong 2019, pp. 4-5]
3.  **水力层析成像反演**：采用`Simultaneous Successive Linear Estimator (SimSLE)`算法，结合EPM模型（VSAFT2软件），利用合成数据进行瞬态水力层析成像反演，估算整个区域的水力传导系数（K）和贮水率（Ss）分布。 [Dong 2019, pp. 5-5]
4.  **等效性验证**：利用反演得到的K和Ss场，在EPM模型中对独立抽水试验进行预测，并将预测水头与原始DFN模型模拟的观测水头进行对比（`validation`）。 [Dong 2019, pp. 1-1]

## Key Findings
- **空间REV是等价性的判据**：本研究定义了裂隙连通概率的空间表征单元体（spatial REV）。若该空间REV存在，则DFN与EPM等价，利用基于EPM的HT可以准确预测整个区域的流场。 [Dong 2019, pp. 1-1]
- **稀疏裂隙网络（无空间REV）**：对于不存在空间REV的稀疏网络（如Model A），基于EPM的HT反演主能捕捉大尺度连通裂隙，但无法有效分离水力隔离区域。这表现为其无法识别出不与注水井相连的观测井，导致对这些井的水头预测偏高（`overpredicted`）。 [Dong 2019, pp. 1-1, pp. 6-7]
- **稠密裂隙网络（空间REV临近或存在）**：对于裂隙密度较高的网络（如Model B, C），HT反演能成功刻画主要的导水结构（如断层F1, F2）和低渗透区分隔开的独立裂隙簇。在验证中，更多的数据点聚集在1:1线附近，说明估计的EPM参数场可以很好地预测DFN的独立水流行为。在Model C中，连一口未连接裂隙的验证井（V12）的水头都被成功预测，表明反演模型捕捉到了这种非连通特征并将其转化为低K区。 [Dong 2019, pp. 7-9]
- **贮水率（Ss）估算的异常**：反演估算的Ss呈现与裂隙分布相关的异常模式。在DFN模型中所有裂隙被赋予统一的Ss值，但基于EPM的HT估算结果却显示，连通裂隙区域具有高Ss值，而低K区具有低Ss值。这种现象是由于模型替代效应（DFN与EPM）和参数补偿共同作用的结果。 [Dong 2019, pp. 5-7]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 若裂隙连通概率的空间REV存在，则DFN与EPM等价，基于EPM的HT可准确预测流场。 | [Dong 2019, pp. 1-1] | 定义的准则基于整个DFN区域。 | 反之亦然，等价性成立。 |
| 对于无空间REV的稀疏DFN（Model A），HT无法区分与抽水井无水力联系的井，导致对这些井的水头被高估。 | [Dong 2019, pp. 1-2, pp. 7-8] | Model A共200条裂隙 | 这导致`overpredicted`，即预测水头高于DFN模拟值。 |
| 对于裂隙密度极高的Model C，HT能捕捉到非连通特征，使未连接裂隙的验证井（V12）水头被准确预测。 | [Dong 2019, pp. 7-8] | Model C共1000条裂隙 | 反演将非连通性转化为了低K区。 |
| 反演所得高K区主要沿大断层（F1, F2）和裂隙密集连接区域分布。 | [Dong 2019, pp. 7-8] | 所有模型（A, B, C） | Model C的周边还出现了一个圆形低K区。 |
| 估算的Ss场出现异常：连通裂隙区呈高Ss，低K区呈低Ss。 | [Dong 2019, pp. 5-7] | 所有模型 | 这被认为是用连续EPM模型替代离散DFN模型进行反演时的产物。 |

## Limitations
- **二维简化模型**：本研究采用二维DFN模型，并忽略了真实世界中存在的岩石基质对水流的影响。 [Dong 2019, pp. 3-4, pp. 4-5]
- **合成实验**：所有实验均为合成数值实验，结论的有效性尚未通过现场实验证实。 [Dong 2019, pp. 2-3]
- **几何参数单一**：未探讨裂隙几何参数（如方向、大小、位置分布等）变化对HT性能的影响，主要关注裂隙密度。 [Dong 2019, pp. 3-4]
- **模型边界效应**：无通量边界会影响估计结果，例如在Model C的K层析图中，外围出现了圆形的低K区域。 [Dong 2019, pp. 7-8]

## Assumptions / Conditions
- **裂隙水流**：裂隙内水流假设为层流。二维裂隙网络模型的主控方程基于裂隙导水系数（T）和贮水系数（S）。 [Dong 2019, pp. 4-5]
- **无基质**：DFN模型模拟时未包含包围裂隙的岩石基质，仅计算裂隙中的水头分布。 [Dong 2019, pp. 4-5]
- **恒定裂隙参数**：每组裂隙（Set1, Set2, F1, F2）内部的水力和几何参数保持不变。 [Dong 2019, pp. 3-4]
- **初始条件和边界**：初始水头场在空间上均匀分布，为100 m。模型所有边界设为无通量边界。 [Dong 2019, pp. 4-5]
- **EPM模型等效性**：基于SimSLE和EPM-hetero模型反演得到的参数场不是DFN模型的真实参数，而是能在观测井处重现所有注水试验水头过程的`conditional effective parameter fields`。 [Dong 2019, pp. 8-10]

## Key Variables / Parameters
- **裂隙连通概率的空间表征单元体** (`spatial REV of the fracture connectivity probability`): 用于判定DFN与EPM等价性的关键概念。 [Dong 2019, pp. 1-1]
- **水力传导系数 (K) / 贮水率 (Ss)**: 水力层析成像直接反演的目标参数场。 [Dong 2019, pp. 5-5]
- **裂隙强度 (Fracture Intensity)**: 控制DFN模型性能的核心变量，本研究中用裂隙总数（Model A: 200, B: 500, C: 1000）来衡量。 [Dong 2019, pp. 3-4]
- **导水系数 (T)**: `T = Kb = kρg b / μ`，裂隙中水流模拟的核心参数，由渗透率和隙宽决定。 [Dong 2019, pp. 4-5]
- **裂隙渗透率 (k) / 裂隙隙宽 (b)**: 定义裂隙水力特性的基础参数，具体取值见片段表格。 [Dong 2019, pp. 3-4]
- **残差方差 (Residual Variance)**: 用于表征HT估计结果的不确定性。 [Dong 2019, pp. 5-7, pp. 7-8]

## Reusable Claims
- **Claim 1**: 基于等效多孔介质模型的水力层析成像在DFN中的有效性，可以通过裂隙连通概率的空间REV是否存在来判定。若该空间REV存在，则HT-EPM方法有效；若不存在，则该方法仅能捕捉大尺度连通特征，无法精细刻画小尺度非连通结构。[Dong 2019, pp. 1-1] （适用条件：二维DFN，无基质，基于泊松过程生成的裂隙。）
- **Claim 2**: 使用EPM模型对DFN生成的数据进行HT反演时，可能产生与先验认知相悖的贮水率（Ss）场，即高导水区同时呈现高贮水率。这并非反映真实物理属性，而是连续介质模型替代离散模型时产生的“条件有效参数”效应，在解释此类结果时需要谨慎。[Dong 2019, pp. 5-7, pp. 8-10] （适用条件：无基质DFN模型生成的数据，使用连续EPM模型进行反演。）
- **Claim 3**: HT反演得到的不确定性（残差方差）图并不完全遵循探测到的高渗透带模式，无法直接作为裂隙网络的“分辨率矩阵”使用。低不确定性区域可能出现在高K带周围，也可能沿某些连通裂隙延伸，甚至在估计的低K带附近，但其空间模式与高K带并不完全一致。[Dong 2019, pp. 5-7, pp. 7-8] （适用条件：基于SimSLE的HT反演。）

## Candidate Concepts
- [[fractured reservoir]]
- [[discrete fracture network]]
- [[equivalent porous media]]
- [[representative elementary volume]]
- [[hydraulic tomography]]
- [[conditional effective parameters]]

## Candidate Methods
- [[FracMan]]
- [[MAFIC]]
- [[SimSLE]]
- [[VSAFT2]]

## Connections To Other Work
索引片段未提供可直接确认的与其他具体研究的详细比较或否定性结论。但可从主题上连接到：
- 关于等效连续介质模型（EPM）适用性的研究，特别是涉及 [[representative elementary volume]] 的经典讨论。
- 其他在水力层析成像中使用EPM进行反演以刻画[[fracture network]]的研究，例如Illman (2014), Zha et al. (2016)等。未从索引片段中确认这些研究与本工作的具体结论差异。
- 水流模型选择，如双重孔隙度或双重渗透率模型（EPM-dual）与本研究采用的非均质EPM模型（EPM-hetero）的异同点。[Dong 2019, pp. 1-2]

## Open Questions
- 该结论在包含真实岩石基质的复杂三维裂隙网络中是否依然成立？未从索引片段中确认。
- 现场尺度的实验能否验证这些合成实验的发现？未从索引片段中确认。
- 裂隙的几何参数（如方向、尺寸的空间变异性）而非仅仅是密度对EPM等效性有何定量影响？未从索引片段中确认。
- 是否存在一个定量的裂隙密度阈值，可以普遍地判定空间REV的成立与EPM模型的适用性？未从索引片段中确认。

## Source Coverage
本知识页基于论文的14个索引片段，覆盖了摘要、方法设计、关键结果讨论和主要结论等多个部分。索引片段包含了三个模型的层析成像结果图（图2，图4）及其详细解释，因此对核心实验结果的覆盖度较高。然而，片段缺失了对SimSLE反演算法的具体公式和实现细节的描述，也缺少对“裂隙连通概率的空间REV”这一关键概念如何具体计算和定义的严格数学描述。讨论和结论部分的信息相对完整。
