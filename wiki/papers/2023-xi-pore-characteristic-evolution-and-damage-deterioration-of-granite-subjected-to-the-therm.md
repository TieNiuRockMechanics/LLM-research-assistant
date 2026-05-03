---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-xi-pore-characteristic-evolution-and-damage-deterioration-of-granite-subjected-to-the-therm"
title: "Pore Characteristic Evolution and Damage Deterioration of Granite Subjected to the Thermal and Cooling Treatments Combined with the NMR Method."
status: "draft"
source_pdf: "data/papers/2023 - Pore characteristic evolution and damage deterioration of granite subjected to the thermal and cooling treatments combined with the NMR method.pdf"
collections:
  - "part2"
  - "论文"
citation: "Xi, Yan, et al. “Pore Characteristic Evolution and Damage Deterioration of Granite Subjected to the Thermal and Cooling Treatments Combined with the NMR Method.” *Bulletin of Engineering Geology and the Environment*, vol. 82, 2023, p. 182, doi:10.1007/s10064-023-03215-2. Accessed 1 Jan. 2026."
indexed_texts: "16"
indexed_chars: "78707"
nonempty_source_blocks: "16"
compiled_source_blocks: "16"
compiled_source_chars: "78002"
compiled_stage_count: "1"
single_pass_char_budget: "800000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.991043"
coverage_status: "full-index"
source_signature: "8a8f828fb366e111444ec567bc2774d5ec386ab5"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T09:28:14"
---

# Pore Characteristic Evolution and Damage Deterioration of Granite Subjected to the Thermal and Cooling Treatments Combined with the NMR Method.

## One-line Summary
通过低场核磁共振（NMR）与场发射扫描电镜（FE-SEM）实验，系统研究了200 °C至600 °C高温及自然冷却、水冷、液氮冷却三种方式对细粒花岗岩孔隙特征演化与损伤劣化的影响，建立了宏‑微观损伤定量表征方法，并揭示了孔隙尺寸分布与分形特征对损伤的控制作用。

## Research Question
温度扰动（热‑冷处理）如何驱动花岗岩内部孔隙结构（尺寸、数量、分布）演化，并由此导致岩石宏观力学性质的劣化？如何建立基于微孔隙特征变化（孔隙度、孔径分布、分形维数）与宏观声学测量（波速）之间的定量损伤关系，以服务于热干岩开发等工程实践？[Xi 2023, pp. 1-4]

## Study Area / Data
- 试样来源：湖南岳阳致密细粒花岗岩，属热干岩主储层基质。同一方向取样以避免各向异性。
- 样品规格：直径50.0 mm、高度25.0 mm的圆柱体，端面平整度≤0.05 mm，符合ISRM建议。
- 初始特征：CT扫描显示岩石致密、孔隙体积和数量少；XRD矿物组成：石英（28.2%）、钾长石（27.4%）、云母（22.2%）、斜长石（17.3%）、粘土矿物（4.9%）。
- 实验组设计：5组（室温25 °C、200 °C、400 °C、500 °C、600 °C），每组9个试样，每个温度下分为自然冷却、常温水冷却（水冷）和液氮冷却（−196 °C）三种方式，每种方式3个试样，结果取平均值。
- 加热制度：恒速率2.5 °C/min加热至目标温度，恒温180 min，冷却时间4 h；所有试样在105 °C下干燥48 h后恢复至室温以排除含水量对NMR结果的影响。[Xi 2023, pp. 3-5]

## Methods
- 热‑冷处理：五组花岗岩试样在不同目标温度和冷却方式下进行热冲击处理，干燥后待测。
- FE-SEM观察：氩离子抛光‑场发射扫描电镜用于观察微裂纹与微孔隙的形态、开度、长度及连通情况。
- 低场NMR实验：使用纽迈Micro MR12-025 V分析仪（共振频率12 MHz，探头线圈直径60 mm，32.00±0.02 °C，CPMG序列：TE=0.1 ms，TW=3000 ms，NECH=8000，NS=128）。试样先真空2 h、20 MPa饱水24 h，去除表面水后包裹保鲜膜立即测试，获得T₂谱和孔隙度。
- 超声测量：测量纵波波速（P波），用于计算宏观损伤系数。
- 损伤系数计算：基于波速的损伤因子Dₚ₋wave = 1 − (VₚN/Vₚ₀)²；基于孔隙度的损伤因子Dporosity = 1 − (1 − Pₙ)/((1−P₀)·(1−Pₙ)/(1−P₀)的推导式（具体见公式(10)‑(12)）。
- 分形分析：利用Menger海绵模型和NMR T₂谱，通过公式ln[1 − V(≥r)/Vₐ] = (3 − Dₛ) ln(r/L)计算岩石颗粒的分形维数，并按小、中、大孔加权平均获得综合分形维数。
- 数据拟合：对孔隙度、波速、损伤系数等随温度和冷却方式的变化进行非线性拟合，建立经验预测公式。[Xi 2023, pp. 4-20]

## Key Findings
1. 孔隙度演化：同一冷却方式下，花岗岩孔隙度随温度升高呈“先缓后急”增长（25 °C→400 °C缓慢，400→600 °C急剧）。200 °C时自然冷却下孔隙度因热膨胀挤压而轻微下降。600 °C时自然、水、液氮冷却的孔隙度分别达2.48%、2.76%、3.38%，增幅分别为138.45%、165.38%、225.00%。[Xi 2023, pp. 9-11]
2. 孔径分布转化：热处理‑冷却使小孔向中、大孔转化，中、大孔比例显著增加，且孔径增大对孔隙度提升贡献最大。600 °C时大孔含量增幅达132.35 ~ 171.43%（液氮冷却最高）。[Xi 2023, pp. 11-13]
3. 冷却方式效应：T₂谱峰面积、最大弛豫时间T₂max及孔隙度均显示LN₂冷却 > 水冷却 > 自然冷却；低于400 °C时差异较小，600 °C时差异显著。[Xi 2023, pp. 9-10]
4. 宏观‑微观损伤关系：基于波速的损伤因子Dₚ‑wave和基于孔隙度的损伤因子Dporosity均随温度单调增加，液氮冷却损伤最大；两者呈非线性正相关（R² > 0.97），且大孔孔隙度与总孔隙度‑波速拟合曲线高度相似，表明大孔为控制波速和损伤的主导因素。[Xi 2023, pp. 15-20]
5. 分形特征：花岗岩孔隙分布具有良好的统计分形特性（R² = 0.99），分形维数在2.470 ~ 2.510范围内变化。温度 > 200 °C时分形维数随温度升高而降低；同一温度下，液氮冷却的分形维数最高（反映更非均质的孔隙结构），自然冷却最低。分形维数与孔隙损伤因子呈非线性负相关。[Xi 2023, pp. 20-23]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 600 °C时自然冷却孔隙度2.48%，水冷2.76%，液氮冷3.38%，增幅138.45 ~ 225.00% | [Xi 2023, pp. 9-11] | 细粒花岗岩，升温速率2.5 °C/min，恒温180 min，冷却4 h，饱水NMR测量 | 孔隙度‑温度关系可用PN = y₁ + z₁e^(r₁T)拟合（R²≥0.98） |
| 600 °C时大孔含量天然冷1.58%，水冷1.82%，液氮冷2.28%，增幅132.35 ~ 171.43% | [Xi 2023, pp. 11-13] | 孔径分类：小孔r ≤ 0.1 μm，中孔0.1 < r ≤ 1 μm，大孔r > 1 μm | 大孔增加是孔隙度变化的主因，液氮冷却对大孔扩展最显著 |
| 基于波速的损伤Dₚ‑wave拟合式：Dₚ‑wave(T,N)=1+1.21×10⁻⁴T²+0.07T+1.63N²−4.35N | [Xi 2023, pp. 15-16] | T(°C)；N=1自然冷却，2水冷，3液氮冷 | 由实测波速和公式(3)(4)导出，用于任意温度损伤预测 |
| 基于孔隙度的损伤Dporosity拟合式：Dporosity(T,N)=1.61+1.18×10⁻⁴T²−0.05T+0.60N²−0.96N | [Xi 2023, pp. 16-17] | 同前 | 与波速损伤趋势一致，200 °C自然冷却因孔隙度下降出现负值 |
| 大孔孔隙度‑波速关系VₚN,large=1090.84+5639.12e^(−2.15P_large)与总孔隙度曲线高度相似 | [Xi 2023, pp. 18-19] | 所有冷却方式的数据合并拟合 | 实证大孔是决定波速衰减和损伤的关键尺度 |
| 分形维数加权公式Ds = (Dsm·Psm + Dmed·Pmed + Dlar·Plar)/Ptotal，R² = 0.99 | [Xi 2023, pp. 20-21] | 基于NMR T₂谱和Menger海绵模型 | 分形维数随T > 200 °C下降，与Dporosity呈负非线性关系（R²>0.91） |
| FE‑SEM显示常温下微裂纹纳米级、数量少；400 ~ 600 °C后裂纹开度、长度显著增加，出现穿晶裂纹 | [Xi 2023, pp. 7-8] | 氩离子抛光片观察 | 定性证据，需与NMR定量数据互补 |

## Limitations
- 孔隙度‑损伤关系推导中假设岩石基质体积不变，且仅考虑裂隙发展引起的孔隙增加，未考虑矿物相变或颗粒破碎可能带来的基质体积变化 [Xi 2023, pp. 16-17]。
- FE‑SEM只能观测局部微观区域，无法反映整个试样的微裂纹全貌，难以单独量化冷却方式的影响 [Xi 2023, pp. 7-8]。
- 仅针对单一来源的细粒花岗岩，所得拟合公式和分形参数对其他岩性的普适性尚未验证。
- 实验温度最高600 °C，对于HDR储层可能超过650 °C的高温条件，更高温度下的损伤行为需进一步研究 [Xi 2023, pp. 1, 23]。
- 文中未讨论加热速率、恒温时间以及水饱和过程对NMR结果的敏感性，这些参数可能影响定量关系的外推。

## Assumptions / Conditions
- 岩石孔隙度增加完全由热‑冷处理引起的裂隙发展造成，岩石基质体积Vr在处理前后保持不变 [Xi 2023, pp. 16-17]。
- NMR弛豫过程中，表面弛豫占主导，体弛豫和扩散弛豫可忽略；孔径尺寸与横向弛豫时间T₂成正比（r=nT₂），且表面弛豫率为常数 [Xi 2023, pp. 4-5, 20]。
- 孔隙分类标准按弛豫时间划分：小孔0 ~ 5 ms，中孔5 ~ 50 ms，大孔>50 ms；或按半径划分：小孔r ≤ 0.1 μm，中孔0.1 < r ≤ 1 μm，大孔r > 1 μm [Xi 2023, pp. 8, 11]。
- 试样干燥至105 °C、48 h后真空饱水，假设孔隙完全被水充填，NMR信号与孔隙体积呈线性关系。
- 超声波速损伤计算公式Dₚ‑wave = 1 − (VₚN/Vₚ₀)²适用于所有温度与冷却组合，未考虑波传播各向异性变化。
- 分形分析基于Menger海绵构造思想，认为孔隙系统为统计分形体，且中、大孔部分的分形标度区良好 [Xi 2023, pp. 19-20]。

## Key Variables / Parameters
- 热处理温度 T（°C）：200, 400, 500, 600（室温25作为基准）
- 冷却方式 N：自然冷却(1)、水冷却(2)、液氮冷却(3)
- 孔隙度 PN（%）：由NMR T₂谱积分得到
- 小、中、大孔含量及峰值面积：Psm, Pmed, Plar；弛豫峰I、II、III面积
- T₂最大弛豫时间 T₂max（ms），表征最大孔径
- 纵波波速 Vp（m/s），用于宏观损伤因子
- 基于波速的损伤 Dₚ‑wave（‰）：1 − (VₚN/Vₚ₀)²
- 基于孔隙度的损伤 Dporosity（‰）：由PN、P₀推导的损伤变量
- 分形维数 Ds：加权综合分形维数，范围2.470 ~ 2.510
- 拟合常数：各经验公式中的y₁, z₁, r₁, a₁, b₁, j, k, r₁等，依赖于冷却方式 [Xi 2023, pp. 11, 15-17, 21]

## Reusable Claims
- 随着热处理温度的升高（200 ~ 600 °C），细粒花岗岩的NMR孔隙度呈先缓慢后急剧的增加趋势；该行为可由PN = y₁ + z₁exp(r₁T)精确描述（R² ≥ 0.98），且中‑大孔径（r > 0.1 μm）的发育是造成孔隙度上升的主因。条件：升温速率2.5 °C/min、恒温180 min，试样干燥至恒重。
- 冷却方式对损伤的增强效果排序为：液氮冷却（−196 °C） > 常温水冷（≈25 °C） > 自然冷却；随着温度的升高，这一差异在600 °C时更为显著，表现为T₂谱峰右移幅度和最大弛豫时间T₂max的增大。
- 基于波速的宏观损伤因子Dₚ‑wave与基于孔隙度的微观损伤因子Dporosity之间存在非线性正相关关系（R² > 0.97），且大孔孔隙度与波速的拟合式与总孔隙度‑波速拟合式高度一致，表明大孔隙是热‑冷损伤下控制岩石声学性质劣化的关键尺度。
- 花岗岩孔隙系统在热‑冷处理后呈现良好的统计分形特征（R² = 0.99），分形维数Ds在2.47 ~ 2.51之间；当T > 200 °C时，Ds随温度升高而单调下降，并可通过负非线性函数与Dporosity关联（R² > 0.91）。分形维数可作为表征热‑冷岩石损伤程度的辅助参数。
- 所建立的拟合模型（如公式(6)、(13)、(30)、(31)）可用于估算任意热历史（T, N）下细粒花岗岩的孔隙度、波速及宏‑微观损伤程度，适用温度区间25 ~ 600 °C，冷却方式覆盖自然、水、液氮。

## Candidate Concepts
- [[thermal damage of granite]]
- [[pore size distribution and NMR T2 spectrum]]
- [[fractal dimension of rock pores]]
- [[cooling method effect on rock damage]]
- [[micro-macro damage relationship]]
- [[ultrasonic wave velocity damage factor]]
- [[porosity-based damage variable]]
- [[thermal shock cracking]]
- [[Menger sponge model for pore fractals]]
- [[hot dry rock reservoir damage]]

## Candidate Methods
- [[low-field nuclear magnetic resonance (NMR) for rock pore characterization]]
- [[argon ion polishing FE-SEM for microcrack observation]]
- [[NMR T2 spectrum used for pore size classification]]
- [[damage factor from P-wave velocity]]
- [[damage factor from porosity change]]
- [[fractal dimension calculation from NMR data]]
- [[nonlinear empirical fitting for thermal-cooling damage prediction]]
- [[proton density-weighted MRI for pore connectivity]]

## Connections To Other Work
- 与众多研究一致：热‑冷处理会降低岩石波速和强度，且快速冷却（水、液氮）的劣化效果更显著（如Isaka et al. 2019; Kang et al. 2021等）[Xi 2023, pp. 2-2]。
- 先前CT与SEM研究已观测到随温度升高微裂纹增多、扩展，本工作通过NMR量化了孔隙度与孔径分布的演变，深化了对微观损伤机制的理解[Xi 2023, pp. 2-2]。
- 文中利用NMR进行孔隙度测量的方法与Zhang et al. (2019)、Yang et al. (2020)等相似，并参考Li et al. (2021)的数值模拟方法分析热损伤分布[Xi 2023, pp. 2-3]。
- 分形分析方法借鉴了Wu et al. (2019b)的加权平均思想和Yang et al. (2022)的推导路径，将分形维数与损伤耦合[Xi 2023, pp. 19-20]。
- 基于波速的损伤定义参考Sha et al. (2020)的研究，基于孔隙度的损伤变量参考Feng et al. (2022)的框架[Xi 2023, pp. 15-16]。

## Open Questions
- 本研究中建立的损伤关系是否可推广至更高温度（>650 °C）以及更长加热/冷却时间的情形？[Xi 2023, pp. 1, 23]
- 不同岩性（如砂岩、玄武岩）在本文所提出模型中的适用性如何，拟合参数是否需要依岩石矿物学特征重新标定？
- 微观损伤（孔隙度变化）与宏观力学参数（抗压强度、弹性模量）之间的直接映射关系尚未在该研究中给出显式形式，需进一步实验验证。
- 液氮快速冷却形成的极端温度梯度是否会导致非均匀损伤场，对NMR结果的空间代表性产生何种影响？
- 文中分形维数在200 °C附近出现转折，其物理机制及与其他热力学参数（如矿物膨胀系数差异）的内在联系尚不明确。
- MRI显示的质子密度聚集能否进一步发展成渗透网络模型，用于预测热‑冷处理后的渗透率演化？[Xi 2023, pp. 13-14]

## Source Coverage
All 16 non‑empty indexed fragments from the source PDF were processed in a single‑pass Markdown compilation.  
- Indexed text chunks: 16  
- Indexed characters: 78 707  
- Compiled source blocks: 16 (100.0 % coverage by block)  
- Compiled characters: 78 002 (99.1 % coverage by characters)  
Coverage status: full‑index. Strategy: single‑pass‑markdown. Source signature: 8a8f828fb366e111444ec567bc2774d5ec386ab5.
