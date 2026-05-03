---
type: "method"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
name: "基于生成对抗网络的 DFN 生成 (GAN-based DFN)"
aliases:
  - "WGAN-GP"
  - "SinGAN"
  - "FracGen"
  - "Upscaling-GAN"
  - "AI-Geo upscaling"
sources:
  - "2025-teng-generating-high-fidelity-discrete-fracture-networks-from-low-dimensional-latent-spaces"
  - "2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers"
  - "2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai"
---

# 基于生成对抗网络的 DFN 生成 (GAN-based DFN)

## Purpose

利用生成对抗网络从少量图片或低维潜变量中学习裂缝网络形态，生成高保真、保留统计特征的二维离散裂隙网络，支持升尺度。
## Aliases

- WGAN-GP
- SinGAN
- FracGen
- Upscaling-GAN
- AI-Geo upscaling
## Workflow

收集/生成 DFN 图像数据集；训练 GAN（生成器+判别器），使用改良结构如 WGAN-GP、双 PatchGAN、自注意力机制、hinge 损失+梯度惩罚等提升质量；通过潜空间采样或图像金字塔级联生成任意尺寸图像；采用局部填充消除拼接痕迹。
## Inputs

- 裂缝图像数据集（二值或灰度）
## Outputs

- 任意尺寸的高保真裂缝网络图像（灰度/二值）
## Assumptions

- 训练样本统计分布已知或可代表整体
- 图像内部块具有重复特性
## Strengths

- 无需显式参数化，保留复杂拓扑和开度变异性
- 可生成大尺度网络
## Limitations

- 目前主要限于 2D，扩展 3D 难度大
- 生成质量依赖训练数据多样性和数量
## Related Concepts

- discrete-fracture-network
## Source Papers

- [2025-teng-generating-high-fidelity-discrete-fracture-networks-from-low-dimensional-latent-spaces](../papers/2025-teng-generating-high-fidelity-discrete-fracture-networks-from-low-dimensional-latent-spaces.md)
- [2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers](../papers/2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers.md)
- [2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai](../papers/2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai.md)
