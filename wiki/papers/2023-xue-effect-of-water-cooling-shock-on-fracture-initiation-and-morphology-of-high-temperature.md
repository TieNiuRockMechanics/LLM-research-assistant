---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-xue-effect-of-water-cooling-shock-on-fracture-initiation-and-morphology-of-high-temperature"
title: "Effect of Water-Cooling Shock on Fracture Initiation and Morphology of High-Temperature Granite: Application of Hydraulic Fracturing to Enhanced Geothermal Systems."
status: "draft"
source_pdf: "data/papers/2023 - Effect of water-cooling shock on fracture initiation and morphology of high-temperature granite Application of hydraulic fracturing to enhanced geothermal systems.pdf"
collections:
  - "1文章:2D-3D分形关系"
  - "论文"
citation: "Xue, Yi, et al. \"Effect of Water-Cooling Shock on Fracture Initiation and Morphology of High-Temperature Granite: Application of Hydraulic Fracturing to Enhanced Geothermal Systems.\" *Applied Energy*, vol. 337, 2023, 120858. doi:10.1016/j.apenergy.2023.120858."
indexed_texts: "17"
indexed_chars: "80285"
nonempty_source_blocks: "17"
compiled_source_blocks: "17"
compiled_source_chars: "74097"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.922925"
coverage_status: "full-index"
source_signature: "73787267d6d445c53779a4f3707b7bb9c7531390"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:29:09"
---

# Effect of Water-Cooling Shock on Fracture Initiation and Morphology of High-Temperature Granite: Application of Hydraulic Fracturing to Enhanced Geothermal Systems.

## One-line Summary
建立了一个考虑水冷冲击导致岩石力学参数劣化的热-流-固耦合模型，用于研究干热岩（HDR）水力压裂中水冷冲击对裂缝起裂与形态的影响，并通过实验和分析解进行了验证。 [Xue 2023, pp. 1-2]

## Research Question
水冷冲击如何影响HDR水力压裂的裂缝起裂、扩展及形态？初始岩温、地应力和换热系数在其中起何种作用？ [Xue 2023, pp. 1-2, 3-4]

## Study Area / Data
- 实验用花岗岩采自江苏省徐州市，为粗粒花岗岩，浅灰色，属于典型的地热储层岩石。 [Xue 2023, pp. 7-8]
- 数值模拟参数基于青海共和盆地干热岩地热储层GR1井的勘探参数 (见表2)。 [Xue 2023, pp. 5-7]
- 高温花岗岩水力压裂实验（200°C）采用Zhou等和Zhang等的实验方案进行验证。 [Xue 2023, pp. 7-8]
- 岩石力学参数劣化关系综合了本研究与文献中加热-水冷处理后的力学试验数据，覆盖Strathbogie花岗岩、开放花岗岩、monzonitic花岗岩等多种岩性，加热温度范围25–800°C (表1)。 [Xue 2023, pp. 2-3]
- 验证还使用了应力阴影效应的解析解（Sneddon & Elliot, 1946）以及Hubbert等、Haimson等、Ito & Hayashi、Zhang等提出的裂缝起裂压力准则，并对比了Zoback等和Lu等的实验/数值结果。 [Xue 2023, pp. 8-10, 10-12]

## Methods
- 建立了完全耦合的热-流-固（THM）模型，引入水冷冲击导致的弹性模量和抗拉强度随冷却幅度ΔT的经验劣化关系（式16、17）。 [Xue 2023, pp. 4-5]
- 控制方程包括含热-孔压耦合项的力学平衡方程（式4）、质量守恒方程（式6）和能量守恒方程（式7）。 [Xue 2023, pp. 3-4]
- 采用最大拉应力准则和Mohr-Coulomb准则判断岩石损伤，损伤变量D基于应变软化模型定义（式8-10）；渗透率和热导率随损伤演化（式11-13）。 [Xue 2023, pp. 3-4]
- 岩石非均质性通过Weibull分布赋予力学参数随机值（式18）。 [Xue 2023, pp. 5-7]
- 数值实现采用COMSOL Multiphysics与MATLAB联合求解，MATLAB计算损伤后回传参数（图7）。 [Xue 2023, pp. 5-7]
- 模型验证：（1）加热-水冷后花岗岩单轴压缩和巴西劈裂试验（25–400°C）；（2）高温花岗岩水力压裂实验(200°C)；（3）应力阴影效应与Sneddon和Elliot解析解对比；（4）起裂压力与多组已有解析公式和实验数据对比。 [Xue 2023, pp. 7-10, 10-12]

## Key Findings
1. 水冷冲击显著降低高温花岗岩的抗拉强度，归一化抗拉强度随冷却幅度ΔT呈指数衰减：f_t(ΔT)=f_t(T0)⋅(1.31−0.31 e^(0.002ΔT))（式17）。 [Xue 2023, pp. 4-5]
2. 热应力和水冷冲击共同作用下，裂缝起裂压力大幅降低。例如，初始岩温300°C时，不考虑水冷冲击需5.9 MPa起裂，考虑后仅需1.8 MPa。 [Xue 2023, pp. 12-15]
3. 热应力对裂缝起裂的贡献随温度升高而增大，300°C时热应力可提供达81%的所需拉应力。 [Xue 2023, pp. 12-15]
4. 与仅考虑HM耦合相比，水冷冲击可诱导更多次级裂缝，形成更复杂的裂缝网络，并增大最终刺激体积（SRA）。 [Xue 2023, pp. 12-15, 15-17]
5. 初始岩温越高，热应力和抗拉强度劣化程度越大，越易形成裂缝分支，最终损伤面积也越大。 [Xue 2023, pp. 12-15, 15-17]
6. 地应力差增大使裂缝主要沿最大水平主应力方向扩展，且SRA减小。 [Xue 2023, pp. 17-18]
7. 表面换热系数增大加速降温，降低起裂压力，增大SRA和压裂效果。 [Xue 2023, pp. 18-19]
8. HDR水力压裂开裂机制是水冷冲击引起的抗拉强度劣化、冷缩热应力和孔隙水压力三者共同作用的结果；低温水沿裂缝侵入导致裂尖温度与强度进一步下降，触发二次裂缝。 [Xue 2023, pp. 19-20]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 水冷冲击后花岗岩抗拉强度随冷却幅度ΔT按f_t(ΔT)=f_t(T0)(1.31−0.31e^(0.002ΔT))衰减；弹性模量类似衰减（式16）。 | Xue 2023, pp. 4-5 | 基于本文及文献中加热-水冷处理花岗岩数据的归一化均值。 | 适用于粗粒花岗岩在水冷条件下的强度劣化评估。 |
| 300°C初始岩温时，水冷冲击使起裂压力从5.9 MPa降至1.8 MPa。 | Xue 2023, pp. 12-15 | 数值模拟，THM耦合，参数见表2。 | 证实抗拉强度劣化与热应力为主导致裂因素。 |
| 300°C时，热应力对裂缝起裂的贡献可达总所需拉应力的81%。 | Xue 2023, pp. 12-15 | 根据不同初始岩温和注入压力的贡献分析（图19）。 | 热应力贡献远大于孔压贡献。 |
| 水冷冲击产生的裂缝网络比温度无关工况更复杂，主裂缝宽度和长度更大。 | Xue 2023, pp. 15-17 | THM与HM耦合损伤演化对比（图20）。 | 注入压力相同条件下，温度效应显著增强压裂效果。 |
| 归一化SRA随初始岩温和换热系数增大而增加，随地应力比α_σ增大而减小。 | Xue 2023, pp. 12-15, 15-17, 17-18, 18-19 | 参数变化模拟，T0=100,200,300°C; h=1000,2000,3000 W/m²K; ασ=1,1.5,2。 | SRA基于损伤区面积计算，用于量化压裂效果。 |
| 加热-水冷后花岗岩微裂隙随温度升高增多；400°C巴西劈裂出现次级裂纹。 | Xue 2023, pp. 7-8 | 本文实验，加热25–400°C后水冷。 | 裂隙形态与数值模拟一致（图12）。 |
| 模型计算的诱导应力与Sneddon & Elliot (1946) 解析解吻合良好（m=100近均质，m=5非均质）。 | Xue 2023, pp. 8-10 | 裂纹面形状差异导致一定误差，但分布趋势一致。 | 验证了该模型在应力场分析上的可靠性。 |
| 本模型起裂压力落入Hubbert & Willis、Haimson & Fairhurst、Ito & Hayashi、Zhang等的理论变化区间，并与Zoback等、Lu等的实验结果一致。 | Xue 2023, pp. 10-12 | HM耦合验证，不考虑温度效应。 | 表明模型可合理预测不同加压速率下的起裂压力。 |

## Limitations
- THM耦合模型假设HDR为连续各向同性多孔介质，忽略流体与岩石的化学反应以及水的相变（假定高压下始终保持液态）。 [Xue 2023, pp. 2-3]
- 非均质性仅通过力学参数Weibull分布引入，未考虑颗粒间热膨胀系数的各向异性。 [Xue 2023, pp. 5-7]
- Biot系数简化为阶跃函数（D<1时为α0，D=1时为1），完全损伤岩石的比热容取为流体的比热容。 [Xue 2023, pp. 3-4]
- 水冷冲击劣化公式（式16、17）基于多种花岗岩的平均归一化数据拟合，可能未充分反映特定岩性的差异性。 [Xue 2023, pp. 4-5]
- 压裂液性质利用NIST数据库插值引入，但模型假定局部热平衡，忽略了重力和惯性力。 [Xue 2023, pp. 5-7]
- 模型为二维，可能无法完全再现三维裂缝网络的复杂性（SRA仅在二维损伤区内计算）。 (未明确三维模拟)

## Assumptions / Conditions
- HDR为连续各向同性孔隙介质；流体为单相流且满足达西定律；忽略化学反应和水相变；满足局部热平衡；忽略重力和惯性力。 [Xue 2023, pp. 2-3]
- 岩石破坏采用应变软化模型，起裂判据为最大拉应力准则和Mohr-Coulomb准则。 [Xue 2023, pp. 3-4]
- 岩石力学参数因水冷冲击的劣化遵循基于加热-水冷试验的指数型经验关系。 [Xue 2023, pp. 4-5]
- 实验最高温度400°C，数值模拟最高300°C；地应力取共和盆地GR1井参数。 [Xue 2023, pp. 5-7, 7-8]
- 验证试验在无围压或特定围压条件下进行，数值模拟的边界条件与试验对应。 [Xue 2023, pp. 7-8, 8-10]

## Key Variables / Parameters
- 冷却幅度 ΔT = T0 - T，T0为初始岩温，T为当前温度。 [Xue 2023, pp. 4-5]
- 水冷劣化后的弹性模量 E(ΔT) 和抗拉强度 f_t(ΔT) (式16,17)。 [Xue 2023, pp. 4-5]
- 热膨胀系数 α_T，Biot系数 α，泊松比 ν，剪切模量 G，排水体积模量 K。 [Xue 2023, pp. 3-4]
- 初始渗透率 k0，初始孔隙度 φ0，初始热导率 λ_s0，初始比热容 C_ps0。 [Xue 2023, pp. 3-4, 5-7]
- 表面换热系数 h，注入流体温度 T_ext。 [Xue 2023, pp. 3-4, 18-19]
- 地应力比 α_σ = σ_H / σ_h，最大、最小水平主应力。 [Xue 2023, pp. 17-18]
- 损伤变量 D，均质度指数 m，损伤影响系数 α_Dk, α_Dλ, α_DC。 [Xue 2023, pp. 3-4, 5-7]
- 储层刺激面积 SRA（由损伤区面积等效确定）。 [Xue 2023, pp. 15-17]

## Reusable Claims
- 水冷冲击下高温花岗岩抗拉强度根据 f_t(ΔT)=f_t(T0)(1.31−0.31 e^(0.002ΔT)) 降低，该公式可用于量化冷却幅度驱动的强度劣化。 [Xue 2023, pp. 4-5] 条件：基于加热至800°C后水冷的数据，适用花岗岩。
- 在300°C初始岩温下，热应力可贡献总起裂拉应力的81%，是HDR水力压裂的主导机制。 [Xue 2023, pp. 12-15]
- 裂缝起裂压力随初始岩温升高而近线性降低，已被实验证实。 [Xue 2023, pp. 2-2]
- 提高表面换热系数可加速降温，降低起裂压力，并增大储层刺激面积。 [Xue 2023, pp. 18-19]
- 地应力差异大时裂缝沿最大主应力方向优势扩展，SRA减小；均匀地应力下裂缝呈随机方向网络。 [Xue 2023, pp. 17-18]
- 所建THM耦合模型能同时再现高温花岗岩水力压裂的裂缝形态和起裂压力，可用于EGS压裂设计参考。 [Xue 2023, pp. 7-8, 8-10]

## Candidate Concepts
- [[water-cooling shock]] [Xue 2023, pp. 1-2]
- [[fracture initiation pressure]] [Xue 2023, pp. 10-12]
- [[thermal stress fracturing]] [Xue 2023, pp. 12-15]
- [[stimulated reservoir area (SRA)]] [Xue 2023, pp. 15-17]
- [[cracking mechanism of HDR hydraulic fracturing]] [Xue 2023, pp. 19-20]
- [[rock mechanical parameter deterioration due to cooling]] [Xue 2023, pp. 4-5]
- [[THM coupling model]] [Xue 2023, pp. 3-4]
- [[stress shadow effect]] [Xue 2023, pp. 8-10]
- [[heterogeneity of rock in hydraulic fracturing]] [Xue 2023, pp. 5-7]
- [[enhanced geothermal system (EGS)]] [Xue 2023, pp. 1-2]

## Candidate Methods
- [[THM coupled numerical simulation for hydraulic fracturing]] [Xue 2023, pp. 3-4, 5-7]
- [[Weibull distribution for rock mechanical heterogeneity]] [Xue 2023, pp. 5-7]
- [[empirical degradation functions for water-cooling shock]] [Xue 2023, pp. 4-5]
- [[damage-based permeability evolution]] [Xue 2023, pp. 3-4]
- [[Brazilian splitting test for tensile strength after thermal treatment]] [Xue 2023, pp. 7-8]
- [[stress shadow analytical validation (Sneddon & Elliot)]] [Xue 2023, pp. 8-10]
- [[fracture initiation pressure validation against multiple criteria]] [Xue 2023, pp. 10-12]

## Connections To Other Work
- 与Aliyu和Archer (2021) 的多裂缝HDR热储数值模型相比，本研究进一步耦合水冷冲击效应和THM耦合。 [Xue 2023, pp. 2-2]
- 支持Lu等 (2022) 关于热刺激降低裂缝起裂压力的实验室认识，并提供数值模型证据。 [Xue 2023, pp. 2-2]
- 直接验证Zhou等 (2018) 热冲击下花岗岩水力压裂实验的裂缝形态。 [Xue 2023, pp. 7-8]
- 延续Zhang等 (2019, 2021) 热应力作用下裂缝起裂与扩展机理的思路，补充了水冷劣化的定量描述。 [Xue 2023, pp. 10-12]
- 对比Tomac和Gutierrez (2017) 的BPM-DEM细观模型，本研究采用含非均质性的连续损伤方法。 [Xue 2023, pp. 2-2]
- 应力阴影验证直接引用经典Sneddon & Elliot (1946) 解析解。 [Xue 2023, pp. 8-10]
- 起裂压力验证覆盖Hubbert & Willis (1957)、Haimson & Fairhurst (1967)、Ito & Hayashi (1991)、Zhang等 (2017) 等多种判据。 [Xue 2023, pp. 10-12]

## Open Questions
- 当压裂液为液氮等低温流体时，水的相变（如沸腾）如何影响冷却冲击与裂缝起裂？当前模型未考虑相变。 [Xue 2023, pp. 2-3]
- 现场尺度下三维裂缝网络的真实形态及其在温度-应力梯度下的演化规律尚需研究。 (二维模型未涉及)
- 流体-岩石化学反应（如矿物溶解）对长期渗透率演变的影响未被纳入。 [Xue 2023, pp. 2-3]
- 本文的水冷劣化经验公式能否推广至玄武岩、砂岩等其他岩类？ [Xue 2023, pp. 4-5]
- 最优注入速率与流体温度以最大化SRA并控制诱发地震风险的问题尚未讨论。 (未提及)
- 天然裂缝或节理与热致裂缝的相互作用未被考虑。 (无数据)

## Source Coverage
处理了全部17个非空索引片段，覆盖索引字符数80285，编译字符数74097，块覆盖率1.0，字符覆盖率0.922925。源文件签名：73787267d6d445c53779a4f3707b7bb9c7531390。
