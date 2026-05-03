---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2019-ma-the-equivalent-discrete-fracture-networks-based-on-the-correlation-index-in-highly-fract"
title: "The Equivalent Discrete Fracture Networks Based on the Correlation Index in Highly Fractured Rock Masses."
status: "draft"
source_pdf: "data/papers/2019 - The equivalent discrete fracture networks based on the correlation index in highly fractured rock masses.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Ma, Guowei, et al. \"The Equivalent Discrete Fracture Networks Based on the Correlation Index in Highly Fractured Rock Masses.\" *Engineering Geology*, 2019, doi:10.1016/j.enggeo.2019.105228. Accessed 2026."
indexed_texts: "13"
indexed_chars: "60979"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T23:44:11"
---

# The Equivalent Discrete Fracture Networks Based on the Correlation Index in Highly Fractured Rock Masses.

## One-line Summary
提出基于关联指数（correlation index）评估单个裂隙重要性，并构建密度降低的等效离散裂隙网络模型，通过等效渗透率因子在牺牲较小精度的前提下大幅降低计算复杂度。[Ma 2019, pp. 1-1]

## Research Question
如何在高裂隙岩体中，通过识别不同裂隙对渗透性的贡献差异，构建一种既能显著减少裂隙数量（从而降低计算复杂度）又能保持原始渗透性特征的等效离散裂隙网络？[Ma 2019, pp. 1-1, 7-8]

## Study Area / Data
研究未使用特定野外场地数据，而是基于随机分形模型生成了典型的合成离散裂隙网络（DFN）。裂隙几何参数由以下规则生成：长度服从幂律分布，孔径采用常数、对数正态或与长度相关三种分布，中心位置通过分形模型或泊松过程生成。所有数值试验均使用多次随机实现（如10次）以稳定统计结果。[Ma 2019, pp. 4-7, 10-11]

## Methods
- **关联指数定义**：定义关联指数 S = N̄ · b̄^γ · P̄_c^β，其中 N̄ 为归一化交点数，b̄ 为归一化水力孔径，γ 为孔径权重因子（二维取2，三维取3），P̄_c 为归一化密度概率，β 为密度显著性因子。该指数用于量化单个裂隙对整体网络水力性质的重要性。[Ma 2019, pp. 7-8]
- **密度降低策略**：根据关联指数对裂隙排序，保留高重要性的裂隙，舍弃低重要性裂隙，形成密度降低的等效模型。[Ma 2019, pp. 1-1, 7-8]
- **等效渗透率因子**：引入因子 ω_r 表示密度降低前后域总透射率的比例，通过该因子可将等效模型的结果恢复至原始域水平。[Ma 2019, pp. 8-10]
- **方向渗透率曲线**：采用旋转子域法（5 m × 5 m，步长15°）计算各方向渗透率，忽略孤立裂隙和死端，构建渗透率曲线，并利用形状相似性评价等效模型。[Ma 2019, pp. 8-10]
- **裂隙网络生成**：基于分形模型，长度使用截断幂律分布（指数 a，渗透系数 p），孔径分别假设为常数、对数正态或与长度相关（利用 E, ν, K_IC），中心位置采用分形分布（分形维数 D_q）或均匀分布。[Ma 2019, pp. 4-7]
- **网格质量评估**：通过自由度、平均纵横比和渗透率曲线误差 ε_r 衡量等效模型的计算效率与精度。[Ma 2019, pp. 8-10 表格]

## Key Findings
- 当依据关联指数去除50%裂隙时，方向渗透率曲线的形状与原始域仍高度相似，因此可利用等效渗透率因子准确复原总透射性。[Ma 2019, pp. 8-10]
- 若裂隙孔径与长度正相关，长裂隙的重要性被强化，密度降低过程中的误差较常数孔径情形更小；若孔径服从对数正态分布且标准差较大，误差则加速增大。[Ma 2019, pp. 10-11]
- 裂隙中心位置的分形维数 D_q 对等效模型适用性影响显著：分形维数越低（分布越聚集），密集区裂隙更可被替代，早期误差被抑制，但过高密度降低率会导致误差急剧上升。以 ε_r=0.1 为上限，D_q=1.75、1.85、1.95 时容许的最大裂隙去除率分别为81.6%、91.3%和98.0%。均匀分布时误差始终低于0.082。[Ma 2019, pp. 11-11]
- 该方法能改善裂隙‑基质域的网格质量，并可快速准确估算不同边界条件下的气体产能。[Ma 2019, pp. 1-1]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 50%裂隙被忽略后，渗透率曲线与原始域形状相似，ω_r 可恢复结果 | [Ma 2019, pp. 8-10] | 二维分形 DFN，常数孔径 | 形状相似性是等效方法的基石 |
| 孔径与长度相关时，密度降低误差低于常数孔径情形 | [Ma 2019, pp. 10-11] | K_IC·=0.6 MPa·m^½, E=5×10^4 MPa, ν=0.25 | 长裂隙主导骨架，保持相似性 |
| 对数正态孔径且 σ_b=0.5μ_b 时，误差随降低率加速上升 | [Ma 2019, pp. 10-11] | μ_b=5 mm, σ_b=2.5 mm | 高离散孔径削弱等效性 |
| 均匀分布时误差稳定于0.082以下 | [Ma 2019, pp. 11-11] | β=0，分形维数接近2 | 均质情形最为稳定 |
| D_q=1.75 时，ε_r=0.1 容许最大降低率为81.6% | [Ma 2019, pp. 11-11] | 分形中心位置，幂律长度 | 聚类越强，容许降低率越低 |
| 密度降低可显著改善网格质量（自由度从20979降至11811，误差7.92%） | [Ma 2019, pp. 8-10 表格] | 常数孔径，50%降低率 | 效率提升与精度损失的折中 |

## Limitations
- 仅考虑了裂隙长度、孔径和中心位置构成的参数集，其他几何属性（如粗糙度、充填物）未纳入。[Ma 2019, pp. 7-8]
- 权重因子 β 和 γ 的选择依赖于裂隙分布特征，文中仅给出部分配置，泛化能力尚待验证。[Ma 2019, pp. 11-11]
- 结果精度强烈依赖于密度降低程度和分布类型，对高度非均质情况，可接受的降低率有限。[Ma 2019, pp. 10-11, 11-11]
- 仅验证于二维合成裂隙网络，三维情况仅给出 γ 的建议值，未进行实际模拟。[Ma 2019, pp. 7-8]
- 所有分析均基于立方律假设，未讨论偏离立方律的流动行为。[Ma 2019, pp. 7-8]

## Assumptions / Conditions
- 裂隙流遵循立方律（二维 γ=2，三维 γ=3）。[Ma 2019, pp. 7-8]
- 裂隙网络由分形模型生成，长度服从幂律分布，孔径采用常数、对数正态或与长度相关三种模式。[Ma 2019, pp. 4-7]
- 模拟中施加恒定压力梯度，仅考虑主干网络（去除孤立裂隙和死端）。[Ma 2019, pp. 8-10]
- 裂隙方向的具体统计模型（如 Fisher 分布参数）未从索引片段中确认。
- 等效性评价基于方向渗透率曲线的形状相似性和包络面积。[Ma 2019, pp. 8-10]

## Key Variables / Parameters
- S：关联指数，综合评估裂隙重要性。[Ma 2019, pp. 7-8]
- N̄：归一化交点数，当前裂隙交点数与平均值的比值。[Ma 2019, pp. 7-8]
- b̄：归一化水力孔径。[Ma 2019, pp. 7-8]
- γ：孔径显著性因子（二维=2，三维=3）。[Ma 2019, pp. 7-8]
- β：密度显著性因子（均匀分布=0，非均匀=1）。[Ma 2019, pp. 11-11]
- P̄_c：归一化密度概率。[Ma 2019, pp. 7-8]
- ω_r：等效渗透率因子，密度降低率 r 时的恢复比例。[Ma 2019, pp. 8-10]
- a：长度幂律指数。[Ma 2019, pp. 2-4]
- p：渗透系数，控制裂隙质量密度。[Ma 2019, pp. 2-4]
- D_q：裂隙中心位置分形维数。[Ma 2019, pp. 11-11]
- μ_b, σ_b：对数正态孔径的均值与标准差。[Ma 2019, pp. 4-7]
- l_min, l_max：裂隙长度上下界。[Ma 2019, pp. 2-4]
- k_{rθ}：密度降低率为 r、测试方向 θ 时的平均渗透率。[Ma 2019, pp. 8-10]
- ε_r：等效域与原始域渗透率曲线的相似性误差。[Ma 2019, pp. 8-10, 11-11]
- E, ν, K_IC：用于长度相关孔径模型的弹性参数与断裂韧度（仅案例使用）。[Ma 2019, pp. 10-11]

## Reusable Claims
- “当裂隙孔径与长度正相关时，长裂隙的导流贡献被放大，在密度降低过程中骨架网络更具代表性，因此误差低于常数孔径或高离散孔径情形。” [Ma 2019, pp. 10-11] （适用条件：裂隙开度受长度控制，适用于应力敏感型裂隙系统。）
- “在裂隙中心位置呈低分形维数（如 D_q=1.75）时，裂隙密集区的个体裂隙可替代性强，优先移除这些裂隙能在早期压低形状相似性误差；但过度降低会迅速放大方差。” [Ma 2019, pp. 11-11] （适用条件：分形中心分布，需结合密度权重因子 β 进行调制。）
- “基于关联指数的密度降低法可在保持方向渗透率曲线形状相似的条件下，将二维域自由度从约2.1万降至1.2万，同时仅引入7.9%的渗透率曲线误差。” [Ma 2019, pp. 8-10 表格] （适用条件：常数孔径、分形长度、二维情况，误差上限可接受。）
- “等效渗透率因子 ω_r 可将缩减网络计算得到的平均透射率缩放回原始域水平，从而避免直接模拟全裂隙域。” [Ma 2019, pp. 8-10] （限制：需保证方向渗透率曲线形状相似，ω_r 依赖于降低率和分布类型。）

## Candidate Concepts
- [[correlation index]]
- [[equivalent discrete fracture network (E-DFN)]]
- [[permeability similarity]]
- [[equivalent permeability factor]]
- [[density-reduced model]]
- [[fracture network connectivity]]
- [[hydraulic aperture]]
- [[power-law length distribution]]
- [[fractal fracture network]]
- [[log-normal aperture distribution]]
- [[directional permeability curve]]
- [[backbone of fracture network]]

## Candidate Methods
- [[stochastic fractal DFN generation]]
- [[rotational subdomain method]] for directional permeability
- [[Monte Carlo simulation]]
- [[two-point flux approximation (TPFA)]]
- [[equivalent permeability factor calibration]]
- [[correlation index-based fracture significance evaluation]]

## Connections To Other Work
- 文中将所提方法与早期“等效离散裂隙网络（E-DFN）”方法进行对比，指出后者未评估裂隙重要性且生成的网络几何不真实，但具体 E-DFN 文献未在片段中给出。[Ma 2019, pp. 1-2]
- 分形裂隙网络生成基于系列前期研究，如 Bour and Davy (1997)、Darcel et al. (2003)、de Dreuzy et al. (2001)、Liu et al. (2015)，可直接连接到 [[fractal fracture models]]。[Ma 2019, pp. 4-7]
- 在讨论随机实现与不确定性时引用了 Chesnaux et al. (2009)、Earon and Olofsson (2018)、Hamdia et al. (2018) 以及 Vu-Bac et al. (2016) 的敏感性与不确定性分析工具箱，可连接到 [[uncertainty quantification in DFN]]。[Ma 2019, pp. 1-2]
- 导水率与几何参数的关系参考了 Ren and Santamarina (2018)，可连接到 [[geometric controls on permeability]]。[Ma 2019, pp. 7-8]
- 整体框架可主题性连接到 [[fracture reservoir simulation]], [[upscaling of fractured media]], [[percolation theory in fracture networks]]。

## Open Questions
- 权重因子 β 和 γ 在任意裂隙几何配置下的最优选择机制是什么？未从索引片段中确认。
- 该方法在三维真实裂隙网络中的适用性与精度如何？未从索引片段中确认（仅给出 γ 取值建议）。
- 当裂隙包含粗糙度、充填物或处于复杂应力环境时，关联指数与等效因子的有效性是否仍能保持？未从索引片段中确认。
- 等效渗透率因子 ω_r 对多实现的统计稳健性如何？片段仅提及误差范围依赖于降低率和分布模型，未作系统分析。[Ma 2019, pp. 10-11]
- 方法能否推广到多相流或非达西流情形？未从索引片段中确认。

## Source Coverage
本页内容基于该论文的13个索引片段撰写，片段涵盖了摘要、引言、部分符号定义、关联指数的核心定义、渗透率曲线相似性的初步结果，以及孔径分布和裂隙位置分布影响的案例讨论。信息偏向于方法框架和关键参数影响的描述，缺少完整的模型实现细节（如裂隙方向的具体生成方式、ω_r 的完整计算流程）、所有案例的定量结果以及更深入的误差分析。三维验证、与现场数据的对比以及与其他降阶方法的定量比较等重要信息未被片段覆盖，因此部分内容标注为“未从索引片段中确认”。
