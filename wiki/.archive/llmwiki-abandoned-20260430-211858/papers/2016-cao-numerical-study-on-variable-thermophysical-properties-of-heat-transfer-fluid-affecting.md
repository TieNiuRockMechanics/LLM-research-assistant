---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2016-cao-numerical-study-on-variable-thermophysical-properties-of-heat-transfer-fluid-affecting"
title: "Numerical Study on Variable Thermophysical Properties of Heat Transfer Fluid Affecting EGS Heat Extraction."
status: "draft"
source_pdf: "data/papers/2016 - Numerical study on variable thermophysical properties of heat transfer fluid affecting EGS heat extraction.pdf"
collections:
citation: "Cao, Wenjiong, et al. \"Numerical Study on Variable Thermophysical Properties of Heat Transfer Fluid Affecting EGS Heat Extraction.\" *International Journal of Heat and Mass Transfer*, vol. 92, 2016, pp. 1205-1217. doi:10.1016/j.ijheatmasstransfer.2015.09.081."
indexed_texts: "11"
indexed_chars: "54142"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T20:04:04"
---

# Numerical Study on Variable Thermophysical Properties of Heat Transfer Fluid Affecting EGS Heat Extraction.

## One-line Summary
通过数值模拟，对比了在考虑热物性随温度、压力变化的条件下，水与超临界二氧化碳(SCCO₂)增强型地热系统(EGS)的长期采热性能，并分析了变物性的影响 [Cao 2016, pp. 1-1]。

## Research Question
热物性随温度和压力显著变化的传热流体如何影响EGS的采热过程，特别是水-EGS与SCCO₂-EGS在流动行为与热提取性能上的差异 [Cao 2016, pp. 1-1]。

## Study Area / Data
未从索引片段中确认具体地理研究区。模拟采用了一个假想的EGS地下域，几何尺寸为2000×6000×2000米。储层为一个500×500×500米的多孔立方体，位于地下约4000米深度。采用五点井网布局(一注四采)，注入井位于储层中心，生产井靠近储层四角，井距为282.8米 [Cao 2016, pp. 3-4]。

## Methods
- **数值模型**: 采用局部非热平衡(LTNE)模型，耦合了多孔介质中流体的质量、动量守恒方程，以及岩石基质和裂隙流体的能量守恒方程 [Cao 2016, pp. 2-3]。
- **流体物性**: 引入了真实水与SCCO₂的压力和温度依赖的热物性（密度、粘度、比热容、导热系数）[Cao 2016, pp. 1-1]。通过设置分组案例，研究了单一物性假设为常数（取最小值、中值或最大值）时对采热性能的影响 [Cao 2016, pp. 3-4]。
- **求解器**: 使用商业CFD软件FLUENT 6.3，通过用户自定义函数(UDF)定制非标准项，采用SIMPLEC算法处理压力-速度耦合 [Cao 2016, pp. 4-5]。
- **对比案例**: 设置了基础对比案例（Case 1为真实水；Case 2为真实SCCO₂），并针对SCCO₂-EGS进行了额外的参数化研究，变量包括储层渗透率、注入压力和生产井距 [Cao 2016, pp. 6-8]。

## Key Findings
- **采热性能**: 在给定注入压力下，水-EGS的寿命比SCCO₂-EGS更长，但后者的采热速率更高，导致两者在运行结束时的累计采热量大致相同 [Cao 2016, pp. 1-1]。水-EGS的采热率略高是由其更长的寿命和从围岩获得的热补偿更多导致的 [Cao 2016, pp. 6-8]。
- **自然对流**: 相对于水，SCCO₂的密度-温度依赖性强，在储层中引发更强的自然对流，使得SCCO₂-EGS的采热过程更倾向于在储层底部区域进行 [Cao 2016, pp. 1-1]。当地层渗透率更小、流体注入压力更低或储层体积更大时，SCCO₂-EGS储层中的自然对流相对更强 [Cao 2016, pp. 1-1]。
- **变物性影响灵敏度**: SCCO₂-EGS的生产性能普遍对流体热物性变化更敏感 [Cao 2016, pp. 1-1]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| SCCO₂-EGS的储层自然对流强于水-EGS，表现为沿井连线的垂直速度分量与合速度之比 (uz/|u|) 的正负峰值均大于后者 | [Cao 2016, pp. 5-6] | 模拟对比Case 1(水)与Case 2(SCCO₂)；储层渗透率K=1.0×10⁻¹⁴ m²，注入压力p_in=10 MPa，井距d_w=282.8 m | 自然对流的证据之一。 |
| 在相同条件下，SCCO₂-EGS的低温区向生产井扩展更快，表明其采热速率更高 | [Cao 2016, pp. 5-6] | 模拟对比Case 1(水)与Case 2(SCCO₂) | 通过岩石温度分布演化图对比得出。 |
| 水-EGS运行结束时（16.3年）的热提取率约为0.46，SCCO₂-EGS（12.5年）约为0.44，差别很小 | [Cao 2016, pp. 6-8] | 模拟对比Case 1(水)与Case 2(SCCO₂) | 总热提取率相近，但水-EGS因寿命更长而略高。 |
| 对SCCO₂-EGS，减小储层渗透率（1.0×10⁻¹⁴ m²到1.0×10⁻¹⁵ m²）或降低注入压力（10 MPa到5 MPa），可增强自然对流 | [Cao 2016, pp. 6-8] | 基于Case 2(SCCO₂)的参数化研究 | 通过比较uz/|u|值得到。 |
| 对SCCO₂-EGS，增大井距（282.8 m到565.7 m），使uz/|u|负峰值增大约0.23，正峰值增大约0.06 | [Cao 2016, pp. 8-11] | 基于Case 2(SCCO₂)的参数化研究 | 量化了储层体积对自然对流强度的影响。 |

## Limitations
- 模拟的EGS储层为理想化的均质多孔介质，裂缝网络被简化为连续多孔介质，未考虑真实裂隙分布的非均质性 [Cao 2016, pp. 2-3]。
- 模型假设围岩无流体损失（零孔隙度、零渗透率），未考虑实际EGS运行中可能的工作流体漏失 [Cao 2016, pp. 3-4]。
- 模拟求解时未采用湍流模型，而是通过DNS方法处理井筒中可能存在的湍流，其准确性未从索引片段中确认 [Cao 2016, pp. 4-5]。
- 热-电转换效率被假设为恒定值0.14，未考虑温度变化对该效率的影响 [Cao 2016, pp. 8-11]。

## Assumptions / Conditions
- **局部热非平衡（LTNE）假设**: 模型分别求解流体温度(Tf)和岩石温度(Ts)，两者通过体积换热系数进行热交换 [Cao 2016, pp. 2-3]。
- **多孔介质假设**: 储层被视为具有有限孔隙度和渗透率的多孔介质区域，流体流动遵循达西定律的扩展形式 [Cao 2016, pp. 2-3]。
- **有效物性近似**: 采用Bruggeman近似计算储层中岩石和流体的有效导热系数 [Cao 2016, pp. 2-3]。
- **物性依赖**: 流体密度、粘度、比热容和导热系数被视为温度和压力的函数 [Cao 2016, pp. 2-3]。
- **模型几何与边界**: 模拟域为一个包含井、储层和围岩的单一域。外部边界设置为绝热，注入井为定压入口，生产井为定压出口 [Cao 2016, pp. 4-5]。
- **围岩不渗透**: 假设围岩的孔隙度和渗透率为零，即不考虑流体损失 [Cao 2016, pp. 3-4]。

## Key Variables / Parameters
- **操作参数**: 流体注入压力 p_in，流体产出温度。
- **物理性质**: 流体密度 qf，粘度 l，比热容 cpf，导热系数 kf；岩石比热容 cps，导热系数 ks。
- **储层参数**: 孔隙度 e，渗透率 K，井距 d_w，储层体积 [Cao 2016, pp. 6-8]。
- **性能指标**: 热提取率 h (定义为已提取热量与储层初始含热量之比)，净电力输出 W_e，采热速率 [Cao 2016, pp. 8-11]。
- **流动特征**: 流体速度矢量 u，垂直速度分量与合速度之比 uz/|u|（用于表征自然对流强度） [Cao 2016, pp. 5-6]。

## Reusable Claims
- **Claim 1**: 对于超临界CO₂作为工作流体的增强型地热系统(SCCO₂-EGS)，其储层内的自然对流强度会随储层渗透率的减小而相对增强 [Cao 2016, pp. 6-8]。**适用条件**: 模拟基于理想五点井网、均质多孔介质储层的SCCO₂-EGS模型。**证据**: 当渗透率从1.0×10⁻¹⁴ m²降至1.0×10⁻¹⁵ m²时，表征自然对流强度的参数uz/|u|峰值增加 [Cao 2016, pp. 6-8]。
- **Claim 2**: 在SCCO₂-EGS中，增大注入井与生产井之间的距离，可以增强储层中的自然对流 [Cao 2016, pp. 8-11]。**适用条件**: 模拟基于理想五点井网、均质多孔介质储层的SCCO₂-EGS模型。**证据**: 井距从282.8 m增加至565.7 m，使uz/|u|的负峰值增大约0.23，正峰值增大约0.06 [Cao 2016, pp. 8-11]。
- **Claim 3**: SCCO₂-EGS的生产性能对流体热物性变化的敏感性高于水-EGS [Cao 2016, pp. 1-1]。**适用条件**: 该结论来自于对水基和SCCO₂基工作流体，将其密度、粘度、比热容和导热系数逐一假设为常数（取最小、中、最大值）的多组案例综合比较。**证据**: 通过对表1中Group 2和Group 3模拟结果的综合分析得出 [Cao 2016, pp. 1-1, 8-11]。

## Candidate Concepts
- [[Enhanced Geothermal System]]
- [[Local Thermal Non-Equilibrium]]
- [[Supercritical Carbon Dioxide]]
- [[Natural Convection in Porous Media]]
- [[Variable Thermophysical Properties]]
- [[Heat Extraction Ratio]]
- [[Quintuplet EGS Well Configuration]]

## Candidate Methods
- [[Numerical Simulation of EGS]]
- [[Computational Fluid Dynamics for EGS]]
- [[Porous Media Flow and Heat Transfer Modeling]]
- [[FLUENT User Defined Functions for EGS]]
- [[Parametric Study of EGS Performance]]
- [[Bruggeman Approximation for Effective Thermal Conductivity]]

## Connections To Other Work
- 本工作在模型上扩展了之前的研究 [Cao 2016, pp. 1-1]，并遵循了Pruess [7,8] 的工作，采用五点井网作为模型几何基础 [Cao 2016, pp. 3-4]。文中总结前人工作时指出，Pruess[7,8]预测SCCO₂-EGS因气体般的低粘度在给定泵功下具有更大的能量提取率，但其较小的体积热容意味着需要更大质量流量才能传输与水同等的热量，且Joule-Thomson效应可能导致其产出井温度降低，从而提取更少的能量 [Cao 2016, pp. 1-2]。
- 主题上可连接至其他[[EGS performance comparison]]研究，以及关于[[SCCO2 as working fluid]]的经济可行性评估，如Atrens等人[15]和Mohan等人[16]的工作 [Cao 2016, pp. 1-2]。

## Open Questions
- 真实裂缝性储层中的非均质性如何影响SCCO₂的自然对流和采热性能，未从索引片段中确认。
- 模拟中假设的无流体损失条件在多大程度上偏离实际EGS运行情况，及其对结论可靠性的影响，未从索引片段中确认。
- 除渗透率、注入压力和井距外，其他参数（如储层温度、岩石热物性）对自然对流的影响，未从索引片段中确认。
- 长周期运行中，水-岩或SCCO₂-岩化学反应对系统性能的反馈影响，被忽略，因此是开放性问题 [Cao 2016, pp. 1-2]。

## Source Coverage
本页基于该论文的11个索引片段，覆盖了摘要、引言、模型方法、案例设置、结果与讨论部分。片段主要来自文章开头和结尾部分，对核心的对比结果和参数化分析结论有较好覆盖。然而，片段可能缺失了部分中间结果的详细数据、网格无关性验证的细节、以及两组变物性研究案例（Group 2 & 3）的全面讨论。全文共12页，本次索引片段主要集中在第1-8页，后半部分的具体数据图表分析可能存在覆盖不足。
