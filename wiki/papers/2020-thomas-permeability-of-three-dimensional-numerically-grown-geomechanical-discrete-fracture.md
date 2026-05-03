---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-thomas-permeability-of-three-dimensional-numerically-grown-geomechanical-discrete-fracture"
title: "Permeability of Three-Dimensional Numerically Grown Geomechanical Discrete Fracture Networks With Evolving Geometry and Mechanical Apertures."
status: "draft"
source_pdf: "data/papers/2020 - Permeability of Three-Dimensional Numerically Grown Geomechanical Discrete Fracture Networks With Evolving Geometry and Mechanical Apertures.pdf"
collections:
citation: "Thomas, Robin N., et al. \"Permeability of Three-Dimensional Numerically Grown Geomechanical Discrete Fracture Networks With Evolving Geometry and Mechanical Apertures.\" *Journal of Geophysical Research: Solid Earth*, vol. 125, no. 7, 2020, e2019JB018899. doi:10.1029/2019JB018899."
indexed_texts: "22"
indexed_chars: "106579"
nonempty_source_blocks: "22"
compiled_source_blocks: "22"
compiled_source_chars: "107075"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004654"
coverage_status: "full-index"
source_signature: "40ccfd597a202e09047f1d602aafa1e75285a421"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T03:27:34"
---

# Permeability of Three-Dimensional Numerically Grown Geomechanical Discrete Fracture Networks With Evolving Geometry and Mechanical Apertures.

## One-line Summary
利用有限元线弹性断裂力学方法生成三维地质力学离散裂缝网络（GDFN），并在生长过程中评估其等效渗透率张量，揭示机械生长过程中裂缝相互作用对网络几何与水力特性的控制，相比随机DFN，GDFN表现出显著各向异性和应力诱导渗透率特征。[Thomas 2020, pp. 1-1]

## Research Question
- 机械过程如何影响三维裂缝网络的几何形态与渗透率演化？[Thomas 2020, pp. 1-1]
- 与基于随机方法的离散裂缝网络（SDFN）相比，地质力学裂缝网络（GDFN）的水力特性（尤其等效渗透率张量）有何差异？[Thomas 2020, pp. 2-3]
- 均匀裂缝开度与基于力学原理的开度分布对流体流动和等效渗透率的影响如何？[Thomas 2020, pp. 1-1]

## Study Area / Data
- 数值模拟域为20 m×20 m×20 m的立方体，材料参数选用硬岩（如花岗岩、花岗闪长岩）相关值，以贴近放射性废物处置等深部应用。[Thomas 2020, pp. 3-5][Thomas 2020, pp. 9-11]
- 生成了六组地质力学裂缝网络（GDFN A–F），初始裂缝数量分别为30、60、90，初始裂缝包含水平裂缝（半径0.5 m，法向量(0,0,1)）和倾斜裂缝（半径2.5 m，法向量(4,5,1)），随机分布在域中央区域。[Thomas 2020, pp. 9-11]
- 对比分析采用两组随机DFN：SDFN Set 1（各向同性，固定半径4.3 m）和SDFN Set 2（各向异性，与GDFN初始定向比例一致）。[Thomas 2020, pp. 13-14]
- 数据与数值结果可通过国家地球科学数据中心获取（Thomas et al., 2020a）。[Thomas 2020, pp. 22-22]

## Methods
1. **地质力学裂缝生长**：采用Imperial College Geomechanics Toolkit (ICGT)，基于线弹性断裂力学，从初始缺陷出发，在单轴远场拉应力（顶部施加2×10^6 Pa，底部固定，其他面牵引自由）下准静态生长。[Thomas 2020, pp. 3-5]
   - **离散化**：八叉树网格自动生成，裂缝尖端用20个尖端节点离散，采用二次等参四面体（体积）和三角形（表面）单元。[Thomas 2020, pp. 3-5]
   - **变形求解**：线弹性各向同性本构，有限元求解应力与位移。[Thomas 2020, pp. 5-6]
   - **应力强度因子（SIF）计算**：位移相关法（DC）计算三种模态SIF（K_I, K_II, K_III），并用NURBS平滑尖端SIF分布。[Thomas 2020, pp. 5-6]
   - **生长准则**：混合模态比较SIF K_v（公式3）达到材料断裂韧性K_IC时裂缝扩展；扩展角ψ用Richard准则（公式4）；扩展长度由修正的两步Paris型法则分配（公式6、7），参数β_f=0.35，β_n=2，最大单步扩展量Δa_v=2 m。[Thomas 2020, pp. 6-7]
   - **裂缝延伸与相交处理**：尖端矢量生成三角形条带以扩展裂缝面；当尖端与其他裂缝面或边界相交时，尖端失活（形成T型相交），同时允许部分X型相交。[Thomas 2020, pp. 7-8]
   - **终止条件**：所有尖端终止于其他裂缝或边界，或混合模态准则不再满足。[Thomas 2020, pp. 7-8]
2. **等效渗透率计算**：基于Darcy流有限元模拟，分别沿三个方向施加压差（100 Pa/10 Pa），计算体积平均压力梯度与流量，求解超定线性系统获得等效渗透率张量k（公式13），采用中心90%体积的流动套筒法减小边界效应。[Thomas 2020, pp. 8-9]
   - 基质渗透率固定为10^{-15} m²；裂缝渗透率由局部开度h按k_f = h²/12（公式9）计算。[Thomas 2020, pp. 8-9]
   - 力学开度通过在变形后提取裂缝面两侧位移差而得。[Thomas 2020, pp. 17-19]

## Key Findings
- 六组GDFN的生长均表现出强烈的各向异性：水平裂缝优先扩展，倾斜裂缝因应力遮蔽而延迟激活；最终裂缝网络趋于类似密度和几何特征，表明区域应力、断裂韧性和机械生长过程是控制网络形成的主要因素，而非初始随机分布。[Thomas 2020, pp. 11-12][Thomas 2020, pp. 21-22]
- 与各向同性SDFN（Set 1）相比，GDFN具有更高的各向异性和更高的最终水平渗透率；各向异性SDFN（Set 2）可更好地匹配GDFN的各向异性，但缺少机械相互作用导致的裂缝弯曲、选择性生长等特征。[Thomas 2020, pp. 13-14][Thomas 2020, pp. 17-17]
- 当裂缝开度均匀（0.001 m）时，GDFN在第四或第五个生长步发生水平渗透突破（percolation），垂直方向极少突破；渗透率张量从初始各向同性迅速变为水平各向异性。[Thomas 2020, pp. 13-14]
- 采用力学开度（单轴拉伸10^7 Pa诱导）时，开度分布高度非均匀，最大开度出现在大裂缝中心及域边缘；流体流动强烈通道化于少数裂缝上，与真实深部网络中少数裂缝提供主要流动路径的观测一致。[Thomas 2020, pp. 17-19]
- 力学开度下，等效渗透率与裂缝强度（P32）关系呈非线性：总空隙体积φ随P32增长梯度逐渐增大；渗透突破表现为渐变过程而非均匀开度时的跳跃，因为倾斜裂缝开度极低，降低了连通效率。[Thomas 2020, pp. 19-20]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| GDFN在单轴拉伸下水平裂缝优先扩展，倾斜裂缝因机械相互作用后激活 | [Thomas 2020, pp. 11-12] | 顶部拉应力2×10^6 Pa，底部固定，其他面牵引自由；材料K_IC=1.8×10^6 Pa·m^{1/2} | 六组GDFN均表现出类似行为 |
| 均匀开度GDFN的渗透突破发生在第4或第5生长步，P32约0.15–0.25 m^{-1} | [Thomas 2020, pp. 13-14] | 开度固定0.001 m，基质渗透率10^{-15} m² | 突破时k_xx和k_yy从10^{-14}量级跃增到10^{-12} m² |
| 力学开度下GDFN E在生长步18的开度分布：开度范围10^{-5}–10^{-3} m，域边缘和大裂缝中心最高 | [Thomas 2020, pp. 17-19] | 拉伸应力1×10^7 Pa，无流体压力 | 裂缝开度受应力遮蔽和自由边界效应影响 |
| 力学开度下流体通道化：大部分流动集中于少数连接好且开度大的裂缝 | [Thomas 2020, pp. 19-20] | 同力学开度条件 | 与Bisdom等(2015)、Follin等(2014)现场观测一致 |
| SDFN Set 2（各向异性随机）比Set 1更接近GDFN的渗透率和渗透突破特征，但缺少弯曲和机械选择性生长 | [Thomas 2020, pp. 17-17] | 裂缝半径固定4.3 m，取向比例与GDFN初始相同 | 表明随机模型可模拟各向异性，但机械过程引入关键差异 |
| GDFN最终裂缝表面积分布接近正态或对数正态，而非自然网络中常见的幂律分布 | [Thomas 2020, pp. 12-13] | 初始裂缝半径0.5 m和2.5 m，未包含极小裂缝 | 若纳入更小裂缝，选择性激活将主要集中在大裂缝 |

## Limitations
- 仅考虑单轴拉伸边界条件，未涉及多期应力状态或压缩/剪切条件。[Thomas 2020, pp. 20-21]  
- 裂缝相遇时主要形成T型相交，未系统模拟X型相交及相交准则（如Renshaw & Pollard, 1995），可能影响网络拓扑和渗透特征。[Thomas 2020, pp. 7-8]  
- 裂缝扭转角未引入，以避免尖端几何过于复杂，可能忽略模式III破碎效应。[Thomas 2020, pp. 6-7]  
- 初始裂缝尺寸分布较窄，导致最终表面积分布呈对数正态而非自然幂律，若增加更小裂缝将显著增加计算成本。[Thomas 2020, pp. 12-13]  
- 等效渗透率计算未评估代表性体积单元（REV）及采样尺度敏感性。[Thomas 2020, pp. 8-9]  
- 生长过程中未考虑流体压力与应力耦合，也未包含化学和热效应。[Thomas 2020, pp. 1-2]  
- 力学开度模拟仅采用拉伸应力，未包含压缩下的摩擦与接触效应（尽管方法上可行）。[Thomas 2020, pp. 11-12]

## Assumptions / Conditions
- 岩石基质为线弹性、各向同性、均质材料；裂缝表面为应力自由面，未考虑充填物质。[Thomas 2020, pp. 5-6]  
- 变形为准静态，无惯性效应。[Thomas 2020, pp. 1-1]  
- 远场应力条件：顶部施加均匀拉应力，底部无位移，四周牵引自由，无体积力。[Thomas 2020, pp. 5-6]  
- 裂缝生长由混合模态比较应力强度因子K_v ≥ K_IC触发，采用Richard准则确定扩展角。[Thomas 2020, pp. 6-7]  
- 裂缝尖端扩展量由修正两步Paris型法则分配（β_f=0.35，β_n=2）。[Thomas 2020, pp. 6-7]  
- 流动为不可压缩单相达西流，忽略基质中裂缝开度变化对渗透的影响；流体粘度1×10^{-3} Pa·s。[Thomas 2020, pp. 8-9]  
- 力学开度计算时忽略流体压力，仅由机械变形导致。[Thomas 2020, pp. 17-19]

## Key Variables / Parameters
- **域尺寸**：20×20×20 m³ [Thomas 2020, pp. 9-9]  
- **初始裂缝数量**：30, 60, 90 [Thomas 2020, pp. 9-9]  
- **初始裂缝半径与取向**：水平0.5 m，法向量(0,0,1)；倾斜2.5 m，法向量(4,5,1) [Thomas 2020, pp. 9-9]  
- **材料参数**：E=2×10^9 Pa, ν=0.2, K_IC=1.8×10^6 Pa·m^{1/2} (或1×10^6 Pa·m^{1/2}按Wei等2016)，K_IC/K_IIC=0.7540, K_IC/K_IIIC=1.5881 [Thomas 2020, pp. 9-9][Thomas 2020, pp. 6-6]  
- **断裂力学参数**：比较SIF公式(3)；扩展角公式(4)中A=140°, B=-70°；Paris指数β_f=0.35, β_n=2；最大单步扩展量Δa_v=2 m [Thomas 2020, pp. 6-7]  
- **流动模拟参数**：基质渗透率k_m=10^{-15} m²；均匀开度0.001 m（裂缝渗透率8.33×10^{-11} m²）；力学开度对应拉伸应力1×10^7, 0.5×10^7, 0.25×10^7 Pa [Thomas 2020, pp. 13-13][Thomas 2020, pp. 19-19]  
- **等效渗透率计算**：源/汇压力100 Pa/10 Pa，流量子域中心90% [Thomas 2020, pp. 8-9]  
- **P32（裂缝强度）**：裂缝总面积/体积 [Thomas 2020, pp. 9-9]

## Reusable Claims
- 基于线弹性断裂力学的三维裂缝网络生成方法可以再现裂缝的机械相互作用、弯曲表面和选择性生长，这些特征在随机DFN中缺失。[Thomas 2020, pp. 1-1][Thomas 2020, pp. 21-22]  
  - 条件：需给定材料断裂韧性、初始缺陷分布和远场应力。  
- 在单轴拉伸条件下，地质力学裂缝网络的水平渗透率显著高于垂直方向，且渗透率随生长步逐渐增加，突破后水平渗透率比随机各向同性网络更高。[Thomas 2020, pp. 13-14]  
  - 条件：域为立方体，拉伸方向垂直，裂缝倾向水平。  
- 当裂缝开度由应力场诱导时，等效渗透率的突破表现为渐变过程，而非均匀开度时的突变，且流动高度通道化于少数裂缝。[Thomas 2020, pp. 19-20]  
  - 条件：采用力学开度，且应力方向与裂缝取向关系符合本文设置。  
- GDFN的最终裂缝面积极分布接近正态或对数正态，若欲获得幂律分布，需在初始分布中引入更大幅宽或更小裂缝，但会增加计算成本。[Thomas 2020, pp. 12-13]  
- 随机DFN若按各向异性分布配置取向和密度，可部分逼近GDFN的各向异性和渗透阈值，但无法捕捉机械相互作用导致的弯曲、相交特征及应力诱导的渗透各向异性细节。[Thomas 2020, pp. 17-17]

## Candidate Concepts
- [[地质力学离散裂缝网络 (GDFN)]]  
- [[等效渗透率张量]]  
- [[应力强度因子 (K_I, K_II, K_III)]]  
- [[混合模态断裂准则]]  
- [[裂缝相互作用]]  
- [[裂缝弯曲]]  
- [[突破渗透 (percolation)]]  
- [[P32裂缝强度]]  
- [[流动通道化]]  
- [[力学开度]]  
- [[修正Paris型法则]]  
- [[NURBS SIF平滑]]

## Candidate Methods
- [[有限元线弹性断裂力学生长模拟]]  
- [[位移相关法 (DC) SIF计算]]  
- [[八叉树自适应网格划分]]  
- [[Richard裂缝扩展角准则]]  
- [[两步Paris型裂缝长度分配]]  
- [[裂缝相交处理 (T型终止)]]  
- [[等效渗透率张量计算 (流动套筒法)]]  
- [[力学裂缝开度提取 (节点位移差)]]

## Connections To Other Work
- 与二维地质力学裂缝生长工作（Olson, 2004; Renshaw & Pollard, 1994）相比，本工作拓展到三维，通过有限元方法实现任意网格和复杂裂缝相互作用。[Thomas 2020, pp. 3-3][Thomas 2020, pp. 12-13]  
- 对比了Paluszny & Matthäi (2010) 二维裂缝生长与开度影响，以及Lang et al. (2014) 的三维DFN渗透率张量计算框架，表明三维模拟可避免二维低估连通性的问题。[Thomas 2020, pp. 1-2][Thomas 2020, pp. 8-9]  
- 力学开度导致的流动通道化与Bisdom et al. (2015)、Follin et al. (2014) 的野外观察及应力敏感开度研究一致。[Thomas 2020, pp. 19-20]  
- 随机DFN的拓扑差异与Sanderson & Nixon (2015) 的讨论呼应，指出Poisson DFN中总是产生X型相交，而真实网络存在T型相交，受力学控制。[Thomas 2020, pp. 2-2]  
- Darcy流与耦合热-水-力模拟已有实施（Salimzadeh et al., 2018），本工作专注于纯机械生长与后续流动计算。[Thomas 2020, pp. 3-3]

## Open Questions
- 多期应力状态（如先张后剪）如何影响裂缝网络几何与水力特性？[Thomas 2020, pp. 20-21]  
- 引入裂缝扭转角与尖端分叉后，网络连通性和渗透率将如何变化？[Thomas 2020, pp. 6-6]  
- 如何有效纳入宽尺寸分布的初始缺陷，以再现自然幂律长度分布？[Thomas 2020, pp. 12-13]  
- X型相交的动态判据（如Renshaw & Pollard, 1995）对网络拓扑及渗透特性的定量影响？[Thomas 2020, pp. 7-8]  
- 等效渗透率张量的REV尺度依赖性及升尺度适用性？[Thomas 2020, pp. 8-9]  
- 压缩应力条件下摩擦与接触对网络生长及开度分布的作用？[Thomas 2020, pp. 11-12]  
- 如何将GDFN与实际特定场地（如核废料处置库）的参数直接匹配，以预测现场水力特性？[Thomas 2020, pp. 21-21]

## Source Coverage
所有22个非空索引片段均已处理并整合入本页面。按片段块数计，覆盖率为100%（22个编译块/22个源块）；按字符数计，覆盖率为100.4%（107,075编译字符/106,579源字符）。未使用任何非索引信息。
