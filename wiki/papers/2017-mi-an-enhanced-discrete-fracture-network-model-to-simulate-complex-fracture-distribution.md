---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-mi-an-enhanced-discrete-fracture-network-model-to-simulate-complex-fracture-distribution"
title: "An Enhanced Discrete Fracture Network Model to Simulate Complex Fracture Distribution."
status: "draft"
source_pdf: "data/papers/2017 - An Enhanced Discrete Fracture Network model to simulate complex fracture distribution.pdf"
collections:
  - "雷恩学派分形研究"
citation: "Mi, Lidong, et al. \"An Enhanced Discrete Fracture Network Model to Simulate Complex Fracture Distribution.\" *Journal of Petroleum Science and Engineering*, vol. 159, 2017, pp. 1-10, doi:10.1016/j.petrol.2017.06.035."
indexed_texts: "11"
indexed_chars: "53768"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "53800"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.000595"
coverage_status: "full-index"
source_signature: "9a2b72cebc194b00198bce01ea5a94ecb99ef382"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T18:43:30"
---

# An Enhanced Discrete Fracture Network Model to Simulate Complex Fracture Distribution.

## One-line Summary
本文提出一种增强型离散裂缝网络（EDFN）模型，通过基于裂缝交点和端点的最小网格离散化与快速图像处理算法优化基质分块，可在极低网格数下高效且准确地模拟复杂裂缝分布及基质-裂缝流体交换，并已扩展至含非达西机理的页岩气藏模拟。[Mi 2017, pp. 1-1]

## Research Question
如何高效表征复杂裂缝网络并准确模拟基质与裂缝间的流体交换，是裂缝性储层数值模拟的核心挑战。[Mi 2017, pp. 1-1] 现有多重连续介质方法（MCA）、离散裂缝模型（DFM）、嵌入式离散裂缝模型（EDFM）和传统离散裂缝网络（DFN）方法均存在计算效率低、精度不足或难以处理任意方向裂缝等局限。[Mi 2017, pp. 1-1] 本文旨在开发一种增强型离散裂缝网络（EDFN）模型，在最大限度减少网格数量的同时，保持对任意方向、互联裂缝的高精度模拟能力。[Mi 2017, pp. 1-1]

## Study Area / Data
- **验证案例 1（简单裂缝配置）**：三维矩形储层，尺寸 100×100×100 ft³，中心一条长 100 ft 的裂缝与一口水平井，无流动边界，裂缝对称分布将储层划分为四个等体积区域，生产甲烷，参数见表 1。[Mi 2017, pp. 7-9]
- **验证案例 2（复杂裂缝分布）**：储层尺寸 600×300×20 ft³，含不规则复杂裂缝网络，水平生产井，用于对比 NFFLOW 和 CMG 软件，储层参数同表 1。[Mi 2017, pp. 7-9]
- **示例 1（任意方向裂缝网络）**：单井非常规储层模型，包含 58 条尺寸 20×20×20 ft³ 的任意倾角裂缝，模拟 60 天气生产。[Mi 2017, pp. 9-9]
- **页岩气藏应用**：储层尺寸 5000×2500×100 ft³，裂缝网络包含 5 条不同长度的平面水力裂缝和 81 条次生裂缝。[Mi 2017, pp. 9-10] 基质渗透率 100 nD，孔隙度 4.4%，Langmuir 压力 2170.8 psi，Langmuir 体积 2.72 scf/ft³ 等。[Mi 2017, pp. 10-12]

## Methods
- **EDFN 数学模型**：包含裂缝流动、基质流动、基质-裂缝质量传递和水平井筒流动四个模块，基于单相气体达西流假设，裂缝交点无累积，裂缝渗透率由立方定律 kf = w²/12 计算，基质内流动简化为一维非稳态达西流，质量传递以 recharge rate 形式耦合，水平井视为大裂缝处理。[Mi 2017, pp. 1-3][Mi 2017, pp. 3-5]
- **裂缝网络离散化**：在裂缝交点和端点放置节点，直接以节点划分裂缝网格，网格数满足 Nfracture-grid > Σ(Nintersection_i + 1)，极大减少裂缝表征所需网格数。[Mi 2017, pp. 5-5]
- **基质离散化**：采用快速图像处理算法，将储层域二值化为像素图像，计算每个像素到各裂缝网格的最短有效距离，将该像素分配给距离最短的裂缝网格以形成粗化基质块（体积 Vmi = n·S·h）。[Mi 2017, pp. 5-7] 粗块等体积转化为宽度等于裂缝网格长度的矩形，再沿垂直裂缝方向进行对数细分（每粗块 10 层精细网格），简化为 1D 流动问题。[Mi 2017, pp. 5-7] 基质与总网格数分别满足 Nmatrix-grid > 20 × Nfracture-grid 和 Ngrid > 21 × Nfracture-grid。[Mi 2017, pp. 5-7]
- **与 Sarda 方法的区别**：Sarda et al. (2001) 在裂缝中点设边界，本方法直接用节点作为网格边界；Sarda 的基质分区为整块，本方法在裂缝两侧分别划分非对称基质块，更精细反映裂缝网络拓扑。[Mi 2017, pp. 5-5][Mi 2017, pp. 5-7]
- **验证**：与 NFFLOW、CMG 对比，误差用 L2 相对误差评估。[Mi 2017, pp. 7-9]
- **页岩气非达西机理**：通过 Civan (2010) 表观渗透率模型引入气体滑移和 Knudsen 扩散，以 Langmuir 等温模型处理解吸，并考虑应力相关裂缝开度（Mi et al., 2016a）。[Mi 2017, pp. 9-10]

## Key Findings
- 简单裂缝案例中，EDFN 结果与 NFFLOW 高度吻合，气体速率、累计产量和平均储层压力的平均相对误差均小于 0.5%。[Mi 2017, pp. 7-9]
- 复杂裂缝网络中，EDFN 与 CMG 结果一致，对应误差分别为 5.98%、1.12% 和 1.95%，而 NFFLOW 因加权平均网格不能反映拓扑导致产气量高估超 80%。[Mi 2017, pp. 7-9]
- EDFN 的网格数远少于 CMG（如 374 对比 7965），减少约 20 倍，同时维持了高精度。[Mi 2017, pp. 9-9]
- EDFN 成功模拟了含 58 条任意倾角裂缝的复杂网络，展示了处理任意方向裂缝的能力。[Mi 2017, pp. 9-9]
- 页岩气模拟显示（30 年）：考虑解吸增产 10.79%，考虑滑移和扩散增产 16.91%，三者同时考虑增产 30.30%；应力相关裂缝开度的影响可忽略。[Mi 2017, pp. 9-10] 裂缝压力约 0.001 天即降至井底压力，基质压力受极低渗透率和裂缝分布控制，SRV 外部压力传播缓慢。[Mi 2017, pp. 10-12]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| EDFN vs NFFLOW 简单裂缝案例的平均相对误差 <0.5% | [Mi 2017, pp. 7-9] | 对称裂缝，边界无流动，参数如表 1 | 基础准确性验证 |
| NFFLOW 复杂裂缝产气误差 >80%，EDFN 与 CMG 误差 5.98%、1.12%、1.95% | [Mi 2017, pp. 7-9] | 复杂网络，CMG 用 7965 格，EDFN 用 374 格 | EDFN 显著优于 NFFLOW，与 CMG 接近 |
| 总网格数 Ngrid > 21 × Nfracture-grid | [Mi 2017, pp. 5-7] | 粗块细分为 10 层对数网格 | 理论计算成本优势 |
| 解吸+滑移+扩散使页岩气产量增加 30.30% | [Mi 2017, pp. 9-10] | 表 3 参数，裂缝网络含 5+81 条 | 非达西机理的综合影响 |
| 应力相关裂缝开度影响极小（相对差异 <0.001%） | [Mi 2017, pp. 10-12] | 表 4，高导流裂缝 | 导流能力冗余 |
| EDFN 可模拟 58 条任意倾角裂缝的 60 天生产 | [Mi 2017, pp. 9-9] | 表 1 参数 | 任意方向能力论证 |

## Limitations
- 当前 EDFN 数学公式仅针对二维单相气体达西流，三维扩展未在文中展开。[Mi 2017, pp. 1-3]
- 基质矩形等效和一维流动假设对极不规则基质块可能引入近似误差。[Mi 2017, pp. 5-7]
- 应力敏感影响可忽略的结论基于极高导流裂缝条件，当裂缝开度或渗透率更低时可能不再适用。[Mi 2017, pp. 9-10]
- 未涉及小裂缝与基质网格尺度相近时的非相邻连接问题。[Mi 2017, pp. 1-1]
- 验证仅为数值对比，缺少物理实验或现场数据支持。

## Assumptions / Conditions
- 单相气体达西流（可扩展至非达西机理）。[Mi 2017, pp. 1-3]
- 裂缝流满足达西定律，渗透率由立方定律给出。[Mi 2017, pp. 1-3]
- 基质流动简化为一维非稳态达西流，基质块等效为矩形。[Mi 2017, pp. 1-3][Mi 2017, pp. 5-7]
- 基质-裂缝质量交换垂直于裂缝面，在裂缝网格两侧发生。[Mi 2017, pp. 3-5]
- 二维平面内任意两裂缝交于一点，交点无累积。[Mi 2017, pp. 1-3]
- 水平井视为大裂缝处理。[Mi 2017, pp. 3-5]
- 图像处理时像素分辨率足够，以保证分配收敛。[Mi 2017, pp. 5-5]
- 页岩气模拟中采用 Civan 表观渗透率、Langmuir 等温吸附、Mi et al. (2016a) 应力相关开度模型。[Mi 2017, pp. 9-10]

## Key Variables / Parameters
- Nfracture-grid, Nmatrix-grid, Ngrid [Mi 2017, pp. 5-7]
- 裂缝开度 w, 裂缝渗透率 kf [Mi 2017, pp. 1-3]
- 像素分辨率 Npix_x, Npix_y [Mi 2017, pp. 5-5]
- 基质渗透率 km, 孔隙度 φ [Mi 2017, pp. 1-3]
- 气体速率、累计产量、平均压力 [Mi 2017, pp. 7-9]
- Langmuir 压力/体积，基质孔隙半径，应力敏感模量 [Mi 2017, pp. 10-12]
- 基质对数细分层数（本文取 10）[Mi 2017, pp. 5-7]

## Reusable Claims
- EDFN 裂缝网格数由交点和端点决定，满足 Nfracture-grid > Σ(Nintersection_i + 1)，可最小化网格。（条件：二维连通裂缝网络）[Mi 2017, pp. 5-5]
- 快速图像处理算法通过最短有效距离将像素分配给裂缝网格，所得基质分块能反映裂缝网络拓扑结构。（条件：像素分辨率充分）[Mi 2017, pp. 5-7]
- 将粗化基质块等体积转化为矩形并进行对数细分，可有效捕捉瞬态交换，总网格数约为 21 倍裂缝网格数。（条件：矩形宽度取裂缝长度，流动可视为一维）[Mi 2017, pp. 5-7]
- 复杂裂缝网络中，EDFN 与 CMG 精度相当，但网格数减少约 20 倍。（条件：复杂裂缝，CMG 使用对数局部加密网格）[Mi 2017, pp. 7-9][Mi 2017, pp. 9-9]
- 页岩气中同时考虑解吸、滑移和 Knudsen 扩散可使 30 年累计产量提升约 30%。（条件：表 3 参数，高导流裂缝）[Mi 2017, pp. 9-10]
- 在高导流裂缝条件下，应力相关开度变化对页岩气产能影响可忽略。（条件：开度极小但相对纳米达西基质仍为无限导流）[Mi 2017, pp. 9-10]

## Candidate Concepts
- [[Enhanced Discrete Fracture Network (EDFN) model]]
- [[fracture network discretization based on intersections and extremities]]
- [[rapid image processing for matrix partition]]
- [[shortest effective distance assignment]]
- [[logarithmic grid refinement in matrix blocks]]
- [[1D flow reduction for matrix-fracture exchange]]
- [[non-Darcy flow mechanisms (gas slippage, Knudsen diffusion, desorption)]]
- [[stress-dependent fracture aperture]]
- [[Civan apparent permeability model]]
- [[Langmuir isotherm for shale gas desorption]]

## Candidate Methods
- [[EDFN grid discretization algorithm]]
- [[pixel-based distance computation for matrix block assignment]]
- [[equivalent rectangular coarse matrix block transformation]]
- [[Voronoi-like partitioning using fracture grids as seeds]]
- [[comparison with NFFLOW and CMG for validation]]
- [[incorporation of apparent permeability and desorption in EDFN]]

## Connections To Other Work
- 与 Sarda et al. (2001) 相比，EDFN 改进了裂缝节点划分方式和基质非对称分块，提高了网格映射精度。[Mi 2017, pp. 5-5][Mi 2017, pp. 5-7]
- 与 McKoy and Sams (2010) 的 NFFLOW 相比，EDFN 用图像处理算法代替加权平均虚拟网格，能更真实反映裂缝网络拓扑，从而显著提升复杂网络下的精度。[Mi 2017, pp. 7-9]
- 与 CMG（IMEX）对比表明，EDFN 以更少的网格实现了相近的模拟精度，体现了计算效率优势。[Mi 2017, pp. 7-9]
- 页岩气建模借鉴了 Civan (2010) 的表观渗透率模型和 Moridis et al. (2010) 的吸附处理方案，并集成了 Mi et al. (2016a) 的应力相关裂缝开度模型。[Mi 2017, pp. 9-10]

## Open Questions
- EDFN 模型向三维扩展时，裂缝节点定义和基质三维图像处理算法的适应性未讨论。
- 裂缝交叉处更复杂的流动行为（如多相流、惯性流）未纳入模型。
- 快速图像处理算法对像素分辨率的收敛准则缺乏定量描述，仅有加倍分辨率检验截断误差的建议。[Mi 2017, pp. 5-5]
- 矩形等效和对数细分在非规则基质块上的近似误差未作定量分析。
- 应力敏感可忽略的结论是否适用于基质渗透率更低或裂缝初始开度更小的储层？
- 文中缺乏 EDFN 模型在历史拟合和实际油田产量预测中的应用实例。

## Source Coverage
所有非空的索引片段（共 11 个）均已完整纳入本页面，覆盖全部索引字符数 53,768（源字符数 53,800），覆盖率 1.0。来源签名：9a2b72cebc194b00198bce01ea5a94ecb99ef382。
