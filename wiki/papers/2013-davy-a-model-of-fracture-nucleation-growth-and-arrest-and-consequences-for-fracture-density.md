---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2013-davy-a-model-of-fracture-nucleation-growth-and-arrest-and-consequences-for-fracture-density"
title: "A Model of Fracture Nucleation, Growth and Arrest, and Consequences for Fracture Density and Scaling."
status: "draft"
source_pdf: "data/papers/2013 - A model of fracture nucleation, growth and arrest, and consequences for fracture density and scaling.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Davy, Philippe, et al. \"A Model of Fracture Nucleation, Growth and Arrest, and Consequences for Fracture Density and Scaling.\" *Journal of Geophysical Research: Solid Earth*, vol. 118, 2013, pp. 1393-1407. doi:10.1002/jgrb.50120."
indexed_texts: "19"
indexed_chars: "94729"
nonempty_source_blocks: "19"
compiled_source_blocks: "19"
compiled_source_chars: "95101"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.003927"
coverage_status: "full-index"
source_signature: "9d85255b69a648fc71d891869e25cfa8ca0ab8d7"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T14:58:30"
---

# A Model of Fracture Nucleation, Growth and Arrest, and Consequences for Fracture Density and Scaling.

## One-line Summary
提出一种基于裂缝成核、生长与停止（arrest）简化力学规则的新型离散裂缝网络（[[DFN]]）模型，核心假设是大裂缝阻止小裂缝生长，从而自然产生与实际观察一致的多尺度自相似裂缝尺寸分布。

## Research Question
如何构建一个既能反映裂缝间空间相互作用，又能在多个数量级上再现裂缝长度-密度标度关系的随机DFN模型？[Davy 2013, pp. 1-1]

## Study Area / Data
模型验证与讨论中引用了以下地区的裂缝网络数据 [Davy 2013, pp. 12-13]:
- **挪威** Hornelen 盆地 [[joint system]]
- **瑞典** Forsmark、Simpevarp、Laxemar 场地 [[joint system]]
- **圣安德烈亚斯断层系统** [[San Andreas fault system]]

## Methods
模型构建基于以下理论框架与数值实现 [Davy 2013, pp. 2-3][Davy 2013, pp. 6-7]:
- **三维离散裂缝网络（[[3D DFN]]）生成**：在 H2OLAB 软件平台中实现，裂缝简化为圆盘，嵌入三维多面体域。
- **裂缝成核**（Nucleation）：假设核均匀分布（位置与产状），可选用指数或幂律长度分布；考虑“所有核初始即存在”及“恒定成核率”两种端元情况。[Davy 2013, pp. 3-4]
- **裂缝生长律**（Growth Law）：采用幂律形式 \( v(l) = dl/dt = C l^a \)，其中 \( a \) 为生长指数，\( C \) 为与远程应力相关的常数。[Davy 2013, pp. 4-4]
- **裂缝停止规则**（Arrest Rule）：基于UFM（通用裂缝标度模型）规则，即裂缝扩展至与更大裂缝相交时停止。[Davy 2013, pp. 5-6]
  - **模式A**：裂缝首次与较大裂缝相交即停止（仅半径自由度）。
  - **模式B**：裂缝可与一较大裂缝相切继续生长，直至与第二个较大裂缝相交（半径与中心移动两个自由度）。
- **分布统计**：通过裂缝长度密度分布 \( n(l, L) \) 描述网络特征，分析其在不同时间步的演化。[Davy 2013, pp. 1-2]

## Key Findings
1.  **产生双区（two-regime）长度分布** [Davy 2013, pp. 5-6][Davy 2013, pp. 7-8]:
    - **稀释区**（Dilute regime, 小尺度）：裂缝自由生长，长度分布 \( n(l) \propto l^{-a} \)，标度指数由生长律指数控制。
    - **密区/UFM区**（Dense/UFM regime, 大尺度）：裂缝被较大裂缝停止，呈自相似分布 \( n(l) \propto l^{-(D+1)} \)，其中 \( D \) 为裂缝中心网络的拓扑维数，标度指数准恒定（三维中 \( D=2 \)，指数为 -3）。
2.  **临界过渡尺度** \( l_c \) 存在，将稀释区与密区分开，并随系统演化向小尺度扩展 [Davy 2013, pp. 6-7][Davy 2013, pp. 9-10]。
3.  **UFM区的密度项** \( d_{UFM} (= D g^D) \) 不是常量，其值依赖于裂缝停止模式（模式B的密度项约为模式A的1.5倍）及裂缝产状分布。[Davy 2013, pp. 10-12]
    - 对于单组近乎平行的裂缝，\( d_{UFM} \propto 1/\sin(\theta) \)，其中 \( \theta \) 为产状的标准差。
    - 数值范围：根据产状各向异性和停止模式，\( d_{UFM} \) 从 2.0 变化至 32。[Davy 2013, pp. 11-12]
4.  **网络演化特征**：在无量纲时间 \( t' \approx 0.5 \)（最小核生长至系统最大尺度所需时间），系统基本达到准稳态，此后密度增长极为缓慢。[Davy 2013, pp. 12-12]
5.  **几何特征**：生成的DFN天然形成大量“T”型裂缝交切（T-intersections），与野外观察一致，区别于经典泊松随机模型的大量“X”型交切。[Davy 2013, pp. 8-9]

## Core Evidence Table
| 证据 | 来源 | 条件 / 假设 | 备注 |
| :--- | :--- | :--- | :--- |
| 裂缝长度分布 \( n(l) \) 在稀释区遵循幂律，标度指数 \( a \) 等于生长律指数 \( a \)。 | [Davy 2013, pp. 4-4] | 恒定的成核率 \( \dot{n}_N \) 和非零、与时间无关的生长速度 \( v(l) \)。 | 适用于裂缝不相互作用的自由生长阶段。 |
| UFM密区的长度分布为 \( n(l) = D g^D l^{-D-1} \)。 | [Davy 2013, pp. 6-6] | 裂缝停止规则为大裂缝阻止小裂缝，裂缝长度 l 正比于到最近较大裂缝的距离 d（l = gd）。 | 标度指数 \( D+1 \) 是准通用的；在三维中 D=2，指数为3。 |
| 模拟DFN的过渡尺度 \( l_c \) 随时间减小。 | [Davy 2013, pp. 8-8, p. 10-10] | 恒定型核率或所有核初始存在的端元情况。 | UFM区随系统演化逐渐“吞并”稀释区。 |
| 当裂缝产状为单组且标准差为 θ 时，UFM区密度项 \( d_{UFM} \approx 2/\sin\theta \) (模式 A)。 | [Davy 2013, pp. 12-12] | 模式A停止规则。 | 该式表达了裂缝相交长度与中心间距的几何校正关系。 |
| 瑞典Forsmark和Simpevarp场地节理网络的等效三维UFM密度项估计在 3 至 5.5 之间。 | [Davy 2013, pp. 13-13] | 通过立体学规则从二维露头密度项换算。 | 该值与模拟结果在产状变异性大于20°–30°时获得的密度项范围一致。 |

## Limitations
- **模型停止标准缺失**：目前没有明确的力学标准来终止裂缝生成过程，网络将持续增长直至无空间容纳最小核（\( l_N \)）。需引入能量考虑来确定自然终止点。[Davy 2013, pp. 12-12]
- **成核简化**：假设成核在空间上均匀分布，未考虑已有裂缝尖端附近的应力集中对局部成核的促进作用。[Davy 2013, pp. 12-12]
- **生长律简化**：模型使用单一幂律生长律，未显式计算局部应力场对应力强度因子K的影响，从而忽略了产状与局部应力对生长速率的控制。[Davy 2013, pp. 12-12]
- **裂缝形状假设**：假设裂缝为圆盘，这忽略了裂缝在受阻挡时可能发生的各向异性生长，并简化了裂缝交切的尺寸（假设为点接触）。[Davy 2013, pp. 12-12]
- **应用局限性**：本文为方法论第一步，未涉及后续水力或力学应用所需的关键信息，如裂缝开度（aperture）或强度参数的讨论。[Davy 2013, pp. 2-2]

## Assumptions / Conditions
- **裂缝简化形状**：所有裂缝均假设为平面圆盘。[Davy 2013, pp. 6-6]
- **核均匀分布**：在完整岩石中，裂缝核的位置和产状均匀分布。[Davy 2013, pp. 3-3, p. 7-7]
- **成核/生长定律**：成核率恒定，或所有核在初始时刻一次给定；生长律采用幂律形式 \( v = C l^a \)。[Davy 2013, pp. 4-4, p. 5-5]
- **核心机械规则**：大裂缝阻止小裂缝生长（小裂缝不能穿过大裂缝）。[Davy 2013, pp. 1-2]
- **裂缝停止模式**：考虑两种端元模式A（首交点停止）和模式B（切向生长至第二交点停止）。[Davy 2013, pp. 5-6]
- **几何齐次性**：假设研究的裂缝系统具有分形或欧几里得拓扑维数 D。[Davy 2013, pp. 5-6]

## Key Variables / Parameters
- \( n(l, L) \)：裂缝长度密度分布，定义为单位体积（尺寸为L）内长度在 [l, l+dl] 范围内的裂缝数量。[Davy 2013, pp. 1-2]
- \( a \)：幂律长度标度指数（稀释区）以及生长律指数。[Davy 2013, pp. 2-2, p. 4-4]
- \( D \)：裂缝中心网络的质量（拓扑）维数。[Davy 2013, pp. 1-2]
- \( \dot{n}_N \)：成核率。[Davy 2013, pp. 4-4]
- \( l_N \)：核的特征长度尺度。[Davy 2013, pp. 3-3]
- \( l_c \)：稀释区与UFM密区之间的临界过渡长度尺度。[Davy 2013, pp. 6-6]
- \( d_{UFM} = D g^D \)：UFM区长度分布的密度项，无量纲。[Davy 2013, pp. 8-8]
- \( g \)：裂缝停止长度与裂缝间距之比。[Davy 2013, pp. 5-6]
- \( \theta \)：表征裂缝产状变异性的角度（如一组节理倾角/走向的标准差）。[Davy 2013, pp. 10-10]

## Reusable Claims
- **Claim 1**: 在裂缝网络演化模型中，基于“大裂缝阻止小裂缝”这一简化力学规则，可以自然产生一个具有准通用标度指数（三维中为 -3）的自相似密集区（UFM regime）。其成立条件是大裂缝在力学上对小裂缝生长起主导性阻挡作用。[Davy 2013, pp. 1-2, p. 5-6, p. 13-13]
- **Claim 2**: 裂缝长度分布 \( n(l) \) 的稀释区（小尺度）标度指数直接受控于裂缝生长律的指数，即 \( n(l) \propto l^{-a} \)，其中 \( a \) 为生长速率 \( v \) 与长度 \( l \) 幂律关系 \( v \propto l^a \) 中的指数。该结论基于恒定成核率和无裂缝相互作用的自由生长假设。[Davy 2013, pp. 4-4, p. 7-7]
- **Claim 3**: UFM 密集区长度分布的密度项 \( d_{UFM} \) 不是唯一的，其数值主要取决于两个因素：裂缝停止模式（模式A或B）和裂缝产状分布的各向异性。对于单组亚平行裂缝，\( d_{UFM} \) 反比于产状标准差的正弦值。当产状各向异性极强时，\( d_{UFM} \) 可达32，而均匀分布时约为2-3。[Davy 2013, pp. 10-12]
- **Claim 4**: 将UFM规则与裂缝生长律结合产生的DFN模型，可定量再现天然裂缝系统（如瑞典Forsmark场地）中观察到的裂缝密度分布。这表明，简单的力学交互作用规则可能是产生地壳中复杂多尺度裂缝网络的关键机制之一。[Davy 2013, pp. 13-13]

## Candidate Concepts
- [[Discrete Fracture Network (DFN)]]
- [[fracture nucleation, growth, and arrest]]
- [[universal model of fracture scaling (UFM)]]
- [[power-law length distribution]]
- [[fracture density term]]
- [[dense vs. dilute fracture regime]]
- [[T-intersections in fracture networks]]
- [[subcritical fracture growth]]
- [[fracture interaction rule]]
- [[fracture reservoir]]
- [[stereological analysis]]

## Candidate Methods
- [[3D time-wise DFN generation method]]
- [[H2OLAB platform for DFN simulation]]
- [[mode A and mode B fracture arrest rules]]
- [[calculation of fracture density distribution n(l)]]
- [[power-law fracture growth model]]
- [[critical transition scale analysis between dilute and dense regimes]]
- [[numerical analysis of dfm density term vs. orientation distribution]]

## Connections To Other Work
- **与UFM模型的关系**：本文模型的核心停止规则直接继承和发展自 Davy 等人 (2010) 提出的“可能的通用裂缝标度模型”（即UFM框架）。[Davy 2013, pp. 1-2, p. 6-6]
- **与经典DFN模型的对比**：本文明确指出，传统的随机DFN模型（如泊松过程模型）未能反映裂缝网络的空间复杂性和多尺度相关性，而本文的模型旨在超越此类模型。[Davy 2013, pp. 1-1, p. 12-12]
- **与裂缝力学模拟的关系**：本文方法是对完全机械耦合的裂缝生长数值模拟（如 Cowie et al., 1993; Renshaw & Pollard, 1994 等）的大幅简化，旨在克服后者在计算效率和网络规模上的局限性，以模拟包含数百万条裂缝的三维网络。[Davy 2013, pp. 2-3, p. 12-12]
- **对网络属性的影响**：生成的DFN由于具有特定的空间相关性，其连通性和流动特性与具有相同长度分布的传统随机模型“显著不同”。这是开发此类基于过程模型的动机之一。[Davy 2013, pp. 1-2]
- **与野外数据的一致性**：模型的输出结果（UFM区的标度指数和密度项，以及“T”型交切）与来自挪威、瑞典和美国圣安德烈亚斯断层系统的多个野外数据集定量一致。[Davy 2013, pp. 13-13]

## Open Questions
- 地质裂缝系统中，决定破裂过程最终停止的能量或力学标准是什么？如何在简化DFN模型中引入这一标准？[Davy 2013, pp. 12-12]
- 局部应力场（特别是已有裂缝尖端附近的应力集中）如何影响成核和生长速率？将这一反馈机制纳入模型会如何改变最终网络的结构和密度分布？[Davy 2013, pp. 12-12]
- 如何超越圆盘假设，发展能模拟裂缝各向异性生长、非点式交切及其对UFM密度项 \( d_{UFM} \) 影响的模型？[Davy 2013, pp. 12-13]
- 如何通过进一步的三维立体学分析，将模型预测的 \( d_{UFM} \) 与更多场地的三维裂缝密度数据进行系统对比？[Davy 2013, pp. 13-13]
- 模型产生的“T”型交切为主的拓扑结构和自相似密度分布，对岩体水力传导及力学性质的具体量化影响是什么？[Davy 2013, pp. 13-13]

## Source Coverage
本文基于提供的所有 19 个索引文本片段进行编译整理。所有非空源代码块均已纳入分析，覆盖率为 100%（按代码块和字符数计）。索引字符总数为 94729，编译后的源字符总数为 95101。
