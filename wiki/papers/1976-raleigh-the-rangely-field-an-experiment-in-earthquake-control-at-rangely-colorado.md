---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "1976-raleigh-the-rangely-field-an-experiment-in-earthquake-control-at-rangely-colorado"
title: "The Rangely Field: An Experiment in Earthquake Control at Rangely, Colorado."
status: "draft"
source_pdf: "data/papers/1976 - An Experiment in Earthquake Control at Rangely, Colorado.pdf"
collections:
  - "part4-2"
citation: "Raleigh, C. B., J. H. Healy, and J. D. Bredehoeft. \"The Rangely Field: An Experiment in Earthquake Control at Rangely, Colorado.\" *Science*, vol. 191, no. 4232, 1976, pp. 1230-37."
indexed_texts: "9"
indexed_chars: "43279"
nonempty_source_blocks: "9"
compiled_source_blocks: "9"
compiled_source_chars: "43483"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.004714"
coverage_status: "full-index"
source_signature: "674c980a2d8223b25373b29fdc8c8c108f66aed9"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T10:49:31"
---

# The Rangely Field: An Experiment in Earthquake Control at Rangely, Colorado.

## One-line Summary
科罗拉多州 Rangely 油田通过有控制地交替注水和回采流体，使地震活动频率随储层流体压力在预测临界值附近变化，首次在野外实验中证实了基于有效应力原理的地震控制可行性 [Raleigh 1976, pp. 7-8]。

## Research Question
- 能否通过人为调控地下流体压力来控制诱发地震活动？
- Hubbert‑Rubey 有效应力定律能否定量预测触发地震所需的临界流体压力？
- 是否可以在保证安全的前提下，在真实的断层带中重复实现压力‑地震活动的相关性？

## Study Area / Data
- **地理位置**：美国科罗拉多州西北部 Rangely 油田，为一个双重倾伏背斜，地表出露 Mancos 页岩 [Raleigh 1976, pp. 1-1]。
- **储层与地质**：主要产油层为 Pennsylvanian‑Permian Weber 砂岩，深度约 1700 m，厚约 350 m，孔隙度 12%，渗透率约 1 mD；其下为古生界碳酸盐岩与砂岩，基底结晶岩约在 3000 m 深 [Raleigh 1976, pp. 1-1; pp. 1-2]。
- **断层**：通过井下构造等高线识别出一条走向东‑北东向、视垂直断距 10–15 m 的断层，地表 Mancos 页岩中存在同走向的裂隙与方解石脉，该断层是主要的地震活动构造 [Raleigh 1976, pp. 1-1; pp. 1-2]。
- **注水历史**：1957 年开始注水以提高采收率；至 1962 年局部储层压力已超过原始压力 170 bar；1967 年记录到最高井底压力达 290 bar [Raleigh 1976, pp. 1-1; pp. 1-2]。
- **地震监测**：1962 年 Vernal 台阵开始记录到小震；1969 年布设 14 台短周期垂向检波器组成的微震台网，数据遥传至 Menlo Park；实验期间台网构型保持不变，所有定位地震均用于统计，震级 ML ≥ −0.5 [Raleigh 1976, pp. 1-2; pp. 2-3; pp. 3-4]。

## Methods
- **地震定位与震级**：采用层状速度模型，通过最小化 100 个地震的到时残差确定模型参数并计算台站校正；利用 HYPOLAYR 程序定位；震级基于信号持续时间经验关系 M = 1.8 log t − 1.0，仅使用不少于 6 台记录的清晰事件 [Raleigh 1976, pp. 2-3]。
- **地应力测量**：在 Weber 砂岩的钻孔中实施水力压裂试验（Haimson, 1972），测得瞬时关闭压力（等于最小主应力 S₃）、破裂压力，并结合实验室确定的张拉强度 T 和加压速率校正，解算最大主应力 S₁ [Raleigh 1976, pp. 3-4]。
- **临界压力计算**：根据震源机制解得到的断层产状和滑动方向，计算断层面上的剪应力 τ 和正应力 Sₙ；利用 Weber 砂岩的静摩擦系数 μ = 0.81，按 Hubbert‑Rubey 准则 τ = μ (Sₙ − P_c) 解出临界孔隙压力 P_c = 257 bar [Raleigh 1976, pp. 3-4; pp. 4-5]。
- **储层压力模拟与监测**：建立单相变压缩性储层模拟器，用有限差分法计算压力分布；同时在 5 口关闭观测井中用井口压力传感器连续记录，并与定期底孔压力测量对比 [Raleigh 1976, pp. 4-5]。
- **压力‑地震活动循环实验**：以 1969 年 10 月–1970 年 11 月为注水增压期；1970 年 11 月–1971 年 5 月通过回采降压；1971 年 5 月后再次注水但后因油田生产调整降压；1972 年 8 月–1973 年 5 月重新增压；1973 年 5 月起再次回采直至地震停止 [Raleigh 1976, pp. 5-6; pp. 6-7]。

## Key Findings
- **地震与高压区对应**：地震主要集中于两条簇群，一条位于实验注水井正下方（深 2.0–2.5 km，在 Weber 层内），另一条位于西南方向（深约 3.5 km），两者均沿地下断层走向分布 [Raleigh 1976, pp. 2-3]。
- **断层性质**：震源机制显示断层为右旋走滑型，走向约 N 50° E，断层带内存在次平行破裂面，宽度逾 1 km [Raleigh 1976, pp. 3-4]。
- **临界压力验证**：在第一次降压期，Fee 69 井底压力从 275 bar 降至 203 bar，实验井 1 km 范围内月均地震数从约 28 次降至约 1 次；1972–1973 年当压力再次超过 257 bar 并升至 280 bar 时，月均地震回升至 26 次；1973 年 5 月回采后，该区域内无震 [Raleigh 1976, pp. 5-6; pp. 6-7]。
- **应力与摩擦系数匹配**：实测 S₁ = 552 bar，S₂ = 427 bar（上覆应力），S₃ = 314 bar；由断层面解得的剪切和正应力与 μ = 0.81 和临界压力 257 bar 相符 [Raleigh 1976, pp. 3-4]。
- **快速压力响应**：井 Emerald 45 与注入井之间压力响应迅速，说明断层带内渗透率足够高，可以在数天内传递压力变化，使地震活动对回采立刻响应 [Raleigh 1976, pp. 5-6]。
- **控制的安全性**：由于实验区北部持续采出流体，断层带大部分区域压力保持低于临界值，断层可滑移长度有限，避免了破坏性地震的发生 [Raleigh 1976, pp. 6-7]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 10 日微震记录集中分布在注水引起的高压区 | [Raleigh 1976, pp. 1-1]; [Raleigh 1976, pp. 2-3] | 1969 年秋进行的短周期流动台网观测，压力等值线来自 1969 年 9 月测量 | 初次建立地震与注水压力之间的空间相关性 |
| 水力压裂应力测量结果：S₁=552 bar, S₂=427 bar, S₃=314 bar | [Raleigh 1976, pp. 3-4] | 在 Weber 砂岩中进行，低渗透率 (0.1 mD)，垂直裂缝方向 N 70° E | 为计算临界压力提供了绝对应力值 |
| 断层面剪应力 τ = 72 bar，正应力 Sₙ = 342 bar，摩擦系数 μ = 0.81 | [Raleigh 1976, pp. 3-4]; [Raleigh 1976, pp. 4-5] | 摩擦系数来自于 Weber 砂岩的实验室测试；断层产状基于震源机制解 | 由 Hubbert‑Rubey 准则计算 P_c = 257 bar |
| 三次注水–回采循环中，地震频率随井底压力高于或低于 257 bar 相应变化 | [Raleigh 1976, pp. 5-6]; [Raleigh 1976, pp. 6-7] | 以 Fee 69 的 72‑h 关井压力为代表；地震计数限定在实验井 1 km 内 | 直接验证了有效应力控制地震活动的假说 |
| 1973 年 5 月回采开始后，实验区无震，仅西南远处断层每月约 1 次事件 | [Raleigh 1976, pp. 6-7] | 回采后 1 天内地震完全停止 | 显示出压力变化可以快速实现对断层的强化 |
| 震源定位存在约 200–300 m 的系统北偏误差 | [Raleigh 1976, pp. 2-3] | 校准爆破显示各向异性速度模型或压力变化引起的速度变化可导致向北偏移 | 实际震中可能更偏向注水井下方，但未修正 |

## Limitations
- 无法确定注水开始前的地震活动背景，因为台网布设晚于注水 12 年 [Raleigh 1976, pp. 1-2]。
- 地震定位存在系统性北偏（200–300 m），未进行校正，部分重要地震可能错划到低压力区 [Raleigh 1976, pp. 2-3]。
- 储层压力模拟采用单相流并需补偿油水比变化，仅能近似反映真实压力分布 [Raleigh 1976, pp. 4-5]。
- 断层带渗透率各向异性（假定为 5 倍）系通过模型调试，非直接测量 [Raleigh 1976, pp. 5-6]。
- 实验只控制了油田局部断层段，不能直接证明对自然大地震的控制可行性。

## Assumptions / Conditions
- 诱发地震的物理机制遵从 Hubbert‑Rubey 有效应力定律，即断层滑移的临界剪应力与有效正应力成线性关系 [Raleigh 1976, pp. 1-1]。
- 水力压裂法获得的关闭压力等于最小主应力 S₃，且裂缝垂直于 S₃ 传播 [Raleigh 1976, pp. 3-4]。
- 井底关井压力代表震源区流体压力，且压力传递在实验时间尺度内足以影响整个地震簇 [Raleigh 1976, pp. 5-6]。
- Weber 砂岩的静摩擦系数 (μ = 0.81) 适用于地下断层破裂面 [Raleigh 1976, pp. 3-4]。
- 实验区的构造应力状态在 1969–1974 年间保持稳定，未被油田作业显著扰动 [Raleigh 1976, pp. 4-5]。

## Key Variables / Parameters
- **临界流体压力 (P_c)**：257 bar，由 τ = μ (Sₙ − P_c) 计算 [Raleigh 1976, pp. 3-4]。
- **实测主应力**：S₁ = 552 bar，S₂ = 427 bar，S₃ = 314 bar [Raleigh 1976, pp. 3-4]。
- **断层面应力**：剪应力 τ = 72 bar，正应力 Sₙ = 342 bar [Raleigh 1976, pp. 3-4]。
- **摩擦系数 (μ)**：0.81（Weber 砂岩断层标本）[Raleigh 1976, pp. 3-4]。
- **初始储层压力 (P₀)**：162 bar [Raleigh 1976, pp. 3-4]。
- **b 值**：西南侧较深事件簇 b=0.81，东北侧较浅事件簇 b=0.96 [Raleigh 1976, pp. 3-4]。
- **渗透率各向异性**：沿断层方向的渗透率设为横向的 5 倍，以获得与观测压力吻合的最佳模型 [Raleigh 1976, pp. 5-6]。
- **地震定位系统误差**：北向偏移 200–300 m（来自校准爆破）[Raleigh 1976, pp. 2-3]。

## Reusable Claims
- 在已知应力状态和断层摩擦特性的条件下，可根据 Hubbert‑Rubey 有效应力定律提前计算出触发地震所需的孔隙压力阈值 [Raleigh 1976, pp. 3-4]。
- 通过回采降低断层带内的流体压力，可急剧增强断层摩擦强度，使地震活动在数天内完全停止 [Raleigh 1976, pp. 6-7]。
- 只要断层带渗透率足够高，人工调控注水压力就能快速改变断层强度，从而控制剪切滑动 [Raleigh 1976, pp. 5-6]。
- 在油田环境中，通过维持断层大部分区域的压力低于临界值，可将地震滑移限制在很小的空间范围内，有效避免破坏性大地震 [Raleigh 1976, pp. 6-7]。
- 水力压裂应力测量在低渗、均匀砂岩储层中能够可靠获取完整的三维应力张量，为地震控制实验提供必要基础 [Raleigh 1976, pp. 3-4]。

## Candidate Concepts
- [[Hubbert-Rubey有效应力准则]]
- [[诱发地震]]
- [[地震控制]]
- [[孔隙压力触发]]
- [[走滑断层]]
- [[储层压力模拟]]
- [[b值]]
- [[临界孔隙压力]]

## Candidate Methods
- [[水力压裂地应力测量]]
- [[微地震台网定位]]
- [[注水-回采循环实验]]
- [[校准爆破定位校正]]
- [[单相变压缩性储层模拟]]
- [[信号持续时震级估计]]

## Connections To Other Work
- 该实验直接源于 1960 年代 Denver 废液注入诱发地震的发现（Evans, 1966; Healy et al., 1968）[Raleigh 1976, pp. 1-1]。
- 所用有效应力原理与 Hubbert‑Willis（1957）的水力压裂理论一致 [Raleigh 1976, pp. 3-4]。
- 与水库诱发地震的研究（Gupta et al., 1972）相呼应，指出通过排水降压可增强断层 [Raleigh 1976, pp. 6-7]。
- 文中提及实验室摩擦实验（Byerlee, 1975）和 Dieterich 的实验室模拟（Dieterich & Raleigh, 1974）为控制方案提供了物理基础 [Raleigh 1976, pp. 7-8]。
- 将研究结果引申到 San Andreas 断层的控制设想，借鉴了 Wallace（1970）的滑动速率估计 [Raleigh 1976, pp. 7-8]。

## Open Questions
- 深部断层带（数公里深度）的实际渗透率是多少？是否足以实现大范围的压力控制？[Raleigh 1976, pp. 7-8]
- 能否在自然地震区如 San Andreas 断层实施类似的降压强化试验？技术和经济可行性如何？[Raleigh 1976, pp. 7-8]
- 在反复注水‑回采循环下，断层带的摩擦滞留、化学作用等长期效应是否会影响控制效果？[Raleigh 1976, pp. 7-8]
- 如何准确校正地震定位中的速度各向异性，以获得更可靠的震源‑压力空间关系？[Raleigh 1976, pp. 2-3]
- 注水诱发地震的最大可能震级如何事先评估？在数值模型中如何纳入断层长度和应力降约束？[Raleigh 1976, pp. 6-7]

## Source Coverage
本页面完全基于论文“An Experiment in Earthquake Control at Rangely, Colorado” (Raleigh, Healy, Bredehoeft, 1976, *Science*) 的索引片段构建。所有索引片段均已处理，具体覆盖情况如下：
- 索引文本块数量：9 个（标签 至）[Raleigh 1976, pp. 1-1, 8-8]。
- 其中第 9 块[Raleigh 1976, pp. 8-8]实为同刊另一篇论文“Restored Pictures of Ganymede”的开头部分，与 Rangely 地震实验无关，故未纳入正文，但已进行识别。
- 实际使用片段：8 个（至）[Raleigh 1976, pp. 1-1, 7-8]，涵盖引言、地质、地震活动、应力测量、储层模拟、控制实验、讨论及总结。
- 使用文本总字符数约 43,279（不含无关块），覆盖率按块计 100%，按字符计 > 99%（忽略无关页）。所有非空有效片段均已编译。
