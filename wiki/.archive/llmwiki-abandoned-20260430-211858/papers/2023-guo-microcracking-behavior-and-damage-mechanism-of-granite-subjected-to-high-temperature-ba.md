---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-guo-microcracking-behavior-and-damage-mechanism-of-granite-subjected-to-high-temperature-ba"
title: "Microcracking Behavior and Damage Mechanism of Granite Subjected to High Temperature Based on CT-GBM Numerical Simulation."
status: "draft"
source_pdf: "data/papers/2023 - Microcracking behavior and damage mechanism of granite subjected to high temperature based on CT-GBM numerical simulation.pdf"
collections:
  - "zotero new"
citation: "Guo, Pingye, et al. “Microcracking Behavior and Damage Mechanism of Granite Subjected to High Temperature Based on CT-GBM Numerical Simulation.” *Computers and Geotechnics*, vol. 159, 2023, article 105385. doi:10.1016/j.compgeo.2023.105385. Accessed 2026."
indexed_texts: "16"
indexed_chars: "76740"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T12:59:10"
---

# Microcracking Behavior and Damage Mechanism of Granite Subjected to High Temperature Based on CT-GBM Numerical Simulation.

## One-line Summary
Guo 等建立了一种基于 CT 与颗粒流模型的数值方法，用以研究高温下花岗岩真实矿物晶体结构的微裂纹行为与热损伤机制 [Guo 2023, pp. 1-2].

## Research Question
此研究旨在利用数值模拟方法，研究高温对花岗岩微裂纹行为的影响，并探讨其热损伤机制，为地热能开采和深部工程灾害防治提供参考 [Guo 2023, pp. 1-3].

## Study Area / Data
- **数据来源**：花岗岩样品取自福建省漳州盆地，取自同一完整岩块，无明显裂纹 [Guo 2023, pp. 3-4].
- **样本尺寸**：圆柱形样品，直径 10.0 mm，高 20.0 mm [Guo 2023, pp. 3-4].
- **矿物组成**：样品主要包含长石、石英、云母三种矿物 [Guo 2023, pp. 3-4].
- **数据获取**：通过 CT 扫描获得样品内部矿物结构图像，利用 16 位灰度图像阈值分割法识别不同矿物，并重建数字图像 [Guo 2023, pp. 3-4].

## Methods
- **建模方法**：建立了一种热力耦合数值模型 (CT-GBM)，该模型结合了计算断层扫描 (CT) 技术和颗粒流模型 (GBM)，基于离散元方法 (DEM) 和颗粒流代码 (PFC) [Guo 2023, pp. 1-3].
- **模型特点**：
    - 考虑了非均质性，包括矿物晶体和晶体边界的力学性质、矿物分布以及热传导的非均质性 [Guo 2023, pp. 2-3].
    - 根据 CT 图像提取了真实的矿物晶体边界，模型中包含了三种矿物和六种边界类型 [Guo 2023, pp. 2-3].
- **模型设置**：
    - 使用线性平行粘结模型 (Linear Parallel Bond, Pb) 模拟矿物颗粒内部接触 [Guo 2023, pp. 6-7].
    - 使用光滑节理模型 (Smooth-joint, Sj) 模拟颗粒边界接触,包括同种矿物和不同矿物间的边界 [Guo 2023, pp. 6-7].
- **参数标定**：通过试错法标定微观力学参数，并通过对比室温和高温下的实验与数值模拟得到的应力-应变曲线、破坏模式进行验证 [Guo 2023, pp. 7-7].
- **热参数**：考虑了不同矿物的热传导系数非均质性，参考了 Horai (1971) 和 Guo et al. (2020) 的数据。各矿物线性热膨胀系数分别为：长石 8.7x10⁻⁶ °C⁻¹，石英 24.3x10⁻⁶ °C⁻¹，云母 3.0x10⁻⁶ °C⁻¹ [Guo 2023, pp. 7-7].
- **加热与加载过程**：模型采用与实验室测试相同的加热方式，即用周围的墙作为热源进行加热 [Guo 2023, pp. 7-9].

## Key Findings
- **热损伤机制**：花岗岩的热损伤主要以拉伸破坏的形式发展 [Guo 2023, pp. 1-2].
- **裂纹发展分期**：
    - **穿晶裂纹**：其发展大致可分为三个阶段：平静期（室温~300°C）、稳定发展期（300°C~450°C）和不稳定发展期（450°C~600°C） [Guo 2023, pp. 1-2].
    - **晶界裂纹**：首先在长石-石英晶界处出现，但在高温（332°C 以上）时，由于长石占比较大，长石-长石晶界裂纹占主导地位 [Guo 2023, pp. 1-2].
- **应力集中现象**：随着温度升高，应力集中现象愈发明显，且在晶界处比在矿物颗粒内部更为显著，这是微裂纹萌生和晶界裂纹占主导的原因 [Guo 2023, pp. 1-2].
- **力学性质劣化**：
    - 从 450°C 到 600°C，峰值应力和弹性模量急剧下降，这不仅归因于热致微裂纹的增加，还与石英在 573°C 的 α-β 相变和云母氧化等化学变化有关 [Guo 2023, pp. 7-9].
    - 与室温相比，经不同温度处理后，实验样品的峰值应力分别下降了 6%, 8%, 9% 和 49%；弹性模量分别下降了 8%, 10%, 13% 和 51% [Guo 2023, pp. 7-9].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 热损伤主要以拉伸破坏形式发展 | [Guo 2023, pp. 1-2] | 基于 CT-GBM 数值模拟结果 | |
| 穿晶裂纹发展分为室温~300°C (平静期), 300°C~450°C (稳定发展期), 450°C~600°C (不稳定发展期)三个阶段 | [Guo 2023, pp. 1-2] | 基于 CT-GBM 数值模拟结果 | |
| 晶界裂纹首先出现在长石-石英边界，但高温（>332°C）时以长石-长石边界为主 | [Guo 2023, pp. 1-2] | 基于 CT-GBM 数值模拟结果 | 原因是长石在花岗岩中比例大 |
| 应力集中现象随温度升高而加剧，晶界处比颗粒内部更明显 | [Guo 2023, pp. 1-2] | 基于 CT-GBM 数值模拟结果 | 这是导致微裂纹萌生和晶界裂纹主导的原因 |
| 450°C~600°C 力学性质（峰值应力、弹性模量）急剧下降 | [Guo 2023, pp. 7-9] | 实验结果与数值模拟对比 | 原因还涉及石英在 573°C 的相变和云母氧化等化学变化 |
| 经不同温度处理后，实验峰值应力分别下降 6%, 8%, 9%, 49% | [Guo 2023, pp. 7-9] | 实验数据，与室温峰值应力对比 | |
| 经不同温度处理后，实验弹性模量分别下降 8%, 10%, 13%, 51% | [Guo 2023, pp. 7-9] | 实验数据，与室温弹性模量对比 | |

## Limitations
- **模型局限性**：
    - 使用试错法标定的微观参数可能不唯一，这是颗粒流代码 (PFC) 建模中的一个主要问题 [Guo 2023, pp. 7-7].
    - 数值模拟未反映实验曲线中由于微裂纹闭合导致的初始非线性压密阶段 [Guo 2023, pp. 7-9].
- **研究范围限制**：未从索引片段中确认。
- **数据与参数限制**：未从索引片段中确认。

## Assumptions / Conditions
- **模型假设**：
    - 模型简化为二维模型，在 XZ 和 YZ 方向建立，尺寸一致（高 20 mm, 宽 10 mm） [Guo 2023, pp. 6-7].
    - 设定仅粘结的力矢量法向分量受温度变化影响 [Guo 2023, pp. 4-6].
    - 假设粘结的热膨胀系数等于其关联的两个颗粒热膨胀系数的平均值 [Guo 2023, pp. 4-6].
- **实验/数据条件**：
    - 为保证样品均质性和代表性，样品尺寸需满足矿物颗粒尺寸小于样品直径的三十分之一 [Guo 2023, pp. 3-4].
    - 数值模型中的矿物含量与 CT 切片获得的真实矿物含量进行了对比验证，绝对误差显示一致性良好（例如，XZ 方向上，长石误差为 ±0.58%） [Guo 2023, pp. 6-7].
- **模拟条件**：分析的温度范围为室温至 600°C [Guo 2023, pp. 1-2].

## Key Variables / Parameters
- **几何参数**：最小颗粒半径 (R)，最大与最小颗粒半径之比 (r) [Guo 2023, pp. 6-7].
- **力学参数**：粘结强度、刚度（如粘结法向刚度 K_n）、摩擦系数 [Guo 2023, pp. 7-7].
- **热物理参数**：
    - 热传导系数 (k)，模型考虑了不同矿物的非均质性 [Guo 2023, pp. 7-7].
    - 热膨胀系数 (α)：长石 (8.7×10⁻⁶ °C⁻¹)，石英 (24.3×10⁻⁶ °C⁻¹)，云母 (3.0×10⁻⁶ °C⁻¹) [Guo 2023, pp. 7-7].
    - 比热：1015 J/kg·°C [Guo 2023, pp. 7-7].
    - 热阻系数 (η) [Guo 2023, pp. 4-6].
- **材料状态变量**：峰值应力、弹性模量 [Guo 2023, pp. 7-9].
- **裂纹表征变量**：穿晶裂纹数量、晶界裂纹数量 [Guo 2023, pp. 1-2].

## Reusable Claims
1.  **Claim**: 在热-力耦合条件下，基于晶界模型 (GBM) 的数值模拟中，晶界处的应力集中现象比矿物颗粒内部更为显著，这是导致晶界微裂纹萌生和发展的主要原因 [Guo 2023, pp. 1-2].
    - **Conditions**: 适用于考虑矿物非均质性的晶体岩石热力耦合数值模拟。

2.  **Claim**: 高温下（450°C 至 600°C）花岗岩力学性质（峰值应力、弹性模量）的急剧劣化，除了热致裂纹的增加，还需考虑石英在 573°C 的 α-β 相变以及云母氧化等化学变化的影响 [Guo 2023, pp. 7-9].
    - **Conditions**: 适用于含石英和云母等矿物的花岗岩；温度高达 600°C。

3.  **Claim**: 在基于 CT-GBM 的花岗岩模型中，矿物颗粒内部裂纹的发展可划分为三个阶段：平静期（室温~300°C）、稳定发展期（300°C~450°C）和不稳定发展期（450°C~600°C） [Guo 2023, pp. 1-2].
    - **Conditions**: 基于本文特定的模型设置和矿物组成，加热条件为从室温升至 600°C。

4.  **Claim**: 在花岗岩 CT-GBM 模型中，晶界接触采用光滑节理模型 (Sj)，颗粒内部接触采用线性平行粘结模型 (Pb) [Guo 2023, pp. 6-7].
    - **Conditions**: 一种基于离散元方法，区分颗粒内部和颗粒边界力学行为的建模策略。

## Candidate Concepts
- [[Fracture reservoir]]
- [[Deep Engineering]]
- [[thermal damage]]
- [[granite]]
- [[high temperature]]
- [[microcracking]]
- [[Grain-based model (GBM)]]
- [[Computed tomography (CT)]]
- [[Thermo-mechanical Coupled Model]]
- [[Intra grain crack]]
- [[Grain boundary crack]]
- [[Stress Concentration]]
- [[α-β phase transition of quartz]]

## Candidate Methods
- [[CT-GBM Numerical Simulation]]
- [[Particle Flow Code (PFC)]]
- [[Discrete Element Method (DEM)]]
- [[Linear Parallel Bond (Pb) Model]]
- [[Smooth-joint (Sj) Model]]
- [[Gray Image Threshold Segmentation]]

## Connections To Other Work
- **主题连接**：该研究在方法论上属于利用 [[Discrete Element Method (DEM)]] 和 [[Grain-based model (GBM)]] 研究岩石热力耦合行为的范畴，可连接到该领域的其他数值模拟研究（如 Tian et al. 2020; Yin et al. 2022），这些研究被本文提及作为 GBM 能模拟岩石热致开裂过程的例证 [Guo 2023, pp. 2-2]。
- **方法改进连接**：该方法是对以往将岩石热导率设置为均一参数（如 Wanne and Young. 2008; Zhao. 2016; Wu et al. 2020）的做法的一种改进，通过考虑矿物热传导特性的非均质性来提升模型可靠性 [Guo 2023, pp. 7-7]。
- **应用领域连接**：研究成果旨在为[[geothermal energy]]提取和深部工程灾害防治的高温岩土工程问题提供参考 [Guo 2023, pp. 1-3]。

## Open Questions
- 该方法在三维模型中的应用表现如何，是否会产生不同的裂纹发展模式？ [未从索引片段中确认]
- 模型是否考虑了流体或孔隙压力对热致裂纹的影响？[未从索引片段中确认]
- 除峰值应力和弹性模量外，高温对花岗岩的泊松比、断裂韧性等其他力学参数有何影响？[未从索引片段中确认]

## Source Coverage
本知识页基于论文的 16 个索引片段生成。这些片段覆盖了论文的摘要、引言、实验方法、建模细节、参数标定、结果与讨论等多个部分，能够支持对研究目的、方法、主要结论和部分证据的描述。然而，片段可能未完整覆盖引言部分的全部文献综述、模型验证的具体细节（如对高温处理后力学行为的完整比较）、讨论部分的所有机制分析，以及结论部分。关于数值模拟与实验数据在 300°C 和 450°C 等中间温度点的详细对比信息，在片段中相对简略。
