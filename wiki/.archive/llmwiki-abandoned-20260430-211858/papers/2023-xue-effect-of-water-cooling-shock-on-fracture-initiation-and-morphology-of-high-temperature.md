---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-xue-effect-of-water-cooling-shock-on-fracture-initiation-and-morphology-of-high-temperature"
title: "Effect of Water-Cooling Shock on Fracture Initiation and Morphology of High-Temperature Granite: Application of Hydraulic Fracturing to Enhanced Geothermal Systems."
status: "draft"
source_pdf: "data/papers/2023 - Effect of water-cooling shock on fracture initiation and morphology of high-temperature granite Application of hydraulic fracturing to enhanced geothermal systems.pdf"
collections:
  - "1文章:2D-3D分形关系"
  - "论文"
citation: "Xue, Yi, et al. \"Effect of Water-Cooling Shock on Fracture Initiation and Morphology of High-Temperature Granite: Application of Hydraulic Fracturing to Enhanced Geothermal Systems.\" *Applied Energy*, vol. 337, 2023, 120858. doi:10.1016/j.apenergy.2023.120858."
indexed_texts: "17"
indexed_chars: "80285"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T12:11:46"
---

# Effect of Water-Cooling Shock on Fracture Initiation and Morphology of High-Temperature Granite: Application of Hydraulic Fracturing to Enhanced Geothermal Systems.

## One-line Summary
本文通过热-流-固（THM）耦合数值模型与室内实验，研究了水冷冲击对高温花岗岩水力压裂起裂压力与裂缝形态的影响，以期为增强型地热系统（EGS）的人工热储建造提供依据 [Xue 2023, pp. 1-2]。

## Research Question
在干热岩（HDR）水力压裂过程中，由低温流体注入引起的水冷冲击如何导致高温花岗岩力学参数劣化，并进一步影响裂缝的起裂与最终形态？ [Xue 2023, pp. 1-2]。

## Study Area / Data
研究结合了数值模拟与物理实验。实验所用花岗岩样来自中国福建省南安市，被加工成直径50 mm、高100 mm的圆柱体，并进行了20°C至600°C的加热和水冷处理 [Xue 2023, pp. 2-3]。

## Methods
1.  **理论模型建立**：建立了一个热-流-固（THM）耦合模型，该模型耦合了固体变形、流体渗流和热传导方程，用于分析干热岩水力压裂的起裂机制 [Xue 2023, pp. 1-2]。
2.  **水冷冲击效应表征**：基于加热和水冷处理后的花岗岩力学实验结果（包括本文实验及文献数据），建立了水冷冲击引起的冷却幅度 (ΔT) 与弹性模量、抗拉强度劣化程度之间的函数关系 [Xue 2023, pp. 4-5]。
3.  **模型验证**：通过将数值模拟结果与理论解析解（如裂缝诱导应力场）以及高温花岗岩的室内水力压裂实验结果进行对比，验证了耦合模型的有效性 [Xue 2023, pp. 1-2, 8-10]。
4.  **数值模拟软件**：使用COMSOL Multiphysics软件和MATLAB平台进行多物理场交叉耦合模拟 [Xue 2023, pp. 5-7]。

## Key Findings
1.  **水冷冲击导致力学参数劣化**：高温花岗岩经水冷冲击后，其弹性模量和抗拉强度会随冷却幅度（ΔT）的增大而显著降低。文中给出了描述这一劣化过程的经验公式（Eqs. 16-17） [Xue 2023, pp. 4-5]。
2.  **裂缝起裂与形态受影响**：水冷冲击被确认为是影响干热岩水力压裂过程中裂缝起裂和最终形态的关键因素。水冷诱发的热应力会加速裂缝的起裂与扩展 [Xue 2023, pp. 1-2]。
3.  **实验与模拟相符**：通过高温花岗岩水冷压裂实验验证了数值模拟结果。实验表明，加热温度越高，水冷处理后试件的裂纹数量越多，这与力学参数劣化直接相关 [Xue 2023, pp. 7-8]。模拟结果能够准确重现实验中裂缝从边界起裂并向中心延伸形成环形分布的形态与数量 [Xue 2023, pp. 8-10]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 水冷冲击后花岗岩试件中新生成的裂纹最多。 | [Wu et al. 2021, cited in Xue 2023, pp. 2-3] | 对比了高温花岗岩在烤箱冷却、空气冷却和水冷却后的力学性质。 | 间接引用，原文未提供页码。 |
| 水冷后花岗岩的弹性模量和抗拉强度随加热温度升高而降低。 | [Xue 2023, pp. 2-3, Table 1] | 总结了文献中不同温度（最高600°C）下的实验结果。 | 本文自身实验数据与文献数据。 |
| 水冷冲击劣化函数被建立：E(ΔT) 和 f_t(ΔT)。 | [Xue 2023, pp. 4-5, Eqs. 16-17] | 基于归一化处理后的实验数据。 | 冷却幅度ΔT是初始温度与当前温度的差值。 |
| 数值计算的诱导应力与解析解匹配良好。 | [Xue 2023, pp. 8-10, Fig. 15] | 简化模型，忽略温度影响，仅关注力学效应。 | 对比了均质（m=100）和非均质（m=5）条件下的结果。 |
| 模拟的裂缝形态与数量与实验观察结果吻合。 | [Xue 2023, pp. 8-10, Fig. 12] | 模型尺寸与参数与试验试件一致。 | 裂缝从边界起裂并向中心延伸。 |

## Limitations
1.  未从索引片段中确认数值模型对复杂三维裂缝网络交汇与扩展的模拟能力。
2.  水冷冲击劣化函数（Eqs. 16-17）是基于特定花岗岩（南安市）的实验数据回归得到的，其在其他岩性或其他温度范围下的普适性未从索引片段中确认 [Xue 2023, pp. 4-5]。
3.  模型验证解析解部分忽略了温度效应 [Xue 2023, pp. 8-10]。

## Assumptions / Conditions
1.  模型假设固体和流体始终处于局部热平衡状态（Eq. 7） [Xue 2023, pp. 3-4]。
2.  花岗岩被视为具有弹塑性性质，并采用应力-软化模型（而非弹性-脆性模型）来描述其在高应力和高温下的应力-应变特征 [Xue 2023, pp. 3-4]。
3.  数值模拟中使用了特定的物理力学参数，如最大水平主应力15 MPa，最小水平主应力10 MPa，初始渗透率1 mD等（Table 2） [Xue 2023, pp. 8-10]。

## Key Variables / Parameters
-   **独立变量**：冷却幅度 ΔT (cooling amplitude) [Xue 2023, pp. 4-5]。
-   **关键力学参数**：弹性模量 E (elastic modulus)，抗拉强度 f_t (tensile strength)， Biot系数 α，损伤变量 D [Xue 2023, pp. 3-5]。
-   **物理场变量**：孔隙水压力 p，体积应变 ε_v，温度 T，渗透率 k [Xue 2023, pp. 3-4]。
-   **材料参数**：岩石密度 ρ，热传导系数 λ_s，热膨胀系数 α_T，孔隙率 ϕ，比热容 C_ps [Xue 2023, pp. 8-10, Table 2]。
-   **模型指标**：均质度 m (homogeneity index) [Xue 2023, pp. 8-10]。

## Reusable Claims
1.  **[适用于高温花岗岩]在水力压裂模拟中，水冷冲击的效应可以通过建立冷却幅度(ΔT)与弹性模量、抗拉强度的劣化函数来表征**，具体函数形式为 `E(ΔT) = E(T_0)[1.348 - 0.347e^(0.00215ΔT)]` 和 `f_t(ΔT) = f_t(T_0)[1.31 - 0.31e^(0.002ΔT)]` [Xue 2023, pp. 4-5]。该方法的限制是函数参数来源于特定花岗岩的实验数据回归。
2.  **[适用于数值模拟]在进行水冷冲击数值模拟时，参数更新应分步进行：第一步根据冷却幅度更新由热冲击直接导致的抗拉强度和弹性模量劣化；第二步再根据损伤计算结果更新弹性模量、渗透率和热传导系数等参数** [Xue 2023, pp. 5-7]。
3.  **[基于实验证据]水冷处理后，花岗岩的力学性能劣化程度与加热温度正相关，表现为更高温度处理后试件裂纹数量增加、卸载压缩破坏更剧烈、巴西劈裂可能出现次生裂纹** [Xue 2023, pp. 7-8]。

## Candidate Concepts
-   [[Enhanced Geothermal System (EGS)]]
-   [[Hydraulic Fracturing]]
-   [[Water-cooling shock]]
-   [[Thermal-Hydraulic-Mechanical (THM) Coupling]]
-   [[Hot Dry Rock (HDR)]]
-   [[Fracture initiation pressure]]
-   [[Fracture morphology]]
-   [[Damage variable]]
-   [[Strain-softening model]]

## Candidate Methods
-   [[THM coupling model]]
-   [[Fracture criterion]]
-   [[Damage evolution equation]]
-   [[Numerical simulation]]
-   [[COMSOL Multiphysics]]
-   [[MATLAB]]
-   [[Uniaxial compression test]]
-   [[Brazilian splitting test]]
-   [[Stress shadow effect analysis]]

## Connections To Other Work
-   **与ECS模型的关系**：本文研究的THM耦合模型是ECS应用的基础问题，文中提及了Aliyu和Archer等人关于多裂缝储层优化的THM模型研究 [Xue 2023, pp. 2-2]。
-   **与冷却流体类型研究的关系**：文中引述了Kang等人对比空气、水和液氮冷却对花岗岩力学性质影响的工作，表明不同冷却介质引起的热冲击效应是可比对的 [Xue 2023, pp. 2-3]。
-   **与细观模拟方法的关系**：文中引用了Tomac和Gutierrez使用[[bonded particle model]]从微观角度模拟热效应对裂缝扩展影响的研究 [Xue 2023, pp. 2-3]。

## Open Questions
-   水冷冲击对水力压裂效果的影响在不同的原始地应力场（如正断层、走滑断层应力机制）下是否具有普遍规律？未从索引片段中确认。
-   除弹性模量和抗拉强度外，水冷冲击对渗透率、热传导系数等参数演化的直接影响，在模型中是如何量化考虑的？当前索引片段主要展示了通过损伤变量间接影响这些参数，直接影响未详述。

## Source Coverage
本页依据17个提供的索引片段编写，主要覆盖了论文的**摘要、引言（问题提出与文献综述）、方法论（控制方程和模型建立）、关键结果（实验与模拟对比）和部分验证**内容。可能缺失的信息包括：更详细的参数敏感性分析、对特定地质工程案例的应用模拟、以及完整的讨论与结论部分。
