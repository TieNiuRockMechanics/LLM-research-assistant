---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2016-bonneau-impact-of-a-stochastic-sequential-initiation-of-fractures-on-the-spatial-correlatio"
title: "Impact of a Stochastic Sequential Initiation of Fractures on the Spatial Correlations and Connectivity of Discrete Fracture Networks."
status: "draft"
source_pdf: "data/papers/2016 - Impact of a stochastic sequential initiation of fractures on the spatial correlations and connectivity of discrete fracture networks.pdf"
collections:
citation: "Bonneau, François, et al. “Impact of a Stochastic Sequential Initiation of Fractures on the Spatial Correlations and Connectivity of Discrete Fracture Networks.” *Journal of Geophysical Research: Solid Earth*, vol. 121, 2016, pp. 5641–5658, doi:10.1002/2015JB012451."
indexed_texts: "14"
indexed_chars: "67365"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T19:59:52"
---

# Impact of a Stochastic Sequential Initiation of Fractures on the Spatial Correlations and Connectivity of Discrete Fracture Networks.

## One-line Summary
该研究提出一种顺序母-子泊松点过程来模拟离散裂缝网络，发现该过程能自然产生空间相关性，显著改变裂缝网络的连通性和逾渗阈值 [Bonneau 2016, pp. 1-1]。

## Research Question
如何将通过机械相互作用驱动的裂缝起裂顺序融入随机离散裂缝网络模拟，以及这种顺序起裂如何影响裂缝网络的空间相关性和连通性？[Bonneau 2016, pp. 1-1]

## Study Area / Data
本研究为基于数值模拟的理论和方法研究，未指定具体野外研究区。数据来源为计算机生成的合成离散裂缝网络 [Bonneau 2016, pp. 6-7]。模拟域为体积 90 × 90 × 90 m 的立方体，包含从均匀密度图生成的 10,000 条裂缝，裂缝迹长服从指数为 1.8、上下界为 1 至 30 m 的截断幂律分布 [Bonneau 2016, pp. 6-7]。

## Methods
- **顺序母-子泊松点过程**：在非均质泊松点过程的框架内，提出一种顺序模拟算法来生成裂缝中心点。该过程迭代进行，在每一序列中，根据已模拟裂缝周围的简化三维应力模型来调整裂缝成核概率：在裂缝尖端应力集中区概率增加，在应力阴影区概率降低 [Bonneau 2016, pp. 2-4]。
- **几何力学模型**：采用对称椭球体近似裂缝尖端的应力集中区和应力阴影区。椭球体的几何形状由相对于裂缝尺寸的缩放因子 αs、βs（阴影区）和 αp、βp（应力集中区）定义 [Bonneau 2016, pp. 2-4]。
- **相关维数计算**：使用相关维数 Dc 量化 DFN 的空间相关性，该维数基于裂缝中心点间的空间相关性函数 C2(r) 估算。该 Dc 的值为 3 表示完全无空间相关性（均匀泊松分布），小于 3 则表示存在聚类/相关性 [Bonneau 2016, pp. 5-7]。
- **连通性评估**：采用 E-type 图对一系列尺度下相关裂缝网络的连通性进行量化，并与经典泊松点过程生成的网络及文献结果进行对比 [Bonneau 2016, pp. 1-1, 7-9]。
- **敏感性分析**：研究输入参数对 DFN 空间相关性的影响，具体包括地质力学模型参数（应力集中区和阴影区相对范围 αp, βp, αs, βs）、强度因子（g, h）以及起裂序列数（s） [Bonneau 2016, pp. 9-11]。

## Key Findings
- **空间相关性的涌现**：顺序母-子泊松过程使裂缝围绕较大裂缝的尖端组织，从而产生空间相关系。相比经典泊松过程生成的网络，其相关维数 Dc 显著低于 3（例如，对于随机取向的裂缝网络，经典过程 Dc ≈ 3.00 ± 0.01，顺序过程 Dc ≈ 2.58 ± 0.09）[Bonneau 2016, pp. 6-7]。
- **参数 h 与 g 的影响**：空间相关性的强度主要由强度因子 h 控制，Dc 随 log h 增加而下降；强度因子 g 对 Dc 的影响很小。这一关系对裂缝取向分布的敏感性很低 [Bonneau 2016, pp. 11-12]。
- **起裂序列数的影响**：模拟序列数 s 会影响空间相关性。当序列数很少（如 s=1）时，会引入一种‘1/f 噪声’效应，导致 Dc 低于真实值。随着序列数增加，相关性逐渐显现并趋于稳定。在可能的计算成本下，s=250 是一个较好的折中方案 [Bonneau 2016, pp. 12-13，由片段逻辑推断]。
- **对连通性的影响**：空间相关性会影响特定尺度下的网络连通性和逾渗阈值。参数 h 会降低连通性，而参数 g 的影响很小 [Bonneau 2016, pp. 1-1，13，由片段逻辑推断]。
- **E-型图分析**：顺序过程在均质输入密度图下，产生的 E-型图（即平均裂缝密度图的标准差）比经典泊松过程更高，表明收敛更困难且存在聚类效应 [Bonneau 2016, pp. 7-9]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 顺序过程产生的随机取向 DFN 的平均相关维数 Dc 为 2.58 ± 0.09，而经典泊松过程为 3.00 ± 0.01 | Table 1 [Bonneau 2016, pp. 6-7] | 100 次实现，各含 10,000 条裂缝，迹长 1-30 m 幂律分布，域 90x90x90 m | Dc=3 表示无空间相关；值越低相关性越强 |
| Dc 主要随强度因子 h 变化，实验模型 Dc(h) ≈ −0.18 log h + 2.96 ± 0.09 | Equation (3) [Bonneau 2016, pp. 11-12] | g=10, 其他参数为默认值 | 模型拟合基于数值实验 |
| Dc 作为 g 的函数几乎为常数，实验模型 Dc(g) ≈ −0.03 log(g) + 2.81 ± 0.09 | Equation (4) [Bonneau 2016, pp. 11-12] | h=10, 其他参数为默认值 | 单组裂缝与随机取向结果相似 |
| 在均质密度图下，顺序过程的 E-型图标准差 (1.30 × 10⁻³ m⁻³) 高于经典泊松过程 (2.08 × 10⁻⁴ m⁻³) | 文本描述与图5 [Bonneau 2016, pp. 7-9] | 1,000 次实现，输入密度 1.37 × 10⁻² 中心 m⁻³ | 高标准差指示聚类和不均匀性 |

## Limitations
- **裂缝生长交互的忽略**：该方法忽略了裂缝生长过程中的交互作用以及生长过程中成核的裂缝，可能低估从老裂缝起裂的新裂缝数量，从而导致网络连通性被低估 [Bonneau 2016, pp. 4-6]。
- **应力模型的简化**：用于近似应力扰动的椭球体模型是简化的一阶模型，可能在某些局部不一致（如裂缝平行于主压应力方向时），但在缺乏远场应力信息时预期能在平均意义上模拟地质力学效应 [Bonneau 2016, pp. 2-4]。
- **‘1/f 噪声’效应**：当模拟序列数过少时（特别是 s=1），方法会引入“1/f 噪声”效应，导致相关维数 Dc 低于预期值，需要谨慎选择序列数以获得准确的相关性估计 [Bonneau 2016, pp. 12-13]。
- **假设各向同性阴影区**：当前应力阴影模型是各向同性的，这使得在分析参数 g 对方向性裂缝组的影响时，其结果与随机取向情况相似 [Bonneau 2016, pp. 11-12]。

## Assumptions / Conditions
- **远场应力未知**：在模拟 DFN 时，通常无法获得远场应力，因此本方法基于平均意义上的地质力学效应进行模拟 [Bonneau 2016, pp. 2-4]。
- **裂缝密度图已知**：模型假设可以获取一个先验的裂缝密度图 d(x,y,z)，该图可能来自应变分析 [Bonneau 2016, pp. 4-6]。
- **裂缝长度分布反映生长和合并过程**：模拟中采用指数为 1.8 的截断幂律分布来描述裂缝长度，这一假设与断裂生长和合并过程一致 [Bonneau 2016, pp. 6-7]。
- **各向同性分布**：用于计算空间相关性函数 C2(r) 的方法假设裂缝中心点分布是各向同性的，作者认为在从完整岩石和均匀取向分布开始的简单情况下，这是一个合理近似 [Bonneau 2016, pp. 6-7]。

## Key Variables / Parameters
| Variable | Description | Source |
|---|---|---|
| Dc | 关联维数，量化裂缝中心点空间聚类程度 (Dc=3 表示完全随机) | [Bonneau 2016, pp. 5-7] |
| αp, βp | 控制裂缝尖端应力集中椭球区相对于裂缝尺寸的缩放因子 | [Bonneau 2016, pp. 2-4] |
| αs, βs | 控制裂缝两侧应力阴影椭球区相对于裂缝尺寸的缩放因子 | [Bonneau 2016, pp. 2-4] |
| g | 应力集中区的强度因子，影响种子被接受的概率 | [Bonneau 2016, pp. 4-6] |
| h | 阴影区的强度因子，影响种子被拒绝的概率 | [Bonneau 2016, pp. 4-6] |
| s (或 p(s)) | 模拟序列数（或每序列模拟的裂缝百分比），控制顺序效应的时间分辨率 | [Bonneau 2016, pp. 9-11] |
| P(x,y,z) | 在位置 (x,y,z) 处，一个潜在种子被选择进行模拟并激活的概率 | [Bonneau 2016, pp. 4-6] |
| ```E-type``` | E-型图，用于评估局部裂缝密度均值及其方差，以衡量连通性 | [Bonneau 2016, pp. 7-9] |
| a | 裂缝迹长（幂律分布） | [Bonneau 2016, pp. 6-7] |

## Reusable Claims
- **Claim 1**：在 DFN 模拟中，使用基于力学相互作用的顺序母-子泊松点过程，可使生成网络的关联维数 Dc 显著低于 3，表明空间相关性自然涌现。**条件**：模型采用简化的应力集中/阴影椭球体，并序贯更新种子选择概率。**证据**：在 100 次实现中，随机取向 DFN 的 Dc 从 3.00 降至 2.58 [Bonneau 2016, pp. 6-7]。**限制**：不适用于非脆性/非力学主导的裂缝机制，且依赖于输入参数。
- **Claim 2**：在该模型中，空间相关性的强度主要由阴影区强度因子 h 控制，表现为 Dc ≈ −0.18 log h + 2.96。应力集中区强度因子 g 对聚类程度的直接影响很小。**条件**：基于定义的椭球几何和强度因子在默认取值附近变化。**证据**：通过敏感性分析得出方程 (3) 和 (4) [Bonneau 2016, pp. 11-12]。**限制**：此定量关系仅针对所述的模拟设置和参数范围，外推需谨慎。
- **Claim 3**：在模拟中，裂缝起裂的序列数（s）是一个关键控制参数：过少的序列（特别是 s=1）会引入‘1/f 噪声’并产生虚假的低 Dc。足够的序列数才能揭示真实的、由力学作用产生的空间相关性。**条件**：模拟域和裂缝密度与文中一致。**证据**：比较了 s=1, 250, 1000 等情况下的 Dc 值，发现了收敛行为 [Bonneau 2016, pp. 12-13]。**限制**：最佳序列数可能随总裂缝数、域大小等变化。
- **Claim 4**：由这种顺序过程产生的空间相关 DFN，其连通性与经典泊松 DFN 不同，表现为在特定尺度上影响逾渗行为和连通性参数。**条件**：通过 E-型图和连通性指标比较了相关与非相关网络。**证据**：文中定量证实了空间相关性对逾渗阈值的影响 [Bonneau 2016, pp. 1-1, 7-13]。**限制**：未从片段中确认具体的逾渗阈值变化数值。

## Candidate Concepts
- [[Spatial correlation in DFN]]
- [[correlation dimension]]
- [[sequential parent-daughter Poisson point process]]
- [[fracture network connectivity]]
- [[percolation threshold of fracture networks]]
- [[E-type map]]
- [[fractal fracture networks]]
- [[Stress shadow effect in fracture propagation]]

## Candidate Methods
- [[Sequential Poisson point process simulation]]
- [[Correlation function analysis for point processes]]
- [[Box-counting fractal dimension]] (对比中提到)
- [[E-type estimation for density fluctuation]]
- [[Sensitivity analysis in DFN parameterization]]

## Connections To Other Work
- **经典泊松方法对比**：该方法直接针对经典均匀或非均质泊松点过程在 DFN 模拟中的不足，后者忽略了裂缝间的力学相互作用，导致空间相关性低 [Bonneau 2016, pp. 1-2]。
- **DFN 模拟改进**：研究是对现有改进 DFN 统计模型或融入力学交互效应方法（如 Josnin et al. 2002；Cladouhos and Marrett 1996；Davy et al. 2013 等）的补充，提出了一个基于顺序成核的新视角 [Bonneau 2016, pp. 1-2]。
- **自然裂缝网络特征**：研究结果与天然裂缝系统中观察到的“发育不良”和“发育良好”网络（Wu and Pollard 1995）或“不饱和”与“饱和”网络（Josnin et al. 2002）的概念具有可比性，因为该过程能自然再现这些状态及其过渡 [Bonneau 2016, pp. 4-6]。
- **逾渗与连通性**：研究定量证实了早期发现（如 Odling and Webman 1991），即尽管长度和取向统计相同，但由不同过程产生的网络其全局连通性和渗透性可能存在偏差 [Bonneau 2016, pp. 1-2]。

## Open Questions
- 如何将裂缝生长过程中的相互作用以及生长过程中成核的裂缝整合到此模型中，以纠正可能的连通性低估？[Bonneau 2016, pp. 4-6]
- 如何在缺乏直接物理测量的情况下，将模型参数 (α, β, g, h) 与真实的岩石力学参数建立统计或直接关系？[Bonneau 2016, pp. 9-11]
- 对于非均质性极强的网络（如 Dc 低于 2.5），当前方法可能面临适用性边界，这需要进一步研究 [Bonneau 2016, pp. 12-13]。

## Source Coverage
本页面依据论文索引片段中的 14 个段落生成。覆盖范围包括摘要、引言、方法描述（第 2.1-2.3 节）、部分结果（E-type 分析）和参数敏感性分析（第 3.1-3.3 节）。片段主要集中于方法的数学描述、空间相关性（相关维数 Dc）的分析与敏感性，但对连通性的具体量化结果（如逾渗阈值变化、特定尺度连通性对比）和讨论/结论部分覆盖不足。因此，页面在方法学、空间相关性结论和参数影响方面较为详尽，但在连通性详细结果、与其他方法定量对比以及更广泛的讨论方面可能存在信息缺失。
