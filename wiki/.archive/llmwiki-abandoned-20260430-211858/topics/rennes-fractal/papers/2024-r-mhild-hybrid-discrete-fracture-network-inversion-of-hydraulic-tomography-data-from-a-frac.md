---
type: "paper"
paper_id: "2024-r-mhild-hybrid-discrete-fracture-network-inversion-of-hydraulic-tomography-data-from-a-frac"
title: "Hybrid Discrete Fracture Network Inversion of Hydraulic Tomography Data From a Fractured-Porous Field Site."
status: "draft"
source_pdf: "data/papers/2024 - Hybrid Discrete Fracture Network Inversion of Hydraulic Tomography Data From a Fractured-Porous Field Site.pdf"
citation: "Römhild, Lukas, et al. \"Hybrid Discrete Fracture Network Inversion of Hydraulic Tomography Data From a Fractured-Porous Field Site.\" 2024."
indexed_texts: "18"
indexed_chars: "87979"
compiled_at: "2026-04-27T19:47:29"
---

# Hybrid Discrete Fracture Network Inversion of Hydraulic Tomography Data From a Fractured-Porous Field Site.

## One-line Summary

本文提出一种混合离散裂缝网络（DFN）反演方法，通过考虑非零基质渗透率，成功应用于德国哥廷根裂缝-孔隙场地的水力层析成像（HT）数据，并利用独立热示踪实验验证了结果[Lukas 2024, pp. 1-1]。

## Research Question

如何准确表征裂缝-孔隙介质场地中水力传导率的异质性？现有连续介质模型或纯DFN模型可能不足以描述同时包含离散裂缝和可渗透孔隙基质的系统，因此需要一种结合两者的混合反演方法[Lukas 2024, pp. 2-3]。

## Study Area / Data

- **场地**：位于德国哥廷根大学北校区，莱纳塔尔地堑东肩，地质构造复杂。岩性为下中科伊帕（Lower and Middle Keuper），以粘土序列和粉砂岩层为主；顶部14 m为第四纪石灰岩和粘土岩，含石英、长石和方解石矿化[Lukas 2024, pp. 2-3]。
- **HT实验**：2018年4月进行，为交叉孔多级抽水试验。在井O的隔离段以约30 L/min速率抽水，井M的对应隔离段（M2-M5）记录压力响应（精度1 mmH₂O，时间分辨率20 ms），形成四个源-接收对的层析配置。M5数据因噪声过高被排除。抽水井自身数据因不适用2D模型而未使用[Lukas 2024, pp. 3-5]。

## Methods

1. **标准走时反演**：基于pyGIMLi框架，采用广义高斯-牛顿法，利用Dijkstra算法计算水力走时，反演水力扩散率，再通过恒定比储水率（5×10⁻⁵ m⁻¹）转换为水力传导率。网格分辨率垂直0.5 m、水平1 m，源和接收点建模为点[Lukas 2024, pp. 5-6]。
2. **混合DFN反演**：在已有DFN反演方法基础上扩展，考虑基质非零渗透率。采用贝叶斯框架，通过马尔可夫链蒙特卡洛（MCMC）方法（含可逆跳跃算法）生成后验DFN集合。DFN参数包括裂缝位置、长度、水力传导率（优先范围未从索引片段中确认）。基质参数（K=10⁻⁶ m/s，Ss=5×10⁻⁵ m⁻¹）基于单井多层抽水试验[Lukas 2024, pp. 6-7]。基于光学遥视数据，识别三组主要裂缝方位（投影到2D后倾角为-0.94°、-26.31°、49.64°），并固定于反演中。初始DFN包含人工和随机生成的裂缝，以确保连通性[Lukas 2024, pp. 7-7]。

## Key Findings

- 混合DFN反演生成的后验裂缝网络（以最后一次迭代为例包含23条裂缝）中，裂缝水力传导率约0.25–0.99 m/s，比基质高约五个数量级[Lukas 2024, pp. 8-9]。
- 后验网络中仅有一条裂缝（编号B）直接连接两个对侧观测段，对应走时反演识别的高扩散率带；多数连接通过多条裂缝间接实现[Lukas 2024, pp. 8-9]。
- 部分裂缝末端与抽水段或观测段之间存在小间隙，间隙中的连接由基质流动维持，凸显了混合模型的重要性[Lukas 2024, pp. 8-9]。
- 利用独立热示踪实验数据对反演结果进行了成功验证[Lukas 2024, pp. 1-1]。

## Limitations

- 本文采用二维正向模型，因此无法使用抽水井自身的三分扩散数据[Lukas 2024, pp. 3-5]。
- M5观测段数据因噪声过高而被排除，减少了可用数据量[Lukas 2024, pp. 3-5]。
- 走时反演中使用的比储水率假设为恒定值（5×10⁻⁵ m⁻¹），可能导致不确定性[Lukas 2024, pp. 5-6]。
- 其他局限性未从索引片段中确认。

## Reusable Claims

- 混合DFN反演方法能成功应用于裂缝-孔隙介质场地的HT数据，并通过独立热示踪实验验证[Lukas 2024, pp. 1-1]。
- 后验裂缝水力传导率比基质高约五个数量级（0.25–0.99 m/s vs. 10⁻⁶ m/s）[Lukas 2024, pp. 8-9]。
- 多数跨井连接由多条裂缝间接形成，而非单一直接通道[Lukas 2024, pp. 8-9]。
- 使用光学遥视数据确定的固定裂缝方位角可有效约束反演[Lukas 2024, pp. 7-7]。
- 初始DFN的随机选择不影响最终后验集合的收敛[Lukas 2024, pp. 7-7]。

## Candidate Concepts

- [[Hydraulic Tomography]]
- [[Discrete Fracture Network]]
- [[Hybrid DFN Inversion]]
- [[Travel Time Inversion]]
- [[Markov Chain Monte Carlo]]
- [[Reversible Jump MCMC]]
- [[Hydraulic Diffusivity]]
- [[Specific Storage]]
- [[Hydraulic Conductivity]]
- [[Fractured-Porous Medium]]
- [[Matrix Flow]]

## Candidate Methods

- [[pyGIMLi]]（广义高斯-牛顿反演框架）
- [[Gmsh]]（网格生成）
- [[Gibbs Sampling]]（数据方差估计）
- [[Dijkstra's Algorithm]]（走时计算）

## Open Questions

- 本文方法在三维情况下如何扩展？相应结果未从索引片段中确认。
- 更精细的数据密度是否能够揭示更小尺度的裂缝特征？未从索引片段中确认。
- 基质参数（K、Sₛ）的均匀假设对反演结果的敏感性如何？未从索引片段中确认。

## Source Coverage

本页主要基于论文摘要（第1页）、方法部分（第2-7页）和结果/验证部分（第8-9页）的索引片段撰写。具体引用包括：[Lukas 2024, pp. 1-1], [Lukas 2024, pp. 2-3], [Lukas 2024, pp. 3-5], [Lukas 2024, pp. 5-6], [Lukas 2024, pp. 6-7], [Lukas 2024, pp. 7-7], [Lukas 2024, pp. 8-9]。所有非平凡结论均已标注来源。
