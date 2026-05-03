---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-chen-equivalent-permeability-distribution-for-fractured-porous-rocks-correlating-fracture-a"
title: "Equivalent Permeability Distribution for Fractured Porous Rocks: Correlating Fracture Aperture and Length."
status: "draft"
source_pdf: "data/papers/2020 - Equivalent Permeability Distribution for Fractured Porous Rocks Correlating Fracture Aperture and Length.pdf"
collections:
citation: "Chen, Tao. \"Equivalent Permeability Distribution for Fractured Porous Rocks: Correlating Fracture Aperture and Length.\" *Geofluids*, vol. 2020, 2020, article 8834666, 12 pp., doi:10.1155/2020/8834666."
indexed_texts: "11"
indexed_chars: "54860"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "55078"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003974"
coverage_status: "full-index"
source_signature: "74887d713624c2a9239d02c55cdd49847d24e67c"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T02:25:03"
---

# Equivalent Permeability Distribution for Fractured Porous Rocks: Correlating Fracture Aperture and Length.

## One-line Summary
本研究定量分析了裂缝长度与开度关联模型对裂缝性多孔岩石等效渗透率分布的影响，揭示了等效渗透率张量分布随关联指数和裂缝几何参数变化的统计规律，并建立了平均等效渗透率与关联指数的指数关系以及渗透率与裂缝密度的幂律关系。 [Chen 2020, pp. 1-2]

## Research Question
裂缝长度与开度之间的关联关系如何制约大尺度裂缝性多孔介质网格块的等效渗透率分布？此前研究多关注单一网格块的等效渗透率，而“correlated length and aperture on equivalent permeability distributions of grid blocks for large-scale fractured porous media has yet to be clarified” [Chen 2020, pp. 2-2]。

## Study Area / Data
本研究使用合成数据，非特定研究区。二维离散裂缝网络生成于L = 20 m的正方形域。裂缝长度服从截断幂律分布，幂指数 a = 2.5，下界 l_min 分别取 4 m、6 m、8 m、10 m，上界 l_max = 40 m。裂缝数量 N 为 50、75、100、125。开度与长度遵循 w = γ l^D，其中 γ = 1.2×10^{-4}，关联指数 D 从 0.5 到 1.0（步长 0.1）。裂缝位置和产状假设为纯随机均匀。共生成16组几何参数组合，每组10次实现，总计960个离散裂缝模型。 [Chen 2020, pp. 2-3] [Chen 2020, pp. 3-5]

## Methods
1. **离散裂缝模型生成**：基于 Monte Carlo 方法和 ADFNE 软件生成具有关联开度‑长度的二维裂缝网络。裂缝长度服从幂律分布，开度按 w = γ l^D 给定。D 从 0.5（恒断裂韧度）到 1.0（恒驱动应力）代表不同力学状态。 [Chen 2020, pp. 2-3] [Chen 2020, pp. 3-5]
2. **等效渗透率升尺度**：将裂缝网格细分到 2 m×2 m Cartesian 网格，采用多重边界升尺度方法。对每个网格块分别沿 x 和 y 方向施加线性边界条件，求解稳态渗流，通过 Darcy 定律反算等效渗透率张量 k_xx、k_yy、k_xy。基质渗透率固定为 k_m = 1 md，裂缝渗透率由立方律 k_f = w^2/12 计算。流动方程采用多点通量近似（MPFA），利用 MRST 代码求解，并与全穿透裂缝解析解进行验证。 [Chen 2020, pp. 3-5]

## Key Findings
1. 当 D=0.5 时，随着 l_min 和 N 增大，对角线等效渗透率分量由幂律分布向对数正态分布、再向正态分布过渡；D 增大时该过渡减缓，主要因为非均质性增强。 [Chen 2020, pp. 9-10]
2. 平均无量纲等效渗透率 〈k'〉 与关联指数 D 满足指数关系 〈k'〉 = A·10^{B·D}，系数 A、B 随 l_min 和 N 增大而增大。 [Chen 2020, pp. 5-7]
3. 〈k'〉 与无量纲裂缝密度 ρ（∑ (l_i/2)^2 / A）遵循幂律 〈k'〉 = β·ρ^C；幂指数 C 约 1.1–1.3，系数 β 和 C 随 D 增大而增大。 [Chen 2020, pp. 7-9]
4. 关联指数 D 增大时，渗透率各向异性增强（渗透率椭圆长/短轴比增加）。 [Chen 2020, pp. 9-10]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 对角线等效渗透率分布随 l_min、N 增加发生幂律→对数正态→正态过渡；过渡速度随 D 增大而变慢 | [Chen 2020, pp. 5-5, 9-10] | 2D DFN，D∈[0.5,1]，l_min∈[4,10] m，N∈[50,125]，随机产状 | 结论(1)、(2) |
| log(〈k'〉) 与 D 呈线性关系，可用指数函数拟合 | [Chen 2020, pp. 5-7] | γ=1.2×10^{-4}，a=2.5，l_max=40 m | 系数 A~10^{1.4}–10^{2.4}，B~3.4–4.3 |
| log(〈k'〉) 与 log(ρ) 呈线性关系，可用幂律拟合 | [Chen 2020, pp. 7-9] | 不同 D 下所有几何构型 | C≈1.1–1.3，β 随 D 增大 |
| 等效渗透率各向异性随 D 增大而增强 | [Chen 2020, pp. 9-10] | 基于渗透率张量椭圆 | 图10 |

## Limitations
- 开度模型仅为经验幂律（w = γ l^D），未考虑应力等力学本构关系，实际裂缝开度受地应力影响显著。 [Chen 2020, pp. 9-10]
- 所有分析基于二维离散裂缝网络，是三维真实情况的简化，向三维推广需要更复杂的几何数据和计算平台。 [Chen 2020, pp. 9-10]
- 裂缝产状假设为均匀随机，未考虑成簇、分带等非均质分布。 [Chen 2020, pp. 2-3]

## Assumptions / Conditions
- 岩石基质渗透率恒为 k_m = 1 md。 [Chen 2020, pp. 3-5]
- 裂缝长度服从截断幂律分布，指数 a = 2.5，l_min∈[4,10] m，l_max=40 m。 [Chen 2020, pp. 2-3]
- 裂缝开度与长度关联为 w = γ l^D，γ=1.2×10^{-4}。 [Chen 2020, pp. 2-3]
- 裂缝产状和位置为纯随机、均匀分布。 [Chen 2020, pp. 3-5]
- 升尺度网格尺度为 2 m×2 m，采用多重边界法。 [Chen 2020, pp. 3-5]

## Key Variables / Parameters
- D：开度‑长度关联指数（0.5–1.0）
- l_min：最小裂缝长度（4 m，6 m，8 m，10 m）
- N：裂缝数量（50，75，100，125）
- k_xx, k_yy, k_xy：等效渗透率张量分量
- 〈k'〉：平均无量纲等效渗透率（归一化至 k_m）
- ρ：无量纲裂缝密度（∑ (l_i/2)^2 / A）
- 指数模型系数：A，B
- 幂律模型系数：β，C

## Reusable Claims
1. 在二维随机裂缝性多孔岩石中，若开度‑长度遵循 w = γ l^D（γ=1.2×10^{-4}，D=0.5），增加最小裂缝长度和裂缝数量会使对角线等效渗透率分量从幂律分布转向对数正态进而正态分布；对于 D>0.5 的情形，该过渡因非均质性增强而减缓。 [Chen 2020, pp. 5-5, 9-10]
2. 平均无量纲等效渗透率与关联指数 D 可用指数函数 〈k'〉 = A·10^{B·D} 描述，其中 A 和 B 随 l_min 和 N 增大而增大（条件：γ=1.2×10^{-4}，a=2.5，l_min≤10 m，N≤125，基质渗透率 1 md）。 [Chen 2020, pp. 5-7]
3. 对于关联开度‑长度模型，平均无量纲等效渗透率与无量纲裂缝密度 ρ 满足幂律 〈k'〉 = β·ρ^C，C 约 1.1–1.3，且 β 和 C 均随 D 增大而增大，表明裂缝密度与开度模型对等效渗透率存在交互影响。 [Chen 2020, pp. 7-9]
4. D 越高，裂缝网络的渗透率各向异性越强（渗透率椭圆长/短轴比越大）。 [Chen 2020, pp. 9-10]

## Candidate Concepts
- [[等效渗透率分布]]
- [[裂缝开度-长度关联]]
- [[多重边界升尺度方法]]
- [[幂律裂缝长度分布]]
- [[无量纲裂缝密度]]
- [[渗透率张量各向异性]]
- [[离散裂缝网络模型]]
- [[关联指数D]]
- [[指数函数渗透率模型]]
- [[幂律渗透率-密度关系]]

## Candidate Methods
- [[Monte Carlo 离散裂缝网络生成]]
- [[多重边界升尺度方法]]
- [[ADFNE 开源软件]]
- [[MRST 油藏模拟工具箱]]
- [[多点通量近似（MPFA）]]
- [[渗透率张量椭圆分析]]
- [[Spearman 秩相关系数评估]]

## Connections To Other Work
- Klimczak 等（2010）确认了裂缝长度‑开度关联的立方律对网络尺度流的重要性；本研究将关注点从单一网格块拓展到网格块等效渗透率分布，进一步证实其影响。 [Chen 2020, pp. 2-2, 7-7]
- Leung 和 Zimmerman（2012）提出基于几何参数估计宏观水力传导系数的方法，本研究发现〈k'〉与ρ的幂律指数接近 1，与其线性相关的结论一致。 [Chen 2020, pp. 7-7]
- Bisdom 等（2016）指出不同开度模型对等效渗透率的影响取决于基质渗透率；本研究在考虑 1 md 基质渗透率条件下得到长度‑开度模型显著影响渗透率幅值的结论，与之相符。 [Chen 2020, pp. 5-5, 7-7]
- 本研究采用的多重边界升尺度方法源自 Chen 等（2015），并被用于三维裂缝性岩石的渗透率研究（Chen 等，2018），提供了稳健的升尺度框架。 [Chen 2020, pp. 3-5]

## Open Questions
- 若采用其他开度分布（如对数正态、基于应力‑力学本构的开度模型），等效渗透率的统计分布将如何改变？ [Chen 2020, pp. 9-10]
- 二维结果向三维推广时，关联开度‑长度模型对等效渗透率分布的影响规律是否保持一致？需要真实裂缝几何数据和高效计算平台支撑。 [Chen 2020, pp. 9-10]
- 在裂缝产状非均匀（如成簇、应力定向）条件下，本文所揭示的分布过渡规律是否依然成立？ [Chen 2020, pp. 2-3]

## Source Coverage
所有 11 个非空索引片段均已处理。源文本覆盖率：按文本块计 100%，按字符计 100.4%（compiled_source_chars 55078，indexed_chars 54860）。源文件签名：74887d713624c2a9239d02c55cdd49847d24e67c，覆盖状态：full-index。
