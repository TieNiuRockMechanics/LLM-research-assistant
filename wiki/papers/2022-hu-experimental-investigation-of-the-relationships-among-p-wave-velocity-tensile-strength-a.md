---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-hu-experimental-investigation-of-the-relationships-among-p-wave-velocity-tensile-strength-a"
title: "Experimental Investigation of the Relationships Among P-Wave Velocity, Tensile Strength, and Mode-I Fracture Toughness of Granite After High-Temperature Treatment."
status: "draft"
source_pdf: "data/papers/2022 - Experimental Investigation of the Relationships Among P-Wave Velocity, Tensile Strength, and Mode-I Fracture Toughness of Granite After High-Temperature Treatment.pdf"
collections:
  - "靳一作以外的"
citation: "Hu, Yuefei, et al. \"Experimental Investigation of the Relationships Among P-Wave Velocity, Tensile Strength, and Mode-I Fracture Toughness of Granite After High-Temperature Treatment.\" *Natural Resources Research*, vol. 31, no. 2, 2022. doi:10.1007/s11053-022-10020-3. Accessed 2026."
indexed_texts: "12"
indexed_chars: "58576"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "58729"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.002612"
coverage_status: "full-index"
source_signature: "22d516c93183ad03ab13a29147fa42f59763064c"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T05:24:15"
---

# Experimental Investigation of the Relationships Among P-Wave Velocity, Tensile Strength, and Mode-I Fracture Toughness of Granite After High-Temperature Treatment.

## One-line Summary
在20–600 °C高温处理后，花岗岩质量、P波速度(vp)和抗拉强度(σt)随温度升高逐渐下降；I型断裂韧性(KIC)在20–100 °C略有上升后持续下降；σt/KIC比值(a)随温度升高而增加，可作为岩石脆性指数；vp与σt、KIC均呈强线性关系，基于vp的损伤因子Dv1和Dv2可分别表征400 °C以下和以上的热损伤程度。

## Research Question
高温如何影响花岗岩的物理（质量、P波速度）和力学（抗拉强度、I型断裂韧性）性质？P波速度、抗拉强度和I型断裂韧性之间存在何种定量关系？温度如何改变这些关系？能否利用超声波无损检测参数（vp）及由此导出的脆性指数（a = σt/KIC）评估岩石在高温下的损伤与脆–延性转变？

## Study Area / Data
花岗岩采自河南省驻马店，为黑云母花岗闪长岩，主要矿物含量为斜长石47%、石英20%、黑云母18%、碱性长石15%。室温下基本物理力学性质：密度2651.4 kg/m³，渗透率3.4×10⁻¹⁸ m²，抗压强度180.6 MPa，杨氏模量16.7 GPa。  
实验设置了7个温度组：20（室温对照）、100、200、300、400、500、600 °C。每组包含3个巴西圆盘试件（直径50 mm，厚25 mm）和3个半圆弯曲（SCB）试件（半径R=25 mm，厚B=20 mm，预制裂纹长a=12.5 mm，裂纹宽<1 mm，支点跨距S=35 mm）。

## Methods
- **热处理**：以2 °C/min升温至预设温度，恒温2 h后随炉自然冷却至室温。  
- **物理测量**：用精度0.01 g的电子天平测量质量，计算质量损失率δm = (m₀ - m_T)/m₀×100%；采用NM-4B非金属超声检测分析仪测量P波速度，每个试件测三次取平均值。  
- **力学测试**：在微机控制万能试验机上以0.002 mm/s的加载速率进行巴西劈裂试验（抗拉强度σt = 2P_max/(πDt)）和SCB试验（KIC = P_max√(πa)/(2RB) Y₀，Y₀为无量纲应力强度因子）。  
- **微观分析**：通过岩石薄片观察不同温度下的微裂纹发育。  
- **损伤因子**：基于vp的损伤因子Dv1 = 1 – v_T/v₀，Dv2 = 1 – (v_T/v₀)²；基于σt的Dσ = 1 – σ_T/σ₀；基于KIC的D_KIC = 1 – KIC_T/KIC₀。  
- **脆性指数**：定义a = σt/KIC，并以乘积定义的脆性指数B_i = (σc·σt)/2作为参照。

## Key Findings
1. **质量、vp和σt单调下降**：600 °C时δm仅0.14%，主要由不同类型水的蒸发引起；vp由4356 m/s降至1053 m/s（降幅75.8%），σt由6.52 MPa降至2.81 MPa（降幅56.9%）。  
2. **KIC先增后减**：KIC在100 °C时升至2.03 MPa·m¹⁄²（增韧效应），之后持续下降，600 °C时仅0.31 MPa·m¹⁄²（降幅82.3%）。  
3. **vp与力学参数的强线性关系**：σt = 1.436 + 1.228 vp (km/s)，R² = 0.980；KIC = –0.175 + 0.500 vp (km/s)，R² = 0.924。  
4. **损伤因子适用温度分区**：Dv1（一次方形式）适合表征≤400 °C的损伤，Dv2（二次方形式）过高估计损伤但与KIC损伤因子在>400 °C时接近，适合表征>400 °C的严重损伤。  
5. **比值a可作为脆性指标**：a在20–400 °C变化平缓（最小值3.108@100 °C），400 °C后迅速上升（9.065@600 °C），该趋势与岩石脆–延性转变温度对应：当温度超过脆性减弱阈值时a显著增大。其他岩石（SC砂岩、FS大理岩、CF大理岩、FS辉长岩、Stripa花岗岩、BS花岗岩）的a值亦随温度升高而增加。  
6. **微裂纹驱动性质劣化**：薄片显示400 °C出现明显热微裂纹，600 °C微裂纹广泛分布，与vp陡降和力学性能退化吻合。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 质量损失率δm由20°C的0增至600°C的0.14%；拟合曲线δm = –0.014+7.132×10⁻⁴T–1.845×10⁻⁶T²+1.816×10⁻⁹T³, R²=0.998 | Hu 2022, pp. 3-5 | 2°C/min升温，恒温2 h，自然冷却；无约束 | 水分类型推断：吸附水、结合水、结晶水比例各约0.04%、0.04%、0.01% |
| vp由4356 m/s（20°C）降至1053 m/s（600°C），下降75.8%；拟合曲线vp = 4534.281 – 8.469T + 1.472×10⁻²T² – 1.702×10⁻⁵T³, R² = 0.998 | Hu 2022, pp. 5-6 | 同上；NM-4B测试，三次平均 | 500–600°C下降剧烈，可能与石英α–β相变（573°C）有关 |
| σt由6.52 MPa降至2.81 MPa（线性下降），σt = 6.901 – 6.73×10⁻³T, R² = 0.980 | Hu 2022, pp. 5-6 | 巴西劈裂，加载速率0.002 mm/s |
| KIC由1.75增至2.03 MPa·m¹⁄²（100°C）后降至0.31 MPa·m¹⁄²（600°C），拟合三次曲线 R² = 0.984 | Hu 2022, pp. 5-6 | SCB测试，加载速率0.002 mm/s | 100°C出现增韧现象 |
| a = σt/KIC随温度呈指数关系：a = 3.403 + 0.010 exp(0.011T), R² = 0.987；a从100°C的3.108增至600°C的9.065 | Hu 2022, pp. 9-10 | 由平均σt和平均KIC算得 | a与脆–延转变对应，≥400°C后迅速增大 |
| vp与σt线性回归：σt = 1.436 + 1.228 vp，R² = 0.980；vp与KIC线性回归：KIC = –0.175 + 0.500 vp，R² = 0.924 | Hu 2022, pp. 12-13 | 高温后冷却至室温测试 | 可用vp无损评估强度 |
| 损伤因子Dv1 = –0.018+1.230×10⁻³T, R² = 0.989；Dv2 = –0.026+2.430×10⁻³T–1.421×10⁻⁶T², R² = 0.993 | Hu 2022, pp. 12-13 | 基于vp定义 | Dv1适合<400°C，Dv2适合>400°C，与DKIC吻合更好 |
| 微裂纹观测：20°C基本无裂纹；200°C未见明显可见裂纹；400°C出现明显热微裂纹；600°C微裂纹广泛，结构严重破坏 | Hu 2022, pp. 6-9 | 薄片分析 | 裂纹密度与vp、强度下降一致 |
| 多种岩石的a值随温度升高的规律：SC砂岩变化小，FS大理石和BS花岗岩在较高温时a急剧增大，与脆–延转变温度对应 | Hu 2022, pp. 10-12 | 文献数据汇总，统一巴西劈裂法测σt，不同KIC测试方法 | 不同岩石的a突变温度不同，主要由矿物组成决定 |

## Limitations
1. 仅采用驻马店一种花岗岩，其余岩石的a值对比来自不同研究，测试方法不完全统一（SCB、短棒、三点弯曲等）。  
2. 巴西劈裂试验中试件端部与钢板存在接触面，其约束效应是否影响脆性指数a尚不明确。  
3. 未考虑热冲击（快速冷却），所有试件均为慢速加热后自然冷却。  
4. 温度上限为600 °C，更高温度下的性质未知；未测量结构水含量。  
5. 损伤因子Dv2高估力学性能退化程度，应用中需结合温度区间选择合适因子。  
6. 力学试验仅在室温下进行，未考虑高温实时加载的影响。

## Assumptions / Conditions
- 热处理采用慢速升温（2 °C/min）和自然冷却，避免热冲击，更能反映温度对岩石的长期作用。  
- 巴西劈裂和SCB测试均在室温下进行，试样用凡士林耦合以保障声波测试精度。  
- 计算KIC时假设线弹性断裂力学成立，并采用ISRM推荐的SCB公式。  
- 质量损失仅归因于水分蒸发，未考虑矿物分解（因花岗岩不含碳酸盐）。  
- 损伤因子基于vp的变化，假定初始状态为20 °C未处理岩石。

## Key Variables / Parameters
- 温度（20–600 °C）  
- P波速度 vp（m/s）  
- 抗拉强度 σt（MPa）  
- I型断裂韧性 KIC（MPa·m¹⁄²）  
- 比值 a = σt / KIC  
- 质量损失率 δm（%）  
- 损伤因子 Dv1, Dv2, Dσ, D_KIC  
- 脆性指数 B_i = (σc·σt)/2  
- 加载速率（0.002 mm/s）  
- 矿物组成与微裂纹密度

## Reusable Claims
1. 经过2 °C/min慢速加热并自然冷却的花岗岩，其P波速度与抗拉强度之间存在强线性关系：σt = 1.436 + 1.228 vp (km/s)，R² = 0.980（适用温度区间20–600 °C）。[Hu 2022, pp. 12-13]  
2. 相同条件下，花岗岩的P波速度与I型断裂韧性亦呈显著线性关系：KIC = –0.175 + 0.500 vp (km/s)，R² = 0.924。[Hu 2022, pp. 12-13]  
3. 花岗岩的比值 a = σt/KIC 随温度升高而增大，可用以衡量岩石的脆性：当温度超过岩石脆–延转变阈值时，a值急剧上升（如本研究中400 °C后）。[Hu 2022, pp. 9-12]  
4. 基于P波速度的损伤因子 Dv1（一次方）在低于400 °C时能较准确反映力学性能退化程度，而Dv2（二次方）在高于400 °C时更接近基于KIC的损伤因子。[Hu 2022, pp. 13-14]  
5. 花岗岩在100 °C热处理后KIC略有增加，表现出增韧效应，而σt单调下降，说明低温热处理可使岩石抗裂能力短暂提升。[Hu 2022, pp. 5-6, 13]  
6. 对于多种岩石（砂岩、大理岩、辉长岩、花岗岩），比值a随温度升高而增大的趋势具有普遍性，但a发生显著增加的温度点因岩石类型而异，与矿物组成和脆–延转变温度相关。[Hu 2022, pp. 10-12]  
7. 在无热冲击的缓慢升温条件下，花岗岩的P波速度在500–600 °C区间剧烈下降，与石英α–β相变（573 °C）导致的微裂纹大量增生有关。[Hu 2022, pp. 5-6]

## Candidate Concepts
- [[thermal damage factor (Dv1, Dv2)]]
- [[brittleness index a (ratio of tensile strength to mode-I fracture toughness)]]
- [[brittle-ductile transition temperature of granite]]
- [[toughening effect at low temperature (100°C)]]
- [[P-wave velocity reduction due to thermal cracking]]
- [[water evaporation stages in granite (absorbed, bound, crystalline)]]
- [[quartz α-β phase transition at 573°C]]
- [[microcrack density and rock strength correlation]]
- [[non-destructive evaluation using ultrasonic velocity]]
- [[empirical relationship between tensile strength and fracture toughness]]

## Candidate Methods
- [[Brazilian splitting test for tensile strength (ISRM)]]
- [[semi-circular bend (SCB) test for mode-I fracture toughness]]
- [[ultrasonic pulse velocity measurement (NM-4B)]]
- [[petrographic thin section analysis for thermal microcracks]]
- [[slow heating and natural cooling protocol (2°C/min)]]
- [[mass loss rate measurement for thermal damage]]
- [[regression analysis of vp vs. mechanical properties]]
- [[damage factor definition based on P-wave velocity]]
- [[normalization of P-wave velocity for inter-granite comparison]]

## Connections To Other Work
- 与多项花岗岩高温P波速度测试结果进行归一化比较（Fan et al. 2017; Griffiths et al. 2017; Yang et al. 2017; Zhu et al. 2017; Jin et al. 2019; Qin et al. 2020; Miao et al. 2021），vp随温度降低的规律具有普适性。[Hu 2022, pp. 5-6, Table 4, Fig. 5]  
- σt-KIC经验关系与Haberfield & Johnston (1989) σt/KIC=13.14、Zhang (2002) =6.88、Vavro & Soucek (2013) =4.02、Wang et al. (2007) =2.82进行比较，本实验结果落在中间并接近Vavro & Soucek曲线。[Hu 2022, pp. 9-10, Fig. 8]  
- 脆性指数B_i = (σc·σt)/2（Kahraman & Altindag 2004; Sha et al. 2020）与本文提出的a指数相互印证，a增大对应脆性减弱、延性增强。[Hu 2022, pp. 10-12]  
- 其他岩石的a值与脆–延转变温度的关系：CF大理岩（Guo et al. 2020）在400 °C后显延性；Stripa花岗岩（Alm et al. 1985）300 °C微裂纹显现；BS花岗岩（Zuo et al. 2017）脆–延转变阈值250 °C；本花岗岩400 °C后脆性明显下降（Yang et al. 2021a）。[Hu 2022, pp. 10-12]  
- 花岗岩损伤阶段划分（Zhang et al. 2018）与本研究的Dv2和温度分区建议一致。[Hu 2022, pp. 13]

## Open Questions
1. 使用不同KIC测试方法（如短棒，CCNBD）得到的σt/KIC比值是否具有相同的温度依赖性？[Hu 2022, p. 14]  
2. 巴西劈裂试验端部接触约束效应对脆性指数a的影响有多大？若改用直接拉伸等其它σt测试方法，a–温度关系是否一致？[Hu 2022, p. 12]  
3. 更高温度（>600 °C）下花岗岩的a值变化以及结构水逸出对断裂韧性的定量影响尚不清楚。[Hu 2022, p. 5]  
4. 如何将基于vp的双区损伤因子（Dv1和Dv2）应用于实际工程中的原位岩石稳定性评估，尤其针对含天然裂隙的高温岩体？[Hu 2022, p. 14]  
5. 不同加热–冷却路径（如热冲击）下，vp、σt、KIC之间的关系以及a指数的适用性如何？[未在本文研究，但方法部分提及热冲击被排除]  
6. 岩石矿物组成和胶结类型如何主导a的突变温度？如何建立矿物学参数与脆–延转变的预测关系？[Hu 2022, p. 11]

## Source Coverage
本页面严格基于所有提供的12个非空索引片段编写，共涵盖58,729字符，源文本块覆盖率达100%，字符覆盖率为100.26%（由于少量断字修复导致字符数略增）。未使用任何外部信息。来源唯一为 Hu et al. (2022)。
