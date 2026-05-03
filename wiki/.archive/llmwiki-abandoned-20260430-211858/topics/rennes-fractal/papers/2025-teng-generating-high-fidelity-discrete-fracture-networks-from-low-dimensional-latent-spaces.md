---
type: "paper"
paper_id: "2025-teng-generating-high-fidelity-discrete-fracture-networks-from-low-dimensional-latent-spaces"
title: "Generating High-Fidelity Discrete Fracture Networks from Low-Dimensional Latent Spaces Using Generative Adversarial Network."
status: "draft"
source_pdf: "data/papers/2025 - Generating high-fidelity discrete fracture networks from low-dimensional latent spaces using generative adversarial network.pdf"
citation: "Teng, Zheng, et al. \"Generating High-Fidelity Discrete Fracture Networks from Low-Dimensional Latent Spaces Using Generative Adversarial Network.\" *International Journal of Rock Mechanics and Mining Sciences*, vol. 196, 2025, 106301. doi:10.1016/j.ijrmms.2025.106301. Accessed 2026."
indexed_texts: "21"
indexed_chars: "100667"
compiled_at: "2026-04-27T19:49:02"
---

# Generating High-Fidelity Discrete Fracture Networks from Low-Dimensional Latent Spaces Using Generative Adversarial Network.

## One-line Summary

本文提出了一种基于 Wasserstein GAN with Gradient Penalty (WGAN-GP) 的低维参数化方法，从仅 8–64 维的隐空间中生成高保真离散裂缝网络（DFN），在显著降低参数空间维度的同时，保持了裂缝位置、长度、方向的统计特征，并能有效融入先验知识约束 [Teng 2025, pp. 1-1, pp. 5-6]。

## Research Question

如何从低维隐空间生成高保真的离散裂缝网络，以解决传统 DFN 参数化方法导致的高维参数空间带来的病态性和计算负担，同时保证生成的 DFN 能忠实反映裂缝的统计特征以及有限的先验知识（如已知裂缝的存在和连通性）？[Teng 2025, pp. 1-1, pp. 2-3]

## Study Area / Data

本研究主要使用合成 DFN 训练数据集，裂缝位置、长度、方向分别服从分形分布、幂律分布和 von-Mises 分布 [Teng 2025, pp. 2-3]。共制备了 3 组数据集，每组包含 30,000 个 DFN 样本，裂缝数量分别为 10、20 和 50 条，对应的图像分辨率分别为 64×64 px（10、20 裂缝）和 128×128 px（50 裂缝）[Teng 2025, pp. 5-6]。此外，还从天然野外露头中映射了真实 DFN 样本用于训练 WGAN-GP 模型，以验证方法对真实数据的适用性 [Teng 2025, pp. 2-3]。

## Methods

1. **DFN 训练样本生成**：采用基于乘法级联过程的方法生成分形空间分布（分形维数 Dc 设为 1.5 或 2），裂缝长度服从幂律分布，方向服从 von-Mises 分布 [Teng 2025, pp. 3-4]。
2. **生成模型**：使用 WGAN-GP（Wasserstein GAN with Gradient Penalty），其生成器将低维隐参数 z 映射为 DFN 图像，判别器以 Wasserstein-1 距离为度量并施加梯度惩罚以满足 Lipschitz 约束 [Teng 2025, pp. 4-5]。
3. **隐空间维度实验**：测试了 2、4、8、16、32、64 六种隐维度，比较生成 DFN 的质量与统计一致性 [Teng 2025, pp. 5-6]。
4. **先验知识约束**：制备条件化 DFN 训练数据集，包含若干固定裂缝和连通裂缝，评估方法在约束下的生成能力 [Teng 2025, pp. 7-8]。
5. **后处理与统计验证**：将生成图像从 64×64 或 128×128 像素缩放至 300×300 像素，使用概率霍夫变换（PHT）提取线段信息，对裂缝位置、长度、方向进行分形维数、幂律分布和 von-Mises 分布拟合 [Teng 2025, pp. 5-6]。

## Key Findings

- **低维隐空间的有效性**：隐维度低至 8 即可生成包含 20 条裂缝的高质量 DFN 图像，而传统参数化方法需 80 个参数，实现了显著的模型降维 [Teng 2025, pp. 5-6]。
- **统计特征保持**：生成 DFN 的裂缝数量、位置（分形维数 Dc）、长度（幂律指数）、方向（von-Mises 集中参数）与训练 DFN 高度一致；例如，分形维数 Dc 在生成样本中围绕训练样本的测量值（约 1.9 或 1.8）小范围波动 [Teng 2025, pp. 6-7]。
- **隐维度对统计量的影响**：隐维度对裂缝数量的影响很小，即使极低维度也能生成预期数量的裂缝；但隐维度增加可改善图像中裂缝的清晰度和笔直度 [Teng 2025, pp. 5-6]。
- **先验知识约束能力**：方法能够生成条件化 DFN，尊重指定的固定裂缝和连通裂缝信息 [Teng 2025, pp. 7-8]。
- **对不同裂缝参数的鲁棒性**：改变裂缝长度范围（lmin 或 lmax）时，模型仍能稳定生成高保真 DFN [Teng 2025, pp. 7-8]。
- **光滑全局调控**：每个隐参数影响整体裂缝分布模式而非单条裂缝，改变隐参数时 DFN 的位置、长度、方向连续光滑变化 [Teng 2025, pp. 5-6]。

## Limitations

- **图像分辨率与检测误差**：图像中裂缝边界或交叉处的模糊区域导致一条裂缝被误识别为多条短裂缝，造成观测到的裂缝数量偏高（高于预期）[Teng 2025, pp. 6-7]。
- **分形维数测量偏差**：由于乘法级联采样过程中空间离散分辨率有限，训练样本实测分形维数与预设值存在偏差（如预设 1.5 时实测约 1.75），生成 DFN 的测量值也相应略有偏移 [Teng 2025, pp. 6-7]。
- 其他局限性（如对极复杂裂缝网络或三维 DFN 的扩展能力）未从索引片段中确认。

## Reusable Claims

- “使用 WGAN-GP 可从低维隐空间生成高保真 DFN，隐空间维度低至 8 即可满足 20 裂缝场景，而传统方法需 80 个参数” [Teng 2025, pp. 5-6]。
- “生成的 DFN 在裂缝数量、分形位置分布、幂律长度分布和 von-Mises 方向分布上与训练数据统计一致，差异主要来源于图像后处理的分辨率限制” [Teng 2025, pp. 6-7]。
- “该参数化方法中每个隐参数影响整体裂缝分布模式，隐空间变化导致 DFN 全局光滑变化” [Teng 2025, pp. 5-6]。
- “模型可融入先验知识（如固定裂缝和连通裂缝），生成条件化的 DFN” [Teng 2025, pp. 7-8]。
- “低维隐空间显著缓解了 DFN 反演的病态性和计算负担” [Teng 2025, pp. 1-1]。

## Candidate Concepts

- [[离散裂缝网络]]
- [[WGAN-GP]]
- [[分形分布]]
- [[幂律分布]]
- [[von-Mises分布]]
- [[低维参数化]]
- [[先验知识约束]]
- [[概率霍夫变换]]
- [[模型降维]]
- [[病态反演]]

## Candidate Methods

- [[Wasserstein GAN with Gradient Penalty]]
- [[乘法级联过程]]
- [[概率霍夫变换]]
- [[条件化 DFN 生成]]

## Open Questions

- 对于裂缝数量超过 50 条或分辨率更高的 DFN，所需的最小隐维度是多少？未从索引片段中确认。
- 该方法在三维 DFN 生成中的表现如何？未从索引片段中确认。
- 与其他生成模型（如变分自编码器或扩散模型）相比，WGAN-GP 方法在保真度和效率上的优劣？未从索引片段中确认。
- 真实露头 DFN 样本训练的具体结果（定量统计对比）未在片段中完整呈现。

## Source Coverage

本页面引用的论文索引片段来自以下页码范围：pp. 1-1, 1-2, 2-3, 3-4, 4-5, 5-6, 6-7, 7-8。
