---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-ren-a-comprehensive-review-of-tracer-tests-in-enhanced-geothermal-systems"
title: "A Comprehensive Review of Tracer Tests in Enhanced Geothermal Systems."
status: "draft"
source_pdf: "data/papers/2023 - A comprehensive review of tracer tests in enhanced geothermal systems.pdf"
collections:
citation: "Ren, Yaqian, et al. \"A Comprehensive Review of Tracer Tests in Enhanced Geothermal Systems.\" *Renewable and Sustainable Energy Reviews*, vol. 182, 2023, 113393."
indexed_texts: "51"
indexed_chars: "250948"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T11:44:21"
---

# A Comprehensive Review of Tracer Tests in Enhanced Geothermal Systems.

## One-line Summary
本篇综述系统回顾了增强型地热系统（EGS）中的示踪剂测试技术，基于14个EGS场地的134次测试，总结了利用示踪剂表征储层、预测热突破的方法、示踪剂类型及测试设计准则 [Ren 2023, pp. 1-1]。

## Research Question
如何系统地运用示踪剂测试来表征增强型地热系统（EGS）的储层特性（如井间连通性、储层体积、换热表面积）并预测其热突破（thermal drawdown）？ [Ren 2023, pp. 1-1]

## Study Area / Data
本综述的数据基础是来自全球14个增强型地热系统（EGS）场地的134次示踪剂测试结果 [Ren 2023, pp. 1-1][Ren 2023, pp. 6-7]。涉及的具体场地名称（除文中明确提及的Fenton Hill, Hijiori, Rosemanowes, Soultz-sous-Forêts, Habanero, Ogachi外）未从索引片段中完全确认。

## Methods
本研究采用文献综述法，回顾并分析了EGS示踪剂测试的解释方法、示踪剂材料特性、测试设计技术及示踪剂响应 [Ren 2023, pp. 3-3]。具体的解释模型和方法包括：
- 通过示踪剂质量回收率评估[[interwell connectivity]] [Ren 2023, pp. 3-4]。
- 利用基于停留时间分布（RTD）的多种方法估算[[reservoir volume]]，如`模态体积`(modal volume)、`积分平均体积`(integral mean volume)和`示踪剂扫掠孔隙体积`(pore volume swept by a tracer) [Ren 2023, pp. 4-5]。
- 评估[[heat transfer surface area]]的三种方法：1) 基于Fenton Hill场地经验关系的模态体积法；2) 利用不同扩散系数的惰性示踪剂法；3) 同时注入吸附示踪剂和惰性示踪剂的“延迟因子”法 [Ren 2023, pp. 5-5]。
- 解释BTC数据的数学模型，如基于“双重孔隙”系统的半解析反应性溶质运移拉普拉斯变换反演代码（RELAP）模型 [Ren 2023, pp. 5-5]。

## Key Findings
1.  **热突破预测的改进**：与仅使用惰性示踪剂相比，加入新型示踪剂（如吸附示踪剂、温度响应示踪剂）能更可靠地预测热突破。这一观点由来已久，近期通过高质量现场测试数据和解释模型的发展得到了验证 [Ren 2023, pp. 1-1][Ren 2023, pp. 1-2]。
2.  **示踪剂选择的关键因素**：选择示踪剂时，必须考虑测试目标、储层条件（如pH、温度、岩石类型）以及示踪剂的物理化学性质（如热稳定性、检测限） [Ren 2023, pp. 1-1][Ren 2023, pp. 1-2]。
3.  **设计良好的测试至关重要**：一个经过精心设计，综合考虑了示踪剂注入质量、水力流态和样品采集策略的测试，是获取高质量数据和准确确定储层特征的保证 [Ren 2023, pp. 1-1]。
4.  **模态体积的应用与局限**：Fenton Hill的多次示踪剂测试表明，模态体积与储层热交换能力的估算值相关，并对长期产出流体的热突破有显著影响。然而，基于Fenton Hill经验关系的模态体积-换热表面积关联方法，尚无证据表明可应用于其他地热田 [Ren 2023, pp. 4-5][Ren 2023, pp. 5-6]。
5.  **示踪剂分类**：基于物理化学性质，示踪剂可分为惰性（inert）和新型（novel）两大类。新型示踪剂包括吸附、温度响应、气体和纳米颗粒示踪剂。在汇总的41种注入材料中，惰性示踪剂使用次数最多（167次） [Ren 2023, pp. 6-7]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 新型示踪剂的加入能更可靠地预测热突破。 | [Ren 2023, pp. 1-1] | 近期高质量现场测试与模型发展。 | 该想法提出多年，新近得到验证。 |
| 示踪剂测试可估算井间连通性、裂缝体积、换热表面积和热突破。 | [Ren 2023, pp. 3-4] | EGS场地。 | 此为示踪剂测试的常见目标参数。 |
| 质量回收率可用于评估[[interwell connectivity]]。连通性越好，回收率越高。质量回收率通过对响应曲线（BTC）进行归一化为停留时间分布（RTD）后计算。 | [Ren 2023, pp. 3-4] | 稳态条件假设和惰性溶质示踪行为。 | 水力条件的波动会影响参数精度。 |
| 注入吸附和惰性示踪剂可通过“延迟因子”估算[[heat transfer surface area]]。 | [Ren 2023, pp. 5-5] | 吸附示踪剂的延迟由速率限制的吸附引起，并与换热表面积成正比。 | 该方法探测的表面积覆盖了微孔隙和粗糙度，比有效换热表面积大几个数量级。使用RELAP模型解释BTC数据。 |
| 模态体积在Fenton Hill与热交换能力相关，影响长期热突破。 | [Ren 2023, pp. 4-5] | Fenton Hill EGS场地。 | 模态体积可能代表低阻抗、直接流动路径的体积。 |
| 水力压裂后，模态体积可能增加。 | [Ren 2023, pp. 4-5] | Hijiori和Rosemanowes EGS场地。 | 表明压裂增加了低阻抗流动通道。 |
| 在汇总的41种EGS示踪剂中，24种为惰性示踪剂，被注入167次。 | [Ren 2023, pp. 6-7] | 全球14个EGS场地，134次测试。 | 惰性示踪剂是应用最广泛的类型。 |

## Limitations
1.  **解释方法的限制**：解释井间连通性和储层体积的常规方法（如RTD）依赖于“稳态条件”和“惰性溶质示踪剂行为”的假设，而稳态水力传导难以实现，这会影响参数精度 [Ren 2023, pp. 4-5]。
2.  **换热表面积评价方法的局限**：
    *   基于Fenton Hill经验关系（模态体积法）的方法，尚无证据表明可应用于其他地热田 [Ren 2023, pp. 5-6]。
    *   吸附示踪剂方法探测到的吸附表面积比有效换热表面积大几个数量级，因为它覆盖了微孔隙和粗糙度 [Ren 2023, pp. 5-5]。
    *   利用不同扩散系数惰性示踪剂和吸附示踪剂的方法尚未在EGS场地尺度得到现场测试验证 [Ren 2023, pp. 5-6]。
3.  **数据质量问题**：因不可预测的示踪剂反应活性和注入量不足导致的低质量示踪剂数据，是定量分析的常见阻碍 [Ren 2023, pp. 1-2]。
4.  **应用范围限制**：EGS储层的高温、低含水量特点，使得部分适用于冷水环境的示踪剂因热降解而失效 [Ren 2023, pp. 1-2]。
5.  **综述本身限制**：本综述不包含天然示踪剂（如卤化物、温度、压力信号） [Ren 2023, pp. 6-7]。

## Assumptions / Conditions
- **模型条件**：用于计算井间连通性和储层体积的常规方法假设储层处于“稳态条件”，且示踪剂行为为“惰性溶质” [Ren 2023, pp. 4-5]。
- **储层模型**：RELAP模型假设流动路径为具有均匀裂缝孔径的“平行板”，常用于简化裂缝型储层 [Ren 2023, pp. 5-5]。
- **关键前提**：预测热突破的前提是确定了[[heat transfer surface area]] [Ren 2023, pp. 5-6]。

## Key Variables / Parameters
- `C(t)`: 突破曲线（BTC），即示踪剂浓度历史 [Ren 2023, pp. 3-4]。
- `E(t)`: 停留时间分布（RTD） [Ren 2023, pp. 3-4]。
- `q_out`: 体积产出流量 (m³/s) [Ren 2023, pp. 3-4]。
- `M_inj`: 示踪剂注入质量 (kg) [Ren 2023, pp. 3-4]。
- `R`: 示踪剂质量回收率 [Ren 2023, pp. 2-3]。
- `t*`: 平均停留时间 (s) [Ren 2023, pp. 2-3]。
- `V`: 累积产出流体体积 (m³) [Ren 2023, pp. 4-5]。
- `V_modal`: 模态体积 (m³)，对应于RTD曲线峰值。可能代表低阻抗连接通道的体积 [Ren 2023, pp. 5-5]。
- `<V>`: 积分平均体积 (m³)，被视为整个裂缝系统体积的近似值 [Ren 2023, pp. 4-5]。
- `V_p`: 示踪剂扫掠孔隙体积 (m³) [Ren 2023, pp. 4-5]。
- `A_f`: 换热表面积 (m²) [Ren 2023, pp. 5-6]。
- `R_f`: 延迟因子 [Ren 2023, pp. 2-3]。
- `T_prod`: 生产井流体温度 (K) [Ren 2023, pp. 5-6]。
- `T_r`: 岩石温度 (K) [Ren 2023, pp. 5-6]。
- `T_w`: 注入流体温度 (K) [Ren 2023, pp. 5-6]。
- `m_dot`: 质量流量 (kg/s) [Ren 2023, pp. 5-6]。
- `φ_m`: 基质孔隙度 [Ren 2023, pp. 2-3]。
- `BTC`: 突破曲线 [Ren 2023, pp. 2-3]。
- `RTD`: 停留时间分布 [Ren 2023, pp. 2-3]。

## Reusable Claims
1.  在EGS中，示踪剂质量回收率可以作为评估[[interwell connectivity]]的指标：回收率越高，连通性越好。此评估通过将示踪剂响应曲线（C(t)）转化为停留时间分布（E(t)）来计算 [Ren 2023, pp. 3-4]。
2.  同时注入吸附示踪剂和惰性示踪剂，可以通过分析吸附示踪剂因吸附引起的“延迟”来估算[[heat transfer surface area]]。但该方法测得的表面积是吸附表面积，其数值比有效换热表面积大几个数量级，因为它包含了微孔隙和粗糙度的贡献 [Ren 2023, pp. 5-5]。
3.  在[[EGS reservoir]]的[[hydraulic fracturing]]之后进行的示踪剂测试显示，模态体积（V_modal）可能会增加，这表明压裂作业增加了从注入井到生产井的低阻抗、直接流动通道 [Ren 2023, pp. 4-5]。

## Candidate Concepts
- [[enhanced geothermal system]] / [[EGS]]
- [[interwell connectivity]]
- [[reservoir volume]]
- [[heat transfer surface area]]
- [[thermal drawdown]] / [[thermal breakthrough]]
- [[inert tracer]] / [[novel tracer]]
- [[breakthrough curve]] / [[BTC]]
- [[residence time distribution]] / [[RTD]]
- [[modal volume]]
- [[dual-porosity system]]
- [[fracture reservoir]]

## Candidate Methods
- [[tracer test]]
- [[Reactive Transport Laplace Transform Inversion (RELAP) model]]
- [[single-well injection-withdrawal (SWIW) test]]
- [[fiber-optic distributed temperature sensing]]

## Connections To Other Work
- **EGS工程问题**：综述指出示踪剂测试旨在解决因压裂不充分或过度导致的EGS问题，如`优势流`（`short circuit`）、流体损失和热性能低下 [Ren 2023, pp. 3-4]。这将其与[[hydraulic fracturing design]]和[[reservoir characterization]]联系起来。
- **与其他领域技术的关联**：示踪剂测试在污染物迁移追踪、水文调查、油气工业中已广泛应用。这些领域的技术发展为EGS应用提供了参考经验，例如用于孔隙介质的纳米颗粒合成方法和特性 [Ren 2023, pp. 1-2]。
- **温度监测技术**：利用分布式光纤温度传感（DTS）进行热传输研究，可以检测交叉流裂缝，其结果与示踪剂测试结果互补 [Ren 2023, pp. 5-6]。

## Open Questions
- 在非Fenton Hill的EGS场地，如何可靠地建立模态体积与换热表面积之间的经验或物理关系？ [Ren 2023, pp. 5-6]
- 如何解决吸附示踪剂探测的吸附表面积远大于有效换热表面积的问题，以提高热突破预测精度？ [Ren 2023, pp. 5-5]
- 如何验证基于不同扩散系数惰性示踪剂或吸附示踪剂的换热表面积评估方法在实际EGS场地尺度的有效性？ [Ren 2023, pp. 5-6]
- 针对EGS储层高温、低含水量的特点，新型示踪剂（如纳米颗粒、温度响应示踪剂）的现场应用潜力和长期稳定性如何？ [Ren 2023, pp. 1-2]

## Source Coverage
本知识页依据论文的前6页（共51个索引片段）构建，主要覆盖了文章的摘要、引言、方法总览、解释方法（第2节）和示踪剂类型（第3节）的起始部分。覆盖深度偏重研究动机、核心参数解释方法和初步发现。关于示踪剂类型的详细物理化学性质（第3节后续部分）、示踪剂测试设计技术（第4节，如示踪剂选择、注入量计算、采样策略）以及全球各场地具体的示踪剂测试结果汇编（附录A）等关键信息，未从现有索引片段中确认。综述中对示踪剂响应、设计技术的深入讨论以及完整的结论可能存在于未提供的论文后续部分。
