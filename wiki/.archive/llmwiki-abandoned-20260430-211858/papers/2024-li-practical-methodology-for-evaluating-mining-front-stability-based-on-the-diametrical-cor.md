---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2024-li-practical-methodology-for-evaluating-mining-front-stability-based-on-the-diametrical-cor"
title: "Practical Methodology for Evaluating Mining Front Stability Based on the Diametrical Core Deformation Technique."
status: "draft"
source_pdf: "data/papers/2024 - Practical Methodology for Evaluating Mining Front Stability Based on the Diametrical Core Deformation Technique.pdf"
collections:
  - "zotero new"
citation: "Li, Yizhuo, and Hani S. Mitri. \"Practical Methodology for Evaluating Mining Front Stability Based on the Diametrical Core Deformation Technique.\" *Minerals*, vol. 14, no. 385, 2024, https://doi.org/10.3390/min14040385. Accessed 2026."
indexed_texts: "9"
indexed_chars: "42461"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T14:18:50"
---

# Practical Methodology for Evaluating Mining Front Stability Based on the Diametrical Core Deformation Technique.

## One-line Summary
本研究提出了一种将直径岩心变形技术（DCDT）与三维数值模拟相结合的方法，用于评估地下矿山开采工作面的稳定性，并在加拿大魁北克省 Eleonore 金矿的一个通道工作面进行了演示 [Li 2024, pp. 1-2] [Li 2024, pp. 12-13]。

## Research Question
如何利用从开采工作面垂直钻取的岩心的直径变形数据，并结合数值模型，建立一套实用的工作面稳定性评估方法？[Li 2024, pp. 1-2]

## Study Area / Data
案例研究数据来自加拿大魁北克省北部的 Eleonore 金矿，该矿由 Newmont Corporation 拥有。研究在一段位于 530 水平、埋深约 530 m 的 access drift 工作面进行。从该工作面上钻取了一段金刚石钻头岩心，岩性为 wacke（瓦克岩）。岩心的完整部分（距工作面约 2.5 m 处）被用于进行 DCDT 测量。此外，收集了该区域 wacke 的完整岩石及岩体力学参数（见表1）。[Li 2024, pp. 2-3] [Li 2024, pp. 5-7]

## Methods
1. **岩心变形测量**：使用高精度定制装置沿岩心周向测量最大直径 \( d_{\text{max}} \) 和最小直径 \( d_{\text{min}} \) 的变化，以反映应力解除引起的弹性恢复。DCDT 基于线弹性假设：最大、最小直径方向分别对应局部主应力方向。[Li 2024, pp. 3-5]
2. **应力估计**：利用 DCDT 解析模型（式 2a–2c）和完整岩石弹性模量 \( E \)、泊松比 \( \nu \)，由直径变化反算垂直于钻孔轴平面内的主应力 \( \sigma_L \)、\( \sigma_l \) 和轴向应力 \( \sigma_x \) 共同作用下的原始状态。当 \( \sigma_x=0 \) 时首先估计工作面处的应力，后续结合数值模拟得到的三维应力状态进行更新。[Li 2024, pp. 5-7]
3. **三维数值模型**：使用 Rhino CAD 和 FLAC3D 建立包含 access drift 的 50 m × 50 m × 50 m 线弹性模型，边界条件为辊轴约束，考虑根据原位应力测量结果初始化的应力场，并将 \( \sigma_3^0 \) 方向按 DCDT 结果顺时针旋转 10°。通过灵敏度分析将工作面附近网格尺寸细化至 0.075 m。[Li 2024, pp. 7-8]
4. **损伤区建模**：因观察到岩心前 2.5 m 存在爆破诱发损伤，采用去应力爆破本构模型进行模拟，引入岩体破碎因子 \( \alpha=0.4 \) 和应力耗散因子 \( \beta=0.6 \)，并按式（3）~（5）修改损伤区的弹性模量、泊松比和应力张量。[Li 2024, pp. 8-9]
5. **应力调整迭代**：以 FLAC3D 在距工作面 2.5 m 处（完整岩心所在深度）计算出的应力 \( \sigma_L^C \)、\( \sigma_l^C \) 及其方向为目标，迭代调整初始主应力 \( \sigma_2^0 \)、\( \sigma_3^0 \) 的大小和方向，直至计算值与 DCDT 结果的差异在约 5% 以内。[Li 2024, pp. 9-12]
6. **稳定性评价**：在调整后的线弹性应力场基础上，采用 Hoek–Brown 破坏准则计算安全系数（FS）（强度与施加应力的比值，在 \( \sigma_1=\sigma_3 \) 的静水压力线上取值）。[Li 2024, pp. 12-13]

## Key Findings
- 该方法成功利用单段完整岩心的 DCDT 测量结果，结合数值迭代，获得与实测应力一致的三维应力分布，FLAC3D 与 DCDT 结果的差异不超过 5%。[Li 2024, pp. 9-12]
- 通过模拟前 2.5 m 的损伤区（α=0.4，β=0.6），并调整远场应力，可重现工作面附近的应力状态。[Li 2024, pp. 8-9] [Li 2024, pp. 9-12]
- 研究表明，DCDT 可以作为一种评估开采工作面稳定性的实用工具。[Li 2024, pp. 12-13]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 工作面处（σx=0）由 DCDT 估计的局部主应力 σL=25.0 MPa，σl=3.5 MPa。 | [Li 2024, pp. 5-7] | 使用 wacke 完整岩石的 E、ν（表1）；假设平面应力状态。 | 后续考虑 σx 后更新。 |
| 距工作面 2.5 m 处完整岩心的应力状态：FLAC3D 计算值 σL=26.3 MPa，σl=9.5 MPa，σx=12 MPa（迭代后）。 | [Li 2024, pp. 9-12] | 经过 5 次迭代调整远场应力。 | DCDT 值与 FLAC3D 结果差异约 ≤5%。 |
| 损伤区采用 α=0.4，β=0.6 的去应力本构模型。 | [Li 2024, pp. 8-9] | 参数选自文献 [13]；损伤深度设定为 2.5 m（岩心破碎段长度）。 | 用于模拟先前爆破造成的岩体劣化。 |
| 三维数值模型（FLAC3D）经过网格灵敏度分析，工作面附近细化至 0.075 m，共 929,042 个单元。 | [Li 2024, pp. 7-8] | 线弹性模式；初始应力场根据原位测量结果转动 10°。 | 位移记录收敛。 |
| 岩心取自 Eleonore 矿 530 水平 access drift，岩性为 wacke。 | [Li 2024, pp. 2-3] [Li 2024, pp. 3-5] | 金刚石钻头垂直于工作面钻取。 | 部分岩心因爆破破碎。 |

## Limitations
- 单一的岩心测量点不足以充分代表整个工作面的应力变化；片段明确指出需要更多岩心来改善应力估计。[Li 2024, pp. 7-8]
- 损伤区参数（α=0.4，β=0.6）直接取自先前研究，未在本研究中进行独立标定。[Li 2024, pp. 8-9]
- 稳定性分析所采用的安全系数计算方法（在静水压力线上取值）并非唯一方式，且阈值选择依赖于分析者。[Li 2024, pp. 12-13]
- 完整的稳定性分析结果（如安全系数等值线图、潜在破坏区域）未从索引片段中确认。

## Assumptions / Conditions
- 岩石在应力解除过程中表现为各向同性线弹性材料。[Li 2024, pp. 3-5] [Li 2024, pp. 5-7]
- 岩心的直径变形完全由原先地应力解除引起，且变形是可恢复的。
- 岩心钻取方向与工作面垂直，DCDT 推定的主应力位于垂直于钻孔轴的平面内。[Li 2024, pp. 3-5]
- 观察到的岩心破碎是由上一次爆破引起，可用去应力爆破本构模型及其经验参数描述。[Li 2024, pp. 8-9]
- 数值模型调整为线弹性、小变形分析；稳定性评价则采用 Hoek–Brown 破坏准则。
- 迭代调整中，当 FLAC3D 与 DCDT 的应力差异在 5% 以内时认为可接受。[Li 2024, pp. 9-12]

## Key Variables / Parameters
| Variable / Parameter | Description | Role | Source |
|----------------------|-------------|------|--------|
| \( d_{\text{max}}, d_{\text{min}} \) | 测量得到的岩心最大、最小直径 | DCDT 的输入 | [Li 2024, pp. 5-7] |
| \( d_o \) | 应力解除前的原始岩心直径 | 由式（2c）计算 | [Li 2024, pp. 5-7] |
| \( E, \nu \) | 完整岩石的弹性模量与泊松比 | 用于 DCDT 解析模型 | [Li 2024, pp. 5-7] |
| \( \sigma_L, \sigma_l \) | 垂直于钻孔轴平面内的局部主应力 | 待估计量 | [Li 2024, pp. 5-7] |
| \( \sigma_x \) | 沿钻孔轴方向的局部应力 | 从数值模型中获取 | [Li 2024, pp. 5-7] [Li 2024, pp. 12-13] |
| \( \sigma_2^0, \sigma_3^0, \theta^0 \) | 数值模型中初始化的远场主应力大小与方向 | 迭代调整变量 | [Li 2024, pp. 9-12] |
| \( \alpha, \beta \) | 岩体破碎因子与应力耗散因子 | 描述损伤区力学性质 | [Li 2024, pp. 8-9] |
| \( \text{FS} \) | 安全系数（强度/施加应力） | 稳定性指标 | [Li 2024, pp. 12-13] |

## Reusable Claims
1. **DCDT 应力反演**：在垂直于开挖面的钻孔中，若岩石为线弹性且已知其完整岩石弹性常数（\( E, \nu \)），测量岩心直径变化（\( d_{\text{max}}, d_{\text{min}} \)）后，可通过 DCDT 解析模型（式 2a–2c）估计垂直于钻孔轴平面内的主应力大小和方向，但前提是能获得该位置的轴向应力 \( \sigma_x \)。［证据：[Li 2024, pp. 5-7]］［限制：仅适用于线弹性各向同性岩石；需要高精度的直径测量；对于三维应力状态需结合数值方法获取 \( \sigma_x \)］
2. **数值模型迭代匹配约束**：当只有单点应力估计时，可通过调整数值模型中远场主应力的大小和方向进行迭代计算，使距工作面特定深度的应力状态（如主应力大小和方向）与 DCDT 结果匹配在 5% 以内，从而获得可用于稳定性分析的整个工作面应力分布。［证据：[Li 2024, pp. 9-12]］［限制：迭代收敛依赖初始值；单点匹配不能保证整个区域应力场的唯一性。］
3. **爆破损伤区的等效模拟**：若岩心前方存在已知深度的爆破损伤区（由破碎岩心段长度确定），可使用去应力爆破本构模型并设定参数 \( \alpha=0.4, \beta=0.6 \) 来模拟该区域的模量降级、泊松比修正和应力耗散。［证据：[Li 2024, pp. 8-9]］［限制：参数取自特定文献，推广到其他岩性或爆破条件时需要验证；损伤区近似为均匀区。］
4. **DCDT 与 Hoek–Brown 准则联合评估稳定性**：在通过 DCDT 和数值迭代获得可信的线弹性应力场后，可选择 Hoek–Brown 破坏准则进行工作面稳定性分析，其安全系数可通过静水压力线上的强度与应力比值简单估算。［证据：[Li 2024, pp. 12-13]］［限制：安全系数计算方法与分析者选择的阈值有关；未与其他准则对比。］

## Candidate Concepts
- [[Diametrical Core Deformation Technique]]
- [[mining front stability]]
- [[stress relief core deformation]]
- [[damage zone modelling]]
- [[destress blasting]]
- [[linear elastic stress analysis]]
- [[Hoek–Brown failure criterion]]
- [[factor of safety]]

## Candidate Methods
- [[diametrical core deformation measurement]]
- [[3D finite difference modelling (FLAC3D)]]
- [[iterative stress adjustment in numerical models]]
- [[damage zone parameterization (α, β)]]
- [[stress path matching with elastic model]]
- [[Hoek–Brown based stability assessment]]

## Connections To Other Work
- 本工作中使用的 DCDT 解析模型源自同一作者此前开发并验证的模型［Ref. 9 in original paper］。[Li 2024, pp. 5-7]
- 损伤区模拟所采用的“去应力面板”本构模型及其参数（α、β）引用自关于面板去应力的研究［Ref. 13］；修改泊松比的公式来自另一工作［Ref. 14］。[Li 2024, pp. 8-9]
- 除以上联系外，未从索引片段中确认与其他具体研究论文的直接对比或扩展关系。

## Open Questions
- 当只有一个岩心测点时，迭代调整得到的应力场的唯一性和代表性如何？是否需要更多的岩心数据加以约束？[Li 2024, pp. 7-8] 明确建议未来应钻取更多岩心进行验证。
- 损伤区参数（α=0.4，β=0.6）在其他岩性、不同爆破设计下的适用性如何？[Li 2024, pp. 8-9]
- 采用 Hoek–Brown 准则计算安全系数的具体阈值以及工作面破坏区域的分布未从索引片段中确认。
- 该方法对非线弹性或各向异性岩石的适用性尚未讨论。

## Source Coverage
本页所依据的索引片段共 9 段，来源于 PDF 的多个页面（pp. 1–13）。片段覆盖了论文的摘要、引言、案例研究描述（部分）、DCDT 测量与解析模型、数值模型建立、损伤区建模、应力调整迭代过程以及方法论总结。未包含：完整的原位地应力张量（式 1）、完整的表 1 数值、岩心直径原始测量数据表、详细的稳定性分析结果（安全系数等值线等）。因此，关于该方法最终稳定性结论的定量细节和模型验证的深入讨论无法从索引片段中完全确认。
