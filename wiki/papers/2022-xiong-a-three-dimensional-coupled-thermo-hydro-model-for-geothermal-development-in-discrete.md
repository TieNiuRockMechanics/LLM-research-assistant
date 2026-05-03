---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-xiong-a-three-dimensional-coupled-thermo-hydro-model-for-geothermal-development-in-discrete"
title: "A Three-Dimensional Coupled Thermo-Hydro Model for Geothermal Development in Discrete Fracture Networks of Hot Dry Rock Reservoirs."
status: "draft"
source_pdf: "data/papers/2023 - A three-dimensional coupled thermo-hydro model for geothermal development in discrete fracture networks of hot dry rock reservoirs.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Xiong, Feng, et al. \"A Three-Dimensional Coupled Thermo-Hydro Model for Geothermal Development in Discrete Fracture Networks of Hot Dry Rock Reservoirs.\" *Gondwana Research*, 2022, doi:10.1016/j.gr.2022.12.002."
indexed_texts: "14"
indexed_chars: "69863"
nonempty_source_blocks: "14"
compiled_source_blocks: "14"
compiled_source_chars: "70178"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004509"
coverage_status: "full-index"
source_signature: "bb20aeb1602785bafccf078fe3a2f001b5e73de5"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:10:55"
---

# A Three-Dimensional Coupled Thermo-Hydro Model for Geothermal Development in Discrete Fracture Networks of Hot Dry Rock Reservoirs.

## One-line Summary
作者开发了一个基于Galerkin有限元法的三维耦合热-水（T-H）模型，用于模拟干热岩储层离散裂缝网络（DFN）中的非线性流体流动和热传输过程，并以澳大利亚Habanero增强型地热系统（EGS）为例评估了不同注入压力下的40年产热效能。[Xiong 2022, pp. 1-1]

## Research Question
如何在考虑非线性Forchheimer流动和局部热非平衡（LTNE）的条件下，准确模拟三维离散裂缝网络中的耦合热-水过程？进而，注入/生产压力和温度如何影响EGS储层的产热效率与寿命？[Xiong 2022, pp. 1-2, pp. 2-3]

## Study Area / Data
研究区域为澳大利亚南澳Cooper Basin的Habanero增强型地热储层。该储层基底为花岗岩，最深记录温度521.45 K（深度4391 m）。经过水力压裂，形成了包含642条裂缝的离散裂缝网络。从Habanero 1井（注入井）至Habanero 4井（生产井）截取了一个500 m × 500 m × 240 m的DFN域，包含421条多边形裂缝。[Xiong 2022, pp. 10-11]  
参数数据（裂缝孔径、岩石/流体热物性、注入/生产压力等）主要引用自Xu et al. (2015)和Yang et al. (2019)，并通过2013年180天循环试验的监测数据反演得到Forchheimer系数β=25.0。[Xiong 2022, pp. 11-12, pp. 11-12] 具体模型参数见表2。[Xiong 2022, pp. 12-12]

## Methods
- **流动模型**：稳态流体流动采用Forchheimer定律描述非线性渗流，结合质量守恒和Reynolds方程，假设裂缝为水力各向同性，渗透率服从立方定律。[Xiong 2022, pp. 2-3]  
- **热传输模型**：基于局部热非平衡（LTNE）理论，用两个能量守恒方程分别描述裂缝内流体的对流与导热，以及岩石基质的导热和热交换（牛顿冷却定律）。[Xiong 2022, pp. 3-4]  
- **数值离散**：采用Galerkin有限元法对流动方程和热传输方程进行空间离散。为抑制热传输方程中由于对流占优引起的数值振荡，引入了一种简化的迎风加权方案（依据Heinrich et al. 1977）。[Xiong 2022, pp. 4-6, pp. 5-5]  
- **耦合策略**：采用显式顺序求解（隐式向后Euler差分），即先迭代求解流动方程得到速度场，再更新热传输方程中的对流项，同时根据流体温度更新粘度（式32），直至压力和温度的迭代残差满足容差。[Xiong 2022, pp. 5-6]  
- **坐标转换**：求解时需将每个裂缝单元的三维全局坐标转换为二维局部坐标。[Xiong 2022, pp. 6-6]  
- **模型验证**：通过交叉裂缝模型和多交叉裂缝模型，将预测压力–流量曲线与实验结果对比（NMAE 4.8%~5.4%）；通过单裂缝解析解（Hu et al. 2014）和交叉裂缝COMSOL解验证热传输模型（NMAE 0.8%~1.1%）。[Xiong 2022, pp. 6-9, pp. 6-9]  
- **Habanero案例**：对H1-H4双井系统模拟40年地热开采，共计算了7种注入压力（6, 15, 25, 30, 35, 40, 45 MPa）和固定生产压力5 MPa的场景，并分析了注入温度（354.15 K, 364.15 K, 374.15 K）的影响。同时对比了线性Darcy流与Forchheimer流，以及2D与3D模型的结果。[Xiong 2022, pp. 11-14]

## Key Findings
- 在Habanero案例中，当注入压力为6 MPa时，40年内平均生产温度几乎不变（仅下降0.06%），而注入压力升至45 MPa时，温度在40年内下降46.47%。[Xiong 2022, pp. 12-12]  
- 注入压力从6 MPa增至45 MPa，初始发电功率由4.9 MW上升至12.5 MW，但40年后功率下降60.2%。[Xiong 2022, pp. 12-12]  
- 热突破时间随注入压力增大而缩短：PH1=15, 25, 35, 40, 45 MPa对应的热突破时间分别为31.6, 26.2, 17.4, 15.0, 13.0年。[Xiong 2022, pp. 12-13]  
- 提高注入温度可延长热突破时间：当注入温度从354.15 K升高至374.15 K（PH1=30 MPa），热突破时间从24.6年延长至25.4年。[Xiong 2022, pp. 13-13, pp. 14-14]  
- 在低注入压力（6 MPa）下，线性Darcy流与Forchheimer流预测的生产温度几乎一致；但在高注入压力（25 MPa, 30 MPa）下，Forchheimer流预测的温度分别比线性流高4.3%和10.9%，表明高压时非线性效应不可忽略。[Xiong 2022, pp. 13-13, pp. 14-14]  
- 3D模型预测的生产温度低于2D模型（40年后温度高1.91%），因为2D模型不能真实反映三维裂缝的非均匀分布，导致渗透率偏高，热迁移过快。[Xiong 2022, pp. 14-15]  
- 注入井和生产井附近出现高流速区，流速比其余位置高一个数量级以上，且随着注入压力增大，高流速区半径由约10 m扩展至约15 m。[Xiong 2022, pp. 12-12, pp. 12-13]

## Core Evidence Table
| Evidence                                                         | Source                   | Conditions                                                                 | Notes                                      |
|------------------------------------------------------------------|--------------------------|----------------------------------------------------------------------------|--------------------------------------------|
| 低注入压力（6 MPa）下40年生产温度几乎不变（下降0.06%）          | Xiong 2022, pp. 12-12    | Habanero DFN, PH4=5 MPa, Tin=364.15 K, b0=240 µm, β=25                    | 线性流与非线性流结果一致                     |
| 高注入压力（45 MPa）下40年生产温度下降46.47%                    | Xiong 2022, pp. 12-12    | 同上                                                                       | 非线性效应明显，产热衰减迅速                 |
| 热突破时间：PH1=25 MPa→26.2年，PH1=35 MPa→17.4年              | Xiong 2022, pp. 13-13    | 同上                                                                       | 注入压力升高显著缩短热突破时间               |
| 注入温度从354.15 K升至374.15 K，热突破时间延长约0.8年          | Xiong 2022, pp. 13-13    | PH1=30 MPa, PH4=5 MPa                                                      | 注入温度对寿命有正向影响                     |
| 非线性流比线性流预测的温度高4.3%（25 MPa）和10.9%（30 MPa）     | Xiong 2022, pp. 14-14    | PH1=25, 30 MPa, PH4=5 MPa                                                  | 高压下线性模型低估热提取                     |
| 3D模型比2D模型预测的温度低1.91%（40年后）                        | Xiong 2022, pp. 14-15    | PH1=25 MPa, PH4=5 MPa, 选取x=0.0 m截面                                     | 2D模型高估热回收效率                         |
| 流量测试反演得Forchheimer系数β=25，R²=0.85                     | Xiong 2022, pp. 11-12    | H1-H4井180天循环试验数据                                                   | 反演值用于后续模拟                           |
| 流动模型验证NMAE：交叉裂缝4.8%~5.2%，多交叉裂缝5.4%             | Xiong 2022, pp. 7-7      | 与Li et al. (2016)、Liu et al. (2016)实验对比                               | 证明Forchheimer流模拟的有效性                |
| 热传输模型验证NMAE：交叉裂缝与COMSOL对比0.8%~1.1%               | Xiong 2022, pp. 9-9      | 交叉角度138.8°~172.9°，hc=1000 W/(m²·K)                                   | 证明简化LTNE模型与迎风方案的准确性            |
| 网格收敛性：网格数>380,000时温度差异约0.9%                       | Xiong 2022, pp. 12-12    | Habanero案例，389,600与779,200网格对比                                     | 网格敏感度可接受                             |
| 迭代收敛：压力9次迭代，温度15次迭代                              | Xiong 2022, pp. 12-13    | 网格数389,600，无具体压力条件                                              | 表明隐式顺序算法收敛性能良好                 |

## Limitations
- 模型仅适用于单相水流动，不能模拟因沸腾引起的两相（水/蒸汽）流动。[Xiong 2022, pp. 15-15]  
- 数值解尚未用长期现场温度、流量监测数据验证，且所需监测时长可能超过热突破时间。[Xiong 2022, pp. 15-15]  
- 采用简化的顺序耦合策略，对于强耦合问题可能需要多迭代，本研究中流动与热传输属于松耦合，仅需少量迭代，但未详细讨论强耦合适用性。[Xiong 2022, pp. 5-6]  
- 岩石基质被假定为完全不透水且无热对流，这可能低估了实际E-E EGS中基质的贡献。[Xiong 2022, pp. 2-3]  
- 热传输模型中热对流项采用简化的迎风方案，其最优系数依赖于Peclet数，但该方法在极高速流动下的普适性未作进一步探讨。[Xiong 2022, pp. 5-5]  
- 模型假设裂缝为单宽、光滑平行板，使用立方定律计算渗透率，未考虑粗糙度、接触面积等因素对非线性流的复杂影响。[Xiong 2022, pp. 2-3]

## Assumptions / Conditions
- 岩石基质渗透率极小，裂缝是流体唯一通道，基质视为不透水。[Xiong 2022, pp. 2-3]  
- 裂缝内流体为单相、不可压缩，且裂缝处于饱和状态；流动由Forchheimer模型描述。[Xiong 2022, pp. 2-3]  
- 岩石基质仅作为热源，其内部的热传输仅以热源形式影响裂缝流体，不考虑基质内的热对流。[Xiong 2022, pp. 2-3]  
- 采用局部热非平衡（LTNE）假设，即裂缝流体与基质温度不等，通过牛顿冷却定律交换热量。[Xiong 2022, pp. 3-4]  
- 水在深部高压下不沸腾，密度变化可忽略，但粘度随温度显著变化（采用经验公式，式32）。[Xiong 2022, pp. 5-5]  
- 裂缝渗透率服从立方定律，且假设水力各向同性（kx=ky=b²/12）。[Xiong 2022, pp. 3-3]  
- 模拟中使用的Forchheimer系数β通过现场循环试验反演获得，且在整个模拟期内保持恒定。[Xiong 2022, pp. 11-12]

## Key Variables / Parameters
- 裂缝孔径 b0 = 240 µm [Xiong 2022, pp. 12-12]  
- 初始岩石温度 Tf,0 = 524.15 K [Xiong 2022, pp. 12-12]  
- 注入流体温度 Tin = 364.15 K [Xiong 2022, pp. 12-12]  
- 岩石-流体界面传热系数 hc = 1500 W/(m²·K) [Xiong 2022, pp. 12-12]  
- 流体密度 ρf = 1000 kg/m³ [Xiong 2022, pp. 12-12]  
- 流体比热 cf = 4200 J/(kg·K) [Xiong 2022, pp. 12-12]  
- 流体导热系数 kf = 0.6 W/(m·K) [Xiong 2022, pp. 12-12]  
- 注入压力 PH1 = 6, 15, 25, 30, 35, 40, 45 MPa（敏感性分析）[Xiong 2022, pp. 12-12]  
- 生产压力 PH4 = 5 MPa [Xiong 2022, pp. 12-12]  
- 反演Forchheimer系数 β = 25.0 [Xiong 2022, pp. 12-12]  
- 粘度-温度经验关系：μ = 1 / [29.83·(Tf - 14.55)] [Xiong 2022, pp. 5-5]  
- 验证阶段参数：流体密度1000 kg/m³，粘度0.001 Pa·s，比热4200 J/(kg·K)，导热系数0.6 W/(m·K) [Xiong 2022, pp. 8-8]  
- 交叉裂缝案例 NMAE：4.8%, 5.1%, 5.2% [Xiong 2022, pp. 7-7]；多交叉裂缝案例 NMAE：5.4% [Xiong 2022, pp. 7-7]  
- 热传输验证案例 hc = 1000 W/(m²·K)（单裂缝分析解对比）[Xiong 2022, pp. 8-8]

## Reusable Claims
- **Forchheimer流动的3D DFN有限元格式**：本文推导了基于Galerkin弱形式的Forchheimer流动有限元方程（式10-21），可用于其他非线性裂缝渗流问题，但需注意渗透矩阵的迭代更新策略。[Xiong 2022, pp. 3-4]  
- **LTNE热传输的迎风有限元方案**：提出了一种适用于离散裂缝网络的瞬态热传输迎风有限元公式（式23-31），能有效抑制高Péclet数下的数值振荡，可移植至其他裂缝介质热模拟，但迎风因子的计算依赖于单元边速度和Péclet数（式26-27）。[Xiong 2022, pp. 4-6]  
- **隐式顺序耦合框架**：实现了流动-热传输的顺序双向弱耦合方法，通过粘度更新实现反馈，适用于多数T-H松耦合问题，对于强耦合可能需要增加内迭代。[Xiong 2022, pp. 5-6]  
- **非线性流动对热提取的影响阈值**：在Habanero型EGS条件下，当注入压力≤6 MPa时，非线性效应可忽略；≥25 MPa时，Forchheimer流预测的温度比Darcy流高4.3%–10.9%，说明高压操作必须考虑惯性效应。[Xiong 2022, pp. 13-14]  
- **3D模型相对于2D模型的修正量**：在Habanero案例中，3D模型预测的生产温度比2D模型低约1.91%（40年后），表明2D模拟会高估热回收效率，适合初步评估但非精确设计。[Xiong 2022, pp. 14-15]  
- **注入参数对储层性能的影响规律**：注入压力升高虽能提高初期发电功率，但会加速热突破（如PH1=35 MPa时突破时间仅17.4年）；提高注入温度可略微延长热突破（在30 MPa下，温度升高10 K可延长约1年）。这些结论为该类储层运行策略提供参考，但需注意结果针对特定裂缝网络和参数集。[Xiong 2022, pp. 12-13, pp. 13-13]

## Candidate Concepts
- [[discrete fracture network (DFN)]]
- [[enhanced geothermal system (EGS)]]
- [[hot dry rock (HDR)]]
- [[Forchheimer flow]]
- [[local thermal non-equilibrium (LTNE)]]
- [[cubic law]]
- [[Galerkin finite element method]]
- [[upwind scheme]]
- [[thermal breakthrough]]
- [[implicit sequential coupling]]
- [[Peclet number]]
- [[nonlinear fluid flow in fractures]]
- [[heat transfer coefficient]]
- [[temperature-dependent viscosity]]

## Candidate Methods
- [[three-dimensional coupled thermo-hydro model for DFN]]
- [[finite element discretization of Forchheimer equation]]
- [[LTNE heat transfer model for fractured rock]]
- [[upwind weighted residual method for convection-dominated transport]]
- [[iterative implicit coupling of flow and heat transfer]]
- [[inversion of Forchheimer coefficient from field flow test]]
- [[comparison against experimental cross-cutting fracture flow data]]
- [[validation against analytical solution for single fracture thermal transport]]
- [[comparison with COMSOL for cross-cutting fracture temperature field]]

## Connections To Other Work
- 与Xu et al. (2015)的简单管道流T-H模型直接相关：本文将其扩展至全三维DFN并引入Forchheimer流动。[Xiong 2022, pp. 2-2, pp. 11-11]  
- 延续了Chen et al. (2018)和Wang et al. (2019)的工作，在三维统一管道网络法基础上，采用有限元法并改进了热传输数值方案（迎风法）。[Xiong 2022, pp. 2-2, pp. 4-4]  
- 与Sun et al. (2017)的离散裂缝热-流-力耦合模型对比，本文着重于T-H耦合，并引入非线性流动，但未考虑力学变形。[Xiong 2022, pp. 2-2]  
- 流动模型验证引用了Li et al. (2016)的交叉裂缝实验和Liu et al. (2016)的多交叉裂缝实验。[Xiong 2022, pp. 7-7]  
- 热传输模型验证引用了Hu et al. (2014)的单裂缝解析解，且与COMSOL结果对比。[Xiong 2022, pp. 7-9]  
- 非线性的讨论建立在Forchheimer方程经典工作（Ruth & Ma 1992, Giorgi 1997）和裂缝非线性流研究（Zhou et al. 2015, Rong et al. 2016, Xiong et al. 2018）之上。[Xiong 2022, pp. 1-2]  
- 采用和验证了Heinrich et al. (1977)的迎风有限元方法。[Xiong 2022, pp. 5-5]

## Open Questions
- 如何将模型扩展至两相流（水-蒸汽）以适应可能的沸腾场景？[Xiong 2022, pp. 15-15]  
- 现场长期监测数据（流量、温度）何时能用于进一步验证模型预测，尤其是热突破后的阶段？[Xiong 2022, pp. 15-15]  
- 在强非线性或高流速区域，现有迎风方案的优化准则是否需要进一步改进？[Xiong 2022, pp. 5-5]  
- 如何将力学效应（如裂缝变形、应力变化）耦合进模型，以形成完整的THM耦合？[Xiong 2022, pp. 2-2, 未深入讨论]  
- 岩石基质的微小渗透性或热对流在长期开采中是否可能产生与假设不同的影响？[Xiong 2022, pp. 2-3]  
- 对于其他地质条件的EGS，本文得出的注入压力阈值和热突破规律是否具有普适性？

## Source Coverage
所有14个非空索引片段均已处理并纳入本页面的撰写，覆盖了论文的标题、摘要、引言、数学模型、数值方法、模型验证、Habanero案例研究及结论等完整内容。按索引字符数统计，编译源文本共70,178个字符，全部被使用，覆盖率为100%（按片段数）和100.45%（按字符数，因格式化引入少量额外字符）。源签名：bb20aeb1602785bafccf078fe3a2f001b5e73de5，编译策略：单遍markdown。
