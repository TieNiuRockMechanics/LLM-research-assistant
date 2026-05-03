---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-marji-the-explosive-fracturing-technique-analysis-for-highly-low-permeable-reservoirs-using"
title: "The Explosive Fracturing Technique Analysis for Highly Low Permeable Reservoirs Using Analytical, Displacement Discontinuity and Finite Difference Coupled Method."
status: "draft"
source_pdf: "data/papers/2023 - The explosive fracturing technique analysis for highly low permeable reservoirs using analytical, displacement discontinuity and finite difference coupled method.pdf"
collections:
  - "论文"
citation: "Marji, Mohammad Fatehi, et al. “The Explosive Fracturing Technique Analysis for Highly Low Permeable Reservoirs Using Analytical, Displacement Discontinuity and Finite Difference Coupled Method.” *Journal of Petroleum Geomechanics*, vol. 6, no. 3, autumn 2023, p. 44. DOI: 10.22107/JPG.2023.412506.1208."
indexed_texts: "12"
indexed_chars: "58727"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T13:22:55"
---

# The Explosive Fracturing Technique Analysis for Highly Low Permeable Reservoirs Using Analytical, Displacement Discontinuity and Finite Difference Coupled Method.

## One-line Summary
本研究提出并验证了一种耦合解析方法、显式有限差分法（FDM）和位移不连续法（DDM）的数值模拟方案，用于分析爆炸压裂在极低渗透储层中引起的径向裂缝起裂与扩展过程，并揭示了冲击波与气体压力在裂缝扩展中的耦合作用机制 [Marji 2023, pp. 1-3]。

## Research Question
如何通过结合冲击波与气体压力效应的解析-数值耦合方法，准确模拟低渗透储层井眼周围因爆炸引起的径向裂缝起裂与动态扩展过程，并评估其作为非常规储层增产技术的潜力？ [Marji 2023, pp. 1-3]

## Study Area / Data
研究以伊朗某油田的储层岩石为背景案例进行了模拟，但未从索引片段中确认具体的油田名称、岩性、埋深或储层物性参数。 [Marji 2023, pp. 3-4]

## Methods
本研究采用了一种三阶段耦合方法框架：
- **解析解验证**：基于Lame-Navier弹性动力学方程和格林函数解，推导了冲击波作用下井眼周围裂缝起裂的解析解，用于验证数值模型 [Marji 2023, pp. 1-4]。
- **冲击波起裂模拟 (FDM)**：使用二维显式有限差分程序FLAC2D，模拟爆炸冲击波在弹性连续介质中的传播和由此引起的径向裂缝起裂过程，模型边界采用粘性吸收边界以模拟无限域 [Marji 2023, pp. 8-9]。在FLAC2D中施加的压力脉冲波形由双重指数函数描述（公式22-26），该函数考虑了爆轰压力、频率相关衰减系数和井眼半径等因素 [Marji 2023, pp. 9-10]。
- **气体压力驱动扩展模拟 (DDM)**：基于间接边界元法，采用高阶位移不连续单元（具体实现于TDDQCR代码），模拟高压爆生气体准静态地驱动已有径向裂缝的进一步扩展 [Marji 2023, pp. 8-12]。气体压力被假定为爆轰压力的50%到60% [Marji 2023, pp. 10-12]。

## Key Findings
- **裂缝起裂模式**：有限差分模型（仅考虑冲击波）预测，井眼周围会形成约8条主要的对称径向裂缝，为后续气体压力驱动扩展提供了初始裂纹模式 [Marji 2023, pp. 9-10]。
- **裂缝扩展的主导机制**：数值模拟结果表明，高压爆生气体在驱动径向裂缝进一步扩展中起主导作用。气体压力驱动是井眼周围岩石径向裂缝扩展的主要机制 [Marji 2023, pp. 10-12]。
- **耦合模拟的有效性**：提出的耦合FDM-DDM方法能够完整模拟从冲击波起裂到气体驱动扩展的整个爆炸压裂过程，最终形成了长度不一的径向裂缝网络，有望提高井眼产能 [Marji 2023, pp. 10-12]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 爆炸冲击波可在井眼周围产生约8条主要的对称径向裂缝（忽略微裂纹和不成熟裂缝） | [Marji 2023, pp. 9-10] | 基于FLAC2D的有限差分模型，仅考虑冲击波作用，采用特定波形和模型参数。 | 此为裂缝起裂阶段的模拟结果。 |
| 高压爆生气体是驱动径向裂缝扩展的主要机制，因其在裂缝中流动时施加极高压力 | [Marji 2023, pp. 10-12] | 基于TDDQCR代码的间接边界元模拟，气体压力约为爆轰压力的50%-60%。 | 此为裂缝扩展阶段的模拟结果。 |
| 爆炸压力脉冲波形可用双重指数函数近似，其中最大壁面压力、衰减系数与岩石的密度、P波波速、体积模量和剪切模量相关 | [Marji 2023, pp. 9-10] | 结合了Brady和Brown (2005)的建议公式（公式22-26）。 | 关键输入参数方程，用于FDM模拟。 |
| 通过格林函数解可推导出爆炸冲击波产生的位移、应变和应力场的解析表达式 | [Marji 2023, pp. 4-6] | 基于线弹性、各向同性、均质连续介质假设，并应用于二维问题。 | 解析解用于验证数值方法的正确性。 |

## Limitations
- 本研究的数值模拟是基于二维模型的，可能未完全捕捉实际三维空间中裂缝网络的复杂几何形态和相互作用 [Marji 2023, pp. 3-4]。
- 模型仅考虑了岩石的弹性行为，未从索引片段中确认是否考虑了岩石的非弹性变形、破裂过程区或天然裂缝的影响。
- 气体压力被假定为爆轰压力的一个固定比例（50%-60%），这个简化可能不完全符合实际复杂的爆生气体压力演化过程 [Marji 2023, pp. 10-12]。
- 裂缝扩展阶段的模拟为准静态，并未与冲击波阶段的动态效应进行实时双向耦合。
- 模拟结果仅展示了8条对称裂缝的模式，但未从索引片段中确认是否考虑了储层非均质性或地应力不均匀性导致的非对称裂缝扩展。

## Assumptions / Conditions
- **介质属性**：岩石被假定为**弹性、各向同性、均质且连续**的介质 [Marji 2023, pp. 6-8]。
- **模型维度**：问题被简化为二维平面应变或平面应力问题。
- **加载阶段分离**：裂缝起裂过程主要由爆炸冲击波的动态作用控制，而后续扩展过程则由准静态高压气体压力主导，这两个阶段在模拟中是先FDM后DDM的顺序耦合 [Marji 2023, pp. 10-12]。
- **气体压力模型**：作用于裂缝壁面的气体压力简化为爆炸压力的一个固定百分比（约50%-60%） [Marji 2023, pp. 10-12]。
- **数值边界**：在FDM模拟中，采用了粘性吸收边界条件来模拟无限大岩体中的波传播，以避免边界反射干扰 [Marji 2023, pp. 8-9]。

## Key Variables / Parameters
- **输入参数**：
    - 岩石力学参数：密度 (ρ)，P波波速 (c<sub>p</sub>)，S波波速 (c<sub>s</sub>)，体积模量 (K)，剪切模量 (μ)。
    - 爆源参数：最大壁面压力 (P<sub>0</sub>)，井眼半径 (r<sub>b</sub>)。
    - 压力波形参数：频率依赖的衰减系数 (α, β)，归一化因子 (N) [Marji 2023, pp. 9-10]。
- **关键变量**：
    - 应力 (σ<sub>ij</sub>)，应变 (ε<sub>ij</sub>)，位移 (u<sub>j</sub>) [Marji 2023, pp. 4-6]。
    - 位移不连续量：裂缝表面的剪切 (D<sub>x</sub>) 和法向 (D<sub>y</sub>) 不连续度 [Marji 2023, pp. 6-8]。
    - 爆炸压力 (P)，随时间变化 [Marji 2023, pp. 9-10]。

## Reusable Claims
- **Claim 1**：在弹性岩石介质中，仅由爆炸冲击波作用导致的井周裂缝起裂会形成一组大致均匀分布的径向裂缝，其数量（本模拟为8条）为后续气体压力驱动扩展提供了初始几何构型。**条件**：适用于均质、各向同性、连续岩体，不考虑地应力差异 [Marji 2023, pp. 9-10]。**限制**：裂缝数量受模型参数和材料属性影响，未考虑微裂纹合并过程。
- **Claim 2**：在爆炸压裂中，高压爆生气体（压力约为爆轰压力的50%-60%）是驱动径向裂缝显著扩展的主导机制，而非初始的冲击波。**条件**：基于裂缝面承受均匀或准静态气体压力作用的假设 [Marji 2023, pp. 10-12]。**限制**：此结论来自将冲击波与气体压力效应分阶段解耦的数值模拟。
- **Claim 3**：采用格林函数可用于推导爆炸冲击波在弹性体中引起的应力-应变场的解析解，并可作为验证有限差分法（FDM）动态模拟精度的基准。**条件**：限于线弹性动力学框架，采用特定的指数型爆炸压力脉冲函数 [Marji 2023, pp. 4-6]。**限制**：解析解对复杂几何和本构关系的扩展性有限。

## Candidate Concepts
- [[explosive fracturing]]
- [[low permeable reservoirs]]
- [[crack propagation]]
- [[shock wave]]
- [[gas-driven fracturing]]
- [[displacement discontinuity method]]
- [[finite difference method]]
- [[Green's function]]
- [[rock blasting]]
- [[fracture mechanics]]

## Candidate Methods
- [[coupled FDM-DDM]]
- [[analytical solution (Lame-Navier)]]
- [[higher-order displacement discontinuity]]
- [[FLAC2D]]
- [[TDDQCR code]]
- [[absorbing boundary condition]]

## Connections To Other Work
- 本研究将爆炸压裂与其他非水基压裂技术（如泡沫压裂、LPG压裂）进行了对比，指出其是一种成本效益高且环境友好的增产方法（引用了Rogala等人的研究） [Marji 2023, pp. 2-3]。
- 引用了Zhu等人关于电脉冲可控冲击波提高渗透率的工作，以及Sheng等人、Settgast等人关于爆炸压裂流动行为模型和晚期气体驱动裂缝模型的研究，表明该工作建立在已有的爆炸/脉冲压裂研究基础之上 [Marji 2023, pp. 2-3]。
- 在爆炸加载机制上，引用了Donnell等人提出的冲击波与气体压力联合作用的概念 [Marji 2023, pp. 3-4]。
- 方法上，继承了线性弹性断裂力学（LEFM）和边界元法在岩石断裂力学中的应用，可连接到[[hydraulic fracturing simulation]]、[[dynamic fracture mechanics]]等主题。

## Open Questions
- 未从索引片段中确认该耦合方法对实际三维、非均质储层的预测能力如何。
- 未从索引片段中确认该技术在现场应用中的经济成本、环境风险和增产效果与水力压裂的定量对比结果。
- 如何将模拟中的8条对称裂缝模式推广到更一般的地应力条件下的非对称、随机裂缝网络？未从索引片段中确认相关讨论。

## Source Coverage
本页面的所有信息均源自提供的12个索引片段，这些片段主要覆盖了论文的摘要、引言、方法理论与部分数值模拟结果。信息集中在方法的推导（解析解、FDM、DDM）、耦合策略的描述和模拟发现的裂缝模式。然而，关于案例研究的详细参数（如表1）、模型验证的具体对比、定量化的增产效果评估、详细的文献综述讨论和完整的结论等内容，在索引片段中可能缺失或覆盖不全。
