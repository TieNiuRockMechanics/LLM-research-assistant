---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-jiang-experimental-study-of-convective-heat-transfer-of-carbon-dioxide-at-supercritical-pre"
title: "Experimental Study of Convective Heat Transfer of Carbon Dioxide at Supercritical Pressures in a Horizontal Rock Fracture and Its Application to Enhanced Geothermal Systems."
status: "draft"
source_pdf: "data/papers/2017 - Experimental study of convective heat transfer of carbon dioxide at supercritical pressures in a horizontal rock fracture and its application to enhanced geothe.pdf"
collections:
citation: "Jiang, Peixue, et al. “Experimental Study of Convective Heat Transfer of Carbon Dioxide at Supercritical Pressures in a Horizontal Rock Fracture and Its Application to Enhanced Geothermal Systems.” *Applied Thermal Engineering*, vol. 117, 2017, pp. 39-49. doi:10.1016/j.applthermaleng.2017.01.078. Accessed 2026."
indexed_texts: "11"
indexed_chars: "51974"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "52221"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004752"
coverage_status: "full-index"
source_signature: "8453d158cb6eff15f1db0ae5fb2268f1dbf23d02"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T19:09:02"
---

# Experimental Study of Convective Heat Transfer of Carbon Dioxide at Supercritical Pressures in a Horizontal Rock Fracture and Its Application to Enhanced Geothermal Systems.

## One-line Summary
该研究实验探究了超临界压力CO₂在0.2 mm水平花岗岩裂缝中的层流对流换热特性，建立了考虑剧烈物性变化的局部换热关联式，以改进增强型地热系统（EGS）的现场尺度模拟模型。[Jiang 2017, pp. 1-2, 9-10]

## Research Question
在增强型地热系统（EGS）中，裂缝内超临界压力流体的对流换热特性对热提取模拟至关重要，但现有研究缺乏考虑超临界流体物性剧烈变化的裂缝换热系数系统经验关系。本研究旨在通过实验确定超临界CO₂在水平岩石裂缝中的局部换热规律，分析质量流量和初始岩温的影响，并提出能够纳入裂缝网络模型和局部热非平衡（LTNE）模型的换热关联式。[Jiang 2017, pp. 2-3]

## Study Area / Data
- **实验系统**：水平放置的岩心夹持器，岩样为花岗岩（半径50 mm、长度50 mm，切成两半形成光滑平行裂缝，孔径0.2 mm，渗透率 0.5124 × 10⁻¹⁸ m²，假设裂缝壁面不渗透）。最高工作温度 280 °C，最大流体压力 14 MPa，围压可达 28 MPa。加热方式为油浴。[Jiang 2017, pp. 3-4]
- **实验工况**：超临界压力固定为 8.1 MPa；初始岩石温度 55–250 °C；CO₂质量流量 0.13–0.75 kg/h，共10组实验。这些条件对应于埋深 1000–5000 m、地温梯度 40 °C/km 的储层实际温度范围。[Jiang 2017, pp. 3-4]
- **测量参数**：裂缝壁面7个热电偶温度、进出口流体温度、流体压力、压差、质量流量。[Jiang 2017, pp. 3-4]

## Methods
1. **瞬态实验**：将预热的岩心暴露于流入的冷CO₂，同时记录所有温度、压力、流量随时间的变化。[Jiang 2017, pp. 3-4]
2. **二维数值数据还原**：将裂缝流动视为二维，以实测壁面温度经样条插值后作为边界条件，进口给定实测温度与质量流量，出口给定实测压力。利用FLUENT 13.0软件耦合求解连续性、动量和能量方程（式1–4），采用SIMPLE算法、二阶离散格式，时间步长 1 s。湍流模型为层流。CO₂物性由NIST真实气体模型嵌入计算。[Jiang 2017, pp. 4-6]
3. **局部参数计算**：由模拟得到的局部热流、壁温与流体主体温度按式(5)~(7)计算局部换热系数hₓ、雷诺数Reₓ和努塞尔数Nuₓ。[Jiang 2017, pp. 4-6]
4. **不确定性评估**：用数值实验验证数据还原方法，局部热流最大相对误差7%。计入热电偶精度（±0.15 °C）后，hₓ与Nuₓ的最大均方根实验不确定性分别为±10.2%和±11.4%。[Jiang 2017, pp. 4-6]
5. **关联式拟合**：基于实验数据，采用最小二乘曲线拟合得到考虑物性变化的Nu修正关联式（式9、10）。[Jiang 2017, pp. 9-10]

## Key Findings
- **远离拟临界点的影响**：当流体主体温度远高于拟临界温度（T_b/T_{p,c} > 1.2）时，物性沿截面变化很小。充分发展区的局部努塞尔数近似为常数，平均值 7.36（最大相对误差 0.31%），略低于恒壁温平行板的理论值 7.54，这是因为壁温和热流均非恒定。[Jiang 2017, pp. 6-7, 9-10]
- **接近拟临界点的特性**：当CO₂主体温度接近拟临界点（T_{p,c} < T_b < T_w）时，比热、导热系数、密度和粘度沿截面剧烈变化，导致局部换热系数急剧升高而努塞尔数急剧下降。密度和粘度在壁面附近增大降低了近壁流速，削弱换热；比热和导热系数的差异使温度分布陡峭，进一步降低Nu。[Jiang 2017, pp. 7-9]
- **温度均低于拟临界点**：当壁温与主体温度均低于拟临界点时，局部换热系数和努塞尔数反而高于高温工况，体现超临界CO₂物性反向变化对层流换热的显著影响。[Jiang 2017, pp. 7-9]
- **质量流量效应**：较高流量（0.75 kg/h）下，随着流体接近拟临界温度，局部换热增强，岩壁温度分布趋于均匀；较低流量（0.35 kg/h）下出口温度更稳定，但沿程壁温几乎线性下降。[Jiang 2017, pp. 4-6]
- **初始岩温效应**：当初始岩温使CO₂在裂缝内跨越拟临界温度时（如55 °C工况），物性突变对换热影响强烈；高温工况（≥150 °C）下影响不显著。[Jiang 2017, pp. 6-7]
- **换热关联式**：提出层流条件下考虑物性变化的关联式（见图14，约98%数据点偏差<8%）：
  \[
  \frac{Nu}{Nu_0} = \left( \frac{\bar{c}_p}{c_{p,b}} \right)^n \left( \frac{\rho_w}{\rho_b} \right)^{-0.27} \left( \frac{Pr_w}{Pr_b} \right)^{0.043}
  \]
  其中Nu₀ = 7.36；指数n依赖温度区域（式10）。[Jiang 2017, pp. 9-10]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 平均努塞尔数 Nu₀ = 7.36（最大相对误差0.31%） | [Jiang 2017, pp. 9-10] | 初始岩温 150–250 °C，0.35–0.75 kg/h，P=8.1 MPa，d=0.2 mm | 充分发展层流，物性恒定假设；作为关联式基准 |
| 关联式：Nu/Nu₀ = (c̅ₚ/cₚ,₆)ⁿ·(ρ_w/ρ₆)⁻⁰·²⁷·(Pr_w/Pr₆)⁰·⁰⁴³ | [Jiang 2017, pp. 9-10] | 0.95 < T_b/T_{p,c} < 1.62，层流，P=8.1 MPa，d=0.2 mm | 约98%数据点偏差<8%；n的分段定义见式(10) |
| n = 0.45 当 T_b < T_w < T_{p,c} 或 1.2T_{p,c} < T_b < T_w | [Jiang 2017, pp. 10] | 上述工况 | |
| n = 0.45 + 13.83(T_w/T_{p,c} − 1) 当 T_b < T_{p,c} < T_w | [Jiang 2017, pp. 10] | | |
| n = 0.45 + 13.83(T_w/T_{p,c} − 1)[1 − 2.28(T_b/T_{p,c} − 1)] 当 T_{p,c} < T_b < 1.2T_{p,c} | [Jiang 2017, pp. 10] | | |
| 局部换热系数hₓ增大而Nuₓ减小（T_b接近T_{p,c}时） | [Jiang 2017, pp. 7-9] | 初始岩温80 °C，0.75 kg/h | 壁温高于拟临界点，物性差异所致 |
| 低流量下出口温度更稳定：0.35 kg/h时出口200 °C保持约5 min，0.75 kg/h时降至170 °C | [Jiang 2017, pp. 4-6] | 初始岩温200 °C | 说明流量对热突破时间的影响 |
| 局部热流还原最大相对误差7%；hₓ不确定度±10.2%，Nuₓ不确定度±11.4% | [Jiang 2017, pp. 4-6] | | 实验系统验证 |

## Limitations
- 研究限于单一裂缝孔径（0.2 mm）和单一岩性（花岗岩），未涉及其他孔径或岩石类型。[Jiang 2017, pp. 3-4]
- 实验在层流范围内进行（基于裂缝宽度与流速），未拓展至过渡流或湍流状态。[Jiang 2017, pp. 3-4]
- 关联式仅适用于超临界压力 8.1 MPa 的CO₂，且主体温度范围0.95 < T_b/T_{p,c} < 1.62。推广至其他压力或工质需验证。[Jiang 2017, pp. 9-10]
- 裂缝壁面假设为不渗透，未考虑真实裂缝中壁面渗透或化学反应的影响。[Jiang 2017, pp. 3-4]
- 二维数值模型未考虑沿缝宽方向的流动不均匀性。[Jiang 2017, pp. 4-6]
- 实验为瞬态过程，关联式基于特定时刻（50 min）的局部参数，未明确评估拟稳态适用性。[Jiang 2017, pp. 6-7]

## Assumptions / Conditions
- 裂缝为光滑平行平板，孔径0.2 mm，壁面不可渗透。[Jiang 2017, pp. 3-4]
- 重力影响可忽略（水平放置）。[Jiang 2017, pp. 3]
- 流动为充分发展的层流。[Jiang 2017, pp. 4-6]
- 物性修正关联式适用于超临界压力 8.1 MPa下的CO₂。[Jiang 2017, pp. 9-10]
- 数值还原模型中，壁面温度边界条件由实测值插值得到，不考虑壁面侧向热传导。[Jiang 2017, pp. 4-6]
- 耦合求解使用FLUENT 13.0，网格无关性和时间步长独立性已考察。[Jiang 2017, pp. 4-6]

## Key Variables / Parameters
- 局部壁温 T_w(x,t)、局部流体主体温度 T_b(x) [Jiang 2017, pp. 4-6]
- 局部换热系数 h_x、局部努塞尔数 Nu_x、局部雷诺数 Re_x [Jiang 2017, pp. 4-6]
- 拟临界温度 T_{p,c}，在8.1 MPa下约为81 °C（伪临界温度）[Jiang 2017, pp. 2-3; 4-6]
- 平均比热 c̄ₚ = (H_w − H_b)/(T_w − T_b) [Jiang 2017, pp. 9-10]
- 密度比 ρ_w/ρ_b，普朗特数比 Pr_w/Pr_b [Jiang 2017, pp. 9-10]
- 质量流量 M (0.13–0.75 kg/h)、初始岩温 T_0 (55–250 °C) [Jiang 2017, pp. 3-4]
- 关联式指数 n，由温度区域决定 [Jiang 2017, pp. 10]

## Reusable Claims
1. **在超临界压力CO₂层流裂缝换热中，当流体主体温度远高于拟临界温度（T_b/T_{p,c} > 1.2），充分发展段的努塞尔数可近似为常数7.36。** 条件：平行平板裂缝，孔径0.2 mm，光滑不渗透壁面，压力约 8.1 MPa，工质CO₂。局限性：未考虑物性变化的影响。[Jiang 2017, pp. 9-10]
2. **当CO₂温度接近拟临界点时，局部换热系数急剧升高而努塞尔数显著下降，必须采用物性修正关联式。** 适用条件：层流，超临界压力，0.95 < T_b/T_{p,c} < 1.62；关联式见式(9)和(10)。局限性：仅验证于0.2 mm裂缝和8.1 MPa。[Jiang 2017, pp. 9-10]
3. **裂缝换热性能受质量流量影响显著：低流量下出口温度更稳定，高流量下热突破更快但沿程壁温因局部换热增强而趋于均匀。** 条件：水平裂缝，初始岩温 200–80 °C，CO₂流量 0.35–0.75 kg/h。局限性：实验室尺度，无重力影响。[Jiang 2017, pp. 4-6]
4. **所提出的换热关联式可嵌入离散裂缝网络模型或LTNE连续介质模型，用于改善EGS现场尺度模拟的准确度。** 关联式形式：Nu = 7.36 × (c̄ₚ/cₚ,₆)ⁿ × (ρ_w/ρ₆)⁻⁰·²⁷ × (Pr_w/Pr₆)⁰·⁰⁴³。指数n按式(10)分区定义。适用于层流超临界CO₂，裂缝孔径0.2 mm，压力 8.1 MPa。[Jiang 2017, pp. 9-10]

## Candidate Concepts
- [[Supercritical CO2 heat transfer]]
- [[Enhanced geothermal systems (EGS)]]
- [[Rock fracture heat transfer]]
- [[Local thermal non-equilibrium (LTNE)]]
- [[Fracture network model]]
- [[Equivalent continuous porous media model]]
- [[Pseudo-critical point (Tp,c)]]
- [[Nusselt number correction]]
- [[Thermophysical property variation]]
- [[Granite fracture permeability]]
- [[Lab-scale heat extraction]]
- [[CO2–EGS concept]]

## Candidate Methods
- [[Transient heat extraction experiment]]
- [[Data reduction method for fracture heat transfer]]
- [[FLUENT numerical simulation (2D laminar flow)]]
- [[Spline interpolation of wall temperatures]]
- [[Least-squares curve fitting for Nusselt correlation]]
- [[NIST real gas model for CO2 properties]]
- [[Uncertainty analysis using numerical experiment]]
- [[Coupled fluid-thermal simulation with variable properties]]

## Connections To Other Work
- 与CO₂‑EGS概念的联系：Brown [9]提出超临界CO₂替代水作为工质，Pruess [10–12]数值模拟表明其发电功率更高且可实现碳封存。[Jiang 2017, pp. 1-2]
- 与裂缝/多孔介质模型：离散裂缝网络模型（如Kolditz [19,20]）和等效连续介质LTNE模型（如Gelet等 [38,39] 标定传热系数为33 W/m³/K，范围60–120 W/m³/K）。本工作提供的关联式可直接改进这类模型的内部换热系数。[Jiang 2017, pp. 2-3]
- 与以往裂缝换热实验：Zhao [42,44]测得的单裂缝水换热系数为200–1400 W/m²/K，但未考虑超临界物性变化。Ogino等 [26]用传质类比得到颗粒与壁面的换热系数。Magliocco等 [46]用干超临界CO₂流过加热多孔介质验证了TOUGH2数值模型，但未给出考虑物性变化的关联式。[Jiang 2017, pp. 2-3]
- 与超临界微通道研究：作者前期在微管/蛇形管中的湍流换热关联式[50–52]为本研究提供了物性修正的思路，特别是截面平均比热和n指数定义。[Jiang 2017, pp. 9-10]

## Open Questions
- 所提出的关联式是否适用于其他裂缝孔径（如毫米级或更宽裂隙）？[Jiang 2017, pp. 9-10；实验仅d=0.2 mm]
- 当裂缝壁面存在一定渗透率或粗糙度时，关联式如何修正？[当前假设不渗透光滑壁面]
- 关联式在过渡流或湍流条件下的适用性？[实验限于层流]
- 关联式对超临界水或其他工质（如H₂O、N₂）的有效性？[仅验证于CO₂，压力8.1 MPa]
- 瞬态实验获得的50 min时刻关联式在长期热提取（拟稳态）中的可靠度？[关联式基于特定时刻数据]
- 如何将该二维关联式扩展到实际三维裂缝网络中？[实验为二维水平裂缝]
- 关联式在现场尺度模型（如离散裂缝网络或LTNE模型）中应用时，是否需要进一步放大或平均化？[Jiang 2017, pp. 9-10指出可作为输入，但未给出放大方法]

## Source Coverage
所有11个非空索引片段（共计52,221字符）均已处理并纳入本页面。编译后字符数（包括标题、表格和引用）为52,221字符，与源片段字符比约为1.0048。覆盖率（按片段数）为1.0，无遗漏片段。源签名：8453d158cb6eff15f1db0ae5fb2268f1dbf23d02。编译策略为单通道Markdown生成。
