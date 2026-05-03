---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2022-patidar-a-review-of-tracer-testing-techniques-in-porous-media-specially-attributed-to-the-o"
title: "A Review of Tracer Testing Techniques in Porous Media Specially Attributed to the Oil and Gas Industry."
status: "draft"
source_pdf: "data/papers/2022 - A review of tracer testing techniques in porous media specially attributed to the oil and gas industry.pdf"
collections:
  - "part4-1"
citation: "Patidar, Atul Kumar, et al. \"A Review of Tracer Testing Techniques in Porous Media Specially Attributed to the Oil and Gas Industry.\" *Journal of Petroleum Exploration and Production Technology*, vol. 12, 2022, pp. 3339-3356, doi:10.1007/s13202-022-01526-w."
indexed_texts: "18"
indexed_chars: "86451"
nonempty_source_blocks: "18"
compiled_source_blocks: "18"
compiled_source_chars: "85816"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.992655"
coverage_status: "full-index"
source_signature: "67d7cc845341ed262b0c8caa13dbf54d26b1ed4a"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T04:58:09"
---

# A Review of Tracer Testing Techniques in Porous Media Specially Attributed to the Oil and Gas Industry.

## One-line Summary
本综述系统梳理了放射性、化学及微量物质三类示踪剂在油气勘探开发中的特性、选择标准、测试设计、操作执行与分析解释方法，重点阐释单井示踪测试（SWTT）与井间示踪测试（IWTT）在储层非均质性描述、残余油饱和度测定及水驱优化中的定量应用。

## Research Question
示踪剂测试技术如何通过单井与井间实施方式，为多孔介质中油气储层提供定量化的构造‑地层非均质性信息、井间连通性评价、残余油饱和度（S_or）计算及提高采收率（EOR）优化依据？不同示踪剂类型与测试方法的关键控制参数和适用条件是什么？

## Study Area / Data
本文为综述性论文，未涉及特定油田实例。所引数据均来自已公开发表的文献、行业指南及实验研究成果 [Patidar 2022, pp. 1-2; 14-15]。文献覆盖了油气田示踪测试的历史发展（如五点法注采模式、井间连通性分析）、放射性及化学示踪剂现场应用、以及近年来纳米示踪剂与DNA示踪剂等新兴方向 [Patidar 2022, pp. 2-2; 5-7]。

## Methods
采用文献综述法，首先按示踪剂类型（放射性、化学、微量物质）归纳其物理化学特性及选择原则（表1）[Patidar 2022, pp. 2-4]。接着区分两种主要测试类型：单井示踪测试（SWTT）与井间示踪测试（IWTT），阐述各自目的（定性‑定量）、计算公式（示踪剂用量、残余油饱和度等）、设计阶段（仪器校准与静‑动态岩心模拟）、现场执行（注入‑取样‑关井）以及实验室分析流程（气相色谱、分光光度计、液体闪烁计数器）[Patidar 2022, pp. 7-14]。最后综述不同解释方法（解析法、数值模拟法、半解析法）的应用场景 [Patidar 2022, pp. 14-14]。

## Key Findings
1. 放射性示踪剂与化学示踪剂是当前最具实用性的两类示踪剂，合理选用可对近井筒及井间区域进行精细表征；尽管存在环境争议，但新型示踪剂的持续开发正使该技术成为储层描述的重要工具 [Patidar 2022, pp. 14-14]。
2. 单井示踪测试（SWTT）和井间示踪测试（IWTT）适应不同开发阶段的需求；相较于仅表征近井地带的传统测井和调查手段，示踪测试能提供径向上的综合信息，有助于制定高效的二次和三次采油方案 [Patidar 2022, pp. 14-15]。
3. 气相色谱、分光光度计和液体闪烁计数等分析方法可与人工智能/机器学习（AI/ML）技术结合，以生成和解释测试结果，并可用于优化示踪测试计划 [Patidar 2022, pp. 15-15]。
4. 智能示踪剂（如缓释示踪剂）不仅能辅助储层描述，还能检测、量化和监测相突破，用于生产剖面分析，且成本效益优于生产测井工具 [Patidar 2022, pp. 15-15]。
5. 示踪测试已成功应用于非常规储层，可在压裂和EOR过程中进行实时数据分析，从而优化作业 [Patidar 2022, pp. 15-15]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|-------------|-------|
| 示踪剂须具备可溶性、储层温压下化学稳定、不吸附、低成本、低检测限及环境友好等特性 | [Patidar 2022, pp. 2-4]（表1） | 适用于水基注入流体；放射性示踪剂额外要求相似性、射线性、合适半衰期 | 表1列出12项特性及其参考文献 |
| IWTT示踪剂用量公式：化学示踪剂 \(M = 3.47 \times 10^{-3} \phi S_w h L^{0.265} L^{1.735} \text{MDL}\)，放射性示踪剂还需考虑半衰期和辐射稀释因子 | [Patidar 2022, pp. 7-7] Eq.(1)–(3) | 需要储层厚度、孔隙度、水饱和度、井距、检测限等参数 | 公式中的常数源于经验或理论推导 |
| SWTT残余油饱和度计算公式：\(S_{or} = \beta / (\beta + K)\)，其中 \(\beta = Q_a/Q_b - 1\)，K为分配系数 | [Patidar 2022, pp. 14-14] Eq.(7),(8) | 基于色谱分离原理，适用于均质储层 | 非均质储层可能导致化学剂返排不充分 |
| 化学气体示踪剂如SF₆及PFC类（PDMCB、PMCP、PMCH等）具有化学惰性、高稳定性和高检测灵敏度 | [Patidar 2022, pp. 4-5] | 用于气驱或气体运移监测，在高温下可能降解 | SF₆采用气相色谱‑电子捕获检测器分析 |
| 示踪测试失败可能因流体沿高渗透通道旁流、取样不足、未考虑天然裂缝或含水层稀释等 | [Patidar 2022, pp. 10-11] | 注入压力无显著升高、监测井无响应时需排查 | 可导致错误结论或测试无效 |

## Limitations
- 本文为综述，未提供新的实验或现场数据验证 [Patidar 2022, pp. 1-2]。
- SWTT假设储层相对均质，在强非均质性条件下化学示踪剂返排率低，结果不确定 [Patidar 2022, pp. 7-8]。
- 化学示踪剂在温度超过95°C时可能降解，限制高温油藏应用 [Patidar 2022, pp. 4-5]。
- 放射性示踪剂受限于信号穿透深度（仅数英尺），且存在健康安全与法规风险 [Patidar 2022, pp. 2-2]。
- 取样频率不当或注入‑取样交叉污染会影响数据质量 [Patidar 2022, pp. 10-11]。

## Assumptions / Conditions
- 测试设计假设注入流体均匀驱替，且示踪剂在储层中不发生吸附或化学反应（理想情况）[Patidar 2022, pp. 2-4]。
- 静态设计程序中，假设岩样与流体在模拟储层温压下保持稳定 [Patidar 2022, pp. 8-10]。
- IWTT计算假设井间为径向流或线性流，且忽略毛管力影响 [Patidar 2022, pp. 7-8]。
- 分配系数K定义为示踪剂在油中与水中的浓度比，且在一定温度‑压力‑盐度范围内视为常数 [Patidar 2022, pp. 10-10]。
- 残余油饱和度计算基于色谱延迟因子β，并假定产液量‑峰值的线性关系 [Patidar 2022, pp. 14-14]。

## Key Variables / Parameters
- **孔隙度（φ）**：IWTT采用总孔隙度 [Patidar 2022, pp. 7-7]。
- **水饱和度（S_w）** [Patidar 2022, pp. 7-7]。
- **井距（L）**：注入井与生产井间距离 [Patidar 2022, pp. 7-7]。
- **检测限（MDL/DL）**：区分最低可检出浓度和可定量浓度 [Patidar 2022, pp. 7-7, 11-11]。
- **示踪剂半衰期（t₁/₂）**：仅适用于放射性示踪剂 [Patidar 2022, pp. 7-7]。
- **延迟因子（β）**：SWTT中由酯峰与醇峰的产液量比值确定 [Patidar 2022, pp. 14-14]。
- **分配系数（K）**：受原油组成、盐度和温度影响 [Patidar 2022, pp. 10-10]。
- **段塞体积**：与调查半径、储层厚度、孔隙度、水饱和度和延迟因子相关 [Patidar 2022, pp. 8-8]。
- **注入/采出速率**：影响SWTT段塞体积和水解反应时间 [Patidar 2022, pp. 8-8]。

## Reusable Claims
- 示踪剂测试是油气行业中少数能够对亚地震尺度构造‑地层非均质性进行定量评价的技术之一 [Patidar 2022, pp. 1-1]。
- 化学示踪剂的效益已在石油勘探中得到证实，因其快速、低成本且适用于复杂地下条件 [Patidar 2022, pp. 4-5]。
- 井间示踪测试（IWTT）可揭示定向流动趋势、断层屏障、变形带及储层分隔性 [Patidar 2022, pp. 5-7]。
- 单井示踪测试（SWTT）通过酯的水解和色谱分离原理实现残余油饱和度原位测量，且不改变储层润湿性 [Patidar 2022, pp. 7-8]。
- 静态和动态岩心驱替实验是示踪剂筛选和测试设计的关键步骤 [Patidar 2022, pp. 8-10]。
- 成功的示踪测试依赖于严谨的取样策略：高频采样、及时分析、添加杀菌剂防止生物降解 [Patidar 2022, pp. 10-11]。

## Candidate Concepts
- [[单井示踪测试（SWTT）]]
- [[井间示踪测试（IWTT）]]
- [[残余油饱和度（S_or）]]
- [[延迟因子（β）]]
- [[分配系数（K）]]
- [[水解反应]]
- [[色谱分离]]
- [[五次网格式注采模式]]
- [[亚地震尺度构造非均质性]]
- [[智能示踪剂（缓释示踪剂）]]
- [[纳米示踪剂]]
- [[DNA示踪剂]]
- [[提高采收率（EOR）]]
- [[体积波及效率]]
- [[井间连通性]]

## Candidate Methods
- [[气相色谱（GC）]]
- [[火焰离子化检测器（FID）]]
- [[电子捕获检测器（ECD）]]
- [[温度梯度分离]]
- [[分光光度法（Beer–Lambert定律）]]
- [[液体闪烁计数]]
- [[岩心驱替实验]]
- [[静态配伍性实验]]
- [[数值模拟解释法]]
- [[半解析解释法]]
- [[对数‑注入‑对数（LIL）方法]]
- [[基于人工智能/机器学习的示踪数据分析]]

## Connections To Other Work
- 示踪测试常与脉冲试井、干扰试井等储层表征方法联合使用，以补充井间连通性信息 [Patidar 2022, pp. 4-5]。
- 数字岩石物理（3D成像）与声学/渗流特性关联的研究可作为示踪测试的补充 [Patidar 2022, pp. 2-2]。
- 钯同位素等天然示踪剂在环境水文学中已被证实为有效工具，引申至油气田同样具有参考价值 [Patidar 2022, pp. 2-2]。
- 示踪测试的结果可集成至储层地质模型，用于指导二次和三次采油方案 [Patidar 2022, pp. 14-14]。
- 纳米技术和DNA编码示踪剂的发展借鉴了医学与生物学领域的检测手段 [Patidar 2022, pp. 5-7]。

## Open Questions
- 如何更可靠地将AI/ML技术集成到示踪测试的设计、实时优化与结果解释中？ [Patidar 2022, pp. 14-15]
- 智能示踪剂（如缓释型和纳米示踪剂）在高温高压、高矿化度油藏中的长期稳定性和定量精度尚需验证 [Patidar 2022, pp. 15-15]。
- 非常规储层中多级压裂与示踪剂监测的耦合机制及其对生产动态的实时反馈需要进一步研究 [Patidar 2022, pp. 15-15]。
- 示踪剂测试能否突破目前对非均质储层适应性的限制，发展出更鲁棒的段塞设计方法和数据解释模型？
- 放射性示踪剂的安全替代方案（如可生物降解的化学示踪剂）能否在灵敏度和选择性上达到同等水平？

## Source Coverage
本文的撰写完全基于已索引的18个非空源片段（共86,451字节），所有片段均被编译整合进当前页面（编译后字符数85,816），片段覆盖率为100%，字符覆盖率约99.27%。索引状态为“full-index”，无遗漏的源文本模块。
