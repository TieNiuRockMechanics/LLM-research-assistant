---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-huang-development-and-application-of-three-dimensional-discrete-fracture-network-modeling-a"
title: "Development and Application of Three-Dimensional Discrete Fracture Network Modeling Approach for Fluid Flow in Fractured Rock Masses."
status: "draft"
source_pdf: "data/papers/2021 - Development and application of three-dimensional discrete fracture network modeling approach for fluid flow in fractured rock masses.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Huang, Na, et al. \"Development and Application of Three-Dimensional Discrete Fracture Network Modeling Approach for Fluid Flow in Fractured Rock Masses.\" *Journal of Natural Gas Science and Engineering*, vol. 91, 2021, p. 103957."
indexed_texts: "21"
indexed_chars: "104157"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T02:18:39"
---

# Development and Application of Three-Dimensional Discrete Fracture Network Modeling Approach for Fluid Flow in Fractured Rock Masses.

## One-line Summary
本文是一篇综述，系统回顾了三维离散裂隙网络（3D DFN）建模在裂隙岩体流体流动模拟中的生成方法、几何特性（连通性、分形）以及流动控制方程，并指出现有局限与未来方向。 [Huang 2021, pp. 1-1]

## Research Question
如何生成、离散化并计算三维离散裂隙网络中的单相及多相流体流动？现有方法的优缺点及适用条件是什么？ [Huang 2021, pp. 1-1]

## Study Area / Data
本文为综述性文章，未针对特定研究区域，而是整合了多篇已发表研究的数据与方法，涵盖实验室测量、野外露头及数值模拟证据；重点关注裂隙几何（方向、长度、开度分布）和流动特性（连通性、渗透率、沟道流）的全球成果。 [Huang 2021, pp. 1-1至6-7]

## Methods
采用系统综述方法，围绕三个主题展开调查：①3D DFN的随机生成（基于Fisher分布的方向建模、幂律长度分布、密度参数P32等）；②几何特性分析，包括连通性指标（λ, C1）、逾渗理论及分形维数（D3D与D2D的关系）；③流动控制方程（立方定律、雷诺方程）及其对粗糙裂隙的适用性。同时也提及了地质力学约束的混合DFN模型，但本文聚焦于全随机方法。 [Huang 2021, pp. 2-3, 4-4, 6-7]

## Key Findings
- 2D DFN模型会显著低估渗透率，3D DFN建模方法因此受到越来越多关注。 [Huang 2021, pp. 1-2]
- 随机3D DFN生成时，裂隙方向最常用Fisher分布描述；裂隙长度可服从幂律、指数、对数正态等多种分布。 [Huang 2021, pp. 2-3]
- 天然裂隙表面粗糙度导致局部开度呈非均匀分布（如截断高斯或对数正态），进而诱发优先流或沟道流现象。 [Huang 2021, pp. 3-4]
- 裂隙网络连通性随裂隙密度和尺寸增加而增强，但方向围绕优势方向聚簇会降低连通性；从2D切面提取的连通性在逾渗阈值附近严重低估3D真实情况，并给出了排除面积关系式。 [Huang 2021, pp. 4-5]
- 3D裂隙网络的分形特征与2D切面分维之间存在解析关系，该关系受控于3D长度指数a3D和分维D3D；裂隙煤中3D分维与渗透率正相关。 [Huang 2021, pp. 5-6]
- 对于相对光滑的裂隙（JRC 0–2），雷诺方程会低估流量5–15%；尽管存在近似误差，雷诺方程仍是目前大多数3D粗糙裂隙网络模拟采用的简化形式，尚未有直接求解纳维-斯托克斯方程的3D DFN研究发表。 [Huang 2021, pp. 6-7]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 2D切面显著低估3D裂隙网络连通性，尤其在逾渗阈值附近；提出了排除面积Aex公式(4)以关联2D迹线图与3D密度。 | Lang et al. 2014，引自 [Huang 2021, pp. 4-5] | 裂隙网络处于低到中等密度，逾渗阈值邻域。 | Aex=2πl²（非逾渗迹线图）或l²（逾渗迹线图）。 |
| 对于JRC 0–2的光滑裂隙，雷诺方程比纳维-斯托克斯方程低估流量约5–15%。 | Koyama et al. 2008，引自 [Huang 2021, pp. 6-7] | 流动为层流，裂隙表面相对光滑。 | 粗糙度增大时误差可能更大，如Crandall et al. (2010) 报告透射率差35倍。 |
| 3D裂隙网络连通性随裂隙密度和/或尺寸增加而提高，但方向聚簇使连通性降低。 | Ivanova et al. 2014，引自 [Huang 2021, pp. 4-5] | 研究基于MIT 2010‑2012期间多种网络配置。 | 采用交点密度等指标。 |
| 2D分维D2D与3D分维D3D及3D长度指数a3D存在分异关系，由公式(5)–(7)给出。 | Darcel et al. 2003a，引自 [Huang 2021, pp. 5-6] | 裂隙长度服从幂律分布。 | 当a3D ≥ 2时，D2D = D3D – 1。 |
| 裂隙煤内部3D分形维数与渗透率呈正比。 | Ju et al. 2017，引自 [Huang 2021, pp. 5-6] | 实验室裂隙煤样。 | 实验证据。 |
| 随机DFN模型采用Fisher分布（公式1）定义裂隙丛方向。 | Baghbanan and Jing 2007; Baghbanan and Lanru Jing 2008，引自 [Huang 2021, pp. 2-3] | 裂隙形成簇，方向围绕一个优势矢量。 | κ值控制集中度。 |
| 雷诺方程适用于低流速、开度缓慢变化的假设，能满足大多数水文地质尺度问题。 | de Dreuzy et al. 2012，引自 [Huang 2021, pp. 6-7] | 大尺度裂隙，水力梯度不高。 | 当前缺少直接求解NS方程的3D DFN研究。 |

## Limitations
- 雷诺方程在流速较高或开度剧烈变化时不再准确，而当前尚无直接使用纳维-斯托克斯方程模拟3D DFN的成果，流动模拟精度受限。 [Huang 2021, pp. 6-7]
- 全随机DFN模型忽略T型交叉等复杂拓扑关系及力学成因约束，可能偏离实际裂隙网络结构。 [Huang 2021, pp. 4-4]
- 仅依靠分形维数不足以完整表征3D裂隙网络，还需同时考虑长度、密度、方向等属性。 [Huang 2021, pp. 5-6]
- 本文未提供关于离散化方法、多相流模型和实际应用案例的详细审查，这些局限反映在片段覆盖的不完全性中。

## Assumptions / Conditions
- 随机DFN生成假设裂隙中心在空间内均匀随机分布，方向服从Fisher等概率分布，长度以独立分布赋值。 [Huang 2021, pp. 2-3]
- 流动模拟中广泛采用雷诺方程，这要求流体为层流、流速低且局部开度变化平缓。 [Huang 2021, pp. 6-7]
- 逾渗分析通常假定裂隙网络统计自相似，且在阈值附近服从普适标度律。 [Huang 2021, pp. 4-4]

## Key Variables / Parameters
- **κ**：Fisher分布常数（方向集中度） [Huang 2021, pp. 2-3]
- **a3D**：三维裂隙长度幂律指数 [Huang 2021, pp. 2-3]
- **P32**：单位体积总裂隙表面积 [Huang 2021, pp. 3-4]
- **D3D, D2D**：三维与二维分形维数 [Huang 2021, pp. 5-6]
- **λ**：每个裂隙的平均交点数 [Huang 2021, pp. 4-4]
- **C1**：单位体积交点数 [Huang 2021, pp. 4-4]
- **JRC**：节理粗糙度系数（0–20） [Huang 2021, pp. 3-4]
- **e**：水力开度 [Huang 2021, pp. 6-7]
- **Kij**：局部传导系数 [Huang 2021, pp. 6-7]
- **Aex**：排除面积（关联2D迹线图与3D密度） [Huang 2021, pp. 4-5]

## Reusable Claims
1. 若三维裂隙长度服从幂律分布，其二维切面的分形维数可由关系式D2D = 2（当a3D ≤ 2 且 a3D ≤ D3D – 1）、D2D = D3D – a3D + 1（当a3D ≤ 2 且 a3D ≥ D3D – 1），或D2D = D3D – 1（当a3D ≥ 2）确定。 [Darcel et al. 2003a，引自Huang 2021, pp. 5-6] 条件：裂隙网络满足幂律长度分布。限制：关系不适用于非幂律分布或强非均质方向结构。

2. 从二维迹线图推断三维连通性时，在逾渗阈值附近会出现严重低估，可通过排除面积Aex建立校正：Aex = 2πl²（非逾渗迹线图）或l²（逾渗迹线图）。 [Lang et al. 2014，引自Huang 2021, pp. 4-5] 条件：裂隙网络处于稀疏到中等密度区间。限制：公式基于特定几何假设，可能不适用于强各向异性或非随机网络。

3. 在低流速、裂隙开度变化平缓的条件下，粗糙裂隙流动可由雷诺方程模拟，但对JRC 0–2的光滑裂隙，其流量会被低估约5–15%；若表面更粗糙，误差可能进一步加大（有研究显示透射率差可达35倍）。 [Koyama et al. 2008; Crandall et al. 2010，引自Huang 2021, pp. 6-7] 条件：层流、低雷诺数。限制：不适用于高流速或非达西流，且目前缺乏直接验证的NS方程模拟。

4. 三维随机裂隙网络的连通性随裂隙密度和尺寸增加而改善，但当裂隙方向围绕优势方向聚集时，连通性会降低，因为聚簇减少了不同方向裂隙的交切机会。 [Ivanova et al. 2014，引自Huang 2021, pp. 4-5] 条件：采用交点数密度等指标评估。限制：结论来自数值实验，天然网络的力学成因可能改变连通规律。

5. 对于裂隙煤，内部裂隙网络的三维分形维数与渗透率呈正比关系，分维可作为渗透率预测的间接指标。 [Ju et al. 2017，引自Huang 2021, pp. 5-6] 条件：实验室尺度煤样。限制：尺度外推需谨慎，且依赖分维估算方法。

## Candidate Concepts
- [[Discrete Fracture Network]]
- [[Fracture connectivity]]
- [[Percolation theory]]
- [[Fracture scaling]]
- [[Fractal dimension]]
- [[Joint Roughness Coefficient (JRC)]]
- [[Channeling flow]]
- [[Hydraulic aperture]]
- [[Equivalent permeability]]
- [[Fracture sets]]

## Candidate Methods
- [[Stochastic 3D DFN generation]]
- [[Fisher distribution modeling]]
- [[Power law fracture length distribution]]
- [[Percolation analysis]]
- [[Fractal dimension estimation]]
- [[Reynolds equation approximation]]
- [[Cubic law]]
- [[Excluded area mapping]]

## Connections To Other Work
本文作为综述，多次引用并定位了先前的重要综述工作：Berkowitz (2002) 对裂隙介质流动与传输的全面回顾；Jing (2003) 对岩石力学数值方法能力的分析；Figueiredo et al. (2016) 关于稀疏通道模型的评述；Liu et al. (2016b) 对二维DFN等效渗透率的总结。 [Huang 2021, pp. 1-2] 这些工作为此处聚焦于三维DFN的几何生成与流动计算提供了背景和对比。此外，作者明确指出随机DFN的不足，并指引读者参考Lei et al. (2017) 的地质力学建模综述，从而将本工作与考虑力学成因的DFN方法相连接。 [Huang 2021, pp. 4-4] 未从索引片段中确认与本篇综述有直接后续应用研究的特定链接。

## Open Questions
- 如何将纳维-斯托克斯方程直接应用于3D DFN模拟，以克服雷诺方程在粗糙裂隙高流速条件下的近似误差？ [Huang 2021, pp. 6-7]
- 多相流（如油‑气‑水）在离散裂隙介质中的建模方法及与单相流框架的集成方式是什么？ [Huang 2021, pp. 1-1]
- 如何更真实地在随机DFN中融入天然裂隙的复杂拓扑关系（如T型交叉）和力学约束？ [Huang 2021, pp. 4-4]
- 分形参数与其他几何属性如何协同以完整预测裂隙网络渗流行为？ [Huang 2021, pp. 5-6]
- 未从索引片段中确认关于DFN离散化技术、计算效率优化以及与现场试验验证相关的开放问题，这些可能位于综述后半部分。

## Source Coverage
本页依据所提供的8个索引片段（页码范围1-1至6-7）撰写，覆盖了论文的摘要、引言、3D DFN生成方法（第2节）、连通性与逾渗理论（2.2）、分形特征（2.3）以及数值模拟方法中的控制方程（第3节开头至雷诺方程比较）。关键缺口包括：离散化与网格划分技术、多相流扩展的具体方法、实际工程应用案例、结果讨论以及未来研究方向。这些内容可能存在于原文后续章节，但在现有片段中未体现，因此本页未纳入相应分析。
