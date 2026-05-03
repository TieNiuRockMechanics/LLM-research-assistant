---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2025-liu-revisiting-each-fracture-size-and-spatial-pattern-inference-from-rock-mass-surface-to-i"
title: "Revisiting Each Fracture Size and Spatial Pattern: Inference from Rock Mass Surface to Interior."
status: "draft"
source_pdf: "data/papers/2025 - Revisiting each fracture size and spatial pattern Inference from rock mass surface to interior.pdf"
collections:
  - "zotero new"
citation: "Liu, Yongqiang, et al. \"Revisiting Each Fracture Size and Spatial Pattern: Inference from Rock Mass Surface to Interior.\" *Journal of Rock Mechanics and Geotechnical Engineering*, vol. 17, 2025, p. 1399, doi:10.1016/j.jrmge.2024.08.026."
indexed_texts: "14"
indexed_chars: "68092"
nonempty_source_blocks: "14"
compiled_source_blocks: "14"
compiled_source_chars: "68377"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004186"
coverage_status: "full-index"
source_signature: "390c15eef3a0219295d27c0bca5e67a1569281c1"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T08:40:22"
---

# Revisiting Each Fracture Size and Spatial Pattern: Inference from Rock Mass Surface to Interior.

## One-line Summary
本文提出一种渐进框架与反演方法，从矩形采样窗内的包含迹线数据推断每条裂缝的最可能直径（MPD）及其在岩体内部的真实空间分布模式。[Liu 2025, pp. 1-1]

## Research Question
核心问题：如何从岩体表面迹线推断每条裂缝的尺寸（最可能直径，MPD）与真实空间展布形态？该问题面临两大挑战：一是推断过程需同时依赖单条裂缝的迹长与整个露头的统计特征；二是裂缝尺寸分布的反演属于典型非唯一性问题。[Liu 2025, pp. 1-2][Liu 2025, pp. 2-3]

## Study Area / Data
研究数据包含两部分：
- **蒙特卡洛模拟案例**：生成域50 m × 50 m × 50 m，体密度P30=0.04 m⁻³，裂缝方位服从Fisher分布（倾向200°±2°，倾角25°±2°），直径D服从对数正态分布log N(1.6, 0.4²)，Dmin=1 m，Dmax=13 m。设置三个平行于XZ平面的切割面（Y=10 m, 25 m, 40 m）模拟露头迹线，仅保留包含迹线（contained traces）。后续补充三个不同走向的采样窗以扩展验证。[Liu 2025, pp. 8-10]
- **实际工程案例**：西藏昌都市察达村某高陡岩质边坡，属青藏高原东南缘，发育砂质板岩典型裂隙化岩体。于高分辨率三维岩体表面模型上选取80 m × 50 m垂直矩形采样窗，利用半自动解译技术获取大于0.5 m的迹线47条，优势组平均倾向235.4°、平均倾角66.2°。[Liu 2025, pp. 11-14]

## Methods
方法体系为包含四个步骤的渐进框架及后续反演：
1. **数据准备**：采用ISOAP算法划分裂隙组，仅取包含迹线（完全可见的迹长）以避免删失偏差，并设定0.5 m截断阈值处理截断偏差。[Liu 2025, pp. 3-5][Liu 2025, pp. 14-16]
2. **真迹长分布f(l)估计**：利用向量法校正方位偏差（实际频率Afi通过权重Wi求取，提前假定di为平均迹长的120%）。随后用多扫描线法（扫描线数量m=2N₂+N₁）推导真迹长均值ml，通过包含迹长分布的变异系数COVc估计f(l)的标准差sl（sl=ml·sc/mc），并用KS检验确定最优分布模型。[Liu 2025, pp. 5-8]
3. **直径分布g(D)推断**：假设g(D)服从对数正态分布，基于迹长与直径的高阶矩关系推导出mD和sD；利用Crofton定理验证该假设，即计算相对误差RE<5%则接受对数正态假设。[Liu 2025, pp. 6-8]
4. **MPD求解**：固定sD后，通过联合迹长l和直径分布的概率密度面拟合，确定每条裂缝的唯一MPD，并用经验线性公式简化计算。[Liu 2025, pp. 3-5][Liu 2025, pp. 10-11]
5. **空间模式反演**：由裂缝的方位、MPD、迹线端点及中点，借助向量叉积和模长关系计算真实圆心位置O_i，从而实现每条裂缝的空间定位。[Liu 2025, pp. 8]

## Key Findings
- **MPD预测性能**：蒙特卡洛三切面的平均绝对误差MAE约1 m，平均绝对百分比误差MAPE约20%（如Y=25 m切面MAE=1.211 m，MAPE=20.1%）。引入0.5 m截断偏差后，预测性能提升（MAE降至1.017–1.13 m，MAPE降至17.9%–18.6%）。[Liu 2025, pp. 10-11][Liu 2025, pp. 16-18]
- **迹长‑直径线性关系**：同一露头内迹长l与MPD呈高度线性相关（R²=0.9998），如Y=25 m时MPD=1.034l+0.909。这种关系在删除D>3l的极端值后仍显著，反映了天然裂缝的尺寸效应。[Liu 2025, pp. 10-11][Liu 2025, pp. 16-18]
- **反演空间模式可靠性**：利用MPD反演的裂缝空间分布模式与蒙特卡洛真实三维模型高度相似，表明方法可有效恢复岩体内部裂缝格局。[Liu 2025, pp. 11]
- **工程实例验证**：边坡采样窗反演所得空间模式与三维点云模型叠合后，清晰展示了原位裂缝的延展性；MPD服从对数正态分布（p=0.105），与g(D)假设一致。[Liu 2025, pp. 14-16]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| Y=25 m切面真迹长均值ml=5.111 m，包含迹长均值mc=4.534 m，标准差sc=2.248 m，sl=2.534 m | [Liu 2025, pp. 8-10] 表1 | 仅用包含迹线，多扫描线法+向量法校正 | 为后续推导mD和sD提供基础 |
| 三切面c(l)最优分布均为Gamma分布（p值0.036、0.025、0.019） | [Liu 2025, pp. 8-10] 表2 | KS检验，显著性水平0.05 | f(l)假设与c(l)同分布 |
| 推导的g(D)参数：Y=25 m时mD=5.645 m，sD=2.206 m；Crofton定理验证RE=0.217% | [Liu 2025, pp. 10] 表3 | 假设g(D)对数正态，RE<5% | 通过验证，确保MPD可靠 |
| 三切面MPD预测MAE约1 m，MAPE约20%；含截断偏差后MAE~1.1 m，MAPE~18% | [Liu 2025, pp. 10-11] 表4；[Liu 2025, pp. 16-18] 表6 | 与真实模拟直径对比 | 精度满足工程应用 |
| 边坡实例：ml=12.942 m，mD=14.082 m，sD=5.808 m，RE=3.804% | [Liu 2025, pp. 11-14] | 47条迹线，优势组 | 对数正态假设成立 |
| 边坡MPD‑l经验关系MPD=1.05l+2.1 | [Liu 2025, pp. 14] 图15a | 0.5 m截断 | 简化工程计算 |

## Limitations
- MPD预测的MAE约1 m、MAPE约20%，对于高精度要求仍显不足，未来需进一步提升。[Liu 2025, pp. 16-18]
- 方法基于圆盘假设，虽可为其他形状提供参考，但未直接扩展至椭圆等其他模型。[Liu 2025, pp. 2-3]
- 仅考虑包含迹线，舍弃了大量贯穿和半贯穿迹线，可能损失部分信息。[Liu 2025, pp. 3-5]
- 蒙特卡洛模拟可能未完全复现大裂缝因露头相交形成短迹线的现象，导致个别大直径裂缝预测误差较大。[Liu 2025, pp. 14-16]
- 实际工程中迹线测量存在分辨率依赖和连接合并问题，文中仅通过几何简化处理。[Liu 2025, pp. 1-2]

## Assumptions / Conditions
- 裂缝形状为无厚度的圆盘，直径表示尺寸。[Liu 2025, pp. 2-3]
- 裂缝直径分布假设为对数正态分布，并由Crofton定理验证（RE<5%）。[Liu 2025, pp. 6-8]
- 真迹长分布f(l)与包含迹长分布c(l)具有相同变异系数COV和分布形式。[Liu 2025, pp. 6]
- 采用多扫描线法时，假定扫描线数量m=2N₂+N₁，且内部裂缝效应可忽略。[Liu 2025, pp. 5-6]
- 方位校正时，因直径未知，暂设所有裂缝直径为平均迹长的120%。[Liu 2025, pp. 5]
- 截断偏差阈值为0.5 m（小于该长度的迹线忽略）。[Liu 2025, pp. 14-16]

## Key Variables / Parameters
- D：裂缝直径随机变量；g(D)：直径分布；lD、xD：对数直径的均值与标准差；mD、sD：直径的均值与标准差。[Liu 2025, pp. 2-3]
- l：迹长；f(l)：真迹长分布；g(l)：实测迹长分布；c(l)：包含迹长分布；ml、sl：真迹长均值与标准差；mc、sc：包含迹长均值与标准差。[Liu 2025, pp. 6][Liu 2025, pp. 3-5]
- N0、N1、N2：贯穿、半贯穿、包含迹线条数；R0=N0/N，R2=N2/N。[Liu 2025, pp. 3-5]
- w、h：采样窗宽度与高度；W_i：方位权重；Af_i：校正后实际频率。[Liu 2025, pp. 5]
- Cm：与扫描线相交迹线期望数相关的统计参数。[Liu 2025, pp. 5-6]
- hD：指数分布参数；tD、yD：Gamma分布的形状与逆尺度参数；RE：相对误差。[Liu 2025, pp. 3-5][Liu 2025, pp. 8]
- MPDi：第i条裂缝的最可能直径；Oi：裂缝真实中心位置。[Liu 2025, pp. 2-3][Liu 2025, pp. 8]
- P30：单位体积裂缝条数。[Liu 2025, pp. 8-10]
- MAE、MAPE：预测性能指标。[Liu 2025, pp. 10-11]

## Reusable Claims
- **基于包含迹长的MPD推断**：若裂缝直径服从对数正态分布，且通过Crofton定理验证（RE<5%），则可利用包含迹长的统计特征（ml、sl）推导出sD，进而结合单条迹长l唯一确定其MPD。条件：仅适用于矩形采样窗内的包含迹线；需先使用ISOAP等算法划分裂隙组；迹长截断阈值为0.5 m。来源：[Liu 2025, pp. 6-8][Liu 2025, pp. 10-11]
- **COV传递假设**：在显著删失偏差下，用包含迹长分布c(l)的COV代替真迹长分布f(l)的COV，可以获得更准确的标准差估计。条件：采样窗尺寸相仿或大于裂缝尺寸；包含迹线数量充足。来源：[Liu 2025, pp. 6]
- **迹长‑直径线性关系**：同一露头内，MPD与迹长l存在强线性关系（如MPD≈1.034l+0.909），可快速估算裂缝尺寸。限制：关系式依赖于sD，不同露头需重新拟合；当D>3l的异常点需剔除。来源：[Liu 2025, pp. 10-11][Liu 2025, pp. 16-18]
- **空间模式反演**：基于裂缝方位、MPD、迹线端点，可计算出裂缝圆盘在岩体内的真实位置，实现从表面迹线到场内三维展布的反演。条件：裂缝假定为圆盘；圆盘中心需位于岩体内部（即选择内侧解）。来源：[Liu 2025, pp. 8]
- **截断偏差的正面效应**：实际工程中设定0.5 m截断偏差，既能符合地质调查惯例，又能提升MPD预测精度（MAE降低约6%）。来源：[Liu 2025, pp. 14-16]

## Candidate Concepts
- [[most probable diameter (MPD)]]
- [[contained trace length]]
- [[rectangular sampling window]]
- [[orientation bias correction]]
- [[multi-scanline method]]
- [[lognormal diameter distribution]]
- [[Crofton's theorem]]
- [[non-unique inverse problem]]
- [[spatial pattern inversion]]
- [[truncation bias]]
- [[censoring bias]]
- [[size bias]]
- [[fracture set identification (ISOAP)]]
- [[coefficient of variation (COV)]]
- [[KS test]]

## Candidate Methods
- [[vector method for orientation correction]]
- [[multi-scanline mean trace length estimation]]
- [[KS test for distribution selection]]
- [[Crofton's theorem validation]]
- [[higher-order moment relationship (trace vs diameter)]]
- [[probability density surface fitting for MPD]]
- [[spatial geometric inversion (cross product, vector modulus)]]
- [[Monte Carlo fracture network simulation]]
- [[semi-automatic trace interpretation on 3D point clouds]]

## Connections To Other Work
- 传统裂缝尺寸估计多关注分布统计参数（如Pahl, 1981; Kulatilake and Wu, 1984a; Villaescusa and Brown, 1992; Zhang and Einstein, 2000; Zhu et al., 2014），本文则首次提供单条裂缝MPD的确定方法。[Liu 2025, pp. 1-2]
- 多扫描线法源自Zhang et al. (2016a)，解决矩形窗内包含迹长均值估计问题。[Liu 2025, pp. 5-6]
- 矢量法方位校正基于Kulatilake and Wu (1984b)。[Liu 2025, pp. 5]
- Crofton定理在裂缝尺寸推断中的应用参考了Lyman (2003)、Zhang and Einstein (2000)等人的工作。[Liu 2025, pp. 6-8]
- 包含迹长COV与真迹长COV的等价性由Zhan et al. (2022)证实。[Liu 2025, pp. 6]
- 裂隙组划分采用ISOAP算法（Liu et al., 2022）。[Liu 2025, pp. 8][Liu 2025, pp. 11-14]
- 圆盘假设沿袭Shanley and Mahtab (1976)、Baecher and Lanney (1978)等经典模型。[Liu 2025, pp. 2-3]

## Open Questions
- 如何进一步提高MPD的预测精度，特别是对于大直径小迹线的异常情形？[Liu 2025, pp. 14-16]
- 若裂缝形状为椭圆或更一般的多边形，现有的MPD推断框架能否推广？[Liu 2025, pp. 2-3]
- 当包含迹线数量不足时，如何有效利用贯穿和半贯穿迹线参与MPD估计？[Liu 2025, pp. 3-5]
- 尺寸偏差在蒙特卡洛模拟中未能完全复现真实露头现象，改进模拟策略能否提升验证可信度？[Liu 2025, pp. 14-16]
- 将MPD引入运动学分析与块体理论时，有限块体识别的可靠性如何定量评价？[Liu 2025, pp. 1-2][Liu 2025, pp. 16-18]

## Source Coverage
所有14个非空索引片段均被本页面处理并引用。索引字符数68,092，编译后源字符数68,377，片段覆盖率（按块）100%，按字符覆盖率100.42%。未使用任何片段外信息。片段签名：390c15eef3a0219295d27c0bca5e67a1569281c1。
