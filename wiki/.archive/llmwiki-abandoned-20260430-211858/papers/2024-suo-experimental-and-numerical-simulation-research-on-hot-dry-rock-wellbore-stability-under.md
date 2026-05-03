---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2024-suo-experimental-and-numerical-simulation-research-on-hot-dry-rock-wellbore-stability-under"
title: "Experimental and Numerical Simulation Research on Hot Dry Rock Wellbore Stability under Different Cooling Methods."
status: "draft"
source_pdf: "data/papers/2024 - Experimental and numerical simulation research on hot dry rock wellbore stability under different cooling methods.pdf"
collections:
citation: "Suo, Yu, et al. \"Experimental and Numerical Simulation Research on Hot Dry Rock Wellbore Stability under Different Cooling Methods.\" *Geothermics*, vol. 119, 2024, article 102977."
indexed_texts: "16"
indexed_chars: "78037"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T13:58:41"
---

# Experimental and Numerical Simulation Research on Hot Dry Rock Wellbore Stability under Different Cooling Methods.

## One-line Summary

本研究通过实验与数值模拟，探究了液氮冷却、水冷却和自然冷却三种方式对高温花岗岩物理力学性质的影响，并基于热损伤模型评估了不同冷却方式下的热干岩井筒稳定性 [Suo 2024, pp. 1-2]。

## Research Question

在深层地热（3000–10000 m）开采中，钻井液或其他低温流体侵入井筒与高温岩层发生热交换，导致围岩强度下降与井筒失稳。本研究旨在回答：**不同冷却方式（液氮冷却、水冷却、自然冷却）如何影响高温花岗岩的物理力学性质，以及这些差异如何影响井筒稳定性的热-固耦合响应？** [Suo 2024, pp. 1-2]。

## Study Area / Data

实验所用岩样为花岗岩，来自未从索引片段中确认的具体产地。岩样规格为25 mm × 50 mm 的圆柱体，共75个。岩样分为五组，分别对应室温对照组（25 ℃）及四个目标加热温度（200 ℃、400 ℃、600 ℃、800 ℃），每组15个样品。加热速度为5 ℃/min，并在目标温度恒温2小时。随后采用自然冷却、水冷却和液氮冷却三种方式冷却至室温，并测量其体积、质量、渗透率、有效孔隙度、单轴抗压强度和弹性模量 [Suo 2024, pp. 3-3]。

## Methods

1. **实验研究**：  
   将花岗岩样品按温度梯度分组加热后，采用自然冷却、水冷却、液氮冷却三种方案进行冷却。测量并分析不同温度与冷却方式下岩石的物理性质（体积、质量、渗透率、有效孔隙度）和力学性质（单轴抗压强度、弹性模量）的变化规律 [Suo 2024, pp. 3-5]。

2. **热应力理论分析**：  
   引用热量冲击公式评估冷却引起的拉伸应力 (σ_t)：  
   σ_t = E α ΔT_h (1 − μ) f(h)  [Suo 2024, pp. 5-7]。  
   该式表明冷却流体与岩石的温差 (ΔT) 及流体换热系数 (h) 是控制热应力与岩石损伤的关键因素 [Suo 2024, pp. 5-7]。

3. **数值建模**：  
   - 在实验数据的基础上，修正了高温花岗岩的**破坏准则**，建立了用于评估高高温地层井筒稳定性的**热-固耦合模型** [Suo 2024, pp. 1-2]。  
   - 建立了基基于损伤力学和微元理论的高温花岗岩**热损伤模型**。引入热损伤变量 D_T 表征高温导致的损伤程度，并基于Lemaitre 应变等价假设建立岩石损伤本构 [Suo 2024, pp. 7-8]。  
   - 模型用于分析不同钻井流体温差下的井周应力分布及损伤范围 [Suo 2024, pp. 1-2]。  
   （注：具体的数值格式、网格、软件平台、耦合细节未从索引片段中确认。）

## Key Findings

1. **质量与体积变化**：  
   随着温度升高，各冷却方式下花岗岩体积膨胀、质量减少，且温度越高、冷却方式的差异越明显。800 ℃ 时，液氮冷却的体积膨胀最大（208.52 cm³），质量损失最高 [Suo 2024, pp. 3-5]。

2. **渗透率与孔隙度**：  
   渗透率和有效孔隙度均随温度升高而增大，800 ℃ 时液氮冷却的渗透率可达 4.85E-06 cm/s，有效孔隙度 16.07%，均显著高于水冷却和自然冷却 [Suo 2024, pp. 3-5]。高温导致矿物膨胀、相变和挥发物释放，增加了孔隙-裂隙连通性 [Suo 2024, pp. 5-5]。

3. **力学性质劣化**：  
   - 单轴抗压强度和弹性模量随温度升高而下降，呈“逐渐下降阶段”（25–400 ℃）和“快速下降阶段”（400–800 ℃） [Suo 2024, pp. 5-5]。  
   - 400 ℃以下冷却方式影响不大；超过400 ℃后差异显著，其中**液氮冷却劣化最严重**。800 ℃时，液氮、水冷、自然冷却的抗压强度分别降至 30.03 MPa、34.92 MPa、38.07 MPa [Suo 2024, pp. 5-5]。

4. **热损伤机制与井筒失稳**：  
   低温流体与高温岩石的巨大温差带来了强拉伸热应力。温差 ΔT 和换热系数 h 越大，岩石表面产生的拉应力越强，微裂纹产生、扩展和贯通，是力学性质劣化的主因。这一机制导致井帮围岩易发生坍塌、缩径、漏失等失稳形式 [Suo 2024, pp. 5-7]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 不同冷却方式下，花岗岩体积、质量随温度的变化（25–800 ℃）。 | [Suo 2024, pp. 3-5] | 加热速率5 ℃/min，恒温2小时，三种冷却方式。 | 液氮冷却的体积膨胀和质量损失最大。 |
| 不同冷却方式下，渗透率和有效孔隙度随温度升高而升高。 | [Suo 2024, pp. 3-5] | 同上实验条件。 | 800 ℃时液氮冷却渗透率4.85E-06 cm/s，孔隙度16.07%。 |
| 单轴抗压强度和弹性模量随温度升高而降低，400 ℃后劣化加速。 | [Suo 2024, pp. 5-7] | 室温至800 ℃，三种冷却方式。 | 液氮冷却劣化最严重，800 ℃抗压强度仅30.03 MPa。 |
| 冷却热应力公式 σ_t = E α ΔT_h (1 − μ) f(h)。 | [Suo 2024, pp. 5-7] | 理论分析，源自 Collin 和 Rowcliffe (2000)。 | 拉伸应力受温差和换热系数控制。 |
| 建立了基于 Weibull 分布的岩石热损伤模型，定义热损伤变量 D_T。 | [Suo 2024, pp. 7-8] | 结合Lemaitre 等效假设和微元强度概率分布。 | 用于描述高温引起的初始损伤。 |

## Limitations

- 索引片段未提供完整数值模型的建立参数、网格模型、边界条件和耦合求解细节。
- 井筒稳定性分析的具体工况（钻井液类型、特定深度应力场等）未见于索引片段。
- 实验为室内小尺寸岩心测试，微裂隙扩展和渗透行为与大尺度原位地层的尺度效应未讨论。
- 文中修正的破坏准则的具体表达式和参数均未从索引片段中获得。
- 实验加热上限800 ℃，更高温下（>800 ℃）或循环加热的效应未涉及。

## Assumptions / Conditions

1. 岩石可视为含天然微缺陷的微元集合体，其强度服从概率分布，以此构建热损伤模型 [Suo 2024, pp. 7-8]。
2. 热损伤变量 D_T 独立于应力引起的损伤，可叠加在岩石初始损伤状态上 [Suo 2024, pp. 7-8]。
3. 冷却过程中岩石的损伤主要由温差诱导的拉伸热应力控制 [Suo 2024, pp. 5-7]。
4. 实验中的加热过程是均匀、缓慢升温并恒温2 h，与实际钻井过程中的非均匀、瞬态热冲击可能存在差异。
5. 热-固耦合模型假设岩石为未从索引片段中确认的各向同性或特定本构关系（具体假设未完全展开于片段中）。

## Key Variables / Parameters

- **物理参数**：体积 (cm³)、质量 (g)、有效孔隙度 (%), 渗透率 (cm/s) [Suo 2024, pp. 3-5]
- **力学参数**：单轴抗压强度 (MPa)、弹性模量 (GPa) [Suo 2024, pp. 5-7]
- **冷却参数**：目标加热温度 (℃)、冷却方式 (自然/水/液氮)、温差 ΔT_h (K)、换热系数 h [Suo 2024, pp. 5-7]
- **热应力参数**：拉伸应力 σ_t (MPa)、热膨胀系数 α、泊松比 μ [Suo 2024, pp. 5-7]
- **损伤参数**：热损伤变量 D_T、微元破坏数 n_T [Suo 2024, pp. 7-8]
- **数值模型**：失效准则（修订版）、热-固耦合模型 [Suo 2024, pp. 1-2]

## Reusable Claims

1. **冷却方式对花岗岩力学性质影响的温限效应**：加热峰值温度≤400 ℃时，不同冷却方式对花岗岩压缩强度和弹性模量的影响差异不明显；当峰值温度≥600 ℃后，液氮冷却引起的力学性能劣化显著大于水冷和自然冷却 [Suo 2024, pp. 5-7]。
2. **热冲击劣化由温差和换热系数主导**：计算低温流体侵入引起围岩拉应力的公式 σ_t = E α ΔT_h (1 − μ) f(h) 表明，劣化程度主要取决于岩石与流体间的温差 ΔT_h 及流体的换热系数 h，这为评估不同冷却流体危险性提供了定量依据 [Suo 2024, pp. 5-7]。
3. **高下高温损伤模型框架**：基于 Lemaitre 应变等价理论和微元强度破坏概率的热损伤变量 (D_T) 可表征高温所引起的岩石预损伤，为构建考虑温度历程的井筒稳定性本构模型提供了可直接迁移的损伤力学框架 [Suo 2024, pp. 7-8]。
4. **渗透率和孔隙度的温控增长**：高温加热导致微裂隙扩展和挥发物逸出，使岩石渗透率和有效孔隙度随温度单调递增，尤其在≥600 ℃后增长加剧，且液氮冷却引起的增幅最大。该组数据可支撑热储改造或漏失预测 [Suo 2024, pp. 3-5]。

## Candidate Concepts

- [[Hot dry rock]]
- [[wellbore stability]]
- [[thermal damage model]]
- [[thermal-hydraulic-mechanical (THM) coupling]]
- [[failure criterion revision for granite]]
- [[granite physical-mechanical property degradation]]
- [[thermal shock cracking]]
- [[Liquid nitrogen cooling in geothermal drilling]]
- [[high-temperature rock mechanics]]

## Candidate Methods

- [[Thermal damage variable modeling based on Lemaitre equivalent strain]]  [Suo 2024, pp. 7-8]
- [[Uniaxial compression test under controlled heating and cooling]]
- [[Thermal stress calculation using thermoelastic cooling shock equation]]  [Suo 2024, pp. 5-7]
- [[Experimental-numerical combined wellbore stability analysis]]

## Connections To Other Work

索引片段中明确提及的部分研究包括：
- **Kang 等 (2021)**：也探讨了不同冷却方法对高温花岗岩的影响，同样发现温度较低时影响差异小，600 ℃以上差异显著，其中液氮冷却变化最大 [Suo 2024, pp. 2-2]。
- **Zhang 等 (2021)**：报道水循环冷却导致岩石单轴抗压强度和弹性模量随温度和周次增加而降低 [Suo 2024, pp. 2-2]。
- **Wang 和 Zhou (2019)**：通过数值模拟揭示了钻井加热过程对井壁热损伤的机理 [Suo 2024, pp. 2-3]。
- **Lin 等 (2023)**：建立了热-力损伤 (TMD) 模型，并报道液氮接触煤样时，表面温度急剧下降，内部温度缓慢降低 [Suo 2024, pp. 2-3]。

本文可从**主题上**连接到以下概念与方法：
- 深层地热井筒稳定性的其他冷却/加热数值模型，例如 [[Tao and Ghassemi 2010]] 的热弹性效应对井筒破坏的影响，以及 [[Gao et al. 2017]] 的局部热非平衡横向各向同性热弹效应。
- 岩石热致开裂或热损伤本构的通用建模方法，例如 [[Huang et al. 2022]] 的孔洞岩石热-力耦合塌陷模型。

## Open Questions

- 液氮冷却在其实井筒循环环境下（有压力、非完全均匀接触）的热应力瞬态分布及损伤演化如何？未从索引片段中确认。
- 井筒稳定性热-固耦合模型是否考虑了流体渗流与热对流的全面耦合（即 THM 全耦合），以及对应模型的具体验证案例未给出。
- 修正的破坏准则的形式、参数及其实验/原位验证没有在本索引片段中展开。
- 多次或多循环冷冲击条件下的累积损伤规律未涉及。
- 实验结果向实际深部原位井筒尺寸与应力环境的定量放大方法未谈及。

## Source Coverage

本页内容基于来自《Geothermics》119卷2024年论文的 **16个索引片段**，覆盖了摘要、引言的一部分、实验样品与流程、物理性质、力学性质、热应力理论与热损伤模型推导。数值模拟部分具体细节（网格、破坏准则公式形式、模型参数和模拟工况）、完整讨论、结论和展望的关键信息**目前在索引片段中缺失**。因此，对于“破坏准则修订”和“井筒稳定性耦合行为评估”的具体数值结果与工程含义，只能依据片段中的概要性描述，详细解释需查阅论文全文。
