---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-jiang-experimental-investigation-on-damage-and-seepage-of-red-sandstone-subjected-to-cyclic"
title: "Experimental Investigation on Damage and Seepage of Red Sandstone Subjected to Cyclic Thermal and Cold Treatment."
status: "draft"
source_pdf: "data/papers/2023 - Experimental investigation on damage and seepage of red sandstone subjected to cyclic thermal and cold treatment.pdf"
collections:
  - "zotero new"
citation: "Jiang, Haopeng, et al. \"Experimental Investigation on Damage and Seepage of Red Sandstone Subjected to Cyclic Thermal and Cold Treatment.\" *Geoenergy Science and Engineering*, vol. 222, 2023, 211461."
indexed_texts: "11"
indexed_chars: "52029"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "48690"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.935824"
coverage_status: "full-index"
source_signature: "83b31a35fd67366c3e5251a13f497b6eeb630ba8"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:29:39"
---

# Experimental Investigation on Damage and Seepage of Red Sandstone Subjected to Cyclic Thermal and Cold Treatment.

## One-line Summary
对经历热‑冷循环冲击后的红砂岩进行三轴渗流试验，分析渐进破坏过程中渗透率变化规律，并基于统计损伤理论建立考虑损伤的渗透率模型。 [Jiang 2023, pp. 1-2]

## Research Question
热‑冷循环冲击作用后，红砂岩在应力‑渗流耦合条件下的渗透与损伤特性尚不明确，尤其是循环次数和温度对渐进破裂过程中渗流演化的影响。该研究旨在揭示热‑冷循环对红砂岩力学与渗流行为的劣化机制。 [Jiang 2023, pp. 1-2, 2-2]

## Study Area / Data
- **岩石样品**：红砂岩取自中国吉林省某深部矿山，整体呈红褐色，致密。矿物组成：石英 45%、长石 32%、蒙脱石等黏土矿物 23%，平均密度 2.31 g/cm³。加工成 Φ 50 mm × 100 mm 标准圆柱试样，经真空饱水与声波检测剔除离散性较大的试样。 [Jiang 2023, pp. 2-2]
- **试验条件**：温度水平：20 °C（对照组）、200 °C、400 °C、800 °C、1000 °C；低温恒为 −30 °C。循环次数：10 次与 20 次，每种循环作用 3 个试样。 [Jiang 2023, pp. 2-5]
- **数据来源**：三轴压缩全程应力‑应变‑渗流曲线、特征应力（闭合应力 σ_cc、起裂应力 σ_ci、损伤应力 σ_cd、峰值应力 σ_c、残余应力 σ_cr）、弹性模量、初始渗透率与最大渗透率等，详见原文 Table 1 与 Fig. 3–5。 [Jiang 2023, pp. 5-6, 6-7]

## Methods
- **热‑冷循环处理**：样品在 DHG 智能干燥箱中以 5 °C/min 速率加热至目标温度（200 °C、400 °C、800 °C、1000 °C），恒温 4 h 后立即移入 −30 °C 的冻融箱中冷却 8 h，此为一循环。 [Jiang 2023, pp. 2-5]
- **渗流试验**：采用稳态法，在围压 20 MPa 恒定、孔隙水压 5 MPa 条件下，以 0.01 mm/min 的轴向位移速率进行加载，按达西定律计算渗透率（式 1）。 [Jiang 2023, pp. 2-5, 5-6]
- **损伤本构与渗透率模型**：
  1. 定义热‑冷循环引起的初始损伤 *D(T,n)* = 1 − E(T,n)/E(20°C,0) （式 2）。
  2. 荷载引起的统计损伤 *D_M* 用 Weibull 分布描述（式 3）。
  3. 耦合损伤 *D_tol* = *D_M* + *D(T,n)* − *D_M*·*D(T,n)* （式 4），并推导出损伤本构关系（式 7）。
  4. 基于指数型渗透率模型，引入耦合损伤修正裂缝压缩系数，得到考虑损伤的渗透率模型（式 11）。 [Jiang 2023, pp. 7-9]
- **模型验证**：利用试验数据拟合参数 *m* 与 *K*，计算耦合损伤 *D_tol*，代入渗透率模型得到理论曲线，与试验曲线对比。 [Jiang 2023, pp. 9-10]

## Key Findings
1. **力学特性劣化**：红砂岩的峰值应力和弹性模量均随温度升高及循环次数增加而降低。例如，10 次循环后，1000 °C 下的峰值强度较 200 °C 降低 68.15%，弹性模量降低 37.72%；20 次循环下降幅更大。热损伤是强度与模量衰减的主要原因，冷热循环进一步削弱矿物颗粒间胶结强度。 [Jiang 2023, pp. 6-7]
2. **渗流演化规律**：初始渗透率与最大渗透率均随温度和循环次数增加而增大。10 次循环后，1000 °C 的初始渗透率较 200 °C 增加 208.41%，最大渗透率增加 78.66%；20 次循环下增幅依然显著。温度与循环次数促进内部微裂缝萌生、扩展，导致渗透通道形成。 [Jiang 2023, pp. 6-7]
3. **破坏模式**：低温度、低循环次数时，试样呈单条主控裂缝型破裂；随温度和循环次数增加，出现沿剪切带的树枝状破坏与破碎，表明冷热循环加重了损伤。 [Jiang 2023, pp. 7-7]
4. **特征应力比例**：经历热‑冷循环后，裂缝闭合应力 σ_cc 为峰值应力的 15%–24%，起裂应力 σ_ci 约为 40%，损伤应力 σ_cd 为 69%–75%，残余应力 σ_cr 为 40%–80%。 [Jiang 2023, pp. 5-6]
5. **损伤‑渗透耦合模型**：所建渗透率模型的理论曲线与试验曲线吻合较好，能有效表征渗透率与耦合损伤的关系。渗透率随耦合损伤指数增加，耦合损伤‑应变关系呈“S”型单调递增。 [Jiang 2023, pp. 9-10, 10-11]
6. **参数敏感性**：模型参数 *m* 主要影响峰后曲线形态，*m* 增大脆性破坏越明显；*K* 主要反映峰值应变与强度，*K* 增大峰值应变和强度均提高。 [Jiang 2023, pp. 10-10]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 峰值应力 σ_c 随温度和循环次数下降；1000 °C、10 次循环较 200 °C 降低 68.15%；1000 °C、20 次循环降低 76.56% | [Jiang 2023, pp. 6-7] | 围压 20 MPa，孔压 5 MPa，温度 200–1000 °C，循环 10、20 次 | Table 1 和 Fig. 4 |
| 弹性模量 E 随温度和循环次数下降；1000 °C、10 次循环较 200 °C 降低 37.72%；1000 °C、20 次循环降低 31.62% | [Jiang 2023, pp. 6-7] | 同上 | Table 1 和 Fig. 4 |
| 初始渗透率随温度升高而增大；10 次循环下 1000 °C 较 200 °C 增加 208.41%，20 次循环增加 127.76% | [Jiang 2023, pp. 6-7] | 同上；初始渗透率对应未加载阶段 | Table 1 和 Fig. 5 |
| 最大渗透率随温度升高而增大；10 次循环下 1000 °C 较 200 °C 增加 78.66%，20 次循环增加 70.26% | [Jiang 2023, pp. 6-7] | 同上；最大渗透率对应峰后破坏阶段 | Table 1 和 Fig. 5 |
| 裂缝闭合应力 σ_cc 为峰值应力的 15–24%，起裂应力 σ_ci 约 40%，损伤应力 σ_cd 为 69–75%，残余应力 σ_cr 为 40–80% | [Jiang 2023, pp. 5-6] | 所有热‑冷循环条件 | Table 1 |
| 低温度、低循环次数时呈单条主控裂缝破坏；高温度、高循环次数时呈树枝状破坏并伴随剪切带破碎 | [Jiang 2023, pp. 7-7] | 200 °C、10 次循环对比更高温度/次数 | Fig. 3 |
| 考虑损伤的渗透率模型理论曲线与试验曲线差异不大，能有效表征渗透率‑损伤关系 | [Jiang 2023, pp. 9-10] | 所有测试条件，拟合参数见表 2 | Fig. 6 |
| 耦合损伤 D_tol 随应变呈“S”型单调递增，温度越高初始损伤越大，加载后损伤加速增长直至接近 1 | [Jiang 2023, pp. 10-11] | 各温度与循环次数，应变 0~破坏 | Fig. 8 |
| 渗透率与耦合损伤 D_tol 均随温度呈三次函数形式增长，至 1000 °C 达最大值 | [Jiang 2023, pp. 10-11] | 10 次循环，应变 0.005 和 0.015 | Fig. 9 |

## Limitations
- 每组试验仅使用 3 个试样，样本量较小，结果可能受岩石天然离散性影响（尽管已通过饱水与声波筛选）。 [Jiang 2023, pp. 2-2, 2-5]
- 模型参数 *m* 和 *K* 通过拟合应力‑应变数据获得，缺乏直接物理测量，其外推能力未知。 [Jiang 2023, pp. 9-10]
- 试验仅针对单一岩性（红砂岩）和特定温度/循环次数组合，对其他岩石类型或更宽工况的适用性未经验证。 [Jiang 2023, pp. 10-11]
- 渗透率模型基于经验指数形式和损伤耦合假设，其理论基础（如裂缝压缩系数修正）需更多微观证据支持。 [Jiang 2023, pp. 9-10]

## Assumptions / Conditions
- **材料假设**：红砂岩视为均质连续介质，渗透率计算遵循达西定律。 [Jiang 2023, pp. 5-6]
- **加载条件**：围压 20 MPa 恒定，孔隙水压 5 MPa，轴向位移速率 0.01 mm/min。 [Jiang 2023, pp. 5-6]
- **热‑冷循环制度**：加热速率 5 °C/min，目标温度恒温 4 h，低温 −30 °C 恒温 8 h；干燥处理 20 °C、48 h。 [Jiang 2023, pp. 2-5]
- **损伤模型假定**：荷载损伤服从 Weibull 分布；总损伤采用耦合项组合；有效应力采用 Terzaghi 形式的定义。 [Jiang 2023, pp. 7-9]
- **流体性质**：动力黏度 μ 取 1 × 10⁻³ Pa·s（水温 20 °C）。 [Jiang 2023, pp. 5-6]

## Key Variables / Parameters
- **独立变量**：温度 *T*（20 °C、200 °C、400 °C、800 °C、1000 °C）、热‑冷循环次数 *n*（10、20）。 [Jiang 2023, pp. 2-5]
- **力学响应**：弹性模量 *E(T,n)*、峰值应力 *σ_c*、闭合应力 *σ_cc*、起裂应力 *σ_ci*、损伤应力 *σ_cd*、残余应力 *σ_cr*。 [Jiang 2023, pp. 5-6, 6-7]
- **渗流响应**：初始渗透率 *k_0*、最大渗透率、全程渗透率 *k*。 [Jiang 2023, pp. 5-6, 6-7]
- **损伤变量**：热‑冷初始损伤 *D(T,n)*（式 2）、荷载统计损伤 *D_M*（式 3）、耦合总损伤 *D_tol*（式 4）。 [Jiang 2023, pp. 7-9]
- **模型参数**：Weibull 形状参数 *m* 与尺度参数 *K*；裂缝压缩系数修正因子 *γ*；初始渗透率 *k_0*；峰值有效应力 *σ_e0*。 [Jiang 2023, pp. 7-9, 9-10]
- **试验控制参数**：围压 *σ_3* = 20 MPa，孔隙水压 *p_w* = 5 MPa，有效应力计算采用式 9。 [Jiang 2023, pp. 5-6, 9-10]

## Reusable Claims
- **热‑冷循环对力学性质的劣化**：在 200–1000 °C、循环 10–20 次、围压 20 MPa 条件下，红砂岩峰值应力和弹性模量随温度和循环次数单调下降。热‑冷冲击损伤（热裂化与矿物胶结弱化）是主要原因。 [Jiang 2023, pp. 6-7]
- **渗透率与温度/循环次数的关系**：相同试验条件下，初始渗透率和最大渗透率均随温度和循环次数增加而显著上升。1000 °C、10 次循环的初始渗透率较 200 °C 提高逾 200%。温度与冷热循环加剧了内部微裂纹萌生、扩展，形成更多渗流通道。 [Jiang 2023, pp. 6-7]
- **特征应力阈值范围**：经历热‑冷循环的红砂岩，其闭合应力约为峰值应力的 15%–24%，起裂应力约为 40%，损伤应力约为 69%–75%，残余应力约为 40%–80%。这些比例可作为类似条件下岩石损伤分级的参考。 [Jiang 2023, pp. 5-6]
- **破坏模式转化**：低温和低循环次数时岩石呈单一主控裂缝破坏，高温高循环次数时转向多裂缝树枝状破坏，表明冷热循环改变了内部损伤分布格局。 [Jiang 2023, pp. 7-7]
- **考虑损伤的渗透率模型有效性**：基于统计损伤理论建立的本构模型（式 7）和指数渗透率模型（式 11）能很好地重现红砂岩在热‑冷循环后的应力‑应变‑渗流全过程。耦合损伤 *D_tol* 随应变呈“S”型增长，渗透率随 *D_tol* 指数上升。该模型可用于井筒围岩损伤评估。 [Jiang 2023, pp. 9-10, 10-11]
- **模型参数灵敏度**：Weibull 参数 *m* 决定峰后曲线的陡峭程度（脆性特征），*K* 影响峰值应变和强度水平。这为模型标定提供指导。 [Jiang 2023, pp. 10-10]

## Candidate Concepts
- [[enhanced geothermal system / EGS]]
- [[thermal-cold shock cycle]]
- [[damage constitutive model]] / [[statistical damage theory]]
- [[permeability model with damage coupling]]
- [[hydro-mechanical coupling]]
- [[red sandstone]]
- [[geothermal mining in cold regions]]
- [[Weibull distribution for rock damage]]
- [[effective stress]]
- [[steady-state permeability measurement]]
- [[progressive fracture / progressive fracturing]]

## Candidate Methods
- [[steady-state method for permeability test]]
- [[triaxial compression with coupled hydro-mechanical loading]]
- [[damage variable defined by elastic modulus decay]]
- [[Weibull-based statistical damage modeling]]
- [[exponential permeability model with fracture compressibility correction]]
- [[volumetric strain method for characteristic stress determination]]
- [[controlled thermal-cold cycling treatment (heating furnace + freeze-thaw box)]]

## Connections To Other Work
- **脆性砂岩渗透与损伤**：Jiang et al. (2010) 发现渗透率与各向异性损伤密切相关，本研究进一步将损伤耦合引入热‑冷循环后的渗流模型中。 [Jiang 2023, pp. 1-2]
- **围压对渗透率的影响**：T.C. Li et al. (2021) 指出围压对力学性质和渗透特性影响最大，本试验在恒定 20 MPa 围压下完成，突出了热‑冷损伤的贡献。 [Jiang 2023, pp. 1-2]
- **热‑水‑力耦合参数标定**：Yang et al. (2021) 对加热水冷处理后花岗岩进行了 THM 耦合参数标定，本研究建立的渗透率模型可视为 THM 分析中渗流与损伤模块的简化形式。 [Jiang 2023, pp. 1-2]
- **热循环后岩石渗透率**：Gautam et al. (2020) 研究了 250 °C 循环后花岗岩的渗透率、模量和强度变化；Liu et al. (2020) 进行了热‑水‑力耦合下砂岩渗透试验，并用损伤变量关联温度与渗透率，本研究在更宽温度范围和冷‑热共同作用下提供了新数据。 [Jiang 2023, pp. 2-2]
- **高温后岩石力学性质**：Zhang et al. (2021) 发现加热水冷处理后花岗岩的力学性质转折阈值约为 500 °C；本研究红砂岩在 200–1000 °C 范围内同样观察到剧烈劣化。 [Jiang 2023, pp. 2-2]
- **核废料处置热循环研究**：Gautam et al. (2020) 的 Jalore 花岗岩热循环实验为相关岩石热‑力响应提供了类比。 [Jiang 2023, pp. 11-12]

## Open Questions
- 当前模型仅在红砂岩上验证，对其他储层岩石（如花岗岩、碳酸盐岩）的适用性有待检验。 [Jiang 2023, pp. 10-11]
- 热‑冷循环次数研究仅止于 20 次，更高循环次数下损伤与渗透率的演化是否趋于稳定或加速尚不明确。 [Jiang 2023, pp. 2-5]
- 微观机制（如矿物相变、热裂纹成核与贯通）与宏观渗透率‑损伤关系的多尺度关联仍需深入。 [Jiang 2023, pp. 2-2, 10-11]
- 在实际 EGS 工程中，热‑冷冲击条件更为复杂（流体性质、应力状态波动），如何将实验室模型扩展到现场尺度仍是一个挑战。 [Jiang 2023, pp. 1-2]

## Source Coverage
所有非空索引片段均已处理并编译进本页面。源码片段共 11 个，字符总数 52,029，编译后源码块 11 个，编译后字符数 48,690。按块覆盖率为 1.0，按字符覆盖率约 0.936。源签名为 83b31a35fd67366c3e5251a13f497b6eeb630ba8，覆盖状态为 full-index。
