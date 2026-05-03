---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-hou-quantitative-visualization-and-characteristics-of-gas-flow-in-3d-pore-fracture-system-o"
title: "Quantitative Visualization and Characteristics of Gas Flow in 3D Pore-Fracture System of Tight Rock Based on Lattice Boltzmann Simulation."
status: "draft"
source_pdf: "data/papers/2021 - Quantitative visualization and characteristics of gas flow in 3D pore-fracture system of tight rock based on Lattice Boltzmann simulation.pdf"
collections:
  - "zotero new"
citation: "Hou, Peng, et al. \"Quantitative Visualization and Characteristics of Gas Flow in 3D Pore-Fracture System of Tight Rock Based on Lattice Boltzmann Simulation.\" *Journal of Natural Gas Science and Engineering*, vol. 89, 2021, 103867. Accessed 2026."
indexed_texts: "14"
indexed_chars: "66749"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T03:06:40"
---

# Quantitative Visualization and Characteristics of Gas Flow in 3D Pore-Fracture System of Tight Rock Based on Lattice Boltzmann Simulation.

## One-line Summary
利用考虑气体滑脱效应的3D正则化格子Boltzmann模型（LBM），重构并模拟了致密岩石3D孔隙-裂缝系统中的气体流动，系统考察了微裂缝形态和气体稀薄效应对流动行为及渗透率的影响 [Hou 2021, pp. 1-1].

## Research Question
致密岩石3D孔隙-裂缝系统在孔隙尺度下的几何复杂性是预测气体流动的主要挑战。本研究旨在解决：微裂缝形态和气体稀薄效应如何共同影响孔隙-裂缝系统中的气体流动行为和渗透率？ [Hou 2021, pp. 1-1].

## Study Area / Data
- **实验材料：** 致密砂岩样本取自中国江苏徐州深部矿区 [Hou 2021, pp. 2-5].
- **矿物组成：** 主要矿物为石英（87.3%）、长石（6.1%）和方解石（3.9%） [Hou 2021, pp. 2-5].
- **孔隙类型：** 根据孔隙定义，主要由过渡孔、中孔和大孔组成 [Hou 2021, pp. 2-5].
- **孔隙结构获取：** 采用高分辨率3D X射线显微成像系统（Xradia 510 Versa）进行扫描，圆柱形砂岩样本直径为2 mm，分辨率为2 μm [Hou 2021, pp. 2-5].
- **数字岩心重建：** 基于表征单元体（REV）方法提取了完整致密砂岩的3D孔隙结构，重建后砂岩的孔隙度和连通孔隙度分别为5.71%和3.66%，孔径主要分布在2–60 μm [Hou 2021, pp. 5-5].
- **裂缝重建：** 利用Weierstrass-Mandelbrot分形函数在3D空间中生成具有不同形态的裂缝，以代表储层改造后形成的裂缝网络 [Hou 2021, pp. 5-5].

## Methods
- **数值方法：** 采用基于D3Q19离散速度模型的3D正则化格子Boltzmann模型（Lattice Boltzmann Model, LBM）。该方法的优势在于不受连续性假设限制，具有良好的数值稳定性、天然并行性和简单的流-固边界处理 [Hou 2021, pp. 1-2] [Hou 2021, pp. 5-6].
- **微尺度效应：** 模型考虑了气体滑脱效应。通过建立克努森数（Knudsen number, $Kn$）与弛豫时间的关系，修正了局部有效弛豫时间 [Hou 2021, pp. 6-8].
- **有效平均自由程：** 采用一种概率方法来计算3D多孔介质中受限气体的局部平均自由程（MFP, Mean Free Path），考虑了分子在六个主要方向（$x+, x-, y+, y-, z+, z-$）上受固体壁面限制的运动 [Hou 2021, pp. 6-8].
- **边界条件：** 孔隙壁面采用考虑Knudsen层校正的滑移边界条件，流-固界面假设为完全漫反射状态，并使用碰撞校正函数 $\chi$ 考虑真实气体效应。入口和出口应用基于线性外推的非平衡态外推压力边界条件 [Hou 2021, pp. 8-10].
- **模型验证：** 使用脉冲衰减气体渗透率测量系统（PDP-200）对完整致密砂岩样本进行室内渗透率实验，以验证LBM模型的准确性。实验岩心尺寸为$\Phi 25 \times 50$ mm，模拟采用该砂岩的REV。模拟和实验分别设定了5个不同的出口压力（1, 2, 3, 4和5 MPa）进行比较 [Hou 2021, pp. 10-11].

## Key Findings
- 微裂缝形态和气体稀薄效应是影响孔隙-裂缝系统中气体流动行为的两个强相关因素 [Hou 2021, pp. 1-1].
- 在低压条件下，孔隙-裂缝结构中的气体流动行为更加敏感 [Hou 2021, pp. 1-1].
- 对于具有高粗糙度裂缝或低裂缝连通度的系统，气体稀薄效应更为显著 [Hou 2021, pp. 1-1].
- 基于REV和分形函数重构的3D孔隙-裂缝系统可以有效用于模拟研究 [Hou 2021, pp. 1-1].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 重建砂岩的孔隙度为5.71%，连通孔隙度为3.66%，孔径主要分布在2–60 $μ$m | [Hou 2021, pp. 5-5] | 样本来自江苏徐州，CT分辨率为2 $μ$m | 孔隙度值与压汞实验结果基本一致，孤立孔隙主要分布在小孔径区域。 |
| 低压条件下，孔-缝系统中的气体流动行为更敏感；高粗糙度或低连通性裂缝使气体稀薄效应更敏感 | [Hou 2021, pp. 1-1] | LBM模拟结果 | 这是论文的核心发现，揭示了形态与微尺度效应的耦合作用。 |
| LBM模拟与PDP-200气体渗透率实验在不同出口压力（1–5 MPa）下的结果进行对比验证 | [Hou 2021, pp. 10-11] | 实验岩心$\Phi 25 \times 50$ mm，模拟用REV；模拟中压力梯度设为0.1 MPa/m | 尽管实验与模拟样本尺寸不同，但因为在同一数量级且均超过REV，作者认为尺寸效应可忽略。模型验证的具体结果（如吻合程度）未从索引片段中确认。 |

## Limitations
- 未从索引片段中确认。

## Assumptions / Conditions
- **表征单元体（REV）假设：** 从CT图像中提取的REV能够充分代表整个致密砂岩的孔隙结构特性。当重建砂岩尺寸大于REV尺寸时，样本尺寸对结果的影响可忽略不计 [Hou 2021, pp. 10-11].
- **裂缝形态建模假设：** 采用Weierstrass-Mandelbrot分形函数可以代表性地生成具有不同粗糙度和维度的微裂缝形态 [Hou 2021, pp. 5-5].
- **模型物理假设：** LBM模拟中的气体为等温流动，且气体分子在孔隙壁面的碰撞处于完全漫反射状态 [Hou 2021, pp. 5-6] [Hou 2021, pp. 8-10].
- **边界条件假设：** 入口和出口采用非平衡态外推压力边界，固定了压力梯度（0.1 MPa/m） [Hou 2021, pp. 10-11].

## Key Variables / Parameters
- `渗透率 (Permeability)`：评估流动能力的关键指标，通过达西定律估算 [Hou 2021, pp. 1-2].
- `克努森数 (Knudsen number, $Kn$)`：表征气体微尺度流动特性的无量纲数，与孔径和压力密切相关 [Hou 2021, pp. 1-2] [Hou 2021, pp. 6-8].
- `分形维数 (Fractal dimension, $D$)`：用于定量描述裂缝形态复杂性的参数，取值范围2 ≤ $D$ < 3 [Hou 2021, pp. 5-5].
- `分形粗糙度 (Fractal roughness, $G_0$)`：用于描述裂缝表面起伏程度的参数 [Hou 2021, pp. 5-5].
- `局部有效平均自由程 (Local effective Mean Free Path, $\lambda_{e, local}$)`：经固体壁面限制修正后的气体分子平均自由程，用于关联弛豫时间 [Hou 2021, pp. 6-8].
- `弛豫时间 (Relaxation time, $\tau$)`：LBM中与流体输运系数相关的核心参数，本研究中与$Kn$数关联以反映微尺度效应 [Hou 2021, pp. 6-8].
- `Knudsen层校正函数 $\psi(Kn)$` 与 `碰撞校正函数 $\chi$`：分别用于修正滑移边界和考虑真实气体效应 [Hou 2021, pp. 8-10].

## Reusable Claims
- **Claim 1:** 在LBM模拟中，通过建立弛豫时间与$Kn$数的关系，并结合考虑分子移动受限的局部有效平均自由程计算方法，可以有效模拟微尺度气体流动的滑脱效应 [Hou 2021, pp. 6-8].
  **Conditions:** 适用于等温、微纳米孔隙中的气体流动模拟，需要满足克努森数在合适的微尺度流态范围内。
  **Evidence:** 论文采用此方法构建了3D正则化LB模型，并与实验结果进行了对比验证 [Hou 2021, pp. 10-11].
  **Limitations:** 具体验证误差范围未从索引片段中确认。
- **Claim 2:** 裂缝的几何形态（粗糙度、分形维数）显著影响孔隙-裂缝系统中的气体流动行为与渗透率。高粗糙度或低连通性的裂缝结构会使气体流动对稀薄效应更敏感 [Hou 2021, pp. 1-1] [Hou 2021, pp. 5-5].
  **Conditions:** 该结论基于使用分形函数重构的不同形貌裂缝与致密砂岩REV耦合模型的LBM模拟。
  **Evidence:** 引言中对研究结果的总结。
  **Limitations:** 具体的影响规律、速度分布图像和渗透率变化曲线等定量细节未从索引片段中确认。

## Candidate Concepts
- [[Tight rock]]
- [[3D pore-fracture system]]
- [[Gas slippage effect]]
- [[Knudsen layer]]
- [[Representative Elementary Volume (REV)]]
- [[Fractal fracture]]
- [[Permeability]]
- [[Digital rock physics]]

## Candidate Methods
- [[Lattice Boltzmann Method (LBM)]]
- [[D3Q19 model]]
- [[Non-equilibrium extrapolation boundary condition]]
- [[Micro-X-ray computed tomography (Micro-CT)]]
- [[Weierstrass-Mandelbrot fractal function]]
- [[Pulse-decay permeability measurement]]

## Connections To Other Work
- 未从索引片段中确认任何具体的引用论文关系。从中可抽象出的候选连接主题包括：将LBM应用于页岩、白垩、砂岩的3D数字岩心流动模拟（如Faÿ-Gomord, 2017; Degruyter, 2010; Ju et al., 2017a）；利用$Kn$数修正LBM弛豫时间以模拟微尺度气体流动（如Wang et al., 2017a, 2017b）；以及利用CT扫描重构裂缝网络的研究（如Fan and Zhang, 2013; Wang et al., 2016; Ju et al., 2017b） [Hou 2021, pp. 1-2] [Hou 2021, pp. 5-5].

## Open Questions
- 未从索引片段中确认。可以从主题上推测，可能包括：该模型在其他类型致密岩石（如页岩、煤岩）中的适用性如何？考虑多相流或应力敏感效应时，流动规律会发生什么变化？

## Source Coverage
本页面基于论文的14个索引片段整理而成。覆盖内容偏重于`摘要`、`引言`、`方法`和`模型`部分，提供了关于研究背景、REV重构流程、LBM模型的详细构造（包括有效松弛时间、边界条件和局部平均自由程计算）以及研究主要发现的概述。然而，索引片段缺少详细的`结果`与`讨论`部分，因此对于不同裂缝参数（粗糙度、分形维数、裂缝数量）下的速度分布云图、渗透率变化曲线等定量分析证据严重缺失。此外，`模型验证`的具体对比结果（如误差分析）也未包含在内。
