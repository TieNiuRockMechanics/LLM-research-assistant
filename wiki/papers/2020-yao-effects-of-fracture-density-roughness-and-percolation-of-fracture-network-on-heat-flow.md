---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-yao-effects-of-fracture-density-roughness-and-percolation-of-fracture-network-on-heat-flow"
title: "Effects of Fracture Density, Roughness, and Percolation of Fracture Network on Heat-Flow Coupling in Hot Rock Masses with Embedded Three-Dimensional Fracture Network."
status: "draft"
source_pdf: "data/papers/2020 - Effects of fracture density, roughness, and percolation of fracture network on heat-flow coupling in hot rock masses with embedded three-dimensional fracture ne.pdf"
collections:
  - "雷恩学派分形研究"
citation: "Yao, Chi, et al. \"Effects of Fracture Density, Roughness, and Percolation of Fracture Network on Heat-Flow Coupling in Hot Rock Masses with Embedded Three-Dimensional Fracture Network.\" *Geothermics*, vol. 87, 2020, 101846. doi:10.1016/j.geothermics.2020.101846."
indexed_texts: "12"
indexed_chars: "59021"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "59259"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004032"
coverage_status: "full-index"
source_signature: "7947b1732626196cec22477c65e0838517010274"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T02:18:28"
---

# Effects of Fracture Density, Roughness, and Percolation of Fracture Network on Heat-Flow Coupling in Hot Rock Masses with Embedded Three-Dimensional Fracture Network.

## One-line Summary
本文提出了一个揭示裂隙岩体传热机理并模拟热‑流耦合过程的模型，系统地研究了裂隙密度、粗糙度及裂隙网络逾渗对嵌入三维离散裂隙网络的高温岩体中热‑流耦合的影响。

## Research Question
裂隙密度、裂隙粗糙度以及裂隙网络的逾渗特性如何控制嵌入三维离散裂隙网络的裂隙岩体中的热‑流耦合过程？其中，裂隙网络的连通性（逾渗）是否构成决定性因素？

## Study Area / Data
研究采用数值算例，未涉及具体场地。数值模型域为边长 100 m 的立方体。裂隙采用均匀等直径圆盘模型（Baecher 模型），圆盘直径主要取 20 m，逾渗测试中还使用了 10 m、30 m、40 m 的直径。材料参数主要取自前人研究（Kalinina et al., 2012; Sun et al., 2017），部分参数通过假设设定（表 2）；例如，岩石基质的渗透率取 1.0×10⁻¹⁵ m²，裂隙渗透率取 1.0×10⁻⁸ m²，裂隙厚度为 0.001 m。模型验证采用 100 m×100 m 的二维单裂隙解析解（Barends, 2010），其中裂缝长度为 100 m，厚度为 0.01 m，水流速度为 0.01 m/s。

## Methods
- **裂隙网络生成与网格剖分**：采用自主研发的网格离散化程序。基于 Delaunay 四面体化（使用开源软件 Tetgen）对岩石基质进行四面体单元剖分，同时利用裂隙面恢复技术嵌入三维零厚度三角形裂隙单元，实现岩石基质与裂隙网络的共节点网格。  
- **控制方程**：建立了考虑温度对流体密度和动力粘度影响的热‑流耦合模型。岩石基质中渗流遵循 Darcy 定律和连续性方程，温度场采用对流‑传导能量守恒方程。裂隙中采用零厚度单元，渗透率使用考虑粗糙度修正的平行板立方定律（Louis 1974 公式），热平衡方程包含了来自上下表面的热交换。  
- **求解工具**：以 COMSOL Multiphysics 为平台进行二次开发。岩石基质利用软件内置的流体流动与传热模块，裂隙则通过系数型偏微分方程（Coefficient Form PDE）模拟，实现了裂隙与基质之间物理量的耦合交换。  
- **模型验证**：将三维单裂隙模型退化为二维问题，与 Barends (2010) 给出的解析解进行对比。数值解与解析解在沿裂隙不同位置温度随时间的变化以及不同时刻温度沿程分布上吻合良好。  
- **逾渗与参数分析**：通过 Monte Carlo 试验（每组 10 000 次）研究裂隙密度与逾渗概率的关系，使用排除体积定义无量纲密度 ρ'。对不同的裂隙密度（ρ' = 0.99～4.93）和粗糙度系数（ξ 服从均值为 3、5、7、9、标准差为 1 的正态分布）进行大量样本数值模拟（每组 100 个样本取平均），以出口平均温度和出口平均流量作为评价指标。总模拟时间为 30 年，时间步长 0.1 年。

## Key Findings
1. **裂隙密度的影响**：出口平均流量随裂隙密度增大而增加，且增加幅度（曲线斜率）随密度提高而增大；出口平均温度随裂隙密度增大而降低，且降低速率先减后增，温度曲线由凸形逐步变为凹形，高密度下热突破发生更早，长尾效应显著（Fig. 5‑7）。[Yao 2020, pp. 6-7]  
2. **逾渗概率**：相同裂隙直径下，逾渗概率 P 随无量纲密度 ρ' 增加而上升，P‑ρ' 曲线斜率呈先增后减的趋势；不同直径的曲线在逾渗阈值 ρ'c = 2.281 处相交。[Yao 2020, pp. 7-9]  
3. **逾渗对热‑流耦合的决定性作用**：相同裂隙密度下，逾渗网络的出口平均流量远大于非逾渗网络，形成优势流；逾渗网络的出口温度快速下降，热突破时间明显提前，而非逾渗网络的热响应缓慢。基质的渗透率相对于裂隙极小，进一步强化了逾渗的控制作用。[Yao 2020, pp. 9-11]  
4. **粗糙度的效应**：裂隙厚度的变异性用粗糙度系数 ξ 表征。在非逾渗裂隙网络中，改变裂隙粗糙度对出口平均温度的影响几乎可以忽略；在逾渗网络中，粗糙度变化则引起出口温度曲线的明显分离。这是因为逾渗网络中裂隙主导了渗流，而非逾渗网络中岩石基质对渗流的贡献相对更大。[Yao 2020, pp. 11-12]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 出口平均流量与裂隙密度呈正相关，且斜率随密度增大而增大；同一密度下流量随时间递减 | [Yao 2020, pp. 6-7, Fig. 5] | 3D 离散裂隙网络，d=20 m，ρ'=0.99~4.93，t=0~30 y | 流量递减归因于温度降低导致粘度增大，流动阻力上升 |
| 出口平均温度随裂隙密度增大而降低，曲线形态由凸变凹；高密度下出现早期热突破和长尾效应 | [Yao 2020, pp. 7, Fig. 6-7] | 同上 | 长尾效应与 Chen et al. (2013) 的描述一致 |
| 不同裂隙直径下的逾渗概率曲线在 ρ'c=2.281 处相交 | [Yao 2020, pp. 7-9, Fig. 8] | 立方域 L=100 m，d=10,20,30,40 m，Monte Carlo 测试 | 无量纲密度基于排除体积定义 |
| 逾渗网络的出口平均流量远大于非逾渗网络，出口温度下降更迅速 | [Yao 2020, pp. 9-11, Fig. 13] | ρ'=1.97，d=20 m，相同边界条件 | 基质渗透率 (1e-15 m²) 远小于裂隙渗透率 (1e-8 m²) |
| 对于非逾渗裂隙网络，裂隙粗糙度对出口温度的影响极小；对于逾渗网络，粗糙度影响显著 | [Yao 2020, pp. 11-12, Fig. 16‑17] | 粗糙度系数 ξ 服从正态分布 N(ξ₀,1²)，ξ₀=3,5,7,9 | 非逾渗网络中基质贡献更大 |

## Limitations
- 所有结论均基于数值模拟，未与实际场地监测数据进行对比验证。
- 裂隙网络采用理想化的 Baecher 均匀等直径圆盘模型，且圆盘位置与方向服从均匀分布，未考虑真实岩体中裂隙尺寸服从幂律分布、方向成组等复杂特征。
- 岩石基质被简化为各向同性多孔介质，且基质渗透率被设定为远小于裂隙且为常数，未考虑基质渗透率的非均质性及其随温度/应力的变化。
- 三维热‑流耦合模型仅与二维单裂隙解析解进行了验证，缺少针对复杂三维裂隙网络的验证案例。
- 模拟时间限于 30 年，更长期的热开采行为和热‑力‑化多场耦合效应未被考虑。
- 部分材料参数基于假设设定，未提供实验依据。

## Assumptions / Conditions
- 岩石基质为各向同性、均质的多孔连续介质，其渗透率（1.0×10⁻¹⁵ m²）远小于裂隙渗透率（1.0×10⁻⁸ m²），渗流主要发生在裂隙中。
- 裂隙采用零厚度单元，裂隙厚度 dfr 通过控制方程隐含嵌入，不考虑裂隙开度的力学变形。
- 初始水压力为 6 MPa，对应沸点高于 200 ℃；模型最高温度设为 200 ℃，因此水始终处于液态，可用 Darcy 定律描述。
- 流体的密度和动力粘度仅为温度的函数（关系式未具体列出）。
- 裂隙网络为离散裂隙网络（DFN），采用 Baecher 等直径圆盘模型，圆盘中心点和法向量在空间中均匀随机分布。
- 边界条件：渗流场为定水头边界（入口 H₁=100 m，出口 H₂=0 m），其他边界不透水；温度场入口恒温 T_in=20 ℃，出口自然流出，其余边界绝热；初始岩体温度在主体研究中为 200 ℃，验证模型中为 180 ℃。
- 使用瞬态模拟，总时长 30 年，时间步长 0.1 年。
- 单个裂隙密度级别下的数值结果取 100 个随机样本的平均值，以消除随机性影响。

## Key Variables / Parameters
- 无量纲裂隙密度 ρ'（基于排除体积 V_ex 定义）：0.99, 1.48, 1.97, 2.46, 2.96, 3.45, 3.94, 4.43, 4.93
- 裂隙直径 d：20 m（主研究）；10, 20, 30, 40 m（逾渗分析）
- 粗糙度系数 ξ：均值 ξ₀ = 3, 5, 7, 9，标准差 σ = 1 的正态分布
- 岩石基质渗透率 κ：1.0×10⁻¹⁵ m²
- 岩石基质孔隙率 ϕ_p：0.01
- 裂隙渗透率 κ_f：1.0×10⁻⁸ m²
- 裂隙厚度 d_fr：0.001 m（主研究）；0.01 m（验证）
- 流体（水）密度和动力粘度：温度 T 的函数
- 岩石密度 ρ_p：2700 kg/m³
- 岩石比热容 c_p,p.：1000 J/(kg·K)
- 岩石导热系数 k_p：3 W/(m·K)（主研究）；2.80 W/(m·K)（验证）
- 裂隙充填材料密度：1650 kg/m³
- 裂隙充填材料比热容：900 J/(kg·K)
- 水比热容：4200 J/(kg·K)
- 计算域：100 m×100 m×100 m 立方体
- 初始温度 T_initial：200 ℃（主研究）；180 ℃（验证）
- 入口水温 T_in：20 ℃（主研究）；40 ℃（验证）
- 出口评价指标：平均出口流量 Q(t)，平均出口温度 T(t)

## Reusable Claims
- 在离散裂隙网络中，出口平均流量随裂隙密度增加而单调增加，且增加速率随密度增大而提高（ρ' ∈ [0.99, 4.93]，d=20 m，定水头边界）。[Yao 2020, pp. 6-7]
- 当裂隙密度较大时，热突破发生更早，温度‑时间曲线呈现显著的“长尾”特征，即下降速率随时间趋缓。[Yao 2020, pp. 6-7]
- 对于均匀等直径圆盘裂隙网络，逾渗概率 P 随无量纲密度 ρ' 增加而上升，其变化速率在中等密度区间达到最大，且在逾渗阈值 ρ'c ≈ 2.281 附近对不同直径的曲线出现交汇。[Yao 2020, pp. 7-9]
- 在岩石基质渗透率远小于裂隙渗透率的条件下（如 κ_matrix = 1e-15 m², κ_fracture = 1e-8 m²），裂隙网络的逾渗状态是热‑流耦合的决定性因素：逾渗网络形成优势流，出口流量远超非逾渗网络，导致出口温度更快衰减。[Yao 2020, pp. 9-11]
- 对于非逾渗裂隙网络，裂隙粗糙度的变化对出口平均温度的影响几乎可以忽略；而对于逾渗网络，粗糙度的增大（表现为 ξ₀ 从 3 增至 9）会明显改变温度演变曲线。[Yao 2020, pp. 11-12]
- 流体在逾渗裂隙网络中的流速分布极不均匀，优势通道内的流速远高于其余区域，形成“主控渗流路径”。[Yao 2020, pp. 8-9]

## Candidate Concepts
- [[percolation]] / 逾渗
- [[fracture density]] / 裂隙密度
- [[dimensionless fracture density]] / 无量纲裂隙密度
- [[excluded volume]] / 排除体积
- [[percolation threshold]] / 逾渗阈值
- [[fracture roughness]] / 裂隙粗糙度
- [[roughness coefficient]] / 粗糙度系数
- [[heat-flow coupling]] / 热‑流耦合
- [[discrete fracture network]] / 离散裂隙网络
- [[Baecher disk model]] / Baecher 圆盘模型
- [[zero-thickness element]] / 零厚度单元
- [[tetrahedral mesh]] / 四面体网格
- [[finite element method]] / 有限单元法
- [[COMSOL Multiphysics]] / COMSOL 多物理场
- [[Monte Carlo test]] / 蒙特卡罗试验
- [[thermal breakthrough]] / 热突破
- [[long-tail effect]] / 长尾效应
- [[dominant flow path]] / 优势流动路径

## Candidate Methods
- [[3D discrete fracture network heat-flow coupling model with embedded zero-thickness elements]]
- [[self-developed mesh discretization procedure using Tetgen and fracture surface restoration]]
- [[finite element implementation via COMSOL Multiphysics secondary development with PDE module]]
- [[Monte Carlo percolation probability analysis technique]]
- [[numerical verification against analytical solution for 2D single-fracture heat transport]]

## Connections To Other Work
- 与双重孔隙介质模型（Barenblatt et al., 1960; Warren and Root, 1963）和等效连续介质模型（Shaik et al., 2011; Kalinina et al., 2012）对比，本文强调显式描述裂隙网络结构的必要性。[Yao 2020, pp. 1-2]
- 延续 Chen et al. (2013) 的二维离散裂隙热‑流耦合工作，并将其拓展至三维复杂网络，同时考虑了温度对流体物性的影响。[Yao 2020, pp. 2-3]
- 引用 Louis (1974) 的粗糙平行板渗透率公式，并引入相对粗糙度描述裂隙厚度的变异性。[Yao 2020, pp. 3-4]
- 基于 Balberg et al. (1984) 的排除体积概念和 Huseby et al. (1997) 的无量纲密度定义进行逾渗分析。[Yao 2020, pp. 5-6]
- 逾渗对渗流控制作用的认识与 Berkowitz and Balberg (1993)、Cacas et al. (1990) 等相符；热‑流耦合结果与 Xiong et al. (2019) 关于连通性和导电性影响非线性流动的发现具有内在联系。[Yao 2020, pp. 2, 10, 12]

## Open Questions
- 当裂隙尺寸服从幂律分布或多组方向分布时，逾渗阈值及热‑流耦合行为将如何变化？[未在提供的片段中探讨]
- 若考虑岩石基质渗透率随温度或损伤演化的非线性变化，非逾渗网络中的粗糙度效应是否会变得显著？[仅基于恒定基质渗透率得出粗糙度影响甚微的结论]
- 长期（>30 年）热开采中，热‑力耦合引起的裂隙开度变化是否会改变逾渗路径的稳定性？[片段中未涉及应力/变形场]
- 利用三维复杂裂隙网络的现场数据（如水力试验、示踪试验）对模型进行率定和验证的可行性如何？[仅与二维解析解对比]

## Source Coverage
本文档完全基于提供的索引片段编写，所有非空片段均已被处理。覆盖审计数据如下：
- 索引文本块数：12
- 索引字符总数：59,021
- 非空源块数：12
- 汇编源块数：12
- 汇编源字符数：59,259
- 块覆盖率：1.0
- 字符覆盖率：1.004032
- 源签名：7947b1732626196cec22477c65e0838517010274
- 覆盖状态：full-index
- 编译策略：single-pass-markdown
