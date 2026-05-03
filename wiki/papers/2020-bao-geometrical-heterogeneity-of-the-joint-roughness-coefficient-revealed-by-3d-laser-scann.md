---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-bao-geometrical-heterogeneity-of-the-joint-roughness-coefficient-revealed-by-3d-laser-scann"
title: "Geometrical Heterogeneity of the Joint Roughness Coefficient Revealed by 3D Laser Scanning."
status: "draft"
source_pdf: "data/papers/2020 - Geometrical heterogeneity of the joint roughness coefficient revealed by 3D laser scanning.pdf"
collections:
  - "zotero new"
citation: "Bao, Han, et al. \"Geometrical Heterogeneity of the Joint Roughness Coefficient Revealed by 3D Laser Scanning.\" *Engineering Geology*, vol. 265, 2020, 105415, doi:10.1016/j.enggeo.2019.105415."
indexed_texts: "7"
indexed_chars: "33205"
nonempty_source_blocks: "7"
compiled_source_blocks: "7"
compiled_source_chars: "33343"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004156"
coverage_status: "full-index"
source_signature: "820c8fbfa88a2e76f27ce6770dae7b21358bfdff"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T02:50:44"
---

# Geometrical Heterogeneity of the Joint Roughness Coefficient Revealed by 3D Laser Scanning.

## One-line Summary
基于关山铁路隧道31个闪长岩节理样本的三维激光扫描与分形理论计算，揭示了JRC的采样间隔效应、各向异性及同一方向上的对数正态分布规律，并指出概率密度期望值较算术均值更可靠（最大差异23.1%）。

## Research Question
如何准确刻画同一节理组中JRC的几何异质性，包括：
- 剖面线采样间隔与数字点采样间隔对JRC计算值的阈值效应；
- JRC在不同方向上的各向异性特征；
- 同一方向上JRC值的概率分布规律及其对可靠取值方法的影响。

## Study Area / Data
- **采样地点**：甘肃省关山铁路隧道，位于青藏高原东北缘，埋深765 m，最大水平主应力31.35 MPa（N57°E），最小水平主应力17.16 MPa，垂直主应力21.04 MPa [Bao 2020, pp. 1-2]。
- **岩性**：闪长岩，主要矿物为斜长石、角闪石、辉石和黑云母，晶体尺寸0.1–1.5 mm [Bao 2020, pp. 1-2]。
- **节理样本**：同一组31个节理，优势产状209°∠71°，具有明显的压剪破坏特征及剪切擦痕，擦痕方向用于确定0°参考方向 [Bao 2020, pp. 1-2, 2–3]。
- **数字化数据**：手持式三维激光扫描仪（Handyscan 3D）获取点云，分辨率0.05 mm，激光足迹0.04 mm，测量距离约30 cm；提取10 cm×10 cm研究区域 [Bao 2020, pp. 2-3]。

## Methods
1. **节理形态数字化**：利用Geomagic读取初始点云，通过Matlab进行正交网格插值（间距0.05 mm）生成规则点云，截取10 cm长的剖面线 [Bao 2020, pp. 2-3]。
2. **JRC计算**：基于分形理论，使用公式 \( D = \lg 4 / \lg\{2[1+\cos\arctan(2h/L)]\} \) 计算分形维数D，再由转换公式 \( \text{JRC} = 85.2671(D-1)^{0.5679} \) 获得JRC值 [Bao 2020, pp. 2-3]。
3. **采样间隔效应分析**：
   - 剖面线间隔：在0.1 mm至10 mm间选取12种间隔，计算不同间隔下的JRC均值，确定阈值 [Bao 2020, pp. 2-3, 3–5]。
   - 数字点间隔：选取10条粗糙度差异显著的剖面线，在0.1–2 mm间以0.1 mm增量改变采样点间隔，建立JRC与点间隔的关系 [Bao 2020, pp. 3-5]。
4. **分布特性分析**：
   - 以剪切方向为0°，每15°截取剖面线（12个方向），计算31个样本的JRC值，分析各向异性 [Bao 2020, pp. 5-6]。
   - 对各方向上的JRC进行概率统计，拟合对数正态分布，并用Kolmogorov-Smirnov检验（K-S检验）验证（P值均大于0.47） [Bao 2020, pp. 5-8]。
   - 对比最小值、最大值、算术均值与分布函数期望值 [Bao 2020, pp. 5-8]。

## Key Findings
1. **采样间隔阈值**：
   - 剖面线间隔存在4 mm阈值：小于4 mm时JRC值恒定，大于4 mm后明显波动；该阈值与节理粗糙度无关 [Bao 2020, pp. 2-3, 3–5]。
   - 数字点间隔阈值受粗糙度影响，与JRC呈负指数关系：\( y = 1.8314 e^{-0.067x} \)（y为点间隔阈值(mm)，x为JRC）[Bao 2020, pp. 3-5]。
2. **各向异性**：不同方向平均JRC差异显著，最大均值约为最小均值的1.64倍；最小JRC方向与剪切擦痕方向平行 [Bao 2020, pp. 5-6]。
3. **同一方向变异性**：31个样本在同一方向上的JRC值离散性大（均值4.54–7.43，标准差2.09–3.55），但通过K-S检验证实服从对数正态分布；P值随JRC增大而减小，表明高粗糙度削弱分布规律性 [Bao 2020, pp. 5-8]。
4. **可靠取值方法**：概率密度函数期望值系统性地大于算术均值，最大差异达23.1%；期望值反映真实形态信息，取值更合理 [Bao 2020, pp. 5-8]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 剖面线采样间隔阈值4 mm，低于阈值JRC恒定，高于阈值JRC波动；阈值与粗糙度无关 | [Bao 2020, pp. 2-3, 3–5] | 闪长岩节理，10 cm剖面，间隔0.1–10 mm | 适用于本研究对象，其他岩类需验证 |
| 数字点采样间隔阈值与JRC呈负指数关系：\( y = 1.8314 e^{-0.067x} \) | [Bao 2020, pp. 3-5] | 10条粗糙度不同的剖面线，点间隔0.1–2 mm | 拟合关系仅在所测范围内有效 |
| 同一方向31个样本的JRC服从对数正态分布，K-S检验P值>0.47 | [Bao 2020, pp. 5-8] | 闪长岩节理组，12个方向，每个方向31个值 | 高粗糙度时分布规律性减弱(P值减小) |
| JRC各向异性：最大平均JRC为最小平均JRC的1.64倍；最小JRC方向平行于剪切擦痕 | [Bao 2020, pp. 5-6] | 31个样本，方向间隔15° | 表明剪切方向控制JRC分布 |
| 概率密度期望值比算术均值高，最大差异23.1% | [Bao 2020, pp. 5-8] | 所有12个方向 | 期望值被认为更可靠 |

## Limitations
- 研究仅基于关山隧道闪长岩节理组（31个样本），结论推广至其他岩性需谨慎。
- 采样间隔阈值由特定点云密度和插值方法得到，不同扫描分辨率可能影响阈值。
- 对数正态分布的拟合仅在当前样本规模与K-S检验下成立，未考虑节理尺度效应。
- JRC计算依赖分形维数与经验转换公式，其适用性局限于该转换关系。

## Assumptions / Conditions
- 同一节理组因相同形成机制而具有相似的几何分布和力学特性 [Bao 2020, pp. 1-2]。
- 使用Barton标准剖面图标定的分形维数–JRC公式(2) [Bao 2020, pp. 2-3]。
- 剖面线采样间隔阈值4 mm独立于粗糙度，适用于本研究闪长岩节理 [Bao 2020, pp. 3-5]。
- 数字点间隔阈值公式(3)由10条剖面线拟合，可外推至相近粗糙度范围 [Bao 2020, pp. 3-5]。
- 剪切方向根据节理表面擦痕确定，作为0°参考方向 [Bao 2020, pp. 2-3]。

## Key Variables / Parameters
- 剖面线采样间隔 (0.1 mm ~ 10 mm)
- 数字点采样间隔 (0.1 mm ~ 2 mm)
- 节理粗糙度系数 JRC
- 分形维数 D
- 剖面线方向（以15°间隔旋转的12个方向）
- 各方向JRC的算术均值、标准差、最小值、最大值
- 对数正态分布拟合参数及K-S检验P值
- 概率密度期望值（expected JRC）

## Reusable Claims
1. **采样间隔阈值**：对于闪长岩节理，当剖面线取样间隔小于4 mm时，JRC计算值保持恒定，该阈值不受节理粗糙度影响 [Bao 2020, pp. 2-3, 3–5]。  
   *条件*：基于10 cm剖面线、0.05 mm点云分辨率；其他岩石类型和尺度需验证。
2. **点间隔阈值预测**：数字点采样间隔阈值与JRC呈负指数关系，可根据JRC预选合理点间隔以避免计算失真 [Bao 2020, pp. 3-5]。  
   *条件*：适用JRC约4~20范围，点间隔0.1–2 mm。
3. **JRC各向异性**：同一节理组的JRC具有显著方向依赖性，最小JRC方向倾向于平行剪切擦痕，可用于估计最不利抗剪方向 [Bao 2020, pp. 5-6]。  
   *条件*：由压剪性节理组的31个样本得出。
4. **JRC对数正态分布**：同一方向上的JRC值服从对数正态分布，且高粗糙度会降低分布规律性（K-S检验P值减小）[Bao 2020, pp. 5-8]。  
   *条件*：适用于同组节理，样本量≥31；其他节理组应进行统计检验。
5. **期望值取值方法**：采用概率密度期望值代替算术均值可得到更可靠的JRC代表值，二者差异可达23.1% [Bao 2020, pp. 5-8]。  
   *条件*：需要先验证分布类型（此处为对数正态）。

## Candidate Concepts
- [[Joint Roughness Coefficient (JRC)]]
- [[Fractal Dimension]]
- [[3D Laser Scanning]]
- [[Sampling Interval Effect]]
- [[Anisotropy of JRC]]
- [[Log-normal Distribution of JRC]]
- [[Joint Group]]
- [[Probability Density Function]]
- [[Kolmogorov-Smirnov Test]]
- [[Shear Strength of Rock Joints]]
- [[Geomagic Point Cloud Processing]]
- [[Guanshan Railway Tunnel]]

## Candidate Methods
- [[Fractal Theory for JRC Calculation]]
- [[Handheld 3D Laser Scanning]]
- [[Profile Line Interception and Sampling]]
- [[Orthogonal Grid Interpolation for Point Clouds]]
- [[Threshold Determination of Sampling Interval]]
- [[K-S Test for Distribution Fitting]]
- [[Expected Value from Probability Density Function]]
- [[Anisotropic Analysis of JRC by Directional Profiles]]

## Connections To Other Work
- JRC概念源于Barton (1973)及Barton和Choubey (1977)的剪切强度准则；准确获取JRC是预测抗剪强度的前提 [Bao 2020, pp. 1-1]。
- 分形理论在节理粗糙度表征中的应用延续了Carr和Warriner (1989)、Xie和Pariseau (1994)等的工作，本文采用的分形维数与JRC关系即基于后者 [Bao 2020, pp. 1-1, 2–3]。
- 三维激光扫描技术（Fardin et al., 2001; Assali et al., 2014; Azinfar et al., 2019）和点云处理（Jiang et al., 2016）为本研究提供了高精度形态数据 [Bao 2020, pp. 1-2]。
- 采样间隔对分形维数的影响曾被Lee et al. (1990)、Bae et al. (2011)、Xia et al. (2014)等指出，本文进一步明确了阈值 [Bao 2020, pp. 1-2]。
- JRC各向异性研究（Chen et al., 2016; Wang et al., 2019; Yang et al., 2001）和概率分布研究（Dong et al., 2015; Kim et al., 2015; Luo et al., 2016）提供了背景，本文推进了对同一节理组内分布规律的认知 [Bao 2020, pp. 1-2, 5–8]。

## Open Questions
- 剖面线间隔阈值4 mm是否适用于其他岩性（如沉积岩、变质岩）及更大尺度的节理面？
- 数字点间隔阈值公式\( y = 1.8314 e^{-0.067x} \)是否具备普适性？能否通过物理机制（如粗糙度分级）加以解释？
- 对数正态分布能否描述所有节理组的JRC分布？分布参数（均值、方差）与地质因素（如应力历史、矿物成分）如何关联？
- 采用概率密度期望值代替算术均值后，对实际工程中节理岩体剪切强度评价的影响有多大？是否需要现场验证？
- 如何将各向异性和分布规律纳入随机节理网络模拟，以改进渗流和稳定性分析？

## Source Coverage
所有7个非空索引片段均已处理，覆盖率为100%。  
- 索引文本块数：7  
- 编译源块数：7  
- 覆盖字符比：1.004（编译字符33343 vs. 索引字符33205）  
- 源签名：820c8fbfa88a2e76f27ce6770dae7b21358bfdff，编译策略为单次通过markdown。
