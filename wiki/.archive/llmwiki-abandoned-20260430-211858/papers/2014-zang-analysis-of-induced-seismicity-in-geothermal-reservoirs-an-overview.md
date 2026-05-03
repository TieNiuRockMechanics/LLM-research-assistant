---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2014-zang-analysis-of-induced-seismicity-in-geothermal-reservoirs-an-overview"
title: "Analysis of Induced Seismicity in Geothermal Reservoirs – An Overview."
status: "draft"
source_pdf: "data/papers/2014 - Analysis of induced seismicity in geothermal reservoirs – An overview.pdf"
collections:
  - "3文章 裂缝网络联通渗透性"
citation: "Zang, Arno, et al. “Analysis of Induced Seismicity in Geothermal Reservoirs – An Overview.” *Geothermics*, vol. 52, 2014, pp. 6–21. *ScienceDirect*, doi:10.1016/j.geothermics.2014.06.005. Accessed 2026."
indexed_texts: "23"
indexed_chars: "114390"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T18:49:11"
---

# Analysis of Induced Seismicity in Geothermal Reservoirs – An Overview.

## One-line Summary
本综述在 GEISER 项目框架下，系统分析了不同构造环境中地热储层（以增强型地热系统 EGS 为主）流体注入诱发地震活动的特征、控制参数与较大震级事件（LME）机制，旨在为地震灾害评估与减缓提供依据。[Zang 2014, pp. 1-2]

## Research Question
如何通过分析地热储层中的诱发地震活动，识别关键储层参数、理解较大震级事件的产生机制，并评估和减轻地震危险性？具体包括：地震响应如何受监测网络设计、速度模型、注入水力参数及原地应力状态的影响？最大观测震级与注入体积、注水性之间存在何种关系？[Zang 2014, pp. 1-3]

## Study Area / Data
研究收集了欧洲 GEISER 项目内及全球多个地热、废水处理、水力压裂与科学钻探场地的数据，重点 EGS 场地包括：
- **欧洲**：法国 Soultz‑sous‑Forêts（张扭/走滑应力，最大震级 2.9）、瑞士 Basel（走滑应力，3.4）、英国 Rosmanowes（走滑，2.0）、德国 Groß‑Schönebeck（正断，<1.0）、KTB 科学钻探（走滑，1.4）等。
- **其他地区**：美国 Geysers（走滑，4.6）、萨尔瓦多 Berlin（正断+走滑，4.4）、澳大利亚 Cooper Basin（逆断，3.7）及 Paralana（逆断，2.5）等。
数据包含最大观测震级、最大井口压力、储层深度、最大注入流量、总注入体积、储层类型、应力体制等。[Zang 2014, pp. 2-3, 3-5]

## Methods
- **地震监测与定位**：依赖井下和地表台网的组合；强调台网几何、速度模型和定位算法对震源位置（地震云）的影响。建议采用地表台网增强方位覆盖以确定震源机制。[Zang 2014, pp. 5-5]
- **波形分析**：利用高质量井下数据进行横波分裂、全波形矩张量反演；采用互相关方法提高事件目录完整性和定位精度。[Zang 2014, pp. 5-5]
- **背景成像**：利用地震噪声互相关技术获取储层速度结构和相对速度变化，以识别可能的无震滑动区；需在刺激前采集基线数据。[Zang 2014, pp. 5-6]
- **参数分析**：将最大注入流量、最大井口压力、最大观测震级、注水性（注入速率/井口压力）等与应力体制结合进行对比分析。[Zang 2014, pp. 5-6, 6-7]

## Key Findings
- 最大观测震级与注入流体体积之间存在总的正相关趋势，但数据离散，尤其对于某些 EGS 场地和废水处理井（如落基山兵工厂 #27 为异常高值）。[Zang 2014, pp. 3-3, 6-7]
- 当以注水性（注入速率/井口压力）为横轴时，最大震级呈现一个上边界趋势，绝大多数数据点位于该边界线以下，Groß‑Schönebeck 为下界，仅落基山兵工厂超出边界。[Zang 2014, pp. 6-7]
- 储层水力参数与应力体制密切相关：Soultz 在正断应力体制下表现为高注入流量、低井口压力；Cooper Basin 在逆断体制下为低注入流量、高井口压力。[Zang 2014, pp. 5-6]
- 近注入井的地震事件波形矩张量的各向同性分量显示张性特征，而远离井的事件更趋纯双力偶剪切。[Zang 2014, pp. 1-2]
- Groß‑Schönebeck 场地的总体地震活动水平极低（仅约 80 个事件），但其注水参数（高压高流量）位于多数数据点的边界之外。[Zang 2014, pp. 2-3, 6-7]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 最大观测震级与总注入体积呈正相关趋势，但离散显著，尤其废水处理井 #27 异常。 | [Zang 2014, pp. 3-3] | 多类别流体注入场地的对比；数据来自表 2。 | 图 1 显示 M_max 与 V_total 的关系；趋势并非严格的线性比例。 |
| 注水性（注入速率/最大井口压力）‑最大震级图存在一个上边界，除落基山兵工厂外所有数据点在边界线以下。 | [Zang 2014, pp. 6-7] | 数据取自表 2，包含 EGS、废水处理、页岩压裂等场地。简单注水性计算，未校正动态裂缝效应。 | 图 4 展示边界趋势，Groß‑Schönebeck 为下界、Paralana 注水性最低。 |
| 应力体制影响水力参数模式：Soultz 正断体制下高流向、低压；Cooper Basin 逆断体制下低流向、高压。 | [Zang 2014, pp. 5-6] | 基于图 3 分析；符号按应力体制着色（NF、SS、TF）。 | 废水处理井也呈低流向特征。 |
| 近注入井事件显示张性矩张量分量，远井事件以双力偶剪切为主。 | [Zang 2014, pp. 1-2] | 基于全波形矩张量反演；具体场地未明确（可能为 Basel 等）。 | 摘要提及，细节未在片段中展开。 |

## Limitations
- 综述依赖的多场地数据在监测网络质量、速度模型精度和处理方法上差异极大，可能影响震源参数的可比性。[Zang 2014, pp. 5-5]
- 经济因素常限制 EGS 项目中井下监测系统的广泛部署，导致部分场地定位和机制解分辨率不足。[Zang 2014, pp. 5-5]
- 简单注水性指标对 EGS 场地的适用性存在概念局限，因其未考虑水力压裂驱动的动态裂缝扩展对注入能力的瞬时影响。[Zang 2014, pp. 6-7]
- 最大震级预测方法（断层尺度关系、确定性裂缝模型、概率方法）的验证与对比未在给定片段中深入展示。[Zang 2014, pp. 3-3]

## Assumptions / Conditions
- 综述假设地震总矩与注入体积的线性比例关系（源于 McGarr, 1976）可作为讨论起点，但承认比例因子并非恒定。[Zang 2014, pp. 6-7]
- 注水性定义为最大注入速率与最大井口压力之比，隐含稳态流动和不考虑裂缝动态开启的简化条件，这一假设对 EGS 刺激阶段可能不成立。[Zang 2014, pp. 6-7]
- 从矩张量分量判断张性或剪切破裂时，依赖于足够台站覆盖和可靠的全波形反演，且假定近场速度模型准确。[Zang 2014, pp. 1-2, 5-5]

## Key Variables / Parameters
- **注入参数**：总注入体积 `V<sub>tot</sub>`、最大注入流量 `Q<sub>max</sub>`、最大井口压力 `P<sub>max</sub>`。
- **地震学参数**：最大观测震级 `M<sub>obs max</sub>`、事件数量、地震总矩、震源机制类型（双力偶、张裂成分）。
- **储层特征**：深度、岩石类型、应力体制（NF、SS、TF）、原始渗透性、预处理裂缝发育程度。
- **衍生指标**：注水性（`Q<sub>max</sub>/P<sub>max</sub>`）。

## Reusable Claims
1. **注水诱发地震的最大观测震级与总注入体积存在正相关趋势，但数据分散，需结合具体应力体制和储层物性解释。** 证据：图1汇总了EGS、废水处理、压裂等多种场地数据，整体随体积增大 M_max 升高，但Groß‑Schönebeck等低震级高体积点为例外。[Zang 2014, pp. 3-3, 6-7] 适用条件：适用于开放性注入系统，尚未完全封闭的储层；若存在大型先存断层并注入压力足以触发其滑动，相关性可能被打破。
2. **注水性‑最大震级图可界定一个经验上边界，该边界可辅助快速评估给定注入策略下可能的最大震级风险。** 证据：大部分数据点落于趋势线以下（仅落基山兵工厂超界），Groß‑Schönebeck为下界、Paralana注水性最低。[Zang 2014, pp. 6-7] 限制：边界线依赖于所收集的数据集，未校正EGS动态裂缝扩展；用于前评估时需佐以地区特定信息。
3. **震源机制的空间演化可指示流体运移路径和破裂模式转变：近注入井事件的张性分量增多，随着距离增加转为纯剪切。** 证据：摘要指出全波形矩张量反演结果，近井事件具张性特征。[Zang 2014, pp. 1-2] 限制：此推断适用于监测台站覆盖充分、能可靠分解矩张量各分量的情形；若速度模型不准或台站几何不佳，可能错误归类。

## Candidate Concepts
- [[Enhanced Geothermal Systems (EGS)]]
- [[induced seismicity]]
- [[larger magnitude events (LME)]]
- [[fluid injection]]
- [[injectivity]]
- [[moment tensor inversion]]
- [[stress regime]]
- [[hydraulic fracturing]]
- [[hydro-shear]]
- [[seismic network design]]
- [[velocity model]]
- [[seismic moment-volume relationship]]

## Candidate Methods
- [[full waveform moment tensor inversion]]
- [[cross-correlation based catalogue enhancement]]
- [[seismic noise interferometry for reservoir imaging]]
- [[baseline ambient noise analysis]]
- [[joint inversion of surface and borehole data]]
- [[borehole station deployment optimization]]
- [[maximum magnitude estimation by fault scaling relationships]]

## Connections To Other Work
- 术语调整：Grünthal (2014) 建议将 larger magnitude events (LME) 改称为 seismic events of economic concern (SEECo)，本综述第 3 节对此作了引用。[Zang 2014, pp. 3-3]
- 总矩‑体积比例关系：最早由 McGarr (1976) 提出，本综述作为讨论起点并指出其在不同条件下的变化。[Zang 2014, pp. 6-7]
- 场地案例中对前人的多处引用：如 Basel (Häring et al., 2008; Evans et al., 2012)、Soultz (Cuenot et al., 2008; Dorbath et al., 2009)、Geysers 冷却诱导剪切滑移 (Rutqvist et al., 2010) 等，均在表格 1 中列出。[Zang 2014, pp. 2-3]

## Open Questions
- 未从索引片段中确认如何从机理上精确区分“诱发”与“触发”地震，以及其对应的最大震级控制因素。
- 注水性‑最大震级边界线是否可适用于尚未发生较大事件的新场地，以及是否受注水策略（如间歇注入、流量控制）的调节，原片段未给出直接答案。
- 如何结合储层先存断层几何和摩擦特性，改善 LME 概率预测的确定性或概率性框架，片段中仅提及需进一步发展，细节未呈现。[Zang 2014, pp. 3-3]

## Source Coverage
本页面依据论文提供的**23 个索引片段**编写，这些片段主要来自论文章节的引言（第 1 节）、多场地数据表格（表 1 与表 2）、部分方法讨论（第 2 节）以及结果图示（图 1–4）的描述。片段覆盖了综述的**范围、主要数据来源和几个关键发现**，但**缺乏第 3 节关于较大震级事件机制、第 4 节最大震级预测方法的详细分析**，以及结论部分的完整表述。因此，本文对 LME 发生机理、预测模型及减缓策略的深度讨论可能存在缺失。
