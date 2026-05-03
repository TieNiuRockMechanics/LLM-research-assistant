---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2018-salimzadeh-thermoporoelastic-effects-during-heat-extraction-from-low-permeability-reservoir"
title: "Thermoporoelastic Effects during Heat Extraction from Low-Permeability Reservoirs."
status: "draft"
source_pdf: "data/papers/2018 - Thermoporoelastic effects during heat extraction from low-permeability reservoirs.pdf"
collections:
  - "part3-3"
citation: "Salimzadeh, Saeed, et al. \"Thermoporoelastic Effects during Heat Extraction from Low-Permeability Reservoirs.\" *Energy*, vol. 142, 2018, pp. 546-558. doi:10.1016/j.energy.2017.10.059."
indexed_texts: "12"
indexed_chars: "57552"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T22:31:39"
---

# Thermoporoelastic Effects during Heat Extraction from Low-Permeability Reservoirs.

## One-line Summary
该研究通过数值模拟，探究低渗透地热储层（类似增强型地热系统，EGS）在热提取过程中，热孔弹性耦合效应对单一水平圆盘形裂缝的裂隙开度、流体流动和产热温度的影响，并评估了排水与不排水热膨胀系数假设的适用性 [Salimzadeh 2018]。

## Research Question
在低渗透结晶岩中提取地热时，常用不排水热膨胀系数来代表饱和基质的体积热响应，但真实的流体条件可能并非完全“不排水”。本研究要回答的核心问题是：在不同基质渗透率、Biot 系数和孔隙度条件下，热孔弹性效应如何影响裂缝水力特性与产热过程？以及何种条件下不排水假设不再适用？[Salimzadeh 2018, pp. 3-4, 10-15]

## Study Area / Data
模拟实例取自 Guo et al. (2016)，大致对应澳大利亚 Cooper Basin 的 Habanero 项目。几何构型为一个半径 500 m 的水平圆盘形裂缝，置于 3×3×3 km 立方体岩块的中心。注入井与生产井位于裂缝内，间距 500 m。初始储层压力 34 MPa，初始温度 200°C。注入采用恒定速率 0.0125 m³/s。岩石为低渗透热结晶岩（基质孔隙度 φ=0.01），饱和流体为水 [Salimzadeh 2018, pp. 8-10]。

## Methods
- **耦合策略**：将全耦合热‑水力‑力学（THM）问题解耦为“热‑水力（TH）模型”和“力学接触（M）模型”，两者迭代求解。TH 模型求解基质与裂缝中的非等温流，力学接触模型求解由热孔弹性压缩引起的裂缝接触应力与开度变化 [Salimzadeh 2018, pp. 4-8]。
- **控制方程**：采用隐式耦合形式的一体化方程（式 15‑19），涵盖基质变形、基质流体流动、基质传热、裂缝内流动与传热。关键耦合项包括基质中热‑孔弹性引起的压力变化、裂缝开度对力学应力的依赖等 [Salimzadeh 2018, pp. 6-8]。
- **裂缝模型**：使用 Barton‑Bandis 经验模型描述裂缝在接触应力下的平均水力开度（式 12），裂缝法向刚度 Kn 由模型参数 a、b 确定。裂缝开度变化进一步通过 Kn 与裂缝流体压力关联（式 13‑14）[Salimzadeh 2018, pp. 6-8]。
- **数值方法**：采用有限元法（Galerkin 法空间离散，有限差分时间离散）。力学接触模型使用基于间隙的增广拉格朗日法处理裂缝面上的摩擦接触约束，并假设接触面保持“粘滞”状态（无相对滑动）。TH 与 M 模型在每个时间步内迭代至收敛 [Salimzadeh 2018, pp. 8]。
- **验证**：模型已针对粘性、韧性和滤失区的水力压裂解、单裂缝热传播解析解以及双缺口裂纹扩展实验等多类问题进行过验证 [Salimzadeh 2018, pp. 8]。本研究中，还通过与 Guo et al. (2016) 的算例对比，进一步验证了模拟器和网格的可靠性 [Salimzadeh 2018, pp. 10]。

## Key Findings
- **不排水与排水热响应的显著差异**：对给定岩石参数（φ=0.01，α=1），不排水体积热膨胀系数 βu = 3.0×10⁻⁵ /°C，比岩石固体热膨胀系数高约 25%（因为水的热膨胀系数约为岩石的 30 倍）。若不排水热膨胀系数被用于饱和基质，则计算得到的基质收缩更大，裂缝开度增加，导致热突破更早。示例中，产流温度降至 130°C 的突破时间，不排水情形不足 21 年，而排水（即仅用岩石固体系数）情形延长至 27.6 年 [Salimzadeh 2018, pp. 10-11]。
- **基质渗透率的控制作用与不排水条件的临界值**：基质渗透率降低时，由基质冷却引起的压力耗散逐渐增强。当基质渗透率 km 降至 10⁻²² m² 时，结果与不排水解吻合；但当 km = 10⁻²⁰ m² 时，不排水假设已不准确。推导表明，要实现不排水行为，需满足 km ≤ 8.43×10⁻²³ m²，而实例中的 km = 10⁻²⁰ m² 远高于此临界值，因此实际系统处于部分排水状态 [Salimzadeh 2018, pp. 12-13]。
- **热传递以导热为主**：基质渗透率变化（10⁻¹⁷ 至 10⁻²² m²）对 30 年后的温度分布影响很小，表明基质内热传输主要是一维热传导，仅在羽流边缘存在二维效应 [Salimzadeh 2018, pp. 12]。
- **开度分布与压力耗散**：热孔弹性应力在注入点附近形成高开度区，并朝向生产井方向延伸。随着基质渗透率降低，基质压力耗散加剧，导致更多基质收缩，裂缝开度反而增大，这有助于流体向生产井流动 [Salimzadeh 2018, pp. 12]。
- **Biot 系数的影响**：将 Biot 系数从 1 降至 0.2（更接近真实极低孔隙度花岗岩），裂缝开度随之减小，产流温度下降趋缓（130°C 到达时间约 22.4 年），不排水与排水行为差距缩小但仍明显 [Salimzadeh 2018, pp. 13-14]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 使用不排水热膨胀系数 βu=3.0×10⁻⁵ /°C 时，产流温度降至130°C的时间不足21年；使用排水（岩石固体）系数时延长至27.6年 | [Salimzadeh 2018, pp. 10-11] | φ=0.01，α=1，基岩低渗，均质初始裂缝开度 | 验证了与Guo et al. (2016) 一致性 |
| 基质渗透率 km=10⁻²² m² 的结果与不排水解良好吻合；km=10⁻²⁰ m² 时已偏离不排水解 | [Salimzadeh 2018, pp. 12-13] | 模拟30年，相同热-水力边界 | 支持了不排水假设需极低渗透率 |
| 不排水行为的临界基质渗透率推导为 km ≤ 8.43×10⁻²³ m² | [Salimzadeh 2018, pp. 13] | 基于无量纲扩散时间与热时间的比较 | 该临界值远低于示例渗透率 |
| 基质渗透率变化对温度分布影响很小，热传输以传导为主 | [Salimzadeh 2018, pp. 12] | 30年后温度剖面 | 支持TH模型中的简化假设 |
| Biot 系数α=0.2时，裂缝开度减小，130°C突破时间约22.4年 | [Salimzadeh 2018, pp. 13-14] | 相同初始和边界条件，σ’=0.2 | 部分排水行为对α敏感 |

## Limitations
- 模拟局限于单个水平圆盘形裂缝，且裂缝表面假设为粘滞（无剪切滑动），未考虑真实裂缝网络的多裂缝相互作用、错动及剪切扩容 [Salimzadeh 2018, pp. 8]。
- 岩体被假定为均质、各向同性，未纳入天然裂隙、非均质性和各向异性的影响 [Salimzadeh 2018, pp. 8-10]。
- 研究未考虑流体与岩石的化学反应（如溶解、沉淀）导致渗透率或孔隙度的长期变化 [未从索引片段中确认]。
- 数值模型虽经过基准验证，但缺少与现场长期监测数据的直接对比，其预测能力局限于所模拟的理想化条件 [Salimzadeh 2018, pp. 8]。
- 分析以恒定速率注入且产流温度变化为关注点，未探讨变流量运行或完全产热周期的影响 [未从索引片段中确认]。

## Assumptions / Conditions
- 裂缝为半径 500 m 的水平圆盘形平面，位于3×3×3 km的弹性均质体中 [Salimzadeh 2018, pp. 8-10]。
- 流体为不可压缩或微弱可压的纯水，裂缝内流动遵守立方定律 [Salimzadeh 2018, pp. 3-4, 6-8]。
- 基质力学行为为线弹性，热‑孔弹性耦合通过 Biot 系数和热膨胀系数实现 [Salimzadeh 2018, pp. 4-6]。
- 裂缝力学行为由 Barton‑Bandis 经验模型描述，且假设接触期间裂缝面间无相对滑动（“stick”模式）[Salimzadeh 2018, pp. 6-8]。
- 热过程仅考虑热传导（基质）和对流（裂缝），忽略热辐射和流体相变 [Salimzadeh 2018, pp. 6-8]。
- 基质与裂缝间的流体交换通过法向渗透率系数 kn 描述，且假设局部热平衡 [Salimzadeh 2018, pp. 4-6]。
- 不排水热膨胀系数的理论推导基于无流体泄漏、基质孔隙压力完全由温度变化引起的假设 [Salimzadeh 2018, pp. 10]。
- 渗透率临界值分析基于无量纲时间比，假设热前缘传播速度远大于压力扩散 [Salimzadeh 2018, pp. 13]。

## Key Variables / Parameters
- 裂缝水力开度 \(a_f\)、初始开度 \(a_0\)、Barton‑Bandis 参数 \(a\) 和 \(b\)
- 基质渗透率 \(k_m\)、流体的粘度 \(\mu_f\)、基质孔隙度 \(\phi\)
- 基质压力 \(p_m\)、裂缝压力 \(p_f\)、基质温度 \(T_m\)、裂缝温度 \(T_f\)
- 岩石固体体积热膨胀系数 \(\beta_s\)、流体的 \(\beta_f\)、不排水等效系数 \(\beta_u\)（或 \(\beta_{eq}\)）
- Biot 系数 \(\alpha\)、Skempton 系数 \(B\)、岩石体积模量 \(K\)、固体颗粒模量 \(K_s\)
- 流体压缩系数 \(c_f\)、裂缝法向刚度 \(K_n\)
- 几何与操作参数：裂缝半径 500 m，井间距 500 m，域尺寸 3×3×3 km，初始压力 34 MPa，初始温度 200°C，注入速率 0.0125 m³/s
- 无量纲压力扩散时间 \(t_{Dp}\) 与热扩散时间 \(t_{Dh}\)，用于判断不排水条件界限

## Reusable Claims
- **Claim 1**: 在低渗透 EGS 储层中，若直接采用不排水热膨胀系数而忽略实际存在的部分排水效应，将高估基质收缩与裂缝开度增加，导致预测的热突破时间显著提前。此效应在水的热膨胀系数远大于岩石时尤为明显。**条件**: 基质渗透率处于 10⁻¹⁸ 至 10⁻²¹ m² 量级且孔隙度很低时，系统并非完全排水或完全不排水。**证据**: 模拟显示不排水假设下温度降至 130°C 不足 21 年，而等效排水假设下为 27.6 年 [Salimzadeh 2018, pp. 10-11]。**限制**: 结论基于给定的岩石和流体参数，且裂缝为单一水平裂缝。
- **Claim 2**: 对于典型的低孔（~0.01）结晶岩，要使基质的热‑孔弹性行为可近似为不排水，基质渗透率须低于约 8.4×10⁻²³ m²；渗透率在 10⁻²⁰ m² 量级时已处于部分排水状态，不能安全地沿用不排水热膨胀系数。**条件**: 采用式 (30)‑(33) 推导，适用于 Biot 系数约 1 的情况。**证据**: 通过无量纲时间比较和数值验证 [Salimzadeh 2018, pp. 13]。**限制**: 该临界值依赖于热扩散系数与压力扩散系数的比值，适用于本文参数范围。
- **Claim 3**: 热孔弹性响应对 Biot 系数敏感：较低的 Biot 系数（如 α=0.2）减弱了孔隙压力变化引起的体积应变，导致计算的裂缝开度减小，延长热产出时间，并使结果向排水解靠近，但仍有明显差异。**条件**: 孔隙度极低的结晶岩，Biot 系数通常小于 1。**证据**: 当 α=0.2 时，产出流体温度降至 130°C 约需 22.4 年 [Salimzadeh 2018, pp. 13-14]。**限制**: 仅针对特定几何和操作参数。

## Candidate Concepts
[[thermoporoelasticity]], [[fracture aperture (Barton-Bandis)]], [[undrained thermal expansion coefficient]], [[enhanced geothermal systems (EGS)]], [[low-permeability reservoir]], [[penny-shaped fracture]], [[cubic law]], [[Skempton coefficient]], [[Biot coefficient]], [[dimensionless time analysis]], [[heat extraction]], [[contact mechanics in fractures]], [[implicit coupling]]

## Candidate Methods
[[coupled THM numerical model]], [[Galerkin finite element method]], [[augmented Lagrangian contact algorithm]], [[Barton-Bandis fracture model]], [[implicit-explicit decoupling (TH-M)]], [[finite difference time discretization]], [[dimensionless pressure & thermal diffusion analysis]]

## Connections To Other Work
- 本研究直接基于 Salimzadeh et al. (2017a, b, c) 开发的完全耦合热‑孔弹性裂缝模型，但进行了形式上的解耦以降低计算成本 [Salimzadeh 2018, pp. 4-6]。
- 算例及验证数据引自 Guo et al. (2016) 的 EGS 模拟，并与其结果在均质初始开度条件下取得了良好的一致性 [Salimzadeh 2018, pp. 10]。
- 裂缝的力学响应采用 Barton‑Bandis 模型（Bandis et al. 1983; Barton et al. 1986），该模型广泛用于描述地下裂缝在法向应力下的非线性闭合行为 [Salimzadeh 2018, pp. 6]。
- 不排水热膨胀系数的概念与分析源自 McTigue (1986)，本研究中进一步导出了等效系数的显式表达式并与数值模型结合 [Salimzadeh 2018, pp. 10]。
- 从主题上，该工作可与 [[fracture network EGS simulation]]、[[thermal breakthrough prediction in doublet systems]]、[[poroelastic backstress in fractured media]] 等方法与概念建立联系。

## Open Questions
- 在包含多裂缝和天然裂隙网络的非均质储层中，本研究所揭示的部分排水行为会如何演化？[未从索引片段中确认]
- 若允许裂缝发生剪切滑动（非 stick 模式），裂缝开度的动力变化及对应的热‑水力响应将如何改变？[未从索引片段中确认]
- 长期运行下，矿物沉淀/溶解效应是否会显著影响基质渗透率，从而改变部分排水的程度？[未从索引片段中确认]
- 对于不同注入流体（如 CO₂ 或超临界水），热膨胀系数差异极大，所得临界渗透率条件需要如何修正？[未从索引片段中确认]
- 现场监测数据（如微震、压力、温度）的缺乏使本模型的现场适用性验证成为关键缺口 [未从索引片段中确认]。

## Source Coverage
本 Markdown 页依据 12 个索引片段整理，这些片段覆盖了摘要、引言中的问题背景、计算模型的耦合框架与控制方程、模拟设置、部分参数敏感性结果以及关于不排水/排水行为的关键讨论。信息侧重模型描述、数值实现与核心力学机制，对模拟的全部参数表格、所有敏感性案例的完整结果图以及论文的结论部分覆盖不足。例如，岩石固体热膨胀系数 βs 的具体数值未直接给出，仅从 βu 关系推断；对孔隙度变化的系统性影响仅在片段中简要提及。因此，本页所呈现的部分参数细节和量化关系可能无法反映原文全部数据。总体而言，片段偏向方法-结果，缺失对现场应用、全耦合与解耦方案比较等深入讨论的细节。
