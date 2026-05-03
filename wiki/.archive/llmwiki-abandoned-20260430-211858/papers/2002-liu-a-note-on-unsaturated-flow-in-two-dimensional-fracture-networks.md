---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2002-liu-a-note-on-unsaturated-flow-in-two-dimensional-fracture-networks"
title: "A Note on Unsaturated Flow in Two-Dimensional Fracture Networks."
status: "draft"
source_pdf: "data/papers/2002 - A note on unsaturated flow in two-dimensional fracture networks.pdf"
collections:
citation: "Liu, H. H., et al. \"A Note on Unsaturated Flow in Two-Dimensional Fracture Networks.\" *Water Resources Research*, vol. 38, no. 9, 2002, p. 1176. doi:10.1029/2001WR000977. Accessed 2026."
indexed_texts: "9"
indexed_chars: "44543"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T11:34:03"
---

# A Note on Unsaturated Flow in Two-Dimensional Fracture Networks.

## One-line Summary
通过二维离散裂隙网络数值模拟，研究了非饱和稳态流行为，指出重力驱动的垂向流径主导流动，短小裂隙虽不贡献全局流量但增强裂隙‑基质相互作用，并提出层状介质中流径平均间距随深度增加的假设，同时引入毛细屏障“影响区”概念以评价地下洞室渗流 [Liu 2002, pp. 1-1, 8-8]。

## Research Question
非饱和条件下二维裂隙网络中稳态流的流径特征、连通性控制因素及对基质相互作用和渗流的影响尚未被充分认识。本研究旨在通过包含数千条裂隙的大规模数值模拟，揭示非饱和裂隙网络的流动行为与机理 [Liu 2002, pp. 1-1, 1-2]。

## Study Area / Data
模拟域为 10 m × 10 m 的二维竖直剖面，裂隙基于 Nevada 州 Yucca Mountain 非饱和带 Topopah Spring 焊接凝灰岩（TSw）单元统计特性生成。裂隙分为 5 组，其迹长、平均孔径、渗透率及 van Genuchten 参数 α 和 m 列于 Table 1。孔隙度与裂隙密度用于校准孔径‑迹长关系 b = cLᵈ，其中 c = 1.008 × 10⁻⁴，d = 0.317 [Liu 2002, pp. 2-3, 3-4]。未从索引片段中确认具体的边界供水流量及其他场地数据。

## Methods
采用 TOUGH2 多相流代码进行稳态非饱和流模拟，网格单元约 16,000 个。单裂隙水力特性使用 van Genuchten 模型描述，参数 m = 0.633，饱水饱和度 Ss = 1，残余饱和度 Sr = 0.01，α 与迹长相关。裂隙网络生成方法类似 Kwicklis and Healy [1993]。对相同统计特征的两个随机实现进行模拟，结果相似，仅展示其中一个 [Liu 2002, pp. 3-4, 4-5]。

## Key Findings
- 流径主要由连通的大迹长裂隙控制，在重力主导作用下呈垂向展布；亚水平裂隙提供垂向流径间的横向沟通，导致流径的水平扩散 [Liu 2002, pp. 1-1, 4-5]。
- 大量小迹长裂隙不参与全局流动，但与主要流径相连的部分仍增强网络连通性，并可能显著影响裂隙‑基质相互作用，对基质扩散等机制尤为重要 [Liu 2002, pp. 1-1, 6-7, 8-8]。
- 在层状非饱和裂隙系统中，平均流径间距具有深度依赖性：随深度增加而增大，只要流动由重力驱动。这一假设可能适用于 Yucca Mountain 的焊接单元，但需要进一步证实 [Liu 2002, pp. 1-1, 8-8]。
- 引入“毛细屏障影响区”概念来描述裂隙网络向地下洞室的渗流。当洞室上方裂隙内水积累的高度超过该裂隙的空气进入值（≈1/α）时发生渗漏；若裂隙在达到该高度前与侧向流动通路相连，渗漏可能被抑制，导致二维网络中毛细屏障效应与均质多孔介质显著不同 [Liu 2002, pp. 7-8]。
- 增大裂隙 α 值会降低毛细压力梯度，导致部分上坡方向的流径消失，如沿 cd 段的垂向二次流 [Liu 2002, pp. 6-7]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 流动路径一般垂直，亚水平裂隙促进横向扩展 | [Liu 2002, pp. 1-1, 4-5] | 二维非饱和裂隙网络，稳态，重力主导 | 基于图2的路径图，排除水通量<0.01%总补给的裂隙段 |
| 小迹长裂隙不参与全局流动，但部分与主路径连接并影响基质相互作用 | [Liu 2002, pp. 6-7, 8-8] | 稳态条件，初始裂隙饱和度0.1% | 通过饱和度>7%的裂隙段分布图识别，Zone A 中许多小裂隙连接至骨干 |
| 流径平均间距随深度增加（层状系统，重力驱动） | [Liu 2002, pp. 1-1, 8-8] | 基于模拟结果提出的假设，需现场验证 | 示意性三层模型（图4）描述机理 |
| 毛细屏障效果在二维裂隙网络中不同于多孔介质，渗透率增加未使渗漏减少 | [Liu 2002, pp. 7-8] | 渗流模拟，裂隙与洞室相交 | 因缺乏横向流动路径，高度依赖裂隙走向和连接性 |
| α 值增大时，部分垂向流径消失（如从d点向下的流径） | [Liu 2002, pp. 6-7] | 增大α后毛细压力梯度降低 | 对比图2和图5，表明参数敏感性 |

## Limitations
- 所有模拟均为二维稳态，无法反映三维流动路径的绕流和真实毛细屏障三维效应 [Liu 2002, pp. 1-1]。
- 裂隙网络统计特性仅基于 Yucca Mountain TSw 单元单次校准，通用性未经验证。
- 未涉及瞬态流、基质–裂隙非平衡交互及地球化学过程。
- 模拟域相对较小（10m 尺度），边界效应可能影响大尺度推断。
- 未从索引片段中确认是否对网格分辨率、收敛性及参数不确定性进行了严格分析。

## Assumptions / Conditions
- 二维竖直剖面裂隙网络，稳态非饱和流，等温条件 [Liu 2002, pp. 1-1]。
- 单裂隙可概化为二维多孔介质，其本构关系由 van Genuchten 模型描述 [Liu 2002, pp. 2-3]。
- 裂隙孔径与迹长服从经验幂律关系 b = cLᵈ，参数基于场地平均空气渗透率校准 [Liu 2002, pp. 2-3]。
- 裂隙初始饱和度设为 0.1%，残-余饱和参数固定：Ss = 1，Sr = 0.01，m = 0.633 [Liu 2002, pp. 2-3]。
- 基质不透水，仅考虑裂隙内的流动，基质仅作为交互对象考虑（如基质扩散）而未模拟基质水流 [Liu 2002, pp. 1-1]。
- 流径判断基于通量阈值（<0.01%顶部总通量即忽略）[Liu 2002, pp. 4-5]。

## Key Variables / Parameters
- 裂隙几何：迹长 L，平均孔径 b，连通性（未量化）
- 水力参数：van Genuchten 模型参数 α, n, m (m = 1 − 1/n)，相对渗透率 kr，有效饱和度 Se，毛细压力 Pc
- 裂隙组参数：见表1，包含渗透率 k
- 孔径‑迹长系数：c = 1.008 × 10⁻⁴, d = 0.317
- 流径表征：流径间距（深度函数），水平扩展宽度，垂直流径数量
- 毛细屏障指标：影响区高度，空气进入值 ≈1/α

## Reusable Claims
- **Claim 1**：在重力主导的二维非饱和裂隙网络中，流动路径主要由连通的大迹长裂隙决定，路径方向趋于垂直；亚水平裂隙充当横向连接通道，造成路径的水平扩散 [Liu 2002, pp. 4-5]。  
  **条件**：稳态、非饱和补给、裂隙迹长分布分异明显、基质流可忽略。  
  **限制**：二维假设可能高估垂向连续性和低估三维迂回；未考虑瞬态补充和基质储存。

- **Claim 2**：短小裂隙尽管不贡献全局贯通流量，但它们与骨干流动路径的连接会扩大裂隙‑基质的接触面积，从而增强溶质扩散、热交换等依赖于界面面积的相互作用过程 [Liu 2002, pp. 6-7]。  
  **条件**：必须有部分小裂隙与主流动路径存在力学连通；适用于溶质运移或基质扩散主导的情形。  
  **限制**：未从索引片段中确认量化增强倍数，且模拟假设基质仅作为交换对象而未模拟其内部流动。

- **Claim 3**：层状非饱和裂隙系统中，若各层垂向裂隙密度不同，流径间距会随深度增加而增大，这是因为下层有限的垂向裂隙数量迫使流径汇聚（流聚焦）。该机制可能存在于 Yucca Mountain 焊接单元，但需要钻孔或开挖记录验证 [Liu 2002, pp. 4-6, 8-8]。  
  **条件**：重力驱动流，各层裂隙连通性允许流径重排，补给空间分布相对均匀。  
  **限制**：证据来自二维概念模型和数值实验，实际地质体可能受三维裂隙网络和瞬态事件（如暴雨脉冲）调制。

- **Claim 4**：定义“毛细屏障影响区”为洞室上方裂隙中水积累并可能发生渗漏的区域。当裂隙被水充填的高度超过自身空气进入值（≈1/α）且缺乏有效侧向排水路径时，渗漏启动。这解释了为何裂隙网络中渗透率增大未必减少渗漏，与均质多孔介质的认识不同 [Liu 2002, pp. 7-8]。  
  **条件**：地下洞室与亚垂直裂隙相交，补给持续，不考虑蒸发。  
  **限制**：二维网络中侧向排水路径常被低估，需三维模型更真实评估影响区形状和有效性。

## Candidate Concepts
- [[unsaturated flow in fractures]]
- [[discrete fracture network model]]
- [[flow focusing in vadose zone]]
- [[capillary barrier effect]]
- [[fracture-matrix interaction]]
- [[percolation in fracture networks]]
- [[gravity-driven fracture flow]]
- [[influence zone of capillary barrier]]
- [[seepage into underground openings]]

## Candidate Methods
- [[TOUGH2 multiphase simulator]]
- [[van Genuchten model for fracture]]
- [[fracture network generation by statistical realization]]
- [[trace length–aperture correlation]]
- [[particle tracking or flux thresholding for flow paths]]
- [[steady state unsaturated flow simulation]]

## Connections To Other Work
- 与早期有限裂隙数的二维非饱和网络模拟（如 Kwicklis and Healy [1993]、Karasaki et al. [1993]）相比，本研究在大规模含数千裂隙的网络中进行，揭示了流径结构与大裂隙的主控作用 [Liu 2002, pp. 1-2]。
- Therrien and Sudicky [1996] 的三维分析指出裂隙连通性导致不规则水力头分布，本研究在二维下观察到类似的垂直‑水平路径耦合。
- Liu and Bodvarsson [2001] 利用相同裂隙网络模型发展本构关系，本工作延伸为流径与渗流问题。
- 与现场观测（Wang et al. [1999] 在 Yucca Mountain 隧道中看到的孤立湿润带）定性一致，支持模拟流聚焦模式 [Liu 2002, pp. 4-5]。
- 与多孔介质毛细屏障研究（例如 Birkholzer et al. [1999]）对比，表明裂隙网络中渗透率增加未减少洞室渗漏，凸显离散裂隙效应 [Liu 2002, pp. 7-8]。
- 方法学上承接 Pruess and Tsang [1990] 等将单裂隙视为多孔介质的思路，并采用 TOUGH2 代码。

## Open Questions
- 三维裂隙网络中毛细屏障影响区的形状、连通性与渗流阈值是否显著不同于二维情形？[Liu 2002, pp. 1-1]
- “流径间距随深度增加”的假设在瞬态补给、存在基质吸力变化的条件下是否依然成立？
- 小裂隙对基质‑裂隙溶质交换（如基质扩散）的增强幅度能否通过明确的双渗透率模型加以验证？
- α 等参数的敏感性及其在野外尺度上的变异性如何影响流径拓扑？
- 不排除的基质流动是否会改变骨干流径的控制作用？

## Source Coverage
本页依据论文摘要、引言、方法与结果、结论部分的 9 个索引片段写作，覆盖了研究目的、模拟设置、关键发现和主要讨论要点。片段包含表格、图示描述及部分结果讨论，但未提供完整方法细节（如网格生成具体算法、边界条件设置的全部参数）、敏感性分析详析以及全部参考文献列表。关于现场验证数据与模拟的定量对比信息也未能从片段中确认。因此部分段落（例如基质扩散的量化增强）仅为定性描述。
