---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2017-cartwright-a-review-of-radioactive-isotopes-and-other-residence-time-tracers-in-understandi"
title: "A Review of Radioactive Isotopes and Other Residence Time Tracers in Understanding Groundwater Recharge: Possibilities, Challenges, and Limitations."
status: "draft"
source_pdf: "data/papers/2017 - A review of radioactive isotopes and other residence time tracers in understanding groundwater recharge Possibilities, challenges, and limitations.pdf"
collections:
citation: "Cartwright, Ian, et al. \"A Review of Radioactive Isotopes and Other Residence Time Tracers in Understanding Groundwater Recharge: Possibilities, Challenges, and Limitations.\" *Journal of Hydrology*, vol. 555, 2017, pp. 797–811. doi:10.1016/j.jhydrol.2017.10.053."
indexed_texts: "23"
indexed_chars: "114377"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T20:24:22"
---

# A Review of Radioactive Isotopes and Other Residence Time Tracers in Understanding Groundwater Recharge: Possibilities, Challenges, and Limitations.

## One-line Summary
本文系统综述了利用放射性同位素（³H、¹⁴C、³⁶Cl、惰性气体同位素）及随时间变化的人造示踪剂（如CFCs、SF₆）估算地下水补给率的原理、应用、优势与局限性，强调所有示踪剂均给出平均停留时间与平均补给率，需在宏观弥散与混合的制约下谨慎解读 [Cartwright 2017, pp. 1-2]。

## Research Question
如何利用放射性同位素及其他停留时间示踪剂确定地下水补给的位置与量级？这些示踪剂在应用中面临哪些技术困难、解释挑战和方法学局限？[Cartwright 2017, pp. 1-2]

## Study Area / Data
本文为综述性论文，不局限于单一研究区。文中引用了大量案例研究（见 Table S1），涵盖从温带、热带到半干旱、干旱区的多种气候与水文地质条件，但索引片段未提供具体案例数据 [Cartwright 2017, pp. 2-3]。数据来源主要包括：
- 全球大气降水中的 ³H、¹⁴C 等同位素记录 (IAEA 网络)；
- 文献中报道的 CFCs、SF₆、⁸⁵Kr 等大气浓度历史曲线；
- 各研究区的实际地下水样品测试（示踪剂浓度、主要离子、稳定同位素等）[Cartwright 2017, pp. 2-3, 6-6]。

## Methods
**1. 示踪剂类型与适用范围**  
- 放射性同位素：³H（半衰期 12.32 a）、¹⁴C（~5730 a）、³⁶Cl（301 ka）以及惰性气体放射性同位素 ³⁹Ar、⁸¹Kr、⁸⁵Kr，覆盖几年到数十万年的停留时间 [Cartwright 2017, pp. 2-3]。  
- 大气累积示踪剂：CFCs、SF₆、Halon-1301 等，以其大气浓度的时间演化推断过去百年的补给时间 [Cartwright 2017, pp. 2-3]。  
- 其他辅助指标：主要离子浓度、δ¹⁸O 和 δ²H 的季节性变化等 [Cartwright 2017, pp. 2-3]。

**2. 停留时间推断模型**  
- 集总参数模型：指数流模型（均匀潜水含水层、均匀补给）、指数-活塞流模型、部分指数流模型以及基于一维对流-弥散方程的弥散模型 [Cartwright 2017, pp. 3-4]。  
- 更新率（Renewal Rate）方法：假定含水层上部每年接受补给并与旧水混合，旧水被向下置换，用年度演化方程 Cg(t) = (1–RN) Cg(t–1) e⁻ᵏ + RN Ci(t) 模拟示踪剂浓度变化 [Cartwright 2017, pp. 4-5]。

**3. 由停留时间估算补给率 R 的方程**  
- 垂直流：R = φ v_z，v_z = z/t_s [Cartwright 2017, pp. 4-5]。  
- 承压含水层水平流：R = φ v_x (a_aq / a_r) [Cartwright 2017, pp. 4-5]。  
- 指数流系统：R = φ H ln(H/(H–z)) / s_z [Cartwright 2017, pp. 5-5]。  
- 更新率与补给率关联（未在片段中给出直接换算公式，但更新率 RN 本身指示年补给分数）[Cartwright 2017, pp. 5-5]。

**4. 特定示踪剂的解释方法**  
- ³H/³He 法：t = (1/k) ln( ³He_T / ³H + 1 )，无需已知 ³H 输入函数，但需校正非衰变成因的 ³He 及扩散损失 [Cartwright 2017, pp. 6-6]。  
- ¹⁴C 测年：需校正“老碳”稀释效应，常用主要离子、稳定碳同位素及 ⁸⁷Sr/⁸⁶Sr 等辅助 [Cartwright 2017, pp. 6-7]。

## Key Findings
- 所有放射性及大气累积示踪剂记录的是平均停留时间与平均补给率，并非特定年份的补给事件或水的“年龄”，其平均时间尺度随停留时间增长而加大 [Cartwright 2017, pp. 1-2]。
- 示踪剂覆盖的时间范围从几年（³H、CFCs）到数十万年（³⁶Cl），因此可以同时刻画现代补给与古补给行为 [Cartwright 2017, pp. 2-3]。
- 宏观弥散与地下水系统中不同水流路径的混合严重制约了停留时间与补给率估算的精度 [Cartwright 2017, pp. 1-2, 4-5]。
- 在补给计算中，多数研究依赖于现有基础设施（如开采井），其采样层位可能不完全代表含水层流通部分，可能产生偏差 [Cartwright 2017, pp. 1-2]。
- ³H/³He 法反映饱和带停留时间，因此估算的是纯补给速率（不含非饱和带入渗时间），且在低补给率条件下 ³He 的扩散损失可达 20% [Cartwright 2017, pp. 6-6]。
- ¹⁴C 是使用最广泛的长周期示踪剂，但在确定老碳贡献时存在难点，尤其在多种老碳源共存的系统中，限制了停留时间精度 [Cartwright 2017, pp. 6-7]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 所有示踪剂记录的是平均停留时间与平均补给率，非具体年龄或年份补给率 | [Cartwright 2017, pp. 1-2] | 适用于所有已讨论的停留时间示踪剂 | 这一性质有利于提供代表性补给率，但不利于与水位波动等短期方法对比 |
| 宏观弥散和混合限制了地下水停留时间和补给率的估算精度 | [Cartwright 2017, pp. 1-2] | 所有类型含水层，尤其当采样井截取混合水时 | 成为普遍性限制因素 |
| 在指数流系统中，补给率 R 可由 R = φ H ln(H/(H–z)) / s_z 计算 | [Cartwright 2017, pp. 4-5] | 均质潜水含水层、分布均匀的补给、厚度恒定 | 方程应用依赖已知孔隙度 φ 和有效厚度 H |
| 更新率模型可通过逐年混合方程模拟示踪剂浓度，RN 表示年补给置换分数 | [Cartwright 2017, pp. 4-5] | 通常假设年补给事件与年混合周期，半干旱区可调整时间步长 | 可用时间序列或单一示踪剂测量值求解 RN |
| ³He 扩散损失在补给率低至 30 mm/yr 时可达 20% | [Cartwright 2017, pp. 6-6] | 基于 Solomon and Cook (2000) 的建议 | 导致 ³H/³He 年龄偏老，需校正 |
| 南半球 ³H 炸弹脉冲残余活度已低于现代降水，允许用单次测量配合集总参数模型或更新率法估算停留时间 | [Cartwright 2017, pp. 6-6] | 南半球地区 | 北半球仍需时间序列或需判断水样位于炸弹峰哪一侧 |

## Limitations
- 宏观弥散和混合效应使任何单一年龄或停留时间都有可能被“抹平”，无法赋予样品一个精确值 [Cartwright 2017, pp. 1-2]。
- 许多研究利用现有井孔，其筛选段可能仅截取含水层部分厚度，导致得出的停留时间与补给率不代表整个含水层 [Cartwright 2017, pp. 1-2]。
- 不同示踪剂的时间平均尺度不同，导致它们给出的补给率难以与短期方法（如水位波动法、蒸渗仪）直接对比 [Cartwright 2017, pp. 1-2]。
- ¹⁴C 测年要求精确估算老碳稀释，但在多源老碳系统中存在较大不确定性 [Cartwright 2017, pp. 6-7]。
- ³H/³He 法受陆源 He 干扰和 ³He 扩散损失影响，在低补给率地区损失显著 [Cartwright 2017, pp. 6-6]。
- 北半球 ³H 炸弹峰已衰减且弥散，难以识别精确峰位，限制了峰位位移法的应用 [Cartwright 2017, pp. 5-6]。

## Assumptions / Conditions
**模型假设与适用条件**：
- 指数流模型：含水层均质、各向同性、恒定厚度，补给在空间和时间上均匀分布，地下水流线垂直 [Cartwright 2017, pp. 3-4]。
- 指数-活塞流模型：存在承压与无压流动段的组合 [Cartwright 2017, pp. 3-4]。
- 部分指数流模型：采样井仅截取含水层上部特定比例 [Cartwright 2017, pp. 3-4]。
- 弥散模型：符合一维对流-弥散方程 [Cartwright 2017, pp. 3-4]。
- 更新率方法：假定年内补给水与上部地下水完全混合，且混合后等体积水被向下传输，时间步长通常设为 1 年 [Cartwright 2017, pp. 4-5]。
- ³H/³He 法：需假定除 ³H 衰变外无其他显著的 ³He 源，且 ³He 扩散损失可被合理估计或忽略 [Cartwright 2017, pp. 6-6]。
- ¹⁴C 测年：需假定土壤 CO₂ 的 ¹⁴C 初始活性已知或可通过地化模型校正 [Cartwright 2017, pp. 6-7]。
- 补给率由停留时间换算时，通常假定流动路径为垂直（R = φ v_z）或已知补给区与含水层截面积比 [Cartwright 2017, pp. 4-5]。

## Key Variables / Parameters
| 变量/参数 | 描述 | 参考 |
|-----------|------|------|
| R | 补给率 [L T⁻¹] | [Cartwright 2017, pp. 4-5] |
| RN | 更新率 [T⁻¹]，通常以年⁻¹ 表示 | [Cartwright 2017, pp. 4-5] |
| v_z, v_x | 垂向与水平向地下水流速 [L T⁻¹] | [Cartwright 2017, pp. 4-5] |
| a_aq, a_r | 含水层截面积、补给区面积 [L²] | [Cartwright 2017, pp. 4-5] |
| H, H_b | 含水层厚度、有效厚度 [L] | [Cartwright 2017, pp. 4-5] |
| z | 采样深度（水位以下）[L] | [Cartwright 2017, pp. 4-5] |
| φ | 孔隙度 | [Cartwright 2017, pp. 4-5] |
| t, s_z, s | 时间、深度 z 处的停留时间、停留时间 [T] | [Cartwright 2017, pp. 4-5] |
| k | 衰变常数 [T⁻¹] | [Cartwright 2017, pp. 4-5] |
| Cg, Ci | 地下水中示踪剂浓度/活度、输入浓度/活度 | [Cartwright 2017, pp. 4-5] |
| C_ppt | 降水中溶质长期平均浓度 [M V⁻¹] | [Cartwright 2017, pp. 3-4] |
| P | 降水量 [L T⁻¹] | [Cartwright 2017, pp. 3-4] |

## Reusable Claims
1. **停留时间示踪剂反映的是平均量而非瞬时值**：所有讨论的示踪剂（放射性同位素、CFCs、SF₆ 等）估算的都是地下水系统的平均停留时间和平均补给率，其平均窗口随停留时间延长而增加 [Cartwright 2017, pp. 1-2]。**适用条件**：任何使用这些示踪剂的补给研究。**限制**：该性质使得示踪剂结果难以与短期、点尺度的补给观测直接对比。
2. **指数流模型下的补给率公式**：对于厚度 H 的均质潜水含水层，当采样点位于水位下深度 z 且停留时间为 s_z 时，补给率 R 可由 R = φ H ln(H/(H–z)) / s_z 计算 [Cartwright 2017, pp. 4-5]。**适用条件**：满足指数流模型假设（均匀补给、均质、厚度固定）。**限制**：需确定有效厚度、孔隙度，且要求 s_z 估计准确；宏观弥散未被考虑。
3. **更新率方法可处理不规律补给**：更新率模型 Cg(t) = (1–RN) Cg(t–1) e⁻ᵏ + RN Ci(t) 不强制要求补给为年周期，可调整时间步长用于半干旱区 [Cartwright 2017, pp. 4-5]。**适用条件**：具备年内平均输入函数 Ci(t)，并已知衰变常数 k。**限制**：要求混合完全，长期运行可得到合理的平均 RN，但对个别年份的代表性有限。
4. **³H/³He 法可独立于输入函数计算停留时间**：公式 t = (1/k) ln(³He_T/³H + 1) 消除了对 ³H 输入历史的需求 [Cartwright 2017, pp. 6-6]。**适用条件**：³H 活性可测，且能准确扣除大气及陆源 ³He，同时校正 ³He 的扩散损失。**限制**：低补给率下扩散损失显著，可能大幅高估年龄。

## Candidate Concepts
- [[groundwater recharge]]
- [[residence time tracers]]
- [[radioactive isotopes]]
- [[lumped parameter models]]
- [[exponential flow model]]
- [[exponential-piston flow model]]
- [[partial-exponential flow model]]
- [[dispersion model]]
- [[renewal rate]]
- [[bomb pulse tritium]]
- [[tritium-helium-3 method]]
- [[carbon-14 dating]]
- [[CFCs and SF6 as age tracers]]
- [[macroscopic dispersion]]
- [[diffuse vs focused recharge]]
- [[semi-arid recharge]]

## Candidate Methods
- [[exponential flow model]]
- [[exponential-piston flow model]]
- [[partial-exponential flow model]]
- [[dispersion model (LPM)]]
- [[renewal rate approach]]
- [[tritium-helium-3 dating]]
- [[14C age correction with geochemical models]]
- [[CFC and SF6 dating]]
- [[noble gas radioactive isotope dating (39Ar, 81Kr, 85Kr)]]
- [[water table fluctuation method]] (作为对比)
- [[lysimeter method]] (作为对比)
- [[chloride mass balance]] (提及但未详细描述)

## Connections To Other Work
- 本文综述中提到多个早期综合评述，如 Allison et al. (1994)、de Vries and Simmers (2002)、Scanlon et al. (2002, 2006)、Anderson (2005)、Healy (2010)，这些工作聚焦于补给的物理测量与模拟 [Cartwright 2017, pp. 2-2]。
- 集总参数模型的经典框架来自 Maloszewski and Zuber (1982, 1992) 以及 Jurgens et al. (2012) 的扩展与应用 [Cartwright 2017, pp. 3-4]。
- 更新率方法由 Leduc et al. (2000)、Le Gal La Salle et al. (2001) 提出并在非洲半干旱区应用，后被 Cartwright et al. (2007b) 等人推广 [Cartwright 2017, pp. 4-5]。
- 关于宏观弥散对停留时间示踪剂解释的影响，与 Sudicky and Frind (1981)、Bethke and Johnson (2008)、McCallum et al. (2014b, 2015)、Suckow (2014)、Gleeson et al. (2016)、Kirchner (2016a,b) 等研究相衔接 [Cartwright 2017, pp. 4-5]。
- 本文体现的示踪剂方法论可与物理补给估算方法（如 [[water table fluctuation]]、[[lysimeter]]、[[catchment water budget]]）形成互补或对照 [Cartwright 2017, pp. 2-2, 2-3]。

## Open Questions
- 如何在弥散和混合不可避免的情况下，为给定样品赋予一个有物理意义的“平均停留时间”？[Cartwright 2017, pp. 4-5]
- 在多种老碳源共存且各自贡献难以量化的系统中，如何提高 ¹⁴C 补给率估算的可靠性？[Cartwright 2017, pp. 6-7]
- 不同示踪剂给出的补给率因时间平均尺度差异而不一致时，如何设计和实施多示踪剂联合反演？方法学指南尚不完善。
- 对于非常低补给的地区（如极端干旱区），现有示踪剂（包括惰性气体）的灵敏度和校正方法是否足以产生有意义的补给率约束？[Cartwright 2017, pp. 6-6] 提及 ¹⁴C 在干旱区不饱和带 CO₂ 的 ¹⁴C 活度可能 <100 pMC，但未给出统一应对策略。
- 如何更有效地利用非理想井孔（滤水管段过长、井间混合）的数据？片段仅指出问题，未提供解决方案 [Cartwright 2017, pp. 1-2]。

## Source Coverage
本页依据该论文的 23 个索引片段编撰，片段主要覆盖摘要、引言（挑战、术语）、示踪剂类型与原理、集总参数模型与补给率方程、更新率方法、³H、¹⁴C 等关键示踪剂的细节与局限性。Table S1 中包含的案例研究及应用数值未在片段中体现，因此无法提供具体研究区的定量结果。讨论部分关于宏弥散与混合的深入分析仅在片段中提及，处理方案的具体细节可能存在于全文后半部分，未充分覆盖。此外，关于 ³⁶Cl 和惰性气体同位素（³⁹Ar、⁸¹Kr）的应用实例和局限性讨论也较为简略。因此，本知识页的内容偏向方法学概览和识别的主要问题，缺失了大量具体案例细节及部分方法的深入定量讨论。
