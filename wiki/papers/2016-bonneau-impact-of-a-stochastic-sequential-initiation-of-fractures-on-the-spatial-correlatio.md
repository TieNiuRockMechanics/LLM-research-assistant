---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2016-bonneau-impact-of-a-stochastic-sequential-initiation-of-fractures-on-the-spatial-correlatio"
title: "Impact of a Stochastic Sequential Initiation of Fractures on the Spatial Correlations and Connectivity of Discrete Fracture Networks."
status: "draft"
source_pdf: "data/papers/2016 - Impact of a stochastic sequential initiation of fractures on the spatial correlations and connectivity of discrete fracture networks.pdf"
collections:
citation: "Bonneau, François, et al. “Impact of a Stochastic Sequential Initiation of Fractures on the Spatial Correlations and Connectivity of Discrete Fracture Networks.” *Journal of Geophysical Research: Solid Earth*, vol. 121, 2016, pp. 5641-5658, doi:10.1002/2015JB012451."
indexed_texts: "14"
indexed_chars: "67365"
nonempty_source_blocks: "14"
compiled_source_blocks: "14"
compiled_source_chars: "67691"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004839"
coverage_status: "full-index"
source_signature: "4d3ac69ff9f501970c9cbee1622a2838ef7db1b5"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T18:03:22"
---

# Impact of a Stochastic Sequential Initiation of Fractures on the Spatial Correlations and Connectivity of Discrete Fracture Networks.

## One-line Summary
本文提出一种顺序父子泊松点过程，在三维离散断裂网络中引入源于力学相互作用的层次结构与空间相关性，并系统分析其对分形维数、渗透阈值及局部连通性的影响。[Bonneau 2016, pp. 1-1]

## Research Question
如何将断裂力学相互作用原则整合到随机DFN模拟中，并量化由此产生的空间相关性与连通性效应？[Bonneau 2016, pp. 1-1]

## Study Area / Data
研究基于合成数据，无具体野外研究区。所有三维离散断裂网络均在边长为 90 m 的立方域内生成（中心 30 m³ 用于分析以减小边界效应）。断裂长度服从指数为 1.8（部分测试使用指数 3）的截断幂律分布，范围 1–30 m。分析包含均匀密度图与异构密度图两种场景。[Bonneau 2016, pp. 6-7, 12‑13]

## Methods
- **简化的断裂力学模型**：每个平面断裂对象附带两个椭球体，分别代表应力影区（降低概率）和应力集中区（提高概率）。椭球范围由因子 (αₛ, βₛ) 和 (αₚ, βₚ) 控制。[Bonneau 2016, pp. 2-3]
- **顺序父子泊松点过程**：模拟分 s 个“播种”序列进行。每个序列先用非均匀泊松过程生成候选中心，再按式(1)的概率接受/拒绝候选点，使之受已存在断裂的影响：
  \[
  P_s(x,y,z) = \frac{N}{s}\frac{1+g\times N_{\text{acc}}(x,y,z)}{1+h\times N_{\text{shad}}(x,y,z)} \Big/ \sum_{i=1}^{N} \frac{1+g\times N_{\text{acc}}(x,y,z)_i}{1+h\times N_{\text{shad}}(x,y,z)_i}
  \]
  其中 g≥1 为应力集中区强度因子，h≥1 为影区强度因子。[Bonneau 2016, pp. 3-5]
- **空间相关性度量**：采用对相关函数 C₂(r)≈r^Dc 估计关联维数 Dc，基于中心点对距离统计。[Bonneau 2016, pp. 4-5]
- **连通性分析**：借助渗透理论定义渗透因子 pf = ∑⟨lᵢ³⟩/V，统计渗透概率与每断裂平均交点数随长度和播种比例的变化。[Bonneau 2016, pp. 12-14]

## Key Findings
1. **经典泊松过程产生不相关网络**（Dc≈3），而顺序过程产生空间相关网络（Dc 约 2.4–2.8），且取向集中度对 Dc 影响较小。[Bonneau 2016, pp. 6-7]
2. **影区强度因子 h 是控制 Dc 的主要参数**：Dc(h)≈−0.18 log h + 2.96 ± 0.09；g 的影响微弱：Dc(g)≈−0.03 log(g)+2.81 ± 0.09。[Bonneau 2016, pp. 11-12]
3. **播种比例临界值**：当每序列模拟的断裂占比 ≤10% 时，Dc 收敛；≤0.4% 时基本稳定。但相同 Dc 的 DFN 可能呈现不同的层次组织（如小断裂在大断裂尖端的聚集程度、X 型相交数量）。[Bonneau 2016, pp. 11-12]
4. **顺序过程降低渗透阈值**：与不相关网络相比，渗透因子 pf 减小，且随着每序列模拟比例下降，阈值进一步降低。[Bonneau 2016, pp. 13-14]
5. **局部连通性模型改变**：顺序播种使小断裂交点数增加、大断裂交点数减少，再现“欠发育”到“充分发育”的断裂化体制；若每序列模拟比例过高，则会在中等尺度出现不连续。[Bonneau 2016, pp. 14-15]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 经典泊松 DFN 的 Dc≈3.01±0.07（单组）；顺序过程 Dc≈2.47±0.09 | [Bonneau 2016, pp. 6-7] | 幂律指数 1.8，均匀密度图，10 000 断裂 | 表1，100 次实现均值 |
| 影子区强度 h 与 Dc 的对数关系模型 | [Bonneau 2016, pp. 11-12] | g=10，其他几何参数固定（图1） | 式(3) |
| 每序列模拟 0.1% 断裂时，渗透概率曲线明显左移 | [Bonneau 2016, pp. 13-14] | 幂律指数 3，各项同性取向 | 图13 |
| 顺序播种改变不同长度断裂的交点分布：小断裂交点多，大断裂交点少 | [Bonneau 2016, pp. 14-15] | 幂律指数 3，各项同性取向 | 图14 |
| 均匀密度图下，顺序过程产生的 E‑type 图仍近均匀，但标准偏差增大且有轻微中心偏倚 | [Bonneau 2016, pp. 7-8] | 1000 次实现，g=h=100 | 图5 |
| 异构密度图下，顺序过程保持与参考图的相关性（相关系数 0.76），但弱于经典泊松（0.98） | [Bonneau 2016, pp. 8-9] | g=h=100 | 图6 |

## Limitations
- 假设断裂在模拟时已处于最终状态，忽略了生长、相互作用与合并过程，可能低估连通性。[Bonneau 2016, pp. 2, 15]
- 关联维数 C₂(r) 基于各向同性假设，对取向集中的网络不适用，且未能完全区分不同层次组织。[Bonneau 2016, pp. 6, 15]
- 顺序过程引入微弱的边界效应（中心偏多），接受/拒绝机制对密度图存在一定偏差。[Bonneau 2016, pp. 7-8]
- 计算成本随序列数 s 增加显著增长：10 000 断裂若每序列模拟 10 个，耗时约 10 min。[Bonneau 2016, pp. 11]
- 简化力学模型无法考虑远场应力、各向异性应力扰动的真实非对称性，仅作为平均效应的替代。[Bonneau 2016, pp. 2, 15]

## Assumptions / Conditions
- 断裂径向生长与合并效应已由长度分布律反映，因此可直接栽植最终形态的平面对象。[Bonneau 2016, pp. 2]
- 使用对称椭球模型近似拉伸断裂的一阶应力扰动，默认影区为各向同性。[Bonneau 2016, pp. 2, 6]
- 断裂长度服从指数为 1.8（或 3）的截断幂律，范围 1 – 30 m。[Bonneau 2016, pp. 6, 12]
- 分析关联维数时采用中心子体积（30 m³）以减轻断裂截断效应。[Bonneau 2016, pp. 6]
- 渗透试验中采用的幂律指数 a=3，使小断裂占比较高，以突出空间相关性的影响。[Bonneau 2016, pp. 12-13]
- 所有渗透分析均在各项同性取向下进行。[Bonneau 2016, pp. 12]

## Key Variables / Parameters
- **关联维数 Dc**（由对相关函数得出）[Bonneau 2016, pp. 5]
- **渗透因子 pf** = ∑lᵢ³/V，其中 lᵢ 为断裂等效长度 [Bonneau 2016, pp. 13]
- **每断裂平均交点数**（按长度标准化）[Bonneau 2016, pp. 14]
- **过程参数**：
  - 序列数 s，每序列模拟断裂占比 p(s) = 100/s [Bonneau 2016, pp. 3, 11]
  - 应力集中区强度因子 g（≥1），影区强度因子 h（≥1）[Bonneau 2016, pp. 4]
  - 应力集中区椭球范围因子 αₚ、βₚ；影区范围因子 αₛ、βₛ [Bonneau 2016, pp. 2-3]
- **统计参数**：断裂长度幂律指数 a，取向分布类型 [Bonneau 2016, pp. 6, 12]

## Reusable Claims
- 顺序父子泊松点过程可在不具备明确力学求解的情况下，为三维 DFN 引入可调的空间相关性，同时尊重长度、取向等先验统计。[Bonneau 2016, pp. 1-2, 4‑5]
- 网络的空间相关性与连通性可通过调整影区强度 h 进行粗略控制，且 h 对 Dc 存在半对数线性关系，可作为调谐依据。[Bonneau 2016, pp. 11-12]
- 与经典泊松 DFN 相比，机械层次播种能降低渗透阈值，特别是在长度分布指数较大（小断裂主导）时。[Bonneau 2016, pp. 13-14]
- 即使 Dc 相同，播种节奏（p(s)）仍影响局部交点数分布，说明 Dc 不足以唯一描述网络的层次结构。[Bonneau 2016, pp. 12, 15]
- 顺序过程天然再现“欠发育—充分发育”体制的过渡，无需额外规则。[Bonneau 2016, pp. 4-5, 14]

## Candidate Concepts
- [[离散断裂网络 (DFN)]] 
- [[空间相关性 (spatial correlation)]] 
- [[关联维数 (correlation dimension)]] 
- [[渗透阈值 (percolation threshold)]] 
- [[顺序父子泊松点过程 (sequential parent-daughter Poisson point process)]] 
- [[伪力学模型 (pseudo-mechanical model)]] 
- [[应力影区与应力集中区 (stress shadow and concentration zones)]] 
- [[幂律长度分布 (power-law length distribution)]] 
- [[E‑type 图 (E‑type map)]]

## Candidate Methods
- [[关联维数估计 (C₂(r) 方法)]]
- [[顺序泊松种子模拟 (sequential seeding algorithm)]]
- [[渗透分析 (percolation analysis)]]
- [[敏感度分析 (sensitivity analysis)]]
- [[Monte Carlo 断裂取样 (Monte Carlo fracture sampling)]]

## Connections To Other Work
- **与 Davy 等 (2010, 2013) 的通用断裂模型**：均通过种子-生长-停止过程产生层次网络，但本文采用固定最终状态与椭球区驱动，而非实时传播至最近断裂距离。[Bonneau 2016, pp. 2, 15]
- **与 Cladouhos & Marrett (1996) 的联动模型**：他们建立二维联动与幂律分布的关联，本文则在三维中量化排序种子对分形与连通性的影响。[Bonneau 2016, pp. 2]
- **与 Wu & Pollard (1995)、Josnin 等 (2002) 等**：本文模拟的自然再现了“欠发育”与“充分发育”断裂体制，与这些工作中的描述一致。[Bonneau 2016, pp. 4, 14]
- **与 Darcel (2003) 的发现一致**：对于高幂律指数网络，空间相关性能改变渗透阈值。[Bonneau 2016, pp. 13]
- **排除体积概念 (Balberg et al., 1984)**：本文所用渗透因子 pf 借鉴了此概念，并按照 Bour & Davy (1997, 1998) 和 de Dreuzy et al. (2000) 的形式定义。[Bonneau 2016, pp. 13]

## Open Questions
- 如何定义一种非各向同性的空间相关性度量，以同时捕捉断裂中心的聚集及其大小的层次组织？[Bonneau 2016, pp. 15]
- 将弯曲、分叉断裂纳入顺序模拟会对连通性产生何种额外影响？[Bonneau 2016, pp. 15]
- 能否通过现场数据或物理实验约束 g、h 等参数，使顺序过程与实际断裂过程建立关系？[Bonneau 2016, pp. 15-16]
- 在考虑非各向同性影区（如滑动断裂尖端的不对称应力集中）时，参数化方案如何选择？[Bonneau 2016, pp. 15]
- 顺序播种引入的边界效应能否通过修正算法消除？[Bonneau 2016, pp. 7-8]

## Source Coverage
本页面已处理并提供所有 14 个非空索引片段，覆盖率为 100%（片段数：14/14，字符覆盖比 1.004839）。[Coverage audit record]
