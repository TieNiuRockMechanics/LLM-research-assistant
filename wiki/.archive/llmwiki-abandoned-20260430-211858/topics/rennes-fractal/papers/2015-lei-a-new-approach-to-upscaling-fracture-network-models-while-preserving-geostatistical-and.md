---
type: "paper"
paper_id: "2015-lei-a-new-approach-to-upscaling-fracture-network-models-while-preserving-geostatistical-and"
title: "A New Approach to Upscaling Fracture Network Models While Preserving Geostatistical and Geomechanical Characteristics."
status: "draft"
source_pdf: "data/papers/2015 - A new approach to upscaling fracture network models while preserving geostatistical and geomechanical characteristics.pdf"
citation: "Lei, Qinghua, et al. \"A New Approach to Upscaling Fracture Network Models While Preserving Geostatistical and Geomechanical Characteristics.\" *Journal of Geophysical Research: Solid Earth*, vol. 120, no. 7, 2015, doi:10.1002/2014JB011736."
indexed_texts: "22"
indexed_chars: "107132"
compiled_at: "2026-04-27T19:34:02"
---

# A New Approach to Upscaling Fracture Network Models While Preserving Geostatistical and Geomechanical Characteristics.

## One-line Summary
本文提出了一种将二维裂缝网络模型升级到更大尺度的方法，该方法能够保留较小尺度“源”裂缝模式的地质统计和地质力学特性 [Lei 2015, pp. 1-1]。

## Research Question
本文旨在解决在升级裂缝网络模型时，如何同时保留裂缝系统的地质统计特征（如空间组织、长度、连通性）和地质力学特性（如裂缝开度、剪切位移在应力作用下的分布）这一核心问题 [Lei 2015, pp. 1-1]。研究聚焦于原位尺度（1–100米），在此尺度下，流体流动通常由裂缝主导，尤其是在结晶岩石中 [Lei 2015, pp. 1-2]。

## Study Area / Data
研究使用了来自野外露头的裂缝模式数据。该露头系统形成了两个近乎垂直的、层位正交的裂缝组，走向分别为约100°（Set 1）和约140°（Set 2），这些裂缝是构造张裂过程中形成的 [Lei 2015, pp. 2-4]。裂缝系统发育在约26厘米厚的石灰岩层中，该岩层夹在几乎不透水的页岩之间，裂缝是层间限定的 [Lei 2015, pp. 2-4]。研究者从一个约12米×12米的露头图中提取了一个6米×6米的方形子区域（包含约1000条裂缝）作为样本，以测量其标度特性 [Lei 2015, pp. 2-4]。图中的成像分辨率约为0.05米 [Lei 2015, pp. 2-4]。一个更小的2米×2米区域被选用于地质力学建模，并作为网络升级的“源”网络 [Lei 2015, pp. 2-4]。

## Methods
该方法主要包含以下步骤 [Lei 2015, pp. 1-1]:
1.  **源网络特性分析**: 使用分形几何和幂律关系分析露头裂缝模式在空间组织、长度、连通性及法向/剪切位移方面的标度特性 [Lei 2015, pp. 1-1]。
2.  **地质力学建模**: 使用有限-离散元方法（FEMDEM）对大小为2米×2米的裂缝岩石样本进行地质力学建模，以捕捉其在原位应力作用下裂缝开度和剪切位移的真实分布 [Lei 2015, pp. 1-1][Lei 2015, pp. 7-9]。
3.  **网络升级**: 开发了一种新颖的方案，该方案通过在递归自引用晶格中容纳离散时间随机游走，将裂缝及其依赖于应力和标度的属性成核并传播到更大区域（高达54米×54米） [Lei 2015, pp. 1-1]。该方法的关键在于利用从源网络统计量化得到的特征（如裂缝中心的间距分布、断裂长度、曲率等）来指导生长晶格中裂缝的生成 [Lei 2015, pp. 7-10]。
4.  **水力行为模拟**: 通过单相流模拟，对不同地质力学情景下多尺度裂缝网络的水力行为进行建模 [Lei 2015, pp. 1-1]。

## Key Findings
- 研究中的裂缝模式是非分形的，分形维数 *D* 接近 2 [Lei 2015, pp. 1-1][Lei 2015, pp. 4-5]。
- 裂缝长度分布倾向于遵循幂律，指数 *a* 在 2 到 3 之间 [Lei 2015, pp. 1-1]。针对该研究模式，从累积分布和密度分布估计的 *a* 值分别为 *a* = 2.45 和 *a* = 2.37 [Lei 2015, pp. 5-6]。
- 该方法的优势包括：保留了天然裂缝的非平面性、捕获了长裂缝的存在、保持了裂缝开度变化的真实性，以及尊重了位移-长度相关性的应力依赖性 [Lei 2015, pp. 1-1]。
- 在不同的地质力学情景下，观测到了不同的渗透率标度趋势，并识别出一个转变区，在此区域中，随着网络尺度的增加，流动结构从高度通道化转变为分布式 [Lei 2015, pp. 1-1]。

## Limitations
文章在讨论中提到，潜在重要的三维效应在本研究中未被处理 [Lei 2015, pp. 2-4]。关于方法在其他地质环境下的适用性或计算成本的讨论，未从索引片段中确认。

## Reusable Claims
- 该研究中，裂缝模式是非分形的（分形维数 D ≈ 2.0），这意味着裂缝中心在二维空间中表现出均匀填充 [Lei 2015, pp. 4-5]。
- 应用于该裂缝系统的幂律长度指数 *a* （约 2.4）表明，随着裂缝尺寸增大，其数量递减的模式可由幂律模型捕获 [Lei 2015, pp. 5-6]。
- 在使用该升级方法生成的网络中，在不同地质力学应力场景下，可以观测到渗透率随尺度变化的非单调行为，这是通过考虑应力依赖的裂缝属性实现的 [Lei 2015, pp. 1-1]。

## Candidate Concepts
- [[fracture reservoir]]
- [[Discrete Fracture Networks (DFNs)]]
- [[power law length distribution]]
- [[fractal dimension]]
- [[scale-dependent permeability]]
- [[in situ stress]]
- [[FEMDEM (combined finite-discrete element method)]]

## Candidate Methods
- [[FEMDEM geomechanical model]] (用于模拟岩石力学行为) [Lei 2015, pp. 1-1]
- [[discrete-time random walk in recursive self-referencing lattices]] (用于裂缝的成核与传播) [Lei 2015, pp. 1-1]

## Open Questions
- 该研究方法能否成功扩展到三维裂缝网络？未从索引片段中确认。
- 该方法的计算成本是否可以进一步降低以使其适用于更大的工程尺度和实际的储层模拟？未从索引片段中确认。

## Source Coverage
- [Lei 2015, pp. 1-1] (摘要，方法概述，关键发现)
- [Lei 2015, pp. 1-2] (研究范围，研究背景)
- [Lei 2015, pp. 2-4] (研究区域与数据，数据特性)
- [Lei 2015, pp. 4-5] (分形维数分析)
- [Lei 2015, pp. 5-6] (长度分布分析，幂律指数)
- [Lei 2015, pp. 6-7] (裂缝开度-长度模型，地质力学建模)
- [Lei 2015, pp. 7-9] (源网络特性，空间信息)
- [Lei 2015, pp. 9-10] (随机游走传播方法)
