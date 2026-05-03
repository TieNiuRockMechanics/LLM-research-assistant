---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai"
title: "Constructing Large-Scale High-Fidelity Fracture Networks Based on Generative AI."
status: "draft"
source_pdf: "data/papers/2026 - Constructing large-scale high-fidelity fracture networks based on generative AI基于生成式人工智能构建大规模高保真断裂网络.pdf"
collections:
  - "神经网络结合分形网络研究"
citation: "Nie, Mengmeng, et al. \"Constructing Large-Scale High-Fidelity Fracture Networks Based on Generative AI.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 200, 2026, 106426. doi:10.1016/j.ijrmms.2026.106426."
indexed_texts: "14"
indexed_chars: "67330"
nonempty_source_blocks: "14"
compiled_source_blocks: "14"
compiled_source_chars: "63832"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.948047"
coverage_status: "full-index"
source_signature: "406517599604d0bd512975d8f0b1429d0c233a23"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T08:29:19"
---

# Constructing Large-Scale High-Fidelity Fracture Networks Based on Generative AI.

## One-line Summary

提出Upscaling-GAN算法：直接从野外小尺度裂缝图像学习，通过GAN训练+patch-by-patch拼接两阶段生成，构建任意尺寸的高保真裂缝网络，同时保持裂缝开度空间变异性且GPU内存消耗近乎恒定。

## Research Question

如何从小尺度野外裂缝网络图像生成满足工程尺度分析的大尺度高保真裂缝网络？需克服传统随机/分形DFN方法无法真实再现裂缝几何、开度变化，以及现有GAN类方法依赖二值化/骨架化预处理导致信息丢失和GPU内存受限等问题。

## Study Area / Data

- 训练数据：来自Karimpouli等（2020）的一幅500×500像素的小尺度裂缝网络图像（原文Fig.6），假设物理尺寸为5 m × 5 m［Nie 2026, pp. 5-6］。
- 无其他野外研究区信息；模型验证均在二维图像上进行。

## Methods

- **总体框架**：Upscaling-GAN属于AI-Geo平台中的AIG-Upscaling模块，通过两阶段构建大尺度图像［Nie 2026, pp. 2-3］。
- **阶段1（GAN训练）**：基于单张训练图，训练GAN以学习裂缝特征。
  - 生成器（Fig.3）：输入空间噪声和局部填充（local padding），生成3 × 3个128 × 128的patch，再拼接为384 × 384图像；包含卷积+局部填充（Conv-lp）、批归一化、LeakyReLU、自注意力机制、上采样和多个ResBlock；丢弃了随机空间图以加速训练［Nie 2026, pp. 2-4］。
  - 判别器（Fig.4）：采用双PatchGAN架构（Hybrid‑D），两个分支结构相同，但一卷积层使用标准卷积，另一使用空洞卷积扩大感受野［Nie 2026, pp. 3-5］。
  - 损失函数：判别器采用hinge损失+梯度惩罚（梯度惩罚权重λ = 10），生成器采用非饱和hinge损失（式1‑3）［Nie 2026, pp. 4-5］。
- **阶段2（大尺度生成）**：将训练好的GAN应用于patch‑by‑patch生成范式（Fig.5）。依次生成单个小图，利用已生成的相邻patch的像素进行局部填充，消除拼接边界不一致性；最后丢弃最右侧/最下方用于填充的过渡patch，按需拼接至任意尺寸，GPU内存主要受patch尺寸限制而与目标图像尺寸无关［Nie 2026, pp. 5-6］。
- **定量验证**：对生成图像先使用基于复剪切波变换的自动化裂缝迹线检测（Prabhakaran等，2019）提取矢量裂缝几何，再用FracPaQ工具箱统计裂缝方向、强度（圆形扫描线法，Mauldon等，2001）、长度（MLE拟合幂律分布）和开度（骨架化+距离变换）［Nie 2026, pp. 7-10］。
- **对比方法**：（1）vanilla模型——基于原PatchGAN和sigmoid交叉熵损失的模型；（2）传统分形‑几何建模方法——基于Watanabe & Takahashi（1995）的裂缝网络生成，并用Upscaling‑GAN生成图的统计参数作为约束［Nie 2026, pp. 11-12］。

## Key Findings

1. **高保真几何复现**：AI生成裂缝网络（1000 × 1000至3000 × 3000像素）在视觉和定量上准确再现了训练图的两组优势方向（近0°/180°和90°），裂缝强度（约1.48‑1.92 m⁻¹）、长度幂律分布（α≈3.45‑3.57，原图3.45）以及开度空间变异（变异系数0.32‑0.37，原图0.42）［Nie 2026, pp. 6-10］。
2. **优于vanilla模型**：vanilla生成的图像局部裂缝过密，长度分布参数严重偏离（α = 14.17，xₘᵢₙ = 2.46），生成器损失稳定在>3（Upscaling‑GAN约为1），训练曲线振荡严重［Nie 2026, pp. 11-12］。
3. **超越传统分形方法**：分形方法无法隐式表征裂缝开度、弯曲度和空间相关性，需后期赋予恒定开度；Upscaling‑GAN则直接从原图学习并自然保留这些特征［Nie 2026, pp. 12及Fig.15］。
4. **内存高效扩展**：当目标图像尺寸从1000 × 1000增至3000 × 3000像素时，GPU峰值内存消耗基本不变（Fig.8），突破了许多GAN模型的内存瓶颈［Nie 2026, pp. 6］。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 裂缝方向玫瑰图显示AI生成图像与实图均以N‑S和E‑W向为主，但生成图的0°–30°区间比例略低 | Nie 2026, pp. 7-8 (Fig.10) | 使用复剪切波检测+ Otsu阈值分割提取裂缝段，方向从正Y轴顺时针计算 | 误差可能来自预处理中某些裂缝迹线未被完整提取 |
| 裂缝强度：实图1.9207 m⁻¹，生成图分别为1.476、1.748、1.7549 m⁻¹ | Nie 2026, pp. 8-9 (Fig.12) | 采用圆形扫描线方法，采样圆数量随图像面积增加（9→36→144→324） | 强度整体一致，小尺度非均质性导致实图值略高 |
| 长度分布符合幂律：实图α=3.4487，xₘᵢₙ=0.8003；Upscaling‑GAN α≈3.45‑3.57，xₘᵢₙ≈0.7‑1.1；vanilla α=14.1679，xₘᵢₙ=2.4562 | Nie 2026, pp. 9-10, 11‑12 (Fig.13,14) | MLE拟合，拟合概率均>97%；提取时可能漏长裂缝 | 生成图最长裂缝~5 m，实图~3.24 m，因实图部分长裂缝在预处理时中断 |
| 开度变异系数：实图CV=0.42，生成图CV=0.32‑0.37；平均开度2.65 px（实） vs 2.50‑3.90 px（生成） | Nie 2026, pp. 10-11 (Table 2) | 通过骨架化+距离变换计算开度，未在训练中使用 | 模型直接从原图学习开度变化，避免了常数开度假设 |
| GPU峰值内存消耗随目标图像尺寸增大近乎不变 | Nie 2026, pp. 6 (Fig.8) | 生成时使用patch‑by‑patch，补丁尺寸128×128 | 内存取决于补丁大小，而非最终图像大小 |
| 双PatchGAN+hinge损失+梯度惩罚训练稳定，生成器损失~1，远低于vanilla模型的>3 | Nie 2026, pp. 4-5, 6‑7, 11‑12 (Fig.7,14c) | 训练780 epoch，学习率0.0002，batch size 60，λ=10 | 改进的损失函数避免了梯度消失，提升收敛性和生成质量 |

## Limitations

- 定量分析仍需对生成图像进行二值化、骨架化等后处理，该过程中可能遗漏裂缝迹线，导致方向分布微小偏差和最大长度误差［Nie 2026, pp. 7-10］。
- 仅使用单张训练图像，模型在其他裂缝模式上的泛化能力未经验证［Nie 2026, pp. 5-6］。
- 当前为二维框架，尚未扩展到三维裂缝网络建模。
- 训练图像的物理尺寸被假定为5 m × 5 m，实际尺度转换需额外标定。
- 虽然局部填充消除了相邻拼接块的接缝，但极长程（>百米）的结构一致性仍有待检验。

## Assumptions / Conditions

- 单张小尺度图像包含了该裂缝系统的代表性统计特征，且裂缝空间变异性可由patch扩展捕捉［Nie 2026, pp. 2-3,5‑6］。
- 训练和生成均限于二维灰度图像。
- 用于定量评估的圆形扫描线法、幂律MLE拟合等统计手段适用，且预处理（剪切波检测、Otsu阈值）能可靠提取裂缝骨架。
- 损失函数中梯度惩罚的λ固定为10，符合Gulrajani等推荐值［Nie 2026, pp. 4-5］。

## Key Variables / Parameters

- **模型结构**：patch数量3 × 3，单patch尺寸128 × 128；生成器输入噪声维度128，每个噪声patch分辨率4 × 4；生成器和判别器均使用谱归一化；判别器采用双PatchGAN（空洞卷积与标准卷积）［Nie 2026, pp. 3-5, Table 1］。
- **训练参数**：epoch数780，学习率0.0002（生成器与判别器），batch size 60，总样本数6000，梯度惩罚权重λ=10［Nie 2026, pp. 6-7, Table 1］。
- **损失函数**：判别器hinge损失 L_D₁ + λ·梯度惩罚（式1‑3），生成器非饱和hinge损失 L_G = -E[D(G(z))]［Nie 2026, pp. 4-5］。
- **裂缝统计变量**：方向（玫瑰图），强度（圆形扫描线法，式4），长度幂律分布参数α和xₘᵢₙ（式5），开度均值、标准差、变异系数CV［Nie 2026, pp. 7-11］。

## Reusable Claims

1. **Upscaling‑GAN可从单张500×500裂缝图像生成任意尺寸的二维裂缝网络，且保留原始裂缝的方向分布、强度、长度幂律标度和开度变异性**。条件：无需对原始图像进行二值化或骨架化预处理。［Nie 2026, pp. 6-11］
2. **采用双PatchGAN判别器和hinge损失+梯度惩罚，相比单PatchGAN+sigmoid交叉熵损失，显著提升裂缝网络生成的几何逼真度和训练稳定性**。［Nie 2026, pp. 11-12］
3. **patch‑by‑patch生成配合局部填充，使GPU内存限制只取决于补丁大小而非目标图像尺寸，可实现工程尺度的大图生成**。［Nie 2026, pp. 5-6］
4. **直接从原始图像学习的裂缝开度具有空间变化性，克服了传统DFN或GAN方法中裂缝开度常设为常数或丢失的问题，对裂缝岩体渗流‑力学耦合模拟至关重要**。［Nie 2026, pp. 10-12］
5. **定量验证时，自动化裂缝迹线检测（复剪切波变换）与FracPaQ工具组合，可有效评估生成裂缝网络的几何属性，但检测不完整可能引入轻微偏差**。［Nie 2026, pp. 7-10］

## Candidate Concepts

- [[Upscaling-GAN]]
- [[patch-by-patch generation paradigm]]
- [[fracture network upscaling]]
- [[fracture aperture]]
- [[fracture intensity]]
- [[circular scanline]]
- [[power-law length distribution]]
- [[fracture orientation rose diagram]]
- [[discrete fracture network (DFN)]]
- [[generative adversarial network]]
- [[hinge loss]]
- [[gradient penalty]]
- [[local padding]]
- [[spectral normalization]]
- [[dual-discriminator architecture]]
- [[automated fracture trace detection]]
- [[complex shearlet transform]]
- [[FracPaQ]]

## Candidate Methods

- [[Upscaling-GAN framework]]
- [[GAN training with local padding]]
- [[dual-PatchGAN discriminator]]
- [[hinge loss with gradient penalty]]
- [[automated fracture trace detection (complex shearlet transform)]]
- [[FracPaQ toolbox for fracture quantification]]
- [[circular scanline method for fracture intensity]]
- [[power-law MLE fitting for fracture length]]
- [[fracture skeletonization and distance transform for aperture]]
- [[dilated convolution in discriminator]]

## Connections To Other Work

- 基础GAN架构源自Goodfellow等（2014），并基于Abdellatif等（2024）的patch‑based无限纹理合成方展开，改进判别器结构和损失函数［Nie 2026, pp. 2-5］。
- 双PatchGAN判别器与Sun等（2023）的Hybrid‑discriminator思路相似，并引入空洞卷积增强多尺度感知能力［Nie 2026, pp. 3-4］。
- 裂缝生成领域，Zhou等（2025）的FracGen基于SinGAN进行裂缝上采样，但需要二值化和骨架化预处理，无法保留开度；本工作避免了此类预处理和信息丢失［Nie 2026, pp. 1-2,10‑11］。
- Chen等（2023）使用VAE-GAN进行裂缝随机反演，Teng等（2025）用WGAN-GP生成裂缝网络，均未直接处理裂缝开度的空间变异性［Nie 2026, pp. 2］。
- 传统分形‑几何DFN建模（Watanabe & Takahashi, 1995; Davy et al., 2010）需要预设统计参数且无法自动生成弯曲裂缝和变开度，Upscaling‑GAN的生成图在统计一致的前提下包含了更丰富的几何细节［Nie 2026, pp. 12］。
- 训练数据源自Karimpouli等（2020）的煤岩裂缝图像，裂缝检测和统计工具分别采用Prabhakaran等（2019）的复剪切波算法和Healy等（2017）的FracPaQ工具箱［Nie 2026, pp. 5-6,7‑8,13‑14］。

## Open Questions

- 模型对含多组错综裂缝、不同母岩类型及复杂交切关系的裂缝图像的泛化能力如何？
- 能否将二维Upscaling‑GAN扩展至三维，同时保持裂缝连通性和拓扑一致性？
- 能否融入裂缝力学成因或应力场先验，以提升生成裂缝的地质合理性？
- 局部填充在数百米尺度的大图像中是否能维持全局连通性？
- 若现场获得的训练图像不能完全代表目标区域特征，模型如何进行迁移学习或小样本微调？
- 丢弃随机空间图虽加速训练，其对长程空间结构的影响是否充分评估？

## Source Coverage

本页面完全基于提供的全部14个非空索引片段编译，原始索引字符数67 330，编译后字符63 832，覆盖比率按块计为1.0，按字符计约为0.948。所有论断均附源片段标注，无遗漏或自行补充的信息。
