---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2016-maillot-connectivity-permeability-and-channeling-in-randomly-distributed-and-kinematically"
title: "Connectivity, Permeability, and Channeling in Randomly Distributed and Kinematically Defined Discrete Fracture Network Models."
status: "draft"
source_pdf: "data/papers/2016 - Connectivity, permeability, and channeling in randomly distributed and kinematically defined discrete fracture network models.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Maillot, J., et al. \"Connectivity, Permeability, and Channeling in Randomly Distributed and Kinematically Defined Discrete Fracture Network Models.\" *Water Resources Research*, vol. 52, 2016, pp. 8526-8545. doi:10.1002/2016WR018973."
indexed_texts: "20"
indexed_chars: "95732"
nonempty_source_blocks: "20"
compiled_source_blocks: "20"
compiled_source_chars: "96207"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004962"
coverage_status: "full-index"
source_signature: "81470be7ee25c56a54ca8def39557b6fa9b32259"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T16:22:02"
---

# Connectivity, Permeability, and Channeling in Randomly Distributed and Kinematically Defined Discrete Fracture Network Models.

## One-line Summary
比较了泊松离散裂隙网络（DFN）与基于运动学生长规则的DFN在连通性、渗透率与流动通道化上的差异，发现运动学模型渗透率系统性偏低、通道化更强，且阈值密度高出约50%。

## Research Question
当裂缝具有相同的统计密度、长度和方位分布时，与经典的泊松（空间随机）DFN相比，由简化的成核、生长和停止规则生成的运动学DFN模型在连通性、渗透率和流动结构（尤其是通道化）方面有何差异？传统泊松假设是否会导致对流动性质的系统性高估？[Maillot 2016, pp. 1-1, 1‑2]

## Study Area / Data
本研究基于合成三维DFN模型，未使用特定野外场地。所有网络均由盘状裂缝构成，长度服从指数为‑4的幂律分布（幂律指数 a=4，即 n(l) ∝ l⁻⁴）。裂缝方位各向同性。模型域为立方体，生成域边长 L_G=15，分析子域边长 L=10（以最小裂缝长度 l_min=1 度量）。针对4种运动学模型和对应的4种等效泊松模型，每种统计获得超过1000次蒙特卡洛实现。透水性先设为全裂缝恒定，后扩展为对数正态分布（标准差 σ=0~2），且单裂缝内导水系数视为均匀。[Maillot 2016, pp. 1-1, 2‑3, 3‑5, 5‑6, 6‑7, 7‑8]

## Methods
- **泊松模型（PM）**：裂缝位置独立随机，具有与运动学模型相同的密度、长度和方位分布 [Maillot 2016, pp. 1-2, 2‑3]。
- **运动学裂缝模型（KFM）**：基于 Davy et al. (2010, 2013) 的简化运动学规则——裂缝经历成核（随机位置与方位）、生长（Charles 定律，dℓ/dt = C ℓ^a，取 C=1, a=3）和停止（仅当遇到更大裂缝时停止）。考虑两种停止模式（A：最多一个 T 终止；B：最多两个 T 终止）和两种生长模式（顺序 S：低的成核率；竞争 C：高的成核率），组合得到 KFMAS、KFMAC、KFMBS、KFMBC 四种变体 [Maillot 2016, pp. 2-3, 3‑5, 5‑6]。
- **指标体系**：用面密度 p₃₂（总裂缝面积/体积）、逾渗参数 p、主干密度 d_b、流动通道化密度指标 d_Q 和功率平均指数 ω 等量化几何与水力性质 [Maillot 2016, pp. 5-6]。
- **流动模拟**：采用 H2OLAB 平台的混和有限元法，施加渗透计式边界条件（对面定水头 h=1, h=0，其余面隔水），网格分辨率大于最小裂缝长度和 T 形交叉，交叉小于网格的部分被移除 [Maillot 2016, pp. 6-7]。

## Key Findings
1. **连通性差异**：相同 p₃₂ 下，运动学模型的交叉数量比泊松模型少约 1.6~2 倍；运动学模型中 T 形交叉占比达 60%~94%，而泊松模型全为 X 形交叉 [Maillot 2016, pp. 7-8, 8‑9]。
2. **渗透率对比**：恒定导水系数时，运动学模型的渗透率系统性低于等效泊松模型，幅度为 1.5~10 倍（AS 型模型接近逾渗阈值时差异最大）。渗透率与 p₃₂ 呈线性关系，但运动学模型的表观阈值 p_Qc ≈ 1.5，比泊松模型的 p_Qc ≈ 1.14 高出约 50% [Maillot 2016, pp. 9-11, 17‑18]。
3. **流动主干与通道化**：
   - 高密度泊松模型的主干密度占 p₃₂ 的 73%~93%，而低密度运动学模型（AS）仅约 30%。主干密度不能完全解释渗透率差别 [Maillot 2016, pp. 11-12]。
   - 引入通道化指标 d_Q（加权流动的有效面积密度），运动学模型的 d_Q 比泊松模型小 1.5~3 倍，表明流动更集中于少数通道 [Maillot 2016, pp. 12-13]。
   - 对所有模型，渗透率 K 与 d_Q 在低密度下近似呈二次方关系（K ≈ 1.5 d_Q²），高密度下趋近线性 [Maillot 2016, pp. 13-15]。
4. **导水系数变异的影响**：引入对数正态导水系数分布（σ 从 0 到 2），渗透率仅略有增加，但通道化增强。运动学模型的功率平均指数 ω 为负值（‑0.5~0），反映串联控制；泊松模型的 ω 为正（0.1~0.25），偏并联或几何平均。这说明运动学网络对低导水裂缝更敏感 [Maillot 2016, pp. 13-15, 15‑16]。
5. **靠近逾渗阈值的行为**：最低密度的 KFMAS 模型表现出临界特性（如关系非线性），且运动学模型的逾渗阈值附近行为与经典逾渗理论（平方律）偏离较大 [Maillot 2016, pp. 9-11, 16‑17]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 运动学模型的渗透率比等效泊松模型低 1.5~10 倍；对于相同的统计性质，运动学模型的渗透率总是更低。 | [Maillot 2016, pp. 1-1, 9‑11, 17‑18] | 恒定裂缝导水系数；密集区裂隙长度分布指数 ‑4。 | AS 模型（密度最低）差异可达一个数量级。 |
| 渗透率与 p₃₂ 呈线性关系：对 PM，K = 0.46 (p₃₂ − 1.14)；对 KFM，K = 0.40 (p₃₂ − 1.50)。 | [Maillot 2016, pp. 9-11] | 同上，尺寸 L=10，各向同性方位。 | KFM 的阈值密度高出约 50%。 |
| 交叉数量 N_i 与 p₃₂ 线性相关：N_i = k (p₃₂ − d_C)，PM 的 k=0.33，KFM 的 k=0.215；每个裂缝的平均交叉数 I_F(l) 在 KFM 中约为 PM 的 1/2。 | [Maillot 2016, pp. 8-9] | 所有模型；长度分布指数 ‑4。 | 差异随密度增大而增大。 |
| 运动学模型中 T 形交叉占比为 60%~94%（顺序模式 >90%，竞争模式 66%~74%）。 | [Maillot 2016, pp. 7-8, 8‑9] | 四种 KFM 变体。 | 泊松模型全为 X 交叉。 |
| 流动通道化指标 d_Q = (1/V) (∑ S_f Q_f)² / (∑ S_f Q_f²)，d_Q 表示有效流动面积密度。对于 PM，d_Q 约为 p₃₂ 的 1/4~1/3；对于 KFM，约为 p₃₂ 的 1/10~1/5。 | [Maillot 2016, pp. 12-13] | 恒定导水系数；所有模型。 | d_Q 越小通道化越强。 |
| 渗透率与 d_Q 的关系对所有模型近似统一：K ≈ 1.5 d_Q²（低密度）或 K ≈ 1.4 (d_Q − 0.25)（高密度）。 | [Maillot 2016, pp. 12-15] | 恒定导水系数。 | KFMAS 偏离线性较远，二次方关系更适合。 |
| 引入对数正态导水系数分布（σ=0~2），渗透率变化不大；运动学模型的功率平均指数 ω 为 ‑0.5~0，PM 为 0.1~0.25。 | [Maillot 2016, pp. 13-16] | 各模型，σ 至多 2。 | ω 负数表示流动受低导水系数控制（串联特征）。 |
| KFMBS/KFMBC 的主干密度占 p₃₂ 的 90%~95%，PMBS/PMBC 占 73%~93%，而 KFMAS 仅约 29%。 | [Maillot 2016, pp. 11-12, 12‑13] | 恒定导水系数。 | 主干密度差异不能完全解释渗透率差别。 |

## Limitations
- 仅分析了密集区（> l_c）的裂隙，未考虑稀疏区对渗透率的贡献。稀疏区贡献被认为较小，但未直接验证 [Maillot 2016, pp. 3-5]。
- 流动模拟中假设单裂缝内导水系数均匀，仅研究了恒定或对数正态分布，且未与裂隙长度建立相关性。然而，研究指出系统尺寸大于孔径相关长度的约 20 倍时该假设可接受，但实际天然系统的相关长度可能未知 [Maillot 2016, pp. 5-6]。
- 未深入探索域尺寸 L、T 交叉尺寸以及成核分布非均匀性的影响。成核位置在文中为均匀随机，但真实情况受应力影响 [Maillot 2016, pp. 16-17]。
- 通道化指标 d_Q 基于裂隙总流量定义，不考虑裂隙平面内的流动非均匀性，因此是对实际流动密度的上限估计 [Maillot 2016, pp. 16-17]。
- 逾渗阈值附近的行为基于有限的 p 值（均大于 pc）外推，未直接模拟接近 pc 的网络，结论具有不确定性 [Maillot 2016, pp. 9-11, 16‑17]。
- 四种运动学模型仅代表个别参数组合，更广泛的参数空间（如生长指数、成核率谱）的影响尚未讨论 [Maillot 2016, pp. 3-5, 16‑17]。

## Assumptions / Conditions
- 三维盘形裂缝，长度分布为指数 ‑4 的密集区幂律（a=4）[Maillot 2016, pp. 3-5]。
- 裂缝方位各向同性，成核位置均匀随机 [Maillot 2016, pp. 3-5]。
- 生长服从 Charles 定律 (dℓ/dt = C ℓ^a)，C=1, a=3 [Maillot 2016, pp. 2-3, 3‑5]。
- 停止规则：小裂缝遇到大裂缝即停止（A 模式 1 个 T 终止，B 模式最多 2 个 T 终止）[Maillot 2016, pp. 2-3]。
- 分析限于 l_c 以上的密集区，去除小于 l_min=1 的裂缝，L=10 [Maillot 2016, pp. 5-6]。
- 单裂缝内导水系数恒定，且全裂缝恒定（初始情况）或服从独立同分布的对数正态分布 [Maillot 2016, pp. 5-6]。
- 流动边界：对面定水头，其余面隔水，即渗透计式条件 [Maillot 2016, pp. 6-7]。
- 等效泊松模型具有与相应 KFM 相同的密度、长度和方位分布，仅空间结构不同 [Maillot 2016, pp. 5-6]。
- 统计结果基于每种模型超过 1000 次实现 [Maillot 2016, pp. 6-7]。

## Key Variables / Parameters
- **p₃₂**：面密度（总裂缝面积/体积）[Maillot 2016, pp. 5-6]。
- **p**：逾渗参数（与缝长三次方加权有关）[Maillot 2016, pp. 5-6]。
- **n_I**：交叉总数，**I_F(l)**：长度为 l 的裂缝的平均交叉数 [Maillot 2016, pp. 8-9]。
- **T 交叉比例**：T 形交叉占总交叉的百分比 [Maillot 2016, pp. 8-9]。
- **等效渗透率 K_eq**（或 K）[Maillot 2016, pp. 9-11]。
- **主干密度 d_b**：参与流动的裂缝总面积/体积 [Maillot 2016, pp. 11-12]。
- **流动通道化密度 d_Q**：按流量加权的有效流动面积密度 [Maillot 2016, pp. 12-13]。
- **功率平均指数 ω**：衡量导水系数分布的平均方式（‑1 和 1 之间）[Maillot 2016, pp. 13-15]。
- **σ**：对数导水系数的标准差 [Maillot 2016, pp. 13-15]。
- **l_min**、L：最小裂缝长度和系统尺度（基准长度和导水系数用于无量纲化）[Maillot 2016, pp. 5-6]。

## Reusable Claims
1. 在相同的长度分布、密度和方位下，基于运动学规则（含 T 形交叉）的 DFN 的渗透率比空间随机（泊松）DFN 低 1.5~10 倍；密度越低，差异越大 [Maillot 2016, pp. 1-1, 9‑11, 17‑18]。
2. 渗透率与面密度 p₃₂ 近似线性，但运动学网络的表观逾渗阈值比泊松网络高出约 50%，且线性参数不同 [Maillot 2016, pp. 9-11]。
3. 流动通道化指标 d_Q 可统一描述渗透率与有效流动面积的关系：K ≈ 1.5 d_Q²（低密度）或 K ≈ 1.4 (d_Q − 0.25)（高密度），且该关系对模型类型不敏感 [Maillot 2016, pp. 12-15]。
4. 运动学 DFN 的通道化更强：d_Q 仅为泊松模型的 1/3~1/1.5；主干中高死端比例和串联型流动结构是其内在原因 [Maillot 2016, pp. 9-10, 12‑13, 15‑16]。
5. 当裂缝导水系数存在变异时，运动学网络的功率平均指数 ω 倾向于负值（‑0.5~0），表明流动结构更接近串联，对低导水裂缝敏感；泊松网络的 ω 为 0.1~0.25，接近并联-几何平均 [Maillot 2016, pp. 15-16]。
6. 裂缝交叉数量与 p₃₂ 线性相关，且运动学模型的交叉效率低于泊松模型（每单位 p₃₂ 产生的交叉数少约 40%）[Maillot 2016, pp. 8-9]。
7. 运动学模型生成的裂缝长度分布自然地得到指数为 ‑4 的幂律，且 T 交叉丰度高，更符合天然裂隙网络的统计特征 [Maillot 2016, pp. 1-1, 2‑3, 3‑5]。
8. 主干密度 d_b 不能单独解释渗透率差异：即使主干密度相近，运动学模型的渗透率仍低于泊松模型，表明其流动路径的结构连通效率更低 [Maillot 2016, pp. 11-12]。

## Candidate Concepts
- [[discrete fracture network (DFN)]]
- [[Poisson DFN / Poisson model]]
- [[kinematic fracture model (KFM)]]
- [[fracture nucleation, growth and arrest]]
- [[T intersection / X intersection]]
- [[connectivity]]
- [[percolation parameter p]]
- [[dimensional analysis for fracture networks]]
- [[flow channeling / channeling indicator dQ]]
- [[power-averaging exponent omega]]
- [[backbone density]]
- [[truncated power law length distribution]]
- [[effective permeability / equivalent permeability]]
- [[percolation threshold in DFN]]
- [[transmissivity variability / lognormal transmissivity]]

## Candidate Methods
- [[Davy et al. kinematic DFN generation (UFMLAB)]]
- [[H2OLAB mixed-hybrid finite element flow solver]]
- [[3D DFN permeability upscaling]]
- [[percolation parameter calculation for 3D fracture networks]]
- [[Monte Carlo DFN realization and statistical analysis]]
- [[dimensional scaling of permeability (T0/l0)]]
- [[participation ratio for flow channeling]]
- [[power-average exponent estimation from permeability variance]]

## Connections To Other Work
- 继承自 Davy et al. (2010) 的通用断裂标度模型与 Davy et al. (2013) 的成核‑生长‑停止框架 [Maillot 2016, pp. 1-2, 2‑3]。
- 与 de Dreuzy et al. (2000, 2001a,b, 2012) 关于幂律长度分布 DFN 的逾渗与渗透率研究一脉相承；本文的泊松模型结果与这些工作一致 [Maillot 2016, pp. 5-6, 7‑8, 9‑11]。
- 参与了关于 DFN 空间结构重要性的持续讨论（Darcel et al., 2003；de Dreuzy et al., 2010, 2012；Wellman et al., 2009 等）[Maillot 2016, pp. 1-1, 2‑3]。
- 通道化指标 d_Q 的构思受物理学中“参与率”（Bell and Dean, 1970；Edwards and Thouless, 1972）及 Davy et al. (1995, 2010) 的启发 [Maillot 2016, pp. 12-13]。
- 文中提出的幂律断裂密度模型与天然断裂系统的观测（Bour et al., 2002；Bonnet et al., 2001）相呼应 [Maillot 2016, pp. 1-2, 2‑3]。
- 关于导水系数变异对渗透率影响的分析与 de Dreuzy et al. (2010, 2012), Desbarats (1992), Knudby and Carrera (2005) 等的研究形成比较 [Maillot 2016, pp. 13-15]。

## Open Questions
- 运动学模型的临界长度 l_c 在实际场地（如 Forsmark 等）的确切取值仍不确定，估计在 1‑20 m，但野外测量难以直接获取该长度，这影响密度阈值的解释 [Maillot 2016, pp. 16-17]。
- 当前通道化指标 d_Q 仅按单裂缝流量定义，未考虑裂缝平面内的非均匀流；如要匹配钻孔观测的流动密度，需结合缝内通道化研究 [Maillot 2016, pp. 16-17]。
- 裂缝长度与导水系数之间可能存在正相关，这种相关性对通道化的影响尚待评估 [Maillot 2016, pp. 16-17]。
- 成核位置的非均匀性（受周围裂缝应力影响）对生成的 DFN 结构及流动性质的敏感性尚未探索 [Maillot 2016, pp. 3-5, 16‑17]。
- 对接近逾渗阈值时的运动学网络行为，现有模拟的 p 值仍较高，需要专门的近阈值数值实验来确认其临界指数是否与经典逾渗理论一致 [Maillot 2016, pp. 9-11, 16‑17]。
- 本文只研究了生长指数 a=3 的情况，不同 a 值对密度项与流动性质的影响未知 [Maillot 2016, pp. 3-5]。
- 域尺寸 L、T 交叉的具体尺寸对结果敏感性的系统量化仍有待开展 [Maillot 2016, pp. 16-17]。

## Source Coverage
本页完全基于提供的 20 个索引片段（对应 PDF 页码 至）[Maillot 2016, pp. 1-1, 20-20]编译而成。所有非空片段均已处理，块覆盖率为 1.0，字符覆盖率为 1.004962  （因标点转换略有超出）。编译策略为单程直接整合，未采用检索增强。片段覆盖详情：`indexed_texts: 20, compiled_source_blocks: 20, coverage_ratio_by_blocks: 1.0, coverage_ratio_by_chars: 1.004962`。
