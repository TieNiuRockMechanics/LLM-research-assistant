---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-huang-development-and-application-of-three-dimensional-discrete-fracture-network-modeling-a"
title: "Development and Application of Three-Dimensional Discrete Fracture Network Modeling Approach for Fluid Flow in Fractured Rock Masses."
status: "draft"
source_pdf: "data/papers/2021 - Development and application of three-dimensional discrete fracture network modeling approach for fluid flow in fractured rock masses.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Huang, Na, et al. \"Development and Application of Three-Dimensional Discrete Fracture Network Modeling Approach for Fluid Flow in Fractured Rock Masses.\" *Journal of Natural Gas Science and Engineering*, vol. 91, 2021, p. 103957."
indexed_texts: "21"
indexed_chars: "104157"
nonempty_source_blocks: "21"
compiled_source_blocks: "21"
compiled_source_chars: "100358"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.963526"
coverage_status: "full-index"
source_signature: "01800bf96df14de85b4405d6a81cd3ea3f425ea6"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T04:02:53"
---

# Development and Application of Three-Dimensional Discrete Fracture Network Modeling Approach for Fluid Flow in Fractured Rock Masses.

## One-line Summary

本文综述了三维离散裂隙网络（3D DFN）建模方法在模拟天然裂隙岩体流体流动中的发展与应用，重点探讨模型生成、离散化、流动计算及多相流扩展等关键问题。

## Research Question

天然裂隙岩体深处三维裂隙网络的几何与水力特性难以直接观测，如何开发和应用三维离散裂隙网络（DFN）模型以解决模型生成、离散化、流动计算，并处理复杂网络结构带来的挑战？本文旨在回顾3D DFN建模方法的最新进展，特别强调上述核心环节。

## Study Area / Data

本文为综述性文章，不涉及特定研究区。所依赖的数据和方法来源于前人大量现场测量、露头迹线分析以及对裂隙几何特征（长度、产状、开度等）的统计描述。文中指出，裂隙网络的几何特征只能通过统计建模获得，如使用蒙特卡洛方法生成符合特定概率分布的随机裂隙网络 [Huang 2021, pp. 2-3]。此外，引用的野外数据包括裂隙长度的幂律分布范围、分形维数估算（如 La Pointe (1988) 报告的3D裂隙系统分形维数2.4 – 2.7）等 [Huang 2021, pp. 5-6]。

## Methods

本文对3D DFN建模方法的全面回顾涵盖以下核心方法：

- **随机生成方法**：采用蒙特卡洛模拟，假设裂隙为圆盘、椭圆板或多边形，并将长度、位置、产状、开度视为服从特定分布的随机变量 [Huang 2021, pp. 2-3]。
- **连通性分析**：利用逾渗理论，通过逾渗参数p和阈值pc评价裂隙网络的连通性；相关表达式如de Dreuzy et al. (2000)给出的三维随机椭圆系统逾渗参数公式 [Huang 2021, pp. 4-5]。
- **分形与尺度分析**：借助分形几何和幂律模型描述裂隙网络的尺度不变特征；由2D迹线图分形维数推断3D分形维数 [Huang 2021, pp. 5-6]。
- **流动控制方程与数值计算**：
  - 控制方程：Navier-Stokes方程简化为立方定律和Reynolds方程，多数研究采用Reynolds方程模拟粗糙裂隙中的流动 [Huang 2021, pp. 6-7]。
  - 离散化方法：包括边界元法（BEM）、有限元法（FEM）、混合混合有限元、虚拟单元法（VEM）等，并区分完全一致网格、部分一致网格和非一致网格处理裂隙交线 [Huang 2021, pp. 7-8]。
- **多相流扩展**：评述了在离散裂隙‑基质介质中处理多相流的数值方法，如FEM叠加法、非连续Galerkin法等，重点关注裂隙与基质的相互作用 [Huang 2021, pp. 8-9]。

## Key Findings

- 与连续介质方法相比，3D DFN模型能够显式表征裂隙几何和连通性，从而更准确地预测裂隙岩体中的渗流 [Huang 2021, pp. 1-1][Huang 2021, pp. 6-6]。
- 二维DFN模型会严重低估三维实际渗透率 [Huang 2021, pp. 1-2]。
- 裂隙网络拓扑（由裂隙排列决定）和裂隙尺度非均质性（如开度变化）共同控制流动路径：拓扑提供第一级连通框架，而开度非均质性促使流体选择高传导通道 [Huang 2021, pp. 3-4][Huang 2021, pp. 8-8]。
- 裂隙长度与开度存在正相关关系时，相比于假设常数平均开度的模型，渗透率可增大1 – 2个数量级 [Huang 2021, pp. 3-4]。
- 对于大规模、复杂裂隙网络的离散化与流动计算，目前仍存在计算难题，已有研究尝试采用图简化、非一致网格等策略，但需平衡效率与精度 [Huang 2021, pp. 7-8]。
- 非线性流动在三维DFN中的研究极少，仅有个别工作通过耦合Forchheimer方程进行探索 [Huang 2021, pp. 8-9]。
- 3D打印技术被用于制造可控裂隙网络的物理模型，为验证数值方法提供了新途径 [Huang 2021, pp. 9-9]。

## Core Evidence Table

| Evidence (证据) | Source (来源) | Conditions (条件) | Notes (备注) |
|----------------|--------------|------------------|--------------|
| 2D DFN模型相比3D模型明显低估渗透率 | [Huang 2021, pp. 1-2] | 基于立体学分析；适用于粗糙裂隙网络 | 与Berkowitz和Adler (1998)等结果一致 |
| Reynolds方程相对于Navier‑Stokes方程，对粗糙度JRC = 0 – 2的裂隙，流量低估约5 – 15% | [Huang 2021, pp. 6-7] | 裂隙壁面平滑，流动为层流 | 引用Koyama et al. (2008) |
| 裂隙长度‑开度半相关或完全相关时，突破时间提前，渗透率增大 | [Huang 2021, pp. 3-4] | 基于三维DFN模拟 | 由Hyman et al. (2016)得出 |
| 当幂律指数a > D + 1时，连通性由大裂隙主导；a < D + 1时，由小裂隙主导 | [Huang 2021, pp. 5-5] | D为分形维数，适用于具有分形特征的裂隙网络 | 参考Darcel et al. (2003b) |
| 三维DFN的连通性在逾渗阈值附近被二维切面显著低估，该低估随密度增加而减小 | [Huang 2021, pp. 4-5] | 基于幂律长度分布的裂隙网络 | Lang et al. (2014)的结论 |
| 非一致网格方法（如扩展有限元）可在无需节点对齐的情况下处理裂隙交线，但需弱约束来保证水头连续和流量守恒 | [Huang 2021, pp. 7-8] | 使用PDE约束优化方法 | Berrone et al. (2014a,b)的工作 |

## Limitations

- 本文并非穷尽性综述，仅引用了有限文献 [Huang 2021, pp. 1-2]。
- 3D DFN模型在处理大量裂隙、复杂交切关系时，网格剖分和流动计算仍然难以实现，计算成本极高 [Huang 2021, pp. 7-8]。
- 多数研究采用Reynolds方程而非直接求解Navier‑Stokes方程，高流速条件下非线性效应被忽略 [Huang 2021, pp. 6-7]。
- 目前针对三维DFN中非线性流动的研究非常有限 [Huang 2021, pp. 8-9]。
- 实验室制备具有复杂裂隙网络的岩样十分困难，相关物理实验验证不足 [Huang 2021, pp. 9-9]。

## Assumptions / Conditions

- 裂隙形状常假设为圆盘、椭圆板或多边形，并假设裂隙面为平行平板 [Huang 2021, pp. 2-3]。
- 裂隙几何特征（长度、位置、产状、开度）常被假设为相互独立，服从某种概率分布（如幂律、对数正态、Fisher分布） [Huang 2021, pp. 2-3]。
- 流动控制方程主要基于立方定律和Reynolds方程，即假定裂隙内为层流、开度缓变，忽略惯性项 [Huang 2021, pp. 6-7]。
- 模型通常在稳态、定密度条件下求解 [Huang 2021, pp. 6-6]。
- 连通性分析依赖于逾渗理论，并假设裂隙位置随机或服从幂律长度分布 [Huang 2021, pp. 4-5]。
- 多相流模拟中需简化处理裂隙‑基质界面的饱和度不连续性 [Huang 2021, pp. 8-8]。

## Key Variables / Parameters

- **裂隙长度** (l)：幂律分布指数 a_3D (2–4.5) [Huang 2021, pp. 2-3]。
- **裂隙密度**：单位体积裂隙数 (P30) 或单位体积裂隙面积 (P32) [Huang 2021, pp. 3-3]。
- **逾渗参数** (p) 与阈值 (pc)：决定网络是否整体连通 [Huang 2021, pp. 4-5]。
- **分形维数** (D)：D3D (2.15–2.7) 和 D2D [Huang 2021, pp. 5-6]。
- **水力开度** (e) 与局部开度分布 (bij)：服从截断高斯、对数正态或幂律分布 [Huang 2021, pp. 3-4]。
- **渗透率** (K) 或等效渗透率：通过达西定律反算 [Huang 2021, pp. 6-7]。
- **连通性指标**：平均每裂隙交点数 (λ)、单位体积交线长度 (C1, L1) [Huang 2021, pp. 4-4]。
- **Fisher常数** (κ)：控制裂隙产状集中程度 [Huang 2021, pp. 2-3]。
- **立方定律参数**：流量 Q、裂隙宽度 w、水力梯度 J [Huang 2021, pp. 6-7]。

## Reusable Claims

- 若需精确评估裂隙岩体渗流，应采用三维DFN，因为二维模型会大幅低估渗透率，立体学效应不可忽略 [Huang 2021, pp. 1-2]。
- 在裂隙开度缓变且流速较低的条件下，可用Reynolds方程替代Navier‑Stokes方程进行流动模拟，但会引入5 – 15%的流量低估 [Huang 2021, pp. 6-7]。
- 对于具有幂律长度分布的裂隙网络，当幂律指数 a3D > D+1 时，大裂隙控制连通性；反之则小裂隙主导，该关系可用于尺度效应分析 [Huang 2021, pp. 5-5]。
- 裂隙长度与开度存在正相关时，等效渗透率可比常数开度模型高1 – 2个数量级，因此在DFN建模中应考虑该相关性 [Huang 2021, pp. 3-4]。
- 采用非一致网格（如扩展有限元）处理裂隙网络时可避免显式匹配交线节点，但需要额外的弱约束来保证水头连续和流量守恒 [Huang 2021, pp. 7-8]。
- 三维裂隙网络的分形维数 D3D 可由二维露头迹线图通过 D2D = D3D – 1 估算，但需注意适用条件 [Huang 2021, pp. 5-6]。

## Candidate Concepts

- [[discrete fracture network (DFN)]]
- [[fracture connectivity]]
- [[percolation theory]]
- [[fractal geometry]]
- [[power law distribution]]
- [[cubic law]]
- [[Reynolds equation]]
- [[Navier-Stokes equations]]
- [[equivalent permeability]]
- [[fracture network topology]]
- [[aperture heterogeneity]]
- [[channeling flow]]
- [[stochastic modeling]]
- [[multiphase flow in fractured media]]
- [[discrete fracture matrix model]]
- [[Joint Roughness Coefficient (JRC)]]

## Candidate Methods

- [[Monte Carlo simulation]]
- [[boundary element method (BEM)]]
- [[finite element method (FEM)]]
- [[mixed hybrid finite element method]]
- [[virtual element method (VEM)]]
- [[extended finite element method (EFEM)]]
- [[discontinuous Galerkin method]]
- [[conforming mesh generation]]
- [[nonconforming mesh approach]]
- [[graph-based flow algorithms]]
- [[Reynolds equation solver]]
- [[PDE-constrained optimization]]
- [[3D printing of fracture networks]]

## Connections To Other Work

- 本文与大量综述和研究紧密相连：Berkowitz (2002) 关于裂隙介质流动与运移的综述为本研究提供了基础；Lei et al. (2017) 侧重裂隙岩体的地质力学‑水力耦合DFN模拟，而本文重点关注纯水力学DFN的几何与数值方法 [Huang 2021, pp. 1-2][Huang 2021, pp. 4-4]。
- 在三维DFN模型生成与连通性分析方面，与Balberg et al. (1984)、de Dreuzy et al. (2000)、Bour & Davy (1998) 等的研究直接衔接 [Huang 2021, pp. 4-5]。
- 流场数值解方面，与Erhel et al. (2009)、Berrone et al. (2014a)、Hyman et al. (2014) 等提出的非一致网格、完全一致网格剖分方法形成对比 [Huang 2021, pp. 7-8]。
- 在多相流模拟上，兼顾了Kim & Deo (1999, 2000)、Hoteit & Firoozabadi (2008) 等的工作，并参考了Phillips et al. (2020) 等关于多孔介质多相流的最新综述 [Huang 2021, pp. 8-9]。
- 非线性流动研究方面，与Zhang & Nemcik (2013) 的单一裂隙工作及Liu et al. (2016a) 的二维网络工作相联系 [Huang 2021, pp. 8-9]。

## Open Questions

- 如何针对含大量裂隙、复杂交切关系的大规模三维DFN开发既保持关键几何特性又能显著提高计算效率的敏捷数值技术？ [Huang 2021, pp. 8-9]
- 在三维裂隙网络中非线性（惯性）流动的定量规律尚不明朗，仅有个别初步模拟工作，未来需系统研究高水力梯度下的非线性效应 [Huang 2021, pp. 8-9]。
- 如何建立适用于工程尺度（油气田、地热储层等）的三维DFN有效升尺度方法，将小尺度模型参数可靠地扩展到大尺度？ [Huang 2021, pp. 8-9]
- 利用3D打印技术制备可控裂隙网络试样进行渗流实验，虽然已显现潜力，但如何用其校准与验证复杂的DFN流动模型仍待深入 [Huang 2021, pp. 9-9]。
- 在三维DFN中直接求解Navier‑Stokes方程的研究几乎是空白，高雷诺数流动的适用性需要探讨 [Huang 2021, pp. 6-7]。

## Source Coverage

所有非空索引片段均已处理。  
- 索引文本块数量：21  
- 源文本总字符数：104,157  
- 编译后正文总字符数：100,358  
- 按字符计算的覆盖比率：0.9635 (约96.35%)  
- 编译策略：单章节全文编译（single-pass-markdown）  
- 签名信息：来源指纹 01800bf96df14de85b4405d6a81cd3ea3f425ea6，覆盖状态为 full-index。
