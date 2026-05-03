---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2025-wu-thermal-property-of-reservoir-rocks-at-thermal-mechanical-coupled-conditions-and-resulta"
title: "Thermal Property of Reservoir Rocks at Thermal–Mechanical Coupled Conditions and Resultant Impact on Performance of Geothermal Systems."
status: "draft"
source_pdf: "data/papers/2025 - Thermal Property of Reservoir Rocks at Thermal–Mechanical Coupled Conditions and Resultant Impact on Performance of Geothermal Systems.pdf"
collections:
  - "zotero new"
citation: "Wu, Ming, et al. \"Thermal Property of Reservoir Rocks at Thermal–Mechanical Coupled Conditions and Resultant Impact on Performance of Geothermal Systems.\" *Rock Mechanics and Rock Engineering*, vol. 58, 2025, pp. 8773-8798, doi:10.1007/s00603-025-04587-5."
indexed_texts: "20"
indexed_chars: "98531"
nonempty_source_blocks: "20"
compiled_source_blocks: "20"
compiled_source_chars: "97506"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.989597"
coverage_status: "full-index"
source_signature: "f232c929dd94a07b32ae1dc5be67da72c2c18bd0"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T08:44:50"
---

# Thermal Property of Reservoir Rocks at Thermal–Mechanical Coupled Conditions and Resultant Impact on Performance of Geothermal Systems.

## One-line Summary
本研究通过实验测定了共和花岗岩、康定花岗岩和松辽砂岩在热力耦合条件下的热导率、比热容和热膨胀系数，并基于实验数据建立热-水耦合数值模型评估了热物性对地热系统性能的影响，发现比热容增大可提高生产温度、延长储层寿命并降低压差，而热导率的变化对热提取性能影响不显著。[Wu 2025, pp. 1-2]

## Research Question
地热储层原位高温、高应力条件对岩石热物性的潜在影响尚缺乏系统研究，热力耦合下的传热机制不明确，现有实验数据基础有限，因此需要针对特定地热田实际测量岩石热参数。研究问题为：高温及轴向应力如何耦合影响典型储层岩石的热导率、热膨胀系数和比热容？这些热物性参数的变化如何影响多孔砂岩和裂隙花岗岩地热储层的热提取性能（生产温度、寿命、压差、累积热能）？[Wu 2025, pp. 1-4]

## Study Area / Data
岩样取自三个中国典型地热田：青海省共和盆地（共和花岗岩）、四川省康定地区的鲜水河断裂带（康定花岗岩）、黑龙江省松辽盆地肇州县（松辽砂岩）。三个区域的大地热流值均高于中国平均值（61.5±13.9 MW/m²），地热资源丰富。实验数据包括：热导率测试温度30−180°C、轴向应力0.25−15 MPa及部分60 MPa；热膨胀系数测试从室温至1000°C；比热容测试温度50−250°C。数值模拟基于实测数据，对多孔砂岩储层（初始温度100°C）和裂隙花岗岩储层（初始温度240°C）进行热-水耦合计算。[Wu 2025, pp. 3-4, 14-15]

## Methods
- **热导率**：采用DRPL–3B系统，基于ISRM建议的稳态法（分棒法），在封闭腔体内测量圆柱试样（Ф50×25 mm）的导热系数，温度30、60、90、120、150、180°C，轴向应力0.25、3、6、9、12、15 MPa。对松辽砂岩另做60 MPa高应力试验。[Wu 2025, pp. 3-5]
- **热膨胀系数**：采用ZRPY-1000系统，按ASTM标准，以10°C/min速率从室温加热至1000°C，记录Ф8.5×50 mm圆柱试样的线性热变形。[Wu 2025, pp. 4-5]
- **比热容**：采用BRR型系统，基于混合冷却法（ASTM标准），将粉末试样在50‑250°C炉内加热后迅速与水混合（水岩比4:1），按能量守恒计算。[Wu 2025, pp. 4-5]
- **数值模拟**：使用有限元求解器OpenGeoSys，建立热-水耦合模型，含质量守恒（Darcy’s law/ cubic law）和能量守恒（局部热平衡假设）。模拟方案包括不同比热容（砂岩4组、花岗岩5组）和不同热导率（各4组）共17个工况，分析温度场、渗流场及采热指标。[Wu 2025, pp. 13-16]

## Key Findings
1. **热导率的温度-应力耦合行为**：温度升高使低孔隙花岗岩热导率降低，高孔隙砂岩先升后降；轴向应力增加使热导率上升，但存在阈值。高温增强了低孔隙花岗岩的应力敏感性，却降低了高孔隙砂岩的应力敏感性。当应力超过裂纹损伤应力（σ_cd）时，热导率因内部裂纹扩展而下降。[Wu 2025, pp. 5-10]
2. **热膨胀系数与温度**：热应变和线膨胀系数随温度呈四阶段变化（稳定增长‑573°C附近因石英相变急剧增长‑波动‑衰减/缓慢增长）。相同温度下，矿物粒径更粗的共和花岗岩比康定花岗岩表现出更高的热变形和膨胀系数。100–250°C范围内，膨胀系数基本呈线性增长。[Wu 2025, pp. 10-12]
3. **比热容的温度依赖性**：三种岩石比热容均随温度升高而增加，松辽砂岩增幅最显著（50→200°C增大53.8%），花岗岩增幅约14‑16%。高温条件下岩石储热能力增强，且与热开裂引发的能量耗散有关。[Wu 2025, pp. 11-13]
4. **热物性对地热系统性能的影响**：热导率变化对生产温度衰减和寿命影响可忽略（热提取主要受热对流控制）。而比热容增大能明显提升平均生产温度、延长储层寿命（砂岩延长21.1%，花岗岩延长13.7%）、降低生产井与注入井间压差（约1.6‑2.0%），并使累积采热量增加12‑21%。[Wu 2025, pp. 17-22]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 共和花岗岩30°C、0.25 MPa时平均λ=3.24 W/(m·°C)；孔隙率增加时λ下降 | [Wu 2025, pp. 5-6, Table 1] | 天然干燥状态，Ф50×25 mm试样 | 遵循λ_eff = nλ_w/g + (1-n)λ_s |
| 轴向应力从0.25升至15 MPa，低、高温下λ增幅：花岗岩3.8%/16.8%、砂岩31.2%/20.7% | [Wu 2025, pp. 6-8, Fig. 2d] | 温度30/180°C | 孔隙率和温度共同影响应力敏感性 |
| 松辽砂岩在0.25→30 MPa时λ由2.33增至2.93 W/(m·°C)，30→60 MPa时降至2.55 W/(m·°C)；σ_cd=42.5 MPa | [Wu 2025, pp. 8-10, Fig. 4] | 25°C，Ф25×25 mm试样 | 超过σ_cd后裂纹增加致λ下降 |
| 热应变在石英相变温度573°C附近急剧增大；共和花岗岩矿物粒径更大，100‑250°C线膨胀系数9.03‑12.50×10⁻⁶°C⁻¹ | [Wu 2025, pp. 10-12, Figs. 5-6] | 无应力，10°C/min升温至1000°C | 粒径粗的热变形更显著 |
| 比热容50→250°C：共和花岗岩759→869 J/(kg·°C) (+14.5%)，康定花岗岩812→946 (+16.5%)，松辽砂岩641→986 (+53.8%) | [Wu 2025, pp. 11-13, Fig. 7] | 粉末试样，水岩比4:1 | 符合Maier‑Kelley方程C_P=C1+C2T+C3T⁻² |
| 比热容从641增至986 J/(kg·°C)，砂岩储层寿命延长21.1%，累积热能增加20.6% | [Wu 2025, pp. 17-22, Fig. 12, 17] | 注入温度25°C，生产/注入流量42 kg/s | 比热容增大提升储热，减缓温度衰减 |
| 热导率在1.6‑2.6 W/(m·°C)范围内变化对砂岩和花岗岩储层生产温度曲线影响极小 | [Wu 2025, pp. 17-18, Fig. 11] | 模拟温度100°C/240°C，60年开采 | 主要传热方式为对流，热导率作用微弱 |

## Limitations
- 实验仅在轴向应力（最高15 MPa）下进行，未实现真三轴应力状态下的热物性测量。
- 热导率测试温度上限180°C，低于部分干热岩实际温度；系统侧向隔热措施仍有待优化以减少热损失。
- 数值模拟仅考虑热-水两场耦合，未耦合应力/变形（热膨胀系数的影响未计入采热评估）。
- 模型基于均质各向同性假设，未考虑储层非均质性和化学反应。
- 缺乏现场数据对数值模型进行标定和验证。[Wu 2025, pp. 23-24]

## Assumptions / Conditions
- **实验假设**：试样加工后自然干燥3天以消除水分影响；热导率测试中侧向用绝热材料包裹以减少误差；线膨胀系数计算时已扣除系统标定值；比热容测试中假设水岩混合过程绝热且无相变。[Wu 2025, pp. 3-5]
- **数值模拟假设**：储层均质各向同性；换热流体始终为液态，无物理化学反应；基质渗流满足达西定律，裂隙渗流满足立方定律；裂隙内为层流；流体与基质之间基于局部热平衡假设。[Wu 2025, pp. 13-14]
- **边界与初始条件**：砂岩储层初始压力10 MPa，注入/产量42 kg/s，初始温度100°C，注入水25°C；花岗岩储层初始压力35 MPa，注入10 kg/s、产出9 kg/s，初始温度240°C，注入水70°C。[Wu 2025, pp. 14-15]

## Key Variables / Parameters
- 热导率 λ (W/(m·°C))
- 比热容 C (J/(kg·°C))
- 热膨胀系数 α (10⁻⁶°C⁻¹)
- 温度 T (°C)，轴向应力 σ (MPa)，孔隙率 n (%)
- 生产温度 T_pro，储层寿命（以温度降10%为标准），累积采热量 S_T
- 数值模型参数：基质/裂隙渗透率、孔隙率、水动力黏度 (随温度变化) 等 (见表6) [Wu 2025, pp. 15-16]

## Reusable Claims
- 在30‑180°C、0.25‑15 MPa范围内，低孔隙花岗岩（<1%）的热导率随温度升高而降低，随轴向应力增大而升高；高温条件会增强这种应力敏感性，而高孔隙砂岩（~14%）则相反，高温反而减弱应力敏感性。 [Wu 2025, pp. 6-8]
- 当轴向应力超过岩石的裂纹损伤应力 σ_cd 时，热导率转而下降，表明微裂纹扩展导致的热阻增加起主导作用。 [Wu 2025, pp. 8-10]
- 热膨胀系数在100–250°C呈稳定线性增长，可用α = α1 + α2·T 描述，矿物粒径越大热变形越显著。 [Wu 2025, pp. 10-12]
- 比热容随温度升高而单调增加，且可用Maier–Kelley方程拟合；高孔隙岩石（松辽砂岩）的比热容增幅远大于低孔隙花岗岩。 [Wu 2025, pp. 12-13]
- 在热提取模拟中，仅改变热导率对生产温度和寿命几乎无影响；而增加比热容可明显提升生产温度、延长储层寿命、降低注采压差并增加累积采热量。 [Wu 2025, pp. 17-22]

## Candidate Concepts
- [[thermal–mechanical coupling]]
- [[thermal conductivity]]
- [[specific heat capacity]]
- [[thermal expansion coefficient]]
- [[enhanced geothermal system]] (EGS)
- [[hydrothermal system]]
- [[fractured reservoir]]
- [[porous sandstone reservoir]]
- [[Gonghe granite]]
- [[Kangding granite]]
- [[Songliao sandstone]]
- [[heat extraction performance]]
- [[crack damage stress]] (σ_cd)
- [[phonon mean free path]]
- [[thermal cracking]]

## Candidate Methods
- [[steady-state divided bar method]] (ISRM)
- [[DRPL-3B thermal conductivity testing system]]
- [[ZRPY-1000 thermal expansion test system]]
- [[BRR specific heat capacity testing system (hybrid cooling)]]
- [[OpenGeoSys]]
- [[finite element method]]
- [[thermal–hydraulic coupling model]]
- [[discrete fracture network (DFN) model]]
- [[Maier–Kelley equation]] for specific heat capacity

## Connections To Other Work
- 热导率与孔隙率反相关，与先前研究一致。[Wu 2025, pp. 5-6, cite Sayed 2011; Robertson et al. 1974]
- 温度升高使声子平均自由程减小，是热导率下降的原因之一。[Wu 2025, pp. 6, cite Wen et al. 2015]
- 高应力下热导率变化与裂纹演化阶段（σ_cc, σ_ci, σ_cd, σ_c）对应。[Wu 2025, pp. 9, cite Cai et al. 2004]
- 石英相变（573°C）对热变形的影响与Sun et al. (2016) 一致。[Wu 2025, pp. 10]
- 比热容与温度的关系符合经典固体热容模型（Debye）和Maier–Kelley经验公式。[Wu 2025, pp. 12-13, cite Abdulagaov et al. 2018; Maier & Kelley 1932]
- 地热系统数值模拟通常基于有限元软件OpenGeoSys，并参考了Soultz EGS项目的注入/生产方案。[Wu 2025, pp. 15, cite Watanabe 2017]

## Open Questions
- 真三轴高温条件下岩石热物性的演化规律尚不清楚。
- 热-力-化多场耦合中岩石热物性动态变化对长期地热开采的影响有待研究。
- 热膨胀系数在热-水-力全耦合模型中对热提取性能的定量影响尚未评估（本研究中未耦合应力场）。
- 现场实测数据对数值模型的校验尚未开展。
- 高温裂隙花岗岩中有效热导率的微观机理（矿物热膨胀与裂纹竞争）需要更细致实验分析。
[Wu 2025, pp. 23-24]

## Source Coverage
所有提供的20个非空索引片段均已处理，覆盖整篇论文的引言、方法、实验、模拟和结论部分。索引文本总字符数97506，编译使用字符数97506，覆盖率（按字符）约98.96%，按源块覆盖率100%。所有信息均源自标识为 [Wu 2025, pp. X-X] 的片段，未添加任何片段外的数据或推断。
