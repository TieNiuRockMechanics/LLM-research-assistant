---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-afshari-moein-fracture-network-characterization-using-stress-based-tomography"
title: "Fracture Network Characterization Using Stress-Based Tomography."
status: "draft"
source_pdf: "data/papers/2018 - Fracture Network Characterization Using Stress-Based Tomography.pdf"
collections:
citation: "Afshari Moein, Mohammad Javad, et al. \"Fracture Network Characterization Using Stress-Based Tomography.\" *Journal of Geophysical Research: Solid Earth*, 2018, p. 9324, doi:10.1029/2018JB016438. Accessed 2026."
indexed_texts: "18"
indexed_chars: "86036"
nonempty_source_blocks: "18"
compiled_source_blocks: "18"
compiled_source_chars: "86459"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004917"
coverage_status: "full-index"
source_signature: "ff238112e45aca3dbe6f3b201a2e7aeec7234011"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T20:35:28"
---

# Fracture Network Characterization Using Stress-Based Tomography.

## One-line Summary
引入应力层析成像（stress-based tomography），利用贝叶斯框架通过井孔应力剖面反演离散裂隙网络（DFN）的概率分布，以刻画深部地热储层中裂隙网络的关键几何特征。

## Research Question
能否利用原位应力沿井孔的非均质性（主要受天然裂隙滑动控制）反演裂隙网络的几何（位置、长度、方向），从而在仅有井眼图像等有限先验信息下约束增强型地热系统（EGS）的裂隙网络模型？[Afshari 2018, pp. 1-1, 1-2, 2-3]

## Study Area / Data
- 通过数值试验验证，其观测数据为沿井孔的至少一个主应力分量的方向和一个主应力分量的大小（如β和σ₁剖面），用于校准DFN。所用的“观测”应力剖面由2D位移不连续方法（DDM）正演模拟生成。
- 测试了两个算例：[Afshari 2018, pp. 8-9, 9-11]
  - 简单合成网络：100×100 m²域内4条大型正交裂隙；剖面数据源于沿中心井孔（X=0）提取的σ₁和β（每0.5 m一个点，共201点）。
  - 基于露头的网络：取自瑞士阿尔卑斯Grimsel地区Tschingelmad结晶岩露头（50×40 m²域，裂隙最小长度8 m，长度分布幂指数2.6，两组优势方位30°和−65°）。
- 井孔应力非均质的观测依据参考了Basel EGS和Soultz-sous-Forêts EGS的实际井眼图像和应力估算（图1、2），但本论文的方法仅利用模拟的应力剖面作为反演输入。 [Afshari 2018, pp. 1-2, 3-4]

## Methods
1. **正演模拟**：采用基于位移不连续方法（DDM）的2D拟静态力学模拟器（Jalali, 2013），假设平面应变、岩石各向同性均质、裂隙为Mohr-Coulomb摩擦界面（Barton-Bandis模型），计算给定远场应力（σ_h=20 MPa，σ_v=38 MPa，剪切应力为零）下裂隙滑动引起的应力重新分布，提取井孔位置应力剖面σ₁和β。 [Afshari 2018, pp. 4-6]
2. **贝叶斯反演框架**：利用马尔可夫链蒙特卡罗（MCMC）中的Metropolis-Hastings随机游走算法，以先验信息（裂隙长度幂律分布、两组优势方位、最小间距、最小长度等）生成初始DFN；每次迭代随机移动一条裂隙，计算新的应力剖面，通过似然函数（假设观测误差服从正态分布，结合应力方向和大小）与Metropolis-Hastings接受准则判断是否保留。保留的实现组成后验概率分布的“集合”（ensemble）。 [Afshari 2018, pp. 6-8]
3. **概率图生成**：将集合中各DFN像素化并叠加，计算每个像素出现裂隙的频率，得到裂隙位置与长度的概率分布图。 [Afshari 2018, pp. 11-12]
4. **所需观测**：反演至少需要一个主应力方向和一个主应力分量的大小；单一应力方向不足以重建简单的DFN。 [Afshari 2018, pp. 6-7]

## Key Findings
- 提出的应力层析成像方法能够成功成像未与井孔相交的较长裂隙，但对远离井孔的小裂隙分辨率有限；断裂概率图能明显分辨出主要裂隙的位置和长度。 [Afshari 2018, pp. 12-13, 13-15]
- 在简单合成算例中，反演准确恢复了所有裂隙的位置和长度；在复杂露头算例中，最长裂隙的成像效果最好，部分小裂隙或紧邻井孔的裂隙尖端导致的应力扰动未能完全重现（如在Y=-1.8 m处σ₁剖面的峰值偏差）。 [Afshari 2018, pp. 12-13]
- 随裂隙网络复杂度增加，MCMC收敛所需迭代次数增加（合成案例约200次后收敛，露头案例约5000次后趋于稳定），且均方根误差也增大（311 vs 684）。 [Afshari 2018, pp. 11-12, 12-13]
- 摩擦角较低（10°）时裂隙滑动产生较强的应力非均质，利于反演；测试表明即使采用结晶岩典型摩擦角（35°）也能重建网络的主要特征。 [Afshari 2018, pp. 12-13]
- 反演对裂隙强度参数（如法向与剪切刚度）的约束不足，建议在反演前对不同强度参数进行测试。 [Afshari 2018, pp. 13-15]

## Core Evidence Table
| 证据 | 来源片段 | 条件 | 备注 |
|------|----------|------|------|
| 应力层析成像可通过贝叶斯反演和DDM正演重构裂隙网络概率图，识别未与井孔相交的长裂隙。| [Afshari 2018, pp. 1-1, 1-2, 11-12] | 需至少一个主应力方向和大小，采用2D平面应变假设，裂隙长度服从幂律分布，方位已知。 | 合成与露头案例均验证，但露头案例中小裂隙或极近井孔裂隙尖端的峰值未被完全再现。 |
| MCMC接受准则（Metropolis-Hastings）有效地将模拟应力剖面与观测拟合，产生后验集合，集合前半作为burn-in舍弃。| [Afshari 2018, pp. 7-8, 11-12] | 先验信息包括裂隙长度指数、最小长度、最小间距和裂隙组方位；反演中裂隙数量固定。 | 收敛后RMS误差在简单案例约311，复杂案例约684。 |
| 正演应力扰动主要受裂隙长度控制，长裂隙影响更大；因此反演对长裂隙更敏感。| [Afshari 2018, pp. 8-9, 12-13] | 远场应力均匀，岩石弹性参数固定（E=60 GPa，υ=0.25），裂隙横向连续（2D）。 | 同一结论在Valley et al. (2014)的灵敏度分析中也有提及。 |
| 即使使用35°摩擦角，反演仍能重建主要裂隙几何特征，但应力剖面变幅减小。| [Afshari 2018, pp. 12-13] | 与10°摩擦角的结果对比，实际深层结晶岩摩擦角通常为30°–45°。 | 该测试在supporting information中提供。 |
| 反演成功率与裂隙网络的先验统计信息（长度分布、组数、最小间距）强相关；长度分布幂指数未知时可在1.5–3.5范围内尝试并选择拟合最佳者。| [Afshari 2018, pp. 7-8, 15-15] | 适用于地质先验信息不全的情况。 | 未确认不同指数对结果鲁棒性的系统分析。 |

## Limitations
- 目前框架限于2D平面应变，未考虑三维裂隙几何和非均匀地应力场，实际3D反演需开发高效快速的3D力学模拟器。 [Afshari 2018, pp. 13-15]
- 反演对裂隙力学参数（法向和剪切刚度）难以约束，需预先测试不同强度参数以选择合理估计，这限制了结果的客观性。 [Afshari 2018, pp. 13-15]
- 裂隙数量在反演中固定，未纳入跨维MCMC以自动决定裂隙数；长度分布幂指数和裂隙密度（常数c）也假定已知。 [Afshari 2018, pp. 15-15]
- 仅使用单井应力剖面，不能唯一确定所有裂隙的几何；对于未与井孔相交的小裂隙或离井较远的裂隙，概率图上可能模糊或遗漏。 [Afshari 2018, pp. 12-13, 13-15]
- 实际井孔应力分量获取存在不确定性，尤其是Shmax的估算带有较大误差，且获得完整应力张量剖面困难。 [Afshari 2018, pp. 3-4]

## Assumptions / Conditions
- 假设岩石为各向同性均质线弹性，裂隙遵循Mohr-Coulomb摩擦准则，滑动服从Barton-Bandis模型。 [Afshari 2018, pp. 4-6]
- 假设远场应力为常数（20 MPa水平、38 MPa垂直，无剪切），且当前应力场由单次构造加载事件形成；忽略重力引起的应力随深度梯度。 [Afshari 2018, pp. 4-6]
- 假设井孔应力观测误差服从正态分布，且应力方向和大小的观测相互独立。 [Afshari 2018, pp. 7-8]
- 反演需要已知裂隙组的方位（两组固定），各组成员的长度分布服从幂律（2D露头顶部通常指数为1.5–3.5），且存在最小裂隙长度和最小间距约束。 [Afshari 2018, pp. 7-8, 8-9]
- 二维模型假设裂隙在面外无限延伸，井孔垂直且位于模型中央。 [Afshari 2018, pp. 4-6]
- 裂隙网络中的小尺度裂隙（小于最小长度截止值）被忽略，因其对应力扰动影响甚微。 [Afshari 2018, pp. 8-9]

## Key Variables / Parameters
- 远场主应力：σ₃（最小水平应力）= -20 MPa，σ₁（最大垂直应力）= -38 MPa，剪切应力为零。 [Afshari 2018, pp. 4-6]
- 岩石弹性参数：E=60 GPa，ν=0.25。 [Afshari 2018, pp. 6-7]
- 裂隙力学参数：法向刚度Kₙ=1e11 Pa/m，剪切刚度Kₛ=1e10 Pa/m，内聚力c=0，摩擦角ϕ=10°（部分测试用35°）。 [Afshari 2018, pp. 6-7]
- 应力观测变量：沿井孔的最大主应力方向β和最大主应力大小σ₁；数据点间距在合成案例为0.5 m，露头案例为0.2 m。 [Afshari 2018, pp. 8-9, 9-11]
- 裂隙几何先验参数：
  - 合成案例：两组方位45°和−45°，最小间距10 m，长度幂指数1.5，最小长度40 m，域100×100 m²。 [Afshari 2018, pp. 8-9]
  - 露头案例：两组方位30°和−65°，最小间距约2.5 m，长度幂指数2.6，最小长度8 m，域50×40 m²。 [Afshari 2018, pp. 9-11]
- MCMC参数：接受率由似然比与先验比决定，建议不动，链长数目越复杂越长；burn-in取前半部分。 [Afshari 2018, pp. 7-8, 11-12]

## Reusable Claims
1. 当至少一个主应力分量的大小和一个主应力方向沿井孔被观测时，可通过基于DDM的快速正演和随机游走MCMC反演出裂隙网络的位置和长度概率分布，且对未与井孔相交的长裂隙有较高敏感性。 [Afshari 2018, pp. 6-7, 12-13]
   - 条件：需预知裂隙组的方位和长度幂律分布，岩石近似均质各向同性，2D平面应变，裂隙滑动服从摩擦定律。
   - 限制：不适用于三维非均质应力场，对远离井眼的小裂隙分辨率低。
2. 应力层析成像的概率图能够直接反映裂隙的空间不确定性，该图谱可被进一步用于流量模拟或地震风险评估。 [Afshari 2018, pp. 11-12]
   - 条件：后验集合经过burn-in并足够大；裂隙密度和长度范围已由先验约束。
3. 反演结果的质量与先验长度分布指数密切相关，若该指数未知，可尝试在1.5–3.5范围内运行多次MCMC并选取似然最优值。 [Afshari 2018, pp. 15-15]
   - 但未系统验证该策略的稳定性和唯一性。
4. 剪胀角和裂隙剪切强度参数（刚度、内聚力）对应力非均质的影响在塑性滑动阶段较小，因此采用低摩擦角（10°）增强滑动并简化参数选择不影响反演的基本能力。 [Afshari 2018, pp. 12-13]
5. 该框架可与示踪剂、水力或地球物理层析成像数据进行联合反演，以增强对复杂三维裂隙网络的约束，但需要3D快速力学模拟器。 [Afshari 2018, pp. 13-15]

## Candidate Concepts
- [[应力层析成像 (Stress-Based Tomography)]]
- [[离散裂隙网络 (DFN)]]
- [[位移不连续方法 (DDM)]]
- [[贝叶斯反演 (Bayesian Inversion)]]
- [[马尔可夫链蒙特卡罗 (MCMC)]]
- [[Metropolis-Hastings 接受准则]]
- [[裂隙概率图 (Fracture Probability Map)]]
- [[增强型地热系统 (EGS)]]
- [[应力非均质 (Stress Heterogeneity)]]
- [[井眼诱发裂隙 (Borehole Breakouts)]]
- [[幂律长度分布 (Power-law Length Distribution)]]
- [[Barton-Bandis 裂隙模型]]
- [[Mohr-Coulomb 摩擦准则]]
- [[远场应力 (Far-field Stress)]]
- [[裂隙网络反演 (Fracture Network Inversion)]]

## Candidate Methods
- [[基于DDM的2D拟静态力学模拟]]
- [[贝叶斯MCMC随机游走反演]]
- [[应力剖面提取与似然函数构建]]
- [[多分量应力观测联合似然]]
- [[DFN集合像素化生成概率图]]
- [[Burn-in 与收敛监测]]
- [[先验约束下的初始DFN随机生成]]
- [[裂隙平移更新（均匀分布命题）]]
- [[跨维MCMC（Transdimensional Inversion）]] (未来的潜在方向)

## Connections To Other Work
- Somogyvári et al. (2017) 提出了跨维MCMC用于示踪剂层析成像来表征裂隙网络，为本研究固定裂隙数目的MCMC奠定了基础，未来可将其跨维特性引入应力层析成像。 [Afshari 2018, pp. 6-7, 15-15]
- Valley et al. (2014) 尝试通过最小化单井水平应力方向观测与模拟的差异来重构裂隙几何，但未能重建复杂网络，为此本工作提出贝叶斯框架以扩展至多裂隙系统。 [Afshari 2018, pp. 2-3]
- 正演所依赖的DDM代码由Jalali (2013)开发，并与解析解（Sneddon, Haimson, Detournay & Cheng）验证。 [Afshari 2018, pp. 4-6]
- 应力非均质的尺度特征与Blake & Davatzes (2011), Day-Lewis et al. (2010), Valley & Evans (2014)等研究相符，均指出裂隙网络是控制应力波动的主要因素。 [Afshari 2018, pp. 1-2]
- Safari et al. (2014) 和 Leis & Gao (2018) 研究了裂隙网络对应力变异的影响，本工作将这些认识转化为反演工具。 [Afshari 2018, pp. 2-3]
- 露头数据源自Ferrari et al. (2017) 和 Ziegler et al. (2013, 2014)对Grimsel地区结晶岩裂隙的详细描述。 [Afshari 2018, pp. 9-11]

## Open Questions
- 应力层析成像在三维非均质地应力场下是否仍有效？需要开发高效的3D DDM或等效模拟器。 [Afshari 2018, pp. 13-15]
- 如何将井孔图像以外的其他地球物理或水文观测（如示踪剂、水力层析）与应力数据联合以改善反演的唯一性和分辨率？ [Afshari 2018, pp. 13-15]
- 若裂隙长度分布指数和裂隙数量未知，采用跨维MCMC自动确定参数的鲁棒性如何？ [Afshari 2018, pp. 15-15]
- 实际EGS场地中，应力测量存在显著误差，尤其Shmax的估算偏差较大，这种误差传播对概率图的影响有多大？ [Afshari 2018, pp. 3-4]
- 在真实深部地层中，裂隙的力学参数（特别是刚度）高度不确定且空间变化，参数不确定性与几何反演的耦合效应尚未探究。 [Afshari 2018, pp. 13-15]
- 当井孔穿越多条裂隙且裂隙网更密集时，应力叠加效应可能导致反演出现多解，如何量化后验分布的多模态特性？

## Source Coverage
所有18个非空索引片段均已被处理，涵盖完整论文正文（含摘要、引言、方法、案例、结果、讨论、参考文献）。索引总字符数为86,036，编译后源字符数为86,459，覆盖率达到 1.0（按片段数）和约 1.0049（按字符数）。所有来源签名一致，表示全文被完整索引，无遗漏。
