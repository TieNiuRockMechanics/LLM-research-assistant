---
type: "paper"
paper_id: "2018-lei-correlation-between-fracture-network-properties-and-stress-variability-in-geological-me"
title: "Correlation Between Fracture Network Properties and Stress Variability in Geological Media."
status: "draft"
source_pdf: "data/papers/2018 - Correlation Between Fracture Network Properties and Stress Variability in Geological Media.pdf"
citation: "Lei, Qinghua, and Ke Gao. \"Correlation Between Fracture Network Properties and Stress Variability in Geological Media.\" *Geophysical Research Letters*, vol. 45, no. 8, 2018, doi:10.1002/2018GL077548. Accessed 2026."
indexed_texts: "10"
indexed_chars: "46811"
compiled_at: "2026-04-27T19:37:42"
---

# Correlation Between Fracture Network Properties and Stress Variability in Geological Media.

## One-line Summary

本研究通过数值模拟和基于张量的应力分析方法，发现裂缝网络中局部应力扰动与局部裂缝强度呈正线性相关，且连通裂缝系统在临界应力状态下表现出显著的全局应力变异性。[Lei 2018, pp. 1-1]

## Research Question

裂缝网络属性与地质介质中的应力变异性之间存在何种关联？[Lei 2018, pp. 1-1]

## Study Area / Data

研究使用两类裂缝网络数据：(1) 合成裂缝网络，遵循幂律长度分布，特征参数包括幂律长度指数 a（1.5、2.0、2.5、3.0、3.5）和平均裂缝强度 γ（2.5 和 5.0 m⁻¹）；(2) 天然裂缝网络，基于 [[Hornelen Basin]] 露头测绘图案提取（引用 Odling, 1997）。所有模型均采用 10 m × 10 m 的二维域。[Lei 2018, pp. 1-2, 2-4]

## Methods

应力场由 [[有限-离散元模型]]（FDEM）获得 [Lei 2018, pp. 1-1]。应力数据分析采用基于张量的数学形式，具体包括：(1) 计算欧几里得距离 d(Sᵢ, S̄) = ||Sᵢ – S̄||_F 作为局部应力扰动度量 [Lei 2018, pp. 4-5]；(2) 使用 [[Fréchet均值]] 确定平均应力张量，该均值等于远场（构造）应力张量 [Lei 2018, pp. 4-5]；(3) 使用有效方差 Ve(S) 表征整体应力分散 [Lei 2018, pp. 10-11]。

## Key Findings

1. 局部应力扰动 d(S, S̄) 与局部裂缝强度 γ（单位面积裂缝总长度）呈正线性相关，该关系在不同裂缝网络、摩擦系数和构造应力条件下普遍成立 [Lei 2018, pp. 5-10, 10-11]。
2. 上述线性相关系数强烈依赖构造应力条件 [Lei 2018, pp. 10-11]。
3. 当裂缝网络连通（p > pc）时，系统能容纳显著增大的滑移应变，尤其在高差应力比（S∞xx/S∞yy = 3.0）和低摩擦系数（μ = 0.6）条件下 [Lei 2018, pp. 10-11]。
4. 整体应力有效方差 Ve(S) 在连通裂缝系统和高差应力条件下最大；在非连通域（p < pc）中 Ve(S) 与摩擦系数 μ 无关，而在连通域（p > pc）中 Ve(S) 随 μ 增大而显著减小 [Lei 2018, pp. 10-11]。
5. 裂缝连通性对控制地质介质中的应变/应力分布起关键作用，连通且处于临界应力状态的系统表现出强烈的应变局部化和应力分散 [Lei 2018, pp. 11-11]。

## Limitations

- 研究局限于二维场景，三维情况下的相关性未从索引片段中确认 [Lei 2018, pp. 1-2]。
- 假设裂缝模式是古应力演化的结果，与当代构造应力无关，且不考虑残余应力效应 [Lei 2018, pp. 1-2]。
- 分析仅针对固定尺度，未考虑尺度效应 [Lei 2018, pp. 1-2]。
- 天然裂缝网络仅来自 Hornelen Basin 单一露头，其代表性可能有限（未从索引片段中明确确认）。

## Reusable Claims

- “Local stress perturbation, quantified by Euclidean distance of local stress tensor to mean stress tensor, has a positive, linear correlation with local fracture intensity, defined as the total fracture length per unit area.” [Lei 2018, pp. 1-1]
- “A well-connected fracture system under a critically stressed state exhibits strong local and global stress variabilities.” [Lei 2018, pp. 1-1]
- “The effective variance of the entire stress field increases substantially as the fracture system transits from disconnected to connected states, especially under high differential stress.” [Lei 2018, pp. 10-11]

## Candidate Concepts

[[fracture network]] [[stress variability]] [[local fracture intensity]] [[effective variance]] [[tensor-based stress analysis]] [[Fréchet mean]] [[finite-discrete element model]] [[power law length scaling]] [[percolation parameter]] [[sliding strain]] [[critically stressed state]] [[Hornelen Basin]]

## Candidate Methods

[[finite-discrete element method (FDEM)]] [[tensor-based stress variability characterization]] [[Euclidean distance between stress tensors]] [[effective variance computation]] [[power law fracture network generation]] [[outcrop mapping analysis]]

## Open Questions

- 三维场景下裂缝网络属性与应力变异性的相关性是否仍保持正线性关系？(未从索引片段中确认)
- 尺度效应如何影响本研究得到的定量关系？(未从索引片段中确认)
- 残余应力对裂缝网络应力分布的影响是什么？(未从索引片段中确认)
- 天然裂缝网络的多样性（如非幂律分布）是否会改变结论？(未从索引片段中确认)

## Source Coverage

[Lei 2018, pp. 1-1], [Lei 2018, pp. 1-2], [Lei 2018, pp. 2-4], [Lei 2018, pp. 4-5], [Lei 2018, pp. 5-10], [Lei 2018, pp. 10-11], [Lei 2018, pp. 11-11], [Lei 2018, pp. 11-12]
