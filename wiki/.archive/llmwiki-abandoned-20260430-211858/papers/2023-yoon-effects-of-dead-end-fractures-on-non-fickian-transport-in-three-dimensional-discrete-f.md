---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-yoon-effects-of-dead-end-fractures-on-non-fickian-transport-in-three-dimensional-discrete-f"
title: "Effects of Dead-End Fractures on Non-Fickian Transport in Three-Dimensional Discrete Fracture Networks."
status: "draft"
source_pdf: "data/papers/2023 - Effects of Dead-End Fractures on Non-Fickian Transport in Three-Dimensional Discrete Fracture Networks.pdf"
collections:
citation: "Yoon, Seonkyoo, et al. \"Effects of Dead-End Fractures on Non-Fickian Transport in Three-Dimensional Discrete Fracture Networks.\" 2023."
indexed_texts: "17"
indexed_chars: "83282"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T12:15:08"
---

# Effects of Dead-End Fractures on Non-Fickian Transport in Three-Dimensional Discrete Fracture Networks.

## One-line Summary
本研究通过大规模三维离散裂隙网络模拟和一种基于图论的新型死端裂缝识别方法，揭示了死端裂缝对非Fickian溶质运移的控制作用，并发现死端裂缝密度在渗透阈值处最大化，导致最强的晚时拖尾，可作为非Fickian输运的有效预测指标 [Yoon 2023, pp. 1-1, 1-2]。

## Research Question
死端裂缝如何定量影响三维裂隙网络中的非Fickian溶质运移，其效应如何随裂缝密度和网络拓扑改变？虽然死端裂缝被认为是导致溶质滞留的低速区域，但其与非Fickian输运的直接量化关系此前尚不明确 [Yoon 2023, pp. 1-1]。

## Study Area / Data
研究采用半通用（semi-generic）三维离散裂隙网络合成数据集，未基于特定野外场地。模拟域为边长 15 m 的立方体，系统生成了具有不同裂缝长度分布（幂律指数 α）和不同裂缝密度的网络实现，覆盖了从低于到远高于渗透阈值的范围 [Yoon 2023, pp. 2-3, 3-4, 4-6]。

## Methods
- **裂隙网络生成**：在 15 m 立方域内生成泊散型（statistical）三维离散裂隙网络，裂缝长度服从幂律分布，控制参数为幂律指数 α（如 2.0, 2.2, 2.4）和归一化裂缝密度 ρ（ρ = n / n_c，n 为裂缝总数，n_c 为渗透阈值裂缝数）[Yoon 2023, pp. 2-3, 3-4]。
- **死端裂缝识别**：提出一种基于图论的新方法。将裂隙网络映射为图（裂缝→顶点，交线→边，引入源点和汇点代表出入口边界），通过双连通分量（biconnected component）分解，找出那些移除后会使源‑汇分离的连通分量，其对应的裂缝即定义为死端裂缝（具体算法见表 1）[Yoon 2023, pp. 4-6, 6-7, 7-8]。该方法与传统的 2‑core 子图定义进行了对比 [Yoon 2023, pp. 6-7]。
- **流动与溶质运移模拟**：采用 dfnWorks 套件，仅考虑平流输运，忽略分子扩散、基质扩散和吸附。基质假设为不透水（适用于硬岩如花岗岩）。施加 1 MPa 水平压力差，其余侧面为无流动边界。使用有限体积法（PFLOTRAN）求解稳态压力场，通过粒子追踪计算首次通过时间分布（FPTD）[Yoon 2023, pp. 7-8]。
- **非Fickian特征量化**：对 FPTD 的 95% 至 99.99% 分位数区间进行线性回归求得尾斜率；斜率小于 3 判定为非Fickian。同时计算 FPTD 的第二矩（方差）以度量到达时间的非均质性 [Yoon 2023, pp. 8-10]。

## Key Findings
1. 溶质晚时拖尾强度在渗透阈值（ρ = 1）处达到最大，此时尾斜率最小；随着 ρ 增加，拖尾减弱。当 ρ ≤ 2 时尾斜率 <3，表现为非Fickian输运；ρ > 2 后尾斜率显著下降，输运进入Fickian区 [Yoon 2023, pp. 8-10]。
2. FPTD 的方差（第二矩）与尾斜率趋势一致：ρ > 2 后方差急剧减小，表明高连通性限制了到达时间的散布，网络结构复杂性下降 [Yoon 2023, pp. 8-10]。
3. 死端裂缝密度是预测非Fickian输运的有效拓扑指标：在渗透阈值处死端裂缝大量存在，导致强滞留；随连通性增强死端裂缝减少，非Fickian特征减弱 [Yoon 2023, pp. 1-1, 8-10]。
4. 与2‑core子图方法相比，基于双连通分量的死端裂缝定义能更准确地识别影响溶质运移的拓扑结构 [Yoon 2023, pp. 6-7]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 尾斜率在 ρ=1 时最小，随 ρ 增加增大；ρ≤2 时斜率<3 (非Fickian)，ρ>2 时>3 (Fickian) | [Yoon 2023, pp. 8-10] | α=2.0, 2.2, 2.4；仅平流；忽略扩散与吸附；域尺寸15 m | 基于合成DFN的数值模拟结果 |
| FPTD 第二矩随 ρ 增加而下降，ρ>2 后降幅尤为显著 | [Yoon 2023, pp. 8-10] | 同上 | 强化晚时拖尾趋势的统计量 |
| 渗透阈值处死端裂缝密集，导致强非Fickian拖尾；死端裂缝密度与拖尾程度正相关 | [Yoon 2023, pp. 1-1, 8-10] | 使用归一化密度ρ，死端由双连通分量法识别 | 将拓扑结构与输运异常直接关联 |
| 双连通分量法比2-core方法能更真地反映对溶质滞留负责的死端结构 | [Yoon 2023, pp. 6-7] | 图节点为裂缝，边为交线 | 方法对比，结论源自图论分析与物理直观 |

## Limitations
- 模拟未考虑裂缝内孔径变异性，因此结果和结论仅适用于网络结构主导、孔内非均质效应可忽略的物理场景 [Yoon 2023, pp. 3-4]。
- 只考虑平流输运，未包括分子扩散、基质扩散和吸附，不适用于基质渗透性显著或扩散/吸附作用较强的介质 [Yoon 2023, pp. 7-8]。
- 网络为统计生成的半通用模型，未用真实地质力学过程（如裂缝成核、生长）约束，可能与天然裂隙拓扑有差异 [Yoon 2023, pp. 2-3]。
- 所有结论基于固定域尺寸（15 m）和特定边界条件（单方向压力梯度，侧向无流），尺度与各向异性效应未在片段中讨论。

## Assumptions / Conditions
- 基质为不透水介质，流体仅在裂隙中流动，无基质‑裂隙交换 [Yoon 2023, pp. 7-8]。
- 溶质输运仅由平流驱动，扩散、吸附、反应均忽略 [Yoon 2023, pp. 7-8]。
- 裂缝内隙宽恒定且光滑，内部粗糙度及其对流动的影响不纳入 [Yoon 2023, pp. 3-4]。
- 裂缝网络由泊松散生成，裂缝长度服从幂律分布，无地质力学约束 [Yoon 2023, pp. 2-3]。
- 流动由 1 MPa 水平压差驱动，其余边界无流动，形成水平一维宏观流动 [Yoon 2023, pp. 7-8]。
- 归一化密度 ρ 以临界渗透阈值 n_c 为基准，n_c 由数值渗透概率曲线（文中图1）确定 [Yoon 2023, pp. 3-4, 4-6]。

## Key Variables / Parameters
- ρ：归一化裂缝密度，ρ = n / n_c（n为裂缝数量，n_c为渗透阈值）[Yoon 2023, pp. 3-4]。
- α：裂缝长度幂律分布的指数，研究中使用 α = 2.0, 2.2, 2.4 [Yoon 2023, pp. 4-6, 8-10]。
- n_c：临界渗透阈值（最小使网络连通跨越域的裂缝数）[Yoon 2023, pp. 3-4]。
- FPTD 尾斜率：从 95% 至 99.99% 分位数回归获得，用于诊断非Fickian性（<3 为非Fickian）[Yoon 2023, pp. 8-10]。
- FPTD 第二矩（方差）：度量溶质到达时间分散程度的指标 [Yoon 2023, pp. 8-10]。
- 死端裂缝密度：网络中死端裂缝的数量或占比，由基于图论的分解方法确定 [Yoon 2023, pp. 6-7, 8-10]。

## Reusable Claims
- 在基质不透水且无扩散/吸附的三维离散裂隙网络中，死端裂缝密度在渗透阈值处达到最大，导致首次通过时间分布的晚时拖尾最强，输运呈现非Fickian特征（尾斜率<3）；死端裂缝密度可作为预测非Fickian程度的有效拓扑指标 [Yoon 2023, pp. 1-1, 1-2, 8-10]。适用条件：仅平流，忽略孔内变异性。
- 当归一化裂缝密度从 ρ=1 增加至 ρ>2 时，死端裂缝密度下降，网络连通性增强，晚时拖尾减弱，输运逐渐转变为Fickian型（尾斜率>3）[Yoon 2023, pp. 8-10]。条件：幂律长度指数 α 在 2.0‑2.4 区间，域尺寸 15 m。
- 基于双连通分量分解的图论方法比传统2‑core子图法能更准确地识别造成溶质滞留的死端裂缝，因为前者能区分分离源‑汇的关键连接 [Yoon 2023, pp. 6-7]。适用：以裂缝为节点、交线为边的图表示。
- 死端裂缝密度是表征三维裂隙网络非Fickian输运潜力的强预测变量，尤其在渗透阈值附近和低连通度区间 [Yoon 2023, pp. 1-2, 8-10]。

## Candidate Concepts
- [[dead-end fracture]]  
- [[non-Fickian transport]]  
- [[percolation threshold]]  
- [[discrete fracture network (DFN)]]  
- [[first passage time distribution (FPTD)]]  
- [[late-time tailing]]  
- [[graph theory in fracture networks]]  
- [[biconnected component]]  
- [[flow channelization]]  
- [[fracture connectivity]]

## Candidate Methods
- [[dfnWorks]]  
- [[graph-based dead-end fracture identification]]  
- [[biconnected component decomposition]]  
- [[advective particle tracking]]  
- [[finite volume flow solver (PFLOTRAN)]]  
- [[tail slope estimation (FPTD)]]  
- [[percolation analysis]]  
- [[synthetic fracture network generation]]

## Connections To Other Work
- 文中明确引用了关于裂缝密度对流动通道化影响的研究（如 Hyman 2020; Hyman, Dentz, et al. 2019; Sherman et al. 2019, 2020），本研究在此基础上将焦点延伸至死端裂缝的定量作用 [Yoon 2023, pp. 1-2, 3-4]。
- 与2‑core子图方法的对比直接连接了先前广泛采用的图论死端定义，指出其局限性 [Yoon 2023, pp. 6-7]。
- 利用 Makedonska et al. (2016) 关于孔径变异性在低方差、短相关长度时对升尺度性质影响较小的结论，支撑了忽略孔内变量的合理性 [Yoon 2023, pp. 3-4]。
- 依据 Dentz et al. (2004) 的尾斜率判据（斜率<3为非Fickian）对输运类型进行划分 [Yoon 2023, pp. 8-10]。
- 主题上可连接到 [[fracture-matrix interaction]], [[geomechanical fracture modeling]], [[aperture variability]], [[anomalous transport in porous media]] 等领域，但当前片段未提供这些连接的详细定量分析。

## Open Questions
- 若计入分子扩散、基质扩散和吸附等过程，死端裂缝造成的晚时拖尾将如何改变？[Yoon 2023, pp. 7-8 指出仅考虑平流]
- 孔内孔径变异性在哪些条件下会明显增强或削弱死端裂缝的滞留效应？当前结论仅适用于变异性可忽略的场景 [Yoon 2023, pp. 3-4]。
- 本研究使用的固定域尺寸（15 m）下得出的最大拖尾在渗透阈值处的规律在其它尺度是否成立？[片段未讨论尺寸效应]
- 幂律指数 α 与渗透阈值和死端密度的定量关系能否建立普适性预测模型？当前只报道了有限几个 α 值的结果 [Yoon 2023, pp. 4-6]。
- 所提出的死端裂缝识别方法及非Fickian拖尾预测能力在真实岩体示踪试验中表现如何，尚需野外验证 [未从索引片段中确认]。

## Source Coverage
本知识页基于论文的 17 条索引片段撰写，覆盖了摘要、引言、方法（网络生成、图论死端识别、流动与溶质运移模拟）以及主要结果（尾斜率与第二矩随 ρ 的变化趋势）。片段页码跨度为 pp. 1‑10，而全文共 17 页，故缺失内容包括详细讨论、更多 α 值的系统结果、图论方法的深入验证、与真实数据的比较分析以及结论部分的完整总结。此外，文中图件和表格的详细信息（如渗透概率曲线、FPTD 完整图形、死端密度分布等）未在片段中直接呈现，因此某些量化关系可能未被完全捕捉。
