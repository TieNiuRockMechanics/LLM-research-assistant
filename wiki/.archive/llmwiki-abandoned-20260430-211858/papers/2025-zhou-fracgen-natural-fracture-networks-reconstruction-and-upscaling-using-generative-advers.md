---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers"
title: "FracGen: Natural Fracture Networks Reconstruction and Upscaling Using Generative Adversarial Networks."
status: "draft"
source_pdf: "data/papers/2025 - FracGen Natural fracture networks reconstruction and upscaling using generative adversarial networks.pdf"
collections:
citation: "Zhou, Changtai, Borui Lyu, and Yu Wang. \"FracGen: Natural Fracture Networks Reconstruction and Upscaling Using Generative Adversarial Networks.\" *International Journal of Rock Mechanics and Mining Sciences*, 2025, doi:10.1016/j.ijrmms.2025.106116. Accessed 2026."
indexed_texts: "16"
indexed_chars: "77664"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T15:15:34"
---

# FracGen: Natural Fracture Networks Reconstruction and Upscaling Using Generative Adversarial Networks.

## One-line Summary
FracGen 是一个基于单图像生成对抗网络（SinGAN）的非参数机器学习模型，利用多尺度金字塔架构从单一露头图像中重建和放大天然裂缝网络，并能保留关键统计特性而无需显式参数化 [Zhou 2025, pp. 1-1]。

## Research Question
如何克服传统方法在复杂几何形态与尺度转换上的局限性，实现对天然裂缝网络的精确重建与放大，使得大尺度模拟能够保留小尺度观测到的关键特征 [Zhou 2025, pp. 1-1]。

## Study Area / Data
训练数据为三张来自不同地质环境的天然裂缝网络图像，均为2m × 2m 范围，分别对应：
- Kilve（Bristol Channel 盆地南缘）干旱大陆岩露头，分辨率236 × 236 [Zhou 2025, pp. 3-5]；
- 苏格兰 Dounreay 地区砂岩露头，分辨率335 × 335 [Zhou 2025, pp. 3-5]；
- West Somerset（Bristol Channel 南岸）石灰岩露头，分辨率116 × 116 [Zhou 2025, pp. 3-5]。

这三张图像经过灰度转换、阈值调整、二值化和骨架化处理，最终获得数字化裂缝网络 [Zhou 2025, pp. 3-3]。

## Methods
FracGen 的整体框架分为三个主要步骤 [Zhou 2025, pp. 3-3]：
1. **裂缝网络数字化**：将露头图像经灰度化、阈值调整、二值化和骨架化处理，获得数字化的裂缝网络 [Zhou 2025, pp. 3-3]。
2. **SinGAN 训练**：采用 SinGAN 的金字塔架构对单一训练图像进行多尺度训练，在不同尺度上构建生成器 \( G_n \) 和判别器 \( D_n \)。训练过程中，输入图像按固定尺度因子 \( r \) 逐级下采样，\( r \) 的值介于1到2之间 [Zhou 2025, pp. 3-5]。生成器通过随机噪声 \( z \) 生成裂缝图案，判别器区分真实样本与生成样本，训练目标为对抗损失与重建损失的优化 [Zhou 2025, pp. 3-3][Zhou 2025, pp. 3-5]。
3. **裂缝网络重建与放大**：利用训练好的多尺度生成器，将随机噪声图输入后逐级生成裂缝网络。对于放大处理，先生成大规模噪声图，再依次输入各级生成器，从而生成大尺度裂缝网络 [Zhou 2025, pp. 3-3]。

评估方法包括：
- 定性评估：视觉对比真实裂缝网络与生成裂缝网络在拓扑结构上的相似性 [Zhou 2025, pp. 5-7]；
- 定量评估：裂缝强度（采用圆形扫描线方法，计算 2D 裂缝强度 \( P_{21} = n / 4r \)）[Zhou 2025, pp. 7-8]、裂缝方位（玫瑰图统计）[Zhou 2025, pp. 7-8]、裂缝长度分布（拟合修正对数正态分布）[Zhou 2025, pp. 8-10]；
- 余弦相似度分析：将裂缝方位和长度数据分箱后，计算生成网络与真实网络在方位和长度分布上的余弦相似度 [Zhou 2025, pp. 10-11]。

## Key Findings
- **定性视觉评估**：FracGen 生成的裂缝网络在整体方向和拓扑结构上与野外调查观测到的细节高度一致，能够捕捉对角线断裂和复杂交叉模式 [Zhou 2025, pp. 5-7]。
- **裂缝强度**：三个地点生成裂缝网络的整体裂缝强度分别为10.16 ± 0.50 m⁻¹、8.97 ± 0.32 m⁻¹、8.82 ± 0.38 m⁻¹，与其实裂缝网络强度10.07 m⁻¹、8.88 m⁻¹、8.86 m⁻¹ 接近 [Zhou 2025, pp. 7-8]。
- **裂缝方位**：生成裂缝网络的方位分布与真实网络一致，均识别出两组节理系，且方位区间高度一致 [Zhou 2025, pp. 7-8]。
- **裂缝长度分布**：生成裂缝网络与真实裂缝网络的裂缝长度均经修正对数正态分布拟合，分布参数 \( x_c \) 和 \( w \) 非常接近，统计特性相似 [Zhou 2025, pp. 8-10]。
- **余弦相似度**：FracGen 生成裂缝网络与真实裂缝网络在裂缝方位和长度上的余弦相似度值较高，表明二者之间存在强对应关系 [Zhou 2025, pp. 1-1][Zhou 2025, pp. 10-11]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| FracGen 能够在不进行显式参数化的情况下，复现天然裂缝的关键统计性质 | [Zhou 2025, pp. 1-1] | 基于三张不同岩性露头的训练图像 | 验证方式包括余弦相似度和概率分布拟合 |
| 生成裂缝网络的整体裂缝强度与真实网络接近（例如10.16 ± 0.50 m⁻¹ vs 10.07 m⁻¹） | [Zhou 2025, pp. 7-8] | 圆形扫描线法计算 \( P_{21} \) | 三组数据均在均值上表现出一致性 |
| FracGen 生成裂缝网络与真实裂缝网络的裂缝长度分布均用修正对数正态分布拟合，且关键参数 \( x_c \) 和 \( w \) 非常接近 | [Zhou 2025, pp. 8-10] | 裂缝长度受有限上下截断限制，分布可能偏离幂律而趋向对数正态 | 反映出生成网络保留了裂缝长度分布的统计特征 |
| 裂缝方位分布（玫瑰图）中，生成网络与真实网络均识别出两个节理系，且方位区间一致 | [Zhou 2025, pp. 7-8] | 适用于含多组节理的裂缝网络 | 方位一致性在干旱大陆岩和砂岩露头中尤为明显 |
| 高余弦相似度值表明生成裂缝网络与真实网络在方位和长度上具有强对应关系 | [Zhou 2025, pp. 1-1][Zhou 2025, pp. 10-11] | 计算方法包含分箱处理 | 具体余弦相似度数值未从索引片段中确认 |

## Limitations
- FracGen 的训练数据包含三张不同地质环境的露头图像，但每种岩性仅采用单张图像进行训练 [Zhou 2025, pp. 3-5]。该模型对不同地质条件与图像质量的泛化潜力未从索引片段中确认。
- 裂缝数字化过程采用的阈值调整和二值化步骤可能导致细尺度裂缝信息丢失 [Zhou 2025, pp. 3-3]。
- 裂缝长度分布受有限上下截断限制，由于分辨率不足和采样约束，小裂缝可能缺失，导致分布由幂律向对数正态偏移 [Zhou 2025, pp. 8-10]。
- 未从索引片段中确认 FracGen 在处理三维裂缝网络、交叉闭合裂缝或充填缝时的能力。
- 未从索引片段中确认模型的计算资源需求、训练时长或收敛特性。

## Assumptions / Conditions
- 训练图像来源于高对比度露头照片，并已通过灰度化、二值化和骨架化获得高质量数字化裂缝网络 [Zhou 2025, pp. 3-3]。
- SinGAN 的金字塔训练架构基于单个训练图像内部的多尺度补丁统计信息，假设图像内特征可迁移至不同尺度 [Zhou 2025, pp. 3-5]。
- 裂缝网络的主要几何统计特征（强度、方位、长度分布）可以从单张二维露头样本中表征，并可扩展至更大尺度 [Zhou 2025, pp. 1-1]。
- 训练和生成过程中使用随机噪声输入，假设输入噪声的随机性可生成多样化的裂缝网络变体 [Zhou 2025, pp. 5-7]。
- 裂缝网络放大依托于多尺度生成器的级联，假定各尺度下学到的裂缝特征可在更大尺度上无失真组合 [Zhou 2025, pp. 3-3]。

## Key Variables / Parameters
- \( G \)：生成器；\( D \)：判别器 [Zhou 2025, pp. 3-3]。
- \( z \)：输入生成器的随机噪声向量 [Zhou 2025, pp. 3-3]。
- \( r \)：尺度因子，介于1到2之间，决定每级训练中图像下采样的程度 [Zhou 2025, pp. 3-5]。
- \( P_{21} = n / 4r \)：二维裂缝强度，其中 \( n \) 为裂缝轨迹与圆形扫描线的交点个数，\( r \) 为扫描线半径 [Zhou 2025, pp. 7-8]。
- \( y \)、\( x \)、\( y_0 \)、\( A \)、\( x_c \)、\( w \)：修正对数正态分布概率密度函数参数，用于拟合裂缝长度分布 [Zhou 2025, pp. 8-10]。
- 对抗损失 \( L_{adv} \) 与重构损失函数 [Zhou 2025, pp. 5-7]。
- 余弦相似度值，用于定量评估生成网络与真实网络在裂缝方位和长度分布上的相似性 [Zhou 2025, pp. 10-11]。

## Reusable Claims
- **Claim 1**：基于 SinGAN 的非参数生成模型能够从单张天然裂缝网络图像中学习并生成保留关键统计特征（强度、方位、长度分布）的新样本，无需显式定义裂缝几何参数。[Zhou 2025, pp. 1-1] [适用条件：训练图像经过高质量数字化预处理；生成网络在金字塔架构多尺度训练后获得。证据：生成网络在三个地质环境不同的露头上均复现了裂缝强度、方位与长度分布的统计一致性。限制：未验证三维裂缝网络与闭合/充填裂缝的适用性。]
- **Claim 2**：利用多尺度生成器级联方法，可将单尺度裂缝网络扩展至更大尺度，同时保持裂缝关键几何特征的统计一致性。[Zhou 2025, pp. 3-3] [适用条件：训练生成器已捕获多尺度下的裂缝补丁统计特征；输入大规模噪声图并通过逐级生成器处理。证据：论文展示了从原始尺度到放大尺度的裂缝网络生成流程。限制：未从索引片段中确认放大后裂缝网络与真实大尺度观测之间的直接量化对比。]

## Candidate Concepts
- [[fracture networks]]
- [[Generative Adversarial Networks]]
- [[non-parametric modeling]]
- [[fracture upscaling]]
- [[single image generative adversarial network]]
- [[multi-scale modeling]]
- [[fracture intensity]]
- [[fracture orientation]]
- [[fracture length distribution]]
- [[cosine similarity]]
- [[lognormal distribution of fracture length]]

## Candidate Methods
- [[SinGAN]]
- [[pyramid architecture for GANs]]
- [[image skeletonization]]
- [[binarization from grayscale]]
- [[circular scanline for fracture intensity]]
- [[rose diagram for fracture orientation]]
- [[modified lognormal distribution fitting]]
- [[cosine similarity analysis for fracture statistics]]

## Connections To Other Work
- FracGen 构建于 GANs 体系之上，该体系在岩石力学中已被扩展至多种形式，包括 SRGAN、cGAN、StyleGAN、CycleGAN、CinCGAN 等，用于解决岩石图像的超级分辨率与多孔结构构建问题 [Zhou 2025, pp. 1-3]。
- 文中提及 Lyu et al. (2024) 提出的多尺度 GAN（MS-GAN）方法，用于从有限钻孔数据构建三维地下地质模型，并表示 FracGen 同样采用了多尺度训练思路 [Zhou 2025, pp. 1-3]。
- 引用先前研究用于说明数字化裂缝网络也可从已有工作中获取，如 Kilve [19]、Dounreay [40]、West Somerset [41] 的露头数据 [Zhou 2025, pp. 3-5]。
- 裂缝长度分布讨论中提及岩石破裂特征（幂律分布与对数正态截断）已被实验室岩石实验和地震能量释放研究所证实 [Zhou 2025, pp. 8-10]。

## Open Questions
- FracGen 是否能处理真实的三维裂缝网络重建与放大，或需扩展至如 MS-GAN 等三维生成架构？
- 在不同图像质量（如噪声、覆盖、分辨率不一）的露头图像上，FracGen 的鲁棒性如何？
- 数字化过程中的阈值与骨架化处理对最终生成裂缝网络连通性、交叉特征的影响程度未量化。
- 生成的裂缝网络在后续的水力-力学模拟中的表现是否与真实裂缝网络一致，尚未从索引片段中确认。
- 该方法的计算复杂度与训练成本是否适用于大规模工程应用场景，未从索引片段中确认。

## Source Coverage
本页依据共 16 个索引片段，覆盖了论文摘要、引言、方法描述（框架与训练细节）、数据来源、定性及定量结果评估，以及部分讨论内容。覆盖相对均衡，主要细节来自摘要与方法部分，结果部分关于裂缝强度、方位、长度分布与余弦相似度的描述较详尽。但以下重要信息可能缺失：详细的网络超参数、训练收敛情况、整套余弦相似度量化数值、放大后裂缝网络的独立验证细节，以及局限性与未来展望的完整讨论。
