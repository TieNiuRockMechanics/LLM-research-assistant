---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2022-he-numerical-evaluation-of-heat-extraction-performance-in-enhanced-geothermal-system-consid"
title: "Numerical Evaluation of Heat Extraction Performance in Enhanced Geothermal System Considering Rough-Walled Fractures."
status: "draft"
source_pdf: "data/papers/2022 - Numerical evaluation of heat extraction performance in enhanced geothermal system considering rough-walled fractures.pdf"
collections:
  - "zotero new"
citation: "He, Renhui, et al. \"Numerical Evaluation of Heat Extraction Performance in Enhanced Geothermal System Considering Rough-Walled Fractures.\" *Renewable Energy*, vol. 188, 2022, pp. 524-44. doi:10.1016/j.renene.2022.02.067. Accessed 2026."
indexed_texts: "18"
indexed_chars: "87795"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T11:09:03"
---

# Numerical Evaluation of Heat Extraction Performance in Enhanced Geothermal System Considering Rough-Walled Fractures.

## One-line Summary
通过144个离散裂隙网络模型的THM耦合模拟，系统评估了粗糙壁裂缝对增强型地热系统（EGS）热提取性能的影响，发现粗糙壁效应会降低热提取峰值、减少总产热量并延长热回收周期，且受力学开度、粗糙度分布以及裂缝方位的显著控制 [He 2022, pp. 1-2]。

## Research Question
现有EGS数值模型多将裂缝简化为平行板，关于裂缝表面粗糙度效应的结论因模型尺寸和计算条件不一致而相互矛盾，且传热系数的作用尚不明确。本研究旨在不同裂缝方位、模型尺寸及开度非均质性条件下，定量评估考虑粗糙壁裂缝时热-水-力耦合作用下的热提取性能差异 [He 2022, pp. 2-3]。

## Study Area / Data
本研究未使用特定地理区域的实际数据，而是构建概念性地热储层模型。裂缝表面粗糙度（JRC）的统计分布形式参考了瑞典 Oskarshamn/Forsmark 和伊朗 Bakhtiary 的现场观测数据，分为正态分布和对数正态分布两种 [He 2022, pp. 6-7]。模型的材料参数见表2-3 [He 2022, pp. 4, 8-9]，数值计算通过二维解析解和热固结案例进行了验证 [He 2022, pp. 4-5]。

## Methods
- **几何模型构建**：基于离散裂隙网络（DFN）方法，建立二维地热储层模型。共设计3组裂缝方位（C1: 30°/150°, C2: 45°/135°, C3: 60°/120°）、4种模型尺寸（S1: 20 m, S2: 100 m, S3: 500 m, S4: 1000 m），以及4种水力开度分布类型（粗糙壁正态分布RN、对应平行板PN；粗糙壁对数正态分布RL、对应平行板PL），总计144个模型。各模型中裂缝密度一致，迹长服从正态分布 [He 2022, pp. 6-8]。
- **粗糙壁表征**：利用JRC与水力开度的经验关系 \( e_h = e_m^2 / JRC^{2.5} \) 将宏观看糙度转化为水力开度的非均质性，当 \( e_h \) 大于力学开度 \( e_m \) 时强制取等。力学开度取20、100、500 μm三种 [He 2022, pp. 7-8]。
- **多场耦合控制方程**：采用THM耦合方法，岩石基质视为多孔介质，传热方程考虑岩石与水的有效热容和有效热导率；裂缝内流体传热采用对流-传热方程，通过牛顿冷却定律引入热交换系数 \( h_{int} = 2h/e_h \)；力学本构考虑温度与孔隙压力引起的应变，裂缝位移用线性刚度描述，渗透率随应力、位移变化 [He 2022, pp. 3-4]。
- **数值求解与验证**：使用三角形网格离散，经网格无关性检验后单元数约40000；时间步长1天，收敛容差10⁻⁶。通过单裂缝换热二维解析解和Bai等热固结解析解验证了数值模型的可靠性 [He 2022, pp. 4-5, 8-9]。

## Key Findings
- **平行板模型与粗糙壁模型的差异**：平行板模型的峰值热提取率出现更早、数值更大；总热提取量始终高于粗糙壁模型；热回收过程持续时间更短 [He 2022, pp. 1-2]。
- **粗糙壁效应的量化**：提出了两个比率指标，分别衡量热提取持续时间和总产出能量的差异，可定量评价粗糙壁效应 [He 2022, pp. 1-2]。
- **控制因素**：粗糙壁效应主要受裂缝网络的力学开度与粗糙度分布影响；裂缝方位对EGS热回收性能具有显著重要性 [He 2022, pp. 1-2]。
- **传热系数的影响**：不同类型的传热系数及其取值会对产出温度产生影响，但其在EGS热提取性能评价中的详细作用仍有待进一步研究 [He 2022, pp. 2-4]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 平行板模型比粗糙壁模型更早出现且更高的热提取率峰值，总热提取量更大，热回收持续时间更短 | [He 2022, pp. 1-2] | 基于144个DFN模型的THM耦合模拟，固定压力梯度，不同尺寸、方位和开度非均质性 | 摘要陈述，缺乏具体数值 |
| 裂缝方位对EGS热回收性能有显著影响 | [He 2022, pp. 1-2] | 三种方位（30°/150°、45°/135°、60°/120°）的比较 | 具体最优方位未从片段中提供 |
| 粗糙壁效应主要受力学开度和粗糙度分布控制 | [He 2022, pp. 1-2] | 力学开度取20、100、500 μm，JRC正态和对数正态分布 |  |
| 所提数值模型能在单裂缝换热和热固结案例中与解析解良好吻合，最大相对误差0.12% | [He 2022, pp. 4-5] | 二维单裂缝解析解（Cheng 等）和热固结解析解（Bai 等） | 验证了THM耦合的可靠性 |
| 传热系数类型和取值影响产出温度，但其作用需进一步研究 | [He 2022, pp. 2-4] | 在THM框架内使用换热系数 \( h \) 和 \( h_{int} \) | 未给出不同系数下的对比结果 |

## Limitations
- 所有结果均为二维概念模型下的数值模拟，未考虑真实三维裂隙网络、非均质围岩及地应力场的复杂性 [He 2022, pp. 2-3]。
- 粗糙壁效应仅通过JRC-水力开度经验关系间接反映，未直接模拟粗糙表面的细观形貌，且该经验公式“未从索引片段中确认”其适用范围与验证。
- 热提取性能差异的结论是相对于平行板参考模型的倾向性判断，未给出两个比率指标的具体数值或阈值。
- 对传热系数作用的分析仅停留在“产生影响”，未从片段中确认如何影响或影响程度 [He 2022, pp. 2-4]。
- 数值验证中解析方法与实验数据的最大偏差达5.23%，被归因于未考虑粗糙度，但未排除其他潜在因素 [He 2022, pp. 4]。
- 所构建的DFN模型强制裂缝密度和拓扑一致，但实际岩体中不同尺度的裂隙网络可能不具备这种自相似性。

## Assumptions / Conditions
- 地热储层视为由岩石基质与离散裂缝构成的等效多孔介质，裂缝渗透率远大于基质，流体主要在裂缝中流动 [He 2022, pp. 3-4]。
- 热传递遵循局部热平衡假设，岩石与流体间的传热由牛顿冷却定律描述 [He 2022, pp. 3-4]。
- 岩石基质为线弹性，裂缝法向和切向刚度恒定，变形引起渗透率变化 [He 2022, pp. 3-4]。
- 裂缝面粗糙度由JRC表征并通过经验公式转化为水力开度非均质性；力学开度设为定值，且水力开度不超过力学开度 [He 2022, pp. 7-8]。
- 模型边界施加固定压力梯度（2×10⁴ Pa/m），左右边界为定压边界，上下为无流动/绝热边界 [He 2022, pp. 8-9]。
- 不同尺寸模型保持裂缝数量、拓扑一致，迹长按比例缩放且服从正态分布 [He 2022, pp. 6-7]。
- 所有算例的初始和边界温度、材料参数（如岩石热导率、比热容等）按表2-3设定，具体数值未从片段中提供 [He 2022, pp. 8-9]。

## Key Variables / Parameters
- **模型几何参数**：裂缝方位（C1/C2/C3）、模型尺寸（S1–S4，20 m 至 1000 m 正方形）、裂缝迹长分布（期望值u，标准差σ）[He 2022, pp. 6-7]
- **裂缝开度与粗糙度**：力学开度 \( e_m \)（20, 100, 500 μm）、JRC分布类型（正态、对数正态）、水力开度 \( e_h \) 及由此定义的非均质性 [He 2022, pp. 7-8]
- **热-水-力耦合参数**：岩石基质有效热容 \((\rho c)_{eff}\)、有效热导率 \(\lambda_{eff}\)、传热系数 \(h\) 与裂缝内等效换热系数 \(h_{int} = 2h/e_h\)、Biot常数 \(\alpha_B\)、热膨胀系数 \(\alpha_T\)、弹性模量 \(E\)、泊松比 \(v\)、裂缝法向/切向刚度 \(k_n, k_s\) [He 2022, pp. 3-4]
- **性能评价指标**：热提取率（Heat extraction rate）、产出水温度、热回收持续时间、总热提取量、两个比率指标（Duration ratio index, Energy ratio index）[He 2022, pp. 1-2]

## Reusable Claims
1. 在基于DFN的增强型地热系统数值模型中，将裂缝处理为粗糙壁（通过JRC-水力开度非均质性表征）相较于平行板假设，会导致热提取率峰值下降且出现时间延迟，总热提取量减少，热回收周期延长。**适用条件**：二维THM耦合模拟，定压梯度边界，裂缝开度非均质性由JRC及力学开度控制；**证据**：[He 2022, pp. 1-2]；**限制**：未提供三维验证，且具体量化幅度取决于模型尺寸与裂缝方位。
2. 可以构建基于热提取持续时间和总产出能量的比值指标，用以定量比较粗糙壁与平行板模型的热回收性能差异。**适用条件**：相同裂缝几何拓扑和边界条件的DFN模型对比；**证据**：[He 2022, pp. 1-2]；**限制**：指标的具体定义和计算公式未在片段中给出。
3. 在DFN模型中，裂缝方位的改变会明显影响EGS的热回收性能。**适用条件**：二维正交双裂缝组DFN，裂缝密度一致；**证据**：[He 2022, pp. 1-2]；**限制**：方位敏感性可能依赖于模型尺寸与开度非均质性，具体趋势未从片段中确认。
4. 采用JRC与水力开度的经验关系 \( e_h = e_m^2 / JRC^{2.5} \) 可以间接、参数化地实现粗糙壁裂缝网络的水力非均质性。**适用条件**：适用于可获取宏观JRC分布的裂隙岩体，且 \( e_h \le e_m \)；**证据**：[He 2022, pp. 7-8]；**限制**：该经验公式基于特定岩体的现场数据拟合，普适性未验证，且未考虑粗糙度的各向异性。
5. 热提取性能评价中，传热系数的取值类型和大小会影响产出温度曲线，但当前缺乏一致的处理方法，其作用机制仍属开放问题。**适用条件**：THM框架内的裂缝-流体换热模拟；**证据**：[He 2022, pp. 2-4]；**限制**：片段中未开展系统的传热系数参数化研究。

## Candidate Concepts
- [[Enhanced Geothermal System (EGS)]]
- [[Discrete Fracture Network (DFN)]]
- [[Thermal-Hydraulic-Mechanical (THM) coupling]]
- [[Rough-walled fracture]]
- [[Joint Roughness Coefficient (JRC)]]
- [[Hydraulic aperture]]
- [[Mechanical aperture]]
- [[Aperture heterogeneity]]
- [[Heat transfer coefficient]]
- [[Heat extraction rate]]
- [[Fracture orientation]]
- [[Equivalent continuum method]]
- [[Poiseuille number]]
- [[Nusselt number]]
- [[Fracture stiffness]]
- [[Biot's constant]]
- [[Thermal consolidation]]

## Candidate Methods
- [[DFN modeling of fractured reservoirs]]
- [[THM coupling simulation (porous media + discrete fractures)]]
- [[JRC-based hydraulic aperture heterogeneity modeling]]
- [[Mesh sensitivity analysis for DFN]]
- [[Numerical validation with analytical solutions (single fracture heat transfer)]]
- [[Analytical solutions for thermal consolidation (Bai et al.)]]
- [[Ratio indices for thermal recovery duration and energy comparison]]
- [[Two-dimensional cross-fracture network generation]]
- [[Fixed pressure gradient boundary condition for EGS simulation]]

## Connections To Other Work
- 与采用等效连续介质方法简化地热储层的数值研究（如cite 10-12）对比，本研究采用 DFN 可以捕捉早期突破和长尾效应，但过去 DFN 研究多假设裂缝为平直板 [He 2022, pp. 2-3]。
- 本课题可连接到基于 JRC [[Joint Roughness Coefficient (JRC)]] 描述裂缝表面形貌的经典工作（Barton [18]），以及通过无量纲数（如 [[Poiseuille number]]、[[Nusselt number]]）分析单裂缝传热特性的实验研究 [He 2022, pp. 2]。
- 数值模型的验证依赖于二维单裂缝换热解析解和 [[Thermal consolidation]] 解析解（Bai et al. [43]），表明模型具备模拟多场耦合的基本能力 [He 2022, pp. 4-5]。
- 在宏观 JRC 分布方面，参考了 Oskarshamn/Forsmark 和 Bakhtiary 的现场数据，暗示可将方法扩展到实际场址尺度的 [[Site characterization]] 与 [[Fracture network statistics]] [He 2022, pp. 6-7]。
- 未从索引片段中发现与其他具体论文的直接比较或引用关系，但可从主题上连接到其他考虑粗糙裂缝换热的 [[EGS numerical modeling]] 工作。

## Open Questions
- 传热系数在不同流动-热传递机制下的恰当取值及其对产出温度曲线的具体影响仍不清楚 [He 2022, pp. 2-4]。
- 所提出的两个比率指标在更广泛的条件（三维模型、不同裂隙形态、非定常边界）下是否仍具有稳健性，未从索引片段中确认。
- 文中仅采用 JRC 的单参数经验关系来间接反映粗糙度，能否充分代表真实粗糙壁裂缝的沟槽流与惯性效应仍待探究。
- 对于其他粗糙度分布形式（如偏态分布、多峰分布）和对数正态、正态以外的统计特征，粗糙壁效应的敏感性未知。
- 模型结论来自概念化二维模型，推广至三维实际工程尺度的适用性需进一步验证。

## Source Coverage
本 Markdown 知识页依据所给 18 个索引片段编写，片段覆盖了摘要、引言（第1-2页）、模型假设与控制方程（第3-4页）、模型构建细则（第6-8页）、网格与计算设置（第8-9页）及部分验证结果（第4-5页）。结果部分的定量数据（如热提取率曲线、两个比率指标的具体数值）在片段中极少呈现，仅有摘要级别的定性描述；讨论部分和结论部分基本未被索引片段覆盖。因此，本页对整体学理和设计有较好呈现，但在详细的定量证据、敏感性分析结果和局限性反思方面可能存在关键信息缺失。
