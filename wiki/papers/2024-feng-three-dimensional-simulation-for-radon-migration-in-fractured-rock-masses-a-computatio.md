---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2024-feng-three-dimensional-simulation-for-radon-migration-in-fractured-rock-masses-a-computatio"
title: "Three-Dimensional Simulation for Radon Migration in Fractured Rock Masses: A Computational Modeling Approach."
status: "draft"
source_pdf: "data/papers/2024 - Three-Dimensional Simulation for Radon Migration in Fractured Rock Masses A Computational Modeling Approach.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Feng, Shengyang, et al. “Three-Dimensional Simulation for Radon Migration in Fractured Rock Masses: A Computational Modeling Approach.” *Rock Mechanics and Rock Engineering*, vol. 57, 2024, pp. 3751-65. doi:10.1007/s00603-024-03766-0."
indexed_texts: "12"
indexed_chars: "59406"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "58906"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.991583"
coverage_status: "full-index"
source_signature: "e5254969f202527c1bbd8c3d9ffd3b616b3a41db"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T08:00:36"
---

# Three-Dimensional Simulation for Radon Migration in Fractured Rock Masses: A Computational Modeling Approach.

## One-line Summary
基于分形离散裂隙网络（DFN）的三维氡迁移数值模型及开源软件 DFNRn 被建立，揭示了裂隙中流体对流主导长距离氡迁移，并分析了裂隙密度逾渗阈值与 DFN 参数及岩体基质参数的关系 [Feng 2024, pp. 1-2, 11-13]。

## Research Question
如何在考虑裂隙与基质双重流动的条件下，准确模拟破碎岩体中的氡迁移，并确定裂隙密度逾渗阈值及其影响因素 [Feng 2024, pp. 2-3, 10-11]。

## Study Area / Data
- 案例研究区：中国衡阳大浦退役铀矿附近，破碎岩体露头宽 25 m、高 19 m，含 145 条裂隙 [Feng 2024, pp. 5-7]。
- 露头裂隙参数由实测拟合得到：Df = 1.62，a = 2.39，α = 1.49，平均方位角 86.4°，Fisher 常数 5.24，平均裂隙开度 1.7 mm，最小/最大开度 0.5/3.6 mm [Feng 2024, pp. 7, Table 1]。
- 面裂隙强度 P21 = 0.37 m⁻¹，经换算体积裂隙密度 P32 = 0.41 m⁻¹ [Feng 2024, pp. 7-8]。
- 模型域尺寸 100 m，底部边界氡浓度设为 3.7×10⁵ Bq/m³，顶部为流出边界；基质渗透率 8.7×10⁻¹³ m²，孔隙度 0.2，基质氡扩散系数 1.1×10⁻⁸ m²/s [Feng 2024, pp. 7-8]。

## Methods
- **裂隙网络生成**：采用双幂律模型描述裂隙空间分布与长度，使用倍增级联过程（multiplicative cascade method）在三维空间确定裂隙位置，具体给出 8 子域概率分配、迭代生成概率密度图及随机向量映射坐标的方法 [Feng 2024, pp. 3-4]。
- **裂隙属性**：方位采用 von Mises–Fisher 分布；开度采用对数正态分布（Baghbanan and Jing, 2007），以误差函数及逆误差函数生成随机开度 [Feng 2024, pp. 4-5]。
- **控制方程**：裂隙中氡迁移方程包含扩散、对流、衰变及与基质交换的垂直通量项（式 5），流体流动用达西定律（式 6）；基质中氡迁移方程包含源项 A = λ E R ρ_b（式 7），基质渗流速度由达西定律给出（式 8），界面通量守恒 J = -J’ [Feng 2024, pp. 5-7]。
- **数值实现**：开源软件 DFNRn（Discrete Fracture Network model for Radon migration），利用 MATLAB 通过 LiveLink 生成 3D DFN 并导入 COMSOL Multiphysics，椭球形裂隙离散为四面体网格，有限元法求解；软件代码公开在 GitHub 上 [Feng 2024, pp. 5-7]。
- **重复计算稳定化**：因随机裂隙网络导致结果波动，默认每个模型运行 8 次取平均，以变异系数 CV≤10% 为稳定判据 [Feng 2024, pp. 10]。

## Key Findings
- 无压力差时，仅靠扩散氡无法到达地表，计算的平均氡析出率仅 3.66×10⁻⁵ Bq/m²/s，远低于实测 (4.53±0.62)×10⁻³ Bq/m²/s；施加 944 Pa 压力差后模拟结果与实测一致，验证模型精度 [Feng 2024, pp. 8-9]。
- 裂隙内流体对流主导氡迁移：裂隙最大氡析出率 0.054 Bq/m²/s，基质最大仅 0.0033 Bq/m²/s，相差 15.4 倍 [Feng 2024, pp. 9]。
- 时间演化：裂隙出口最大氡浓度 1.1 天后开始显著上升并稳定于 44039 Bq/m³（7.2 天），基质出口浓度仅 5602 Bq/m³（5.5 天），稳定时间延长 31％，表明裂隙对流加速运移 [Feng 2024, pp. 9-10]。
- 裂隙密度逾渗阈值 P'₃₂ 与分形维度 Df 关系：1.4≤Df≤1.9 时，P'₃₂ 随 Df 线性下降；Df≤1.3 时无逾渗 [Feng 2024, pp. 11-12]。
- 长度指数 a 在 1.2≤a≤2.8 时 P'₃₂ 变化微弱（0.30–0.38 m⁻¹），a≥2.9 时无逾渗 [Feng 2024, pp. 11-12]。
- 归一化常数 α：1≤α≤1.8 时 P'₃₂ 随 α 增加而下降，α>1.8 后变化极小 [Feng 2024, pp. 12-13]。
- 平均方位角 ω：当 ω<25° 时无裂隙连通（即使生成 40000 条裂隙）；25°≤ω≤40° 时 P'₃₂ 线性下降；60°<ω≤70° 时出现显著下降；与 Fisher 常数 κ 无相关 [Feng 2024, pp. 12-13]。
- 基质参数敏感性：氡源项 A 对析出率影响最大，其次为渗透率 k，扩散系数 D 影响最小；这与均匀介质模型结论相反 [Feng 2024, pp. 13]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 无对流时平均氡析出率 3.66×10⁻⁵ Bq/m²/s，实测 (4.53±0.62)×10⁻³ Bq/m²/s；加 944 Pa 后模拟值与实测一致 | [Feng 2024, pp. 8-9] | 域尺寸 100 m，底部浓度 3.7×10⁵ Bq/m³，基质渗透率 8.7×10⁻¹³ m²，孔隙度 0.2 | 压力差由理想气体状态方程推算为 1033.2 Pa，相对偏差 8.6% |
| 裂隙最大析出率 0.054 Bq/m²/s，基质 0.0033 Bq/m²/s，相差 15.4 倍 | [Feng 2024, pp. 9] | 同上压力差条件 | 表明裂隙对流主导 |
| 裂隙出口浓度 1.1 天后迅速上升，基质出口 5.5 天稳定，稳定时间延长 31% | [Feng 2024, pp. 9-10] | 对流速度 90.9 m/d，基质渗流速度 4.5×10⁻⁷ m/s | 裂隙对流速度远大于基质渗流 |
| P'₃₂ 随 Df 减小：Df=1.4 至 1.9，线性下降；Df=1.3 无逾渗 | [Feng 2024, pp. 11-12] | 其他参数同案例，域尺寸 10 m，温压梯度 0.3°C | 子程序 connectFrac 计算连通度 |
| P'₃₂ 在 1.2≤a≤2.8 时近乎不变 (0.30–0.38)；a=2.9 无逾渗 | [Feng 2024, pp. 11-12] | 同上 |  |
| P'₃₂ 随 α 增加在 α≤1.8 时下降，α>1.8 基本不变，≈0.2 m⁻¹ | [Feng 2024, pp. 12-13] | 同上 |  |
| P'₃₂ 随 ω 变化：ω<25° 无连通，25°≤ω≤40° 线性下降，60°<ω≤70° 显著下降；与 κ 无关 | [Feng 2024, pp. 12-13] | 同上 |  |
| 基质参数：A 影响最大，k 次之，D 最小；与均匀模型相反 | [Feng 2024, pp. 13] | 例中其他参数同 Sect.3 | 推测基质渗透率增高使更多氡进入裂隙对流 |

## Limitations
- 三维裂隙生成基于倍增级联法的一阶模型，未探讨更高阶或其它随机过程 [Feng 2024, pp. 3-4]。
- 裂隙开度假设为对数正态分布，未采用开度‑长度相关模型（文中指出相关性并非普适）[Feng 2024, pp. 4]。
- 裂隙形状简化为椭圆盘，未考虑更复杂的多边形形态 [Feng 2024, pp. 4-5]。
- 压力差计算借用理想气体定律，气体密度需假设为常数，精度受此假设影响 [Feng 2024, pp. 9]。
- 逾渗阈值分析采用 10 m 小模型，结论的尺度外推性未验证 [Feng 2024, pp. 10]。
- 对基质参数影响的分析未考虑裂隙开度分布变化及基质非均质性 [Feng 2024, pp. 13]。
- 所有模拟基于稳态流动假设（除时序分析），未涉及瞬态压力或温度变化 [Feng 2024, pp. 5]。
- 软件自动重复运行 8 次的稳定性判据基于变异系数 10%，未给出敏感性分析 [Feng 2024, pp. 10]。

## Assumptions / Conditions
- 裂隙内无镭，氡源全部由基质提供（仅基质含源项 A）[Feng 2024, pp. 5]。
- 裂隙中流体为单相不可压缩，流态满足达西定律 [Feng 2024, pp. 5]。
- 基质被视为均质多孔介质，渗透率和孔隙度恒定 [Feng 2024, pp. 7]。
- 模型域底部氡浓度恒定，顶部为流出边界 [Feng 2024, pp. 7]。
- 温度梯度小，气体密度近似常数，压力差可用 ΔP = ρ R_g ΔT 估算 [Feng 2024, pp. 9]。
- 裂隙生成采用双幂律分布，空间位置由倍增级联法一阶过程确定，l_ratio = 2, m=8 [Feng 2024, pp. 3-4]。
- Fisher 分布描述方位 [Feng 2024, pp. 4]。

## Key Variables / Parameters
- **裂隙网络参数**：分形维数 Df、长度指数 a、归一化常数 α、平均方位角 ω、Fisher 常数 κ、裂隙开度分布（μ, σ, min, max）、体积密度 P32、面密度 P21 [Feng 2024, pp. 3-4, 7-8, Table 1]。
- **物理参数**：裂隙/基质中氡扩散系数 D/D′、有效衰变常数 λ=2.1×10⁻⁶ s⁻¹、基质孔隙度 ε、基质渗透率 k、氡源项 A = λ E R ρ_b、流体粘度 μ [Feng 2024, pp. 5, 7]。
- **逾渗阈值 P'₃₂**：定义为裂隙连通底部至顶部的临界体积密度 [Feng 2024, pp. 10-11]。
- **压力差 ΔP**：由理想气体定律 ΔP = ρ R_g ΔT 近似 [Feng 2024, pp. 9]。
- **氡析出率**：出口面氡通量，用于验证与敏感性分析 [Feng 2024, pp. 8-9, 12-13]。

## Reusable Claims
- 基于分形 DFN 的氡迁移模型（DFNRn）在加入对流后能准确复现实测氡析出率，压力差可通过温度梯度与理想气体定律估算，为无实测压力差时提供初始值 [Feng 2024, pp. 8-9]。
- 裂隙内流体对流是长距离氡迁移的主导机制，扩散贡献可忽略，因此仅当裂隙连通（P32 > P'₃₂）时模型需考虑裂隙；均匀介质模型会严重低估运移量 [Feng 2024, pp. 9-10]。
- 裂隙体积密度逾渗阈值 P'₃₂ 与 Df（1.4-1.9）呈负相关，与 a（1.2-2.8）基本无关，与 α（≤1.8）负相关，与 ω 负相关（尤其当方位接近渗流方向时），与 κ 无关 [Feng 2024, pp. 11-12]。
- 基质参数中，氡源项是影响析出率的最主要因素，渗透率影响大于扩散系数，与均匀介质模型结论相悖，原因在于增大基质渗透率促使更多氡进入裂隙对流 [Feng 2024, pp. 13]。
- 为保证随机裂隙网络模拟的稳定性，建议每个参数集至少重复运行 8 次取平均 [Feng 2024, pp. 10]。

## Candidate Concepts
- [[fractal discrete fracture network]] (DFN) 三维生成
- [[multiplicative cascade process]] 确定裂隙位置
- [[radon migration in fractured rock mass]]
- [[percolation threshold of fracture density]] P'₃₂
- [[fracture connectivity index Cf]]
- [[dual-power-law model]] for fracture length & spatial distribution
- [[radon exhalation rate prediction]]
- [[radon convection vs. diffusion dominance]]
- [[COMSOL-MATLAB LiveLink coupling]]

## Candidate Methods
- [[DFNRn open-source software]] 3D DFN 氡迁移模拟
- [[multiplicative cascade method for fracture location]] 详细步骤
- [[finite element modeling of coupled fracture-matrix radon transport]]
- [[repeat-run averaging for stochastic DFN stability]]
- [[connectFrac subroutine for connectivity threshold]]
- [[ideal gas law ΔP estimation for subsurface radon convection]]

## Connections To Other Work
- 双幂律模型源自 Davy et al. (1990)，本文扩展至 3D 并用于氡迁移 [Feng 2024, pp. 3-4]。
- 倍增级联过程借鉴 Kim and Schechter (2009)、Verscheure et al. (2012) 等的 2D 方法，首次详述 3D 实现 [Feng 2024, pp. 3]。
- 裂隙开度对数正态分布基于 Baghbanan and Jing (2007) [Feng 2024, pp. 4]。
- 传统氡迁移方程参考 Rogers and Nielson (1991) 及 Chauhan et al. (2014)，本文在裂隙中替换源项为基质通量 [Feng 2024, pp. 5]。
- 实测氡析出率验证方法与 Jonassen (1983)、Hong et al. (2022) 一致 [Feng 2024, pp. 8]。
- 裂隙对流主导的结论与 Richon et al. (2010) 一致 [Feng 2024, pp. 9]。
- 先前 2D 分形 DFN 氡迁移研究（Feng et al. 2020, 2021）通过一维管道简化，本文首次实现 3D 椭圆盘裂隙与基质耦合模拟 [Feng 2024, pp. 4-5]。

## Open Questions
- 模型尚需通过更多不同地质背景（如地震断裂带、火山区域）的实测数据进行验证 [Feng 2024, pp. 14]。
- 裂隙开度与长度相关性假设的影响需进一步探索，因文献证据并不统一 [Feng 2024, pp. 4]。
- 瞬态非达西流或裂隙变形耦合对氡迁移的作用尚未纳入 [未在碎片中明确，但作为开放问题合理]。
- 逾渗阈值与 DFN 参数的关系在小尺度（10 m）获得，其结果能否推广至千米级工程尺度仍需检验 [Feng 2024, pp. 10]。
- 基质非均质性（如分层、侵入体）对氡源项分布和迁移路径的影响亟待研究 [未在碎片中讨论，但属潜在问题]。
- 软件虽开源，但其计算效率在处理数万级裂隙时的表现未见定量报告 [Feng 2024, pp. 5-7]。

## Source Coverage
All non-empty indexed fragments were processed: 12 source blocks from pp. 1-15, total chars 58906 (coverage ratio by chars 0.9916; block coverage 1.0). No fragments omitted. Data extracted exclusively from [Feng 2024, pp. 1-15].
