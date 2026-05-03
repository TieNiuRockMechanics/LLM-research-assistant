---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2007-l-numerical-simulation-of-percolation-law-of-3d-porous-and-fractured-double-medium"
title: "Numerical Simulation of Percolation Law of 3D Porous and Fractured Double-Medium."
status: "draft"
source_pdf: "data/papers/2007 - Numerical simulation of percolation law of 3D porous and fractured double-medium.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Lü, Zhao-xing, et al. \"Numerical Simulation of Percolation Law of 3D Porous and Fractured Double-Medium.\" *Rock and Soil Mechanics*, vol. 28, Suppl., Oct. 2007, pp. 291-294. DOI:10.16285/j.rsm.2007.s1.003."
indexed_texts: "2"
indexed_chars: "7152"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T12:30:56"
---

# Numerical Simulation of Percolation Law of 3D Porous and Fractured Double-Medium.

## One-line Summary
基于VC++6.0开发三维模拟软件，研究了孔隙与裂隙双重介质的渗流规律，发现裂隙的存在显著改变了渗流行为，且渗流转变与孔隙度、裂隙分形维数等参数有关 [Lü 2007, pp. 1-4]。

## Research Question
在传统的多孔介质渗流理论基础上，如何构建并模拟三维孔隙-裂隙双重介质的渗流模型，并探究其渗流规律及关键影响因素？ [Lü 2007, pp. 1-4]。

## Study Area / Data
摘要提及该模型适用于煤床、岩体等领域 [Lü 2007, pp. 1-4]。索引片段未提供具体的研究区域地理信息或实验数据细节。

## Methods
-   **建模方法**：提出了三维孔隙-裂隙双重介质的渗流研究方法，并建立了相应的渗流模型 [Lü 2007, pp. 1-4]。模型将裂隙视为一条非常重要的渗透通道 [Lü 2007, pp. 1-4]。
-   **模拟工具**：基于VC++6.0平台，开发了用于模拟该双重介质渗流现象的三维软件 [Lü 2007, pp. 1-4]。
-   **理论背景**：研究基于渗流理论，其中提及了用于描述连通团簇的“渗透集团”（percolation cluster）和“渗透阈值”（percolation threshold）等概念，并引用了晶格的渗透阈值（如0.592 75和0.311 6）作为参考 [Lü 2007, pp. 1-4]。

## Key Findings
1.  **裂隙增加渗透概率**：在模型中引入裂隙，能显著增加介质的渗透概率值 [Lü 2007, pp. 1-4]。
2.  **渗流规律改变**：裂隙的加入，使得双重介质的渗流规律有别于单一多孔介质 [Lü 2007, pp. 1-4]。
3.  **渗流转变条件**：随着孔隙度、裂隙分形维数和裂隙数量分布初始值的增加，一定会发生渗流转变这一自然现象 [Lü 2007, pp. 1-4]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 模型中的裂隙显著增加渗透概率值。 | [Lü 2007, pp. 1-4] | 基于建立的三维孔隙-裂隙双重介质模型和开发的模拟软件。 | 从论文摘要中提炼出的核心结论。 |
| 裂隙使双重介质与单一多孔介质的渗流规律不同。 | [Lü 2007, pp. 1-4] | 基于孔隙-裂隙双重介质模型与多孔介质模型的模拟结果对比。 | 从论文摘要中提炼出的核心结论。 |
| 随着孔隙度、裂隙分形维数和裂隙数量分布初始值的增加，必然会发生渗流转变现象。 | [Lü 2007, pp. 1-4] | 基于所建模型的模拟研究。 | 明确了控制渗流转变的三个关键参数。 |

## Limitations
索引片段仅包含摘要和第4页的参考文献列表，缺乏对模型构造细节、控制方程、边界条件、参数取值、模拟步骤和详细结果分析的描述。因此，无法评估模型的适用性、模拟的精度和结论的可靠性。

## Assumptions / Conditions
-   研究基于“3D porous medium model” [Lü 2007, pp. 1-4]。
-   关键的模拟条件是将裂隙视为“a very important permeability channel”纳入理论研究中 [Lü 2007, pp. 1-4]。
-   模型成立的假设、具体的物理过程假设（如稳态/非稳态、达西/非达西流）、裂隙的几何与拓扑结构假设等，均未从索引片段中确认。

## Key Variables / Parameters
根据摘要，影响渗流规律和渗流转变的关键变量/参数包括：
-   **孔隙度** [Lü 2007, pp. 1-4]
-   **裂隙分形维数（fracture fractal dimension）** [Lü 2007, pp. 1-4]
-   **裂隙数量分布初始值（fracture number distribution initial value）** [Lü 2007, pp. 1-4]
-   其他涉及的理论概念：
    -   **渗透概率（percolation probability）** [Lü 2007, pp. 1-4]
    -   **渗流阈值（percolation threshold）** [Lü 2007, pp. 1-4]

## Reusable Claims
-   Claim 1: 在三维孔隙介质模型中引入裂隙作为渗透通道，会使得系统的渗流规律与不含裂隙的纯多孔介质相比发生质的改变，其直接表现是渗透概率值的显著增加 [Lü 2007, pp. 1-4]。适用条件：此结论适用于基于渗流理论构建的二维或三维孔隙-裂隙双重介质模型；证据来自该研究的数值模拟；限制是未从片段中获知裂隙是如何具体表征和参数化的。
-   Claim 2: 对于三维孔隙-裂隙双重介质模型，渗流转变现象的发生由孔隙度、裂隙分形维数和裂隙数量分布初始值这几个关键参数的共同增加所触发 [Lü 2007, pp. 1-4]。适用条件：适用于离散介质渗流模型；证据来自该研究的模拟发现；限制在于未阐明各参数的独立影响及其交互作用。

## Candidate Concepts
- [[Percolation Theory]]
- [[Porous Medium]]
- [[Fractured Medium]]
- [[Double-Medium Model]]
- [[Fractal Dimension]]
- [[Percolation Threshold]]
- [[Numerical Simulation]]

## Candidate Methods
- [[3D Porous and Fractured Double-Medium Percolation Model]]
- [[VC++ based Seepage Simulation Software Development]]

## Connections To Other Work
-   索引片段提及多篇参考文献，反映了可连接的研究方向，但未阐述具体关系：
    -   **渗流理论基础**：引用关于二维格子渗流模型和渗透阈值的基础研究 (如 [Vidales 2000]、[Michafl 2002])，表明本研究的3D模型建立在2D渗流理论基础之上 [Lü 2007, pp. 4]。
    -   **裂隙表征**：引用关于煤体裂隙尺度分布 (如 KANG Tian-he 1995 [11]) 和岩体裂隙三维分形分布规律 (如 FENG Zeng-chao 2005 [12]) 的研究，表明本研究的裂隙建模方法可能与[[Fracture Fractal Characterization]]有关 [Lü 2007, pp. 4]。
    -   **方法论借鉴**：引用多孔介质随机模拟模型 (如 ZHANG Dong-hui 2003) 的研究，表明本研究在建模和模拟方法上可能有继承和发展 [Lü 2007, pp. 4]。

## Open Questions
-   裂隙在数值模型中是如何具体实现和几何参数化的？其物理属性（如开度、渗透率）是如何赋值的？
-   孔隙与裂隙之间的双重介质耦合机制是什么？是离散裂隙模型还是等效连续介质模型？
-   渗透阈值与孔隙度、裂隙分形维数、裂隙数量分布初始值之间是否存在定量关系式？
-   模拟结果是否通过物理实验或现场观测数据进行了验证？

## Source Coverage
本页面内容完全基于提供的2个索引片段 [Zhao 2007, pp. 1-4] 和 [Zhao 2007, pp. 4-4]。其中，片段1包含了论文的摘要和引言开头，是信息的主要来源。片段2仅为参考文献列表。由于缺少论文正文的方法、结果和讨论部分，导致对模型细节、模拟过程、数据分析和局限性等关键信息的覆盖严重不足。
