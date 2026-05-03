---
type: "paper"
paper_id: "2023-jalali-high-resolution-characterization-of-excavation-induced-fracture-network-using-contin"
title: "High-Resolution Characterization of Excavation-Induced Fracture Network Using Continuous and Discrete Inversion Schemes."
status: "draft"
source_pdf: "data/papers/2023 - High-Resolution Characterization of Excavation-Induced Fracture Network Using Continuous and Discrete Inversion Schemes.pdf"
citation: "Jalali, Mohammadreza, et al. “High-Resolution Characterization of Excavation-Induced Fracture Network Using Continuous and Discrete Inversion Schemes.” 2023."
indexed_texts: "18"
indexed_chars: "85343"
compiled_at: "2026-04-27T19:46:55"
---

# High-Resolution Characterization of Excavation-Induced Fracture Network Using Continuous and Discrete Inversion Schemes.

## One-line Summary

该论文结合等效多孔介质走时反演（连续）与贝叶斯离散裂缝网络反演（离散）两种方法，高分辨率重建了黏土岩中开挖诱导裂缝网络的渗透率分布与几何结构。

## Research Question

如何利用压气干扰试验数据，通过连续（等效多孔介质）和离散（DFN）反演方案，高分辨率地表征开挖诱导裂缝网络的几何形态、连通性及水力特性，从而评估其对放射性废物处置库长期安全性的影响？[Jalali 2023, pp. 1-1]

## Study Area / Data

- **研究区**：法国ANDRA Meuse/Haute-Marne地下研究实验室（URL）主层的GER gallery。该巷道平行于最小水平主应力方向。[Jalali 2023, pp. 2-4]
- **数据**：在巷道底板钻取的9口密集钻孔（OHZ 6151–6159）中开展了跨孔压气干扰试验。每个钻孔设两个测试段：位置(a) 深度1.2–2.46 m（近巷道底板），位置(b) 深度3.0–4.26 m（较深处）。共记录306组压力干扰，经筛选后151组用于走时反演，7–12组用于DFN反演（取决于重建剖面）。[Jalali 2023, pp. 4-6]

## Methods

1. **走时反演（连续方法）**：
   - 基于等效多孔介质假设，利用跨孔压气响应走时重建三维扩散率层析图。
   - 模型域：x、y方向各6个网格，z方向4个网格（共144个粗网格），通过交错网格方法（Vesnaver & Böhm, 2000）加密至31,104个细胞（36×36×24）。[Jalali 2023, pp. 6-7]
   - 数据处理：对实测压力数据先后进行小波去噪、多项式拟合、求一阶导数，以获取可用于走时反演的峰值时间。[Jalali 2023, pp. 7-9]

2. **DFN反演（离散方法）**：
   - 采用贝叶斯MCMC框架，以非信息先验假设，通过Metropolis-Hastings-Green接受准则拟合DFN模型到压力干扰观测数据。[Jalali 2023, pp. 9-10]
   - 每次迭代随机选择三种几何更新之一：添加裂缝、删除裂缝、移动裂缝。更新后模拟试验并计算似然比（RMS误差），与提议比乘积构成接受概率。[Jalali 2023, pp. 9-10]

## Key Findings

- 走时反演结果表明，该方法能够以高空间分辨率（x、y方向0.26 m，z方向0.57 m）重建三维扩散率分布，并用于约束DFN反演与解释。[Jalali 2023, pp. 7-9]
- DFN反演结果支持了ARNAND等人（2014）的概念模型：巷道底板近区（约1.2 m内）以连通的张裂缝为主，深部（至3.7 m）以离散的剪切裂缝为主；裂缝性质和频率随深度变化。[Jalali 2023, pp. 4-5, 7-9]
- 走时反演的轨迹密度分析显示，整个模型域内没有细胞被少于4条轨迹穿过，因此不存在显著的区域意义受限问题。[Jalali 2023, pp. 7-9]

## Limitations

- 未从索引片段中确认明确的局限性讨论。但可推断：数据筛选过程（剔除非互易干扰等）可能引入选择偏差。[Jalali 2023, pp. 5-6]
- 钻孔损坏带（BDZ）的影响被部分处理，但仅适用于沿钻孔测量的干扰，对于跨孔干扰的处理方式未完全说明。[Jalali 2023, pp. 5-6]
- 走时反演仅适用于近似脉冲源，实测数据需经过严格的时间导数处理，这可能引入误差。[Jalali 2023, pp. 6-7]
- DFN反演仅基于二维剖面，未扩展至完整三维DFN。[Jalali 2023, pp. 9-10]

## Reusable Claims

- “Pneumatic cross-hole tests are preferred for partially saturated induced fractures after excavation” [Jalali 2023, pp. 1-1]。
- “Travel time-based inversion can reconstruct changes in hydraulic properties in three dimensions with high spatial resolution, and the results can constrain DFN inversion” [Jalali 2023, pp. 7-9]。
- “For pressure interferences propagating between zone (a) and (b), the interference from (a) to (b) was chosen due to higher signal-to-noise ratio” [Jalali 2023, pp. 5-6]。
- “Bayesian MCMC with non-informative priors simplifies acceptance criteria to product of likelihood ratio and proposal ratio (Jacobian = 1)” [Jalali 2023, pp. 9-10]。

## Candidate Concepts

- [[excavation-induced fracture network]]
- [[clay host rock]]
- [[radioactive waste repository]]
- [[pneumatic tomography]]
- [[equivalent porous medium]]
- [[discrete fracture network (DFN)]]
- [[borehole damaged zone (BDZ)]]
- [[conceptual model of induced fractures (Armand et al. 2014)]]

## Candidate Methods

- [[travel time-based inversion]]
- [[Bayesian MCMC inversion]]
- [[staggered grid method]]
- [[wavelet denoising]]
- [[MULTISIM borehole simulator]]
- [[Metropolis-Hastings-Green acceptance criteria]]
- [[cross-hole pneumatic interference test]]

## Open Questions

- 未从索引片段中确认开放问题。

## Source Coverage

- 索引片段页数：1–1, 1–2, 2–4, 4–5, 5–6, 6–7, 7–9, 9–10。
- 注：论文共18页（摘要页2/18至18/18），此处覆盖了前10页的主要方法、数据及部分结果；后续页未提供，故后8页的结论与讨论未纳入。
