---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-zhou-variations-in-stress-thresholds-for-heated-granite-subjected-to-rapid-cooling-under-di"
title: "Variations in Stress Thresholds for Heated Granite Subjected to Rapid Cooling under Different Confining Pressures."
status: "draft"
source_pdf: "data/papers/2022 - Variations in Stress Thresholds for Heated Granite Subjected to Rapid Cooling under Different Confining Pressures.pdf"
collections:
  - "zotero new"
citation: "Zhou, Chunbo, et al. \"Variations in Stress Thresholds for Heated Granite Subjected to Rapid Cooling under Different Confining Pressures.\" *Natural Resources Research*, vol. 31, no. 5, 2022, pp. 2653-. doi:10.1007/s11053-022-10098-9."
indexed_texts: "11"
indexed_chars: "53668"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "53909"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004491"
coverage_status: "full-index"
source_signature: "b6c751e1eb17c4568ab8723ce98bef4d60eb4c7a"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:02:43"
---

# Variations in Stress Thresholds for Heated Granite Subjected to Rapid Cooling under Different Confining Pressures.

## One-line Summary
本研究通过高温加热后水冷与液氮冷却花岗岩的三轴压缩实验，结合Hoek–Brown准则与COMSOL模拟，揭示了围压对裂纹起裂、裂纹损伤和峰值三种应力阈值的非线性强化效应及两种冷却方式在不同围压下力学差异的机制。[Zhou 2022, pp. 1-2][Zhou 2022, pp. 17-18]

## Research Question
液氮冷却被提议用于增强地热储层水力压裂形成的裂隙网络，但在高温和围压条件下，水冷与液氮冷却对花岗岩力学性能劣化的差异及其机制尚不清楚。本研究比较了不同围压下两种冷却处理后花岗岩的三个应力阈值（裂纹起裂应力σ<sub>ci</sub>、裂纹损伤应力σ<sub>cd</sub>、峰值应力σ<sub>p</sub>），并揭示热损伤机制与围压效应。[Zhou 2022, pp. 1-2]

## Study Area / Data
实验所用花岗岩采自中国日照，矿物组成为大约25%石英、39%斜长石、22%钾长石和14%黑云母，平均密度2640 kg/m³，弹性模量13.69 GPa，泊松比0.135，平均抗拉强度8.84 MPa，平均单轴抗压强度84 MPa。试件直径50 mm、高100 mm。[Zhou 2022, pp. 2-3]  
热-冷却处理方案：试件先以2‒4°C/min升温至目标温度（25、200、400°C），恒温2 h保证均匀，然后分别用水（室温）或液氮（-196°C）急速冷却1 h，冷却后在自然环境中放置至少24 h恢复到室温再进行压缩试验。[Zhou 2022, pp. 2-3]  
三轴压缩试验在TAW-2000岩石试验系统上进行，围压设置为0、20、40、50、60 MPa，轴压控制方式为位移加载（0.2 mm/min）。[Zhou 2022, pp. 3-5]

## Methods
- 应力阈值识别：基于Martin & Chandler方法，由裂纹体积应变曲线反转点确定σ<sub>ci</sub>，由总体积应变曲线反转点确定σ<sub>cd</sub>，峰值应力σ<sub>p</sub>为破坏强度。[Zhou 2022, pp. 3-5]  
- Hoek–Brown准则拟合：采用Hoek–Brown破坏准则描述应力阈值与围压的凸非线性关系，并估算等效Mohr–Coulomb内摩擦角与黏聚力。[Zhou 2022, pp. 5-6][Zhou 2022, pp. 13-17]  
- COMSOL数值模拟：建立二维轴对称模型，设置均质模型和非均质模型（基于QGS方法重构矿物分布），模拟水冷和液氮冷却过程中的温度梯度及最大主应力演化，评估温度梯度与热膨胀非均质性的贡献。[Zhou 2022, pp. 9-12]  
- 相对变化分析：以水冷试样为基准，计算应力阈值相对变化Δσ = (σ<sub>LN2</sub> - σ<sub>water</sub>)/σ<sub>water</sub> × 100%。[Zhou 2022, pp. 9-12]

## Key Findings
1. 水冷与液氮冷却后，三种应力阈值（σ<sub>ci</sub>、σ<sub>cd</sub>、σ<sub>p</sub>）均与围压呈凸非线性关系，围压削弱了温度对应力阈值的影响；Hoek–Brown准则可良好描述不同围压下两种冷却处理后的峰值强度。[Zhou 2022, pp. 17-18]
2. 当围压 < 40 MPa时，液氮冷却试样的σ<sub>ci</sub>、σ<sub>cd</sub>、σ<sub>p</sub>高于水冷试样，且差异随围压增大被抑制；当围压 > 40 MPa时，出现液氮冷却试样的应力阈值低于水冷试样的趋势。[Zhou 2022, pp. 17-18]
3. 热损伤主要受温度梯度和矿物热膨胀非均质性控制。液氮冷却下较高的力学性能归因于Leidenfrost效应引起的传热受限及体积收缩导致的裂纹闭合。热膨胀非均质性越强，液氮冷却引起的异质性热应力越显著，可能产生更复杂的裂纹。[Zhou 2022, pp. 17-18]
4. 冷却方式对高围压下应力阈值的影响与黏聚力有关。液氮的极低温度引起更强的收缩，使黏聚力增大；但在高围压下，经液氮冷却致密的试样黏聚力提升空间较小，导致其黏聚力低于水冷试样。[Zhou 2022, pp. 17-18]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| σ<sub>ci</sub>, σ<sub>cd</sub>, σ<sub>p</sub>与围压呈凸非线性关系，Hoek–Brown拟合R²在0.932~0.998 | [Zhou 2022, pp. 5-6], Table 2 | 温度25、200、400°C，围压0~60 MPa，水冷与液氮冷却 | 拟合参数m和s随温度变化 |
| 围压从0→20 MPa时σ<sub>ci</sub>急剧升高（如水冷200°C试样增加3.56倍），之后增幅趋缓 | [Zhou 2022, pp. 3-5] | 200°C花岗岩，两种冷却方式 | 说明σ<sub>ci</sub>对低围压敏感 |
| σ<sub>ci</sub>温度敏感性（CV）在单轴条件下最高，高围压下显著降低 | [Zhou 2022, pp. 5-6], Fig.4b | 25~400°C，水冷与液氮冷却 | 围压抑制温度引起的劣化 |
| 围压<40 MPa时，Δσ<sub>ci</sub>, Δσ<sub>cd</sub>, Δσ<sub>p</sub>为正，且随围压增大而减小；>40 MPa时出现负值趋势 | [Zhou 2022, pp. 6-9], Figs.8-10 | 所有温度，两种冷却对比 | LN2冷却在低围压下力学性能更优 |
| COMSOL模拟：均质模型中，温度梯度主导热应力，水冷初期温度梯度高于LN2，但持续时间短；非均质模型中，温度梯度消失后LN2冷却仍存在残余热应力且符号反转 | [Zhou 2022, pp. 12-13], Figs.12-16 | 加热200°C，边界传热系数水1000 W/(m²·K)，LN2 100 W/(m²·K) | 解释了LN2冷却裂纹复杂性 |
| 黏聚力c的差异显著（Δc变化范围-24.15%~84.92%），内摩擦角φ差异较小（Δφ -4.34%~1.93%） | [Zhou 2022, pp. 13-17], Fig.17, Table 1 | 所有冷却及围压条件 | 冷却方法主要通过c影响应力阈值 |

## Limitations
- 液氮冷却实验中，液氮罐盖子在试样浸入后立即关闭，限制了液氮气化后逸出，强化了Leidenfrost效应，可能高估液氮冷却下的力学性能。[Zhou 2022, pp. 6-9]
- COMSOL模型为弹性假设，未考虑塑性变形及裂纹扩展；非均质模型仅考虑热膨胀系数差异，未考虑矿物颗粒界面等其他因素。[Zhou 2022, pp. 9-12]
- 试验仅采用日照花岗岩一种岩性，结论向其他岩石类型推广需谨慎。
- 围压范围限于0~60 MPa，更高围压或地应力条件下的行为未涉及。

## Assumptions / Conditions
- 试件加热至目标温度后恒温2 h使得温度均匀分布。[Zhou 2022, pp. 2-3]
- 冷却处理后所有试件在自然环境中恢复至室温（>24 h）再进行力学测试。[Zhou 2022, pp. 2-3]
- 应力阈值识别方法基于Martin & Chandler的裂纹体积应变和总体积应变反转点，适用于脆性岩石。[Zhou 2022, pp. 3-5]
- Hoek–Brown准则用于描述应力阈值与围压的非线性关系，并据此估算Mohr–Coulomb参数。[Zhou 2022, pp. 5-6, 13-17]
- 数值模拟中，传热边界设为第三类边界条件，水冷传热系数1000 W/(m²·K)，液氮传热系数100 W/(m²·K)（受Leidenfrost影响）。[Zhou 2022, pp. 9-12]
- 非均质模型仅考虑热膨胀系数差异，其他力学和热学参数与均质模型相同。[Zhou 2022, pp. 9-12]

## Key Variables / Parameters
- 自变量：冷却介质（水、液氮）、加热温度（25°C、200°C、400°C）、围压（0、20、40、50、60 MPa）
- 因变量：裂纹起裂应力σ<sub>ci</sub>、裂纹损伤应力σ<sub>cd</sub>、峰值应力σ<sub>p</sub>、相对变化量Δσ、内摩擦角φ、黏聚力c
- 拟合参数：Hoek–Brown材料常数m、s，单轴抗压强度σ<sub>c</sub>（拟合得到）
- 模拟参数：热膨胀系数（均质10.59×10⁻⁶ /K，石英16.6×10⁻⁶，斜长石8.2×10⁻⁶，钾长石4.15×10⁻⁶ /K），热导率2.6 W/(m·K)，比热820 J/(kg·K)，传热系数等

## Reusable Claims
1. 经高温加热后水冷或液氮急冷的花岗岩，其裂纹起裂应力、裂纹损伤应力和峰值应力均随围压升高呈凸非线性增长，可用Hoek–Brown破坏准则很好描述。[Zhou 2022, pp. 17-18]  
   *条件/限制*：花岗岩，加热温度25~400°C，围压0~60 MPa，两种冷却方式；岩石类型和更高围压需验证。
2. 围压对温度引起的应力阈值劣化有显著抑制作用，即温度敏感性（CV）随围压升高而降低。[Zhou 2022, pp. 5-6]  
   *条件/限制*：基于特定花岗岩和冷却速率，可能不适用于极端温度梯度或极低围压。
3. 在低围压（<40 MPa）下，液氮冷却试样的三种应力阈值均高于水冷试样；高围压（>40 MPa）下趋势反转。[Zhou 2022, pp. 17-18]  
   *条件/限制*：实验条件强化了Leidenfrost效应，若液氮充分流动则结论可能不同。
4. 液氮冷却下岩石的较高力学性能主要归因于Leidenfrost效应造成的传热受限以及矿物收缩引起的裂纹闭合；而热膨胀非均质性越强，液氮冷却诱导的异质性热应力越显著，可能产生更复杂的裂纹网络。[Zhou 2022, pp. 17-18]  
   *条件/限制*：需考虑实际储层中液氮流动条件及岩石矿物组成。
5. 不同冷却方式对应力阈值的影响与黏聚力c密切相关，内摩擦角φ变化较小。液氮冷却使试件致密化，黏聚力初始增大，但高围压下黏聚力提升空间减小导致其低于水冷试样。[Zhou 2022, pp. 13-17]  
   *条件/限制*：该解释基于Hoek–Brown推导的等效Mohr–Coulomb参数，适用性受准则本身限制。

## Candidate Concepts
- [[Liquid nitrogen cooling]]
- [[Water cooling]]
- [[Stress thresholds]] (σ<sub>ci</sub>, σ<sub>cd</sub>, σ<sub>p</sub>)
- [[Crack initiation stress]]
- [[Crack damage stress]]
- [[Peak stress]]
- [[Hoek-Brown failure criterion]]
- [[Mohr-Coulomb cohesion and friction angle]]
- [[Thermal damage]]
- [[Temperature gradient]]
- [[Thermal expansion heterogeneity]]
- [[Leidenfrost effect]]
- [[Volumetric contraction and crack closure]]
- [[Confining pressure effect]]
- [[Triaxial compression test]]
- [[Crack volumetric strain method]]

## Candidate Methods
- [[Triaxial compression test under controlled confining pressure]]
- [[Stress threshold identification based on volumetric strain reversal points]]
- [[Hoek-Brown failure criterion fitting]]
- [[Estimation of Mohr-Coulomb parameters from Hoek-Brown]]
- [[COMSOL heat transfer and thermal stress simulation]]
- [[Homogeneous and heterogeneous numerical modeling]]
- [[Quartet structure generation set (QGS) for mineral matrix reconstruction]]
- [[Relative variation analysis Δσ = (σLN2 - σwater)/σwater]]

## Connections To Other Work
- 液氮致裂技术：McDaniel et al. (1997), Grundmann et al. (1998) 的现场应用；Huang et al. (2020) 的综述；Cha et al. (2014) 发现Leidenfrost效应可阻碍液氮传热。[Zhou 2022, pp. 1-2]
- 冷却速率与热梯度对岩石损伤的影响：Li et al. (2020b), Sha et al. (2020), Kang et al. (2021) 比较了不同冷却流体；Wu et al. (2019a, 2019b) 研究了液氮对加热花岗岩物理力学性质的影响。[Zhou 2022, pp. 2-3]
- 围压对热损伤的抑制作用：Wu et al. (2019b), Zhang et al. (2020) 等报道高围压可削弱不同冷却方法造成的热损伤差异；Kumari et al. (2018) 发现力学性质与围压呈非线性关系。[Zhou 2022, pp. 2-3]
- 热损伤机制：Su et al. (2022) 指出温度梯度与矿物热膨胀非均质性是控制热损伤的两个主要因素。[Zhou 2022, pp. 9-12]
- Hoek–Brown准则的应用：Hoek & Brown (2019) 提供现代形式，Xue et al. (2021) 等用于估算内摩擦角和黏聚力。[Zhou 2022, pp. 13-17]

## Open Questions
- 在液氮充分流动、消除Leidenfrost效应后，液氮冷却是否总能造成比水冷更严重的力学劣化？
- 更高围压（>60 MPa）及循环冷却条件下，应力阈值的非线性关系是否仍然适用，以及液氮优势是否消失或反转？
- 非均质模型中考虑更多因素（如矿物界面、微裂纹扩展）后，残余热应力的实际贡献如何？
- 本结论对花岗岩适用，对其他常见地热储层岩石（如砂岩、大理岩）的普适性需要验证。
- 现场尺寸的传热与破裂响应是否与实验室尺度一致，如何放大？

## Source Coverage
本文档完全基于提供的所有11个非空索引片段编写，片段覆盖了原文的全部内容（字符级覆盖率100.45%，片段级覆盖率100%）。所有引用均标注来源，未添加任何片段之外的事实、数据或结论。索引片段总字符数53668，编译后字符数53909。
