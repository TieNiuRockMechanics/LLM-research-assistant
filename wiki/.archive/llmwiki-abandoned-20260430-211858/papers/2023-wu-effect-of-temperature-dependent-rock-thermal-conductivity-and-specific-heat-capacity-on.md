---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-wu-effect-of-temperature-dependent-rock-thermal-conductivity-and-specific-heat-capacity-on"
title: "Effect of Temperature-Dependent Rock Thermal Conductivity and Specific Heat Capacity on Heat Recovery in an Enhanced Geothermal System."
status: "draft"
source_pdf: "data/papers/2023 - Effect of temperature-dependent rock thermal conductivity and specific heat capacity on heat recovery in an enhanced geothermal system.pdf"
collections:
  - "论文"
citation: "Wu, Hui, et al. \"Effect of Temperature-Dependent Rock Thermal Conductivity and Specific Heat Capacity on Heat Recovery in an Enhanced Geothermal System.\" *Rock Mechanics Bulletin*, 2023. DOI: 10.1016/j.rockmb.2023.100045."
indexed_texts: "8"
indexed_chars: "38627"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T12:10:25"
---

# Effect of Temperature-Dependent Rock Thermal Conductivity and Specific Heat Capacity on Heat Recovery in an Enhanced Geothermal System.

## One-line Summary

本研究通过数值模拟探究岩石热导率和比热容随温度变化的特性对增强型地热系统热采收性能的影响，发现二者对热穿透曲线和生产寿命的影响在总体上相互抵消，采用室温下测量的恒定参数可提供可接受的预测精度。[Wu 2023, pp. 1-1]

## Research Question

岩石热导率和比热容随温度变化的特性，如何以及在多大程度上影响增强型地热系统的长期热采收性能和模拟预测？[Wu 2023, pp. 1-1]

## Study Area / Data

未从索引片段中确认具体的实际研究区域。模拟基于一个场级尺度的单裂隙EGS概念模型，模型尺寸为3000 × 3000 × 3000 立方米，中心有一条直径800米的水平主导裂隙。[Wu 2023, pp. 3-3]
模型的温度和物性关系基于前人的实验数据拟合，如Fu et al. (2019), Vosteen and Schellschmidt (2003), Berman and Brown (1985)。[Wu 2023, pp. 3-3]

## Methods

本研究构建了一个场级尺度的单裂隙增强型地热系统模型，模拟了与热采收相关的热-水耦合过程。[Wu 2023, pp. 3-3]
数值模拟采用美国劳伦斯利弗莫尔国家实验室开发的并行多物理场仿真平台GEOS。[Wu 2023, pp. 3-3]
模型中引入了前人实验研究中的两组方程（方程集1和2），用以描述岩石热导率（K）和比热容（Cp）随温度（T）变化的定量关系。具体为：热导率采用Fu et al. (2019)的方程，比热容采用Berman and Brown (1985)的方程，并使用Fu et al. (2019)和Vosteen and Schellschmidt (2003)的实验数据进行拟合。[Wu 2023, pp. 3-3]
通过对比不同情景（如K和Cp均随温度变化、仅Cp随T变化而K恒定在20°C或200°C值、K和Cp均恒定）的模拟结果，分析其影响。[Wu 2023, pp. 5-6]
还进一步分析了不同注入温度（30°C, 50°C, 70°C）和裂隙开度（均匀/非均匀）情景下的影响，并探究了热性能对K和Cp乘积（K·Cp）的依赖性。[Wu 2023, pp. 6-7]

## Key Findings

1.  **热导率和比热容的温度效应相反**：采热过程中岩石温度降低导致热导率（K）增加，但比热容（Cp）减小。[Wu 2023, pp. 1-1] 在典型条件下（岩石温度从200°C降至50°C），K增加20.5%，Cp减少12.9%。[Wu 2023, pp. 3-5]
2.  **热导率增加提升热性能**：K的增加会加速从岩石基质到裂隙流体的热传导，从而提高生产温度，改善热性能。[Wu 2023, pp. 1-1]
3.  **比热容减小削弱热性能**：Cp的减小会削弱热性能，但其影响小于热导率增加带来的影响。[Wu 2023, pp. 1-1]
4.  **综合效应较小**：由于K和Cp的温度效应方向相反，二者在很大程度上相互抵消。因此，考虑温度依赖性的总体影响相对较小。[Wu 2023, pp. 1-1]
5.  **恒定参数的工程适用性**：假设使用室温（20°C）下测量的恒定K和Cp值，可以提供对EGS热性能可接受的预测。在均匀开度情景下，采用恒定参数仅使生产寿命被高估3.9%；在非均匀开度情景下被高估6.8%。[Wu 2023, pp. 5-6]
6.  **热性能依赖于K与Cp的乘积**：EGS模型的热性能主要取决于岩石热导率和比热容的乘积（K·Cp）。由于采热过程中K和Cp反向变化，其乘积在典型注采温差下仅发生轻微变化。[Wu 2023, pp. 7-8]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| K值随温度降低可增加20.5%，Cp值减少12.9% | [Wu 2023, pp. 3-5] | 岩石温度从200°C降至50°C，采用方程集1 | 温度降低由注水导致 |
| 温度依赖的K增加提升了生产温度，Cp减小则降低生产温度 | [Wu 2023, pp. 5-6] | 通过对比不同K/Cp组合（图5）的模拟结果得出 | 二者效应相反 |
| 采用恒定室温参数仅使生产寿命被高估3.9%（均匀开度）和6.8%（非均匀开度） | [Wu 2023, pp. 5-6] | 以生产温度降至120°C为EGS模型终止条件 | 恒定参数为20°C下的测量值 |
| 热穿透曲线在K·Cp值相近时表现出相似趋势 | [Wu 2023, pp. 6-7] | 通过对恒定K和Cp的不同组合进行模拟（图8） | 确认K·Cp是控制热性能的关键参数 |

## Limitations

-   本研究仅使用了单裂隙EGS模型，未从索引片段中确认其对更复杂的裂隙网络或多井系统的适用性。
-   研究仅考虑了热-水耦合过程，未从索引片段中确认是否包含力学（如裂隙变形）或化学过程的影响。
-   温度依赖的K和Cp关系基于特定几组实验数据拟合的方程，其普适性未从索引片段中确认。
-   研究未考虑压力变化对热导率和比热容的影响，尽管承认温度的影响起主导作用。[Wu 2023, pp. 3-3]
-   研究未讨论模拟结果的实验或现场验证。

## Assumptions / Conditions

-   **模型假设**：假设存在一条位于模型中心的水平主导裂隙，连接注入井和生产井。[Wu 2023, pp. 3-3]
-   **物性假设**：热导率和比热容与温度的关系遵循特定的经验方程（Fu et al., 2019; Berman and Brown, 1985）。[Wu 2023, pp. 3-3]
-   **物理场耦合**：数值模拟仅考虑热-水（TH）耦合过程。[Wu 2023, pp. 3-3]
-   **环境影响**：忽略压力变化对热导率和比热容的影响，仅考虑温度的主导作用。[Wu 2023, pp. 3-3]
-   **岩石类型**：参数设置基于EGS储层中常见的典型花岗岩，其K和Cp在0-300°C范围内分别为1–4 W/m/K和750–1200 J/kg/K。[Wu 2023, pp. 3-3]

## Key Variables / Parameters

-   **关键变量**：
    -   岩石热导率（K） [Wu 2023, pp. 1-1]
    -   岩石比热容（Cp） [Wu 2023, pp. 1-1]
    -   生产温度（用于绘制热穿透曲线） [Wu 2023, pp. 5-6]
    -   生产寿命（以生产温度降至120°C为标准） [Wu 2023, pp. 5-6]
    -   K与Cp的乘积（K·Cp） [Wu 2023, pp. 6-7]
-   **关键参数**：
    -   注入温度（Tinj，测试了30°C, 50°C, 70°C）[Wu 2023, pp. 5-6]
    -   裂隙开度分布（均匀开度0.3mm和非均匀开度） [Wu 2023, pp. 5-6]
    -   室温下（20°C）的岩石热导率（2.85 W/m/K）和比热容（772 J/kg/K）[Wu 2023, pp. 3-5]
    -   岩石密度（2700 kg/m³）、孔隙度（0.01）、渗透率（1×10^-16 m²） [Wu 2023, pp. 3-3]
-   **公式名称**：Fu et al. (2019)的热导率-温度关系方程，Berman and Brown (1985)的比热容-温度关系方程。[Wu 2023, pp. 3-3]

## Reusable Claims

1.  **Claim**: 在增强型地热系统（EGS）的数值模拟中，如果系统运行温差导致的岩石热导率和比热容反向变化幅度相似，其组合效应相互抵消，因此采用室温下测量的恒定热参数进行模拟，可用于工程预测，对生产寿命的高估可能小于10%。
    -   **Conditions**: 适用于单裂隙主导的EGS模型；岩石类型为典型花岗岩类；注采温差在150°C左右（如从200°C降至50°C）。
    -   **Evidence**: 采用恒定室温参数模拟，在均匀和非均匀裂隙开度下，生产寿命仅被高估3.9%和6.8%。[Wu 2023, pp. 5-6]
    -   **Limitations**: 该结论基于特定的一组热导率和比热容-温度经验方程得出的；仅在一个单裂隙模型中得到验证。
2.  **Claim**: EGS长期热采收性能主要受控于岩石热导率（K）与比热容（Cp）的乘积（K·Cp）。
    -   **Conditions**: 在热传导主导的岩石基质中向流体传热的过程中成立。
    -   **Evidence**: 模拟结果显示，当K·Cp值相当时，热穿透曲线表现出相似的趋势。[Wu 2023, pp. 6-7]
    -   **Limitations**: 未从索引片段中确认该关系在多相流、复杂裂隙网络或存在明显对流主导区域的储层中是否依然成立。
3.  **Claim**: 岩石降温会导致其热导率增加，但同时会导致其比热容降低。
    -   **Conditions**: 适用于EGS储层中常见的花岗岩类岩石，温度范围0-300°C。
    -   **Evidence**: 基于Fu et al. (2019)和Berman and Brown (1985)等的实验数据拟合方程。在模拟案例中，从200°C冷却至50°C时，K增加20.5%，Cp减少12.9%。[Wu 2023, pp. 3-5]
    -   **Limitations**: 具体变化幅度取决于岩石类型和选用的经验方程。

## Candidate Concepts
-   [[Enhanced Geothermal System (EGS)]]
-   [[Temperature-Dependent Thermal Conductivity]]
-   [[Temperature-Dependent Specific Heat Capacity]]
-   [[Thermal Breakthrough Curve]]
-   [[Production Life Span]]
-   [[Single-Fracture Model]]
-   [[Thermo-Hydro Coupling]]
-   [[Rock Thermal Parameters]]

## Candidate Methods

-   [[Numerical Simulation]]
-   [[GEOS Simulator (LLNL)]]
-   [[Thermal-Hydraulic Coupled Modeling]]
-   [[Empirical Fitting of Thermal Properties]]

## Connections To Other Work

-   本研究引用了多位学者关于岩石热导率温度依赖性的实验研究，确认了热导率随温度升高而降低的普遍关系 [Wu 2023, pp. 1-3]。
-   引述了Guo et al. (2022) 和Vosteen and Schellschmidt (2003) 等研究，确认了比热容通常随温度升高而增加的结论 [Wu 2023, pp. 1-3]。
-   部分先前研究（如Lee and Deming (1998)）已对多种岩石和矿物的热导率测量数据进行整理，并比较了温度修正方程 [Wu 2023, pp. 1-3]。
-   研究指出，大多数EGS数值模型忽略了采热过程中岩石热参数随温度的变化，本研究旨在弥补这一不足 [Wu 2023, pp. 1-3]，但未列出具体忽略了该过程的模型研究名称。
-   本研究的数值模拟基于GEOS平台（Settgast et al., 2017），其热模拟模块的细节已在Guo et al. (2016)中介绍 [Wu 2023, pp. 3-3]。

## Open Questions

-   未从索引片段中确认：该结论（恒定参数可接受）在更复杂的多裂隙或离散裂隙网络（DFN）模型中的适用性如何？
-   未从索引片段中确认：在更长的时间尺度（超过50年）下，K和Cp的温度效应是否会累积并导致更显著的偏差？
-   未从索引片段中确认：对于不同矿物组成的其他岩石类型（非花岗岩），温度依赖的K和Cp的抵消效应是否同样普遍存在？
-   未从索引片段中确认：当考虑更多物理场耦合，如热-水-力（THM）或热-水-化（THC）耦合时，该结论是否依然成立？

## Source Coverage

本Wiki页面基于论文的8个索引片段生成。这些片段覆盖了**摘要（Abstract）**、**引言（Introduction）**、**方法（Methods）**、**结果（Results）**和**结论（Conclusions）**，提供了较为完整的核心信息链条，包括研究动机、模型设置、关键发现和主要结论。然而，索引片段中缺少**详细的实验数据拟合方法和过程**、**模型验证的具体细节**、**完整的参考文献列表**以及**更深入的讨论部分**，可能导致部分技术细节和局限性描述的缺失。
