---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2025-zhao-characterizing-the-intrinsic-complexity-of-natural-fracture-networks-a-novel-fractal-b"
title: "Characterizing the Intrinsic Complexity of Natural Fracture Networks: A Novel Fractal-Based Approach."
status: "draft"
source_pdf: "data/papers/2025 - Characterizing the intrinsic complexity of natural fracture networks A novel fractal-based approach.pdf"
collections:
  - "神经网络结合分形网络研究"
citation: "Zhao, Jingyan, et al. “Characterizing the Intrinsic Complexity of Natural Fracture Networks: A Novel Fractal-Based Approach.” *Engineering Geology*, vol. 358, 2025, 108376. DOI:10.1016/j.enggeo.2025.108376."
indexed_texts: "15"
indexed_chars: "73585"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "70630"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.959842"
coverage_status: "full-index"
source_signature: "43c74cfdde9b4e231141a41e47bfd429df1f1422"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T07:58:14"
---

# Characterizing the Intrinsic Complexity of Natural Fracture Networks: A Novel Fractal-Based Approach.

## One-line Summary
本文基于分形地形理论，识别天然裂隙网络的两种复杂度（原始复杂度和行为复杂度），建立通用的F3s表征框架与FT-DFN建模算法，并提出利用可测几何属性反演分形地形参数的方法；通过煤样CT扫描实验验证，重构的裂隙长度序列与实测值的平均绝对误差为0.21–0.71 mm，优于传统幂律建模方法。[Zhao 2025, pp. 1-1, 7-8]

## Research Question
天然裂隙网络具有分形和随机分布特征，其内在复杂度的准确表征面临三个关键问题：
1. 裂隙网络中存在哪些复杂度类型，它们如何组装？
2. 几何属性和标度不变结构的控制因素是什么，分别属于哪种复杂度？
3. 分形行为的数学定义与复杂度度量如何区分？[Zhao 2025, pp. 1-2]

## Study Area / Data
- **样品来源**：中国宁条塔煤矿煤样，加工成直径与高度均为50 mm的圆柱试样。[Zhao 2025, pp. 5-5]
- **实验设备**：高分辨率X射线显微镜（型号：Xradia 515 Versa），对试样进行CT扫描。[Zhao 2025, pp. 5-5]
- **数据获取**：利用Dragonfly软件对2D切片进行图像处理（裁切、灰度调整、滤波、阈值分割），并通过人工标注修正分割误差；从试样中随机选取6个切片，获得裂隙总数、长度序列、总长度等几何属性。[Zhao 2025, pp. 5-6, 6-6]

## Methods
1. **理论框架**  
   - 分形地形理论指明天然多孔介质为**双复杂度系统**，包括原始复杂度（由标度对象G [包含主裂隙几何属性：长度l、开度α、迂曲度τ] 决定）和行为复杂度（由分形地形Ω[P,F] 及随机性ρ决定）。[Zhao 2025, pp. 2-3, 3-3]  
   - 通用分形地形Ω(P,F)扩展至多重分形地形Ω_P，实现对任意分形行为的统一定义。[Zhao 2025, pp. 2-2]  
   - 建立在**F3s框架**：F3s(G(l,a,τ), Ω_Pi((P1,…,PF)^i), ρ(ρ(θ),ρ(x,y)))，统一表征裂隙网络的几何特征、标度不变性和空间分布。[Zhao 2025, pp. 3-4]

2. **反演算法**  
   - 基于假设“裂隙网络具有层次结构且相邻层次标度行为一致”，建立几何参数与分形地形参数的关系：由裂隙总数N与式(5)导出多组(F,i)解；利用长度序列和式(6)–(8)计算一般标度空亏度P；以总长度L与式(9)的差异最小化为约束，确定最优解。[Zhao 2025, pp. 3-4, 4-5]  
   - 引入离散系数A（式10）表征标度空亏度的异质性。[Zhao 2025, pp. 5-5]

3. **FT-DFN建模**  
   - 基于F3s框架的裂隙网络建模算法，结合主裂隙构造、分形迭代生长和角度/位置概率分布，生成裂隙网络；进一步引入扰动因子k，形成**随机分形地形模型**，以捕捉局部变异性。[Zhao 2025, pp. 6-7]

4. **对比评估**  
   - 与仅依赖几何参数（数密度λ_20、长度密度λ_21）或分形维数（盒计数维数D_b、分形拓扑维数D_t）的表征方法对比，并比较基于最大似然估计（MLE）和对数回归（LR）的幂律建模方法。[Zhao 2025, pp. 7-7, 7-8]

## Key Findings
1. 裂隙网络存在两种独立的复杂度：由主裂隙几何定义的**原始复杂度**和由标度不变行为与随机性定义的**行为复杂度**。基于此建立的F3s框架与FT-DFN模型可系统表征任意裂隙网络。[Zhao 2025, pp. 3-3, 9-9]
2. 从CT扫描煤样6个切片中反演的裂隙长度序列与实测值吻合良好，平均绝对误差（MAE）为0.21–0.71 mm，验证了反演算法的有效性。[Zhao 2025, pp. 7-7, 9-9]
3. 与MLE-或LR-幂律建模相比，分形地形模型生成的裂隙长度序列MAE最低，且对数据质量波动（拟合优度R²=0.92–0.97）表现出更强的鲁棒性。[Zhao 2025, pp. 7-8]
4. 分形地形参数不仅刻画主裂隙几何，还控制网络演化过程，因而能实现裂隙长度序列的一一对应表征，弥补了传统几何参数与分形维数存在多对一映射的缺陷。[Zhao 2025, pp. 7-7]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 反演算法从6个煤样切片裂隙网络中提取的分形地形参数（表1），重构序列与实测值MAE=0.21–0.71 mm | [Zhao 2025, pp. 5-6, 6-7] | 试样为直径50 mm煤柱，CT扫描分辨率由Xradia 515 Versa提供；裂隙简化为直线段 | 误差分析见图5、图7 |
| 随机分形地形模型（引入扰动因子k）较严格分形模型显著降低局部MAE，且总长度预测保持精度 | [Zhao 2025, pp. 6-7] | k定义为均匀分布U(-b,b)，b通过式(13)由P_max、P_min确定 | 灵敏度分析（附录B）表明模型输出稳定 |
| 与MLE、LR建模对比，分形模型在各切片上的MAE均最低，且波动范围小(0.21–0.71 mm)，MLE的MAE升至1.47，LR的MAE升至2.50 | [Zhao 2025, pp. 7-8] | 假设裂隙长度服从幂律分布，拟合优度R²>0.95 | 对比基于六组网络平均模拟结果 |
| 复杂装配参数(l0,P,F,i)能唯一表征长度序列，而D_b、D_t等存在不同网络具有相似值的情况 | [Zhao 2025, pp. 7-7] | 比较对象为图4的六组网络（a-f） | 如表3所示，(b)与(e)的D_t均为1.65，但序列不同 |

## Limitations
- 当前研究限于**二维裂隙网络的表征**，尚未考虑三维空间中的裂隙交切、连通性和体积约束。[Zhao 2025, pp. 8-8]
- 反演算法假设裂隙网络具有理想层次结构和相邻层次一致标度行为，所得分形地形参数是自然裂隙复杂度的有效或理想化表达。[Zhao 2025, pp. 3-4]
- 对多重分形系统，算法仅能提取一般标度空亏度P，未能给出各单独标度行为的详细参数。[Zhao 2025, pp. 5-5]
- 重建过程中角度和位置分布被假设为相互独立的简单分布，这一简化可能影响网络拓扑的精细表征。[Zhao 2025, pp. 6-6]

## Assumptions / Conditions
1. 裂隙网络具有**层次结构**，且相邻层次间呈现一致的标度行为。[Zhao 2025, pp. 3-4]
2. 裂隙的总数、长度序列等几何参数可通过数字图像处理准确获取，并经人工标注修正了过分割与欠分割问题。[Zhao 2025, pp. 5-5]
3. 裂隙被简化为**直线段**以保留主要几何特征，忽略细微弯曲和开度变化。[Zhao 2025, pp. 6-6]
4. 重构时裂隙中点的x、y坐标分布相互独立，角度分布拟合为均匀分布。[Zhao 2025, pp. 6-6]
5. 引入扰动因子k时，k满足零均值的均匀分布，其幅值b由理论范围扩展±15%确定。[Zhao 2025, pp. 6-7]

## Key Variables / Parameters
- **几何参数**：裂隙总数N，主裂隙长度l0，裂隙长度序列l_i，网络总长度L′。[Zhao 2025, pp. 4-4, 5-6]
- **分形地形参数**：标度空亏度P（或一般标度空亏度P），标度覆盖度F，演化层级i。[Zhao 2025, pp. 2-2, 4-4]
- **复杂度装配参数组合**：(l0, P, F, i) 构成表征裂隙网络长度特征的核心集合。[Zhao 2025, pp. 7-7]
- **离散系数**：A（式10），量度标度空亏度的异质性。[Zhao 2025, pp. 5-5]
- **扰动因子**：k～U(-b, b)，用于模拟局部变异性。[Zhao 2025, pp. 6-7]
- **分形维数**：分形拓扑维数D_t（式2–4），由P和F定义。[Zhao 2025, pp. 2-3]
- **其他**：角度分布参数、裂隙中点位置分布范围。[Zhao 2025, pp. 6-6]

## Reusable Claims
1. 天然裂隙介质为**双复杂度系统**，包括由主裂隙几何决定的原始复杂度和由分形迭代行为决定的行为复杂度；仅依靠分形维数不足以完全表征其复杂度。[Zhao 2025, pp. 2-2, 3-3] (条件：裂隙网络显现分形特征，主裂隙可明确识别)
2. 通过推广分形地形至多重分形地形Ω_P，可以实现对**任意分形行为**（自相似、自仿射、多重分形）的统一数学定义。[Zhao 2025, pp. 2-3] (条件：系统满足标度不变性)
3. 裂隙网络的几何参量（总数N、长度序列）可与分形地形参数(F,i,P)建立定量关系（式5–9），从而由可测数据**反演分形结构参数**。[Zhao 2025, pp. 4-4] (条件：网络具有近似层次结构，相邻层次标度一致)
4. **离散系数A**（式10）可作为衡量标度空亏度异质性的指标；A值越大，裂隙长度分布越极化，网络空间组织越不规则。[Zhao 2025, pp. 5-5] (条件：适用于存在多个标度行为的裂隙系统)
5. F3s(G,Ω_Pi,ρ)框架不仅能描述裂隙网络，还能支撑其**等效重建**，生成的网络长度序列MAE可低至0.21–0.71 mm，优于传统幂律建模。[Zhao 2025, pp. 3-4, 7-8] (条件：拥有主裂隙几何参数、分形地形参数及角度/位置分布信息)
6. 引入基于离散系数A的**扰动因子k**（式13），可有效改善局部拟合，提升随机分形地形模型对天然裂隙网络变异的适应性。[Zhao 2025, pp. 6-7] (条件：扰动幅值b的范围根据P_max,P_min按±15%扩展确定)

## Candidate Concepts
- [[dual-complexity system]]
- [[fracture networks]]
- [[fractal topography theory]]
- [[original complexity]]
- [[behavioral complexity]]
- [[scaling object G]]
- [[scaling lacunarity P]]
- [[scaling coverage F]]
- [[multifractal topography]]
- [[scale-invariance properties]]
- [[complexity assembly]]
- [[F3s framework]]
- [[Fractal Topography-based Discrete Fracture Network Model (FT-DFN)]]
- [[discreteness coefficient A]]
- [[random fractal topography model]]
- [[geometric parameters λ20, λ21]]
- [[box-counting dimension Db]]
- [[fractal topological dimension Dt]]
- [[power-law distribution of fracture lengths]]
- [[Maximum Likelihood Estimation (MLE) modeling]]
- [[Logarithmic Regression (LR) modeling]]
- [[CT scanning and image processing for fractures]]

## Candidate Methods
- [[fractal topography modeling]]
- [[inversion algorithm for fractal topography parameters]]
- [[CT scanning (X-ray micro-Computed Tomography)]]
- [[digital image processing workflow (Dragonfly software)]]
- [[manual annotation of fractures]]
- [[perturbation factor k for stochastic variation]]
- [[error analysis (MAE, ε)]]
- [[sensitivity analysis (OAT, NSI)]]
- [[comparison with MLE- and LR-based length sequence generation]]
- [[framework F3s(G, ΩPi, ρ) for fracture network characterization]]

## Connections To Other Work
- 与**分形地形理论**的先前工作紧密关联：Jin et al. (2017a, 2019) 提出的双复杂度概念、分形地形定义以及F3s框架为本研究的直接基础。[Zhao 2025, pp. 2-2]
- 对裂隙网络分形特征的识别延续了Xie et al. (1999)、Yu et al. (2000) 等关于裂隙属性幂律关系的研究。[Zhao 2025, pp. 1-1, 3-4]
- 表征框架与**离散裂隙网络(DFN)模型**相衔接，例如Haryono et al. (2024)、Ma et al. (2020) 等将DFN用于岩体变形分析；本研究的FT-DFN模型融合了分形迭代生长与DFN的空间分配机制。[Zhao 2025, pp. 1-2, 3-4]
- 与基于分形维数反演结构的方法（如Liu et al., 2016; Kolyukhin and Protasov, 2023）相比，本方法通过分形地形参数克服了分形维数“一对多”映射的局限性。[Zhao 2025, pp. 1-2]
- 与裂隙网络几何参数和盒计数分形维数的对比（如Bonnet et al., 2001；Dershowitz and Herda, 1992）显示，复杂装配参数在区分网络唯一性方面优于传统描述量。[Zhao 2025, pp. 7-7]
- 讨论部分指出，本方法未来可与三维岩体结构表征（Luo et al., 2024）、非常规天然气开发（Zhao et al., 2014）、地热开发（Medici et al., 2023）等领域的研究结合。[Zhao 2025, pp. 8-9]

## Open Questions
- 如何将提出的二维表征框架**有效扩展到三维**，并解决裂隙交切、连通性以及三维体积约束等问题？[Zhao 2025, pp. 8-8]
- 如何从多重分形系统中提取**各单独标度行为的详细参数**，而不仅限于一般标度空亏度？[Zhao 2025, pp. 5-5]
- 如何将该小尺度表征方法与**大尺度/现场尺度**的裂隙网络模型及等效参数（升尺度）相结合，以嵌入地质力学模拟器？[Zhao 2025, pp. 8-9]
- 在不同应力条件下，裂隙网络的**动态演化**如何用本文的复杂度装配参数进行描述与预测？[Zhao 2025, pp. 9-9]
- 对所提取分形地形参数的**唯一性**与**稳健性**，在更复杂、强非均质裂隙系统中尚需进一步验证。[Zhao 2025, pp. 1-2, 5-5]

## Source Coverage
所有索引的非空片段（共15个）均被处理并纳入本页编译。片段索引覆盖率为100%（15/15），字符覆盖率为95.98%（70630/73585已编译字符）。[coverage audit metadata]
