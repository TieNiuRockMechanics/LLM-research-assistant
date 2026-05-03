---
type: "paper"
paper_id: "2021-ringel-stochastic-inversion-of-three-dimensional-discrete-fracture-network-structure-with-h"
title: "Stochastic Inversion of Three-Dimensional Discrete Fracture Network Structure with Hydraulic Tomography."
status: "draft"
source_pdf: "data/papers/2021 - Stochastic Inversion of Three-Dimensional Discrete Fracture Network Structure With Hydraulic Tomography.pdf"
citation: "Ringel, Lisa Maria, et al. “Stochastic Inversion of Three-Dimensional Discrete Fracture Network Structure with Hydraulic Tomography.” *Water Resources Research*, vol. 57, no. 8, 2021, e2020WR029382."
indexed_texts: "16"
indexed_chars: "77553"
compiled_at: "2026-04-27T19:44:18"
---

# Stochastic Inversion of Three-Dimensional Discrete Fracture Network Structure with Hydraulic Tomography.

## One-line Summary

该研究提出一种基于水力层析成像数据的随机反演方法，通过可逆跳跃马尔可夫链蒙特卡洛（rjMCMC）同时推断三维离散裂缝网络（DFN）的裂缝数量、位置、长度及水力孔径，并在瑞士Grimsel场的合成测试案例中验证了其可行性 [Ringel 2021, pp. 1-2]。

## Research Question

如何利用水力层析成像实验记录的多压力信号，以最小的先验假设（仅依赖裂缝组概念模型）推断低渗透基岩中三维DFN的结构特征（裂缝数量、位置、长度、孔径）及其不确定性？[Ringel 2021, pp. 2-3]

## Study Area / Data

该研究基于瑞士Grimsel场的概念模型设计了四个合成测试案例 [Ringel 2021, pp. 1-2]。每个案例中，水力层析成像实验通过在不同跨井注入位置依次创建恒定超压，并在相邻观测井接收点记录瞬态压力扰动。数据添加了约均值压力3%标准差的正态分布噪声以模拟测量误差 [Ringel 2021, pp. 5-6]。四种测试案例分别考核：基础案例（案例1）、水力孔径反演（案例2）、增加注入点（案例3）、引入第三裂缝组（案例4）[Ringel 2021, pp. 6-8]。

## Methods

1.  正演模拟：采用有限元法（FEM）求解压力扩散方程，使用开源网格生成器 Gmsh 实现裂交叉处的共形离散，裂缝以壳单元（shell elements）简化为二维椭圆平面 [Ringel 2021, pp. 3-4]。
2.  反演算法：应用可逆跳跃MCMC（rjMCMC）框架 [Ringel 2021, pp. 4-5]。在每次迭代中：
    *   **模型间移动**：随机插入或删除一条裂缝，允许裂缝数量作为未知参数自适应调整 [Ringel 2021, pp. 4-5]。
    *   **模型内移动**：更新已有裂缝的参数（中心坐标、长度、孔径），以提高采样效率 [Ringel 2021, pp. 5-6]。
3.  参数设定：基于先验地质知识定义裂缝组方向、密度及水力孔径范围，采用均匀先验分布；裂缝形状假设为椭圆，均匀孔径；钻孔内水力条件未明确解析 [Ringel 2021, pp. 8-9]。

## Key Findings

*   反演方法能够在无需预设裂缝数量的前提下，成功推断三维DFN的主要几何参数（裂缝位置、长度）及其后验不确定性 [Ringel 2021, pp. 1-2]。
*   基础案例（案例1）中，反演后的DFN后验实现模拟的压力信号与测量数据（含噪声）的均值一致 [Ringel 2021, pp. 6-8]。
*   案例2表明，在适当先验边界内，反演算法能够估计水力孔径 [Ringel 2021, pp. 8-9]。
*   案例3（增加一个与钻孔相连的额外注入点）和案例4（引入第三裂缝组）验证了该方法对更多约束条件及更复杂裂缝网络的适应性 [Ringel 2021, pp. 6-8]。
*   初始阶段的MCMC样本因裂缝与钻孔连接不佳而具有高拟合误差，随后逐渐收敛至后验分布 [Ringel 2021, pp. 8-9]。

## Limitations

*   裂缝形状简化为均匀孔径的椭圆，未考虑非均匀孔径或可能的通道流效应 [Ringel 2021, pp. 8-9]。
*   未明确解析钻孔内的水力条件，假设封隔器可完美隔离注入点 [Ringel 2021, pp. 8-9]。
*   反演性能高度依赖先验概念模型（裂缝组假设）的准确性；先验偏差可能导致误差 [Ringel 2021, pp. 2-3]。
*   所有测试均为合成案例，实际现场应用中数据噪声、模型结构误差和概念不确定性可能更大；计算效率未从索引片段确认。
*   方法仅处理单一井段中的水压响应，未整合其他类型数据（如示踪剂或地球物理信号）[Ringel 2021, pp. 2-3]。

## Reusable Claims

1.  利用rjMCMC进行DFN反演，可以在不预设裂缝数量的情况下推断结构参数及其不确定性 [Ringel 2021, pp. 4-5]。
2.  水力层析成像的多井压力信号能够约束三维DFN的主要几何特征，但需足够多的注入-接收组合以减少非唯一性 [Ringel 2021, pp. 2-3]。
3.  裂缝长度和水力孔径的更新（模型内移动）可提高rjMCMC采样效率，加快收敛 [Ringel 2021, pp. 5-6]。
4.  在合成案例中，以约3%噪声水平添加的测量误差不影响主要信号趋势，反演仍可恢复主要结构 [Ringel 2021, pp. 5-6]。
5.  初始MCMC阶段的样本因钻孔-裂缝连接不佳而被拒绝，需数千到上万迭代才能获得合理后验样本（具体迭代次数未从索引片段确认）。

## Candidate Concepts

- [[discrete fracture network]] (DFN)
- [[hydraulic tomography]]
- [[reversible jump Markov chain Monte Carlo]] (rjMCMC)
- [[finite element method]] (FEM)
- [[conceptual model]]
- [[fracture set]]
- [[prior distribution]]
- [[likelihood function]]
- [[posterior distribution]]
- [[conforming discretization]]
- [[shell elements]]
- [[Gmsh]]

## Candidate Methods

- [[Reversible Jump MCMC]]
- [[Finite Element Method with conforming discretization]]
- [[Gmsh mesh generation]]
- [[Shell elements for fractures]]
- [[Between-model moves]] (insertion/deletion of fractures)
- [[Within-model moves]] (update fracture parameters)
- [[Synthetic test case framework for DFN inversion]]

## Open Questions

-   该方法在实际非合成场地（如Grimsel现场）中的反演效果如何？未从索引片段中确认。
-   如何扩展方法以处理非均匀裂缝孔径、通道流或更多复杂地质特征？未从索引片段中确认。
-   计算效率是否可以进一步提升以适用于更大规模的三维DFN反演？未从索引片段中确认。
-   是否可结合示踪剂层析成像或地球物理数据以减少反演的非唯一性？未从索引片段中确认。

## Source Coverage

本文基于Ringel et al. (2021) 的16个索引片段编写，覆盖了引言（pp. 1-2）、方法（正演FEM及反演rjMCMC，pp. 2-5）、合成测试案例设置（pp. 5-6）及部分结果与讨论（pp. 6-9）。片段未包含完整的结论部分、详细的收敛统计及敏感性分析表格。所有非平凡结论均标注了原始页码来源。
