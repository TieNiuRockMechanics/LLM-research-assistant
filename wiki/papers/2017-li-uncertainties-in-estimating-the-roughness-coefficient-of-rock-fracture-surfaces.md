---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2017-li-uncertainties-in-estimating-the-roughness-coefficient-of-rock-fracture-surfaces"
title: "Uncertainties in Estimating the Roughness Coefficient of Rock Fracture Surfaces."
status: "draft"
source_pdf: "data/papers/2017 - Uncertainties in estimating the roughness coefficient of rock fracture surfaces.pdf"
collections:
  - "zotero new"
citation: "Li, Yanrong, et al. \"Uncertainties in Estimating the Roughness Coefficient of Rock Fracture Surfaces.\" *Bulletin of Engineering Geology and the Environment*, vol. 76, 2017, pp. 1153-1165. doi:10.1007/s10064-016-0994-z."
indexed_texts: "8"
indexed_chars: "38509"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "38517"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.000208"
coverage_status: "full-index"
source_signature: "3806f849b05e42f5ec2955b67cf4c3dc4b161352"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T19:47:14"
---

# Uncertainties in Estimating the Roughness Coefficient of Rock Fracture Surfaces.

## One-line Summary

本文基于 223 条已发表的岩石节理剖面，系统研究了节理粗糙度系数(JRC)估算中的不确定性，发现部分统计参数对采样间隔敏感，而最大高度(Rz)、极限坡度(k)等不敏感；据此提出两组量化估算方程，并通过直剪试验验证；视觉对比法会系统性低估 JRC 约 2–3 个单位，文章据此更新了 Barton 标准剖面图并给出了视觉对比规则。

## Research Question

如何定量评估岩石节理粗糙度系数(JRC)估算中的两类不确定性：1) 量化方程中统计参数与分形维数对采样间隔的敏感性；2) 视觉对比法的主观偏差来源与程度。具体研究问题包括：哪些剖面参数对采样间隔(SI)不敏感？是否可建立考虑 SI 的普适估算方程？视觉对比法结果(JRCv)与量化结果(JRCe)的偏差范围及分布特征如何？如何改进标准剖面图以降低主观误差？

## Study Area / Data

研究数据为文献中收集的 223 条岩石节理剖面，JRC 值由原始研究者测定。剖面分为两组：
- 第一组：112 条剖面，JRC 通过直剪试验反算确定，来源包括 Barton 的 10 条标准剖面、Grasselli (2001) 的 12 条、Bandis et al. (1983) 的 26 条及 Bandis (1980) 的 64 条。这些剖面用于考察采样间隔对量化参数的影响。
- 第二组：111 条剖面，JRC 通过视觉对比获得，来源包括 Du (1995) 9 条、Beer et al. (2002) 3 条、Seidel 和 Haberfield (1995) 24 条、Grasselli (2001) 12 条、Vladimir 和 Tomas (2011) 4 条、Herda (2006) 8 条、Rasouli 和 Hosseinian (2011) 8 条、Jia (2011) 42 条及 Odling (1994) 1 条。用于评估视觉对比的不确定性。

剖面投影长度 68–167.8 mm，JRC 范围 0.4–20.0，岩性涵盖砂岩、灰岩、大理岩、花岗岩、片麻岩、板岩、辉绿岩、粉砂岩等，风化程度从新鲜到中等。剖面均通过 AutoCAD 从文献图像中重采样数字化，第一组以 0.1、0.2、0.4、0.8、1.6、3.2 mm 六种采样间隔(SI)数字化，第二组采用固定 SI = 0.4 mm。

验证用 23 个花岗岩张裂缝试样(120 mm × 120 mm)，取自花岗岩采石场，微风化、清洁表面，进行应变控制直剪试验(法向应力 500 kPa，剪切速率 0.3 mm/min)，JCS 由 Schmidt 锤测定。

## Methods

- **剖面数字化**：将文献剖面图像导入 AutoCAD，按原始比例尺校准，构建等间距垂直线，以交点创建多段线，导入自编程序计算统计参数和分形维数 D。该过程避免了像素分析法带来的厚度误差。
- **参数计算**（定义见附录）：
  - 统计参数：Z₂（一阶导数均方根）、ri（角度 i 标准差）、Rz（最大高度）、k（极限坡度，k = Rz/L）、δ（剖面伸长指数，δ = (Lt - L)/L）
  - 分形维数：Dc（圆规走动法确定）、Dₕ₋ₗ（斜边法确定）
- **采样间隔敏感性分析**：绘制各参数与 JRC 的线性和幂函数相关关系随 SI 的变化，考察常数 a、b 及相关系数 R 的 SI 依赖性。
- **多变量回归**：对敏感参数 δ、ri，以 SI 为第二变量进行回归，建立形式 JRC = a·δ^b·SI^c 的方程；对不敏感参数 k、Rz、Dₕ₋ₗ 直接建立幂律关系。最终推荐两组方程：(1) 考虑 SI 的方程 Eq. 1 (δ)、Eq. 2 (ri)；(2) 独立于 SI 的幂律方程 Eq. 3 (k)、Eq. 4 (Rz)、Eq. 5 (Dₕ₋ₗ)。
- **方程验证**：使用自主研发的便携式测量装置（激光传感器扫描节理面，计算五种参数的 JRC 值并取平均），对 23 个试样预估峰值剪切强度 sₑ，与直剪试验结果 sₜ 对比，计算相对误差 dₑ = |sₑ - sₜ|/sₜ × 100%。
- **视觉对比不确定性评价**：计算第二组 111 条剖面的 JRCₑ（由 Eq. 1–5 得到），统计偏差 c = JRCᵥ - JRCₑ 的分布，分析 |c| 大于 6 的特例，归因于剖面主趋势和标准剖面范围局限。
- **视觉对比图改进**：去除标准剖面主趋势（最小二乘直线水平化），增加 y 轴比例尺及 Rz 值，提出视觉对比基本规则。

## Key Findings

1. 参数 Z₂、ri、δ、Dc 与 JRC 的关系对采样间隔敏感（SI 减小时相关曲线向右、变缓），而 Rz、k、Dₕ₋ₗ 几乎不受 SI 影响，因为 Rz 反映最大高度，k 为 Rz 与投影长度之比，Dₕ₋ₗ 仅依赖峰谷信息。
2. 提出考虑 SI 的方程：JRC = a·δᵇ·SI⁻⁰.²²⁵⁶ (R = 0.8956) 和 JRC = a·(ri)ᵇ·SI⁻¹.⁰⁰⁶⁶ (R = 0.8813)。同时给出独立于 SI 的幂律方程：JRC = 80.37·k⁰.⁶²³⁸ (R = 0.8158)；JRC = 4.6836·Rz⁰.⁶¹⁰⁶ (R = 0.8115)；JRC = 92.709·(Dₕ₋ₗ - 1)⁰.³⁷⁷ (R = 0.8493)。
3. 直剪试验验证：23 个样本中，71% 的相对误差小于 10%，88% 小于 15%，最大误差 23%，表明所提方程能可靠估算节理峰值抗剪强度。
4. 视觉对比偏差：c 呈正态分布，均值约 -2.9，范围 -15 至 8；约 63.4% 的 |c| > 2，11.5% > 8。表明视觉对比系统性低估 JRC 约 2 个单位。
5. 偏差原因：(1) 剖面存在非水平主趋势，去除趋势后视觉对比更接近高 JRC 标准剖面；(2) 标准剖面集范围有限，某些剖面超出其涵盖范围。
6. 更新 Barton 标准剖面图：所有剖面主趋势水平化，添加 y 轴比例尺及 Rz 值；提出视觉对比规则：对比前去除剖面主趋势，若无明显匹配则以 Rz 为主要判据。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| δ 与 JRC 的线性/幂函数关系随 SI 减小右移且变缓；常数 a、b 在不同 SI 下变化 | Li 2017, pp. 3-5, Fig. 2 | 第一组 112 条剖面，SI 0.1–3.2 mm | R 值不随 SI 系统变化 |
| ri 与 JRC 关系随 SI 变化类似 δ；线性相关中 a、b 先负后正，幂律 a、b 递减 | Li 2017, pp. 5-6, Fig. 3 | 同上 | R 保持较高水平 |
| Z₂、Dc 对 SI 极敏感，且范围狭窄(Z₂ 0–0.5, Dc 1.0–1.05)，难以与 SI 建立良好多变量回归 | Li 2017, pp. 5, Fig. 4 | 同上 | 多变量回归 R < 0.5 |
| k、Rz、Dₕ₋ₗ 基本不受 SI 影响，仅反映高阶起伏，其幂律相关性与敏感参数相当 | Li 2017, pp. 6, Fig. 5 | 同上 | 推荐用于工程实践 |
| 多变量回归得出 δ-SI 与 ri-SI 方程，相关系数分别为 0.8956 和 0.8813 | Li 2017, pp. 5, Eqs. 1-2 | 第一组数据 | a、b 表达为 SI 的函数 |
| 直剪试验验证：23 样本中 71% 误差 <10%，88% <15% | Li 2017, pp. 6-8, Fig. 9 | 花岗岩张裂缝，σₙ = 500 kPa | 采用五方程平均 JRC 预估强度 |
| 视觉对比偏差(c)正态分布，均值约 -2.9，63.4% 的 |c| >2 | Li 2017, pp. 8-10, Figs. 10-11 | 第二组 111 条剖面对比 |
| 去除主趋势后，JRCᵥ = 11 的剖面与 ISRM 18–20 匹配，对应 JRCₑ = 19.2 | Li 2017, pp. 10, Fig. 12 | Jia (2011) 剖面 | 说明主趋势导致低估 |
| 更新图：标准剖面水平化，增加 y 轴比例尺和 Rz 值 | Li 2017, pp. 10-12, Fig. 14 | – | 提供视觉对比指南 |

## Limitations

- 所有数字剖面均从文献图像重采样，尽管仔细处理，仍不可避免引入微小误差。
- 所提方程基于 SI 0.1–3.2 mm 的剖面数字化数据，在此范围外的数据应谨慎使用。
- 视觉对比不确定性分析基于 JRCₑ 由 Eq. 1–5 估算，方程本身也存在一定统计误差。
- 直剪试验验证样本数量有限(23 个)，且仅针对花岗岩张裂缝，其他岩性和节理类型有待进一步检验。
- 研究仅关注二维剖面粗糙度，未涉及三维表面特征。

## Assumptions / Conditions

- 原文献中 JRC 值（反算或视觉对比）被视为真实值用于回归和偏差分析。
- 数字化时各剖面按原始比例尺校准，采样点沿投影长度均匀分布。
- 统计参数和分形维数的计算定义依据附录中的公式，且假设剖面数据点等间距。
- 回归分析采用线性和幂函数两种形式，幂函数形式被推荐用于工程实践，因其过原点性质符合物理意义。
- 视觉对比偏差分析中，JRCₑ 取五个方程计算结果的平均值（在强度验证时），但分布统计是按单个参数方程分别给出。
- 验证试验的法向应力固定为 500 kPa，未探讨不同法向应力下方程适用性。

## Key Variables / Parameters

- **JRC**：节理粗糙度系数（0–20）
- **SI**：采样间隔（mm）
- **Z₂**：剖面一阶导数均方根
- **ri**：角度 i 的标准差（°）
- **Rz**：剖面最大高度（mm）
- **L**：剖面投影长度（mm）
- **k**：极限坡度（= Rz/L）
- **δ**：剖面伸长指数 [= (Lt - L)/L]
- **Dc**：圆规走动法分形维数
- **Dₕ₋ₗ**：斜边法分形维数
- **JRCᵥ**：视觉对比法估算的 JRC
- **JRCₑ**：经验方程估算的 JRC
- **c**：视觉对比偏差（c = JRCᵥ - JRCₑ）
- **JCS**：节理壁面抗压强度（由 Schmidt 锤测定）
- **sₑ**、**sₜ**：预估峰值抗剪强度和试验峰值抗剪强度
- **dₑ**：强度预估相对误差

## Reusable Claims

- [[采样间隔对粗糙度参数的影响]]：参数 Z₂、ri、δ、Dc 与 JRC 的定量关系对采样间隔敏感，而 Rz、k、Dₕ₋ₗ 不敏感（基于 112 条剖面，SI 0.1–3.2 mm）[Li 2017, pp. 3-6]。
- [[工程推荐方程]]：对于 SI 在 0.1–3.2 mm 范围内的剖面，可使用 JRC = 4.6836·Rz⁰.⁶¹⁰⁶ (R=0.8115) 或 JRC = 80.37·k⁰.⁶²³⁸ (R=0.8158) 或 JRC = 92.709·(Dₕ₋ₗ-1)⁰.³⁷⁷ (R=0.8493) 进行估算，这些方程对 SI 不敏感[Li 2017, pp. 6]。
- [[视觉对比系统误差]]：视觉对比法平均低估 JRC 约 2.9 个单位，偏差呈正态分布，63.4% 的绝对误差大于 2[Li 2017, pp. 8-10]。
- [[主趋势影响]]：剖面存在非水平主趋势是视觉对比低估 JRC 的重要原因之一，去除趋势后视觉对比与量化结果更为一致[Li 2017, pp. 10]。
- [[标准剖面图更新]]：更新后的 Barton 标准剖面图将所有剖面的最佳拟合直线调整为水平，并增加了 y 轴比例尺和 Rz 值，以辅助视觉对比[Li 2017, pp. 10-12]。
- [[量化估算可靠性]]：基于所提方程的平均 JRC 值在预估峰值抗剪强度时，对花岗岩张裂缝有 88% 的样本误差小于 15%（法向应力 500 kPa 条件下）[Li 2017, pp. 8]。

## Candidate Concepts

- [[joint roughness coefficient (JRC)]]
- [[sampling interval (SI)]]
- [[visual comparison]]
- [[fractal dimension]]
- [[fracture surface roughness]]
- [[peak shear strength]]
- [[JRC-JCS model]]
- [[hypotenuse leg method]]
- [[compass-walking method]]
- [[profile elongation index]]
- [[ultimate slope]]
- [[maximum asperity inclination]]
- [[direct shear test]]
- [[strain-controlled direct shear]]

## Candidate Methods

- [[digitization of rock joint profiles from images]]
- [[hypotenuse leg (h-L) method for fractal dimension]]
- [[compass-walking method for fractal dimension]]
- [[multivariable regression considering sampling interval]]
- [[laser sensor scanning for joint roughness]]
- [[Schmidt hammer rebound hardness test]]
- [[trend removal by least square fitting]]

## Connections To Other Work

- 继承 Barton (1973) 和 Barton & Choubey (1977) 的 JRC 概念及标准剖面，提出视觉对比法的改进。
- 与 Tse & Cruden (1979)、Yu & Vayssade (1991)、Tatone & Grasselli (2010, 2013) 等关于统计参数 Z₂、ri 与 JRC 相关性的研究衔接，指出采样间隔的影响是这些方程差异的主要原因之一。
- 基于 Li & Zhang (2015) 和 Li & Huang (2015) 的综述，前者探讨统计参数与 JRC 的关系，后者探讨分形维数与 JRC 的关系，本文整合并拓展了 SI 敏感性分析，提出新的联合方程。
- 与 Grasselli & Egger (2003)、Gao & Wong (2015) 等三维粗糙度表征工作对比，指出二维参数的局限，但未深入三维分析。
- 引用 Barton & Choubey (1977) 的 JRC-JCS 模型计算峰值抗剪强度用于方程验证。

## Open Questions

- 所提方程在 SI 0.1–3.2 mm 以外的数字化数据上的适用性尚未检验。
- 方程对除花岗岩张裂缝以外的节理类型（如剪切节理、充填节理）的预测能力如何？
- 能否将二维剖面参数与三维表面粗糙度参数关联，进一步提升预测精度？
- 新增的 Rz 尺度作为视觉对比辅助判据的有效性在现场应用中是否足够稳健？
- 视觉对比偏差的分布是否受用户经验影响，能否通过标准化培训降低误差？

## Source Coverage

本文档完全基于原始论文的 8 个非空索引片段编写。所有片段均已处理，无遗漏。覆盖指标：
- indexed texts: 8
- indexed chars: 38,509
- nonempty source blocks: 8
- compiled source blocks: 8
- compiled source chars: 38,517
- coverage ratio by blocks: 1.0
- coverage ratio by chars: 1.000208
- source signature: 3806f849b05e42f5ec2955b67cf4c3dc4b161352
- coverage status: full-index
- compile strategy: single-pass-markdown

未使用任何片段外的作者、页码、数据或结论。所有的推论均明确基于所提供片段中的证据。
