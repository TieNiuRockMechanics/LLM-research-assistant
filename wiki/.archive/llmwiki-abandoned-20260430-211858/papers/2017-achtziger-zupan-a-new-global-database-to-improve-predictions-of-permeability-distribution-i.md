---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2017-achtziger-zupan-a-new-global-database-to-improve-predictions-of-permeability-distribution-i"
title: "A New Global Database to Improve Predictions of Permeability Distribution in Crystalline Rocks at Site Scale."
status: "draft"
source_pdf: "data/papers/2017 - A new global database to improve predictions of permeability distribution in crystalline rocks at site scale.pdf"
collections:
  - "2文章钻孔裂缝分形关系"
citation: "Achtziger-Zupan, P., et al. “A New Global Database to Improve Predictions of Permeability Distribution in Crystalline Rocks at Site Scale.” *Journal of Geophysical Research: Solid Earth*, 2017, doi:10.1002/2017JB014106. Accessed 2026."
indexed_texts: "27"
indexed_chars: "133770"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T20:21:36"
---

# A New Global Database to Improve Predictions of Permeability Distribution in Crystalline Rocks at Site Scale.

## One-line Summary
一个包含约29,000条原位渗透率的全球汇编数据库，用于量化并预测0-2000米深度范围内结晶岩渗透率随深度的分布规律 [Achtziger 2017, pp. 1-1]。

## Research Question
影响结晶岩场地尺度渗透率分布的关键技术与地质因素是什么，能否通过新建立的全球数据库与回归模型更准确地预测深部渗透率分布？[Achtziger 2017, pp. 1-3]。

## Study Area / Data
- **数据量**：汇编了来自221篇论文/报告的大约29,000条原位渗透率测量数据 [Achtziger 2017, pp. 1-1]。
- **地理覆盖**：来自26个国家共128个地区的结晶岩场地；集中在此类研究密集区域（如欧洲、日本）；其余地区数据较少（7%来自“其余地区”，3%来自世界其他地区） [Achtziger 2017, pp. 1-3]。
- **深度范围**：地下0至2000米 (mbgs) [Achtziger 2017, pp. 1-1]。
- **数据内容**：除渗透率或导水系数外，还提取了测试段长度与方向、孔径、估算影响半径和测试体积，以及来自102个文献的温度数据。另外从26个场地的32组跨孔试验中整理出单位出水量/单位贮水系数 (Specific yield/storage) 值 [Achtziger 2017, pp. 3-4]。所有原始单位 (m, ft, D, Lugeon等) 已全部转换为SI单位 [Achtziger 2017, pp. 3-4]。

## Methods
- **数据分离与分析**：按测量方法(6类)、测试段方向(3类)、测试段长度(3类)、测试岩体体积(18类)、岩性(11类)、地质省(6类)、峰值地面加速度(PGA, 4类)、局部应力状态(5类)将合并后的数据库划分为子数据集，并对不同深度区间的渗透率分布统计矩进行计算 [Achtziger 2017, pp. 7-8]。
- **回归分析**：使用对数-对数线性回归 (log(k) = A × log(z) + B) 揭示渗透率随深度的变化规律，并评估不同因素的回归系数与拟合优度 (R²) 及均方根误差 (RMSE) [Achtziger 2017, pp. 1-1][Achtziger 2017, pp. 8-9]。
- **k-means 聚类**：根据平均对数渗透率、方差、偏度在不同深度和子类下的欧氏距离进行聚类，以识别具有相似渗透率分布特征的地质环境 [Achtziger 2017, pp. 8-9]。
- **测试体积计算**：使用圆柱体体积公式 V = π Ri² l 计算测试岩体体积，其中 Ri 为影响半径，l 为测试段长度。对于承压含水层另有修正 [Achtziger 2017, pp. 4-5]。
- **参数换算**：渗透率 k 源自水力传导系数 K 按 k = K μ / (ρ g) 换算 [Achtziger 2017, pp. 3-4]。

## Key Findings
- **深度是最主要控制因素**：基于全部数据集，渗透率与深度的对数关系为 log(k) = -1.5 × log(z) - 16.3（k 单位为 m², z 为 km） [Achtziger 2017, pp. 1-1]。
- **渗透率方差恒定**：在任意深度范围内，渗透率的方差大约为2个数量级，作者推测这反映了脆性断裂带附近的渗透率变化 [Achtziger 2017, pp. 1-1]。
- **地质因素影响排序**：除深度外，最重要的地质控制因素是**当前地震构造活动性**（以峰值地面加速度PGA衡量）和**长期构造地质历史**（以地质省衡量）；岩性的影响相对次要 [Achtziger 2017, pp. 1-1][Achtziger 2017, pp. 1-3]。
- **尺度效应**：基于估算的测试岩体体积观察到明显的尺度依赖性，即“测试岩体体积每增加一个数量级，渗透率变化0.6个数量级” [Achtziger 2017, pp. 1-1]。
- **技术因素影响**：优先采样和水力各向异性对渗透率分布的影响可忽略不计 [Achtziger 2017, pp. 1-1]。
- **单位贮水/出水量趋势**：单位出水量和单位贮水系数与深度呈类似渗透率的下降趋势。拟合公式为 log(Sy/s) = -1.0 × log(z) - 6.0，即深度每增加一个数量级，该值约减小一个数量级 [Achtziger 2017, pp. 4-5]。
- **流态转换**：在浅部200米以浅，裂隙流在承压与非承压间变化；在大约600米以下，以承压裂隙流和基质流为主 [Achtziger 2017, pp. 1-1]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| log(k) = -1.5 × log(z) - 16.3 为全球结晶岩体0–2000 m深度渗透率的整体下降趋势 | [Achtziger 2017, pp. 1-1] | 基于全球29,000样本汇集；z以km为单位 | 此为全部数据的平均回归结果；不同地质省和方法有不同的回归系数 (见表3) [Achtziger 2017, pp. 8-9]。 |
| 渗透率方差在所有深度上大约为2个数量级 | [Achtziger 2017, pp. 1-1] | 基于整个数据集 | 假说归因于脆性断裂带的影响。 |
| 深度、当前地震构造活动性 (PGA) 及长期构造地质历史 (地质省) 是影响k分布的最重要地质因素 | [Achtziger 2017, pp. 1-1] | 回归分析与k-means聚类结果 | 岩性被确认为次要因素 [Achtziger 2017, pp. 1-1]。 |
| 每个数量级的测试岩体体积增加，会导致渗透率0.6个数量级的变化 | [Achtziger 2017, pp. 1-1] | 尺度依赖性通过计算有限样本的 V 值获得 | 依赖估算影响半径 Ri 的精确度 [Achtziger 2017, pp. 4-5][Achtziger 2017, pp. 7-8]。 |
| 单位出水量/贮水系数与深度关系：log(Sy/s) = -1.0 × log(z) - 6.0 | [Achtziger 2017, pp. 4-5] | 基于32个跨孔试验值；z以km为单位 | 1000 m处的典型Ss值约为 1E-6 [Achtziger 2017, pp. 4-5]。 |
| 600 m以深，主导流态为承压裂隙流和基质流 | [Achtziger 2017, pp. 1-1] | 统计观察结果 | 未从索引片段中确认具体的流态判定指标。 |
| 优先采样和水力各向异性对大规模渗透率分布影响可忽略 | [Achtziger 2017, pp. 1-1] | 通过对数据集的测试方法，方向等维度分析得出 | 未从索引片段中确认各向异性分析的具体细节。 |

## Limitations
- **数据分布不均**：数据并非全球均匀分布，主要集中在研究程度高的结晶岩区，在沉积岩盆地/伸展省等区域数据量较少，可能影响特定区域的预测精度 [Achtziger 2017, pp. 7-8]。
- **测试体积估算不准确**：由于报告中常缺失关键输入参数（如测试时间），导致约一半合并数据库的测试体积只能被估算 [Achtziger 2017, pp. 7-8]。
- **方法局限性**：大多数水力测试方法假定径向流进入均质各向同性含水层的解析解，这可能不完全适用于高度非均质的结晶岩断裂带 [Achtziger 2017, pp. 9-10]。
- 未从索引片段中确认作者是否提及数据库的时效性限制或潜在发表偏倚。

## Assumptions / Conditions
- **原假设**：通过回归分析和聚类提取的关键因素（深度、PGA、地质省）可预测结晶岩的场地尺度渗透率范围 [Achtziger 2017, pp. 1-1]。
- **渗透率推算条件**：假设水的动力粘度与密度为常数，且大多数井为垂直井，深度记录正确 [Achtziger 2017, pp. 3-4]。
- **体积计算模型**：假设测试影响范围为一个规则的圆柱体，并基于典型的承压/非承压含水层假设来修正影响半径 [Achtziger 2017, pp. 4-5]。
- **地质条件分类**：假设当前地震活动性可以用峰值地面加速度 (PGA) 完全表征，长期构造地质历史可被简单归类为六种地质省 [Achtziger 2017, pp. 7-8]。

## Key Variables / Parameters
- **因变量**：对数渗透率 log(k) (m²)，水力传导系数 K (m/s)
- **核心自变量**：正对数深度 log(z) (km)
- **回归系数**：斜率 A（在全部数据集中为-1.5），截距 B（在全部数据集中为-16.3）；R² 和 RMSE [Achtziger 2017, pp. 8-9]
- **控制因素分类标签**：峰值地面加速度 PGA (m/s²)、地质省类别、岩性类别、测试方法类型、测试段方向、log测试段长度 (m)、log估算测试岩体体积 (m³) [Achtziger 2017, pp. 7-8]
- **关键物性参数**：单位贮水系数/单位出水量 Sy/s [Achtziger 2017, pp. 4-5]
- **测试几何参数**：测试段长度 l (m)，影响半径 Ri (m)，计算测试体积 V (m³) [Achtziger 2017, pp. 4-5]

## Reusable Claims
1.  ===“在区域到场地尺度的结晶岩地下水数值模拟中，可使用通用经验公式 log(k) = -1.5 × log(z) - 16.3 来预测0-2000米深度范围内的一阶渗透率分布（此公式基于全球29,000个测量点的统计回归均值，预测的方差约为2个数量级）。”=== [Achtziger 2017, pp. 1-1]
2.  ===“对于需要耦合应力-渗流的结晶岩模拟，地质省和峰值地面加速度 (PGA) 应被作为渗透率空间分布的校正因子，因为它们是仅次于深度的最重要地质控制因素，其对渗透率的相对影响可通过论文中的回归系数进行量化，而仅依赖岩性进行分类预测效果次之。”=== [Achtziger 2017, pp. 1-1][Achtziger 2017, pp. 1-3]
3.  ===“当使用不同尺度（如钻孔压水试验 vs 区域模型网格）的渗透率数据时，必须考虑尺度效应，因为估算的测试岩体体积每增加一个数量级，平均渗透率可能会有0.6个数量级的改变（此关系基于有限数量、可计算影响半径的测试数据得出）。”=== [Achtziger 2017, pp. 1-1]
4.  ===“在结晶岩中，单位贮水系数的缺省值可依据关系式 log(Sy/s) = -1.0 × log(z) - 6.0 进行初步设定，其中1000米深度的典型值为 1E-6。此关系式来自大约32组跨孔水力试验。”=== [Achtziger 2017, pp. 4-5]

## Candidate Concepts
- [[crystalline rock permeability]]
- [[fracture flow]]
- [[depth-dependent permeability]]
- [[scale effect in hydrology]]
- [[specific storage]]
- [[geological province]]
- [[peak ground acceleration]]
- [[hydraulic anisotropy]]
- [[borehole hydraulic testing]]

## Candidate Methods
- [[k-means clustering]]
- [[log-log linear regression]]
- [[radial flow analytical solution]]
- [[cross-borehole hydraulic test]]
- [[borehole flowmeter logging]]
- [[Lugeon test]]
- [[packer test]]

## Connections To Other Work
- **与长期研究趋势对话**：作者指出了与Less research has been performed on...的连接，特别提到与大尺度地质过程（如接触/区域变质作用、地震构造活动性、地质历史）对渗透率影响的研究相对较少。本数据库旨在填补这一空白 [Achtziger 2017, pp. 1-3]。
- **从主题上与下列概念/方法相关联**：[[fracture database compilation]] 和 [[crustal permeability]] 以产生可与本数据库对比或整合的新发现；或与 [[thermo-hydro-mechanical (THM) modeling]] 和 [[seismotectonic controls on hydrology]] 等模型结合进行更综合的预测和验证。

## Open Questions
- 未从索引片段中确认作者对于回归模型预测性能的首次测试 (First tests...) 的结论和验证结果。
- 未从索引片段中确认导致渗透率在所有深度保持约2个数量级方差的物理机制是否经过测试，或仅为基于脆性断裂带的假说。
- 未从索引片段中确认该数据库如何具体处理不同应力状态 (NF, SS, TF等) 对渗透率分布的差异化影响。
- 未从索引片段中确认是否探讨了温度梯度异常区对渗透率深度-趋势关系的扰动。

## Source Coverage
本页基于论文《A New Global Database to Improve Predictions of Permeability Distribution in Crystalline Rocks at Site Scale》(Achtziger-Zupan 2017) 的27个索引片段生成。这些片段主要涵盖了摘要、支持信息、数据来源描述、分类与回归方法，以及综合结果表格。覆盖了核心研究问题、方法和关键发现，并对技术因素和地质因素的影响进行了初步评估。然而，关于研究区域地图细节、详尽的聚类图（如轮廓图）、预测模型测试部分 (First tests...)、详细的应力状态分析、以及对主要断层带和高渗透区的针对性讨论等重要信息未从当前索引片段中确认。
