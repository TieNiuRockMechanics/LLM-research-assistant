---
type: "paper"
paper_id: "2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers"
title: "FracGen: Natural Fracture Networks Reconstruction and Upscaling Using Generative Adversarial Networks."
status: "draft"
source_pdf: "data/papers/2025 - FracGen Natural fracture networks reconstruction and upscaling using generative adversarial networks.pdf"
citation: "Zhou, Changtai, et al. \"FracGen: Natural Fracture Networks Reconstruction and Upscaling Using Generative Adversarial Networks.\" *International Journal of Rock Mechanics and Mining Sciences*, 2025, doi:10.1016/j.ijrmms.2025.106116."
indexed_texts: "16"
indexed_chars: "77664"
compiled_at: "2026-04-27T19:48:00"
---

# FracGen: Natural Fracture Networks Reconstruction and Upscaling Using Generative Adversarial Networks.

## One-line Summary

FracGen 是一个基于 SinGAN 的非参数机器学习模型，用于重构和升尺度天然裂缝网络，无需显式参数化即可复制裂缝的关键统计属性 [Zhou 2025, pp. 1-1]。

## Research Question

如何准确建模复杂天然裂缝网络的几何形态，并实现从露头图像到更大尺度的可靠升尺度，从而避免传统方法在几何复杂性和尺度转换上的困难？[Zhou 2025, pp. 1-1]

## Study Area / Data

使用三个不同地点的天然裂缝网络露头图像作为训练数据：(1) 英国布里斯托尔海峡盆地南缘 Kilve 的干旱大陆岩石露头；(2) 苏格兰 Dounreay 地区的砂岩露头；(3) 西萨默塞特布里斯托尔海峡南岸的石灰岩露头。三个训练样本尺寸均为 2 m × 2 m，对应分辨率分别为 236×236、335×335 和 116×116 [Zhou 2025, pp. 3-5]。这些图像经过数字化预处理（灰度化、阈值调整、二值化、骨架化）后用于训练 [Zhou 2025, pp. 3-3]。

## Methods

FracGen 模型包含三个步骤：

1. **裂缝网络数字化**：将露头图像转换为灰度图，调整阈值区分裂缝与背景，二值化并骨架化得到数字化裂缝网络 [Zhou 2025, pp. 3-3]。
2. **SinGAN 训练**：采用 SinGAN 的金字塔架构，在多个尺度上训练生成器 Gₙ 和判别器 Dₙ。训练过程包括初始化、多尺度训练和损失函数优化（对抗损失与重构损失，权重因子 α），使用固定尺度因子 r 逐步下采样图像 [Zhou 2025, pp. 3-5]。
3. **裂缝网络重构与升尺度**：用训练好的生成器，输入随机噪声图 z，生成原始尺度的裂缝网络。对于升尺度，创建更大尺度的噪声图，并依次通过各尺度生成器，产生保留小尺度特征的大尺度裂缝网络 [Zhou 2025, pp. 3-3]。

评价方法包括定性比较、裂缝强度（P₂₁，通过圆形扫描线计算）、裂缝方向玫瑰图、裂缝长度分布（用修改的对数正态分布拟合）以及余弦相似度分析 [Zhou 2025, pp. 7-10]。

## Key Findings

- FracGen 生成的裂缝网络在视觉上成功捕获了露头裂缝的整体方向、拓扑结构和复杂度 [Zhou 2025, pp. 5-7]。
- 裂缝强度（P₂₁）值与真实网络高度一致：干旱大陆岩石、砂岩、石灰岩的生成网络分别为 10.16±0.50 m⁻¹、8.97±0.32 m⁻¹、8.82±0.38 m⁻¹，对应真实值为 10.07 m⁻¹、8.88 m⁻¹、8.86 m⁻¹ [Zhou 2025, pp. 7-8]。
- 裂缝方向玫瑰图显示生成网络与真实网络具有相似的节理组分布和区间 [Zhou 2025, pp. 8-10]。
- 裂缝长度分布符合修改的对数正态分布，其参数（xₑ、w）在生成和真实网络之间非常接近 [Zhou 2025, pp. 8-10]。
- 余弦相似度分析进一步定量证实了生成网络在方向和长度分布上与真实网络的高度相似性 [Zhou 2025, pp. 10-11]。

## Limitations

未从索引片段中确认模型自身的局限性。片段中指出裂缝长度分布受分辨率和采样限制存在有限上下截断，导致偏向对数正态形式 [Zhou 2025, pp. 8-10]，但这是数据本身的特点，未说明模型如何克服或自身局限。

## Reusable Claims

- SinGAN 可以用于天然裂缝网络的多尺度无参数建模，无需显式参数化即可复制关键统计属性 [Zhou 2025, pp. 1-1]。
- 通过余弦相似度测量和概率分布拟合可以定量验证生成裂缝网络的准确性 [Zhou 2025, pp. 1-1]。
- 利用金字塔架构的多尺度生成器可以实现裂缝网络的升尺度，保留原始统计特征 [Zhou 2025, pp. 3-3]。
- 裂缝网络数字化过程包括灰度化、阈值调整、二值化和骨架化 [Zhou 2025, pp. 3-3]。
- 裂缝强度 P₂₁（圆形扫描线法）可有效对比生成与真实裂缝网络的密度分布 [Zhou 2025, pp. 7-8]。
- 修改的对数正态分布能够较好拟合受截断效应影响的裂缝长度分布 [Zhou 2025, pp. 8-10]。

## Candidate Concepts

- [[天然裂缝网络]]
- [[生成对抗网络]]
- [[SinGAN]]
- [[升尺度]]
- [[非参数建模]]
- [[裂缝强度]]
- [[裂缝方向]]
- [[裂缝长度]]
- [[对数正态分布]]
- [[余弦相似度]]
- [[骨架化]]
- [[金字塔架构]]

## Candidate Methods

- [[FracGen]]
- [[SinGAN]]
- [[多尺度GAN]]
- [[裂缝网络数字化]]
- [[圆形扫描线法]]
- [[修改的对数正态分布拟合]]

## Open Questions

未从索引片段中确认。例如：FracGen 能否直接适用于三维裂缝网络建模？模型对不同尺度因子的敏感性如何？训练数据量（仅单幅图像）对泛化能力的影响？这些在索引片段中没有讨论。

## Source Coverage

基于以下索引片段撰写：Zhou 2025, pp. 1-1, pp. 1-3, pp. 3-3, pp. 3-5, pp. 5-7, pp. 7-8, pp. 8-10, pp. 10-11。
