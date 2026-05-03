---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-ringel-stochastic-inversion-of-three-dimensional-discrete-fracture-network-structure-with-h"
title: "Stochastic Inversion of Three-Dimensional Discrete Fracture Network Structure With Hydraulic Tomography."
status: "draft"
source_pdf: "data/papers/2021 - Stochastic Inversion of Three-Dimensional Discrete Fracture Network Structure With Hydraulic Tomography.pdf"
collections:
citation: "Ringel, Lisa Maria, et al. \"Stochastic Inversion of Three-Dimensional Discrete Fracture Network Structure With Hydraulic Tomography.\" 2021."
indexed_texts: "16"
indexed_chars: "77553"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T03:18:22"
---

# Stochastic Inversion of Three-Dimensional Discrete Fracture Network Structure With Hydraulic Tomography.

## One-line Summary
本文提出了一种随机反演方法，利用水力层析成像数据推断三维离散裂隙网络的结构属性，并在基于瑞士Grimsel场地的合成测试案例中进行了验证 [Ringel 2021, pp. 1-1, 1-2]。

## Research Question
如何利用水力层析成像实验获取的多源压力响应数据，随机反演并推断出三维离散裂隙网络中裂隙的数量、位置、长度和水力特性 [Ringel 2021, pp. 1-2, 2-3]？

## Study Area / Data
研究基于合成测试案例，这些案例的设计参考了瑞士Grimsel场地（Grimsel site in Switzerland）的实际情况 [Ringel 2021, pp. 1-2]。数据来源于模拟的水力层析成像实验，在交叉井孔的不同注入位置依次制造恒定超压，并在相邻观测孔中记录由此诱发的瞬态压力扰动。为模拟测量、建模等误差，数据中加入了均值为零、标准差约为压力均值3%的正态分布噪声 [Ringel 2021, pp. 5-6]。

## Methods
该方法的核心原理是利用水力层析成像信息来推断分米尺度上裂隙岩体的三维结构特征 [Ringel 2021, pp. 2-3]。具体流程如下：

1.  **先验信息与概念模型**：基于对裂隙网络的基础地质认识，如沿钻孔或露头获得的裂隙产状、密度和可能的水力开度范围，为特定裂隙组预设其几何和水力参数的现实范围。确切的裂隙结构是未知的 [Ringel 2021, pp. 2-3]。
2.  **正演模型**：采用离散裂隙网络模型，通过开源网格生成器Gmsh将每条裂隙创建为在三维空间中任意定位的椭圆形壳单元，并使用布尔运算处理裂隙间的相交，形成一致离散化。随后，使用有限元方法模拟裂隙网络中的地下水流和压力响应 [Ringel 2021, pp. 3-4]。
3.  **随机反演算法**：通过可逆跳跃马尔可夫链蒙特卡洛方法同时拟合所有记录到的压力响应。该算法允许在反演过程中通过“模型间移动”，即随机插入或删除一条裂隙，来自动调整裂隙的数量和网络结构，无需预先已知裂隙数量。此外，“模型内移动”用于更新裂隙长度和水力开度等参数。新模型被接受的概率根据其后验概率决定，若其误差等于或小于当前模型则更可能被接受，但先验范围之外的模型会被直接拒绝 [Ringel 2021, pp. 2-3, 4-5, 5-6]。
4.  **测试案例设计**：为检验方法性能，设置了四个合成测试案例，包括基础案例、更新水力开度、增加额外注入点，以及定义第三个裂隙组 [Ringel 2021, pp. 6-7]。

## Key Findings
- 反演方法能够从水力层析成像数据中推断出三维离散裂隙网络的主要几何参数及其不确定性 [Ringel 2021, pp. 1-2]。
- 通过合成测试案例演示，该方法能够根据带有噪声的压力响应数据，定位那些构成主要流动路径的导水裂隙。测试案例中记录的压力信号（噪声处理后）的后验DFN模拟结果与测量信号的平均趋势基本吻合 [Ringel 2021, pp. 2-3, 6-7]。
- 可逆跳跃MCMC算法使裂隙的数量和结构能够在反演过程中被迭代调整，无需先验已知 [Ringel 2021, pp. 4-5]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 该方法用于合成测试案例，并基于瑞士Grimsel场地 | [Ringel 2021, pp. 1-2] | 合成案例 | 这是对方法进行演示和性能检验的虚拟现实基础。 |
| 合成测试案例的压力信号添加了标准差约为压力均值3%的正态分布噪声 | [Ringel 2021, pp. 5-6] | 用于模拟误差 | 噪声未掩盖信号的主要趋势。 |
| 裂隙在模型中近似为平面椭圆，具有均匀开度 | [Ringel 2021, pp. 8-9] | 裂隙形状假设 | 考虑到流体主要在交叉点间流动，这可避免考虑尖锐边缘，但未能体现潜在的非均匀开度或沟道化流。 |

## Limitations
- 该方法是基于合成数据进行开发和测试的，其在真实野外场地条件下的适用性有待检验 [Ringel 2021, pp. 5-6]。
- 反演依赖于给定的裂隙组概念模型，对于不符合预设裂隙组的复杂地质情况，评估存在局限 [Ringel 2021, pp. 2-3, 8-9]。
- 模型将裂隙近似为均匀开度的平面椭圆，无法处理潜在的非均匀开度或沿裂隙的沟道化流 [Ringel 2021, pp. 8-9]。
- 未从索引片段中确认该方法对密集裂隙网络或连通性极差网络的反演效果。

## Assumptions / Conditions
- **地质先验知识**：假设存在基本的地质认知，包括典型的裂隙产状、密度和可能的水力开度范围，以此构建裂隙组的先验分布 [Ringel 2021, pp. 2-3]。
- **水力层析实验条件**：假设钻孔中的封隔器系统能够完美隔离各注入点，且钻孔内的水力条件未被解析 [Ringel 2021, pp. 8-9]。
- **裂隙几何与水力特性**：裂隙形状被假设为平面椭圆，且水力开度在每条裂隙上是均匀的 [Ringel 2021, pp. 8-9]。大部分流体会在裂隙交叉点之间直接流动，因此无需考虑尖锐边缘 [Ringel 2021, pp. 8-9]。

## Key Variables / Parameters
反演算法估计的关键未知参数包括：
- **裂隙数量**：网络中裂隙的总数，通过反演动态调整 [Ringel 2021, pp. 4-5]。
- **裂隙中心坐标**：控制裂隙在三维研究区域内的位置 [Ringel 2021, pp. 8-9]。
- **裂隙长度**：指椭圆的长轴长度，其与短轴的比例由概念模型预先给定 [Ringel 2021, pp. 8-9]。
- **水力开度**：部分测试案例中被作为固定值，而在特定测试案例（如案例2）中被作为估计参数 [Ringel 2021, pp. 8-9]。

## Reusable Claims
- **Claim**: An iterative stochastic inversion methodology based on reversible jump MCMC can infer the number, locations, and parameters of fractures in a 3D DFN from hydraulic tomography data without requiring a priori specification of the network’s fracture count. [Ringel 2021, pp. 4-5, 2-3]
    - **Conditions**: This applies under the assumptions that fractures are plane ellipses with uniform aperture, and that their orientations and density ranges can be predefined based on a conceptual model from borehole or outcrop data.
    - **Evidence**: The method employs between-model moves (insert/delete fractures) to adjust model dimension, and within-model moves to update fracture length/aperture, demonstrated in synthetic test cases.
    - **Limitations**: The success depends on the predefined prior distributions for fracture sets, and has only been demonstrated for synthetic test cases.

- **Claim**: Approximating 3D fractures as planar ellipses and implementing them as shell elements in a FEM simulation can provide physically meaningful simulation of flow focusing and connectivity between intersections when the primary flow paths are between those intersections. [Ringel 2021, pp. 3-4, 8-9]
    - **Conditions**: Valid when most flow occurs directly between fracture intersections, using Gmsh for conforming discretization at intersections. Assumes uniform aperture across each fracture.
    - **Evidence**: The implementation was verified against 2D and 3D scenarios with analytical solutions, checking for convergence of numerical solutions and correct simulation of pressure diffusion.
    - **Limitations**: The simplification does not account for non-uniform apertures or channelized flow within a single fracture plane.

## Candidate Concepts
- [[Discrete Fracture Network (DFN)]]
- [[Hydraulic Tomography]]
- [[Fracture Network Inversion]]
- [[Stochastic Inversion]]
- [[Aquifer Characterization]]
- [[Grimsel Test Site]]

## Candidate Methods
- [[Reversible Jump Markov Chain Monte Carlo (rjMCMC)]]
- [[Finite Element Method (FEM) for Fractured Media]]
- [[Gmsh Mesh Generator]]
- [[Discrete Fracture Matrix Model]]
- [[Continuum Model for Fractured Media]]
- [[Tracer Tomography]]

## Connections To Other Work
- 本文引言提及离散裂隙网络模型与**连续介质模型**（continuum model）是模拟裂隙介质的两种主要方法。Hadgu et al. (2017) 通过基准测试比较了两种方法在有效渗透率和示踪剂穿透曲线方面的表现，认为DFN能更好表征结构的非均质性，前提是网络参数被良好刻画 [Ringel 2021, pp. 1-1]。
- 水力层析成像技术已被用于解决裂隙系统中的问题，其他层析成像技术如**示踪剂层析成像**、**应力层析成像**或**地球物理信号联合反演**也可用于裂隙系统表征 [Ringel 2021, pp. 1-2]。
- 正演模拟部分的有限元方法理论可参考 Reddy and Gartling (2010), Zienkiewicz et al. (2014) 和 Langtangen and Mardal (2019) 等文献 [Ringel 2021, pp. 3-4]。

## Open Questions
- 该方法在真实野外场地数据下的反演表现和稳健性如何，尚未从索引片段中确认。
- 如何处理与预设裂隙组概念模型严重不符的复杂或混合成因裂隙网络，未从索引片段中确认。
- 当裂隙网络中同时存在导水和阻滞流动的裂隙时，算法的分辨能力如何，未从索引片段中确认。

## Source Coverage
本页面基于论文 **16** 个索引片段生成。覆盖范围涵盖了引言、方法论、测试案例设置和部分结论。片段包含了论文的标题、作者、关键点和方法框架的详细描述。然而，片段主要来自论文的前半部分（pp. 1-9），缺失了详细的结果分析、讨论（包括对四个测试案例反演性能的具体量化评估）以及最终结论部分。因此，关于反演精度的量化指标、参数不确定性的详细评估以及方法的计算效率等关键信息可能缺失。
