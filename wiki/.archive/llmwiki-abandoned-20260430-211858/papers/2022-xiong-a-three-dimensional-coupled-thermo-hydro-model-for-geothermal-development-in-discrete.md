---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2022-xiong-a-three-dimensional-coupled-thermo-hydro-model-for-geothermal-development-in-discrete"
title: "A Three-Dimensional Coupled Thermo-Hydro Model for Geothermal Development in Discrete Fracture Networks of Hot Dry Rock Reservoirs."
status: "draft"
source_pdf: "data/papers/2023 - A three-dimensional coupled thermo-hydro model for geothermal development in discrete fracture networks of hot dry rock reservoirs.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Xiong, Feng, et al. \"A Three-Dimensional Coupled Thermo-Hydro Model for Geothermal Development in Discrete Fracture Networks of Hot Dry Rock Reservoirs.\" *Gondwana Research*, 2022, doi:10.1016/j.gr.2022.12.002."
indexed_texts: "14"
indexed_chars: "69863"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T11:47:56"
---

# A Three-Dimensional Coupled Thermo-Hydro Model for Geothermal Development in Discrete Fracture Networks of Hot Dry Rock Reservoirs.

## One-line Summary
开发并验证了一个三维耦合热-水（T-H）模型，用于模拟考虑Forchheimer非线性流动的离散裂隙网络（DFN）中的热量开采，并应用于Habanero增强型地热系统储层案例研究 [Xiong 2022, pp. 1-1]。

## Research Question
如何在三维离散裂隙网络中，考虑非线性流体流动（Forchheimer流）和局部热非平衡（LTNE）效应，以准确模拟增强型地热系统（EGS）中的流-热耦合过程？[Xiong 2022, pp. 2-3]

## Study Area / Data
- **Habanero EGS 储层**: 位于澳大利亚库珀盆地，是澳大利亚首个增强型地热资源。基底岩石为花岗岩，在4391米深处记录的最高温度为521.45 K。该储层通过2008年的水力压裂增产措施，形成了高度连通的裂隙系统 [Xiong 2022, pp. 9-11]。
- **验证模型**:
    - 交叉裂隙模型：用于验证流动方程的模型，域尺寸为500 mm × 500 mm × 5 mm，包含4条在不同平面上相交、孔径各异的裂隙 [Xiong 2022, pp. 6-7]。
    - 多交叉裂隙模型：用于验证流动方程 [Xiong 2022, pp. 7-9]。
    - 单裂隙及交叉裂隙模型：用于验证耦合T-H模型中的热传输部分，并与解析解及COMSOL解进行对比 [Xiong 2022, pp. 7-9][Xiong 2022, pp. 9-11]。
- **实验数据**: 流动验证使用了Li et al. (2016) 发表的交叉裂隙模型实验压力与流量数据 [Xiong 2022, pp. 7-9]。

## Methods
- **耦合热-水 (T-H) 模型**: 基于伽辽金有限元法开发，用于三维离散裂隙网络（DFN）模拟 [Xiong 2022, pp. 1-1]。
- **流体流动模型**: 采用 **Forchheimer 模型** 描述裂隙中的非线性流动，该模型结合了粘性力和惯性力的贡献，用于处理由于惯性效应和复杂的裂隙几何形态（如曲折流动、沟槽流）导致的非线性流动行为 [Xiong 2022, pp. 1-2][Xiong 2022, pp. 2-3]。
- **热传输模型**: 基于 **局部热非平衡（LTNE）理论**，该理论通过两个能量守恒方程分别描述裂隙流体和岩石基质中的温度场，并使用牛顿冷却定律描述流体与岩石之间的热交换 [Xiong 2022, pp. 3-4]。
- **数值解法**:
    - 流体流动方程和热传输方程均采用 **有限元法** 进行空间离散 [Xiong 2022, pp. 1-1]。
    - 为解决热传输方程中由于对流项占优导致的数值振荡问题（Peclet数 > 2），采用了 **简单迎风格式 (upwind scheme)** [Xiong 2022, pp. 4-6]。
    - 时间离散采用 **后向欧拉法 (backward Euler method)**，该方法理论上无条件稳定 [Xiong 2022, pp. 6-7]。
- **模型验证**: 将Forchheimer流动方程的模拟结果与已发表的实验结果进行比较；将耦合T-H模型的模拟结果与解析解、COMSOL数值解进行比较 [Xiong 2022, pp. 6-7][Xiong 2022, pp. 7-9][Xiong 2022, pp. 9-11]。
- **案例应用**: 应用所提出的模型模拟了不同注入压力下Habanero EGS储层长达40年的闭式循环地热生产，并评估了热传导机制和生产效率 [Xiong 2022, pp. 1-1][Xiong 2022, pp. 2-3]。

## Key Findings
- **模型有效性**: 提出的方法能有效模拟离散裂隙网络中的耦合T-H过程 [Xiong 2022, pp. 1-1]。
- **流动模型验证**: 在交叉裂隙模型中，Forchheimer模型预测的压力-流量曲线与Li et al. (2016) 的实验结果吻合良好，并且其吻合度优于线性流动模型 [Xiong 2022, pp. 7-9]。
- **热传输模型验证**: 对于单裂隙和特定热量传递系数（hc = 1000 W/(m^2 K)），模型的数值解与解析解保持一致。对于交叉裂隙，模型的温度分布解与COMSOL解吻合，且在网格数大于60,000时偏差可接受 [Xiong 2022, pp. 9-11]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 在交叉裂隙模型中，Forchheimer模型预测的压力-流量曲线比线性模型更接近Li et al. (2016) 的实验结果。 | [Xiong 2022, pp. 7-9] | 域尺寸500x500x5 mm，4条相交裂隙，不同进出口组合。 | 验证非线性流动模型的优越性。 |
| 对于单裂隙热传输模型，当hc=1000 W/(m^2 K)时，程序预测的流体温度分布与解析解在不同时间点（10, 25, 50, 100天）一致。 | [Xiong 2022, pp. 9-11] | 热传递系数hc设为1000 W/(m^2 K)。 | 验证了LTNE模型和热传输求解方法的准确性。 |
| 交叉裂隙热传输模型的结果与COMSOL的数值解吻合。当网格数超过60,000时，与COMSOL解的偏差可接受。 | [Xiong 2022, pp. 9-11] | 交叉裂隙模型，参数见表1。 | 进一步验证耦合模型在复杂几何中的准确性。 |
| Forchheimer系数b受剪切变形影响，在剪切过程中该系数减少了1到3个数量级。 | [Xiong 2022, pp. 1-2] | 此结论源自Rong et al. (2016) 的研究。 | 提示力学耦合对流动特性的重要影响，但本模型未包含。 |
| 流体在裂隙中的流动速率低于通过立方定律预测的速率，原因是异质孔径分布导致的曲折流动。 | [Xiong 2022, pp. 1-2] | 此结论源自Tsang (1984) 的研究。 | 论证了使用非线性流动模型的必要性。 |

## Limitations
- 模型仅为热-水（T-H）耦合模型，未包含应力场（M）的耦合，未能完全反映EGS开采中复杂的多物理场（热-水-力-化）过程 [Xiong 2022, pp. 1-2]。
- 从索引片段中未确认模型是否考虑了裂隙粗糙度、接触率等对流动影响的精细化描述，尽管文中引用了相关研究，但不确定是否将其参数化并融入3D DFN模型。
- 热传输模型中对岩石基质的处理使用了简化的热沉项和牛顿冷却定律，假设了基质温度在流体通过后的体积平均变化 [Xiong 2022, pp. 3-4]。
- Habanero案例模拟时长为40年，模型长期预测的准确性未与40年的实际生产数据进行对比验证 [Xiong 2022, pp. 1-1]。

## Assumptions / Conditions
- **局部热非平衡（LTNE）**: 假设裂隙流体和岩石基质温度不同，可以分别建立能量守恒方程进行描述 [Xiong 2022, pp. 3-4]。
- **非线性流动**: 裂隙中的流体流动遵循Forchheimer定律，而非线性的达西定律 [Xiong 2022, pp. 1-2]。
- **裂隙特性**: 裂隙的孔隙度为1 [Xiong 2022, pp. 3-4]。
- **热能交换**: 岩石基质与裂隙流体之间的热交换遵循牛顿冷却定律 [Xiong 2022, pp. 3-4]。
- **验证条件**: 在比较数值解和解析解时，为接近局部热平衡（LTE）条件，热传递系数hc被设定为1000 W/(m^2 K) [Xiong 2022, pp. 9-11]。
- **模型维度**: 问题被简化为在三维裂隙网络中进行二维流动和传热的耦合模拟，求解时需将三维全局坐标转换为二维局部坐标 [Xiong 2022, pp. 6-7]。

## Key Variables / Parameters
- **流动模型**: 流体压力 (P)，流体动力粘度 (μ)，流体密度 (ρ_f)，Forchheimer系数 (β)，渗透率 (K)，流体流速 (u) [Xiong 2022, pp. 1-2][Xiong 2022, pp. 4-6]。
- **热传输模型**: 流体温度 (T_f)，岩石基质温度 (T_m)，流体/岩石热容 (c_f, c_R)，流体/岩石密度 (ρ_f, ρ_R)，流体热传导系数 (k_f)，岩石基质-流体界面传热系数 (h_c)，流量 (Q)，接触面积 (A) [Xiong 2022, pp. 3-4][Xiong 2022, pp. 7-9]。
- **数值参数**: Peclet数 (Pe)，用于判断对流与热传导的比值，当Pe > 2时需采用迎风格式 [Xiong 2022, pp. 4-6]；迎风因子 (a_ij) [Xiong 2022, pp. 4-6]。

## Reusable Claims
- **Claim 1: 几何维度对预测精度的影响**
  使用二维模型预测非均质分布的三维DFN中的流场和温度场，其结果可能不准确。因此，开发三维模型具有显著潜力。 [Xiong 2022, pp. 2-3]
  - *适用条件:* 模拟对象为具有三维空间非均质分布特征的裂隙网络。
  - *限制/提示:* 虽然三维模型更精确，但其计算成本远高于二维模型。

- **Claim 2: 非线性流动模型在裂隙流模拟中的必要性**
  当裂隙中存在异质孔径分布、粗糙度或高流速时，惯性效应会导致流动偏离线性达西定律。Forchheimer定律结合了粘性和惯性效应，其预测的压降-流量关系比线性模型更贴近实验数据。 [Xiong 2022, pp. 1-2][Xiong 2022, pp. 7-9]
  - *证据:* 在交叉裂隙模型验证中，Forchheimer模型的流动曲线比线性模型更接近实验结果 [Xiong 2022, pp. 7-9]。
  - *限制:* 此声明基于裂隙流，对于多孔介质中的达西流不适用。

- **Claim 3: 热传输数值振荡的抑制**
  在使用标准Galerkin有限元法求解裂隙中的热传导-对流方程时，若Peclet数大于2，离散解会产生空间振荡。采用简单迎风格式可以有效解决此问题。 [Xiong 2022, pp. 4-6]
  - *证据:* 该方法被成功应用于模型的构建和后续验证。
  - *限制:* 迎风格式会引入数值耗散，可能影响解的精度，但保证了稳定性。

## Candidate Concepts
- [[Enhanced Geothermal System (EGS)]]
- [[Discrete Fracture Network (DFN)]]
- [[Coupled Thermo-Hydro (T-H) Model]]
- [[Forchheimer Flow]]
- [[Nonlinear Fluid Flow in Fractures]]
- [[Local Thermal Non-equilibrium (LTNE)]]
- [[Habanero EGS reservoir]]
- [[finite element method in fractures]]

## Candidate Methods
- [[Galerkin finite element method]]
- [[upwind scheme for convection-dominated problems]]
- [[backward Euler method for time integration]]
- [[LTNE-based heat transfer model]]
- [[Newton‘s law of cooling for fracture-matrix heat exchange]]

## Connections To Other Work
- **二维模型的扩展**: 本研究是作者之前发表的二维T-H模型 [Xiong et al. 2022] 的延伸与改进，旨在解决二维模型在预测三维非均质裂隙场时不准确的问题 [Xiong 2022, pp. 2-3]。
- **实验验证直接关联**: 流动模型的验证直接使用了 Li et al. (2016) 发表的多交叉裂隙模型实验结果 [Xiong 2022, pp. 7-9]。
- **理论和方法继承**:
    - 流体流动模型基于经典的Forchheimer和Izbash模型 [Huang and Ayoub, 2008] [Xiong 2022, pp. 1-2]。
    - 热传输模型基于局部热非平衡（LTNE）理论 [Chen et al. 2018, Wang et al. 2019] [Xiong 2022, pp. 3-4]。
    - 迎风格式和最优迎风因子的确定方法源自 Heinrich et al. (1977) [Xiong 2022, pp. 4-6]。
- **可关联的候选方法/概念**:
    - 非线性裂隙流研究: 与Xiong et al. (2018) [接触率对流态影响]、Rong et al. (2016) [剪切对非线性系数影响]、Wang et al. (2016) [次级粗糙度与流态] 等研究同属对裂隙非线性流动行为的探索 [Xiong 2022, pp. 1-2]。
    - 其他T-H模型: 与Sun et al. (2020) 的研究方向相似，但本研究在三维DFN中引入了非线性流动模型 [Xiong 2022, pp. 2-3]。

## Open Questions
- 未从索引片段中确认模型对于更复杂的裂隙网络（如包含裂隙交叉、死端、更广的孔径分布）时的计算效率和鲁棒性。
- 模型在Habanero案例中40年的长期预测结果（如具体的热突破时间、产出井温度下降曲线、不同注入压力下的流量变化）未在片段中详细给出。
- 如何将Forchheimer系数b与具体的、可测量的裂隙几何特性（如粗糙度、接触面积）建立定量关系，未从索引片段中确认。
- 应力场（M）的耦合缺失对该T-H模型长期预测结果（如热开采效率、流动通道变化）的具体影响程度未知。

## Source Coverage
本知识页基于14个索引片段生成，内容覆盖了论文的摘要、引言（文献综述）、方法（数学模型与数值离散）、模型验证（流动与传热）以及案例研究（Habanero储层应用）的大部分核心内容。然而，索引片段并未包含完整的附录、详细的Habanero案例参数表、全部研究结果的数据图表以及最终讨论部分的全文，因此某些详细参数、结果分析和局限性讨论可能不完整。
