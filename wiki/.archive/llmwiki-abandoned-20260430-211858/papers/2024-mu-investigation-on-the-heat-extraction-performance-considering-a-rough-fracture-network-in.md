---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2024-mu-investigation-on-the-heat-extraction-performance-considering-a-rough-fracture-network-in"
title: "Investigation on the Heat Extraction Performance Considering a Rough Fracture Network in Heterogeneous Reservoirs."
status: "draft"
source_pdf: "data/papers/2024 - Investigation on the heat extraction performance considering a rough fracture network in heterogeneous reservoirs.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Mu, Shuxing, et al. \"Investigation on the Heat Extraction Performance Considering a Rough Fracture Network in Heterogeneous Reservoirs.\" *Renewable Energy*, vol. 233, 2024, article 121160. Accessed 2026."
indexed_texts: "12"
indexed_chars: "55265"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T14:10:27"
---

# Investigation on the Heat Extraction Performance Considering a Rough Fracture Network in Heterogeneous Reservoirs.

## One-line Summary
本研究建立了一个新的三维地热开采数值模型，该模型考虑了储层非均质性和基于分形函数的粗糙离散裂缝网络，以研究地质-工程参数对采热性能的影响 [Mu 2024, pp. 1-1]。

## Research Question
如何评估粗糙裂缝网络与非均质储层耦合作用下的地热开采热提取性能？具体探究裂缝数量、裂缝宽度、裂缝粗糙度系数、注入速率、注入温度和地温梯度等参数对采热的影响 [Mu 2024, pp. 1-1]。

## Study Area / Data
- **研究区**: 以青海共和盆地的恰卜恰（Qiabuqia）地热田为例 [Mu 2024, pp. 6-8]。
- **数据来源**: 参考了恰卜恰地热田干热岩（HDR）取心的岩石物理实验结果。
    - 岩石密度范围：1430 到 3710 kg/m³，平均值为 2607 kg/m³ [Mu 2024, pp. 6-8]。
    - 热导率范围：1.85 到 3.20 W/(m·K)，平均值为 2.51 W/(m·K) [Mu 2024, pp. 6-8]。
    - 热容范围：640 到 880 J/(kg·K)，平均值为 754.4 J/(kg·K) [Mu 2024, pp. 6-8]。
    - 基质孔隙度范围：3.85% 到 6.05%，平均值为 5% [Mu 2024, pp. 6-8]。
    - 渗透率范围：1.52 × 10⁻¹⁴ 到 2.56 × 10⁻¹⁴ m²，平均值为 2 × 10⁻¹⁴ m² [Mu 2024, pp. 6-8]。

## Methods
1.  **建立三维数值模型**: 建立了一个三维“井-裂缝-储层”耦合的数值模型 [Mu 2024, pp. 1-3]。
2.  **描述储层非均质性**: 利用空间频率（spatial frequency）来描述储层多个物理参数（如密度、热导率、热容、孔隙度、渗透率）的非均质性 [Mu 2024, pp. 1-1, pp. 4-6]。
3.  **构建粗糙裂缝**: 基于Weierstrass-Mandelbrot分形函数构建粗糙离散裂缝网络（Discrete Fracture Network, DFN） [Mu 2024, pp. 1-1]。
4.  **控制方程**:
    - 将裂隙岩体视为连续多孔介质，使用运动方程和质量守恒方程控制流体流动 [Mu 2024, pp. 3-4]。
    - 利用达西定律（Darcy’s law）描述基质中的流体速度 [Mu 2024, pp. 3-4]。
    - 使用立方定律（cubic law）计算裂缝渗透率 `k_f`，公式中引入了粗糙度系数 `f_f` 进行修正 [Mu 2024, pp. 3-4]。
    - 分别建立岩石基质和裂缝中的能量平衡方程，以描述热交换过程 [Mu 2024, pp. 3-4]。
5.  **求解方案**: 考虑了压力场和温度场的耦合，采用交错方案（staggered scheme）独立求解各物理场，并利用Newton-Raphson方法和后向差分公式进行非线性迭代和时间步进 [Mu 2024, pp. 6-8]。
6.  **模型验证**: 将单裂缝传热的数值解与解析解（Eq. (23)）进行了对比验证 [Mu 2024, pp. 6-8]。模型具体参数设定如下表所示 [Mu 2024, pp. 4-6]：

| 参数 (Properties) | 值 (Value) | 单位 (Unit) |
| :--- | :--- | :--- |
| 井筒直径 (Wells diameter) | 0.1 | m |
| 水力梯度 (Hydraulic gradient) | 1 | mm/m |
| 注入温度 (Injection temperature) | 333 | K |
| 注入速率 (Injection rate) | 120 | l/s |
| 地温梯度 (Geothermal gradient) | 0.03 | K/m |
| 裂缝宽度 (Fracture width) | 0.002 | m |
| 裂缝粗糙度系数 (Fracture roughness coefficient) | 1.6 | / |
| 分形维数 (Fractal dimension) | 2.1 | / |
| 特征尺度参数 (Characteristic scale parameter) | 1e-4 | / |

7. **性能评价指标**: 使用生产温度（production temperature）、产出能量（produced energy）和有效电功率（effective electric power）来评价热提取性能。模拟时间为80年 [Mu 2024, pp. 8-10]。有效电功率的计算考虑了最大热能-机械能转换效率 `η`，取值为0.45 [Mu 2024, pp. 8-10]。

## Key Findings
1.  **裂缝数量的影响**: 当裂缝数量增加到7-9条后，由于优先流动通道已经形成，增加裂缝数量对低温区域扩散的增量影响逐渐减弱 [Mu 2024, pp. 1-1, pp. 8-10]。
2.  **裂缝宽度的影响**: 裂缝宽度增加会加剧热突破现象。当裂缝宽度从0.5 mm增加到3 mm时，80年后的平均生产温度下降6.08%，产出能量下降38.69%，有效电功率下降47.11% [Mu 2024, pp. 10-12]。
3.  **裂缝粗糙度系数的影响**: 增加裂缝粗糙度系数可以延缓热突破并提高采热性能。当粗糙度系数从1.6增加到11.6时，有效电功率增加了19.44% [Mu 2024, pp. 1-1, pp. 10-12]。每增加2个单位的粗糙度系数，生产温度、产出能量和有效电功率均有百分比提升 [Mu 2024, pp. 10-12]。
4.  **注入速率的影响**: 增加注入速率会加剧热突破，但总体上增强了采热性能。当注入速率从60 l/s增加到160 l/s时，有效电功率增加了55.7% [Mu 2024, pp. 1-1]。
5.  **注入温度的影响**: 增加注入温度可以延缓热突破，但会降低产注温差，从而降低热回收效率和有效电功率。例如，注入温度每增加10 K，产出能量和有效电功率显著下降。综合考虑热提取和井筒结垢问题，建议注入温度为333 K – 353 K [Mu 2024, pp. 1-1, pp. 12-14]。
6.  **地温梯度的影响**: 地温梯度对低温流体的扩散面积影响很小，只影响储层温度的绝对值。地温梯度增加会提高产出温度，但不影响热突破现象 [Mu 2024, pp. 12-14]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 裂缝数量增加到7-9条后，对低温区域扩散的影响逐渐减弱。 | [Mu 2024, pp. 1-1, pp. 8-10] | 其他参数同基础模型设定。基础注入速率120 l/s，注入温度333 K，裂缝宽度2 mm。 | 模型尺寸1000m × 1000m × 1000m，模拟80年。 |
| 裂缝宽度从0.5 mm增加到3 mm，80年后平均生产温度降6.08%，产出能量降38.69%，有效电功率降47.11%。 | [Mu 2024, pp. 10-12] | 其他参数同基础模型设定。 | 裂缝宽度增加减少了流体与岩石的热交换时间。 |
| 裂缝粗糙度系数从1.6增加到11.6，有效电功率增加19.44%。 | [Mu 2024, pp. 1-1, pp. 10-12] | 其他参数同基础模型设定。 | 粗糙度系数增加延缓热突破，粗糙度系数每增加2，产出能量和有效电功率有具体百分比提升。 |
| 注入速率从60 l/s增加到160 l/s，有效电功率增加55.7%。 | [Mu 2024, pp. 1-1] | 其他参数同基础模型设定。注入温度333 K，裂缝宽度2 mm。 | 增加注入速率加剧热突破，但总体上增强了采热性能。 |
| 注入温度每增加10 K，产出能量和有效电功率显著下降。建议注入温度为333 K – 353 K。 | [Mu 2024, pp. 1-1, pp. 12-14] | 其他参数同基础模型设定。基础注入速率120 l/s，裂缝宽度2 mm。 | 注入温度低于333 K可能导致井筒结垢。 |

## Limitations
1.  数值模型未从索引片段中确认是否经过现场尺度数据的验证，目前仅与单裂缝传热的解析解进行了对比 [Mu 2024, pp. 6-8]。
2.  模型假设中是忽略了热辐射的，未确认是否考虑其他物理化学过程（如化学反应、岩石溶解与沉淀、流体相变）的影响 [Mu 2024, pp. 3-4]。
3.  未从索引片段中确认模型计算效率和规模存在的潜在限制。
4.  未从索引片段中确认对裂缝网络几何形态的研究是否涵盖了所有可能的分布（如裂缝长度、方向和连接性的多样性），文中仅提及所有裂缝有相同的物理性质，并使用了特定长度（600m）的裂缝 [Mu 2024, pp. 6-8]。

## Assumptions / Conditions
1.  **连续介质假设**: 裂隙岩体被视为连续多孔介质 [Mu 2024, pp. 3-4]。
2.  **忽略热辐射**: 模型假设中未考虑热辐射效应 [Mu 2024, pp. 3-4]。
3.  **裂缝物理性质**: 模型中的所有裂缝具有相同的物理性质 [Mu 2024, pp. 6-8]。
4.  **边界条件**: 外部边界固定且无流动，且绝热 [Mu 2024, pp. 6-8]。
5.  **采注平衡**: 生产井以与注入井相同的速率运行，以维持整个储层的注采平衡 [Mu 2024, pp. 8-10]。
6.  **模型尺寸与裂缝**: 数值模型尺寸为 1000 m × 1000 m × 1000 m，内含长度为 600 m 的粗裂缝 [Mu 2024, pp. 6-8]。
7.  **热能转换效率**: 有效电功率计算时，最大转换效率η一般取0.45 [Mu 2024, pp. 8-10]。
8.  **空间频率构建非均质**: 在利用空间频率描述非均质性时，最短波长由最大整数频率A，B，C决定（即λ_xmin = 1/A）[Mu 2024, pp. 4-6]。

## Key Variables / Parameters
- **地质参数**: 裂缝数量 (Fracture number), 裂缝宽度 (Fracture width, d_f), 裂缝粗糙度系数 (Fracture roughness coefficient, f_f), 裂缝渗透率 (k_f), 基质渗透率 (k), 基质孔隙度 (φ) [Mu 2024, pp. 1-1, pp. 3-4]。
- **工程参数**: 注入温度 (Injection temperature, T_inj), 注入速率 (Injection rate) [Mu 2024, pp. 1-1]。
- **性能指标**: 生产温度 (Production temperature, T_pro), 产出能量 (Produced energy), 有效电功率 (Effective electric power) [Mu 2024, pp. 8-10]。
- **材料参数**: 岩石密度 (ρ_s), 岩石热容 (C_p,s), 岩石热导率 (λ_s), 流体热容 (C_p,f) [Mu 2024, pp. 3-4, pp. 6-8]。
- **其他参数**: 地温梯度 (Geothermal gradient), 分形维数 (Fractal dimension, D), 特征尺度参数 (Characteristic scale parameter, G), 移除/排斥温度 (T_rej) [Mu 2024, pp. 4-6, pp. 8-10, pp. 12-14]。

## Reusable Claims
- **Claim 1 [Mu 2024, pp. 1-1, pp. 1-3]**： 在EGS数值模拟中，若忽略裂缝的实际粗糙形态和储层的非均质性，模型将与实际储层条件不符。因此，使用Weierstrass-Mandelbrot分形函数构建粗糙裂缝，并利用空间频率描述储层物性非均质性，是建立一个更现实的数值模型的有效方法。
- **Claim 2 [Mu 2024, pp. 3-4]**： 对于粗糙裂缝渗透率的计算，可以在立方定律中引入粗糙度系数（f_f）进行修正，公式为 `k_f = d_f^2 / (12 f_f)`。这适用于模型中裂缝被离散为二维单元，且粗糙度被简化为一个系数的场景。
- **Claim 3 [Mu 2024, pp. 10-12]**： 裂缝宽度增加会加剧热突破并降低热提取性能。证据显示，裂缝宽度从0.5mm增至3mm时，有效电功率下降47.11%，这是因为更宽的裂缝减少了低温流体和高温岩石的热交换时间。
- **Claim 4 [Mu 2024, pp. 10-12]**： 增加裂缝粗糙度系数可以有效延缓热突破，并持续提高热提取性能。例如，当粗糙度系数从1.6增加到11.6时，有效电功率可增加19.44%。
- **Claim 5 [Mu 2024, pp. 12-14]**： 增加注入温度虽能延缓热突破，但会导致产注温差减小，从而降低热回收效率和产出能量。因此，注入温度的选择是在延缓热突破和维持高热回收效率之间的权衡。低于333 K还存在结垢风险，故建议区间为333-353 K。

## Candidate Concepts
- [[Enhanced Geothermal System (EGS)]]
- [[Rough Fracture Network]]
- [[Discrete Fracture Network (DFN)]]
- [[Heterogeneous Reservoir]]
- [[Fractal Dimension in Rock Mechanics]]
- [[Thermal Breakthrough]]
- [[Heat Extraction Performance]]
- [[Weierstrass-Mandelbrot Fractal Function]]

## Candidate Methods
- [[Three-Dimensional Numerical Model]]
- [[Darcy's Law]]
- [[Cubic Law with Roughness Coefficient]]
- [[Spatial Frequency Analysis for Heterogeneity]]
- [[Finite Element Method (FEM)]]
- [[Newton-Raphson Method]]
- [[Backward Difference Formula (BDF)]]
- [[Staggered Solution Scheme]]

## Connections To Other Work
- 本文指出，以往研究往往将裂缝描述为理想形态（如光滑表面），并假设储层为均质 [Mu 2024, pp. 1-3]。这使其与以下使用简化裂缝或均质储层假设的候选方法形成对比：[[Ideal Fracture Morphology Models]]， [[Homogeneous Reservoir Models]]。
- 本文在方法上可连接到使用不同储层非均质性实现方式的[[Stochastic Reservoir Modeling]]，以及基于其他分形函数构建裂缝的[[Fracture Surface Generation Techniques]]。
- 本文的模型建立在井-裂缝-储层耦合的框架下，其流体路径主要由井和裂缝网络决定 [Mu 2024, pp. 1-3]，这与[[Wellbore-Reservoir Coupling]]及[[Fracture-Dominated Flow Systems]]概念相关。

## Open Questions
1.  该三维数值模型的计算效率和可扩展性如何？能否应用于更大尺度（如整个地热田）或更复杂裂缝网络（如包含成千上万条裂缝）的模拟？未从索引片段中确认。
2.  模型是否能直接应用于除共和盆地之外的其他地热储层？其在其他地质条件下的通用性未从索引片段中确认。
3.  在长期热开采（>80年）过程中，热-流-固-化（THMC）多场耦合效应（尤其是化学沉淀和岩石力学变形）对粗糙裂缝网络渗透率和采热性能演化的影响是什么？未从索引片段中确认。
4.  如何基于本研究的发现来优化工程参数，以实现特定地热田的经济效益最大化？文章提供了参数敏感性分析，但未从索引片段中确认是否提出了综合优化策略。

## Source Coverage
本知识页内容基于提供的12个论文索引片段，覆盖了文章标题、摘要、部分引言、控制方程、参数设定、部分模拟结果（关于裂缝数量、宽度、粗糙度、注入温度、地温梯度）和结论。内容已覆盖文章的主要创新点和方法，但部分结果（如注入速率的具体影响）描述可能不够详尽，引用信息也不完整（例如第9页和第10页与裂缝粗糙度相关的有效电功率增长数据缺失）。可能缺失详尽的模型验证对比、讨论章节的深入分析以及最终的结论总结。
