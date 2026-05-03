---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2017-lei-the-use-of-discrete-fracture-networks-for-modelling-coupled-geomechanical-and-hydrologi"
title: "The Use of Discrete Fracture Networks for Modelling Coupled Geomechanical and Hydrological Behaviour of Fractured Rocks."
status: "draft"
source_pdf: "data/papers/2017 - The use of discrete fracture networks for modelling coupled geomechanical and hydrological behaviour of fractured rocks.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Lei, Qinghua, et al. \"The Use of Discrete Fracture Networks for Modelling Coupled Geomechanical and Hydrological Behaviour of Fractured Rocks.\" *Computers and Geotechnics*, vol. 85, 2017, pp. 151-176, doi:10.1016/j.compgeo.2016.12.024. Accessed 15 Mar. 2026."
indexed_texts: "35"
indexed_chars: "174105"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T21:04:54"
---

# The Use of Discrete Fracture Networks for Modelling Coupled Geomechanical and Hydrological Behaviour of Fractured Rocks.

## One-line Summary
这篇综述讨论了使用离散裂缝网络（DFN）进行裂缝岩体几何表征、地质力学演化及水力-力学（HM）耦合行为模拟的最新技术，并提出了基于物理的DFN生成和地质力学模拟的建议 [Lei 2017, pp. 1-1]。

## Research Question
如何利用离散裂缝网络（DFN）可靠地模拟裂缝岩体的几何特征、地质力学响应和耦合水力-力学过程？当前不同DFN模型与数值框架各自的优劣是什么？ [Lei 2017, pp. 2-3]

## Study Area / Data
本文为方法论综述，无特定现场研究区域。数据来源于已发表文献中关于地质测绘裂缝网络、随机生成DFN和地质力学生长DFN的各类模拟与观测案例 [Lei 2017, pp. 1-2, 3-6]。

## Methods
- 将DFN模型分为三类进行总结：基于地质测绘的DFN、随机生成的DFN（包括Poisson模型及其改进、分形模型、序列生长模型）和基于地质力学模拟（如线性弹性断裂力学）的DFN [Lei 2017, pp. 3-8]。
- 回顾了整合显式裂缝几何的连续介质、非连续介质和混合地质力学数值模型 [Lei 2017, pp. 1-2]。
- 评述了研究地质力学对裂缝中流体流动影响的数值工作，并讨论了HM模拟对DFN与地质力学模型的选取要求 [Lei 2017, pp. 1-2]。

## Key Findings
- 地质测绘DFN能保留真实裂缝特征，但难以推广至深部岩体和三维结构 [Lei 2017, pp. 6-8]。
- 随机DFN方法简单、高效且适用于三维问题，但其假设的裂缝几何和拓扑可能忽略重要的力学与构造约束，导致较大不确定性 [Lei 2017, pp. 6-8]。
- 地质力学DFN可捕捉自然裂缝的力学特征，但对假设或测量的岩石性质及推断的古应力场高度敏感 [Lei 2017, pp. 6-8]。
- 未来方向之一是发展混合DFN模型，融合不同方法的优势 [Lei 2017, pp. 6-8]。
- 随机DFN中，Poisson模型是基础，改进版本可考虑非均匀空间分布、裂缝属性相关性、未破裂区域、拓扑复杂性及力学相互作用 [Lei 2017, pp. 4-4]。
- 自然裂缝网络的空间组织可用分形维数D描述，其密度-长度分布遵循幂律模型 \( n(l, L) = a L^D l^{-a} \) [Lei 2017, pp. 4-4]。
- 基于层次规则和亚临界裂缝生长法则的序列DFN模型可再现裂缝网络的成核、扩展和停获过程 [Lei 2017, pp. 4-6]。
- 地质力学DFN通常采用线性弹性断裂力学，通过迭代求解应力场、应力强度因子并应用生长准则（如亚临界定律 \( K_O \leq K_I \leq K_{IC} \)）来模拟裂缝网络演化 [Lei 2017, pp. 6-6]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 地质测绘DFN保留真实裂缝特征，但难以应用于深部和3D结构 | Lei 2017, pp. 6-8 | 近地表露头、LIDAR、钻孔成像、地震数据 | 基于对现有方法的描述 |
| 随机DFN模型假设裂缝为直线/多边形，将几何属性视为独立随机变量，可能忽略力学约束 | Lei 2017, pp. 3-4, 6-8 | 基于扫描线、窗口取样等统计的DFN生成 | 包括Poisson模型及其改进 |
| 分形DFN模型使用幂律分布描述裂缝密度-长度关系：\( n(l, L) = a L^D l^{-a} \) | Lei 2017, pp. 4-4 | 适用于呈现标度不变性的裂缝系统 | 分形维数D可通过盒计数法测得 |
| 地质力学DFN通过迭代计算应力强度因子KI和亚临界生长准则（\( K_O \leq K_I \leq K_{IC} \)）模拟裂缝扩展 | Lei 2017, pp. 6-6 | 基于线弹性断裂力学和已知岩石力学参数 | 模拟古应力条件下的裂缝网络形成 |
| 地质力学DFN对岩石性质与古应力场敏感，需耦合多场过程来吻合真实系统 | Lei 2017, pp. 6-8 | 需要可靠的岩石力学输入和地质历史约束 | 不确定性依然存在 |
| 随机DFN的Monte Carlo模拟需足够数量的实现来预测结果范围 | Lei 2017, pp. 4-6 | 有界参数空间，统计平稳性 | 适用于概率框架 |

## Limitations
- 各类DFN模型均有局限：地质测绘DFN受限于数据获取；随机DFN可能违反力学与构造约束；地质力学DFN对输入参数高度敏感 [Lei 2017, pp. 6-8]。
- 综述聚焦于HM行为，并非详尽；仅引用有限文献，更全面的细节需参考其他综述 [Lei 2017, pp. 2-3]。
- 未从索引片段中确认对连续-非连续混合模型局限的具体讨论。
- 未从索引片段中确认对流体-力学耦合计算效率或验证数据不足的明确陈述。

## Assumptions / Conditions
- 随机DFN模型中，裂缝通常被简化为二维直线或三维平面圆盘/多边形，几何属性按特定概率分布独立抽样 [Lei 2017, pp. 3-4]。
- Poisson DFN假设裂缝位置相互独立、均匀分布，除非通过聚类过程或密度场进行修正 [Lei 2017, pp. 4-4]。
- 分形裂缝模型假设裂缝群体具有自相似标度性和长程相关性 [Lei 2017, pp. 4-4]。
- 地质力学DFN模型通常基于线弹性断裂力学，假设各向同性弹性介质，并采用幂律或亚临界生长关系 [Lei 2017, pp. 6-6]。
- 生成DFN时常需定义裂缝终止准则与层次关系，如大裂缝抑制小裂缝的扩展 [Lei 2017, pp. 4-6]。

## Key Variables / Parameters
- 裂缝密度/强度：P₃₀（单位体积裂缝数）、P₂₀（单位面积裂缝迹线数）、P₁₀（单位长度裂缝数） [Lei 2017, pp. 3-4]
- 裂缝尺寸分布：负指数、对数正态、伽马或幂律分布 [Lei 2017, pp. 3-4]
- 分形维数 \( D \) 与幂律指数 \( a \) [Lei 2017, pp. 4-4]
- 应力强度因子 \( K_I \)、材料韧性 \( K_{IC} \)、应力腐蚀极限 \( K_O \) [Lei 2017, pp. 6-6]
- 亚临界裂缝生长速度指数 \( j \)（或亚临界指数 \( n \)） [Lei 2017, pp. 6-6]
- 裂缝形状、方向（如Fisher分布）、开度、剪切位移 [Lei 2017, pp. 3-4, 6-6]
- 能量释放率 \( G \) [Lei 2017, pp. 6-6]

## Reusable Claims
- 随机DFN模型因其简单性和三维适用性而被广泛采用，但其概率性质可能引入与力学过程不一致的裂缝拓扑，在模拟强耦合水力-力学过程时需谨慎 [Lei 2017, pp. 4-4, 6-8]。
- 分形DFN模型通过分形维数D和幂律分布来统一裂缝密度与尺寸的标度行为，适用于从微观到宏观的多尺度裂缝系统，但前提是系统满足自相似假设 [Lei 2017, pp. 4-4]。
- 地质力学DFN模拟中，采用亚临界生长准则（\( K_O \leq K_I \leq K_{IC} \)）可再现低应力条件下的时相关裂缝扩展，但需要可靠的亚临界指数等岩石力学参数作为输入 [Lei 2017, pp. 6-6]。这一声明受限于所假设的线弹性断裂力学框架。
- 改进的随机DFN考虑裂缝空间聚类（如基于地统计学的密度场）和力学交互作用（如应力阴影模型），可以在一定程度上弥补Poisson模型忽视地质力学约束的不足 [Lei 2017, pp. 4-4]。然而，未见定量验证其与真实裂缝网络在耦合HM行为上的对比。
- 开发融合地质测绘、随机统计和地质力学的混合DFN模型是提高裂缝网络真实性的可行方向 [Lei 2017, pp. 6-8]。此声明基于作者对各类方法优缺点的总结，未具体说明混合框架的实现路径。

## Candidate Concepts
- [[discrete fracture network (DFN)]]
- [[fracture network geometry]]
- [[hydromechanical coupling]]
- [[geomechanical modelling]]
- [[fracture propagation]]
- [[fractal fracture network]]
- [[stochastic fracture modelling]]
- [[geologically-mapped fracture network]]
- [[subcritical crack growth]]
- [[stress shadow]]

## Candidate Methods
- [[Poisson DFN generation]]
- [[fractal DFN model]]
- [[sequential DFN growth model]]
- [[linear elastic fracture mechanics (LEFM)]]
- [[boundary element method (BEM)]]
- [[finite element method (FEM)]]
- [[random walk fracture extrapolation]]
- [[invasion percolation]]
- [[Monte Carlo simulation]]

## Connections To Other Work
- 本文指出，关于裂缝网络更广泛的综述可参见Dershowitz and Einstein (1988)、Liu et al. (1999)以及教材Adler and Thovert (1999)等 [Lei 2017, pp. 2-3]。
- 岩石力学数值方法方面参考了Jing and Hudson (2002)、Jing (2003)、Yuan and Harrison (2006)、Bobet et al. (2009)、Lisjak and Grasselli (2014)的综述 [Lei 2017, pp. 2-3]。
- 关于应力对裂缝水流影响的深入讨论可参考Zhang and Sanderson (2002)与Rutqvist and Stephansson (2003) [Lei 2017, pp. 2-3]。
- 以上连接仅为本文引用的综述入口，具体的概念对比或方法继承关系未从片段中确认。

## Open Questions
- 如何有效耦合构造、水文、热和化学过程以生成与真实系统一致的裂缝模式？ [Lei 2017, pp. 6-8]
- 现有改进的随机DFN（如考虑空间聚类、力学交互）在复杂HM耦合问题中的适用性及定量验证尚不明确 [Lei 2017, pp. 4-4, 6-8]。
- 如何利用有限的一维/二维露头或钻井数据可靠地推求三维裂缝网络结构？ [Lei 2017, pp. 3-4]
- 地质力学DFN的输入参数（如亚临界指数、古应力场）通常具有高度不确定性，如何约束？ [Lei 2017, pp. 6-8]

## Source Coverage
本Wiki页面基于35个索引片段中的部分片段编写（主要包括摘要、引言、DFN表示方法的2-6页片段），覆盖了论文前半部分的综述框架、各类DFN模型描述及总结性表格。论文后半部关于连续/非连续地质力学模型的具体细节、HM耦合数值研究案例以及最终建议的深入讨论，可能因片段不足而缺失。重要信息如具体的算例对比、量化结论及表格1的详细内容未在片段中呈现，因此本页在方法比较和定量证据方面存在覆盖缺口。
