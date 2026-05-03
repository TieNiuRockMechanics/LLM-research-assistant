---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2019-walsh-simulating-electropulse-fracture-of-granitic-rock"
title: "Simulating Electropulse Fracture of Granitic Rock."
status: "draft"
source_pdf: "data/papers/2020 - Simulating electropulse fracture of granitic rock.pdf"
collections:
  - "part3-2"
citation: "Walsh, Stuart D.C., and Daniel Vogler. \"Simulating Electropulse Fracture of Granitic Rock.\" *International Journal of Rock Mechanics and Mining Sciences*, preprint, 18 Nov. 2019, eartharxiv.org. Accessed 2026."
indexed_texts: "9"
indexed_chars: "44037"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T01:28:50"
---

# Simulating Electropulse Fracture of Granitic Rock.

## One-line Summary

本文提出一种新的数值建模方法，用于模拟花岗岩等硬质岩石在电脉冲处理下的多物理场断裂过程 [Walsh 2019, pp. 1-3]。

## Research Question

如何精确模拟电脉冲处理中岩石的电-机械耦合行为，特别是放电、电击穿以及后续引起的机械损伤过程，以改善工具设计与控制 [Walsh 2019, pp. 1-3]？

## Study Area / Data

本研究基于数值模拟，未包含实地或实验数据采集。模拟材料采用典型花岗岩，其矿物组成与粒度分布参照 Lac du Bonnet 花岗岩设定 [Walsh 2019, pp. 11-14]。模拟实验设置中，对一块厚度 2 cm、宽度 10 cm 的样本两侧施加单次脉冲 [Walsh 2019, pp. 14-15]。

## Methods

模拟工作分为两个阶段，耦合了电-热-机械多物理场 [Walsh 2019, pp. 8-11, 15-19]：

1.  **电击穿与电流模拟**：模拟电流的传导过程及反馈机制。电阻热耗散导致温度升高，导电率随之变化，遵循经验关系 \(\Lambda = A \exp(-B/k_b\theta)\) [Walsh 2019, pp. 6-8]。为捕捉矿物与微孔隙的导电差异，岩石被建模为“双导电率”材料 [Walsh 2019, pp. 8-11]。电击穿过程采用热击穿模型进行模拟，其中电流的汇聚及其引起的加热最终导致介电性能丧失 [Walsh 2019, pp. 8-11]。
2.  **热机械响应模拟**：计算热传导及热膨胀引起的应力变化。基于多种失效模式准则预测损伤区域，包括剪切破坏、超过单轴抗压强度、超过抗拉强度以及由于长期强度超限导致的压缩或拉伸破坏 [Walsh 2019, pp. 11-14]。岩石的微观结构通过 Voronoi 镶嵌方法生成，以模拟多晶粒组织 [Walsh 2019, pp. 11-14]。
3.  **模型参数**：材料失效准则和 Hoek-Brown 相关参数设为：`s=1`, `a=0.5`, 单轴抗压强度 `σ_c = 122 MPa`, `m = 25`, 抗拉强度 `σ_t = 10 MPa`，剥落极限 `(σ1/σ3)_i` 设为 8 [Walsh 2019, pp. 11-14]。

## Key Findings

- 在给定模拟条件下，单个脉冲即可在岩石内部生成局部导电通道 [Walsh 2019, pp. 14-15]。
- 在初始击穿阶段，放电行为主要受微孔隙度分布控制，这是因为孔隙流体的温度与电导率在反馈作用下迅速增加 [Walsh 2019, pp. 15-19]。
- 局部加热导致的热应力引起了电极附近的张拉破坏和剥落破坏，该区域温度升高超过 200 K [Walsh 2019, pp. 14-15]。
- 模拟结果成功重现了与实验观察相似的岩石起始破裂条件 [Walsh 2019, pp. 15-19]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 电脉冲技术能耗为 100 到 200 J/m³，相比之下传统旋转钻孔能耗为 600 到 950 J/m³ | [Walsh 2019, pp. 3-6] | 基于岩石受拉破坏 | 未从索引片段中确认对比的具体岩石种类 |
| 矿物导电率模型参数：石英 log(A)=6.3 [log(S/m)], B=0.82 [eV] | [Walsh 2019, pp. 6-8] Table 1 | 模拟采用的经验函数，源引自 [25] | 其他矿物参数见原文 Table 1 |
| 矿物微孔隙度：石英 0.9%，斜长石 1.8%，钾长石 0.9%，黑云母 0.9% | [Walsh 2019, pp. 8-11] Table 2 | 数据来自文献 [34] | 孔隙度影响流体相电导率和初始击穿路径 |
| 模拟中，厚度 2cm 的样本在单次脉冲下形成局部通道 | [Walsh 2019, pp. 14-15] | 施加恒定电压降的脉冲 | 源自模拟结果描述 |
| 电极附近区域温度升高超过 200 K | [Walsh 2019, pp. 14-15] | 上一条所述模拟条件 | 源于图 5c 的描述 |
| 模型结果与实验研究对比，显示其能预测岩石的起始破裂 | [Walsh 2019, pp. 15-19] | 未从索引片段中确认用于对比的特定实验 | 结论陈述 |

## Limitations

- 本文档为预印本，截至 2019年11月，仍在同行评审中，其内容可能终版有调整 [Walsh 2019, pp. 1-3]。
- 模型假设所有电阻耗散的能量都转化为热能，忽略了转化为声、光等形式的能量 [Walsh 2019, pp. 6-8]。
- 对于电击穿现象，模型采用热击穿假设，可能无法完全捕捉其他原子尺度或纯电极理论描述的机制 [Walsh 2019, pp. 8-11]。
- 研究仅考虑单脉冲放电的影响，未从索引片段中确认对于多次脉冲、连续放电等更贴近实际工况的模拟评估。
- 模拟基于特定的花岗岩成分和微观结构，其他岩石类型的适用性未验证。
- 模拟假设了设备提供恒定电压降，未包含实际设备详细的电路响应模型 [Walsh 2019, pp. 14-15]。

## Assumptions / Conditions

- 所有的电阻能量耗散（\(q_D\)）完全转化为热能，用于提升岩石温度 [Walsh 2019, pp. 6-8]。
- 采用热击穿作为主要的电介质击穿机制，假设其足以确定击穿路径 [Walsh 2019, pp. 8-11]。
- 岩石孔隙流体的有效盐度假定为 3 wt% 的 NaCl 溶液 [Walsh 2019, pp. 8-11]。
- 材料微观结构与矿物组成基于 Lac du Bonnet 花岗岩的统计数据生成 [Walsh 2019, pp. 11-14]。
- 岩石的机械破坏满足基于 Hoek-Brown 等经验法则的多种失效准则 [Walsh 2019, pp. 11-14]。
- 在模拟电脉冲时，施加在两个电极之间的是恒定电压降，脉冲的具体持续时间、电压幅值等细节未从索引片段中确认 [Walsh 2019, pp. 14-15]。

## Key Variables / Parameters

- **电热变量**：电阻耗散能量 \(q_D\)， 温度增量 \(\Delta\theta\)， 材料导电率 \(\Lambda\) [Walsh 2019, pp. 6-8]。
- **导电率模型参数**：经验常数 `A` 和 `B`，Boltzmann 常数 `kb`， 温度 `θ` [Walsh 2019, pp. 6-8]。具体岩石及矿物的`A`、`B`值见原文 Table 1。
- **材料属性**：各矿物的微孔隙度（见 Core Evidence Table） [Walsh 2019, pp. 8-11]。
- **力学参数**：Hoek-Brown 参数 `s`=1, `a`=0.5；单轴抗压强度 `σ_c`=122 MPa；材料常数 `m`=25；抗拉强度 `σ_t`=10 MPa；剥落极限 `(σ1/σ3)_i`=8 [Walsh 2019, pp. 11-14]。
- **微观结构变量**：花岗岩各矿物相的体积百分比和粒径大小（如钾长石 45%，3.7mm） [Walsh 2019, pp. 11-14]。
- **几何参数**：样本厚度 2 cm，宽度 10 cm [Walsh 2019, pp. 14]。

## Reusable Claims

- **Claim 1**: 在电脉冲初始放电阶段，具有高微孔隙度的区域将主导导电通道的形成。机制在于孔隙流体的导电率随温度上升而增加的反馈环路比致密矿物颗粒更快启动。条件：岩石为含有导电孔隙流体的低初始电导率脆性材料。限制：结论基于花岗岩的“双导电率”数值模拟，且孔隙流体盐度假定为3 wt%，对于干燥或高盐度孔隙流体的岩石可能不同。[Walsh 2019, pp. 15-19]。
- **Claim 2**: 在高电压放电下，岩石的破碎可以由电极附近区域的热应力所引发的张拉破坏和剥落破坏共同导致。条件：脉冲能量足以产生超过200K的局部温升，且岩石的失效符合 Hoek-Brown 准则及其设定的参数。限制：该破坏模式主要在电极附近被观察到，对于远场区域的影响和裂纹扩展过程未从索引片段中确认。[Walsh 2019, pp. 14-19]。
- **Claim 3**: 电脉冲处理后岩石的电导率与温度关系可采用经验模型 \(\Lambda = A \exp(-B/k_b\theta)\) 进行描述。条件：适用于固态矿物，且参数 A和B 可通过查表获得。限制：该模型在超过200°C的高温下（尤其对于流体）可能需要采用 Arps 定律等其他模型替代，如文中所结合的多种经验模型。[Walsh 2019, pp. 6-8]。

## Candidate Concepts

- [[Electropulse Fracture]]
- [[Dielectric Breakdown Model]]
- [[Thermo-Electro-Mechanical Coupling]]
- [[Granitic Rock Microstructure]]
- [[Grain-scale Multiphysics Simulation]]
- [[Microporosity Influence]]
- [[Voronoi Tessellation]]
- [[Electrical Resistive Heating]]

## Candidate Methods

- [[Multiphysics Numerical Simulation]]
- [[Hoek-Brown Failure Criterion]]
- [[Dual-Conductivity Modelling]]
- [[Empirical Conductivity-Temperature Model]]
- [[Finite Element Thermo-Mechanical Analysis]]

## Connections To Other Work

- 本模型的理论背景可连接至早期电脉冲破岩的实验机制研究，例如 Budenstein [12] 提出的固体介质击穿气态通道理论，以及 Lisitsyn 等 [9] 描述的蒸汽-气体空腔膨胀和压力波模型 [Walsh 2019, pp. 3-6]。
- 该建模框架与用于模拟雷击对复合材料影响的模型相似，如文献 [40, 41]，同样采用热击穿假设来跟踪电流和材料的响应 [Walsh 2019, pp. 8-11]。
- 在电脉冲破岩的数值模型领域内，可与 Zuo 等人 [20] 建立的宏观高压脉冲击穿矿石模型在方法论上进行区别与比较，本模型侧重于微观多矿物尺度 [Walsh 2019, pp. 3-6]。

## Open Questions

- 电介质击穿的确切物理机制（纯电击穿、热击穿或两者混合）尚存争议，本模型采用的热击穿假设是否为最精确的描述仍未解决 [Walsh 2019, pp. 8-11]。
- 模型能否准确预测多脉冲、脉冲序列能量累积效应下的岩石损伤发展，未从索引片段中确认。
- 该方法在花岗岩之外的其他硬岩（如玄武岩、片麻岩）或含有不同填充物的岩石中的普适性尚未探索。
- 基于模拟结果进行电极头几何形状、脉冲电压与频率等操作参数的系统性优化设计与工具性能预测，未从索引片段中确认。

## Source Coverage

本 Markdown 页面基于所提供的 9 个索引片段创建，片段页码范围包括 [Walsh 2019, pp. 1-3, 3-6, 6-8, 8-11, 11-14, 14-15, 15-19, 19-22]，其中 pp. 19-22 仅含参考文献信息。覆盖范围包括了摘要、引言背景、模型方法的核心方程与假设、材料设置、单脉冲模拟结果的描述以及最终结论。重要的信息缺失包括：详细的数值实现流程（如时间步进、网格独立性）、完整的定量验证过程与图表分析、所有参考文献的完整讨论，以及后续可能更新的内容。
