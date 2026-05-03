---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2022-wang-improvements-to-the-fracture-pipe-network-model-for-complex-3d-discrete-fracture-netwo"
title: "Improvements to the Fracture Pipe Network Model for Complex 3D Discrete Fracture Networks."
status: "draft"
source_pdf: "data/papers/2022 - Improvements to the Fracture Pipe Network Model for Complex 3D Discrete Fracture Networks.pdf"
collections:
citation: "Wang, Chenhui, et al. \"Improvements to the Fracture Pipe Network Model for Complex 3D Discrete Fracture Networks.\" 2022."
indexed_texts: "12"
indexed_chars: "58030"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T10:52:20"
---

# Improvements to the Fracture Pipe Network Model for Complex 3D Discrete Fracture Networks.

## One-line Summary
从等效流动子域、边界节点处理、电导修正与网络拓扑合并四个方面改进了裂缝管道网络模型（FPNM），并提出了两个量化离散裂缝网络（DFN）复杂度的指标，使渗透率预测偏差在合成DFN上从−35% 降低至 −5.6% [Wang 2022, pp. 1-2, pp. 5-10]。

## Research Question
未从索引片段中确认明确提出的研究问题。根据内容，研究旨在改进现有FPNM以提升其对复杂三维离散裂缝网络的渗透率预测精度。

## Study Area / Data
研究数据为合成离散裂缝网络（DFN），包括：
- **两个初始验证案例**：模型1（5条规则裂缝）与模型2（8条定向裂缝），尺寸100<sup>3</sup>体素，分辨率1 μm/体素 [Wang 2022, pp. 5-6]。
- **六个子DFN场景**（sub1–sub6），其复杂性指标（平均交线数𝐴𝑁<sub>𝑖𝑙</sub>与平均交点数𝐴𝑁<sub>𝑖𝑝</sub>）各不相同，用于测试改进措施 [Wang 2022, pp. 7-8]。
- **两个基准测试案例**（S1：74条裂缝，孔径5 μm；S2：157条裂缝，孔径7 μm），通过ADFNE（版本1.5）生成，裂缝形状为方形，边长服从指数分布（范围0.2–0.8单位长度，均值0.3），并进行连通性分析以确保网络完全渗透 [Wang 2022, pp. 10-11]。
文中提及使用了“realistic fractured samples”（现实裂缝样本），但具体细节未从索引片段中确认 [Wang 2022, pp. 1-2]。

## Methods
- **基础模型**：裂缝管道网络模型（FPNM），将每条裂缝的每条渗流子域（裂缝质心到交线中点的部分）转化为等宽度矩形，用“立方定律”计算传导率，构建由节点元素与键元素组成的管道网络，施加恒压边界（进出口定压，其余面无流），通过求解线性方程组得到节点压力，利用达西定律计算绝对渗透率，线性方程组采用OpenCV代数求解器求解 [Wang 2022, pp. 2-5]。
- **参考基准**：格子Boltzmann方法（LBM），在开源求解器Palabos中进行单相稳态层流模拟，用于验证FPNM结果的准确性 [Wang 2022, pp. 4-5]。
- **四项改进**（针对原有Guo模型的偏差问题）：
  1. **等效宽度与直径修正**：使等效矩形渗流子域具有一致的等效宽度和裂缝直径，以更好地表征流动形态 [Wang 2022, pp. 7-8]。
  2. **边界节点长度修正**：将边界半球形节点按整球处理造成的额外压损予以消除（具体细节未从索引片段中完全确认） [Wang 2022, pp. 7-8]。
  3. **电导修正**：根据裂缝交角𝜃将交线区域局部放大，修正节点电导 𝑔～1/(sin(𝜃))<sup>2</sup>，仅施加于节点元素，不修改代表裂缝中部的键元素 [Wang 2022, pp. 9-10]。
  4. **合并节点与键**：对构建后的管道网络进行后处理，合并距离过近（如质心距离小于半开度）的节点或键，纠正网络拓扑错误 [Wang 2022, pp. 9-10]。
- **复杂度量化指标**：平均交线数 𝐴𝑁<sub>𝑖𝑙</sub> = ∑𝑁<sub>𝑖𝑙</sub>/(2𝑁<sub>𝑓</sub>) 和平均交点数 𝐴𝑁<sub>𝑖𝑝</sub> = ∑𝑁<sub>𝑖𝑝</sub>/(2𝑁<sub>𝑓</sub>) ，包含边界面的交线，用于表征DFN的连接复杂性 [Wang 2022, pp. 5-7]。
- **网络生成与连通性分析**：使用ADFNE代码生成合成DFN，并通过连通性分析去除孤立裂缝 [Wang 2022, pp. 10-11]。

## Key Findings
1. **原有模型在复杂DFN上偏差显著**：Guo的FPNM对简单网络（𝐴𝑁<sub>𝑖𝑙</sub>=3.8, 𝐴𝑁<sub>𝑖𝑝</sub>=0）预测准确，但对复杂网络（𝐴𝑁<sub>𝑖𝑙</sub>=6.0, 𝐴𝑁<sub>𝑖𝑝</sub>=6.13）出现大幅偏差，表明网络复杂度是核心影响因素 [Wang 2022, pp. 5-7]。
2. **提出的两个复杂性指标能够区分DFN的复杂度**：平均交线数和平均交点数越大，网络越复杂，可作为模型适用性及改进效果的参考 [Wang 2022, pp. 5-7]。
3. **四项改进逐步降低了预测偏差**：
   - 应用等效宽度与直径修正后，六个子DFN场景的平均偏差从−35% 降至 −18%（约17%改进） [Wang 2022, pp. 7-8]。
   - 再引入边界节点修正后平均偏差进一步下降（具体数值未完全确认，但后文提到平均偏差被降至−7%再到 −5.6%） [Wang 2022, pp. 7-10]。
   - 电导修正使平均偏差从−7% 降至 −5.6%（约1.4%改进），改善幅度较小是因为仅作用于节点元素 [Wang 2022, pp. 9-10]。
   - 合并节点与键确保了网络拓扑的正确性，避免了因重叠导致的数值问题 [Wang 2022, pp. 9-10]。
4. **改进后模型在复杂基准DFN上得到验证**：在S1（74条裂缝）和S2（157条裂缝）上构建了模型，并分析了裂缝方向分布，但索引片段未直接给出最终的渗透率对比结果 [Wang 2022, pp. 10-12]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Guo的FPNM对模型1（简单DFN）预测准确，对模型2（复杂DFN）偏差大 | [Wang 2022, pp. 5-6] | 模型2的𝐴𝑁<sub>𝑖𝑙</sub>=6.0, 𝐴𝑁<sub>𝑖𝑝</sub>=6.13；模型尺寸100³体素，分辨率1 μm/体素 | 偏差计算公式：deviation = (k_FPNM − k_LBM)/k_LBM ×100% |
| 六种sub DFN场景的平均偏差由−35%降至−18%（仅第一项改进） | [Wang 2022, pp. 7-8] | 子场景sub1至sub6的𝐴𝑁<sub>𝑖𝑙</sub>从5.0到6.0，𝐴𝑁<sub>𝑖𝑝</sub>从1.0到6.13 | 改进措施为等效宽度与直径一致性修正 |
| 电导修正后，六种场景的平均偏差由−7%降至−5.6% | [Wang 2022, pp. 9-10] | 包含所有前序改进；电导修正仅施加于节点元素 | 电导按 𝑔～1/(sin(𝜃))² 更新 |
| 等效宽度与直径的比较：新模型在scenario sub6上计算的等效宽度大于Guo模型 | [Wang 2022, pp. 7-8] | DFN scenario sub6有8条裂缝，𝐴𝑁<sub>𝑖𝑙</sub>=6.0 | 等效宽度需与直径一致才能准确表征流型 |
| 合并节点与键的四种特殊情形（图7a–7d）被列举并用于后处理 | [Wang 2022, pp. 9-10] | 情形包括：质心节点过近、交线中点与质心过近等 | 合并通过C++代码自动完成 |
| S1与S2基准DFN的连通性分析与裂缝方向分布 | [Wang 2022, pp. 10-12] | S1: 74裂缝，孔径5 μm；S2: 157裂缝，孔径7 μm；方向角在X、Y轴峰值80°–100°，Z轴接近均匀分布 | 未提供渗透率对比数字 |

## Limitations
未从索引片段中确认作者明确陈述的局限性。基于内容可推断或注意到的限制包括：
- 改进措施仅在合成DFN上进行验证，现实裂缝样本的适用性未从片段中获知。
- LBM基准本身存在数值误差，其作为绝对真值的精度依赖于网格和计算设置 [Wang 2022, pp. 4-5]。
- 模型仍基于平板裂缝、层流、不可压缩流动的假设，对粗糙裂缝、非达西流、湍流等情景未做讨论。

## Assumptions / Conditions
- 流体为单相、不可压缩、稳态层流（雷诺数定义来源于此） [Wang 2022, pp. 2-4]。
- 裂缝壁面满足无滑移边界条件，裂缝内流动可由简化至两平行板间的“立方定律”描述 [Wang 2022, pp. 2-4]。
- 管道网络模型中将每个裂缝子域等效为矩形域，流动沿裂缝取向对齐，方向不随全局压力梯度改变 [Wang 2022, pp. 2-4, pp. 9-10]。
- 边界条件：进口与出口设定恒定压力，其余面均为无流边界 [Wang 2022, pp. 4-5]。
- 合成DFN中的裂缝用平面椭圆或方形表示，开度和边长按给定确定性值或概率分布赋值 [Wang 2022, pp. 2, 10-11]。

## Key Variables / Parameters
- 𝜇：动力粘度 [Wang 2022, pp. 2-4]
- 𝑃：流体压力 [Wang 2022, pp. 2-4]
- 𝑄<sub>𝑖𝑗</sub>：节点i与j间的体积流量 [Wang 2022, pp. 4-5]
- 𝑔<sub>𝑖𝑗</sub>：节点i与j之间的调和平均电导 [Wang 2022, pp. 4-5]
- 𝑘：网络绝对渗透率（由达西定律计算） [Wang 2022, pp. 4-5]
- 偏差： (𝑘<sub>FPNM</sub>−𝑘<sub>LBM</sub>)/𝑘<sub>LBM</sub>×100% [Wang 2022, pp. 5-6]
- 𝐴𝑁<sub>𝑖𝑙</sub> = ∑𝑁<sub>𝑖𝑙</sub>/(2𝑁<sub>𝑓</sub>)：平均交线数 [Wang 2022, pp. 5-7]
- 𝐴𝑁<sub>𝑖𝑝</sub> = ∑𝑁<sub>𝑖𝑝</sub>/(2𝑁<sub>𝑓</sub>)：平均交点数 [Wang 2022, pp. 5-7]
- 裂缝孔径（aperture） [Wang 2022, pp. 10-11]
- 裂缝边长（square fracture side length） [Wang 2022, pp. 10-11]
- θ：裂缝法向与坐标轴夹角，或裂缝交角（用于电导修正） [Wang 2022, pp. 9-12]
- 等效宽度 (equivalent width) 与 直径 (diameter) [Wang 2022, pp. 7-8]

## Reusable Claims
1. 对于复杂的离散裂缝网络（高平均交线数和平均交点数），原有的FPNM（如Guo模型）预测的渗透率显著偏低；需通过修正等效子域几何和网络拓扑来降低偏差 [Wang 2022, pp. 5-7]。
2. 将裂缝管道网络模型中的等效矩形渗流子域赋予“一致的等效宽度与直径”可使计算的渗透率更接近LBM结果 [Wang 2022, pp. 7-8]。
3. 仅根据裂缝交角放大节点元素的导电率（𝑔∼1/(sin(𝜃))²），而不改变代表裂缝中部的键元素，能够在保持物理合理性的前提下，小幅降低预测偏差 [Wang 2022, pp. 9-10]。
4. 在FPNM构建后对重叠或距离过近的节点与键进行自动合并，能够纠正因网络拓扑错误引起的模拟失真 [Wang 2022, pp. 9-10]。
5. 平均交线数和平均交点数可作为量化DFN复杂性的实用指标，帮助评估FPNM的适用性和改进需求 [Wang 2022, pp. 5-7]。

## Candidate Concepts
- [[Discrete Fracture Network (DFN)]]
- [[Fracture Pipe Network Model (FPNM)]]
- [[Fracture Connectivity]]
- [[Intersection Line Number]]
- [[Intersection Point Number]]
- [[Cubic Law]]
- [[Equivalent Conductance]]
- [[Fracture Aperture]]
- [[Fracture Orientation]]
- [[Percolation Theory]]

## Candidate Methods
- [[Fracture Pipe Network Model (FPNM)]]
- [[Lattice Boltzmann Method (LBM)]]
- [[ADFNE (Alghalandis Discrete Fracture Network Engineering)]]
- [[Finite Element Method (FEM)]]
- [[Boundary Element Method (BEM)]]
- [[Node Merging (Pipe Network)]]
- [[Conductance Correction (Angle-based)]]
- [[Equivalent Width Correction]]
- [[OpenCV Algebraic Solver]]

## Connections To Other Work
- 文中将改进的FPNM与**Guo的模型**（作为旧版FPNM典型代表）进行比较，并指出旧模型在复杂DFN上的局限，明确了改进的来源与目标 [Wang 2022, pp. 5-7]。
- 引用**Sarkar et al. (2004)** 的发现——流体在裂缝内流动方向与裂缝取向一致，不受全局压力梯度方向改变——作为仅对节点元素进行电导修正而不修改键元素的依据 [Wang 2022, pp. 9-10]。
- 在背景中提及**Elsworth (1986)** 的混合边界元-有限元方法和**Dershowitz and Fidelibus (1999)** 将边界元法与FPNM结合的做法，说明FPNM可与其他数值方法衔接 [Wang 2022, pp. 1-1]。
- 使用**LBM**（基于Palabos）作为参考数值解，与**Pan et al. (2006)** 对LBM精度和收敛性的研究形成了方法验证链 [Wang 2022, pp. 4-5]。
- 可主题上链接到其他裂缝网络简化模拟概念，如[[Discrete Fracture Matrix (DFM)]]、[[Embedded Discrete Fracture Model (EDFM)]]、[[Equivalent Continuum Model]]以及裂缝网络生成与表征工具（如[[FraSIM]]）。

## Open Questions
- 改进的FPNM在现实三维裂缝样本（如岩心CT扫描重建或野外露头映射）上的预测能力未经索引片段确认。
- 综合四项改进后，对于更复杂网格（如更高裂缝密度、更宽尺寸分布）的计算稳定性和适用范围是否依然成立未从片段中得知。
- 未讨论粗糙度（如JRC或分形维数）对立方定律适用性和最终渗透率预测的影响。
- 边界节点修正的具体数学形式及作用机制在片段中未充分展示，其普适性有待进一步确认。

## Source Coverage
此页面基于12个索引片段撰写，片段覆盖了论文的首页要点（Key Points）、引言、方法原理、改进具体措施与初步效果、基准DFN构建过程。片段较多地记录了方法改进和部分定量比较（从−35% 到 −5.6%的偏差变化），但对完整的数值结果表、敏感性分析、讨论部分以及针对现实样本的验证细节覆盖不足。因此，本页面较为系统地呈现了改进维度和核心证据，但对模型在外延应用和更全面性能评估方面的信息仍不完整。
