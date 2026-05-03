---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2019-huang-experimental-investigation-of-seepage-and-heat-transfer-in-rough-fractures-for-enhanc"
title: "Experimental Investigation of Seepage and Heat Transfer in Rough Fractures for Enhanced Geothermal Systems."
status: "draft"
source_pdf: "data/papers/2019 - Experimental investigation of seepage and heat transfer in rough fractures for enhanced geothermal systems.pdf"
collections:
  - "part2"
  - "雷恩学派分形研究"
citation: "Huang, Yibin, et al. \"Experimental Investigation of Seepage and Heat Transfer in Rough Fractures for Enhanced Geothermal Systems.\" *Renewable Energy*, vol. 135, 2019, pp. 846-855. 10.1016/j.renene.2018.12.063. Accessed 2026."
indexed_texts: "10"
indexed_chars: "47042"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T23:08:19"
---

# Experimental Investigation of Seepage and Heat Transfer in Rough Fractures for Enhanced Geothermal Systems.

## One-line Summary
本研究通过使用基于Barton JRC标准剖面与3D打印技术制造的可重复人造岩样，实验研究了增强型地热系统（EGS）中粗糙裂隙内的渗流特性与对流换热行为，重点分析了粗糙度方向与围压的影响 [Huang 2019, pp. 1-2]。

## Research Question
如何系统性地评价裂隙表面粗糙度及其方向性对增强型地热系统中渗流和换热效率的影响？[Huang 2019, pp. 1-2]。本研究尝试解决由于岩样不可重复导致粗糙度影响规律归纳不足的问题 [Huang 2019, pp. 2-3]。

## Study Area / Data
- **试样**：基于Barton标准JRC剖面（JRC=10-12及18-20）和3D打印模板制作的圆柱形水泥砂浆人造岩样，直径为50mm。使用两种粗糙度方向组合的试样：（1）轴向为18-20而径向为10-12的试样；（2）轴向为10-12而径向为18-20的试样 [Huang 2019, pp. 2-5]。
- **工作流体**：蒸馏水 [Huang 2019, pp. 3-5]。
- **实验控制条件**：围压设置为1MPa（用于换热实验）、5MPa、10MPa、15MPa（用于渗流实验）；岩石初始温度60, 70, 80, 90°C；流量5 ml/min及20 ml/min等 [Huang 2019, pp. 4-8]。入口水温固定为22°C [Huang 2019, pp. 6-7]。

## Methods
- **实验系统**：利用自主研发的热干岩实验与模拟系统，包含注水系统、岩心夹持器、围压系统、加热系统、测温系统及数据采集系统 [Huang 2019, pp. 3-4]。
- **试样制备**：采用Barton的JRC典型剖面和3D打印技术制造模具，再浇注水泥砂浆（水泥:砂:水比例为1:1:0.4），养护28天制成可重复的人造岩样 [Huang 2019, pp. 4-5]。
- **渗流实验**：在不同围压和入口压力下测量流量，并基于立方定律反算等效水力隙宽 [Huang 2019, pp. 6-7]。
- **对流换热实验**：在围压1MPa下，使流体流过加热后的裂隙试样，记录岩样温度和进出口流体温度。通过牛顿冷却公式计算总热通量，并推导出总对流换热系数（h）的计算公式 [Huang 2019, pp. 5-7]。
- **不确定性分析**：对温度传感器精度及由此引出的温差、换热系数进行了不确定性分析 [Huang 2019, pp. 6-7]。

## Key Findings
- **粗糙度方向对渗流的影响**：垂直于渗流方向的高粗糙度会显著降低渗流能力。当JRC=18-20剖面垂直于水流方向时（试样18-20 & 10-12），其等效水力隙宽小于JRC=10-12剖面垂直于水流方向的试样（试样10-12 & 18-20），导致前者流量更小 [Huang 2019, pp. 6-8]。
- **围压对渗流的影响**：围压对裂隙隙宽有显著影响。围压越高，等效水力隙宽越小。在15MPa高围压下，入口压力的变化对增大裂隙隙宽的效果不明显 [Huang 2019, pp. 7-8]。
- **流量对换热的影响**：更高的注入流速能从热储中提取更多热量。在同等时间内，高流速下岩石温度下降幅度更大 [Huang 2019, pp. 8-9]。
- **初始温度与出口温度的关系**：出口温度与岩石初始温度几乎呈线性关系 [Huang 2019, pp. 9-10]。
- **粗糙度方向对换热的影响**：垂直于水流方向的大粗糙度会强化换热，而平行于水流方向的大粗糙度会减少有效换热面积。粗糙度方向性产生的各向异性通道是主要原因。在相同条件下，试样18-20 & 10-12的总对流换热系数大于试样10-12 & 18-20 [Huang 2019, pp. 9-10]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 垂直于水流方向的高粗糙度降低了渗流能力。 | [Huang 2019, pp. 6-8] | 围压5, 10, 15 MPa；室温渗流实验；试样为18-20 & 10-12和10-12 & 18-20。 | 原因是JRC=18-20垂直于水流方向时，形成更多大尺寸的节理通道，增加了流动阻抗。 |
| 围压增高导致等效水力隙宽减小，在15 MPa围压下，入口压力对隙宽影响不大。 | [Huang 2019, pp. 7-8] | 室温渗流实验；围压5, 10, 15 MPa；入口压力1-14 MPa和2 MPa。 | 等效水力隙宽通过立方定律反算得出。 |
| 较高的流量能从裂隙热储中提取更多热量。 | [Huang 2019, pp. 8-9] | 围压1 MPa；岩石温度70°C和90°C；流量5 ml/min和20 ml/min。 | 表现为40分钟内岩石温度下降幅度更大。 |
| 更高流量和更高温度都能增加对流换热系数，且两者与换热系数均呈近似线性正相关。 | [Huang 2019, pp. 9-10] | 围压1 MPa；岩石温度60, 70, 80, 90°C；流量约5-25 ml/min。 | 基于边界层理论解释：高温使运动粘度降低，边界层变薄，换热增强。 |
| 当JRC=18-20的粗糙度垂直于水流方向时，对流换热系数更大。 | [Huang 2019, pp. 9-10] | 围压1 MPa；岩石温度60, 70, 80, 90°C；对比试样18-20 & 10-12和10-12 & 18-20。 | 粗糙度方向形成了各向异性通道，影响流体扰动和换热面积。 |

## Limitations
- 实验仅使用了两种特定JRC值（10-12和18-20）组合和两种粗细排列方向，结论是否可以推广至其他粗糙度范围未从索引片段中确认 [Huang 2019, pp. 2-5]。
- 岩样为水泥砂浆制成，其热物性与真实花岗岩存在差异，对换热的定量影响未在片段中讨论 [Huang 2019, pp. 4-5]。
- 实验是在单一裂隙和小尺寸岩样（F50 mm×100 mm）条件下进行的，无法完全反映现场尺度裂隙网络的复杂性和传热行为。未从索引片段中确认。
- 围压最高仅施加到15 MPa，可能未覆盖深层EGS储层的真实地应力范围。未从索引片段中确认。

## Assumptions / Conditions
- **实验模型假设**：假设人造的水泥砂浆试样的裂隙特性能够代表真实的干热岩裂隙 [Huang 2019, pp. 4-5]。假设半圆柱体试样在1 MPa围压下实现了紧密接触，流体主要在粗糙裂隙中流动，而非平面滑过 [Huang 2019, pp. 5-6]。
- **计算条件**：对流换热系数的计算中，假设裂隙内的流体平均温度可以用进出口流体的平均温度代替，并以此代表试样内表面温度。假设岩样中心点温度可用进出口流体平均温度表示 [Huang 2019, pp. 6-7]。
- **数据条件**：渗流实验在室温下进行，而换热实验在高温下进行。未从索引片段中确认渗流实验中是否考虑了温度对流体物性的影响 [Huang 2019, pp. 6-7]。

## Key Variables / Parameters
- **JRC (关节粗糙度系数)**：10-12， 18-20 [Huang 2019, pp. 2-4]。
- **流速q (flow rate)**：影响渗流和热提取率的关键控制参数 [Huang 2019, pp. 4-9]。
- **等效水力隙宽b (equivalent hydraulic aperture)**：通过立方定律由压力差和流量反算得到，用于表征渗流能力 [Huang 2019, pp. 7-8]。
- **对流换热系数h (heat transfer coefficient)**：用于评价换热性能的核心指标，由牛顿冷却公式及能标测量参数推导得出 [Huang 2019, pp. 6-7]。
- **温度 (Temperature)**：包括岩石初始温度、岩壁温度 (Tw)、流体进出口温度 (Tin, Tout) ，均对系统换热性能有显著影响 [Huang 2019, pp. 6-10]。
- **围压 (confining pressure)**：影响裂隙闭合和渗流特性的关键力学条件 [Huang 2019, pp. 7-8]。

## Reusable Claims
- **Claim 1**：在粗糙单裂隙中，垂直于流体主流方向的粗糙度（JRC）增大，会导致等效水力隙宽减小，从而降低该方向的渗流能力（基于立方定律反算） [Huang 2019, pp. 6-8]。
  **条件**：此结论基于JRC=10-12和18-20两种剖面，在围压5-15 MPa的层流稳态渗流实验下得出。
  **限制**：未在更高雷诺数湍流或不同JRC组合下验证。
- **Claim 2**：对流换热系数h与流量q和岩石初始温度均呈近似线性正相关。因为高温降低运动粘度，高流速减薄边界层，两者都强化了热传递 [Huang 2019, pp. 9-10]。
  **限制**：该线性关系是基于特定温度（60-90°C）和流量（5-25 ml/min）范围的实验观察，能否外推至更大范围未从片段中确认。
- **Claim 3**：裂隙粗糙度存在方向性效应，即垂直于水流方向的大粗糙度会强化换热（更剧烈的温度变化、更大的h），而平行于水流方向的大粗糙度则会减少有效换热面积 [Huang 2019, pp. 9-10]。
  **证据**：通过对比两个表面总面积相近但JRC方向相反的试样的温度变化曲线和换热系数得出。
- **Claim 4**：在较高围压条件下（如15 MPa），仅改变入口压力对扩大裂缝隙宽的效果不明显，裂隙主要处于闭合状态 [Huang 2019, pp. 7-8]。
  **条件**：此结论适用于处于高应力状态下的深部岩体裂隙。

## Candidate Concepts
- [[Enhanced Geothermal System (EGS)]]
- [[Joint Roughness Coefficient (JRC)]]
- [[fracture aperture]]
- [[convective heat transfer coefficient]]
- [[seepage characteristics in rough fractures]]
- [[anisotropic flow channels]]
- [[hot dry rock (HDR)]]
- [[artificial rock sample reproducibility]]

## Candidate Methods
- [[3D printing for rock fracture replication]]
- [[Barton's JRC profile comparison]]
- [[cubic law for equivalent hydraulic aperture]]
- [[Newton's law of cooling for heat transfer calculation]]
- [[temperature uncertainty analysis]]
- [[cement mortar artificial specimen technique]]

## Connections To Other Work
- 本研究引述并回应了前人关于粗糙表面对微通道换热影响的普遍性结论，同时指出此前基于随机切割花岗岩试样的实验难以提供系统、可重复的规律总结。[Huang 2019, pp. 2-3]。本研究的贡献在于利用3D打印技术实现了试样的可重复性，从而能够系统性地控制粗糙度变量。
- 可主题上连接到使用类似实验方法的其他研究，特别是那些同样使用3D打印技术制备岩心或关注表面形貌对换热系数影响的工作。
- 也可连接到关于裂缝中优势渗流通道形成的研究，本研究的粗糙度方向效应为理解通道形成机制提供了新的实验视角。

## Open Questions
- 对于比JRC=18-20更粗糙或比10-12更光滑的裂隙表面，其渗流和换热规律是否仍然遵循本研究的发现？
- 在更高雷诺数湍流条件下，粗糙度方向性效应的作用是否会发生变化或减弱？
- 真实的HDR工程涉及的是复杂的裂隙网络而非单裂隙，本文的单裂隙发现如何被推广用于裂隙网络的等效参数表征？
- 实验中水泥砂浆的热物性与实际花岗岩的差异，会对换热系数的定量结果产生多大偏差？

## Source Coverage
本页面基于论文的10个索引片段生成，时间戳截至2026年。片段覆盖了摘要、引言部分、实验方法、数据处理以及大部分结果与讨论内容。关于引言中被引用的前人工作细节、实验装置中各部件的具体型号与参数信息未被完全包含。研究结论部分覆盖较为完整，但片段中似乎缺少关于该研究对工程实践具体建议或未来工作展望的充分信息。
