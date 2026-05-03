---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2017-jiang-experimental-study-of-convective-heat-transfer-of-carbon-dioxide-at-supercritical-pre"
title: "Experimental Study of Convective Heat Transfer of Carbon Dioxide at Supercritical Pressures in a Horizontal Rock Fracture and Its Application to Enhanced Geothermal Systems."
status: "draft"
source_pdf: "data/papers/2017 - Experimental study of convective heat transfer of carbon dioxide at supercritical pressures in a horizontal rock fracture and its application to enhanced geothe.pdf"
collections:
citation: "Jiang, Peixue, et al. “Experimental Study of Convective Heat Transfer of Carbon Dioxide at Supercritical Pressures in a Horizontal Rock Fracture and Its Application to Enhanced Geothermal Systems.” *Applied Thermal Engineering*, vol. 117, 2017, pp. 39–49. doi:10.1016/j.applthermaleng.2017.01.078. Accessed 2026."
indexed_texts: "11"
indexed_chars: "51974"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T20:42:07"
---

# Experimental Study of Convective Heat Transfer of Carbon Dioxide at Supercritical Pressures in a Horizontal Rock Fracture and Its Application to Enhanced Geothermal Systems.

## One-line Summary
本研究实验探究了超临界压力下二氧化碳在水平岩石裂隙中的层流对流传热特性，发现其对流传热受流体物性急剧变化影响显著，并提出传热关联式以改进增强型地热系统（EGS）的场级模拟 [Jiang 2017, pp. 1-2]。

## Research Question
- 超临界压力下CO₂在岩石裂隙中的对流传热特性是怎样的？
- 流体物性（近拟临界点）的急剧变化如何影响局部传热性能？
- 能否提出一个可用于EGS场级模拟的传热关联式 [Jiang 2017, pp. 1-2]？

## Study Area / Data
- **岩样**：花岗岩岩心，直径50 mm，长度50 mm，加工成两个光滑平行面，其间以云母片支撑形成0.2毫米水平光滑裂隙 [Jiang 2017, pp. 3-4]。
- **实验工况**：初始岩石温度55至250°C，CO₂质量流量0.13至0.75 kg/h，超临界压力8.1 MPa，共计10个实验工况 [Jiang 2017, pp. 3-4]。
- **数据来源**：实验室搭建的高温高压装置，测量裂隙壁面温度、流体进出口温度、流体压力、压差和质量流量 [Jiang 2017, pp. 1-4]。

## Methods
- **实验装置**：搭建了一套可运行在温度顶高280°C、流体压力14 MPa、围压28 MPa下的实验系统 [Jiang 2017, pp. 1-2, 9-10]。
- **测试段**：水平放置花岗岩裂隙，孔径0.2 mm，基质渗透率极低（视为不渗透）[Jiang 2017, pp. 3-4]。
- **数据处理方法**：提出一种实验数据处理与还原方法，结合数值模型计算局部热流密度 hx，进而得到局部Nusselt数。实验传递给CFD逆向计算，与实验对比误差在7%以内 [Jiang 2017, pp. 1-2, 4-6]。
- **关键公式**：
  - 局部传热系数：hx = qw(x) / (Tw(x) - Tb(x)) [Jiang 2017, pp. 4-6]
  - 局部Reynolds数：Rex = (ρ u de) / μ = 2M / (W μb(x)) [Jiang 2017, pp. 4-6]
  - 局部Nusselt数：Nux = (hx de) / k = 2 hx d / kb(x) [Jiang 2017, pp. 4-6]
- **关联式提出**：基于物性变化（比焓比、密度比、Pr数比）修正常物性Nusselt数 [Jiang 2017, pp. 9-10]。

## Key Findings
1. **传热关联式**：提出描述超临界CO₂在岩石裂隙中层流局部传热的关联式，与实验数据的偏差在8%以内（涵盖98%数据点）[Jiang 2017, pp. 9-10]。
2. **质量流率效应**：在壁温远高于拟临界温度时，流率对传热影响不显著。但当壁温接近拟临界温度时，高流率下物性沿截面急剧变化，局部Nusselt数明显降低 [Jiang 2017, pp. 6-7]。
3. **物性影响机制**：当CO₂主流温度接近拟临界点，密度、粘度、导热系数、比热容急剧变化，导致局部传热系数增加而Nusselt数降低。径向物性差异是主导层流传热变化的原因 [Jiang 2017, pp. 7-9]。
4. **工况适用性**：在深度约2 km、储层温度接近100°C的浅层EGS与CO₂工质温度均接近拟临界点的工况中，本研究的物性影响与关联式适用性明显 [Jiang 2017, pp. 2-3]。
5. **热平衡假设影响**：文献调研指出，岩体与流体间的传热系数对EGS生产温度影响重大。常见局部热平衡（LTE）假设可能掩盖物性剧烈变化带来的非平衡效应 [Jiang 2017, pp. 2-2]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 局部传热关联式能将98%数据偏差控制在8%以内 | [Jiang 2017, pp. 9-10] | 8.1 MPa, 0.2 mm裂隙, 55-250℃岩温, 0.13-0.75 kg/h | 关联式纳入 cp 比、ρ比、Pr比，n值与温度区间有关 |
| 在T0≈200℃时局部Nusselt数在充分发展段趋于常数 | [Jiang 2017, pp. 6-7] | Flow rate from 0.13 up to 0.75 kg/h，工质远离拟临界点 | 热物性变化对传热影响小 |
| 在T0≈80℃时流体温度接近拟临界，局部Nusselt数显著下降 | [Jiang 2017, pp. 6-7] | 流量 0.75 kg/h，50 min后 | 物性剧变削弱了层流局部传热 |
| 当主流流体温度在Tb/Tp,c<1.2区间，h_x和Nux变化剧烈 | [Jiang 2017, pp. 7-9] | 8.1 MPa, 0.2 mm 裂隙 | 比热异常峰与壁面处低Pr等因素共同作用 |
| 传热系数h(x)测量不确定性 ±10.2%， Nux不确定性 ±11.4% | [Jiang 2017, pp. 4-6] | 系统校准与实验统计 | 热通量逆算，实验最大误差7% |

## Limitations
- 研究仅限于单根 0.2 mm 光滑水平裂隙，未纳入粗糙度、化学作用等复杂因素 [Jiang 2017, pp. 3-4]。
- 本实验工况局限于一组超临界压力与低流量，所得关联式尚未在更广泛的工程尺度与三维裂隙网络中获得现场验证 [Jiang 2017, pp. 1-2, 9-10]。
- 数据覆盖主要是稳态或准稳态（t=50 min），对于长期热采过程中的裂隙演化未及考虑 [Jiang 2017, pp. 6-7]。

## Assumptions / Conditions
- **实验假设**：
  - 裂隙壁面为光滑平行板，不可渗透 [Jiang 2017, pp. 3-4]。
  - CO₂处于超临界压力8.1 MPa，流动为层流 [Jiang 2017, pp. 1-2, 4-6]。
- **结果适用条件**：
  - 裂隙两侧温度物理参数按局部热平衡处理于数据处理时 [Jiang 2017, pp. 4-6]。
  - 仅适用于水平裂隙，不考虑浮力影响。
- **关联式条件**：
  - 需要已知常物性Nusselt数 Nu0，并采用给定温度区间内的拟合指数 n [Jiang 2017, pp. 9-10]。

## Key Variables / Parameters
- 几何参数：裂隙孔径 d=0.2 mm [Jiang 2017, pp. 3-4]
- 操作变量：质量流量 M [kg/s或kg/h]，初始岩石温度 T0 [℃]，流体压力 P=8.1 MPa [Jiang 2017, pp. 3-6]
- 导出变量：局部壁温 Tw(x)，局部主流温度 Tb(x)，局部热流 qw(x)，局部传热系数 hx，局部Nusselt数 Nux [Jiang 2017, pp. 4-6]
- 物性参数：比热 Cp，密度 ρ，粘度 μ，导热系数 k，Prandtl数 [Jiang 2017, pp. 7-10]
- 量纲数：Re数，Pr数，Nu数，Tb/Tp,c [Jiang 2017, pp. 7-10]
- 关联式参数：平均比热 Cp = (Hw-Hb)/(Tw-Tb)，ρw/ρb，Prw/Prb，指数 n [Jiang 2017, pp. 9-10]
- 本文贡献的核心参数：修正常物性 Nu0 的经验指数 n [Jiang 2017, pp. 9-10]

## Reusable Claims
- **Claim 1（适用工况与规则齐物性）**：对于超临界CO₂在0.2 mm光滑平行裂隙内的层流传热，当 Tb/Tp,c>1.2 时，物性随温度变化不大，局部Nusselt数近乎常数，常物性假设可用 [Jiang 2017, pp. 7-9]。
- **Claim 2（拟临界恶化效应）**：当壁温和主流温度均近或穿越拟临界点时，层流Nusselt数明显下降。原因是壁面密度大、粘度高，导致近壁速度降低，从而削弱对流传输 [Jiang 2017, pp. 7-9]。
- **Claim 3（关联式形式与适用条件）**：可采用的关联式为 Nu/Nu0 = (Cp -/Cp,b)^n (ρw/ρb)^-0.27 (Prw/Prb)^0.043。指数n根据壁温、主流温度相对拟临界点区间的不同取分段常数。该关联式适用于0.2 mm口径裂隙，8.1 MPa，对98%实验点偏差 <8% [Jiang 2017, pp. 9-10]。
- **Claim 4（对EGS模拟的应用提示）**：在局部热非平衡（LTNE）模拟中使用本关联式，有助于改善浅层EGS（深度≈2 km、储层温度~100°C）且以CO₂为工质时的传热预测精度 [Jiang 2017, pp. 2-3, 9-10]。
- **限制条件**：均为实验粒度（单裂隙、无粗糙度、无浮力），且尚未经大尺度现场验证 [Jiang 2017, pp. 1-2, 3-4]。

## Candidate Concepts
- [[supercritical CO2 heat transfer]]
- [[fracture reservoir]]
- [[enhanced geothermal system (EGS)]]
- [[pseudocritical temperature]]
- [[local thermal non-equilibrium (LTNE)]]
- [[local heat transfer coefficient]]
- [[property variation effect]]
- [[laminar convection in fracture]]
- [[Nusselt correlation for fracture flow]]

## Candidate Methods
- [[experimental heat transfer in rock fracture]]
- [[supercritical pressure convective loop]]
- [[data reduction method for local heat flux]]
- [[CFD-assisted inverse heat conduction]]
- [[uncertainty analysis for heat transfer experiment]]
- [[least-squares correlation building]]

## Connections To Other Work
- 片段中未提供本论文与其他研究的直接实验比较或联合分析，但关键词“局部热非平衡 (LTNE)”与“局部热平衡 (LTE)”模型对比可关联到如 Shaik (2011) 等学者对传热系数在EGS生产温度预测中重要性研究 [Jiang 2017, pp. 2-3]。
- 对超临界CO₂传热物性影响的处理方式可与多种超临界流体传热研究（如水、CO₂在管内湍流）对照，但本页仅限于层流裂隙内的扩展 [Jiang 2017, pp. 9-10]。
- 可连接至候选领域：[[discrete fracture network heat transfer]]、[[field-scale EGS simulation]]、[[CO2-plume geothermal]]。

## Open Questions
- 本关联式及其参数是否适用于其他裂隙孔径（如0.01-2 cm）、其他压力、粗糙裂隙或三维裂隙网络尚未验证 [Jiang 2017, pp. 1-2]。
- 未讨论长期热采中热致裂隙闭缩、矿物溶解/沉淀等对传热的反馈作用。
- 对水平裂隙，尚未评估当温差异大时浮力效应带来的流动修正。
- 在超临界CO₂背压变化时，关联式如何外推未从索引片段中确认。

## Source Coverage
- 本页11个索引片段覆盖论文摘要、引言、实验系统、数据处理、结果分析和关联式得出结论等主要部分。
- 摘要、亮点部分提供了研究目标和主要结论 [Jiang 2017, pp. 1-2, 9-10]。
- 方法部分引出装置、试件、数据还原与分析的具体流程 [Jiang 2017, pp. 3-6]。
- 结果讨论覆盖变流率、变初始温度下的换热特性，直到关联式拟合 [Jiang 2017, pp. 6-10]。
- 未涉及的内容：大多数结论主要依据t=50 min的实验数据，更长时序演化未出现；关联式在更大裂隙网络与多相流中的推广无覆盖；和其他实验/模拟的详细交叉验证在片段中也未呈现。
