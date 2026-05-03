---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2018-chen-effect-of-surface-heat-transfer-coefficient-gradient-on-thermal-shock-failure-of-ceram"
title: "Effect of Surface Heat Transfer Coefficient Gradient on Thermal Shock Failure of Ceramic Materials under Rapid Cooling Condition."
status: "draft"
source_pdf: "data/papers/2018 - Effect of surface heat transfer coefficient gradient on thermal shock failure of ceramic materials under rapid cooling condition.pdf"
collections:
  - "zotero new"
  - "论文"
citation: "Chen, Limin, et al. \"Effect of Surface Heat Transfer Coefficient Gradient on Thermal Shock Failure of Ceramic Materials under Rapid Cooling Condition.\" *Ceramics International*, 2018, doi:10.1016/j.ceramint.2018.02.100."
indexed_texts: "9"
indexed_chars: "40291"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T21:45:54"
---

# Effect of Surface Heat Transfer Coefficient Gradient on Thermal Shock Failure of Ceramic Materials under Rapid Cooling Condition.

## One-line Summary
通过表面传热系数（h）梯度的系统实验与数值模拟，证实 ZrB₂–SiC–石墨（ZSG）复合陶瓷在快速冷却下的热冲击失效由体温度梯度与表面 h 梯度共同决定，不同冷却介质通过改变表面 h 梯度显著影响临界冷却速率。

## Research Question
表面传热系数梯度如何在快速冷却条件下影响陶瓷材料的热冲击失效行为及其临界条件？[Chen 2018, pp. 1-1]

## Study Area / Data
研究对象为热压制备的 ZrB₂ + 20 vol% SiC + 15 vol% 石墨（ZSG）复合陶瓷 [Chen 2018, pp. 2-3]。实验数据包括：不同冷却介质（水、沸水、聚合物水溶液）和冷却模式（RTP 间接接触、淬火直接接触）下的实时温度变化、残余强度、临界体温度梯度 V(max)c 以及表面形貌、相组成变化。[Chen 2018, pp. 1-1, 1-2, 3-4, 4-5, 5-6]

## Methods
- 冷却方式：快速热处理设备（RTP，红外辐射加热，无表面 h 梯度）和传统淬火（试样加热后浸入冷却液）[Chen 2018, pp. 2-3]。
- 冷却介质：20°C 水、100°C 沸水以及先前研究中的聚合物水溶液 [Chen 2018, pp. 1-1, 4-5]。
- 温度测量：实时热电偶采集，记录瞬时冷却速率 V(max)（引起峰值瞬态热应力的瞬时冷却速率）[Chen 2018, pp. 1-2]。
- 力学表征：残余弯曲强度测试，结合微观结构观察（SEM）和 XRD 分析 [Chen 2018, pp. 3-4]。
- 数值模拟：使用 ANSYS 16.0 进行三维瞬态有限元分析，估算温度场和热应力分布 [Chen 2018, pp. 5-6]。

## Key Findings
- **冷却模式的影响**：水为冷却介质时，RTP 间接冷却不引入表面 h 梯度，复合材料强度基本保留；直接淬火引入大的表面 h 梯度，强度严重下降 [Chen 2018, pp. 3-4]。
- **临界体温度梯度的差异**：在水淬条件下，随机相变产生气泡导致大的表面 h 梯度，临界体温度梯度 V(max)c 约为 270 °C s⁻¹；聚合物淬火中聚合物膜降低随机气泡形成，V(max)c 升至约 500 °C s⁻¹；沸水淬火因湍流传热消除 h 梯度，V(max)c > 600 °C s⁻¹（强度无明显下降）[Chen 2018, pp. 4-5, 5-6]。
- **失效机制**：热冲击失效是体温度梯度（由瞬时冷却速率 V 产生）与表面温度梯度（由表面 h 梯度产生）共同作用的结果，表面微裂纹是主要损伤形式 [Chen 2018, pp. 3-4, 6-8]。
- **数值模拟支持**：有限元分析显示两种温度梯度及其相应热应力的存在，验证了实验结论 [Chen 2018, pp. 5-6]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| RTP 间接冷却后强度无衰减，无表面裂纹；直接水淬后强度急剧下降且出现表面微裂纹 | [Chen 2018, pp. 3-4] | 加热温度最高 1200 °C（ΔT=1000 °C），RTP 为辐射加热无直接接触；水淬为浸入 20°C 水 | RTP 不引入表面 h 梯度，淬火引入较大 h 梯度 |
| 水淬条件下，改变加热温度与水体积得到的 V(max)c 约为 270 °C s⁻¹，残余强度离散度在 ΔT≈330 °C 时达最大 | [Chen 2018, pp. 4-5] | 水为 20 °C，试样预热 400 °C 时改变水量；温度差方法时 ΔT=330 °C | 符合 Hasselman 模型，离散性归因于表面微裂纹主导失效 |
| 聚合物水溶液淬冷的 V(max)c 约为 500 °C s⁻¹（先前研究） | [Chen 2018, pp. 4-5] | 材料为相同 ZSG 复合物，淬火条件见于文献 [27] | 聚合物膜提供更均匀的传热，降低表面 h 梯度 |
| 沸水淬冷（100 °C）下 V(max) 约 600 °C s⁻¹ 时残余强度未见明显下降 | [Chen 2018, pp. 4-5] | 试样浸入 100 °C 沸水，无蒸汽膜形成 | 湍流条件下无表面 h 梯度，故 V(max)c > 600 °C s⁻¹ |
| 有限元热‑应力分析显示同时存在由 V 引起的体温度梯度和由 h 梯度引起的表面温度梯度 | [Chen 2018, pp. 5-6] | ANSYS 16.0 三维瞬态模拟，对应不同淬火条件 | 数值模拟定性支持实验现象 |

## Limitations
- 实验未完全复现真实服役条件，结果仅供理解热冲击行为的补充信息 [Chen 2018, pp. 1-2]。
- 仅以一种 ZrB₂ 基复合陶瓷（ZSG）为对象，未从索引片段中确认其可否推广至其他陶瓷体系。
- 数值模拟的具体参数与验证细节未在片段中提供。
- 临界温度梯度 V(max)c 的测定在改变水量实验中存在一定不准确性，但误差在可接受范围 [Chen 2018, pp. 4-5]。

## Assumptions / Conditions
- 实验基于热压 ZSG 复合材料的特定组成（ZrB₂ + 20 vol% SiC + 15 vol% 石墨），其制备参数与微观结构已在先前工作中描述 [Chen 2018, pp. 2-3]。
- 热冲击失效遵循 Hasselman 脆性陶瓷热冲击模型，峰值热应力由瞬时冷却速率 V(max) 决定 [Chen 2018, pp. 1-2, 3-4]。
- 表面 h 梯度的产生源于冷却介质相变或流态不均匀；RTP 冷却视为无 h 梯度，沸水淬冷因全浴沸腾也无 h 梯度 [Chen 2018, pp. 3-4, 5-6]。
- 实时温度数据通过热电偶与数据采集系统获得，并假定重复测试可消除随机误差 [Chen 2018, pp. 2-3]。

## Key Variables / Parameters
- **V(max)**：瞬时冷却速率峰值，对应于峰值瞬态热应力，用于评价热冲击抗力（TSR）[Chen 2018, pp. 1-2]。
- **V(max)c**：临界体温度梯度，即导致热冲击失效的临界 V(max) 值 [Chen 2018, pp. 1-1, 4-5]。
- **表面传热系数梯度（h 梯度）**：表征冷却介质在试样表面传热的不均匀性 [Chen 2018, pp. 1-1]。
- **加热温度 ΔT**（淬火温差）：在传统水淬中作为改变热冲击严重度的唯一变量 [Chen 2018, pp. 4-5]。
- **淬火水量**：在恒温 400 °C 下改变水量以调节冷却效应 [Chen 2018, pp. 4-5]。
- **残余弯曲强度**：热冲击后保留的强度，反映损伤程度 [Chen 2018, pp. 3-4]。

## Reusable Claims
- **表面 h 梯度对热冲击失效有决定性作用**：对 ZrB₂‑SiC‑石墨复合陶瓷，冷却介质引入的表面 h 梯度越大，临界体温度梯度 V(max)c 越低，材料越容易发生热冲击破坏。该结论在对比 RTP、水淬、聚合物淬火和沸水淬火条件下得到证实 [Chen 2018, pp. 1-1, 3-4, 4-5, 5-6]。
- **体温度梯度与表面温度梯度的组合效应**：热冲击失效并非仅由体温度梯度（整体冷却速率）引起，而是体温度梯度和表面温度梯度（由 h 梯度引起）的共同结果。数值模拟确认了两种温度梯度场的存在 [Chen 2018, pp. 6-8]。
- **冷却介质的相变行为决定表面 h 梯度的大小**：水淬时随机气泡导致高 h 梯度；聚合物淬火中高分子链形成的界面膜使传热更均匀，减小 h 梯度；沸水淬火因全浴沸腾而消除汽‑液界面，几乎无 h 梯度 [Chen 2018, pp. 5-6]。该关系有助于根据不同服役环境（类似晴朗天气、雨雪/盐雾等）选择或评价材料 [Chen 2018, pp. 6-8]。
- **V(max)c 可作为定量比较冷却介质苛刻度的指标**：对于同一材料，V(max)c 随表面 h 梯度减小而增大：水淬约 270 °C s⁻¹，聚合物淬火约 500 °C s⁻¹，沸水淬火 >600 °C s⁻¹。该指标可用于其它类似热压陶瓷体系的比较，但前提是材料损伤机制以表面微裂纹为主 [Chen 2018, pp. 4-5, 5-6]。

## Candidate Concepts
- [[Thermal Shock]]
- [[Surface Heat Transfer Coefficient Gradient]]
- [[Body Temperature Gradient]]
- [[Critical Instantaneous Cooling Rate]]
- [[Ultra-High Temperature Ceramics (UHTCs)]]
- [[Surface Microcrack-Dominated Failure]]
- [[Film Boiling vs. Nucleate Boiling]]
- [[Hasselman Thermal Shock Theory]]
- [[Aqueous Polymer Quenching]]
- [[Rapid Thermal Processor (RTP)]]

## Candidate Methods
- [[Direct Contact Quenching]]
- [[Indirect Contact Cooling via RTP]]
- [[ANSYS Finite Element Analysis for Thermal Stress]]
- [[Real-time Temperature Acquisition with Thermocouples]]
- [[XRD Analysis of Post-Shock Ceramics]]
- [[SEM Surface Morphology Characterization]]
- [[Quenching Severity Adjustment by Water Volume]]

## Connections To Other Work
- 本文直接延续团队先前工作 [27]，先前研究采用聚合物淬火剂评价 ZSG 复合材料，首次提出热冲击失效与体温度梯度及表面 h 梯度均相关 [Chen 2018, pp. 1-2, 4-5]。本工作进一步系统验证了该假设。
- 实验结果遵循 Hasselman [30] 关于脆性陶瓷热冲击的模型，即当淬火严重度超过临界值时强度急剧下降 [Chen 2018, pp. 3-4]。
- 水淬条件下残余强度的离散性与文献 [5, 24, 26] 中表面微裂纹主导的热冲击失效模式一致 [Chen 2018, pp. 3-4]。
- 沸水淬火中无表面 h 梯度的解释参考了湍流传热研究 [23]，聚合物淬火中的均匀传热膜机制参考了 [34] [Chen 2018, pp. 5-6]。
- 材料制备与基础参数引用 Wang et al. [10] 等 [Chen 2018, pp. 2-3, 8]。

## Open Questions
- 未从索引片段中确认。
- 可合理推测但未在片段中正面给出的问题：该组合梯度失效机制在其他陶瓷体系（如 Al₂O₃基、Si₃N₄基）中是否普遍适用？真实服役条件下（如反复热冲击、氧化环境叠加）表面 h 梯度的演化规律如何？定量预测模型能否仅基于 V(max) 和 h 梯度实现？

## Source Coverage
本页依据共 9 个索引片段，覆盖了摘要、引言、实验方法、部分结果（RTP/水淬对比、不同淬火介质的 V(max)c 值）、显微结构观察与讨论、实际工况类比，以及完整结论。片段以结果‑讨论‑结论为主，对实验细节（如材料制备参数、RTP 温控精度）和数值模拟的具体建模条件未作详尽展开，因此可能缺失一部分边界条件与误差分析信息。索引片段未包含完整的参考文献列表，但给出了主要参考编号。总体而言，索引覆盖已足以支撑本页的主要证据链。
