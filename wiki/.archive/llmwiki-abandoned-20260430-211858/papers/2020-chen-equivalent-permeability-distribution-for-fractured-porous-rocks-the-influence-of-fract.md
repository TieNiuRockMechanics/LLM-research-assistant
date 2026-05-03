---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2020-chen-equivalent-permeability-distribution-for-fractured-porous-rocks-the-influence-of-fract"
title: "Equivalent Permeability Distribution for Fractured Porous Rocks: The Influence of Fracture Network Properties."
status: "draft"
source_pdf: "data/papers/2020 - Equivalent Permeability Distribution for Fractured Porous Rocks The Influence of Fracture Network Properties.pdf"
collections:
citation: "Chen, Tao. \"Equivalent Permeability Distribution for Fractured Porous Rocks: The Influence of Fracture Network Properties.\" *Geofluids*, vol. 2020, 2020, pp. 1-12, doi:10.1155/2020/6751349."
indexed_texts: "12"
indexed_chars: "56247"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T00:26:59"
---

# Equivalent Permeability Distribution for Fractured Porous Rocks: The Influence of Fracture Network Properties.

## One-line Summary
该研究基于多重边界升尺度方法，系统揭示了二维离散裂缝网络中裂缝几何参数（长度、数量/密度）如何控制等效渗透率张量的统计分布形态与均值变化 [Chen 2020, pp. 1-2]。

## Research Question
裂缝网络几何属性（特别是裂缝长度分布的下限 l_min 与裂缝数量 N）如何影响裂缝性多孔岩石等效渗透率张量分量（k_xx, k_yy, k_xy）的统计分布（直方图形状）与均值？[Chen 2020, pp. 1-2]

## Study Area / Data
- **模型域**: 二维 20 m × 20 m 的随机离散裂缝模型（Discrete Fracture Models），使用 ADFNE 代码随机生成 [Chen 2020, pp. 2-3]。
- **裂缝长度分布**: 服从幂律分布 n(l) = A l^{-a}，幂律指数 a 在 1.3 至 3.5 之间 [Chen 2020, pp. 2-3]。
- **裂缝几何参数变化**: 长度下界 l_min 从 4 m 依次增加至 6 m，8 m，10 m；裂缝数量 N 从 50 依次增加至 75，100，125。长度上界 l_max 固定为 40 m [Chen 2020, pp. 2-3]。
- **裂缝强度验证**: 面裂缝强度 P21（单位面积裂缝迹长）变化范围为 0.79 至 4.03 m/m²，与 Äspö 硬岩实验室的实测数据范围一致 [Chen 2020, pp. 8-9]。
- **实现次数**: 每组几何参数生成 10 次随机实现 [Chen 2020, pp. 8-9]。

## Methods
- **数值升尺度方法**: 采用先进的“多重边界方法”（Multiple Boundary Method），将离散裂缝模型升尺度为等效裂缝模型 [Chen 2020, pp. 1-2]。
- **流动边界条件**: 应用**线性边界条件**，因其能在一定程度上更真实地模拟地下流态，并且生成的等效渗透率与分析解匹配良好 [Chen 2020, pp. 3-4]。
- **流量与压力求解工具**: 利用 MATLAB Reservoir Simulation Toolbox (MRST) 进行网格划分和稳态流动问题求解 [Chen 2020, pp. 3-4]。
- **等效渗透率计算**: 基于达西定律的矩阵形式，通过对边界特定流量（q_x， q_y）和压力梯度（∇P_x， ∇P_y）的计算来求解，其中非对角线分量 k_xy 和 k_yx 通过平均得到一个对称的渗透率张量 [Chen 2020, pp. 3-4]。
- **网格块尺寸**: 网格块尺寸 lx 与 ly 均为 2 m，施加的压力梯度为 1 Pa/m [Chen 2020, pp. 3-4]。

## Key Findings
- **分布形态对比**: 等效渗透率张量的统计分布直方图呈现不同的形态。对角线分量 k_xx 和 k_yy 的直方图从类似幂律分布向类似对数正态分布转变；非对角线分量 k_xy 呈类似正态分布，中心值在 0 m² 附近 [Chen 2020, pp. 4-6]。
- **几何参数的影响**: 当裂缝长度下限 l_min 较小的条件下（例如4 m， N=50），k_xx 和 k_yy 的分布形态呈类幂律分布，这与三维连通性差的离散裂缝模型结果相似，其主要原因是大量网格块内的裂缝未穿透或低于逾渗阈值，渗透率由基岩控制 [Chen 2020, pp. 4-6]。
- **均值变化**: 对角线等效渗透率张量分量（k'xx 和 k'yy）的均值随无量纲裂缝密度 ρ 的增加而线性增长 [Chen 2020, pp. 6-8]。
- **空间分布**: k_xx, k_yy 和 k_xy 的空间分布彼此不同，主要受裂缝几何形态控制 [Chen 2020, pp. 9-10]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 对角线分量 k_xx 和 k_yy 的直方图形状随裂缝长度和数量增加，从类幂律分布转变为类对数正态分布 | [Chen 2020, pp. 4-6] | 二维离散裂缝模型，基岩有孔隙和渗透率，裂缝服从长度幂律分布 | 类幂律分布出现在连通性较差的模型中，由基岩渗透率主导 [Chen 2020, pp. 4-6]。 |
| 非对角线分量 k_xy 呈类似正态分布，中心值约为 0 m² | [Chen 2020, pp. 4-6] | 同上 | 分布范围随裂缝长度和数量增加而扩展 [Chen 2020, pp. 1-2]。 |
| 对角线等效渗透率张量的均值与无量纲裂缝密度 ρ 呈线性正相关 | [Chen 2020, pp. 6-8] | 变量包括 l_min 和 N 的不同组合 | 结果表明强相关性存在，具体相关系数未在片段中确认。 |
| 应用线**性边界条件**得到的等效渗透率与分析解匹配良好，而**无流动边界条件**或**单一边界法**会低估流量，从而得到偏小的等效渗透率 | [Chen 2020, pp. 3-4] | 数值模拟验证 | 这是选择线性边界条件作为本方法的核心原因。 |

## Limitations
- **二维与三维的差异**: 二维模型假设裂缝垂直延伸，但在真实情况中裂缝的倾角分布会影响连通性和等效渗透率。将二维结果关联至三维并非直接，取决于具体地质背景和裂缝几何属性 [Chen 2020, pp. 9-10]。
- **统计样本量**: 每组几何参数下仅生成 10 次随机实现，对于幂律长度分布的裂缝网络来说可能较少，但文中指出同一参数下的 10 次实现产生了相似的结果，表明统计结果相对稳定 [Chen 2020, pp. 8-9]。
- **二维域截断效应**: 用于随机分布的裂缝网络的固定域（20 m × 20 m）存在“审查效应”（Censor effect），可能会低估真实裂缝长度，但对于幂律长度分布而言，这通常不是一个严重问题 [Chen 2020, pp. 2-3]。

## Assumptions / Conditions
- **裂缝长度分布**: 假设天然裂缝系统的裂缝长度服从幂律分布，幂律指数 a 在 1.3 至 3.5 之间 [Chen 2020, pp. 2-3]。
- **基岩渗透性**: 模型为离散裂缝模型，包含岩石基体具有孔隙度和渗透率，流动可以发生在不连通的裂缝之间 [Chen 2020, pp. 2-2]。
- **裂缝几何简化**: 二维离散裂缝模型中，裂缝被假设为垂直延伸 [Chen 2020, pp. 9-10]。
- **边界条件**: 采用线性边界条件进行升尺度计算，因为它更能代表真实的地下流动状态 [Chen 2020, pp. 3-4]。
- **域尺寸和几何参数的妥协**: 采用的固定域大小（20 m × 20 m）是权衡了获取野外尺度裂缝几何数据的可行性与计算代价的结果 [Chen 2020, pp. 8-9]。

## Key Variables / Parameters
- **k_xx， k_yy**: 等效渗透率对角张量分量 [Chen 2020, pp. 1-2]。
- **k_xy**: 等效渗透率非对角张量分量 [Chen 2020, pp. 1-2]。
- **l**: 裂缝长度 [Chen 2020, pp. 2-3]。
- **l_min, l_max**: 幂律长度分布的下界和上界。l_min 分别取值 4, 6, 8, 10 m；l_max 固定为 40 m。 [Chen 2020, pp. 2-3]。
- **a**: 裂缝长度幂律分布指数 [Chen 2020, pp. 2-3]。
- **N**: 裂缝数量，分别取值 50, 75, 100, 125。 [Chen 2020, pp. 2-3]。
- **P21**: 面裂缝强度（单位面积的裂缝迹线长度），在模型中范围为 0.79 到 4.03 m/m²。 [Chen 2020, pp. 8-9]。
- **ρ**: 无量纲裂缝密度，用于关联等效渗透率均值与标准差。 [Chen 2020, pp. 6-8]。

## Reusable Claims
- **Claim 1**: 对于二维裂缝性多孔介质，当裂缝几何参数（如 l_min 和 N）较小时，等效渗透率对角线分量 k_xx 与 k_yy 的统计分布直方图倾向于呈类幂律分布，这种形态特征源于大部分区域的渗透率由未达到逾渗阈值的基岩所主导。 [Chen 2020, pp. 4-6] [条件：二维模型，裂缝服从幂律长度分布，基岩具有渗透性]
- **Claim 2**: 应用基于线性边界条件的多重边界升尺度方法，可以获得与分析解良好匹配的等效渗透率，而基于无流动边界条件或单一边界法的升尺度会导致等效渗透率被低估。 [Chen 2020, pp. 3-4] [条件：使用数值方法升尺度离散裂缝模型时]。
- **Claim 3**: 二维离散裂缝模型的等效渗透率对角线分量（k_xx, k_yy）的均值与无量纲裂缝密度（ρ）之间存在线性正相关关系。 [Chen 2020, pp. 6-8] [限制：结论基于特定范围的 P21 (0.79-4.03 m/m²) 和幂律分布假设]。

## Candidate Concepts
- [[fractured porous rock]]
- [[equivalent permeability tensor]]
- [[discrete fracture model]]
- [[power law length distribution]]
- [[multiple boundary method]]
- [[percolation threshold]]
- [[representative elementary volume (REV)]]
- [[fracture density]]

## Candidate Methods
- [[multiple boundary upscaling method]]
- [[numerical upscaling]]
- [[ADFNE code (for stochastic fracture generation)]]
- [[MRST (MATLAB Reservoir Simulation Toolbox)]]
- [[linear boundary condition method (for upscaling)]]

## Connections To Other Work
- **对比研究**: 该研究指出，其观察到的 l_min=4m， N=50 条件下 k_xx 和 k_yy 的类幂律分布形态，与此前研究中对三维连通性差的离散裂缝模型进行升尺度后的结果相似 [Chen 2020, pp. 4-6]。
- **方法论关联**: 文章引用了 Lang 等人 [39] 的工作，该研究基于压力和通量的体积平均法计算三维离散裂缝模型的等效渗透率，并指出二维剖面可能低估达三个数量级。本研究的二维结果向三维外推时需谨慎 [Chen 2020, pp. 2-2]。
- **方法论关联**: 文章引用了 de Dreuzy 等人 [37] 对二维离散裂缝网络（假设基岩不透水）中裂缝长度分布影响的分析，以及 Baghbanan 和 Jing [38] 对二维裂隙岩体等效渗透率和 REV 的研究 [Chen 2020, pp. 2-2]。本研究在此基础上，考虑了基岩渗透率的影响。

## Open Questions
- 在 l_min 和 N 变得更大时，k_xx 和 k_yy 的类对数正态分布是否会发生进一步的形态转变，其极限分布形式是什么？（未从索引片段中确认）。
- 文中提到的二维结果向三维进行“适当修正”的具体函数形式或修正系数是什么？（未从索引片段中确认）。
- 幂律指数 a 的变化对等效渗透率分布的具体影响是什么？本研究似乎固定了 a 值？（未从索引片段中确认）。

## Source Coverage
本页内容基于论文《Equivalent Permeability Distribution for Fractured Porous Rocks: The Influence of Fracture Network Properties》所提供的12个索引片段 [Chen 2020, pp. 1-10]。片段覆盖了摘要、引言（部分）、模型建立、数值升尺度方法描述、核心结果（分布形态、均值变化）以及讨论和结论部分。由于索引片段的非连续性，引言中更完整的文献综述、结果中部分统计数据细节、讨论中关于三维模型的更深入对比，以及完整结论部分可能有所缺失。
