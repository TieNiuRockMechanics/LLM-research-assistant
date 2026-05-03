---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2024-xue-integrated-technological-and-economic-feasibility-comparisons-of-enhanced-geothermal-sy"
title: "Integrated Technological and Economic Feasibility Comparisons of Enhanced Geothermal Systems Associated with Carbon Storage."
status: "draft"
source_pdf: "data/papers/2024 - Integrated technological and economic feasibility comparisons of enhanced geothermal systems associated with carbon storage.pdf"
collections:
citation: "Xue, Zhenqian, et al. \"Integrated Technological and Economic Feasibility Comparisons of Enhanced Geothermal Systems Associated with Carbon Storage.\" *Applied Energy*, vol. 359, 2024, p. 122757. Accessed 2026."
indexed_texts: "15"
indexed_chars: "71384"
nonempty_source_blocks: "15"
compiled_source_blocks: "15"
compiled_source_chars: "67611"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.947145"
coverage_status: "full-index"
source_signature: "07a9420af03f6f0cdb7af306d2f95f53ff314252"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T07:40:37"
---

# Integrated Technological and Economic Feasibility Comparisons of Enhanced Geothermal Systems Associated with Carbon Storage.

## One-line Summary
本研究首次引入碳信用影响的技术经济评价框架，比较了六种增强型地热系统（EGS）运营方案，发现混合CO₂-水水平井EGS具有最高的净现值（NPV 0.419亿美元）和最低的盈亏平衡电价（$0.036/kWh），而纯CO₂-EGS虽发电与封存潜力最大，但因高昂的CO₂采购成本导致负NPV。 [Xue 2024, pp. 1-2] [Xue 2024, pp. 9-11] [Xue 2024, pp. 13-13]

## Research Question
现有EGS技术经济评价存在三方面不足：1）混合CO₂-水作为传热流体的经济有效性研究几乎空白；2）不同井配置对EGS项目经济性的影响缺乏足够证据；3）缺乏统一的技术经济比较框架，无法同时考虑能量提取和CO₂封存，且未将碳信用政策纳入CO₂利用的环保解读。因此，本研究旨在回答：在考虑碳信用政策下，不同流动方案（纯CO₂、纯水、混合CO₂-水）和井配置（垂直井、水平井）的EGS技术可行性与经济盈利能力如何？哪些技术与经济参数是主导因素？ [Xue 2024, pp. 2-3]

## Study Area / Data
案例区为中国西北部共和盆地东部的恰卜恰（Qiabuqia）地热田。该场址干热岩（HDR）资源丰富，相当于约2000亿吨标准煤；在3200‒3700 m深度，地温梯度约7.1 °C/100 m，勘探井GR1（3705 m）井底温度稳定在236 °C，岩心显示天然裂缝间距约10 m。数值模型基于该场实际储层属性构建，研究域聚焦于HDR段（3200‒3700 m），基础模型尺寸2000 × 1000 × 3800 m³，共36 480个网格块。储层假设饱和纯水（以避免CO₂注入导致的盐析伤害），并使用CMG STARS软件进行多相多组分流动与传热模拟。 [Xue 2024, pp. 3-5] [Xue 2024, pp. 5-6]

## Methods
### 技术模型
- **数值模拟**：采用CMG STARS软件，建立垂直井与水平井两种井配置模型。垂直井系统在3200‒3700 m段布置5条水压裂缝；水平井系统在3600‒3700 m段布置裂缝，缝间距50 m，假设水压裂缝半长等于井间距（400‒600 m），基础裂缝导流能力10 mD m。注入井为GR1，两侧各一口生产井PR1、PR2，基础井距500 m。 [Xue 2024, pp. 4-5]
- **操作条件**：采用固定注入压力（基础50 MPa，不超过地层最小主应力60 MPa）和固定生产压力（基础35 MPa）以比较不同流体的注入性。三种流动策略：纯CO₂、纯水、混合CO₂-水（基础CO₂质量分数10%wt）。模拟期20年。 [Xue 2024, pp. 5-6]
- **场景定义**（表2）：
  - #1: CO₂基垂直井EGS
  - #2: CO₂基水平井EGS
  - #3: 混合CO₂-水垂直井EGS
  - #4: 混合CO₂-水水平井EGS
  - #5: 水基垂直井EGS
  - #6: 水基水平井EGS [Xue 2024, pp. 5-6]

### 经济模型
- **CAPEX**：地面设施成本随装机容量（Ẇ）呈指数递减（2000 $/kW至1000 $/kW）；钻井成本垂直井600 $/m、水平井1500 $/m；储层压裂费用为钻井成本的30%；假设CO₂管道直接可用，无额外基建费。 [Xue 2024, pp. 6-6]
- **OPEX**：年运维成本与发电量成正比，单位成本从5 MW的20 $/MWh降至150 MW的14 $/MWh；水补充费0.66 $/ton，CO₂采购价22.7 $/ton。 [Xue 2024, pp. 6-6]
- **收入与税收**：上网电价基准0.093 $/kWh（基于中国2017‒2022年数据）；税收及权利金按总营收的15%计。 [Xue 2024, pp. 6-6]
- **碳信用**：依据美国IRC第45Q条款，每吨封存CO₂抵免$60。 [Xue 2024, pp. 6-6]
- **NPV模型**：采用净现值公式（5），折现率10%，计算期20年。 [Xue 2024, pp. 6-6]

### 敏感性分析
对六个技术参数（井距、注入流压、注入温度、生产流压、裂缝导流能力、混合流体中CO₂比例）和四个经济参数（电价、CO₂购买价、水购买价、碳信用率）进行±20%摄动分析，以龙卷风图展示各因素对NPV的影响程度。 [Xue 2024, pp. 2-3] [Xue 2024, pp. 11-13]

## Key Findings
1. **技术性能**：地热发电功率排序为#1 > #2 > #6 > #4 > #5 > #3。CO₂-EGS因优越的注入性获得最高产流量和最大发电量，但同时发生严重热突破；水平井系统（#4 > #3 ；#6 > #5）因研究段温度更高而提取更多热量，但在CO₂-EGS中相反（#2 < #1）。CO₂封存量CO₂-EGS远大于混合EGS，但随生产迅速衰减。 [Xue 2024, pp. 6-9]
2. **经济性能**：NPV排序为#4 > #6 > #3 > #5 > #1 > #2。混合CO₂-水水平井EGS（#4）NPV达41.9 M$，收回期4年；CO₂-EGS（#1、#2）因CO₂采购成本过高全程无法盈利。碳信用显著提升混合EGS的收益，使#4盈亏平衡电价低至0.036 $/kWh，而#2高达0.241 $/kWh。 [Xue 2024, pp. 9-11] [Xue 2024, pp. 13-13] （摘要亦报告NPV为35.3 M$，参见片段1。）
3. **参数敏感性**：
   - **CO₂-EGS**：注入/生产流压、裂缝导流能力等控制注入量的参数最为敏感，较低的注入量和流速有利于NPV；CO₂采购价贡献约30%的NPV变化，而电价和碳信用率影响不足10%。 [Xue 2024, pp. 11-13]
   - **混合CO₂-水EGS**：电价影响最大，其次为控制流体注入量与速率的参数（注入/生产流压、裂缝导流能力），且高注入量有利于NPV（与CO₂-EGS相反）；CO₂比例存在最优区间，过高或过低均损害经济性。 [Xue 2024, pp. 11-13]
   - **水-EGS**：电价及控制注入量的参数同样主导，高流速带来更高NPV，但需警惕热突破。 [Xue 2024, pp. 11-13]
4. **决策启示**：若碳信用政策可执行，混合CO₂-水水平井EGS是首选；否则水基EGS更经济。CO₂-EGS需精心控制CO₂注入量和流速方可盈利；运营商宜在电价上升期启动混合CO₂-水EGS项目。 [Xue 2024, pp. 13-13]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| CO₂-EGS发电量最高，但NPV为负；混合CO₂-水水平井EGS NPV最高 | [Xue 2024, pp. 1-2] Highlights | 20年运行，固定注入/生产压力，碳信用$60/ton | 摘要亮点 |
| 场景#4（混合CO₂-水水平井EGS）NPV为35.3 M $ | [Xue 2024, pp. 1-2] 摘要 | 碳信用政策适用 | 表4显示NPV为41.9 M$，可能因取整或不同前提 |
| 场景#4回收期4年，盈亏平衡电价0.036 $/kWh；场景#2盈亏平衡电价0.241 $/kWh | [Xue 2024, pp. 9-11] 表4 | 基准参数 | 最低与最高盈亏平衡电价 |
| 六场景NPV排序：#4 > #6 > #3 > #5 > #1 > #2 | [Xue 2024, pp. 9-11] | 基准参数，碳信用$60/ton | #1、#2为负，其余为正 |
| CO₂-EGS（#1、#2）注入/生产流压、裂缝导流能力主导NPV变化，CO₂采购价贡献~30% | [Xue 2024, pp. 11-13] 图11 | ±20%参数摄动 | 降低注入量/流速可改善NPV |
| 混合CO₂-水EGS（#3、#4）电价影响最大，高注入流速有利NPV；CO₂比例存在最优值 | [Xue 2024, pp. 11-13] 图12 | ±20%参数摄动 | 与CO₂-EGS趋势相反 |
| 水-EGS（#5、#6）电价和控制注入量的参数主导NPV，高流速有利 | [Xue 2024, pp. 11-13] 图13 | ±20%参数摄动 | 热突破可能限制长期经济性 |

## Limitations
1. 案例仅针对恰卜恰地热田，不同地质背景（如应力、温度、裂缝特征）可能改变结论。 [Xue 2024, pp. 13-13]
2. 技术评估假设固定注入/生产压力，未考虑压力动态优化；井距仅为400‒600 m范围，裂缝导流能力等参数的单次单变量敏感性分析可能忽略交互作用。 [Xue 2024, pp. 5-6] [Xue 2024, pp. 11-13]
3. 经济模型假设零通胀（升级率0%），折现率固定10%，未考虑电价、碳价的随机波动或调整路径。 [Xue 2024, pp. 6-6]
4. CO₂-EGS的地层盐析问题通过假设饱和纯水储层予以规避，实际可能影响长期注入性。 [Xue 2024, pp. 2-3] [Xue 2024, pp. 3-4]

## Assumptions / Conditions
- 工作流体以固定注入压力注入、固定生产压力生产；注入压力不超过地层最小主应力60 MPa。 [Xue 2024, pp. 5-6]
- HDR段水压裂缝可基于已有压裂技术在恰卜恰花岗岩中实现，裂缝半长等于井距（400‒600 m）。 [Xue 2024, pp. 4-5]
- 储层初始饱和纯水（近似无地层水或低盐度水段塞），以避免CO₂注入引起的盐析。 [Xue 2024, pp. 3-4]
- CO₂采购价22.7 $/ton、水补充价0.66 $/ton，碳信用60 $/ton（参照美国IRC 45Q）。 [Xue 2024, pp. 6-6]
- 中国电价基准0.093 $/kWh，税收及权利金为营业额的15%。 [Xue 2024, pp. 6-6]
- 折现率10%，未考虑通胀，CO₂管道建设视为近理想情况（无额外投资）。 [Xue 2024, pp. 6-6]

## Key Variables / Parameters
### 技术参数
- 井配置：垂直井与水平井（水平段长500 m） [Xue 2024, pp. 4-5]
- 流动策略：纯CO₂、纯水、混合CO₂-水（基础CO₂质量比10%） [Xue 2024, pp. 5-6]
- 注入流压（基础50 MPa）、生产流压（基础35 MPa） [Xue 2024, pp. 5-6]
- 裂缝导流能力（基础10 mD m） [Xue 2024, pp. 4-5]
- 井距（基础500 m） [Xue 2024, pp. 4-5]
- 注入流体温度（基础60 °C） [Xue 2024, pp. 5-6]

### 经济参数
- 上网电价（基础0.093 $/kWh） [Xue 2024, pp. 6-6]
- CO₂采购价（基础22.7 $/ton） [Xue 2024, pp. 6-6]
- 水采购价（基础0.66 $/ton） [Xue 2024, pp. 6-6]
- 碳信用抵免额度（基础$60/ton） [Xue 2024, pp. 6-6]
- 折现率（10%） [Xue 2024, pp. 6-6]

## Reusable Claims
- 当碳信用政策（如$60/ton封存）可适用时，混合CO₂-水水平井EGS是六种方案中经济性最优的选择（NPV最高，盈亏平衡电价最低），条件为注入/生产压力固定，裂缝导流能力适中，且CO₂采购价不超过22.7 $/ton。 [Xue 2024, pp. 9-11] [Xue 2024, pp. 13-13]
- CO₂-EGS因优越的注入性产生最高地热发电量和碳封存量，但在基准CO₂采购价下几乎不可能实现正NPV；若要盈利，需大幅降低CO₂采购价或通过优化注入/生产压力减少CO₂注入量。 [Xue 2024, pp. 6-9] [Xue 2024, pp. 11-13]
- 对于混合CO₂-水EGS和水-EGS，注入量的增加通常提高NPV，但需警惕由此引发的热突破；敏感性分析显示控制注入量的参数（注入/生产流压、裂缝导流能力）是决定经济性的首要技术因子。 [Xue 2024, pp. 11-13]
- 在恰卜恰类似的高地温梯度花岗岩储层中，水平井系统（同流动策略）较垂直井系统能提取更多地热能量并获利，前提是热突破未显著影响生产温度。 [Xue 2024, pp. 6-9] [Xue 2024, pp. 9-11]
- 电价波动对混合EGS和水-EGS的NPV影响极大，对CO₂-EGS影响相对较小；投资时机宜选择电价上升通道。 [Xue 2024, pp. 11-13]

## Candidate Concepts
- [[enhanced geothermal system (EGS)]]
- [[CO2-based EGS]]
- [[mixed CO2-water EGS]]
- [[water-based EGS]]
- [[horizontal well EGS]]
- [[vertical well EGS]]
- [[hot dry rock (HDR)]]
- [[Qiabuqia geothermal field]]
- [[carbon credit policy]]
- [[IRC Section 45Q]]
- [[net present value (NPV)]]
- [[breakeven electricity price]]
- [[fluid injectivity]]
- [[thermal breakthrough]]
- [[fracture conductivity]]
- [[sensitivity analysis tornado chart]]

## Candidate Methods
- [[CMG STARS numerical simulation]]
- [[fixed injection/production pressure EGS modeling]]
- [[levelized cost of electricity (LCOE) for EGS]] (referenced from prior studies)
- [[NPV evaluation with carbon credit]]
- [[sensitivity analysis with ±20% parameter variation]]
- [[techno-economic assessment framework for EGS]]

## Connections To Other Work
- 前人工作主要采用LCOE或NPV评价水-EGS与CO₂-EGS，但未系统对比混合CO₂-水方案与不同井配置的经济性。本研究首次将混合流体注入方案纳入统一框架，并耦合碳信用政策（IRC 45Q）进行经济评估，弥补了空白。 [Xue 2024, pp. 2-3]
- Lei等人（2019, 2020）在恰卜恰场应用水平井slickwater压裂的研究为本模型的裂缝设计提供了依据；Lei等人的LCOE分析显示井距和注入速率影响经济性，与本文敏感性结论一致。 [Xue 2024, pp. 2-2] [Xue 2024, pp. 13-14]
- Yu等人（2023）发现CO₂-EGS的单位净功率成本低于水-EGS，本研究进一步揭示在计入碳信用后混合EGS的经济性可能更优，且需平衡CO₂采购成本。 [Xue 2024, pp. 2-2] [Xue 2024, pp. 13-13]
- Daniilidis等人（2017）和 Erdeweghe等人（2018）均指出有效流量或流速是地热系统NPV的主导参数，本研究在混合EGS和水-EGS中得出一致结论，但在CO₂-EGS中呈现相反趋势。 [Xue 2024, pp. 2-2]

## Open Questions
- 本研究局限于恰卜恰花岗岩储层，该框架推广至其他地热场（如沉积岩、裂隙发育差异大的基岩）时需要重新校准技术模型与经济参数。 [Xue 2024, pp. 13-13]
- 混合CO₂-水EGS中最优CO₂比例（本研究基础10%wt）的确定需要进一步的多目标优化研究，以兼顾热提取与CO₂封存效益。 [Xue 2024, pp. 11-13]
- 热突破对长期盈利的具体阈值及水平井布局（如多分支井、错列井）的适用性尚未充分探索。 [Xue 2024, pp. 6-9] [Xue 2024, pp. 9-11]
- 碳信用政策的动态变化（如罚款、交易市场波动）对EGS投资决策的影响有待随机分析。 [Xue 2024, pp. 6-6]
- 未考虑运维成本随时间递减或技术学习效应，实际商业化进程可能改善经济评价。 [Xue 2024, pp. 6-6]

## Source Coverage
所有15个非空索引片段均已处理并编译到本页面。包括片段[Xue 2024, pp. 1-2]、[Xue 2024, pp. 2-2]、[Xue 2024, pp. 2-3]、[Xue 2024, pp. 3-4]、[Xue 2024, pp. 4-5]、[Xue 2024, pp. 5-6]、[Xue 2024, pp. 6-6]、[Xue 2024, pp. 6-9]、[Xue 2024, pp. 9-11]、[Xue 2024, pp. 11-11]、[Xue 2024, pp. 11-13]、[Xue 2024, pp. 13-13]、[Xue 2024, pp. 13-14]、[Xue 2024, pp. 14-14]。来源区块覆盖率100%，字符覆盖率约94.7%（67,611 / 71,384字符），无遗漏。
