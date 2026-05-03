---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2016-mohebbi-rock-mass-structural-data-analysis-using-image-processing-techniques-case-study-cho"
title: "Rock Mass Structural Data Analysis Using Image Processing Techniques (Case Study: Choghart Iron Ore Mine Northern Slopes)."
status: "draft"
source_pdf: "data/papers/2016 - Rock mass structural data analysis using image processing techniques (Case study Choghart iron ore mine northern slopes).pdf"
collections:
  - "审稿人让引用"
citation: "Mohebbi, M., et al. “Rock Mass Structural Data Analysis Using Image Processing Techniques (Case Study: Choghart Iron Ore Mine Northern Slopes).” *Journal of Mining & Environment*, 27 May 2016. Accessed 2026."
indexed_texts: "10"
indexed_chars: "45690"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T20:06:23"
---

# Rock Mass Structural Data Analysis Using Image Processing Techniques (Case Study: Choghart Iron Ore Mine Northern Slopes).

## One-line Summary
针对传统岩体结构面测绘中的人力偏差、安全风险与耗时问题，提出并验证了一种基于数字图像处理的快速、高精度不连续面半自动识别方法，并以伊朗 Choghart 铁矿北坡为案例，获取了多组节理的产状、间距、连续性等定量化数据。

## Research Question
如何克服传统不连续面现场测绘方法（如人工扫线）在采样困难、人为偏差、安全风险、可达性和成本限制等方面的缺陷，利用彩色图像处理算法实现对岩石出露面节理的快速、准确识别与几何参数提取？[Mohebbi 2016, pp. 1-2, 3-4]

## Study Area / Data
研究区为 Choghart 铁矿北坡的多个岩壁出露面。数据来源为用相机垂直拍摄获取的高分辨率彩色数字图像（建议至少 8 百万像素、使用 CCD 传感器），图像中具有标记尺寸的标尺；选取光照差异最小、光照条件相同的图像，并利用斜射光可改善效果。[Mohebbi 2016, pp. 3-5]

## Methods
所开发方法的流程如下：
1. **图像获取与预处理**：将彩色图像转为灰度图，进行直方图平滑；使用基于 GLCM 同质性最小化的局部伽马校正，改善暗部细节；经比较选用全变分去噪以消除表面粗糙度导致的伪迹而保留边缘。[Mohebbi 2016, pp. 5-7]
2. **边缘检测**：采用 Canny 边缘检测器，先通过 Sobel 算子计算梯度幅值与方向，然后进行非极大值抑制，最后采用滞后阈值（高阈值 T1=0.5，低阈值 T2=0.2）提取边缘像素。[Mohebbi 2016, pp. 7-9]
3. **迹线提取**：对边缘图像施用 Hough 变换算法，检测直线节理迹线。[Mohebbi 2016, pp. 9-10]
4. **节理组分类**：首先用减法聚类算法（聚类半径从 0.06 逐步增加到 0.5，寻找连续三个半径下簇数不变的结果）确定节理组数量；再用模糊 c-均值（FCM）算法进行隶属度分配。[Mohebbi 2016, pp. 9-10]
5. **三维产状估算**：假设各节理组服从 Fisher 分布，以手动测绘的少量不连续面作为初始近似，利用几何关系计算节理组在出露面上的迹线角度统计；建立误差目标函数（包含均值 μ、标准差 σ 的误差，影响系数 A=0.7, B=0.3, C=0），采用粒子群优化（PSO）反推倾向、倾角、延展性和间距等参数。[Mohebbi 2016, pp. 10-13]

## Key Findings
- 所提方法在 Choghart 铁矿北墙成功应用，获取了多达 14 张图像中多个节理组的几何参数，包括倾向、倾角、连续性（以长度表示）和间距，并给出了各参数的统计分布（正态、对数正态或指数分布）。[Mohebbi 2016, pp. 13-14]
- 方法在评估细微结构时具有很高精度，且数据采集时间远短于传统方法，被建议作为一种实用技术。[Mohebbi 2016, pp. 1-2]
- 结果显示典型节理组倾向集中在某些优势方向，间距多呈对数正态分布，连续性分布多样。[Mohebbi 2016, pp. 13-14]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 在图像 1 中，节理组 1 的倾向平均 174.16°，标准差 45.53°；连续性平均 34.7 cm，标准差 58.2 cm，呈正态分布；间距平均 12.24 cm，标准差 16.16 cm，呈正态分布。 | [Mohebbi 2016, pp. 13-14, Table 2] | 北墙，基于图像处理方法 | 仅列举代表性数据；节理组 2 和 3 的倾向、连续性同样符合正态或对数正态分布。 |
| 在图像 5 中，节理组 1 倾向平均 52.73°，标准差 89.67°；连续性呈对数正态分布，平均 0.76 cm，标准差 4.08 cm；间距同样呈对数正态分布。 | [Mohebbi 2016, pp. 13-14, Table 2] | 北墙，图像 5 | 该图像内存在多个节理组。 |
| 多数图像中，节理组的间距统计分布为对数正态或正态分布，个别为指数分布（如表 2 中图像 2 节理组 4 连续性为指数分布）。 | [Mohebbi 2016, pp. 13-14, Table 2] | 北墙，不同扫描线图像 | 表中标“*”表示未从片段确认其统计分布。 |
| 使用 Canny 边缘检测和滞后阈值 T1=0.5、T2=0.2 提取的节理迹线能有效避免由于碎石、阴影等产生的虚假边界（在聚类阶段被去除）。 | [Mohebbi 2016, pp. 7-9] | 图像预处理之后、聚类之前 | 原文表明聚类阶段可去除不真实边界。 |
| 通过减法聚类和 FCM 能够自动确定节理组数量，并完成软分类。 | [Mohebbi 2016, pp. 9-10] | 基于迹线的方向数据 | 半径逐步增加，组数稳定时判定最终组数。 |

## Limitations
- 研究仅在一个矿山的北墙实施，方法在不同地质条件（如高度风化、植被覆盖严重）的普适性未从索引片段中确认。
- 三维产状估算依赖于 Fisher 分布假设，且需要少量手动测绘数据作为初始化，该假设的适用条件以及初始数据的敏感性未在片段中深入讨论。
- 片段未提供该方法与传统手工测绘在绝对精度、重复性方面的定量对比分析。
- 图像采集要求高分辨率、垂直拍摄及均匀光照，在现场条件受限时可能难以满足。

## Assumptions / Conditions
- 不连续面的方向服从 Fisher 分布，用于由迹线角度反推三维产状的优化过程。[Mohebbi 2016, pp. 10-13]
- 相机拍摄方向垂直于出露面，以减小透视畸变。[Mohebbi 2016, pp. 3-5]
- 使用至少 8 百万像素分辨率、CCD 传感器的相机，可获得足够的细节。[Mohebbi 2016, pp. 3-5]
- 图像受到局部伽马失真影响，可通过最小化由 GLCM 计算的同质性来估计伽马值并校正。[Mohebbi 2016, pp. 5-7]
- 总变分去噪适合保留边缘细节的同时去除噪声，优于线性、中值等简单滤波器。[Mohebbi 2016, pp. 5-7]
- Canny 边缘检测的滞后阈值 T1=0.5、T2=0.2 适用于该研究图像；这些阈值应通过实验选定。[Mohebbi 2016, pp. 7-9]
- 聚类半径的初始值与步长（0.06 至 0.5，步长 0.01）用于自动确定节理组数量；FCM 进一步细化成员隶属度。[Mohebbi 2016, pp. 9-10]
- PSO 优化中，目标函数针对迹线角度的均值、标准差和偏差（偏差权重设为 0，即忽略），权系数 A=0.7, B=0.3。[Mohebbi 2016, pp. 10-13]

## Key Variables / Parameters
- 图像灰度值、局部伽马值 γ [Mohebbi 2016, pp. 5-7]
- GLCM 同质性 Hom [Mohebbi 2016, pp. 5-7]
- Canny 边缘检测阈值 T1=0.5, T2=0.2 [Mohebbi 2016, pp. 7-9]
- Sobel 算子 Gx, Gy；梯度幅值 G 和方向 θ [Mohebbi 2016, pp. 7-9]
- Hough 变换检测的迹线 [Mohebbi 2016, pp. 9-10]
- 减法聚类半径 radi (0.06~0.5) [Mohebbi 2016, pp. 9-10]
- FCM 模糊加权指数 m 与目标函数 J [Mohebbi 2016, pp. 9-10]
- 不连续面三维产状：倾向、倾角、Fisher 分布系数（未从片段中获取具体值）[Mohebbi 2016, pp. 10-13]
- 迹线角度统计量（均值 μ、标准差 σ、偏差 θ），PSO 优化目标函数中系数 A, B, C [Mohebbi 2016, pp. 10-13]
- 节理组几何参数：连续性（cm）、间距（cm）；统计分布类型（正态、对数正态、指数）[Mohebbi 2016, pp. 13-14]

## Reusable Claims
- 对于光照均匀且高分辨率（≥8 MP）的垂直岩壁图像，采用局部 gamma 校正后经全变分去噪，再用 Canny 边缘检测（Sobel 算子，T1=0.5, T2=0.2）能够可靠提取节理迹线，且碎石、阴影等干扰可在后续聚类阶段滤除。[Mohebbi 2016, pp. 3-7]
- 结合 Hough 变换与减法聚类加 FCM 的流水线，可实现二维节理迹线的自动分组，无需预先指定组数，前提是聚类半径的迭代选取方案（从 0.06 到 0.5，步长 0.01）能稳定确定组数。[Mohebbi 2016, pp. 9-10]
- 若已知出露面产状且各节理组服从 Fisher 分布，利用迹线角度统计量（均值与标准差）构建误差函数并通过 PSO 优化，可从二维图像估算节理组的三维倾向与倾角，其中目标函数中均值权重 0.7、标准差权重 0.3、偏差忽略。[Mohebbi 2016, pp. 10-13]
- 基于图像处理的不连续面测绘方法能在作业时间大幅缩短的前提下获得与手工测绘相当的节理组统计分布（如正态、对数正态），适用于类似 Choghart 铁矿的裸露坚硬岩体边坡。[Mohebbi 2016, pp. 1-2, 13-14]

## Candidate Concepts
- [[rock mass discontinuities]]
- [[joint mapping]]
- [[digital image processing]]
- [[edge detection]]
- [[Hough transform]]
- [[fuzzy c-means clustering]]
- [[subtractive clustering]]
- [[particle swarm optimization]]
- [[fracture orientation]]
- [[fracture spacing]]
- [[fracture persistence]]
- [[Fisher distribution]]
- [[scan-line mapping]]
- [[photogrammetric rock mass characterization]]

## Candidate Methods
- [[image smoothing (histogram, total variation denoising)]]
- [[local gamma correction (GLCM-based)]]
- [[Canny edge detector]]
- [[Sobel operator]]
- [[hysteresis thresholding]]
- [[Hough line detection]]
- [[subtractive clustering for orientation grouping]]
- [[fuzzy c-means (FCM) clustering]]
- [[2D trace to 3D orientation estimation using PSO]]
- [[image-based discontinuity mapping workflow]]

## Connections To Other Work
- Assali 等（文献 [12], [13]）提出了结合 3D 点云（LiDAR 或影像匹配）与 2D 图像的“固体图像”概念，本研究的纯图像方法可视为另一条技术路线，均旨在克服传统现场测绘的不足。[Mohebbi 2016, pp. 2-3]
- Nguyen 等（文献 [11]）采用高分辨率数字照片与数字图像相关（DIC）技术来自动追踪和量化不连续面的位移跳跃，本研究则侧重于利用边缘检测和聚类提取几何参数，二者在裂缝的自动描述上互补。[Mohebbi 2016, pp. 2-3]
- 文中综述的其他研究（如基于 SVM 分类器的裂缝检测）表明已有多种利用图像数据的自动裂缝识别途径，但尚无通用的商业解决方案，本研究为此提供了一种实际可用的技术方案。[Mohebbi 2016, pp. 2-3]

## Open Questions
- 该方法在其他岩性、风化程度或尺度下的适用性如何？阈值参数（如 T1、T2、聚类半径）是否具有跨案例的可迁移性？
- 与激光扫描或立体光学相较，纯图像方法在绝对三维精度上的差距有多大？未从索引片段中确认定量对比数据。
- 所假设的 Fisher 分布是否总是成立？若节理簇呈非 Fisher 分布，三维反演的误差将如何变化？
- 未从索引片段中确认该方法对图像分辨率、光照角度和表面湿度的敏感性分析。

## Source Coverage
本页基于 10 个索引片段生成，覆盖了论文的摘要、引言（含文献综述）、方法论全部流程（图像预处理、边缘检测、迹线提取、聚类与三维估算）以及一个主要结果表格（Table 2）。片段包括了方法步骤的详细公式与流程描述，并提供了北墙多组节理的定量数据。缺失内容包括：方法验证部分的详细对比分析可能未完整呈现（片段只给出结果表格，未说明与传统方法对比的绝对精度）、讨论部分的解释不足、以及图 11（不同边缘检测效果对比）等可视化信息未以文本形式提供。
