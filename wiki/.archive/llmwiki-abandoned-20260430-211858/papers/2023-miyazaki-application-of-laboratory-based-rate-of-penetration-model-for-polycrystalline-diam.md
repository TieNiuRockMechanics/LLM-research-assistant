---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-miyazaki-application-of-laboratory-based-rate-of-penetration-model-for-polycrystalline-diam"
title: "Application of Laboratory-Based Rate of Penetration Model for Polycrystalline Diamond Compact Bit to Geothermal Well Drilling."
status: "draft"
source_pdf: "data/papers/2023 - Application of laboratory-based rate of penetration model for polycrystalline diamond compact bit to geothermal well drilling.pdf"
collections:
  - "part3-2"
citation: "Miyazaki, Kuniyuki, et al. \"Application of Laboratory-Based Rate of Penetration Model for Polycrystalline Diamond Compact Bit to Geothermal Well Drilling.\" *Geomechanics and Geophysics for Geo-Energy and Geo-Resources*, vol. 9, no. 103, 2023, https://doi.org/10.1007/s40948-023-00644-x."
indexed_texts: "7"
indexed_chars: "32002"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T11:56:38"
---

# Application of Laboratory-Based Rate of Penetration Model for Polycrystalline Diamond Compact Bit to Geothermal Well Drilling.

## One-line Summary
基于实验室建立的考虑钻头磨损的机械钻速（ROP）模型，评估其对地热井现场PDC钻头钻井数据的适用性，验证了钻头性能随钻进长度呈指数衰减，并讨论了模型在现场应用中的有效条件与限制 [Miyazaki 2023, pp. 1-2].

## Research Question
实验室开发的PDC钻头ROP模型（Miyazaki et al. 2022）是否能够解释地热井场现场钻井数据？钻头磨损如何影响钻进速度？模型在现场应用中的适用范围与约束条件是什么？ [Miyazaki 2023, pp. 1-2, 8-9].

## Study Area / Data
现场数据来自日本地热区域进行的四次构造探井钻井测试（Field tests No.1至No.4），具体位置未从索引片段中确认。使用的PDC钻头分别记为Bit A、B、C和D。Bit A和B具有与实验室测试钻头相同的几何设计，Bit C和D则配备了防止主切削齿过度侵入岩石的备用切削齿，且后倾角不同 [Miyazaki 2023, pp. 4-5]。钻遇的岩石类型包括玄武岩、石英安山岩、英安岩等，在Field test No.3中推断钻遇了硬侵入玄武岩 [Miyazaki 2023, pp. 5-8, 8-9]。实验室性能评估采用了钻头前后测试（pretest和posttest）以及部分取心样的单轴抗压强度（UCS）测定 [Miyazaki 2023, pp. 5-8]。

## Methods
采用Miyazaki et al. (2022)提出的基于实验室磨损试验的ROP模型。该模型将ROP（u）表达为转速（N）、钻压（W）、岩石单轴抗压强度（Sc）和PCD层平均磨损体积（Vwd）的函数：
u = p0 · N · (W/Sc)^2 · exp(−γ · Vwd)   [Miyazaki 2023, pp. 2-4]。
定义钻头性能参数 p = u/N / (W/Sc)^2 = p0 · exp(−γ · Vwd)。该模型建立在完美清洁理论假设基础上，并经过五种岩石、总进尺98 m的实验室钻进试验标定 [Miyazaki 2023, pp. 2-4]。

现场应用中，通过记录钻进过程中的N、W、u随测量深度（MD）或钻进长度（Ld）的变化，并利用钻前和钻后实验室测试（pretest与posttest）获得的p值进行对比验证。模型有效性通过log p（或p的指数）随Ld的线性变化关系进行评判。同时分析了u/N与W的关系，得到Bingham指数b，并用最小二乘幂律近似拟合 [Miyazaki 2023, pp. 5-8]。现场测试中，p的衰减斜率γ’（指数衰减速率）被用来表征实际岩层研磨性对钻头性能的影响 [Miyazaki 2023, pp. 8-10]。

## Key Findings
- 在四次现场试验中，钻头性能参数p总体随钻进长度Ld呈指数衰减（即log p线性减小），表明模型能够恰当地描述由钻头磨损引起的ROP下降 [Miyazaki 2023, pp. 8-9]。
- 对于Bit C（Field test No.3），p的下降斜率在钻进硬侵入玄武岩时明显变陡，说明岩石研磨性越高，p衰减越快 [Miyazaki 2023, pp. 8-9]。
- 在部分层段，当PDC钻头的固有性能因岩屑输送效率低等原因未能充分发挥时，模型会偏离实际，例如Field test No.3中Ld≈38 m处p的瞬时下降被推断为钻压传递不充分所致（如键槽、岩屑床等） [Miyazaki 2023, pp. 8-9]。
- 实验室前后测试（pretest和posttest）获得的p初始值与最终值大致与现场p–Ld曲线的首尾对应，进一步验证了模型的一致性 [Miyazaki 2023, pp. 8-9]。
- Bingham指数b在本次研究中的所有钻头测试中均接近2，与Maurer完美清洁模型一致 [Miyazaki 2023, pp. 5-8]。

## Core Evidence Table

| Evidence                                                                                      | Source                          | Conditions                                                                         | Notes                                                                                   |
|-----------------------------------------------------------------------------------------------|---------------------------------|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| 现场p值随钻进长度呈指数下降，log p线性递减                                                 | [Miyazaki 2023, pp. 8-9]       | 均匀岩性且井眼充分清洁；Bit A不适用因岩性非均质                                  | Bit C在硬侵入玄武岩层段斜率变陡，证实岩石研磨性影响                                   |
| b值（u/N ∝ W^b）在前后实验室测试中均约为2                                                     | [Miyazaki 2023, pp. 5-8] 表1  | 四种PDC钻头，不同岩石类型                                                        | 符合Maurer (1962)完美清洁模型的预测                                                     |
| Bit B现场磨损极小，钻后u/N仍明显高于其他钻头，对应IADC磨损等级低                            | [Miyazaki 2023, pp. 5-8] 表1  | 钻进总进尺约20 m，岩性可能研磨性低                                               | 证实磨损较小时ROP基本维持                                                              |
| p在Ld≈38 m处出现瞬时大幅下降，但钻头磨损等级低、岩性无变化、泥浆正常                            | [Miyazaki 2023, pp. 8-9]       | 推断由钻压传递不充分（如键槽、岩屑床）引起                                       | 表明井下异常摩擦可导致模型偏差，并非钻头性能真值                                        |
| 模型中指数衰减系数γ’（现场衰减斜率）难以在钻前准确估计，需发展预测方法                        | [Miyazaki 2023, pp. 9-10]      | 该系数反映岩石研磨性，影响模型预测精度                                           | 作者明确建议未来研究方向                                                                 |

## Limitations
- 模型基于特定PDC钻头类型（8.5英寸，58个PDC切削齿，特定几何设计）的实验室数据构建，直接外推至其他设计、尺寸或不同厂家的钻头尚未验证 [Miyazaki 2023, pp. 2-4, 9-10]。
- 现场验证仅涉及日本地热地域的四个有限实例，岩石类型和钻井参数范围有限 [Miyazaki 2023, pp. 4-5]。
- 当PDC钻头固有性能因岩屑输送不良或其他井下条件而无法充分表达时，基于纯磨损的模型会高估ROP [Miyazaki 2023, pp. 8-9]。
- 参数γ’（现场衰减系数）依赖于岩石的原地研磨性，目前在钻前缺乏有效的定量预测方法，成为模型规划的瓶颈 [Miyazaki 2023, pp. 9-10]。
- 现场测试中某些瞬时ROP变化（如Bit C第38 m处）的原因仍未完全明确，仅作为推断 [Miyazaki 2023, pp. 8-9]。

## Assumptions / Conditions
- 模型假设钻进始终处于“完美清洁”条件，即u/N与(W/Sc)^2成正比，且该关系即使在出现磨损时依然成立 [Miyazaki 2023, pp. 2-4]。
- 岩石被处理为均匀介质，现场应用中假定钻进层段的岩石强度Sc可以用临近取心样的实验室测定值代表 [Miyazaki 2023, pp. 5-8]。
- 钻头磨损主要由PCD层体积磨损量Vwd表征，且磨损对ROP的影响通过指数衰减项体现 [Miyazaki 2023, pp. 2-4]。
- 现场测试时，钻压W、转速N和深度数据能够准确测量，且井眼清洁状态允许将模型偏差主要归因于钻头磨损。异常段（如键槽、岩屑床）被视为模型有效性的破坏条件 [Miyazaki 2023, pp. 8-9]。

## Key Variables / Parameters
- u：机械钻速（ROP） [Miyazaki 2023, pp. 2-4]
- N：转速 [Miyazaki 2023, pp. 2-4]
- W：钻压（WOB） [Miyazaki 2023, pp. 2-4]
- Sc：钻进岩石的单轴抗压强度（UCS） [Miyazaki 2023, pp. 2-4]
- Vwd：PCD层平均磨损体积，基于16个切削齿的鼻部和肩部测量 [Miyazaki 2023, pp. 2-4]
- p0：钻头开始磨损时的初始性能参数 [Miyazaki 2023, pp. 2-4]
- γ：实验室磨损效应系数（对Vwd的敏感性） [Miyazaki 2023, pp. 2-4]
- p = u/N / (W/Sc)^2：组合性能参数 [Miyazaki 2023, pp. 2-4]
- γ’（在讨论中引入）：现场p–Ld曲线的指数衰减斜率，反映岩石研磨性，未从索引片段中确认其具体公式编号，但作为关键现场参数讨论 [Miyazaki 2023, pp. 8-10]
- b：Bingham指数，u/N与W^b成正比；本研究案例中b ≈ 2 [Miyazaki 2023, pp. 5-8]

## Reusable Claims
1. 对于具有特定几何设计的PDC钻头，在钻屑清除充分且岩石类型相对均匀的条件下，其钻进性能参数p随累计钻进长度Ld呈指数衰减（p = p0,field · exp(−γ’ · Ld)）。该衰减速率γ’可作为现场岩石研磨性的替代指标，且实验室磨损模型的形式在现场尺度依然有效 [Miyazaki 2023, pp. 8-9]。**限制**：适用范围需针对8.5英寸级PDC钻头进行验证；γ’强烈依赖于现场岩石研磨性，目前不可根据钻井前信息可靠预测；当地层非均质或井眼清洁不良时，该关系可能被打破。

2. 对于所使用的PDC钻头，即使在磨损发展的情况下，现场观测的Bingham指数b仍保持在2左右，与Maurer的完美清洁理论一致，因此可以在模型中直接使用平方关系 (W/Sc)^2 [Miyazaki 2023, pp. 5-8]。**限制**：该发现基于有限的现场数据，且b值可能取决于钻头类型和岩石条件，该研究未覆盖b不等于2的场景。

3. 钻头前后实验室性能测试（pretest和posttest）获得的性能参数ppre和ppost，与现场p–Ld曲线的初值和终值相吻合，表明通过实验室标定可以锚定现场性能衰减的终点，进而辅助钻头寿命估算 [Miyazaki 2023, pp. 8-9]。**限制**：这种对标仅在岩性变化不大且钻井操作正常时成；如果出现推拉力传递异常等情况，现场初始p可能会明显低于ppre。

4. 当检测到ROP和p出现与磨损趋势不符的瞬时突降，且排除岩性变化、泥浆流量及钻头磨损的影响时，可作为井下异常摩擦（如键槽、岩屑床形成）的间接指示，从而为钻井风险管理提供信息 [Miyazaki 2023, pp. 8-9]。**限制**：该论断为基于排除法的推测，未经过多案例系统验证。

## Candidate Concepts
- [[Rate of Penetration (ROP)]]
- [[PDC bit]]
- [[Bit wear]]
- [[Polycrystalline diamond compact (PDC) cutter]]
- [[Rock abrasivity]]
- [[Geothermal well drilling]]
- [[Uniaxial compressive strength (UCS)]]
- [[IADC Dull Grading System]]
- [[Backup cutters]]
- [[Cuttings transport]]
- [[Key seating]]
- [[Cuttings bed]]
- [[Bit torque]]

## Candidate Methods
- [[Miyazaki et al. (2022) laboratory ROP model for PDC bits]]
- [[Maurer’s perfect-cleaning model]]
- [[Bingham’s ROP model and b-exponent]]
- [[Wi wear index (Mazen et al.)]]
- [[Torque-based wear detection (Karasawa et al.)]]
- [[Laboratory drilling test and pre/post comparison]]
- [[Least-squares power approximation for b]]
- [[IADC dull grading for worn volume assessment]]

## Connections To Other Work
- 本研究直接延续了 **Miyazaki et al. (2022) 的实验室磨损模型**，将该模型由实验室尺度推向现场地热井应用 [Miyazaki 2023, pp. 2-4]。
- 模型中的核心关系u/N ∝ (W/Sc)^2 植根于 **Maurer (1962) 的完美清洁理论**；本工作证实即使在钻头磨损发展后，该平方关系仍能保持 [Miyazaki 2023, pp. 2-4]。
- **Bingham (1964)** 通过大量数据提出了b指数的统计范围（0.9‑3.0），本研究中多个PDC钻头获得的b ≈ 2，为平方律模型提供了新的现场证据 [Miyazaki 2023, pp. 5-8]。
- 钻头磨损检测领域，**Karasawa et al. (2016)** 曾报告可通过扭矩定性感知磨损进展，但实际现场扭矩常混入钻柱摩擦，影响了其准确性；**Mazen et al. (2021)** 则发展出基于扭矩和切削面积的磨损指数Wi。本文的模型避开了扭矩测量，直接通过ROP-磨损体积关联进行定量预测 [Miyazaki 2023, pp. 4-5]。
- 关于PDC钻头在地热井中的应用推广，前人工作如 **Raymond et al. (2012)** 和 **Sabri et al. (2016)** 已报道过PDC钻头相较于常规钻头的性能优势，本研究提供的ROP模型预期能进一步优化这类经济性决策 [Miyazaki 2023, pp. 10]。

## Open Questions
- 现场衰减系数γ’的定量预测方法尚未建立，如何根据岩性、钻头设计及钻井参数在钻前合理估算γ’是一个关键缺口 [Miyazaki 2023, pp. 9-10]。
- 模型在不同尺寸、不同切削结构（如不同后倾角、备用切削齿配置）PDC钻头上的适用性范围仍需通过更多实验和现场测试验证 [Miyazaki 2023, pp. 9-10]。
- Field test No.3中在Ld≈38 m处无磨损迹象下的瞬时ROP跌落的确切物理机制，除键槽/岩屑床外是否还有其他因素，有待进一步诊断 [Miyazaki 2023, pp. 8-9]。
- 如何处理非均匀岩性地层中p–Ld的多段衰减以及岩性界面的影响，模型尚未形式化，需发展能够分区段或自适应调整的γ’方法 [Miyazaki 2023, pp. 8-9]。
- 本研究中使用的实验室磨损参数γ与现场衰减系数γ’之间的定量转换关系未给出，可能依赖于实际岩屑输送效率，需进一步研究。

## Source Coverage
本知识页依据Miyazaki et al. (2023) 论文的7个索引片段编写，覆盖了摘要、引言、方法（第2节ROP模型）、现场测试条件与结果（第3节）、讨论（第4节）以及结论部分。片段涵盖了论文的核心叙事主线，尤其是模型的数学形式、现场验证的主要发现和部分瓶颈。然而，**缺失的重要信息**包括：式(3)的具体表达式、现场测试详细的IADC磨损等级表格、实验室测试中岩石类型和强度的完整清单、p–Ld图的定性形状之外的量值标度等。此外，对γ’与岩石研磨性之间的相关性的深入讨论未被完全索引，约束了该关系可被复用的程度。已覆盖的片段偏向于结果与宏观验证，对实验细节和参数量化细节的覆盖有所不足，部分信息需结合原文图表才能完全再现。
