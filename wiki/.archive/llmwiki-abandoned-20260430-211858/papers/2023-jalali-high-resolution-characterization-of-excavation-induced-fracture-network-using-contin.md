---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-jalali-high-resolution-characterization-of-excavation-induced-fracture-network-using-contin"
title: "High-Resolution Characterization of Excavation-Induced Fracture Network Using Continuous and Discrete Inversion Schemes."
status: "draft"
source_pdf: "data/papers/2023 - High-Resolution Characterization of Excavation-Induced Fracture Network Using Continuous and Discrete Inversion Schemes.pdf"
collections:
citation: "Jalali, Mohammadreza, et al. “High-Resolution Characterization of Excavation-Induced Fracture Network Using Continuous and Discrete Inversion Schemes.” *Water Resources Research*, vol. 59, no. 5, 2023."
indexed_texts: "18"
indexed_chars: "85343"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T12:43:06"
---

# High-Resolution Characterization of Excavation-Induced Fracture Network Using Continuous and Discrete Inversion Schemes.

## One-line Summary
利用等效连续介质（旅行时层析成像）和离散裂隙网络（贝叶斯反演）两种方案，高分辨率重建开挖诱导裂隙网络，以评估其水力特性与几何结构 [Jalali 2023, pp. 1-2].

## Research Question
如何通过连续与离散反演方法高分辨率表征开挖诱导裂隙网络的几何形态、连通性及水力特性，从而为放射性废物处置库长期安全评估提供依据？[Jalali 2023, pp. 1-1]

## Study Area / Data
研究区为法国Meuse/Haute-Marne地下研究实验室（URL）主层GER廊道。该廊道平行于最小水平主应力方向。数据来源于隧道底板上9个密集间距钻孔（OHZ 6151–6159）中采集的气动跨孔干扰测试数据集。每个钻孔在a区（靠近隧道底板，约1.31–2.46 m深度，主要发育扩展裂隙）和b区（约3.00–4.26 m深度，主要发育剪切裂隙）分别设置封隔器测试段。最终筛选151组干扰数据用于旅行时反演，7–12组干扰数据用于二维DFN反演 [Jalali 2023, pp. 2-6].

## Methods
- **连续反演（等效连续介质模型）：** 采用基于旅行时的三维反演方法。基于扩散度方程（假设狄拉克脉冲源），通过对瞬态压力数据的小波去噪、多项式拟合和数值微分处理，计算峰值时间并利用SIRT（同时迭代重构技术）反演获得三维扩散率层析图。利用交错网格法将模型域（1.56 m × 1.56 m × 2.28 m）离散化为31104个单元，获得高分辨率图像 [Jalali 2023, pp. 5-7].
- **离散反演（离散裂隙网络模型）：** 采用贝叶斯反演框架，结合DFN生成器与MCMC方法中的Metropolis-Hastings-Green准则拟合观测压力响应。更新过程中随机选择裂隙添加、删除或移位操作，并通过均方根误差评估模型改进。先验比由于使用无信息先验而取值为1，雅可比行列式在离散空间转换中取值为1，接受概率简化为似然比与提案比的乘积 [Jalali 2023, pp. 9-10].
- **DFN生成器：** 采用基于地质统计学的DFN生成器，根据裂隙频率、产状和尺寸等输入参数生成二维DFN模型。裂隙频率和方向由场地的概念模型以及钻孔a区和b区的单孔测试结果提供约束 [Jalali 2023, pp. 9].

## Key Findings
- **连续反演结果：** 三维扩散率层析图能够以高空间分辨率揭示研究域内水力特性的变化，为后续DFN反演提供约束 [Jalali 2023, pp. 8].
- **DFN反演结果：** DFN反演重建了优势裂隙的位置，提供了关于断裂连通性、水力特性及主导结构几何形态的信息。反演识别出决定流体流动和溶质迁移的主要裂隙连接模式 [Jalali 2023, pp. 1-2].
- **水力特性差异：** a区（扩展裂隙带）的气导率显著高于b区（剪切裂隙带）。例如，OHZ 6152孔a区气体传导率为 9.7 × 10⁻⁶ m/s，而b区仅为 1.9 × 10⁻⁸ m/s [Jalali 2023, pp. 4-5].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| a区（扩展裂隙带）气导率在 4.4 × 10⁻⁷ 至 1.5 × 10⁻⁵ m/s 之间，b区（剪切裂隙带）在 6.8 × 10⁻¹⁰ 至 4.7 × 10⁻⁸ m/s 之间 | Table 1, [Jalali 2023, pp. 4-5] | GER廊道底部九个钻孔，a区深度1.20–2.46 m，b区深度3.00–4.26 m | 扩展裂隙带渗透性比剪切带高约2–5个数量级 |
| 三维扩散率层析图重构了研究域内高分辨率水力特性变化 | [Jalali 2023, pp. 8] | 模型域1.56 m × 1.56 m × 2.28 m，网格31104单元 | 利用交错网格法提高名义分辨率 |
| 概念模型区分两类开挖诱导结构：扩展裂隙（a区，深度约1.2 m）和剪切裂隙（b区，深度约3.7 m） | [Jalali 2023, pp. 2] | 廊道平行于最小水平主应力方向，基于Armand et al. (2014) | 扩展裂隙延伸范围在底板和顶板大于侧壁 |

## Limitations
- 连续反演无法直接表征离散结构及其连通性 [Jalali 2023, pp. 1-2].
- DFN反演仅使用二维模型对特定剖面进行重建，未从索引片段确认三维全空间DFN应用情况 [Jalali 2023, pp. 6].
- 气动测试假设裂隙系统部分饱和（充满空气），不直接适用于完全饱和条件 [Jalali 2023, pp. 1-1].

## Assumptions / Conditions
- 开挖诱导裂隙部分填充空气（即部分饱和），因此气动跨孔测试优于水力测试 [Jalali 2023, pp. 1-1].
- 旅行时反演假设脉冲源（狄拉克源）条件，通过压力数据微分化处理可扩展至恒定速率短时测试 [Jalali 2023, pp. 6].
- DFN反演的贝叶斯框架使用无信息先验（先验比=1），且假定观测误差服从正态分布 [Jalali 2023, pp. 9-10].
- 廊道周围不存在构造裂隙，所有岩心中观察到的裂隙均为开挖诱导裂隙 [Jalali 2023, pp. 2].
- 介质为低渗透黏土岩，具有低水力传导性、高吸附能力和自封闭潜力 [Jalali 2023, pp. 1-1].

## Key Variables / Parameters
- **气体传导率 (Gas conductivity)：** 衡量单孔气体流动能力，单位 m/s。a区 4.4 × 10⁻⁷–1.5 × 10⁻⁵ m/s；b区 6.8 × 10⁻¹⁰–4.7 × 10⁻⁸ m/s [Jalali 2023, pp. 4-5].
- **扩散率 (Diffusivity)：** 三维旅行时反演的目标参数，用于描述压力脉冲传播特性 [Jalali 2023, pp. 6].
- **轨迹密度 (Trajectory density)：** 重建网格中每个单元被压力脉冲轨迹穿过的数量，用于评价反演结果的可靠性 [Jalali 2023, pp. 7].
- **RMS误差 (Root Mean Square error)：** 用于DFN反演中评估模拟值与观测值之间拟合程度的似然比依据 [Jalali 2023, pp. 10].
- **裂隙频率 (Fracture frequency)：** DFN生成器的输入参数，由单孔测试和概念模型约束 [Jalali 2023, pp. 9].

## Reusable Claims
- **Claim 1:** 在黏土岩开挖诱导裂隙网络中，靠近隧道底板的扩展裂隙带（深度≤1.2 m，约30%隧道直径）的气导率比深部剪切裂隙带（深度至3.7 m，约80%隧道直径）高2–5个数量级。证据来自GER廊道九个钻孔的气动单孔测试数据 [Jalali 2023, pp. 4-5]。使用条件：廊道平行于最小水平主应力方向；适用于黏土岩中隧道式开挖。
- **Claim 2:** 三维旅行时反演结合交错网格法能够在扰动域（<2 m尺度）内重建亚米级分辨率的扩散率分布，为后续DFN建模提供约束。证据来自GER廊道气动跨孔测试的151组干扰数据反演结果 [Jalali 2023, pp. 6-8]。限制：需高密度传感器阵列与高质量干扰数据支持。
- **Claim 3:** 基于MCMC和DFN生成器的贝叶斯反演框架可利用少量（7–12组）跨孔干扰数据反演出主导裂隙的几何与连通性。证据来自研究采用的DFN反演结果 [Jalali 2023, pp. 9-10]。条件：需连续反演结果提供先验约束。

## Candidate Concepts
- [[excavation-induced fracture network]]
- [[equivalent porous media (EPM)]]
- [[discrete fracture network (DFN)]]
- [[hydraulic tomography]]
- [[pneumatic interference test]]
- [[Bayesian inversion]]
- [[MCMC (Markov Chain Monte Carlo)]]
- [[diffusivity tomogram]]
- [[fracture connectivity]]
- [[underground research laboratory (URL)]]
- [[sirt-erosion-bonehed zone (bdz)]]

## Candidate Methods
- [[travel time-based inversion (SIRT)]]
- [[staggered grid method]]
- [[wavelet denoising]]
- [[DFN generator (geostatistical)]]
- [[Metropolis-Hastings-Green algorithm]]
- [[pneumatic cross-hole testing]]
- [[polynomial fitting for transient data]]

## Connections To Other Work
- 本研究在气动跨孔测试反演方面与前人在阿帕奇利普研究站（ALRS）非饱和裂隙凝灰岩中的工作相关（Vesselinov et al., 2001a, 2001b），该工作利用地质统计学方法重建了1 m尺度的空气渗透率和空气孔隙度分布 [Jalali 2023, pp. 1-2].
- 在裂隙网络概念模型方面，直接基于Armand et al. (2014)在Meuse/Haute-Marne URL提出的开挖诱导裂隙概念模型，该模型区分扩展裂隙区和剪切裂隙区 [Jalali 2023, pp. 2].
- 水力与气动层析成像的一般方法学可连接至[[Brauchler et al. (2013)]]、[[Illman et al. (2010)]]、[[Yeh & Liu (2000)]]的研究 [Jalali 2023, pp. 2].
- 在DFN反演方法学上，与前人[[Somogyvári et al. (2017)]]的DFN-MCMC框架相关 [Jalali 2023, pp. 9-10].

## Open Questions
- DFN反演结果在三维全空间中的适用性未从索引片段中确认。
- 开挖诱导裂隙随时间演化的THM（热-水-力）耦合行为尚未涉及。
- 本方法在其他岩性（非黏土岩）或不同应力场条件下的迁移性未知。

## Source Coverage
本页内容基于18个索引片段中的14个片段（主要来自论文引言、方法、关键图表与结果概述部分，pp. 1-1至10）。索引片段覆盖了研究背景、场地条件、两种反演方法的基本框架以及主要水力特性对比证据。未覆盖的内容可能包括：DFN反演结果的详细定量验证、敏感性分析、全模型域的评价指标、与独立数据（如地质雷达或ERT）的对比讨论、以及结论与工程实际应用建议。索引片段偏重于方法与初步结果展示，部分讨论与详细参数化过程未从片段中确认。
