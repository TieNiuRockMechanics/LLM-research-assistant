---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2010-bunger-stochastic-analysis-of-core-discing-for-estimation-of-in-situ-stress"
title: "Stochastic Analysis of Core Discing for Estimation of In Situ Stress."
status: "draft"
source_pdf: "data/papers/2010 - Stochastic Analysis of Core Discing for Estimation of In Situ Stress.pdf"
collections:
  - "zotero new"
citation: "Bunger, Andrew P. \"Stochastic Analysis of Core Discing for Estimation of In Situ Stress.\" *Rock Mechanics and Rock Engineering*, vol. 43, 2010, pp. 275–286. DOI: 10.1007/s00603-009-0051-3."
indexed_texts: "11"
indexed_chars: "53002"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T18:02:26"
---

# Stochastic Analysis of Core Discing for Estimation of In Situ Stress.

## One-line Summary
本文提出一种基于整个盘长分布（而非典型盘厚）的随机方法，用于从金刚石钻探岩芯的盘裂现象估计原位应力状态 [Bunger 2010, pp. 1-2]。

## Research Question
当岩芯盘长分布高度非高斯、无法定义典型盘长时，如何可靠地利用盘裂数据估计原位应力？传统确定性方法因依赖高斯统计或人为排除较长碎片而受限 [Bunger 2010, pp. 2-3]。

## Study Area / Data
数据来自南澳大利亚奥林匹克丹矿附近的900m NQ2 金刚石钻探花岗岩岩芯（钻头外径75.7mm，岩芯直径50.2mm）。选取了8个40–70m长的区段（深度范围1,029–1,926 m），从中选择了覆盖各段40%以上的5–6m子段进行详细测量，共记录5,494个以圆柱状为主的碎片长度。未刻意区分天然与钻探诱发裂隙，声波井壁扫描显示绝大多数裂隙为钻探诱发（在最浅段，岩芯裂隙275条而扫描可见仅40条天然裂隙，天然裂隙占比<15%）。取样非完全随机，可能低估盘长分布的右尾 [Bunger 2010, pp. 3-4]。在一些区段，盘长分布呈现右尾主导，另一些则为钟形，无法定义单一典型长度 [Bunger 2010, pp. 4-5]。

## Methods
1. **盘裂准则**：采用 Matsuki et al. (2004) 提出的弹性数值准则。岩芯短柱长度 \(L_s\)，当满足  
   \(\sigma_x k_x(L_s/R) + \sigma_y k_y(L_s/R) + \sigma_z k_z(L_s/R) \geq \sigma_t\)（另受应力比约束 \(\sigma_y + \frac{19}{11}\sigma_z \geq \sigma_x \geq 17\sigma_y - 7\sigma_z\)）时，发生拉伸断裂形成盘裂。不预设 \(\sigma_x,\sigma_y,\sigma_z\) 为主应力 [Bunger 2010, pp. 5-5]。
2. **随机建模**：假设原位应力分量 \(\sigma_x,\sigma_y,\sigma_z\) 和岩石抗拉强度 \(\sigma_t\) 服从高斯分布（均值和标准差为待估参数）。通过蒙特卡洛模拟，随机抽取参数组合，利用准则判断在某给定标准化长度 \(L/R\) 下是否断裂，从而生成盘长概率密度分布。模拟结果显示，随平均轴向应力 \(\langle\sigma_z\rangle\) 增加，分布可从右尾主导转变为钟形 [Bunger 2010, pp. 6-7]。
3. **概率框架**：将盘裂准则抽象为集合 \(\hat{H}_{L_i}\)，计算盘长落入第 \(i\) 个区间的概率为  
   \(p(L_i) = p\!\left(\mathbf{y}_i \in \hat{H}_{L_i} \cap \mathbf{y}_j \in \hat{H}^C_{L_j}, \forall j < i\right)\)，其中 \(\mathbf{y}_i\) 为参数向量。这一离散化要求区间大小 \(\Delta L\) 远小于最大盘长但大于岩石非均质性尺度，且假设空间相关性在足够大范围内可忽略 [Bunger 2010, pp. 7-8]。
4. **拟合与估计**：通过优化 \(\{\text{std}(\sigma_t), \langle\sigma_x\rangle, \langle\sigma_y\rangle\}\) 使模拟与实测互补累积分布 \(F(L)\) 达到最佳视觉匹配。垂直应力均值由岩石密度测量给出 \(\langle\sigma_z\rangle = 0.0263h\) MPa (\(h\) 为深度，m)，抗拉强度均值由11次巴西劈裂试验确定为 \(\langle\sigma_t\rangle = 8.9\) MPa，应力标准差固定为0.3 MPa（远小于均值的5-10%），且不考虑弹塑性后验分析 [Bunger 2010, pp. 8-9]。

## Key Findings
- 南澳花岗岩岩芯的盘长分布呈现显著的双模式特征：有的区段为右尾主导（长盘多），有的为钟形，传统基于均值的分析方法受限 [Bunger 2010, pp. 4-5]。
- 随机模拟揭示，保持应力比和抗拉强度不变时，增大轴向应力 \(\langle\sigma_z\rangle\) 可使分布从右尾主导转变为钟形，说明原位参数的局部变化很可能是观测到的分布形态差异的根源 [Bunger 2010, pp. 6-7]。
- 提出的随机方法可利用整个盘长分布估计原位应力，即使分布高度非高斯也适用。初步拟合中，抗拉强度的标准差估计值（约1.3 MPa）与巴西试验结果一致 [Bunger 2010, pp. 8-9]。
- 弹性拉伸盘裂准则在特定条件下适用，但未进行弹塑性后验校核，断言该应力状态是否属于拉伸控制型盘裂需要单独验证 [Bunger 2010, pp. 5】。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 盘长分布形态从右尾主导向钟形转变可由 \(\langle\sigma_z\rangle\) 的增大引起 | [Bunger 2010, pp. 6-7] | 应力比固定，\(\langle\sigma_z\rangle\) 分别为28 MPa和60 MPa；变异系数固定（\(\text{std}(\sigma)=0.1\langle\sigma_z\rangle\)，\(\langle\sigma_t\rangle=9\) MPa，\(\text{std}(\sigma_t)=3\) MPa） | 未对其他应力比条件进行确认 |
| 利用互补累积分布 \(F(L)\) 作为拟合目标，成功优化了 \(\text{std}(\sigma_t),\langle\sigma_x\rangle,\langle\sigma_y\rangle\) | [Bunger 2010, pp. 8-9] | \(\langle\sigma_z\rangle\) 由密度估计，\(\langle\sigma_t\rangle=8.9\) MPa，应力标准差设为0.3 MPa | 抗拉强度标准差估计值与试验值接近，但拟合依赖于初始估计 |
| 南澳花岗岩岩芯中天然裂隙占比不足15%，大部分为钻探诱发 | [Bunger 2010, pp. 3-4] | 基于声波井壁扫描与岩芯观测对比 | 此上限估计，实际天然裂隙可能更少 |

## Limitations
- 未进行弹塑性后验分析，无法确认提出的应力状态不会导致剪切破坏或盘形严重偏离弹性预测 [Bunger 2010, pp. 5]。
- 数据采样非完全随机，可能导致对盘长分布右尾的低估 [Bunger 2010, pp. 4]。
- 当前方法仅针对拉伸型盘裂，若存在剪切引发的盘裂则不适用 [Bunger 2010, pp. 5]。
- 参数估计依赖于垂直应力的先验估计（由密度给出）和抗拉强度均值的试验结果，应力变异性被忽略，这可能影响结果的可推广性 [Bunger 2010, pp. 8-9]。
- 盘长准则中的数值系数仅针对特定钻头几何和材料弹性假设，通用性未从索引片段中确认。

## Assumptions / Conditions
- 盘裂由弹性最大拉伸应力控制，断裂发生在满足不等式(1)和约束(2)的瞬间 [Bunger 2010, pp. 5]。
- 应力分量和抗拉强度均可视为服从高斯分布，且抗拉强度的变异性远大于应力的变异性（本文中应力标准差设为0.3 MPa） [Bunger 2010, pp. 8-9]。
- 在足够大的岩芯段内，参数的空间相关性可忽略，使得整体分布可作为独立抽样处理 [Bunger 2010, pp. 7]。
- 盘裂准则中无需假设 \(\sigma_x,\sigma_y,\sigma_z\) 为主应力，仅受应力比约束 [Bunger 2010, pp. 5]。
- 岩芯碎片均被当作“盘”，但实际包含长度可达数百毫米的碎片，未区分形状或断裂模式（尽管绝大多数呈圆柱/盘状） [Bunger 2010, pp. 3-4]。

## Key Variables / Parameters
- \(\sigma_x, \sigma_y, \sigma_z\)：原位应力分量（可能非主应力），为随机变量，具有均值 \(\langle\sigma\rangle\) 和标准差 \(\text{std}(\sigma)\) [Bunger 2010, pp. 5-6]。
- \(\sigma_t\)：岩石抗拉强度，随机变量，均值 \(\langle\sigma_t\rangle=8.9\) MPa（巴西试验确定），标准差 \(\text{std}(\sigma_t)\) 待估 [Bunger 2010, pp. 8-9]。
- \(L\)、\(L/R\)：盘长及其与岩芯半径比 [Bunger 2010, pp. 5]。
- \(k_x, k_y, k_z\)：与 \(L_s/R\) 有关的数值系数，来自 Matsuki et al. (2004) [Bunger 2010, pp. 5]。
- \(p(L)\)、\(F(L)\)：盘长概率密度与互补累积概率，作为拟合目标 [Bunger 2010, pp. 8]。
- \(\text{std}(\sigma)=0.3\) MPa：应力分量标准差，视为小值固定 [Bunger 2010, pp. 9]。

## Reusable Claims
- **Claim**：当盘长分布为非高斯（如右偏或双峰）时，通过随机建模直接拟合整个分布的概率密度或互补累积分布，可以估计原位应力的均值和标准差。适用条件：有大量碎片长度数据，且能给出合理的先验（如垂直应力梯度和抗拉强度均值） [Bunger 2010, pp. 1-3, 8-9]。
- **Claim**：轴向应力水平 \(\langle\sigma_z\rangle\) 升高可使盘长分布形态从右尾主导转变为钟形，这一机制可用于解释同一钻孔内不同深度段分布特征的差异。条件：其他应力比和材料参数保持稳定 [Bunger 2010, pp. 6-7]。
- **Claim**：基于弹性拉应力准则的盘裂判据（如 Matsuki et al. 2004）可嵌入随机框架，无需假设应力分量为主应力，只需满足应力比约束。限制：仅适用于拉伸开裂为主的案例，不包含弹塑性效应 [Bunger 2010, pp. 5, 8]。
- **Claim**：岩芯盘裂数据中天然裂隙贡献极小（<15%），因此不必刻意区分天然与钻探诱发裂隙即可将全部碎片作为盘裂分析对象。证据来自声波扫描与岩芯对比 [Bunger 2010, pp. 3-4]。

## Candidate Concepts
- [[core discing]]
- [[in situ stress estimation]]
- [[stochastic model]]
- [[tensile failure criterion]]
- [[non-Gaussian distribution]]
- [[complementary cumulative distribution]]]
- [[drilling-induced fracture]]
- [[elastic finite element analysis of core]]
- [[Brazilian tensile strength test]]

## Candidate Methods
- [[Monte Carlo simulation]]
- [[probability density fitting]]
- [[data fitting using visual matching of CDF]]
- [[discing criterion by Matsuki et al. 2004]]
- [[elastic stress analysis of core stub]]
- [[inverse parameter estimation]] from distribution data

## Connections To Other Work
- 与 **Matsuki et al. (2004)** 紧密关联：直接使用其弹性数值盘裂准则及系数，将其从确定性应用扩展至随机框架 [Bunger 2010, pp. 2-3, 5]。
- 借鉴 **Corthésy and Leite (2008)** 的观点：盘裂由拉伸破坏主导，而非早期 Obert and Stephenson (1965) 提出的剪切机理；本文承认弹塑性后验的必要性但未实施 [Bunger 2010, pp. 5-6]。
- 区别于以往仅使用“薄盘”子集或假定高斯分布的工作（如 Ishida and Saito 1995）：本文直接处理全部碎片长度分布，无需人为排除较长的钻探诱发碎片 [Bunger 2010, pp. 2-3]。
- 未从索引片段中确认与其他具体原位应力估计方法的直接比较。

## Open Questions
- 如何将弹塑性盘裂准则融入该随机框架，以处理可能同时发生的剪切破坏或盘形偏差？[Bunger 2010, pp. 5]
- 应力分量的空间相关性与变异性的相对重要性如何？忽略空间相关性是否会在其他岩体中导致显著误差？[Bunger 2010, pp. 7]
- 该方法对非拉伸控制型盘裂（如高差应力下的剪切型盘裂）的适用性？[未从索引片段中确认]
- 取样偏差对分布右尾的影响如何系统纠正？[Bunger 2010, pp. 4]
- 除花岗岩外，该方法在其他岩性和应力环境中的可推广性尚未验证。

## Source Coverage
本页基于论文的11个索引片段生成，覆盖了摘要、引言与动机、数据采集详情、盘裂准则的引入、随机模拟示例、概率框架抽象以及初步拟合过程。对方法的数学抽象和实现细节有一定阐述，但缺少完整的拟合结果对比（仅有示意图）、敏感性分析、完整的参数估计量化以及最终估计的应力值。实验验证局限于单一地质背景与单一准则，对其他地区或准则的扩展讨论有限。
