---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2025-teng-generating-high-fidelity-discrete-fracture-networks-from-low-dimensional-latent-spaces"
title: "Generating High-Fidelity Discrete Fracture Networks from Low-Dimensional Latent Spaces Using Generative Adversarial Network."
status: "draft"
source_pdf: "data/papers/2025 - Generating high-fidelity discrete fracture networks from low-dimensional latent spaces using generative adversarial network.pdf"
collections:
citation: "Teng, Zheng, et al. \"Generating High-Fidelity Discrete Fracture Networks from Low-Dimensional Latent Spaces Using Generative Adversarial Network.\" *International Journal of Rock Mechanics and Mining Sciences*, vol. 196, 2025, 106301, doi:10.1016/j.ijrmms.2025.106301."
indexed_texts: "21"
indexed_chars: "100667"
nonempty_source_blocks: "21"
compiled_source_blocks: "21"
compiled_source_chars: "95817"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.951821"
coverage_status: "full-index"
source_signature: "24a7ee5d1951fe09499901b6586161384a80e7e2"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T08:11:25"
---

# Generating High-Fidelity Discrete Fracture Networks from Low-Dimensional Latent Spaces Using Generative Adversarial Network.

## One-line Summary

提出一种基于WGAN-GP的低维离散裂隙网络（DFN）参数化方法，能够在极低维潜空间生成高保真且忠实于裂隙统计特征与先验知识的DFN，并验证其在反演中的应用有效性。

## Research Question

如何在数据稀缺条件下，实现对复杂离散裂隙网络的低维、条件化参数化，使其既能从低维潜空间生成高保真DFN，又能忠实服从裂隙位置、长度、方向统计分布以及裂隙存在性与连通性等先验知识，以缓解DFN反演的病态性与计算负担？[Teng 2025, pp. 1-2; pp. 2-3]

## Study Area / Data

- **合成DFN训练/测试数据**：基于Marked Point Processes（MPP）生成，裂隙中心位置服从分形分布（维数Dc = 1.5或2），长度服从幂律分布（指数a = 2或3，lmin = 5或10 m，lmax = 20 m），方向服从von-Mises分布（μ = -30°或17°，κ = 5或20）。数据集包含10、20、50条裂隙的随机网络，分辨率分别为64×64和128×128像素，域尺寸20×20 m²，每个数据集含30 000个样本。[Teng 2025, pp. 3-4; pp. 5-6]
- **真实露头图像**：英国Bristol Channel盆地Listock灰岩露头（5个场景）与冰岛Kvíárjökull冰川表面裂隙（2个场景）的高分辨率照片，经窗口扫描随机裁剪生成各30 000个训练样本（64×64像素）。[Teng 2025, pp. 10-12]
- **反演案例参考数据**：合成参考DFN含8条裂隙，两口井（注入与生产），在GEOS中模拟稳态压力场，于49个观测点提取压力值作为反演观测数据。裂隙统计参数：lmin=5 m，lmax=20 m，a=2，μ=-30°，κ=5，Dc=2。[Teng 2025, pp. 12-14]

## Methods

- **训练样本准备**：采用Marked Point Processes（MPP）顺序确定裂隙中心位置、长度与方向，强制分形、幂律、von-Mises等统计分布；对于含先验知识（裂隙存在性、连通性）的训练样本，先生成随机DFN再植入预设裂隙，仅保留满足连通性条件且移除孤立裂隙的样本，共生成30 000个。[Teng 2025, pp. 3-4; pp. 8-10]
- **WGAN-GP模型架构与训练**：生成器与判别器均由残差网络（ResNets）构建；生成器包含4个上采样残差块，判别器包含4个下采样残差块；损失函数含梯度惩罚项（λ=10）；学习率1×10⁻⁴，批大小64；潜空间维度测试值为2、4、8、16、32、64；训练在NVIDIA GeForce RTX 4090上进行，100 000次迭代。[Teng 2025, pp. 4-5]
- **生成DFN的统计分析**：先生成DFN图像，用增强深度超分辨率网络（EDSR）将分辨率从64×64提升至300×300，再用概率霍夫变换（PHT）提取裂隙线段信息，进而统计裂隙数量、长度、位置分形维数、方向von-Mises拟合参数。[Teng 2025, pp. 5-6]
- **反演框架**：使用训练好的WGAN-GP将16维潜变量映射为DFN；前向流体模拟采用GEOS中的嵌入式离散裂隙方法（EDFM）；反演算法为DREAM(ZS)（7条并行链，2000次迭代），通过对比模拟与观测压力数据驱动潜变量采样。[Teng 2025, pp. 12-13]

## Key Findings

1. **低维生成能力**：对于20条裂隙的DFN，传统参数化需80个参数，而所提方法仅需8维潜空间即可生成高保真DFN，维度降低约90%。潜维度过低时生成裂隙模糊，随维度增加质量提升至平稳；但极低维仍能保持裂隙数量与统计特征。[Teng 2025, pp. 5-6; pp. 14-15]
2. **忠实于裂隙统计分布**：在10条、20条、50条裂隙场景下，生成DFN的裂隙位置分形维数、长度幂律指数a、方向von-Mises参数μ和κ均与训练数据高度一致（偏差通常在0.1以内）。即使潜维度仅为4，也能保持这些统计特性。[Teng 2025, pp. 6-7; pp. 7-8; pp. 8-10; figs. 4, 6, 7]
3. **先验知识（存在性与连通性）的继承**：当训练样本植入2条预设连通裂隙时，生成DFN中该连通关系的实现率约87%–90%（训练样本本身约91%–94%）；随预设裂隙数增至4条，成功率下降（训练样本~77%，生成DFN约59%–62%），主要受限于裂隙检测误差而非模型能力。生成DFN的裂隙数、交点数均值与方差均与训练数据接近。[Teng 2025, pp. 10-10; Table 1]
4. **真实裂隙网络生成**：基于灰岩与冰川露头图像训练的WGAN-GP能生成与真实裂隙几何模式（优势方向、弯曲形态、长短裂隙连通格局）高度相似的图像，甚至2维潜空间即可产生令人满意的结果。[Teng 2025, pp. 10-12; Fig. 10]
5. **DFN反演有效性**：合成案例中，采用所提参数化方法，DREAM(ZS)反演能逐步收敛至参考DFN，后验压力预测与参考值吻合良好；可变裂隙数量（由固定维潜空间自然产生）与连通性约束是提升反演效率与鲁棒性的关键。[Teng 2025, pp. 13-14; Figs. 12, 13]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 8维潜空间可生成20条裂隙的高质量DFN，维度降低90% | [Teng 2025, pp. 5-6; pp. 14-15] | DFN分辨率64×64，训练样本30k，裂隙长度幂律分布（a=2, lmin=5m, lmax=20m），方向von-Mises（μ=-30°, κ=5），分形维数Dc=2 | 传统方法需80参数（4参数/裂隙×20） |
| 生成DFN的分形维数Dc约为1.9（预设2.0），长度幂律指数a偏差<0.1，方向拟合μ、κ接近训练值 | [Teng 2025, pp. 6-7; Fig. 4] | 10条裂隙场景，潜维度4–32，5种统计参数组合 | 训练样本Dc因边界截断略低于2.0，生成DFN继承该偏差 |
| 2条预设连通裂隙的连通成功率在生成DFN中达87%–90% | [Teng 2025, pp. 10-10; Table 1] | 训练样本含预设连通裂隙且经连通性筛选；lmin=5m或10m，其它参数a=2，μ=-30°，κ=5，Dc=2；潜维度4、8、16 | 训练样本自身成功率91%~94%，差异主要来自PHT检测误差 |
| 4条预设连通裂隙时，生成DFN连通成功率59%–62% | [Teng 2025, pp. 10-10; Table 1] | lmin=10m，其它统计参数同上；潜维度4、8、16 | 训练样本约77%；检测误差为主因 |
| 反演中后验压力预测与参考值的吻合度高，后验裂隙分布捕捉主要连通路径 | [Teng 2025, pp. 13-14; Figs. 12,13] | 参考DFN含8条裂隙，16维潜空间，49个观测压力点，DREAM(ZS) 7链2000迭代 | 模型的可变裂隙数与连通约束促进反演收敛 |

## Limitations

1. **裂隙检测精度受限**：所用EDSR+PHT方法难以区分方向相近且距离近的裂隙，并可能在模糊区域将单裂隙误判为多条短裂隙；对高密度、弯曲裂隙的检测能力不足，导致裂隙数量和统计参数偏差。[Teng 2025, pp. 5-6; pp. 15-16]
2. **3D拓展困难**：三维DFN生成将面临训练数据量剧增、计算成本高昂（当前128×128单场景训练已超140小时、23 GB显存），且缺乏高精度3D裂隙检测技术；模型架构需重新优化。[Teng 2025, pp. 16-17]
3. **连通性并非100%保证**：生成DFN中预设裂隙的连通性仍可能缺失，残留的不连通DFN会在流/示踪剂反演中引入非线性不确定性。[Teng 2025, pp. 10-10]
4. **模式崩塌倾向**：在低潜维度下，部分生成DFN出现裂隙聚集和区域覆盖减少的现象。[Teng 2025, pp. 5-6]
5. **尺度与分辨率受限**：DFN图像分辨率和GPU内存限制了可生成的裂隙密度与空间尺度，更高密度或更大域需更高分辨率训练样本和更昂贵的计算资源。[Teng 2025, pp. 16-16]

## Assumptions / Conditions

- 裂隙在二维中简化为直线段，不考虑裂隙开度、粗糙度等三维属性。[Teng 2025, pp. 3-4; pp. 16-16]
- 训练样本的裂隙位置、长度和方向分别严格服从分形分布、幂律分布和von-Mises分布；已知统计参数（Dc, a, lmin, lmax, μ, κ）在训练前被固定。[Teng 2025, pp. 3-4]
- 先验连通性约束仅通过训练样本的选择性保留实现，未在损失函数中显式编码。[Teng 2025, pp. 8-10]
- DFN生成域为正方形（20 m×20 m），图像像素为64×64或128×128。[Teng 2025, pp. 3-4]
- 反演案例中，所有裂隙赋予均匀开度（1.5×10⁻³ m）和宽度（0.2 m），基质渗透率恒定为1×10⁻¹⁶ m²，流体为稳态单相。[Teng 2025, pp. 12-13]
- 训练数据集均为30 000个样本；WGAN-GP训练时，潜变量先验为标准高斯分布。[Teng 2025, pp. 4-5]

## Key Variables / Parameters

- **潜空间维度** (LD)：2, 4, 8, 16, 32, 64，决定参数化压缩程度。[Teng 2025, pp. 5-6]
- **裂隙数量**：10、20、50条（合成案例），用于评估不同密度下的生成质量。[Teng 2025, pp. 5-6]
- **统计分布参数**：分形维数 Dc (1.5, 2)；幂律指数 a (2, 3)；长度界限 lmin, lmax (5 m, 10 m, 20 m, 30 m)；方向均值 μ (−30°, 17°, 50°) 与浓度参数 κ (5, 20)。[Teng 2025, pp. 3-4; pp. 7-8; Figs. 4,6,7]
- **预设先验裂隙数**：2, 3, 4条，用于测试条件生成能力。[Teng 2025, pp. 8-10; Table 1]
- **连通成功率 p**：生成DFN中满足预设连通性条件的比例，受潜维度和裂隙数影响。[Teng 2025, pp. 10-10; Table 1]
- **裂隙交点数/裂隙总数的均值与方差**：反映生成网络的拓扑复杂性。[Teng 2025, pp. 10-10; Table 1]
- **流动路径总长度**：从注入到监测裂隙的最短路径长度统计，用于评估输运特性保留度。[Teng 2025, pp. 10-10; Fig. 9]
- **反演中的潜变量**：16维向量，经DREAM(ZS)采样，控制DFN的生成。[Teng 2025, pp. 12-13]

## Reusable Claims

- 基于WGAN-GP的DFN生成器，在8维潜空间中可产出与传统80参数参数化方法视觉与统计质量相当的二维20裂隙DFN，实现约90%的维度缩减（条件：训练集尺寸30k，统计分布参数固定，域分辨率64×64）。[Teng 2025, pp. 5-6; pp. 14-15]
- 当训练样本的裂隙统计服从分形（Dc）、幂律（a）和von-Mises（μ, κ）时，从低至4维潜空间随机生成的DFN能够以偏差<0.1的水平复现这些统计（条件：训练样本数量充足，裂隙检测使用EDSR+PHT）。[Teng 2025, pp. 6-7; Fig. 4]
- 在训练数据中植入预定义连通裂隙并仅保留满足连通性的样本后，WGAN-GP生成的DFN能有效继承这种硬约束：2条预设裂隙时连通成功率接近90%，但成功率随预设裂隙数量增加而下降，4条时约60%（条件：裂隙检测方法为PHT，存在检测误差）。[Teng 2025, pp. 10-10; Table 1]
- 以真实露头图像的小窗口裁剪样本训练WGAN-GP后，可在2维潜空间生成视觉上逼真、保留优势方向和弯曲特征的裂隙网络（条件：训练样本源于同质性区域，图像分辨率64×64）。[Teng 2025, pp. 10-12; Fig. 10]
- 将该低维条件DFN参数化方法与DREAM(ZS)结合，可实现基于稳态压力观测的裂隙网络反演，后验压力预测与参考值高度一致，且模型可变裂隙数量和连通约束有助于收敛（条件：注入-生产井间至少有连通路径，训练数据已包含该连通性）。[Teng 2025, pp. 12-14]

## Candidate Concepts

- [[discrete fracture network (DFN)]]
- [[low-dimensional parameterization]]
- [[Wasserstein GAN with gradient penalty (WGAN-GP)]]
- [[residual network (ResNet)]]
- [[latent space]]
- [[fractal dimension]]
- [[power-law length distribution]]
- [[von-Mises orientation distribution]]
- [[Marked Point Processes (MPP)]]
- [[fracture connectivity]]
- [[prior knowledge constrained generation]]
- [[generative adversarial network]]
- [[DFN inversion]]
- [[pressure field matching]]
- [[mode collapse]]

## Candidate Methods

- [[WGAN-GP with ResNets]]
- [[Marked Point Processes for DFN simulation]]
- [[Enhanced Deep Super-Resolution network (EDSR)]]
- [[Probabilistic Hough Transform (PHT) for fracture detection]]
- [[Embedded Discrete Fracture Method (EDFM) in GEOS]]
- [[DREAM(ZS) MCMC inversion]]
- [[conditional DFN generation via constrained training data]]
- [[multiplicative cascade process for fractal point generation]]
- [[connectivity filtering of training DFNs]]

## Connections To Other Work

- 传统DFN参数化通过Hough变换将裂隙转化为连续场再用PCA降维（如Yao et al., 2018; Lu & Zhang, 2015），但无法保持公认的幂律、分形等统计特征。[Teng 2025, pp. 1-2]
- 先前基于深度学习的DFN降维方法（DSAE, VAE, VAE-GAN）虽然初步验证了可行性，但未检验生成DFN的统计分布，也未考虑裂隙存在性与连通性等硬性先验知识。[Teng 2025, pp. 2-3]
- 本研究采用的WGAN-GP架构（Gulrajani et al., 2017）相比标准GAN改进了训练稳定性，并在二维DFN上取得了高效降维。[Teng 2025, pp. 4-5]
- 反演中利用潜变量全局控制DFN形态、实现平滑过渡的思想与许多水文地质反演中的模型降维策略一致（如利用PCA、VAE），但对离散特征明显的DFN特别有效。[Teng 2025, pp. 5-6; pp. 14-15]
- 裂隙连通性作为硬约束训练生成模型可类比于地质统计模拟中的条件模拟（如Laloy et al., 2018），但文中并未详细对比。[Teng 2025, pp. 8-10]

## Open Questions

- 如何开发更高精度的裂隙检测算法，以支持高密度、弯曲裂隙的可靠统计分析？[Teng 2025, pp. 15-16]
- 如何在三维DFN中实现类似的低维条件参数化，并解决计算成本与检测精度的双重难题？[Teng 2025, pp. 16-17]
- 当先验连通性较复杂（多条监控裂隙且要求多连通路径）时，如何保证生成DFN的高成功率且不引入过多不连通样本？[Teng 2025, pp. 10-10]
- 潜维度的选取标准尚不明确，能否建立基于数据复杂度的自动确定规则？[Teng 2025, pp. 14-15]
- 该方法能否扩展到包含非直线裂隙、三维网络以及变开度、应力相关裂隙的复杂场景？[Teng 2025, pp. 16-17]
- 在真实场地数据（如EGS Collab）的应用中，如何有效整合井孔探测、示踪剂数据等多源信息？[Teng 2025, pp. 7-8]

## Source Coverage

所有21个非空索引片段均已被处理。编译后的源块数为21，总字符数95817，覆盖比（按字符）为0.951821（基于索引字符总量100667）。覆盖状态：full-index。编译策略：single-pass-markdown。来源签名：24a7ee5d1951fe09499901b6586161384a80e7e2。
