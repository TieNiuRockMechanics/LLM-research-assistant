---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2006-feng-research-on-laws-of-2d-percolation-of-fully-random-distribution-fracture-media"
title: "Research on Laws of 2D Percolation of Fully Random Distribution Fracture Media."
status: "draft"
source_pdf: "data/papers/2006 - Research on laws of 2D percolation of fully random distribution fracture media.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Feng, Zengchao, et al. “Research on Laws of 2D Percolation of Fully Random Distribution Fracture Media.” *Chinese Journal of Rock Mechanics and Engineering*, vol. 25, no. Supp. 2, Oct. 2006, pp. 3904-05."
indexed_texts: "2"
indexed_chars: "7167"
nonempty_source_blocks: "2"
compiled_source_blocks: "2"
compiled_source_chars: "6397"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.892563"
coverage_status: "full-index"
source_signature: "1995e126c124e313ed9c35da0e8060800df3ebff"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T12:56:59"
---

# Research on Laws of 2D Percolation of Fully Random Distribution Fracture Media.

## One-line Summary
针对全随机分布裂隙介质，提出了基于裂隙数分形分布的二维逾渗数值模拟方法，获得了连接裂隙分形维数、起始分形常数和孔隙率的逾渗阈值数学表达式，并揭示了逾渗规律。

## Research Question
全随机分布裂隙介质的逾渗行为如何受裂隙分形维数 D、起始分形常数 N₀ 及孔隙率 n 的影响，以及如何定量描述其逾渗阈值。

## Study Area / Data
- 二维正方形格子 (L×L) 上的数值模拟，无真实岩体数据。
- 裂隙分布遵循分形标度律 N(δ)=N₀ δ⁻ᴰ，其中 δ 为裂隙长度尺度。
- 考虑孔隙-裂隙双重介质，孔隙为导通单元，骨架为阻塞单元。

## Methods
- **介质分类**：将裂隙介质划分为部分随机分布、成组分布和全随机分布三类，聚焦全随机情形 [Feng 2006, pp. 1-5]。
- **模型构建**：在 L×L 二维方格子中，按分形裂隙数分布 N(δ)=N₀ δ⁻ᴰ 生成裂隙网络；骨架单元依导通规则形成孔隙-裂隙双重模型，导通规则为 0+0=0, 0+1=1, 1+1=1 [Feng 2006, pp. 1-5]。
- **逾渗判据**：定义逾渗概率 P(n, N₀, D) = M(L)/L²，其中 M(L) 为最大连通团大小，逾渗阈值 n_c 为无穷大团出现时的孔隙率，即 sup{n: P∞(n)=0} [Feng 2006, pp. 1-5]。
- **数值模拟**：通过改变孔隙率 n、分形维数 D 和起始常数 N₀，计算逾渗概率及阈值，分析 D‑n 平面上的临界曲线。

## Key Findings
1. **裂隙分形分布影响逾渗阈值**：当孔隙率 n=0、N₀=e (2.71828) 时，分形维数 D 从 1.60 增至 1.68，逾渗团的形态发生明显变化；当 N₀ 固定时，逾渗概率随 D 增大呈非单调变化 [Feng 2006, pp. 1-5]。
2. **阈值数学模型**：得到描述逾渗临界条件的表达式  
   f(n, N₀, D) = (n_c – n_p) – exp(9.7868 – 4.7791·D)·N₀⁻ᴰ = 0，  
   其中 n_p = 0.59275 为纯经典逾渗阈值。当 f<0 时体系不逾渗，f>0 时逾渗 [Feng 2006, pp. 1-5]。
3. **阈值逼近经典值**：当 D=1, N₀=1 时，计算得到的逾渗阈值 n_c = 0.59，与经典二维随机逾渗阈值 0.59275 一致 [Feng 2006, pp. 5-5]。
4. **孔隙率与阈值的线性关系**：裂隙分形维数 D 与孔隙率 n 在临界曲线上呈近似线性关系，不同 N₀ 对应一族曲线，最终汇交于 n_c = 59.275%±0.003% 的垂直线附近 [Feng 2006, pp. 1-5]。
5. **图 4、图 5 证据**：D‑n 平面上的临界逾渗曲线与合并后的统一曲线（相关系数 R²=0.9926）支持上述数学表达式 [Feng 2006, pp. 1-5]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 逾渗概率 P 随孔隙率 n 和分形维数 D 的变化曲线（图 3） | [Feng 2006, pp. 1-5] | 2D 方格子，N₀=e，n=0 或 D 固定 | 显示 D=1.60–1.68 时逾渗团形态变化 |
| 临界逾渗曲线 D‑n 图（图 4） | [Feng 2006, pp. 1-5] | 孔隙率 n 与 D，N₀=0.1,1,10,100 | 曲线族渐近于 n_c≈0.59275 |
| 统一表达式 f(n, N₀, D)=0 及 R²=0.9926（图 5） | [Feng 2006, pp. 1-5] | 汇总不同 N₀ 的数据 | 验证了 n_c–n_p 与 exp(9.7868–4.7791D)·N₀⁻ᴰ 的线性关系 |
| 经典阈值再现：N₀=1, D=1 时 n_c=0.59 | [Feng 2006, pp. 5-5] | 无孔隙（n=0）或相应条件 | 与 pc=0.59275 一致 |

## Limitations
- 仅限二维正方形格子，未考虑三维实际裂隙网络。
- 模拟基于理想的完全随机分布和分形幂律 N(δ)=N₀ δ⁻ᴰ，未涉及真实岩体裂隙的复杂几何与力学性质。
- 缺乏实验或现场数据验证，结论均为数值模拟结果。
- 未分析裂隙方向各向异性、裂隙开度变化及多相流等因素。

## Assumptions / Conditions
- 裂隙介质为 **全随机分布**（位置与方向均随机）[Feng 2006, pp. 1-5]。
- 裂隙数分布满足严格分形标度律：N(δ)=N₀ δ⁻ᴰ，其中 δ 无量纲化裂隙尺度 [Feng 2006, pp. 1-5]。
- 孔隙-裂隙双重介质模型：孔隙为导通（1），骨架为阻塞（0），导通规则为逻辑加 [Feng 2006, pp. 1-5]。
- 逾渗定义为出现跨越整个系统的无限大连通团。
- 模拟采用 L×L 正方格子，边界条件周期性或固壁未明确说明（根据上下文假设为固定边界）。

## Key Variables / Parameters
- `n`：孔隙率（导通单元占比）
- `D`：裂隙分布的分形维数
- `N₀`：裂隙分布的起始分形常数（δ=1 时的裂隙数）
- `P(n, N₀, D)`：逾渗概率（最大连通团大小与总格子数之比）
- `n_c`：逾渗阈值（P∞>0 时的最小 n）
- `n_p`：纯经典逾渗阈值 (0.59275)
- `L`：方格子边长（尺度参数）

## Reusable Claims
- **裂隙分形分布下的逾渗阈值公式**：n_c = n_p + exp(9.7868 – 4.7791·D)·N₀⁻ᴰ，可推广至具有分形裂隙分布的岩体连通性评估，条件是裂隙分布满足该幂律形式且为二维全随机分布 [Feng 2006, pp. 1-5]。
- **阈值趋同经典值**：当 N₀=1 且 D=1 时，逾渗阈值回归至 0.59，表明在特定参数下该双重介质模型与普通二维随机逾渗等价 [Feng 2006, pp. 5-5]。
- **阈值与 D 的线性关系**：在 D‑n 平面，临界曲线近似线性，这一性质可用于快速估计不同分形裂隙岩体的连通临界孔隙率。

## Candidate Concepts
- [[全随机分布裂隙介质 (Fully random distribution fracture media)]]
- [[孔隙-裂隙双重介质 (Porosity and fracture double-media)]]
- [[逾渗阈值 (Percolation threshold)]]
- [[裂隙分形维数 (Fractal dimension of cracks)]]
- [[二维方格子逾渗 (2D square lattice percolation)]]
- [[起始分形常数 (Initial fractal constant)]]
- [[逾渗概率 (Percolation probability)]]

## Candidate Methods
- [[基于分形裂隙数分布的二维逾渗数值模拟 (Numerical simulation of 2D percolation with fractal crack number distribution)]]
- [[最大连通团法求逾渗阈值 (Percolation threshold by largest cluster size M(L)/L²)]]
- [[分形裂隙网络生成 (Fractal fracture network generation using N(δ)=N₀ δ⁻ᴰ)]]
- [[双重介质导通规则 (Dual-media conduction rule 0+0=0,0+1=1,1+1=1)]]

## Connections To Other Work
- 在裂隙数分布上引用了 Kang Tianhe et al. (1995) 对煤岩体裂隙尺度分形的研究 [Feng 2006, pp. 5-5]。
- 逾渗基本理论参考 Stauffer (1985) 的逾渗导论及后续二维预分形多孔介质逾渗研究 (Michafl et al., 2002) [Feng 2006, pp. 5-5]。
- 作者前期工作包括三维裂隙面密度分形分布 (Feng et al., 2005) 和煤岩裂隙双重介质逾渗机制 (Feng et al., 2005) [Feng 2006, pp. 5-5]。

## Open Questions
- 三维全随机分布裂隙介质的逾渗规律是否可用类似表达式描述？
- 当裂隙分布偏离严格幂律或存在方向组构时，阈值公式如何修正？
- 公式中的经验常数 9.7868 和 4.7791 是否具有普适性，还是仅适用于所采用的方格子模型？
- 真实岩体裂隙网络的逾渗阈值与本文数值结果的偏差需要实验标定。

## Source Coverage
本页内容完全基于以下索引片段构建，所有非空片段均已处理：
- [Feng 2006, pp. 1-5]（含摘要、引言、方法、结果及部分结论）
- [Feng 2006, pp. 5-5]（含结论结尾及参考文献）
覆盖率统计：片段数 2/2（按块计 1.0），字符数 6397/7167（0.8926），已实现全索引覆盖。未添加任何外部信息或推测性结论。
