---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2018-afshari-moein-fracture-network-characterization-using-stress-based-tomography"
title: "Fracture Network Characterization Using Stress-Based Tomography."
status: "draft"
source_pdf: "data/papers/2018 - Fracture Network Characterization Using Stress-Based Tomography.pdf"
collections:
citation: "Afshari Moein, Mohammad Javad, et al. \"Fracture Network Characterization Using Stress-Based Tomography.\" *Journal of Geophysical Research: Solid Earth*, 2018, p. 9324, doi:10.1029/2018JB016438. Accessed 2026."
indexed_texts: "18"
indexed_chars: "86036"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T21:54:22"
---

# Fracture Network Characterization Using Stress-Based Tomography.

## One-line Summary
该文引入应力层析成像方法，在贝叶斯框架下利用井筒应力观测校准离散裂隙网络，并以概率图形式表征深部裂隙网络的位置与长度 [Afshari 2018, pp. 1-1, 2-3]。

## Research Question
如何从有限的井筒应力数据中反演并成像深部地热储层中的裂隙网络形态？其工作假设是天然裂隙的滑移是造成井筒应力非均质性的主控因素 [Afshari 2018, pp. 1-1]。

## Study Area / Data
测试用例使用了两个合成裂隙网络：一个仅含四条正交互补大裂隙的简单合成网络（域 100×100 m²，最小间距 10 m，最小长度 40 m），另一个是由露头映射数据构建的更复杂网络 [Afshari 2018, pp. 8-9]。观测数据为沿垂直井筒的至少一个主应力分量的方向与大小的局部变化 [Afshari 2018, pp. 1-1]。为说明应力观测来源，作者展示了 Soultz-sous-Forêts 和 Basel 增强型地热系统 (EGS) 场地的井壁图像及应力剖面，但实际反演并未使用这些现场数据 [Afshari 2018, pp. 3-4]。

## Methods
提出应力层析成像反演流程，主要包括：
1. **先验与初始 DFN 生成**：基于对裂隙长度、方向和密度的先验统计信息，生成一个随机初始离散裂隙网络 (DFN) 实现 [Afshari 2018, pp. 2-3]。
2. **前向应力模拟**：设定为 2D 平面应变问题，利用位移不连续方法 (DDM) 模拟含裂隙岩体在远场应力作用下的力学响应。裂隙力学行为采用 Barton-Bandis 模型，峰值剪切由 Mohr-Coulomb 准则判定，超过峰值后剪切刚度设为零，并引入恒定的剪胀角 [Afshari 2018, pp. 4-6]。模拟得到沿中心井筒的应力扰动剖面。
3. **贝叶斯 MCMC 反演**：在马尔可夫链蒙特卡洛 (MCMC) 框架下，通过移动域内裂隙位置的方式迭代更新 DFN。每一步将新的模拟应力剖面与“观测”应力剖面进行对比，使用 Metropolis-Hastings 接受准则决定是否接受该更新。似然函数假设应力观测（方向、大小）服从独立正态分布，其方差可调节不同观测量的敏感度 [Afshari 2018, pp. 7-8]。反演过程中保持裂隙数量固定 [Afshari 2018, pp. 6-7]。
4. **后验概率图**：保存所有被接受的 DFN 实现构成后验集合。舍弃前半链以消除初始猜测偏差后，通过统计所有实现中裂隙的出现频率，生成裂隙发生概率图，以可视化可能的裂隙位置和长度 [Afshari 2018, pp. 8-9, 1-1]。
该方法至少需要一个应力大小和一个应力方向的观测数据；仅单一应力方向不足以重建简单网络 [Afshari 2018, pp. 6-7]。

## Key Findings
- 应力层析成像成功重建了简单合成裂隙网络，并用概率图指示了裂隙位置和长度的不确定性 [Afshari 2018, pp. 1-1, 8-9]。
- 仅靠单一应力方向（如 Shmax 方向）反演简单 DFN 是不充分的，必须同时使用至少一个应力方向和一个应力大小观测 [Afshari 2018, pp. 6-7]。
- MCMC 后验集合提供了多个等可能实现，可表达反演结果的不确定性，而非给出单一确定性网络 [Afshari 2018, pp. 8-9]。
- 前向模拟证实，裂隙滑移可在井筒附近产生可检测的应力方向和大小扰动，作为反演的基础信号 [Afshari 2018, pp. 4-6]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 提出的应力层析成像方法能够通过贝叶斯 MCMC 反演井筒应力剖面来生成裂隙概率图 | [Afshari 2018, pp. 1-1, 8-9] | 2D 平面应变，至少一个应力方向和一个应力大小可用，裂隙滑移为主导，前向模型基于 DDM 和 Barton-Bandis | 测试限于合成网络和露头映射网络 |
| 仅使用应力方向进行反演不足以重建简单合成 DFN | [Afshari 2018, pp. 6-7] | 简单四裂隙正交网络 | 在支持信息中展示 |
| 前向模拟采用 DDM 和 Mohr‑Coulomb / Barton‑Bandis 裂隙本构，可计算由裂隙滑移引起的应力扰动 | [Afshari 2018, pp. 4-6] | 假设剪切峰值后零刚度、恒定剪胀角，2D 模型 | 模拟效率较高，适于迭代 |
| MCMC 中使用 Metropolis‑Hastings 接受准则，接受概率为似然比与先验比的乘积 | [Afshari 2018, pp. 7-8] | 采用随机游走提议，假设正向与反向提议概率相等 | 似然基于正态分布 |

## Limitations
- 方法仅在 2D 平面应变假设下建立并测试，未涉及三维真实构造 [Afshari 2018, pp. 4-6]。
- 测试案例为合成和露头映射网络，尚未在深部 EGS 现场数据上验证其有效性和鲁棒性 [Afshari 2018, pp. 8-9]。
- 反演中裂隙数量恒定，不能新增或删除裂隙，限制了捕捉复杂网络拓扑变化的能力 [Afshari 2018, pp. 6-7]。
- 似然函数中观测方差需预先设定，对反演收敛有影响，但其选取策略未在片段中详述 [Afshari 2018, pp. 7-8]。
- 实际 EGS 中沿井筒获取完整应力张量非常困难，而该方法所需的多类型应力观测可能并不总能满足 [Afshari 2018, pp. 7-8]。

## Assumptions / Conditions
- 井筒应力非均质完全由天然裂隙的滑移控制 [Afshari 2018, pp. 1-1]。
- 问题简化为垂直井筒剖面的 2D 平面应变条件 [Afshari 2018, pp. 4-6]。
- 裂隙力学行为遵循 Barton-Bandis 模型，峰值剪切采用 Mohr-Coulomb 准则，超过峰值后剪切刚度降为零，剪胀角恒定 [Afshari 2018, pp. 4-6]。
- 远场应力均匀且已知，可从应力观测中近似推断 [Afshari 2018, pp. 4-6]。
- 应力方向和大小的观测误差服从正态分布 [Afshari 2018, pp. 7-8]。
- 先验信息能够提供裂隙长度、方向和密度的可靠统计分布 [Afshari 2018, pp. 2-3]。
- 反演过程中裂隙仅可通过平移改变位置，其长度与总数固定 [Afshari 2018, pp. 6-7, 8-9]。

## Key Variables / Parameters
- 观测应力分量：至少一个应力方向（如最小水平主应力方位）和一个应力大小（如 Shmin 或 Shmax） [Afshari 2018, pp. 6-7]。
- 远场应力大小和方向 [Afshari 2018, pp. 4-6]。
- DFN 几何参数：裂隙的位置、方向、长度；裂隙间距、总长度 [Afshari 2018, pp. 8-9]。
- 裂隙力学参数：Barton-Bandis 模型中的剪切刚度、剪胀角，Mohr-Coulomb 准则中的摩擦系数或内聚力（未完全详述） [Afshari 2018, pp. 4-6]。
- MCMC 控制参数：观测方差 σ²，链长度，舍弃比例（前一半） [Afshari 2018, pp. 7-8]。
- 位移不连续量（DD 分量），影响应力重新分布 [Afshari 2018, pp. 4-6]。

## Reusable Claims
- 在 2D 平面应变和裂隙滑移主控应力异质的前提下，结合井筒应力方向与大小的观测，通过 MCMC 反演可生成裂隙发生概率图，指示周边裂隙的位置和长度，但不能唯一确定网络几何 [Afshari 2018, pp. 1-1, 6-7, 8-9]。
- 基于 DDM 和 Barton-Bandis/Mohr-Coulomb 组合模型的准静态前向模拟器，可有效计算井筒周围的应力扰动，适用于批量迭代反演 [Afshari 2018, pp. 4-6]。
- 在贝叶斯框架下集成 Metropolis-Hastings 随机游走算法，可通过比较正演响应与多类型应力观测来校准 DFN 实现 [Afshari 2018, pp. 7-8]。
- 单一应力方向观测无法唯一重建简单裂隙网络，说明了多分量应力数据在反演中的必要性 [Afshari 2018, pp. 6-7]。

## Candidate Concepts
- [[Enhanced Geothermal System]]
- [[Fracture Network]]
- [[Discrete Fracture Network (DFN)]]
- [[Stress-Based Tomography]]
- [[Bayesian Inversion]]
- [[Markov Chain Monte Carlo]]
- [[Metropolis-Hastings Algorithm]]
- [[Barton-Bandis Model]]
- [[Displacement Discontinuity Method]]
- [[In Situ Stress]]
- [[Borehole Breakouts]]
- [[Stress Heterogeneity]]
- [[Slip on Fractures]]
- [[DFN Calibration]]
- [[Probability Map]]
- [[Posterior Ensemble]]

## Candidate Methods
- [[Stress-Based Tomography]]
- [[Bayesian MCMC Inversion]]
- [[Displacement Discontinuity Method (DDM)]]
- [[Barton-Bandis Fracture Mechanics]]
- [[Mohr-Coulomb Failure Criterion]]
- [[Random-walk Metropolis-Hastings]]
- [[DFN Forward Stress Simulation]]
- [[Forward Geomechanical Modeling]]

## Connections To Other Work
本工作直接建立在 Somogyvári 等人（2017）的跨井示踪层析成像 DFN 反演方法之上，核心区别在于此处保持裂隙数量固定（而非可变数量）并使用应力观测替代示踪剂突破曲线 [Afshari 2018, pp. 6-7]。贝叶斯 MCMC 反演在相邻领域的应用构成方法基础，包括地震层析成像（Bodin et al., 2012）、示踪剂层析成像（Jiménez et al., 2016）以及裂隙-井筒相交推断（Mardia et al., 2007）[Afshari 2018, pp. 6-7]。此外，应力场贝叶斯反演（Lecampion & Lei, 2010）和非均质介质流-传输表征（Lee & Kitanidis, 2013; Mondal et al., 2010）也为本研究提供了统计框架的参考 [Afshari 2018, pp. 6-7]。整体研究主题还与野外应力表征（Zoback, 2010; Stephansson & Zang, 2012）以及 EGS 诱发地震机理（Amann et al., 2017）相关联，可在[[Hydraulic Fracturing]]、[[Induced Seismicity]]等话题下形成连接。

## Open Questions
- 方法在真实深部 EGS 多井/斜井系统中的适用性，以及如何集成其他观测（如微震、水力数据）以增强反演约束，未从索引片段中确认。
- 3D 扩展中裂隙相交、连通性演化的反演能力，以及可变裂隙数目的处理方案，尚未在片段中讨论。
- 反演对先验统计偏差的敏感性，以及计算成本在实际大规模 DFN 上的可接受性，未从索引片段中确认。

## Source Coverage
本页依据 18 个索引片段撰写，覆盖了论文的摘要、引言、方法框架、前向模拟技术、贝叶斯反演细节以及测试用例描述。片段提供了核心方法和主要验证结论，但对结果的定量评估（如概率图与真实网络的重合度指标）、讨论部分中的局限性深入分析以及现场数据应用展望等具体内容，可能缺失。近半片段集中在 1-7 页的方法说明，后文详细结果和敏感性分析的信息不完整。
