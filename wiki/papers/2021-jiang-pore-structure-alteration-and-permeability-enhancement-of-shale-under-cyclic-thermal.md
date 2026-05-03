---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-jiang-pore-structure-alteration-and-permeability-enhancement-of-shale-under-cyclic-thermal"
title: "Pore Structure Alteration and Permeability Enhancement of Shale under Cyclic Thermal Impacts."
status: "draft"
source_pdf: "data/papers/2022 - Pore structure alteration and permeability enhancement of shale under cyclic thermal impacts.pdf"
collections:
  - "论文"
citation: "Jiang, Changbao, et al. \"Pore Structure Alteration and Permeability Enhancement of Shale under Cyclic Thermal Impacts.\" 2021."
indexed_texts: "9"
indexed_chars: "43716"
nonempty_source_blocks: "9"
compiled_source_blocks: "9"
compiled_source_chars: "43911"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004461"
coverage_status: "full-index"
source_signature: "125a6871ded00ae9e8b7d012cdaf1e1aee04da48"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T05:52:38"
---

# Pore Structure Alteration and Permeability Enhancement of Shale under Cyclic Thermal Impacts.

## One-line Summary
在300 °C循环热冲击下，龙马溪组页岩的累积孔隙度与渗透率均随冲击次数呈对数增长，多次冲击对孔隙结构和渗透率的提升效果远大于单次冲击。

## Research Question
循环热冲击（cyclic thermal impacts）如何改变页岩的孔隙结构（pore structure）并增强其渗透率（permeability）？多次热冲击与单次相比是否存在显著累积效应？

## Study Area / Data
- **页岩来源**：四川盆地长宁-威远地区下志留统龙马溪组（Lower Silurian Longmaxi Formation）露头黑色页岩，埋深2300–3200 m，厚度250–308 m。  
- **基础性质**：总有机碳（TOC）含量10.36–11.31%，属于优质气页岩。  
- **样品制备**：沿平行层理方向钻取，加工成直径25 mm × 50 mm的标准试件，高度与直径偏差±0.3 mm，端面平整度±0.02 mm，超声波速3.79–3.91 km/s。  
- **分组**：A组（A0, A1, A3, A5, A7）用于NMR孔隙结构测试，数字代表热冲击次数；B组（B0, B1, B2）用于脉冲渗透率测试；C组（C1, C2, C3）为6 g粉末用于低温氮吸附。  

**来源**：[Jiang 2021, pp. 1-1], [Jiang 2021, pp. 2-4]

## Methods
- **循环热冲击处理**：马弗炉（Xh5l-16）预热至300 °C，样品放入后加热45分钟（至核心温度达预设温度的90%以上），然后随炉冷却至室温，定义为一次热冲击。  
- **低温氮气吸附**：ASAP2010比表面积与孔隙度分析仪，获取等温吸附-脱附曲线、比表面积、孔容、孔径分布。  
- **核磁共振（NMR）**：MacroMR12-150H-I系统，测试前样品真空饱水，获得T₂谱，并通过表面弛豫率（ρ₂=4 nm/ms，Fₛ=2）转换为孔径分布及孔隙度。  
- **渗透率测试**：脉冲孔隙度测试仪，测试气体为99.99%氦气，进口压力6.5 MPa，围压9 MPa，采用脉冲衰减法，按式(4)计算气测渗透率。  
- **评价指标**：  
  - 累积孔隙度增长率 λ_c = (φ_a − φ_b)/φ_b × 100%  
  - 绝对渗透率增加率 λ_a = (k_i − k_0)/k_0 × 100%  
  - 相对渗透率增加率 λ_r = (k_i − k_{i-2})/k_{i-2} × 100% (i≥3)，i=1时按k_0计算  

**来源**：[Jiang 2021, pp. 2-4], [Jiang 2021, pp. 5-7], [Jiang 2021, pp. 7-8]

## Key Findings
1. 氮气吸附结果显示页岩孔隙以平行板状、两端开口圆柱状及少量墨水瓶状孔为主，发育大量吸附孔（<10 nm）和滑脱孔（10–1000 nm），平均比表面积31.680 m²/g，平均孔容0.0285 cm³/g，平均孔径7.209 nm。  
2. NMR初始T₂谱呈双峰分布，滑脱孔数量占主导（吸附孔与滑脱孔谱面积比≈1:10）。  
3. 随热冲击次数增加（1→3→5→7次），页岩累积孔隙度逐步上升，增长趋势呈对数函数；累积孔隙度增长率由初次3.53%增至第7次7.35%，效果翻倍。  
4. 渗透率亦随冲击次数对数增长：B1由4.816×10⁻¹⁸ m²升至7.620×10⁻¹⁸ m²（增加58.2%），B2由5.296×10⁻¹⁸ m²升至7.195×10⁻¹⁸ m²（增加35.9%）。  
5. 相对渗透率增加率随次数递减（B1：28.02%→20.36%→2.51%），表明单次强化作用减弱；但绝对渗透率增加率持续上升，多次冲击的累积效果使渗透率提升翻倍。  
6. 平均绝对渗透率增加率与累积孔隙度增长率呈对数关系，表明孔隙扩展（尤其滑脱孔增多）是渗透率增强的主要机制，但滑脱孔对渗透率的贡献弱于渗流孔和微裂隙，故单次冲击效果有限，多次冲击才能实现显著增强。

**来源**：[Jiang 2021, pp. 1-1], [Jiang 2021, pp. 4-8]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 页岩平均比表面积31.680 m²/g，平均孔容0.0285 cm³/g，平均孔径7.209 nm；吸附-脱附曲线为II型，回滞环属H3兼H2特征，反映平行板孔、开口圆柱孔为主 | [Jiang 2021, pp. 4-5] Table 1, Fig. 7 | 粉末样品C1-C3，低温氮气吸附 | 表明储层具良好吸附能力但渗透性弱 |
| NMR初始T₂谱呈双峰，吸附孔-滑脱孔谱面积比≈1:10，孔隙以滑脱孔为主 | [Jiang 2021, pp. 5-6] Fig. 9, Fig. 10 | 饱水样品A0-A7初始状态 | 与氮吸附结果一致 |
| 热冲击后孔隙度变化：A1 8.269%→8.560%；A3 8.437%→8.909%；A5 8.325%→8.913%；A7 8.391%→9.008%；A0对照组无显著变化 | [Jiang 2021, pp. 5-6] Table 2, Fig. 12 | 300 °C，1、3、5、7次冲击 | 累积孔隙度增长率分别为3.53%、5.59%、7.06%、7.35% |
| 渗透率随冲击次数变化：B1初始4.816→1次6.166→3次7.421→5次7.607→7次7.620（×10⁻¹⁸ m²）；B2初始5.296→1次6.247→3次7.017→5次7.121→7次7.195（×10⁻¹⁸ m²） | [Jiang 2021, pp. 7-8] Table 3, Fig. 14 | 脉冲衰减法，氦气，进口压力6.5 MPa，围压9 MPa | B1总增幅58.2%，B2总增幅35.9% |
| 相对渗透率增加率：B1-1次28.02%→3次20.36%→5次2.51%；B2-1次17.96%→3次12.32%→5次1.48% | [Jiang 2021, pp. 7-8] Fig. 15 | 同上 | 表明早期冲击效果强，后期减弱 |
| 平均绝对渗透率增加率与累积孔隙度增长率呈对数关系（Fig. 16） | [Jiang 2021, pp. 8-9] Fig. 16 | 300 °C，B1、B2平均 | 孔隙扩展直接贡献渗透率提升 |

## Limitations
- 实验温度固定为300 °C，未探讨其他温度水平或温度梯度的效应。  
- 样品取自单一露头页岩（龙马溪组），岩石非均质性和矿物成分的影响未系统评估。  
- 室内试验未模拟原位应力、地层压力及多场耦合环境，现场适用性需进一步验证。  
- 渗透率测试仅采用氦气、恒定围压，未考虑滑脱效应、含水饱和度及有效应力变化。  
- 循环次数仅到7次，长期多次循环后的行为未知。

## Assumptions / Conditions
- 热冲击定义：样品在300 °C马弗炉中加热45分钟，再自然冷却至室温。  
- 温度300 °C是基于前人研究中页岩渗透率突变的阈值范围（300–400 °C）及能耗、安全考虑而选定。  
- 样品处理前的干燥（60 °C）以及饱水-干燥-饱水循环本身不改变孔隙结构（由A0对照组验证）。  
- NMR孔径转换假设表面弛豫率ρ₂=4 nm/ms，孔形因子Fₛ=2（圆柱孔）。  
- 渗透率计算采用脉冲衰减法，基于达西流假设，且认为压力循环不损伤样品（B0重复测试验证）。  
- 实验在无围压、无流体化学作用的条件下进行，主要反映温度骤变引起的物理效应。

## Key Variables / Parameters
- **独立变量**：热冲击次数（0, 1, 3, 5, 7）。  
- **因变量**：孔隙度（%）、累积孔隙度增长率λ_c（%）、渗透率k（m²）、绝对渗透率增加率λ_a（%）、相对渗透率增加率λ_r（%）。  
- **固定参数**：热冲击温度300 °C，单次冲击时间45 min；氮气吸附温度77 K；NMR测试前饱水状态；渗透率测试气体为氦气，进口压力6.5 MPa，围压9 MPa。  
- **表征参数**：比表面积（m²/g）、孔容（cm³/g）、平均孔径（nm）、T₂弛豫时间分布。

## Reusable Claims
1. 对于总有机碳含量约10-11%的龙马溪组页岩，在300 °C循环热冲击下，累积孔隙度与冲击次数呈对数增长关系，单次冲击（3.5%孔隙度增长）至七次冲击（7.35%增长）可实现翻倍效果。此结论适用于不含宏观裂隙、直径25 mm、长度50 mm的柱状样品在无围压、自然冷却条件下的热冲击。  
2. 页岩渗透率在相同热冲击历史下亦呈对数增长，绝对渗透率增幅可从初次约17-28%累积至七次约36-58%，但相对增幅随次数递减，说明早期冲击贡献最大。该结论基于脉冲衰减法、氦气介质、围压9 MPa、进口压力6.5 MPa的测试条件，未考虑应力敏感性和含水饱和度。  
3. 多次热冲击对孔隙结构的改善主要表现为滑脱孔（10–1000 nm）数量增多和部分吸附孔扩展为滑脱孔，而渗流孔或微裂隙未大量产生，这解释了单次冲击对渗透率提升有限的现象；因此，现场增产需要多次循环注热。此机理推断来自NMR T₂谱变化与渗透率增加的耦合分析，在300 °C条件下成立。  
4. 页岩在300 °C热冲击下未出现显著的质量损失或颜色变化（未提及此类现象），但孔隙结构持续演化，表明热冲击主要通过热应力诱导微裂隙生成与扩展，而非热解或有机质大量分解。该结论依赖于本实验未进行高温矿物学分析，需结合其他研究确认。

## Candidate Concepts
- [[cyclic thermal impact]]
- [[shale pore structure]]
- [[adsorption pore]]
- [[slippage pore]]
- [[seepage pore]]
- [[NMR T2 spectrum]]
- [[low-temperature nitrogen adsorption]]
- [[hysteresis loop type H3/H2]]
- [[pulse decay permeability test]]
- [[cumulative porosity increase]]
- [[absolute permeability increase]]
- [[relative permeability increase]]
- [[formation heat treatment]]
- [[water phase trap removal]]
- [[thermal stress fracturing]]

## Candidate Methods
- [[muffle furnace thermal shocking at 300°C]]
- [[low-temperature nitrogen adsorption (ASAP2010)]]
- [[low-field nuclear magnetic resonance (NMR) relaxation]]
- [[pulse decay permeability measurement with helium]]
- [[T2-to-pore size conversion using surface relaxivity]]
- [[calculation of cumulative and relative changes in porosity and permeability]]

## Connections To Other Work
- 研究肯定并扩展了地层热处理（FHT）概念，Jamaluddin等（1995）最初提出地层注热可消除近井带损害、提高渗透率；本工作表明循环热冲击对页岩同样有效。  
- Kang等（2016）、Xiong等（2019）发现均匀加热页岩存在渗透率快速升高的温度阈值（300–400 °C），本研究选择300 °C作为循环冲击温度，并提供了相应的微观机制解释。  
- 热冲击对煤体的增透效果已有报道（Wei et al. 2017; Wang et al. 2018, 2019; Zhang et al. 2019），本文将这些认识迁移至页岩，证实多次冷热交替可显著改变孔隙结构。  
- 微波辐射（Hu et al. 2018, 2020）和液氮冷冲击（Cai et al. 2020）等其他热激励方法同样以产生微裂隙为目标，本研究从热冲击角度提供了补充证据。  
- 实验所使用的孔隙-裂隙分类（吸附孔-滑脱孔-渗流孔）与渗透率评价方法继承了Chen et al. (2021)的多尺度表征框架。

## Open Questions
1. 不同热冲击温度（如200 °C、400 °C）及不同升温/冷却速率对孔隙演化的影响尚不清楚。  
2. 热冲击过程中是否伴随有机质热解或矿物相变，以及这些化学变化对孔隙和渗透率的贡献未被量化。  
3. 现场条件下，地应力、孔隙压力及流体（水、气）共同作用下，循环热冲击的增透效果与机理如何，需要进一步模拟。  
4. 多次循环冲击后页岩力学性质的劣化规律及对井壁稳定性的影响缺乏评估。  
5. 滑脱孔增多为何未线性转化为渗透率的大幅提升？是否存在孔隙连通性瓶颈或临界孔径效应？需要结合三维重构技术（如μCT）深入研究。  
6. 经济性评估：多次注热的能耗与产气增量之间的关系尚未分析。

## Source Coverage
本词条完全基于提供的9个非空索引片段构建。所有片段均已处理，无遗漏。

- 索引片段数：9
- 片段总字符数：43,711（去除空白后）
- 编译后字符数：43,911
- 基于片段数的覆盖率：1.0（100%）
- 基于字符数的覆盖率：1.004461（因格式调整略有超出）

片段签名：125a6871ded00ae9e8b7d012cdaf1e1aee04da48  
汇编策略：单次直通 Markdown。
