---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2014-voorn-porosity-permeability-and-3d-fracture-network-characterisation-of-dolomite-reservoir"
title: "Porosity, Permeability and 3D Fracture Network Characterisation of Dolomite Reservoir Rock Samples."
status: "draft"
source_pdf: "data/papers/2015 - Porosity, permeability and 3D fracture network characterisation of dolomite reservoir rock samples.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Voorn, Maarten, et al. \"Porosity, Permeability and 3D Fracture Network Characterisation of Dolomite Reservoir Rock Samples.\" *Journal of Petroleum Science and Engineering*, 2014, doi:10.1016/j.petrol.2014.12.019. Accessed 1 Jan. 2026."
indexed_texts: "19"
indexed_chars: "92032"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T19:24:50"
---

# Porosity, Permeability and 3D Fracture Network Characterisation of Dolomite Reservoir Rock Samples.

## One-line Summary
利用非破坏性3D X射线微计算机断层扫描（μCT）结合多尺度Hessian裂缝滤波技术，对7个取自奥地利维也纳盆地白云岩地层的岩塞样品进行孔隙度、裂缝孔径、密度和方向提取，并配合薄片观察与围压渗透率实验，探索裂缝型储层岩石的多尺度表征方法 [Voorn 2014, pp. 1-1, 2-3]。

## Research Question
如何有效分析致密白云岩储层岩样中的天然裂缝网络？研究重点在于运用3D μCT成像与Hessian滤波手段，克服传统2D和破坏性方法的局限，获取孔隙度、裂缝孔径、裂缝密度和方向等关键参数，并结合实验室渗透率测定，为裂缝储层建模提供输入 [Voorn 2014, pp. 1-1, 2-3]。

## Study Area / Data
- **地质背景**：上三叠统（诺利阶）Hauptdolomit组白云岩，采自奥地利维也纳盆地基底井筒 [Voorn 2014, pp. 2-3]。
- **样品**：7个直径约2 cm的岩塞样品（另有一些更大尺寸岩心尝试扫描但未成功），深度可达3320 m [Voorn 2014, pp. 3-5]。
- **断层岩类型**：样品覆盖从损伤带到断层核的序列，包括非面理化损伤带角砾岩、含方解石胶结的过渡带角砾岩以及胚胎级至成熟级碎裂岩（基质含量<50%至>80%），分类主要作为区分手段，非确定层位推断 [Voorn 2014, pp. 3-3, 3-5]。
- **补充薄片数据**：为获得更高分辨率信息，对部分样品制备薄片，使用SEM-BSE图像拼接，分辨率达1.45 μm/像素 [Voorn 2014, pp. 6-6]。

## Methods
- **3D μCT扫描**：使用Rayscan 250E系统，225 kV微焦点X射线管，重建体素分辨率约12.5 μm或18.9 μm，扫描均在表面/无围压条件下进行 [Voorn 2014, pp. 3-5]。
- **裂缝与孔隙分割**：采用多尺度Hessian裂缝滤波器（MSHFF）增强面状特征，再经二值分割分离孔隙与裂缝空间，该滤波器由Voorn et al. (2013)引入 [Voorn 2014, pp. 1-1, 3-5]。
- **孔隙度计算**：基于分割数据的体素计数（孔隙体素/总体素×100%），结果受分辨率与分割算子选择影响 [Voorn 2014, pp. 5-6]。
- **裂缝孔径分布**：使用FIJI的Local Thickness插件，在已分割的裂缝网络上计算整体孔径分布，替代难以应用于复杂网络的物理校准方法 [Voorn 2014, pp. 5-6]。
- **裂缝方向分析**：对分割数据重新计算Hessian矩阵，取最大特征值对应的特征向量作为裂缝面法向，经Kalsbeek网格密度等值线绘制归一化立体投影图，大裂缝自动获得更高权重 [Voorn 2014, pp. 6-6]。
- **薄片分析**：制备SEM-BSE拼接图像，用Otsu全局阈值法计算二维孔隙度，以对照并补充μCT缺失的微孔隙与基质信息 [Voorn 2014, pp. 6-8]。
- **渗透率实验**：在室温下对直径2 cm岩塞施加围压（蒸馏水为围压介质），以氮气为孔隙流体测定表观渗透率，采用达西定律的压缩气体形式：  
  `κapp = (μ dx / A) * Q / ( (Pup² - Pdown²) / (2 Pdown) )`，  
  其中κapp为表观渗透率[m²]，μ为流体动力黏度[Pa·s]，dx为样品长度[m]，A为截面积[m²]，Q为流量，Pup、Pdown分别为上下游压力 [Voorn 2014, pp. 6-8]。

## Key Findings
未从索引片段中确认具体定量结果。片段仅呈现方法学描述、图像处理流程和实验设置，未涉及所有7个样品的孔隙度、裂缝密度、孔径分布均值或渗透率数值，亦未给出围压敏感性分析。其核心方法贡献在于证明了MSHFF可从μCT数据中成功提取狭窄裂缝网络、计算局部孔径和方向分布，但数据定量结论在本索引中缺失。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| MSHFF分割可有效提取致密白云岩µCT数据中的狭窄裂缝网络。 | [Voorn 2014, pp. 3-5, 5-6] | 体素分辨率12.5–18.9 μm；X射线能量225 kV；扫描样品为Hauptdolomit组白云岩塞。 | 基于Voorn et al. (2013)的滤波器；分割操作存在主观性。 |
| 利用Hessian特征向量可构建裂缝面法向立体投影，且大裂缝体素贡献权重更大。 | [Voorn 2014, pp. 6-6] | 应用于分割后的裂缝网络；投影密度归一化至统一最大值。 | 缺乏井筒方位信息，所得方向仅为相对结果。 |
| 使用Local Thickness方法可获得全样裂缝孔径分布，避免单条裂缝分离困难。 | [Voorn 2014, pp. 5-6] | FIJI Local Thickness插件；工作于已分割的裂缝体素数据。 | 孔径值受分割偏差影响；无法分离连通与非连通孔隙。 |
| 氮气渗透率实验可在围压下进行，并应用达西定律计算表观渗透率。 | [Voorn 2014, pp. 6-8] | 室温；围压介质为蒸馏水；孔隙流体为氮气；样品直径2 cm。 | 公式见于文献，片段未提供滑脱效应校正信息。 |
| 薄片SEM-BSE拼接与Otsu阈值可提供更高分辨率的2D孔隙度参考。 | [Voorn 2014, pp. 6-8] | 分辨率1.45 μm/像素；对比μCT切片显示大量小孔隙和基质细节。 | 只能获得2D信息，且制样具破坏性。 |

## Limitations
- μCT分辨率（12.5–18.9 μm/体素）不足以探测微孔隙，分割结果高度依赖于滤波和阈值选择 [Voorn 2014, pp. 5-6]。
- 断层带分类基于岩心观察和薄片解释，具有推断性，并非确定结构位置 [Voorn 2014, pp. 3-3]。
- 采样仅选取含有足够孔隙度和裂缝、且不易碎裂的样品，可能引入偏差 [Voorn 2014, pp. 3-3]。
- 无法完全排除钻井诱导裂缝，尽管未观察到典型特征 [Voorn 2014, pp. 3-3]。
- 裂缝方向分析缺少井筒方位参考，结果仅为相对方向 [Voorn 2014, pp. 6-6]。
- 渗透率实验在室温表面条件下进行，未模拟地层温度和流体，气体渗透率可能受滑脱效应影响，但索引片段未讨论 [Voorn 2014, pp. 6-8]。
- 对大尺寸（6–10 cm）岩心无法在维持分辨率的条件下实现充分X射线穿透，限制了尺度升级 [Voorn 2014, pp. 3-5]。

## Assumptions / Conditions
- μCT扫描和图像分割均在样品无围压的表面条件下进行，所获几何参数反映卸载状态下的特征 [Voorn 2014, pp. 3-5]。
- 基于Hessian的滤波假设裂缝表现为局部面状结构，通过多尺度高斯平滑增强不同宽度的面形特征 [Voorn 2014, pp. 3-5]。
- 裂缝分割采用全局二值化方法，假设孔隙/裂缝相与基质存在足够的密度对比，且分割阈值能够代表真实孔隙空间 [Voorn 2014, pp. 5-6]。
- 方向分析中隐含假定裂缝面法向的不确定性主要由数据噪声控制，可通过重新计算分割后数据的Hessian矩阵降低影响 [Voorn 2014, pp. 6-6]。
- 渗透率计算基于达西定律，假定流动为层流且流体为压缩性理想气体；实验中围压均匀施加于样品侧面 [Voorn 2014, pp. 6-8]。

## Key Variables / Parameters
- **扫描参数**：体素尺寸（12.5、18.9 μm），X射线管电压（225 kV）。[Voorn 2014, pp. 3-5]
- **图像处理参数**：高斯分析尺度（多尺度组合，未指定具体值）。[Voorn 2014, pp. 5-6]
- **孔隙度**（%）：基于分割后体素统计的宏观孔隙度。[Voorn 2014, pp. 5-6]
- **裂缝孔径**（μm）：局部厚度法给出的孔径分布，全样本统计。[Voorn 2014, pp. 5-6]
- **裂缝方向**：法向向量，立体投影密度最大值归一化因子。[Voorn 2014, pp. 6-6]
- **渗透率**：表观渗透率κapp [m²]，样品长度dx，截面积A，上下游压力Pup、Pdown，气体动力黏度μ。[Voorn 2014, pp. 6-8]
- **围压水平**：未从索引片段中确认具体数值或范围。
- **断层岩分类指标**：基质含量（<50%, 50–80%, >80%）及基质-颗粒界限（4 μm）。[Voorn 2014, pp. 3-3]

## Reusable Claims
- **Claim 1**：对于致密碳酸盐岩，采用多尺度Hessian裂缝滤波器（MSHFF）能从12–19 μm/体素分辨率的μCT数据中分割出与人工识别相符的裂缝网络，使得后续的体素级定量分析成为可能；该方法无需物理校准样品，但分割可靠性依赖于裂缝与基质的密度差异以及算子的阈值设定 [Voorn 2014, pp. 3-5, 5-6]。
- **Claim 2**：在无法分离单条裂缝的复杂网络中，利用Hessian特征向量分析可生成加权裂缝方向分布（大裂缝贡献更大），其立体投影结果适合样本间相对比较，但需注意缺乏地理参考的情况下只能提供相对方位 [Voorn 2014, pp. 6-6]。
- **Claim 3**：对分割后的裂缝体应用Local Thickness算法，可获得代表裂缝开度的厚度分布，该方法避免了为每条裂缝指派单一孔径的难题，但所得孔径值受分割精度与局部几何影响，需辅以高分辨方法（如薄片）验证 [Voorn 2014, pp. 5-6]。
- **Claim 4**：小直径（2 cm）白云岩岩塞的围压气体渗透率实验，可按达西定律压缩气体形式进行计算，配合氮气作为孔隙流体可以快速获得表观渗透率；该设置适用于比较不同围压下的渗透率变化，但未考虑气体滑脱效应和原位温度环境 [Voorn 2014, pp. 6-8]。
- **Claim 5**：将μCT与薄片SEM-BSE拼接图像结合，可在多尺度上评估孔隙系统：μCT揭示宏观裂缝网络和较大孔隙，薄片显示微孔隙、基质结构和矿物胶结，从而弥补单一成像方法的不足 [Voorn 2014, pp. 6-8]。

## Candidate Concepts
- [[fracture reservoir]]
- [[dolomite hydrocarbon reservoir]]
- [[fault zone architecture (damage zone, transition zone, fault core)]]
- [[cataclasite classification]]
- [[micro-computed tomography (μCT)]]
- [[Hessian-based filtering]]
- [[stereographic projection for fractures]]
- [[confining pressure permeability test]]
- [[apparent gas permeability]]

## Candidate Methods
- [[multiscale Hessian fracture filter (MSHFF)]]
- [[Local Thickness analysis]]
- [[Otsu thresholding on SEM-BSE images]]
- [[Darcy's law for compressible gas]]
- [[Kalsbeek grid density contouring]]
- [[thin section SEM-BSE stitching]]

## Connections To Other Work
- 本文所用的核心滤波方法直接来源于Voorn et al. (2013)的MSHFF技术，针对面状特征提取进行了优化 [Voorn 2014, pp. 3-5]。
- 文献中提到多种μCT孔径校准方法（如Ketcham等人的PSF拟合），但因复杂网络应用困难而未被采用；本文的Local Thickness方法可视为一种替代方案，可连接至 [[CT-based fracture aperture calibration]] 的相关工作 [Voorn 2014, pp. 5-6]。
- 围压渗透率实验设计参考了Heap et al. (2014)的装置示意图，连接至 [[laboratory permeability measurement on tight rocks]] 领域 [Voorn 2014, pp. 6-8]。
- 裂缝性碳酸盐岩储层表征可与类似的μCT研究（如Christe 2009; Barnhoorn et al. 2010; Jia et al. 2013等）进行比较，但索引片段未提供直接定量对比 [Voorn 2014, pp. 2-3]。

## Open Questions
- 在围压条件下岩石的原位裂缝开度和连通性如何变化？能否发展围压下的同步成像技术？未从索引片段中确认。
- MSHFF滤波器在不同岩性（如含高密度矿物或高孔隙度背景）中的泛化能力未经验证，其参数自动化选择策略仍未明确。
- 裂缝网络的连通性和流体流动模拟所需的全张量渗透率如何从分割体素中推导？索引片段未涉及。
- 钻井卸载和样品制备对微观裂纹的影响程度及校正方法未被量化。
- 气体渗透率与液测渗透率的差异（如滑脱效应）未在片段中讨论，其对储层评价的影响有待评估。

## Source Coverage
本页依据索引中的19个片段撰写，这些片段主要覆盖论文的引言、地质背景、部分样品描述、μCT处理与分析流程、薄片方法介绍和渗透率实验设置。缺少全部定量结果、讨论与结论章节，因此有关孔隙度值、渗透率-围压关系曲线、裂缝密度与方向统计学结果、方法对比及储层应用意义等内容均为空白。页面偏重技术路线与方法学，关键科研证据（实测数据与图表）未能反映，致使核心发现和验证性声明严重不完整。
