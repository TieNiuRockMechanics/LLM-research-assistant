---
type: "paper"
paper_id: "2016-bonneau-impact-of-a-stochastic-sequential-initiation-of-fractures-on-the-spatial-correlatio"
title: "Impact of a Stochastic Sequential Initiation of Fractures on the Spatial Correlations and Connectivity of Discrete Fracture Networks."
status: "draft"
source_pdf: "data/papers/2016 - Impact of a stochastic sequential initiation of fractures on the spatial correlations and connectivity of discrete fracture networks.pdf"
citation: "Bonneau, François, et al. \"Impact of a Stochastic Sequential Initiation of Fractures on the Spatial Correlations and Connectivity of Discrete Fracture Networks.\" *Journal of Geophysical Research: Solid Earth*, vol. 121, 2016, pp. 5641-5658, doi:10.1002/2015JB012451. Accessed 3 Aug. 2026."
indexed_texts: "14"
indexed_chars: "67365"
compiled_at: "2026-04-27T19:35:10"
---

# Impact of a Stochastic Sequential Initiation of Fractures on the Spatial Correlations and Connectivity of Discrete Fracture Networks.

## One-line Summary

本文提出了一种顺序母-子泊松点过程来生成离散裂缝网络（DFN），该方法通过考虑裂缝之间的机械相互作用模拟裂缝的顺序扩展，并定量证明由此产生的空间相关性会影响渗流阈值和特定尺度下的网络连通性 [Bonneau 2016, pp. 1-1]。

## Research Question

Stochastic DFN are classically simulated using stochastic point processes which neglect mechanical interactions between fractures and yield low spatial correlation [Bonneau 2016, pp. 1-1]. The research question is how to integrate physical and geological principles into stochastic DFN simulations, specifically by accounting for mechanical interactions that control fracture initiation, growth, and arrest, and what the impact of this integration is on emerging DFN properties such as network connectivity and fractal dimension [Bonneau 2016, pp. 1-1].

## Study Area / Data

该研究未使用特定的野外数据 [未从索引片段中确认]。该方法是基于合成模拟进行开发和验证的 [Bonneau 2016, pp. 6-7]。例如，DFN 被模拟在一个 90 × 90 × 90 m 的立方体体积内，包含 10,000 条裂缝，裂缝长度服从 1 至 30 m 的截断幂律分布，指数为 1.8 [Bonneau 2016, pp. 6-7]。

## Methods

1.  **顺序母-子泊松点过程 (Sequential Parent-Daughter Poisson Point Process):** 提出了一种模拟裂缝顺序扩展的过程，该过程基于一个简化的三维应力模型 [Bonneau 2016, pp. 2-4]。该模型使用两个椭球分别定義裂缝尖端周围的“应力集中区”和“阴影区”，以近似低阶应力扰动 [Bonneau 2016, pp. 2-4]。
2.  **裂缝扩展控制:** 裂缝被模拟为出现在较大裂缝末端的较小对象，通过计算每个位置的概率 $P(x,y,z)$ 来控制是否生成新裂缝，该概率取决于已模拟裂缝造成的应力集中和松弛 [Bonneau 2016, pp. 4-6]。
3.  **空间相关性的量化:** 使用相关维度 $D_c$ 来量化 DFN 的空间相关性，该方法是基于相关函数的估计，优于经典的盒计数方法 [Bonneau 2016, pp. 6-7]。
4.  **敏感性分析:** 对机械模型参数（应力集中区范围 $(\alpha_p, \beta_p)$、阴影区范围 $(\alpha_s, \beta_s)$、强度因子 $(g, h)$）和序列数量 $(s)$ 进行了敏感性研究，以量化输入参数与空间相关性之间的关系 [Bonneau 2016, pp. 9-11]。
5.  **E-type 地图:** 通过计算 1000 次 DFN 实现的平均值（E-type 地图）来量化和可视化模拟方法造成的偏差 [Bonneau 2016, pp. 7-9]。

## Key Findings

1.  **生成具有空间相关性的DFN:** 提出的顺序激活过程能够生成具有空间相关性的 DFN，其特征是相关维度 $D_c$ 小于 3 [Bonneau 2016, pp. 6-7]。
2.  **量化了空间相关性:** 对于单组、双组和随机取向的裂缝，经典泊松过程的平均 $D_c$ 约为 3.01，而顺序过程的平均 $D_c$ 分别在 2.47、2.55 和 2.58 左右 [Bonneau 2016, pp. 6-7]。
3.  **空间相关性对渗流和连通性的影响:** 该研究定量证实了空间相关性会影响渗流阈值和特定尺度下的网络连通性 [Bonneau 2016, pp. 1-1]。
4.  **敏感性分析结果-强度因子h:** 相关维度 $D_c$ 主要随强度因子 $h$（控制裂缝尖端阴影区）变化，拟合模型为 $D_c(h) \approx -0.18 \log h + 2.96 \pm 0.09$ [Bonneau 2016, pp. 11-12]。
5.  **敏感性分析结果-强度因子g:** 相关维度 $D_c$ 随强度因子 $g$（控制应力集中区）的变化很小，拟合模型为 $D_c(g) \approx -0.03 \log(g) + 2.81 \pm 0.09$ [Bonneau 2016, pp. 11-12]。该现象是因为 $g$ 主要吸引小裂缝至较大裂缝尖端，对裂缝中心间距的影响很小 [Bonneau 2016, pp. 11-12]。
6.  **裂缝取向影响:** 裂缝取向分布对 $D_c$ 与强度因子 $g$ 和 $h$ 的关系影响很小 [Bonneau 2016, pp. 11-12]。
7.  **模拟效率与序列数量:** 增加序列数量 $s$（即更精细地逐次模拟）会显著增加计算时间；将 10,000 条裂缝分为一次 10 条进行模拟，耗时约为 10 分钟，而一次性模拟仅需几秒 [Bonneau 2016, pp. 11-12]。

## Limitations

1.  该方法忽略了裂缝生长过程中的相互作用以及裂缝扩展时成核的裂缝，因此可能低估了从老裂缝中萌生的裂缝数量，进而可能导致低估网络的连通性 [Bonneau 2016, pp. 4-6]。
2.  该方法生成的 E-type 地图比经典 Poisson 过程具有更高的标准差，表明由于聚类效应，该方法收敛性更差 [Bonneau 2016, pp. 7-9]。
3.  方法中的参数（如应力集中区和阴影区的范围、强度因子）与岩石的力学参数有关，但尚未建立直接或统计关系 [Bonneau 2016, pp. 9-11]。
4.  经验性的相关维度 $D_c$ 与强度因子 $h$ 的关系式可能仅在特定参数范围（此处为 $g=10$）内有效 [Bonneau 2016, pp. 11-12]。

## Reusable Claims

1.  [[fracture clustering]] 降低了 DFN 的相关维度 $D_c$。
2.  裂缝间的机械相互作用是造成 DFN 空间相关性的一个关键因素。
3.  空间相关性显著影响 [[discrete fracture network]] (DFN) 的渗流阈值和连通性。
4.  模拟裂缝的顺序性（次数越多）会急剧增加计算成本，但能更精确地反映机械效应。

## Candidate Concepts

[[discrete fracture network (DFN)]]
[[fracture connectivity]]
[[percolation threshold]]
[[fractal dimension]]
[[spatial correlation]]
[[correlation dimension]]
[[parent-daughter process]]
[[fracture initiation and propagation]]
[[mechanical interaction]]
[[stress shadow]]

## Candidate Methods

[[Sequential Poisson point process]] / [[顺序母-子泊松点过程]]

## Open Questions

1.  如何将裂缝生长过程中的相互作用（包括同时成核）纳入此类顺序模拟框架，以解决对网络连通性的潜在低估？
2.  本文建立的模型参数（如应力集中区范围 $\alpha_p, \beta_p$ 和强度因子 $g, h$）能否、以及如何与具体的岩石力学性质和应力状态相关联？
3.  顺序过程导致的 E-type 地图的高标准差对实际预测的不确定性有多大影响，是否能通过改进算法来缓解？

## Source Coverage

所有结论均基于给定的索引片段 [Bonneau 2016, pp. 1-1] 至 [Bonneau 2016, pp. 11-12]。未从索引片段中确认研究区域的具体位置或野外数据，也未确认任何具体的野外案例应用。
