---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2024-farhangi-application-of-artificial-intelligence-in-predicting-the-residual-mechanical-prope"
title: "Application of Artificial Intelligence in Predicting the Residual Mechanical Properties of Fiber Reinforced Concrete (FRC) after High Temperatures."
status: "draft"
source_pdf: "data/papers/2024 - Application of artificial intelligence in predicting the residual mechanical properties of fiber reinforced concrete (FRC) after high temperatures.pdf"
collections:
  - "论文"
citation: "Farhangi, Visar, et al. \"Application of Artificial Intelligence in Predicting the Residual Mechanical Properties of Fiber Reinforced Concrete (FRC) after High Temperatures.\" *Construction and Building Materials*, vol. 411, 2024, 134609. Accessed 2026."
indexed_texts: "19"
indexed_chars: "93379"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T13:40:53"
---

# Application of Artificial Intelligence in Predicting the Residual Mechanical Properties of Fiber Reinforced Concrete (FRC) after High Temperatures.

## One-line Summary
本研究通过建立覆盖100–1200 ℃高温的纤维增强混凝土力学性能数据集，训练人工神经网络模型，预测钢纤维和聚丙烯纤维混凝土的残余抗压强度、抗拉强度与弹性模量，并进行概率分析评估失效风险 [Farhangi 2024, pp. 1-1]。

## Research Question
如何利用人工智能模型准确预测纤维增强混凝土（FRC）在高温作用后的残余力学性能，并量化纤维类型、几何特征、含量及水胶比等因素的影响与失效概率？ [Farhangi 2024, pp. 1-1]。

## Study Area / Data
研究数据并非来自单一地理区域，而是从文献中收集的纤维增强混凝土高温后力学性能数据库。数据集涵盖两种纤维类型：钢纤维（SFRC）与聚丙烯纤维（PFRC），温度范围 100–1200 ℃ 。具体数据量如下：
- 抗压强度：SFRC 286 个数据点，PFRC 114 个数据点；
- 抗拉强度：SFRC 78 个数据点，PFRC 100 个数据点；
- 弹性模量：SFRC 85 个数据点，PFRC 82 个数据点 [Farhangi 2024, pp. 3-3]。

输入特征包括水（W）、胶凝材料（B）、粗骨料（G）、细骨料（S）、纤维含量（F）、纤维长度（l）、纤维直径（d）、温度（T）；SFRC 还包含纤维抗拉强度（fᵤ）[Farhangi 2024, pp. 3-3]。输出为相对力学性能比（%），即高温后与常温力学性能的比值 [Farhangi 2024, pp. 2-3]。

数据集揭示文献中存在空白：纤维含量大于 0.8% 的试件研究不足，低水胶比（<0.4）在 800 ℃ 以上高温的实验数据极为匮乏 [Farhangi 2024, pp. 3-5]。

## Methods
采用多层感知机（MLP）作为 AI 模型，针对每种力学性能和纤维类型分别构建六个独立模型。模型输入层、隐藏层、输出层神经元的最终架构如下：
- 抗压强度 SFRC：9-6-1；PFRC：8-15-1
- 抗拉强度 SFRC：9-16-1；PFRC：8-18-1
- 弹性模量 SFRC：9-3-1；PFRC：8-7-1 [Farhangi 2024, pp. 5-5]

数据线性归一化至 [0,1]，激活函数隐藏层为 tansig，输出层为 purelin。使用 Levenberg-Marquardt 算法，将数据随机分为 70% 训练、15% 验证、15% 测试。采用提前停止防止过拟合。模型性能以均方误差（MSE）和相关系数（R）评估 [Farhangi 2024, pp. 5-5]。

## Key Findings
1. **温度影响最为重要**：在全部输入特征中，温度对纤维增强混凝土力学性能的贡献最大，且聚丙烯纤维混凝土对温度更为敏感，其性能退化比钢纤维混凝土更剧烈 [Farhangi 2024, pp. 5-6]。
2. **钢纤维对抗压强度的保留效应**：在所有温度下，钢纤维直径和长度的增加均能使残余抗压强度比提高，整体上钢纤维混凝土的残余抗压强度高于聚丙烯纤维混凝土 [Farhangi 2024, pp. 1-1]。
3. **聚丙烯纤维对拉伸强度的延缓退化效应**：较高的聚丙烯纤维含量和更长的纤维可减缓高温下抗拉强度的降解速率 [Farhangi 2024, pp. 1-1]。
4. **聚丙烯纤维混凝土的复杂高温行为**：在 600 ℃ 以下，聚丙烯纤维长度增加会导致抗压强度比近似线性上升，但直径过小（可能低于某一阈值）会因蒸气压过高产生微裂纹或扩大裂缝，对抗压强度不利。更高纤维含量可控制开裂，但过量可能增加孔隙率和分散不均 [Farhangi 2024, pp. 6-8]。
5. **失效概率分析结果**：大规模概率分析表明，聚丙烯纤维混凝土的失效概率与水胶比无关，约为 50%；钢纤维混凝土在水胶比 0.4 至 0.5 时失效概率相对较低；当水胶比为 0.5 时，两种纤维混凝土的失效概率均几乎不随纤维含量变化 [Farhangi 2024, pp. 1-1]。
6. **纤维抗拉强度的作用差异**：钢纤维的拉伸强度（fᵤ）对抗压强度的影响小于对抗拉强度和弹性模量的影响，原因是压缩荷载下纤维不直接贡献抗拉，且高温下纤维粘结强度降低导致滑移而非屈服 [Farhangi 2024, pp. 5-6]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 温度是对所有机械性能最重要的影响特征，且聚丙烯纤维对温度更敏感 | [Farhangi 2024, pp. 5-6] | 基于全连接重要性分析，6 个 MLP 模型；特征包括配合比、纤维几何、温度和 fu | 文中没有给出定量重要性指标，仅描述了相对趋势 |
| 钢纤维长度和直径增加在全部温度下提高抗压强度比 | [Farhangi 2024, pp. 1-1] | 预测范围：温度 100–1200 ℃，纤维直径 0.25–2.0 mm，长度 20–60 mm | 属于模型泛化分析结果，非单一试验验证 |
| 聚丙烯纤维含量增加和纤维更长降低抗拉强度降解速率 | [Farhangi 2024, pp. 1-1] | 温度 100–800 ℃，聚丙烯纤维含量 0.02–0.78%（表1），纤维长度 6–52 mm | 基于 PFRC 抗拉强度模型预测 |
| 聚丙烯纤维混凝土在低温区（<600 ℃）抗压强度比随纤维长度线性增加 | [Farhangi 2024, pp. 6-8] | 条件：较低纤维含量，温度低于 600 ℃ | 与纤维的裂纹阻止能力相关 |
| 失效概率对 PFRC 与 W/B 比无显著关系，约为 50% | [Farhangi 2024, pp. 1-1] | 概率分析结果，数据覆盖 W/B 0.29–0.6，纤维含量至多 0.78% | 具体概率密度函数未知 |
| SFRC 在 W/B 0.4–0.5 时失效概率低于其他水胶比 | [Farhangi 2024, pp. 1-1] | 钢纤维混凝土数据集范围见 Table 1 | 失效判定标准未从片段确认 |
| MLP 模型测试集 R 值：fc-S 0.994, ft-S 0.984, E-S 0.991, fc-PP 0.993, ft-PP 0.979, E-PP 0.990 | [Farhangi 2024, pp. 5-6] | 训练/验证/测试划分 70/15/15，Levenberg-Marquardt 优化 | 均方误差较低，表明模型拟合良好 |

## Limitations
1. 研究完全基于收集的已有数据，缺乏对稀疏区域（如纤维含量 >0.8%，低水胶比且温度 >800 ℃）的实验验证 [Farhangi 2024, pp. 3-5]。
2. AI 模型为数据驱动黑箱，泛化时依赖训练数据的分布，对分布外数据的预测需谨慎 [Farhangi 2024, pp. 5-6]。
3. 概率分析的具体方法、失效准则未在片段中详细说明，仅报道了结论 [Farhangi 2024, pp. 1-1]。
4. 数据集由不同研究者产生，可能存在配合比、测试方法、养护条件等未记录的异质性，可能影响模型精度。
5. 仅考虑了两种纤维类型（钢与聚丙烯），未包括其他纤维（如玻璃、碳、玄武岩纤维）。

## Assumptions / Conditions
- **模型假设**：MLP 模型采用 Levenberg-Marquardt 算法训练，隐藏层激活函数 tansig，输出层 purelin，假设输入特征与相对强度之间存在可学习的非线性映射 [Farhangi 2024, pp. 5-5]。
- **数据归一化**：所有输入线性归一化到 [0,1]，假设特征间的关系在归一化后保留 [Farhangi 2024, pp. 5-5]。
- **目标定义**：以加热后力学性能与室温性能的比值作为输出，隐含假设室温状态的力学性能被正确记录，且龄期与试件尺寸的影响可通过比值消除 [Farhangi 2024, pp. 3-3]。
- **概率分析条件**：失效概率的分析基于模型输出或数据分布，具体阈值未说明，但已知概率结果独立于 W/B 比（对于 PFRC）或纤维含量（W/B=0.5 时） [Farhangi 2024, pp. 1-1]。

## Key Variables / Parameters
- **输入特征**（8 或 9 个）：水 (W)、胶凝材料 (B)、粗骨料 (G)、细骨料 (S)、纤维含量 (F)、纤维长度 (l)、纤维直径 (d)、温度 (T)；仅 SFRC 包含纤维抗拉强度 (fᵤ) [Farhangi 2024, pp. 3-3]。
- **输出**：相对抗压强度 (f_c ratio, %)、相对抗拉强度 (f_t ratio, %)、相对弹性模量 (E ratio, %) [Farhangi 2024, pp. 3-3]。
- **纤维几何与材料参数**：纤维直径 d (0.02–2.0 mm)、长度 l (6–60 mm)、纤维拉伸强度 fᵤ (600–2300 MPa 仅钢纤维) [Farhangi 2024, pp. 3-5]。
- **温度**：T = 100–1200 ℃，是影响最大的控制因素 [Farhangi 2024, pp. 5-6]。
- **水胶比 (W/B)**：影响失效概率的重要参数，尤其是对于钢纤维混凝土 [Farhangi 2024, pp. 1-1]。
- **模型超参数**：隐含层神经元数（如 6, 15, 16, 18, 3, 7），算法随机分割比例 70/15/15 [Farhangi 2024, pp. 5-5]。

## Reusable Claims
1. **多层感知机可有效预测高温后 FRC 的相对力学性能，但需分纤维类型和力学性能分别建模**。证据：针对 SFRC 和 PFRC 的六个独立模型在测试集上 R 值介于 0.979 至 0.994，MSE 介于 2.35×10⁻⁴ 至 1.6×10⁻³，表明每个模型结构需定制化 [Farhangi 2024, pp. 5-6]。适用条件：数据集规模较小至中等，输入特征 8–9 个，LM 训练算法配合线性归一化。
2. **在预测高温后 FRC 力学性能时，温度是最重要的输入变量，其影响顺序高于纤维力学参数**。证据：全连接重要性分析显示温度对所有模型输出变化贡献最大，且聚丙烯纤维对温度变化的敏感度高于钢纤维 [Farhangi 2024, pp. 5-6]。限制：该结论来自特定数据集，未确认是否适用于其他温度范围或纤维类型。
3. **纤维含量大于 0.8% 及低水胶比（<0.4）的 FRC 高温实验数据严重不足，为文献明确指出的研究空白** [Farhangi 2024, pp. 3-5]。可被用于指导后续实验设计或领域综述的 gap statement。
4. **对于聚丙烯纤维混凝土，在温度低于 600 ℃ 且纤维含量较低时，纤维长度与残余抗压强度比呈近似线性正相关，可能源于长纤维对微裂纹的抑制作用**，但需注意该关系伴随着直径效应和大掺量下的孔隙率增加 [Farhangi 2024, pp. 6-8]。条件：需限定纤维直径不显著小于某一导致蒸气压过高开裂的阈值。

## Candidate Concepts
- [[fiber reinforced concrete (FRC)]]
- [[residual mechanical properties after fire]]
- [[high temperature concrete degradation]]
- [[artificial neural network (ANN) or MLP]]
- [[probabilistic failure analysis of concrete]]
- [[steel fiber reinforced concrete (SFRC)]]
- [[polypropylene fiber reinforced concrete (PFRC)]]
- [[Levenberg-Marquardt algorithm]]
- [[relative strength ratio]]

## Candidate Methods
- [[Multilayer Perceptron (MLP)]]
- [[Levenberg-Marquardt training]]
- [[Early stopping for overfitting prevention]]
- [[Linear normalization to [0,1]]]
- [[Feature importance analysis in neural networks]]
- [[Dataset division by fiber type and mechanical property]]
- [[Probabilistic modelling for concrete failure]]

## Connections To Other Work
索引片段提及了其他研究者使用不同机器学习模型解决 FRC 或普通混凝土相关问题的尝试：
- [[Jiao et al.]] 使用机器学习预测高性能纤维增强混凝土与普通混凝土间的剪切剥离强度 [Farhangi 2024, pp. 1-2]。
- [[Li et al.]] 利用 SVR 及其集成方法预测 FRC 抗压强度 [Farhangi 2024, pp. 1-2]。
- [[Chen et al.]] 提出深度学习模型（19 个输入）估计高温下 FRC 抗压强度，并与 Eurocode 2 进行对比 [Farhangi 2024, pp. 1-2]。
- [[Shafighfard et al.]] 采用堆叠式机器学习算法预测高温下钢纤维混凝土抗压强度，侧重准确度比较 [Farhangi 2024, pp. 1-2]。
以上工作表明，AI 预测 FRC 高温后性能是活跃领域，本研究在纤维类型覆盖、多目标输出（抗压、抗拉、弹性模量）及概率分析方面进行了扩展。

## Open Questions
1. 纤维含量大于 0.8% 且水胶比低于 0.4 的高温力学行为数据仍极度缺乏，AI 模型在缺乏数据区域的预测可靠性未经验证 [Farhangi 2024, pp. 3-5]。
2. 失效概率分析的具体方法（例如使用何种概率分布、极限状态函数）未在索引片段中披露，需要后续确认 [Farhangi 2024, pp. 1-1]。
3. 模型对更极端温度（>1200 ℃）或不同升降温速率的适用性尚未探讨。
4. 聚丙烯纤维直径低于某一阈值导致蒸气压力诱导微裂纹的具体阈值需要进一步定量 [Farhangi 2024, pp. 6-8]。
5. 模型对不同纤维类型（如玻璃、玄武岩纤维）的迁移能力未研究。

## Source Coverage
本页面基于该论文的 19 个索引片段构建，片段主要覆盖摘要、数据描述、方法架构、部分预测结果与泛化分析、概率结论总结。缺失内容包括：全文的详细讨论部分、完整结论段落、概率分析的具体模型细节、与实验对照的全面验证、以及所有图表的具体数据。因此，本页提供的信息偏向方法和核心发现，而深入的机制解释和验证可能不全。
