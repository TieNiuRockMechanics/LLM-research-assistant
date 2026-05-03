---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2022-zhao-effects-of-temperature-and-increasing-amplitude-cyclic-loading-on-the-mechanical-prope"
title: "Effects of Temperature and Increasing Amplitude Cyclic Loading on the Mechanical Properties and Energy Characteristics of Granite."
status: "draft"
source_pdf: "data/papers/2022 - Effects of temperature and increasing amplitude cyclic loading on the mechanical properties and energy characteristics of granite.pdf"
collections:
  - "靳一作以外的"
citation: "Zhao, Guokai, et al. \"Effects of Temperature and Increasing Amplitude Cyclic Loading on the Mechanical Properties and Energy Characteristics of Granite.\" *Bulletin of Engineering Geology and the Environment*, vol. 81, 2022. DOI: 10.1007/s10064-022-02655-6."
indexed_texts: "11"
indexed_chars: "52580"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T04:14:56"
---

# Effects of Temperature and Increasing Amplitude Cyclic Loading on the Mechanical Properties and Energy Characteristics of Granite.

## One-line Summary
该研究通过 25–600 °C 下递增振幅循环加载实验，揭示了花岗岩的硬化现象（弹性模量对数增长、残余应变减小）和能量特征由非线性向线性转变，并提出弹性能密度与输入能密度的线性模型 [Zhao 2022, pp. 1-2, 10-11]。

## Research Question
温度和递增应力水平如何影响花岗岩在多级循环加载下的力学性质及能量特征？ [Zhao 2022, pp. 1-2]

## Study Area / Data
花岗岩试样取自均质块体，无明显宏观缺陷；矿物组成为钾长石（40–45%）、斜长石（30–35%）、石英（20–25%）、黑云母（3–5%）。加工为 Φ30 mm × 60 mm 圆柱样，共 21 块，按 ISRM 建议方法处理，平均 P 波速度 4.418 km/s。实验设置 7 个温度点：25、100、200、300、400、500、600 °C，采用多级单循环加载（MLSCL），每级上限应力基于同种岩石的常规单轴压缩试验确定 [Zhao 2022, pp. 3-4]。

## Methods
‑ 设备：多功能高温三轴试验机（最大轴向力 1000 kN，最高 650 °C，刚度 4×10^9 N/m）。
‑ 加温：以 2 °C/min 升温至目标温度，保温 2 h 确保均匀。
‑ 加载路径：MLSCL，应力水平上限依次为 0.4、0.6、0.7、0.8、0.9（相对于各温度的 UCS）。未从索引片段中确认加载速率、围压是否施加；文中提及“三轴试验机”但无围压设定描述，很可能为单轴压缩。
‑ 力学参数：弹性模量取各应力水平加载曲线线性段计算。
‑ 能量密度：通过应力‑应变回线积分，总输入能密度 u，弹性能密度 ue，耗散能密度 ud，满足 u ＝ ue ＋ ud [Zhao 2022, pp. 3-5, 7-8]。

## Key Findings
1. 花岗岩在递增幅度循环加载下出现硬化：弹性模量随应力水平呈对数式增长，相对残余应变整体下降；该现象在 100–500 °C 明显，600 °C 时减弱 [Zhao 2022, pp. 5-6, 7-10]。
2. 弹性模量随温度升高而降低，25 °C 最大、600 °C 最小；100–400 °C 各循环（除第一次）模量几乎相同 [Zhao 2022, pp. 5-6]。
3. 25、100 °C 时，总输入能密度 u 和弹性能密度 ue 随应力水平呈近似指数增长；200–600 °C 则转为线性增长（卸载应力水平低于 0.9 时） [Zhao 2022, pp. 1-2, 8-10]。
4. 能量演化以积聚为主：ue 占 u 的绝大部分，耗散比 ud/u 在首循环最高（19.4%–34.8%），随后递减并趋于稳定；温度对能量分配模式影响微弱 [Zhao 2022, pp. 8-9]。
5. 提出 ue ‑ u 线性模型 ue ＝ a·u ＋ b，各温度下 R² ≥ 0.996（a ＝ 0.878–0.940，b 为负值），可作为基于能量的脆性指数基础 [Zhao 2022, pp. 10]。
6. 累计残余应变在 600 °C 时最大，且随应力水平近似线性增长；相对残余应变主要由首循环产生，300–500 °C 范围内递减后趋稳，600 °C 高应力下则急剧增加 [Zhao 2022, pp. 7-8]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 弹性模量随应力水平呈对数增长，相对残余应变减小 | [Zhao 2022, pp. 5-6, 7-8] | MLSCL, 25–600 °C | 100 – 500 °C 硬化显著，600 °C 衰减 |
| ue 与 u 强线性相关（ue ＝ a·u ＋ b），R² ≥ 0.996 | [Zhao 2022, pp. 10] | MLSCL，各温度，未含压实段 | a、b 见表 3，可评价脆性 |
| 100–400 °C 弹性模量（除首循环）几乎相同 | [Zhao 2022, pp. 5-6] | MLSCL，每级取线性段 | 热损伤与循环硬化可能平衡 |
| 200–600 °C，u、ue 随应力水平接近线性增长 | [Zhao 2022, pp. 1-2, 8-10] | 卸载水平 ≤ 0.9 | 低温区则呈指数增长 |
| ud/u 首循环最大（19 – 35 %），后递减趋稳 | [Zhao 2022, pp. 8-9] | MLSCL，全部温度 | 能量积聚主导峰前阶段 |
| 累计残余应变在 600 °C 0.9 应力水平异常增大 | [Zhao 2022, pp. 7-8] | 600 °C, MLSCL | 显示高温塑性增强 |

## Limitations
‑ 试验仅涉及峰前阶段，峰后行为未知 [未从索引片段中确认]。
‑ 加载速率、频率未在片段中给出，可能影响硬化/疲劳特性 [未从索引片段中确认]。
‑ 缺少压实阶段的加卸载数据，限制了线性储能律在低应力的应用 [Zhao 2022, pp. 10]。
‑ 试样尺寸较小（Φ30×60 mm），尺寸效应未讨论 [未从索引片段中确认]。
‑ 结果仅针对一种花岗岩，其他岩石的广义线性关系待验证 [Zhao 2022, pp. 10]。

## Assumptions / Conditions
‑ 试样初始均质、无缺陷，P 波速度接近保证一致性 [Zhao 2022, pp. 3]。
‑ 加热速率 2 °C/min 且保温 2 h 使内部温度均匀，忽略热梯度 [Zhao 2022, pp. 4]。
‑ 应力路径为 MLSCL，每级卸载至零，上限应力由同温度 UCS 决定。未明确说明是否施加围压，很可能为单轴压缩 [未从索引片段中确认]。
‑ 能量计算基于应力‑应变回线，假设卸载曲线下面积代表可释放弹性能，其余为耗散能，符合热力学第一定律 [Zhao 2022, pp. 8]。

## Key Variables / Parameters
‑ 温度 T：25, 100, 200, 300, 400, 500, 600 °C
‑ 应力水平（卸载水平比）：0.4, 0.6, 0.7, 0.8, 0.9
‑ 弹性模量 E（各应力水平的线性段）
‑ 累计残余应变、相对残余应变
‑ 能量密度：u (总), ue (弹性), ud (耗散)，单位 mJ/mm³
‑ 耗散能比 ud/u 或 ue/u
‑ 线性模型参数 a（斜率）、b（截距），ue = a·u + b
‑ 加载路径类型：MLSCL

## Reusable Claims
1. 室温至 600 °C 花岗岩在 MLSCL 峰前阶段出现硬化，弹性模量与应力水平呈对数增长，相对残余应变下降。该规律在 100–500 °C 突出；温度超过 500 °C 硬化减弱。限制：需进一步验证对其他岩石和循环路径的适用性 [Zhao 2022, pp. 5-7, 10]。
2. 200–600 °C 下，当卸载应力水平低于 0.9，u 和 ue 随应力水平几乎线性增加；而 25、100 °C 时呈近似指数增长。可用于判断温度区间内的能量演化特征。限制：仅适用峰前，不含压实阶段 [Zhao 2022, pp. 1-2, 8-10]。
3. 弹性能密度 ue 与总输入能密度 u 存在强线性关系 ue = a·u + b，a ≈ 0.88–0.94，R² ≥ 0.996。该关系可直接用于构建能量脆性指数，评估储层稳定性和可压缩性。限制：基于特定花岗岩、单轴 MLSCL，未含水、围压条件，需推广至其他岩石 [Zhao 2022, pp. 10]。
4. 在 25–600 °C 单轴循环加载下，峰前能量分配以弹性能积聚为主，首循环耗散比最高（约 19–35%），之后递减并稳定；温度对该分配模式影响甚微。限制：不适用于损伤严重的峰后或高周次疲劳 [Zhao 2022, pp. 8-9]。
5. 累计残余应变随应力水平近似线性增加，600 °C 时值最大，可作为热塑性强化的直观指标；相对残余应变在 100–500 °C 总体下降，反映循环硬化。限制：600 °C 下 0.9 应力水平例外，此时相对残余应变激增 [Zhao 2022, pp. 7-8]。

## Candidate Concepts
‑ [[Rock hardening under cyclic loading]]
‑ [[High-temperature granite]]
‑ [[Energy evolution in rocks]]
‑ [[Linear energy storage law]]
‑ [[Energy-based brittleness index]]
‑ [[Fatigue hydraulic fracturing]]
‑ [[Cyclic thermal loading]]
‑ [[Microcrack closure and compaction]]
‑ [[Multilevel single cyclic loading (MLSCL)]]
‑ [[Deformation memory effect of rock]]

## Candidate Methods
‑ [[Multilevel amplitude cyclic loading test]]
‑ [[Energy density calculation from stress-strain loops]]
‑ [[Elastic modulus calculation per stress increment]]
‑ [[Accumulative and relative residual strain analysis]]
‑ [[Linear fitting of elastic energy vs. input energy]]
‑ [[High-temperature triaxial testing]]
‑ [[P-wave velocity screening]]
‑ [[ISRM suggested methods for rock characterization]]

## Connections To Other Work
‑ 本工作发现的硬化现象与 Xia et al. (2015) 在玄武岩、Wong et al. (2020) 在砂岩中的观察一致，提示温和温度或循环加载可能引起强化，需要系统评估 [Zhao 2022, pp. 10]。
‑ 所提出的 ue‑u 线性关系为 [[energy-based brittleness index]] 提供了实验依据，但原文未对比其他能量-脆性模型，可连接至相关脆性评价研究。
‑ 研究结果与疲劳水力压裂（Zang et al. 2013, 2017）和循环升压注入（Chang 2019）存在潜在矛盾：硬化可能使压裂压力升高、裂缝形态变化，需重新考虑注入策略 [Zhao 2022, pp. 11]。
‑ 硬化机制归纳涉及多种微裂纹类型（应力诱导、温度诱导、循环疲劳、时间相关），可导向基于微裂纹尺度的本构模型开发，但论文未提供具体耦合模型 [Zhao 2022, pp. 10]。

## Open Questions
‑ 超过 600 °C 或更多循环周次后，花岗岩的硬化‑劣化转折条件与临界损伤阈值是什么？未从索引片段中确认。
‑ 广义的 ue‑u 线性方程能否统一描述不同岩性？需系统试验 [Zhao 2022, pp. 10]。
‑ 若将压实阶段纳入，线性模型的截距和适用范围如何改变？[Zhao 2022, pp. 10]
‑ 循环硬化对实际 EGS 疲劳压裂的影响：是否导致起裂压力升高、裂缝网络简化？如何优化压裂设计以利用或规避硬化效应？[Zhao 2022, pp. 11]
‑ 考虑深部环境（高围压、孔压）时，花岗岩的循环硬化行为是否依然显著？本试验可能为单轴，需三轴验证。

## Source Coverage
本页面基于 11 条提供的索引片段编写，覆盖了摘要、引言、方法、主要结果、讨论及工程意义的要点。缺失信息包括：具体加载速率、频率、是否施加围压、各温度点样本数及重复性、应力‑应变曲线全貌以外的定量数据，以及详细的统计分析。这些细节需查阅原文才能完善知识页 [未从索引片段中确认]。
