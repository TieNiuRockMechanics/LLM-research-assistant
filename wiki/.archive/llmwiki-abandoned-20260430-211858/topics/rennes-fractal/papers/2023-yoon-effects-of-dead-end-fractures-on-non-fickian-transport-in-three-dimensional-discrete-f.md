---
type: "paper"
paper_id: "2023-yoon-effects-of-dead-end-fractures-on-non-fickian-transport-in-three-dimensional-discrete-f"
title: "Effects of Dead-End Fractures on Non-Fickian Transport in Three-Dimensional Discrete Fracture Networks."
status: "draft"
source_pdf: "data/papers/2023 - Effects of Dead-End Fractures on Non-Fickian Transport in Three-Dimensional Discrete Fracture Networks.pdf"
citation: "Yoon, Seonkyoo, et al. \"Effects of Dead-End Fractures on Non-Fickian Transport in Three-Dimensional Discrete Fracture Networks.\" *Journal of Geophysical Research: Solid Earth*, vol. 128, 2023."
indexed_texts: "17"
indexed_chars: "83282"
compiled_at: "2026-04-27T19:45:56"
---

# Effects of Dead-End Fractures on Non-Fickian Transport in Three-Dimensional Discrete Fracture Networks.

## One-line Summary

该研究揭示了死端裂缝在渗透阈值（percolation threshold）处最大化晚时间拖尾（late-time tailing），从而驱动强非Fickian输运，而超过渗透阈值后网络连通性增加则削弱拖尾 [Yoon 2023, pp. 1-1]。

## Research Question

该研究旨在系统量化死端裂缝（dead-end fractures）对三维离散裂缝网络中非Fickian输运（non-Fickian transport）的影响机制 [Yoon 2023, p. 1-1]。尽管死端裂缝已被识别为可能延迟溶质输运的低速区域，但其与非Fickian输运的直接关系此前一直不明确 [Yoon 2023, p. 1-1]。

## Study Area / Data

该研究没有使用特定的野外场地数据，而是合成生成了三维离散裂缝网络（3D discrete fracture networks, DFNs）模型 [Yoon 2023, pp. 1-1, 3-4]。

- 裂缝网络生成在边长为 `A` = 15 m的立方体域中 [Yoon 2023, pp. 3-4]。
- 系统生成大量具有不同裂缝长度分布指数（`α` = 2.0, 2.2, 2.4）和归一化裂缝密度（`ρ` = 0.5, 1, 4 等，相对于渗透阈值 `ρc`）的DFNs [Yoon 2023, pp. 1-1, 4-6]。
- 未考虑裂缝内孔径变化（aperture variations）以简化模拟，因为结果的结论限定于内裂缝变异性效应相对于网络结构控制可忽略的物理情景 [Yoon 2023, pp. 3-4]。
- 流动和输运模拟使用 dfnWorks 建模套件 [Yoon 2023, pp. 2-3]；流动模拟使用 PFLOTRAN 有限体积求解器 [Yoon 2023, pp. 7-8]。

## Methods

1.  **裂缝网络生成**：在 15 m 立方体域中生成具有不同裂缝密度和长度分布的 3D DFNs [Yoon 2023, pp. 3-4]。
2.  **基于图的死端裂缝识别（novel graph-based method）** [Yoon 2023, pp. 1-1]：
    - 将裂缝网络 `F` 转换为有向图 `G(V, E)`：每条裂缝 `fi` 映射为一个节点 `ui`，两条裂缝相交则对应节点间连边 `eij` [Yoon 2023, pp. 4-6]。
    - 将入口和出口边界分别转换为源节点 `s` 和目标节点 `t` [Yoon 2023, pp. 4-6]。
    - 提出新的定义：通过寻找图中所有不含源和目标节点的双连通分量，这些分量对应的裂缝即为死端裂缝 [Yoon 2023, pp. 6-7]。
3.  **流动与输运模拟**：
    - 施加 1 MPa 压差边界条件（沿 x 轴），其他面为无流边界，假设不可压缩流 [Yoon 2023, pp. 7-8]。
    - 通过求解压力场，重构裂缝网内的欧拉速度场 `u(x)` [Yoon 2023, pp. 7-8]。
    - 模拟溶质粒子输运时仅考虑平流过程（advection），不考虑分子扩散或基质扩散滞留 [Yoon 2023, pp. 7-8]。
4.  **非Fickian输运量化**：通过对首次通过时间分布（FPTDs）的95%至99.99%分位数范围进行线性回归，估算尾部斜率 [Yoon 2023, pp. 8-10]。

## Key Findings

- 死端裂缝对溶质停留时间的影响在临界渗透密度（`ρ ≈ 1`）处最大化，导致强烈的晚时间拖尾（late-time tailing） [Yoon 2023, pp. 1-1, 8-10]。
- 随着裂缝密度超过渗透阈值，网络连通性增加，死端裂缝数量减少，导致晚时间拖尾程度降低，输运向Fickian行为过渡 [Yoon 2023, pp. 1-1, 8-10]。
- 死端裂缝的密度被证明是预测非Fickian输运的良好指标 [Yoon 2023, pp. 1-1]。
- 当归一化裂缝密度 `ρ ≤ 2` 时，FPTD尾部斜率小于3，表现出非Fickian行为；当 `ρ > 2` 时，尾部斜率显著下降，进入Fickian输运区 [Yoon 2023, pp. 8-10]。
- FPTD的方差随裂缝密度增加而显著降低，表明更高裂缝密度限制了到达时间的变异性 [Yoon 2023, pp. 8-10]。

## Limitations

- 裂缝网络生成未使用地质力学模型（geomechanical models），这超出了该研究的范围 [Yoon 2023, pp. 2-3]。
- 模拟中排除了裂缝内孔径变化（aperture variations），其有效性受限于裂缝粗糙度方差低且相关长度短的物理情景 [Yoon 2023, pp. 3-4]。
- 未考虑裂缝-基质相互作用（fracture-matrix interactions）、分子扩散、基质扩散或吸附引起的滞留效应 [Yoon 2023, pp. 7-8]。该研究仅聚焦于平流过程 [Yoon 2023, pp. 7-8]。
- 模拟网络是半通用（semi-generic）的，其结果和结论无法直接适用于具有详细物质属性的特定岩层 [Yoon 2023, pp. 3-4]。

## Reusable Claims

- 死端裂缝密度是预测非Fickian输运的良好指标 [Yoon 2023, p. 1-1]。
- 在渗透阈值（percolation threshold）处，晚时间拖尾（late-time tailing）效应达到最大化 [Yoon 2023, pp. 1-1, 8-10]。
- 当裂缝密度超过渗透阈值时，网络连通性增加，死端裂缝减少，进而削弱非Fickian输运 [Yoon 2023, pp. 1-1, 8-10]。
- 基于图的拓扑方法是识别裂缝网络中死端裂缝的有效手段，特别是通过排除不含源-目标的[[biconnected component]] [Yoon 2023, pp. 6-7]。
- 在平流主导、裂缝内变异性可忽略的简单半通用DFN模型中，网络结构是控制非Fickian输运的关键因素 [Yoon 2023, pp. 3-4]。

## Candidate Concepts

- [[fracture reservoir]]
- [[dead-end fracture]]
- [[non-Fickian transport]]
- [[discrete fracture network]]
- [[percolation threshold]]
- [[late-time tailing]]
- [[graph theory]]
- [[first passage time distribution]]
- [[advective transport]]
- [[flow channelization]]

## Candidate Methods

- [[graph-based dead-end fracture identification]]
- [[dfnWorks]] 工作流
- [[PFLOTRAN]] 有限体积流动模拟
- [[FPTD tail slope fitting]]（在95%-99.99%分位数范围拟合线性回归）

## Open Questions

- 对于更接近自然场景、包含孔径异质性和基质相互作用的DFN，死端裂缝对非Fickian输运的控制作用是否会减弱或改变？未从索引片段中确认。
- 尾部斜率随裂缝密度变化的具体物理机制是什么？为何在 `ρ=2` 附近存在从非Fickian到Fickian的显著转变？未从索引片段中确认。
- 该基于图的方法能否扩展到识别不同几何形状（如弯曲或非平面死端）的死端裂缝？未从索引片段中确认。

## Source Coverage

- [Yoon 2023, p. 1-1]
- [Yoon 2023, p. 1-2]
- [Yoon 2023, p. 2-3]
- [Yoon 2023, p. 3-4]
- [Yoon 2023, p. 4-6]
- [Yoon 2023, p. 6-7]
- [Yoon 2023, p. 7-8]
- [Yoon 2023, p. 8-10]
