---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2024-shaoqun-dong-relationship-between-box-counting-fractal-dimension-and-properties-of-fracture"
title: "Relationship between Box-Counting Fractal Dimension and Properties of Fracture Networks."
status: "draft"
source_pdf: "data/papers/2024 - Relationship between box-counting fractal dimension and properties of fracture networks.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Shaoqun Dong, et al. \"Relationship between Box-Counting Fractal Dimension and Properties of Fracture Networks.\" *Unconventional Resources*, vol. 4, 2024, p. 100068. Accessed 2026."
indexed_texts: "12"
indexed_chars: "57552"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "54152"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.940923"
coverage_status: "full-index"
source_signature: "bb7a28a1b7896f5ecb5d0b818e4c9c90cdd07c69"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T07:44:10"
---

# Relationship between Box-Counting Fractal Dimension and Properties of Fracture Networks.

## One-line Summary
本研究通过蒙特卡洛模拟和多元分析，针对三种二维离散裂缝网络（DFN）——不变长度随机方向、指数长度随机方向、指数长度与 von‑Mises 方向——建立了盒计数分形维数 D 与裂缝数量、平均长度及方向集中度之间的有理函数预测方程，相关性均超过 0.99，并利用实际露头验证了其有效性。[Shaoqun 2024, pp. 1-1, 10-11, 13-14]

## Research Question
如何基于多个裂缝属性（裂缝长度、数量和方向）建立可靠的方程来预测盒计数分形维数 D？以往工作多集中于 D 与单一属性（如密度）的半定量关系，无法全面体现多属性综合影响，也难以用于变参数的裂缝网络。[Shaoqun 2024, pp. 1-2, 5-7]

## Study Area / Data
- **数值实验区域**：100 m × 100 m 的二维方形域，裂缝密度 P₂₀ = n/10⁴。裂缝数量 n 取值 130 至 970 等；固定长度 L 或指数分布平均长度 1/λ 取值 7 至 95；定向分布包括完全随机和 von‑Mises 分布（μ 设为 π/2，κ 在 5 至 100 范围内）。每种参数组合通过多次实现（20 或 100 次）获得平均 D。[Shaoqun 2024, pp. 2-3, 5, 7, 9-11]
- **验证数据**：取自 Wilson [5] 的岩体露头裂缝网络，参数 n=35，1/λ=4，κ=145.18。[Shaoqun 2024, pp. 10-11, 13-14]

## Methods
1. **离散裂缝网络（DFN）建模**：采用标记点过程（MPP），用泊松点过程模拟裂缝中心位置，用固定长度、指数分布（f(L|λ)=λe⁻λᴸ）或 von‑Mises 分布（f(φ|μ,κ)）分别模拟裂缝长度和方向。[Shaoqun 2024, pp. 2-3]
2. **盒计数分形维数计算**：将区域划分为 len/2ᵏ 的网格，利用层次粗化的快速判交算法一次性获得各尺度 r 下包含裂缝的盒子数 N(r)，然后对 log(N(r)) 与 log(1/r) 线性拟合，斜率即为 D。[Shaoqun 2024, pp. 3-5]
3. **多元拟合流程**：首先单变量分析 D 与 n、L（或 1/λ）的关系，确认均可用有理函数 y=(ax+b)/(x+c) 良好描述；进而假设多变量关系为更复杂的广义有理函数形式（如式 6、9、12），通过蒙特卡洛模拟生成的 (n, 平均长度, κ, D) 数据集进行曲面拟合，并评估残差和相关性。[Shaoqun 2024, pp. 5-11]
4. **实际网络验证**：将露头裂缝网络参数代入拟合所得方程，对比预测 D 与直接计算值的误差，并考察不同网格分辨率 k 的影响。[Shaoqun 2024, pp. 10-11]

## Key Findings
- 对于等长随机方向 DFN，D 与 (n, L) 的关系由式 (6) 表示，相关系数 > 0.999，均方根误差 0.0152。[Shaoqun 2024, pp. 5-7]
- 对于指数长度随机方向 DFN，D 与 (n, 1/λ) 的关系由式 (9) 拟合，相关系数 > 0.999，RMSE = 0.0141。[Shaoqun 2024, pp. 7-9]
- 对于指数长度 von‑Mises 方向 DFN，D 与 (n, 1/λ, κ) 的关系由式 (12) 表达，相关系数接近 1，RMSE = 7 × 10⁻⁶；D 随 κ 增大（方向更集中）而减小。[Shaoqun 2024, pp. 9-11]
- 利用实际露头 n=35、1/λ=4、κ=145.18 验证时，预测 D≈0.99507，在不同网格分辨率下的误差均低于 2.3%，证明推导关系有效。[Shaoqun 2024, pp. 10-11, 13-14]
- 所有公式在低裂缝数量或短裂缝时残差较大，适用于高密度裂缝网络。[Shaoqun 2024, pp. 7, 13-14]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 等长随机方向 DFN 的 D 预测式 (6)：D=(1.665n+35.42L+0.3603nL+678.1)/(n+22.43L+0.1759nL+669.7)，RMSE=0.0152，r>0.999 | [Shaoqun 2024, pp. 5-7] | 区域100m×100m，n=130～970，L=7～95，单次实现 | 残差在 n 小或 L 短时较大 |
| 指数长度随机方向 DFN 的 D 预测式 (9)：D=(1.365n+21.18/λ+0.4364n/λ+122.7)/(n+17.52/λ+0.218n/λ+209.4)，RMSE=0.0141，r>0.999 | [Shaoqun 2024, pp. 7-9] | 相同 n、1/λ 范围，20 个实现取平均 D | 扰动大于等长情况，但平均后拟合良好 |
| 指数长度 von‑Mises 方向 DFN 的 D 预测式 (12)，13 个参数 p₁ ～ p₁₃（p₁=1.619, p₂=34.158, p₃=1.209, p₄=0.344, p₅=0.004, p₆=−0.007, p₇=507.549, p₈=23.151, p₉=1.215, p₁₀=0.169, p₁₁=0.002, p₁₂=−0.008, p₁₃=537.385），RMSE=7×10⁻⁶，r≈1 | [Shaoqun 2024, pp. 9-11] | n=100～900，1/λ=10～80，κ=5～100，μ=π/2，每参数 100 个实现取平均 | D 随 κ 增大而降低；最终预测为期望值 |
| 露头验证：n=35, 1/λ=4, κ=145.18，预测 D=0.99507，网格参数 k=8 时误差 2.3%，k=10 时 0.6%，k=13 时 3.014×10⁻⁷%，k>13 误差极小 | [Shaoqun 2024, pp. 10-11] | 数据来自 Wilson [5]，区域尺寸 100，grid 细分数 k 不同 | 验证了式 (12) 的有效性 |

## Limitations
- 所得方程均为数值拟合的有理函数近似，尚未给出基于物理的解析推导。[Shaoqun 2024, pp. 13-14]
- 该研究仅限于二维裂缝网络，且第三类模型将 von‑Mises 分布的主方向 μ 简化为 π/2。[Shaoqun 2024, pp. 9, 13-14]
- 公式适用于高裂缝密度场景；当裂缝数量少或长度短时，细网格下结构快速扭曲，导致残差增大，相关性减弱。[Shaoqun 2024, pp. 7, 13-14]
- 对于第三类模型，预测值代表随机实现集合的期望 D，并非单次实现的精确值。[Shaoqun 2024, pp. 13-14]

## Assumptions / Conditions
- 研究区域固定为 100 m × 100 m，裂缝密度 P₂₀ = n/10⁴。[Shaoqun 2024, pp. 2-3]
- 裂缝长度分布为固定长度或指数分布；方向为完全随机或 von‑Mises 分布（μ 设为 π/2 以简化分析）。[Shaoqun 2024, pp. 2-3, 9]
- 盒计数 D 的计算采用网格分层层级粗化，网格细分数 k > 10 以保证精度。[Shaoqun 2024, pp. 3-5]
- 为降低随机扰动，拟合所用 D 均取多个 DFN 实现（20 或 100 次）的平均值。[Shaoqun 2024, pp. 7-9, 9-10]
- 建立的多变量关系均假定为有理函数形式，该形式由单变量分析推广而来。[Shaoqun 2024, pp. 5-7]

## Key Variables / Parameters
- **n** — 裂缝数量（可由密度 P₂₀ 换算：n = P₂₀ × 10⁴）。[Shaoqun 2024, pp. 2-3, 5]
- **L** — 固定裂缝长度。[Shaoqun 2024, pp. 5]
- **1/λ** — 指数分布的平均裂缝长度。[Shaoqun 2024, pp. 2-3, 7]
- **κ** — von‑Mises 分布的集中度参数，κ 越大裂缝方向越集中。[Shaoqun 2024, pp. 2-3, 9]
- **μ** — von‑Mises 分布的主方向，本研究简化为 π/2。[Shaoqun 2024, pp. 9]
- **D** — 盒计数分形维数。[Shaoqun 2024, pp. 1-1]
- **k** — 网格细分指数，影响 D 的计算精度。[Shaoqun 2024, pp. 3-5, 11-13]

## Reusable Claims
- 在 100 m × 100 m 区域内，对于等长随机方向 DFN，可用式 (6) 根据 n 和 L 预测 D，相关系数 > 0.999，RMSE ≈ 0.015。[Shaoqun 2024, pp. 5-7]
- 对于指数长度随机方向 DFN，式 (9) 可基于 n 和 1/λ 预测 D，RMSE ≈ 0.014。[Shaoqun 2024, pp. 7-9]
- 对于指数长度 von‑Mises 方向 DFN，式 (12) 可基于 n、1/λ 和 κ 预测 D，RMSE = 7 × 10⁻⁶。[Shaoqun 2024, pp. 9-11]
- 在高裂缝密度条件下，增加 n 或平均长度将增大 D，而增加 κ（方向更集中）将减小 D。[Shaoqun 2024, pp. 13-14]
- 所建立的方程可以替代大量数值模拟，实现分形维数的快速估算；应用时须注意区域尺度换算，且第三类模型给出的是随机实现的期望值。[Shaoqun 2024, pp. 13-14]

## Candidate Concepts
- [[fractal dimension]]
- [[box-counting method]]
- [[fracture network]]
- [[discrete fracture network (DFN)]]
- [[Monte Carlo simulation]]
- [[multivariate analysis]]
- [[exponential fracture length distribution]]
- [[von‑Mises orientation distribution]]
- [[orientation concentration parameter κ]]
- [[percolation threshold]]
- [[fracture network permeability]]

## Candidate Methods
- [[discrete fracture network modeling (marked point processes)]]
- [[hierarchical upscaling for box-counting D calculation]]
- [[rational function fitting of D versus fracture properties]]
- [[multiple‑realization averaging for D estimation]]
- [[outcrop fracture trace validation]]

## Connections To Other Work
- 前人研究多集中于 D 与裂缝密度等单一性质的半定量关系，未给出统一的多变量预测方程。[Shaoqun 2024, pp. 1-2]
- D 与连通性和渗透率的关系已被广泛报道；渗流阈值与 D 及其他参数紧密相关。[Shaoqun 2024, pp. 1-2]
- 针对二维/三维裂缝网络，已有研究表明可借助分形特征预测等效渗透率。[Shaoqun 2024, pp. 1-2]
- 低裂缝密度下 D 的不确定性在文献 [39, 40] 中亦有讨论。[Shaoqun 2024, pp. 13-14]
- 实际验证所用裂缝网络来源于 Wilson [5]。[Shaoqun 2024, pp. 10-11]

## Open Questions
- 如何为式 (6)、(9)、(12) 中的拟合参数赋予明确的物理意义？能否推导出对应的解析公式？[Shaoqun 2024, pp. 13-14]
- 当前二维框架能否推广至三维裂缝网络，并保持相似的多变量有理函数形式？[Shaoqun 2024, pp. 13-14]
- 对于低密度、短裂缝的 DFN，是否存在更稳健的 D 估计方法或修正模型？[Shaoqun 2024, pp. 13-14]

## Source Coverage
本页面整合了所有提供的 12 个非空索引片段，未遗漏任何已索引内容。源文本区块覆盖率 1.0，字符覆盖率 0.940923（编译字符 54152，源字符 57552）。[Coverage audit: indexed_texts 12, coverage_ratio_by_blocks 1.0, coverage_ratio_by_chars 0.940923]
