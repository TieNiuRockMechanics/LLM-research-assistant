---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2014-zhang-a-new-method-estimating-the-2d-joint-roughness-coefficient-for-discontinuity-surfaces"
title: "A New Method Estimating the 2D Joint Roughness Coefficient for Discontinuity Surfaces in Rock Masses."
status: "draft"
source_pdf: "data/papers/2014 - A new method estimating the 2D Joint Roughness Coefficient for discontinuity surfaces in rock masses.pdf"
collections:
  - "zotero new"
citation: "Zhang, Guangcheng, et al. \"A New Method Estimating the 2D Joint Roughness Coefficient for Discontinuity Surfaces in Rock Masses.\" *International Journal of Rock Mechanics and Mining Sciences*, 2014."
indexed_texts: "8"
indexed_chars: "35819"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T18:47:07"
---

# A New Method Estimating the 2D Joint Roughness Coefficient for Discontinuity Surfaces in Rock Masses.

## One-line Summary
提出一种基于均方根方法的新粗糙度指标 λ 并结合逻辑函数，以更准确地估算岩体不连续面的二维 Joint Roughness Coefficient (JRC) [Zhang 2014, pp. 1-1].

## Research Question
如何更准确地估算岩体不连续面的二维 Joint Roughness Coefficient (JRC)，以改善不连续面剪切强度和导水开度的计算？现有方法忽略了剪切方向、节理面尺度、起伏角和起伏幅度等多种因素的组合效应 [Zhang 2014, pp. 1-3; Zhang 2014, pp. 6-8].

## Study Area / Data
本研究中使用的数据包括：
- 10条标准不连续面剖面 [Zhang 2014, pp. 5-6].
- Bandis [37] 数字化后的 64 条节理剖面 [Zhang 2014, pp. 5-6].
- 来自文献 [20, 38, 39, 40, 41] 的节理剖面数据，用于验证模型 [Zhang 2014, pp. 5-6; Zhang 2014, pp. 6-8].
未从索引片段中确认研究区域的具体地理位置或地质背景。

## Methods
1. **粗糙度指标 (λ)**：提出一个基于均方根 (Root Mean Square) 方法的新指标 λ。该指标考虑了起伏的倾斜角、幅度及其方向 [Zhang 2014, pp. 1-1]。λ 的计算结合了 h（平均高度）、L（轮廓长度）以及一个常数 α（取值为 1/3）[Zhang 2014, pp. 5-6].
2. **平均高度 (h) 计算**：通过定位最高点和最低点之间的平均值线来确定平均高度 h。计算过程包括迭代搜索，使通过参考线的平均垂直距离（式 8）最小化 [Zhang 2014, pp. 3-5].
3. **逻辑函数拟合**：在 λ 与 JRC 之间建立了逻辑函数关系（式 13-15），用于估算 JRC 的建议值、上界值和下界值 [Zhang 2014, pp. 5-6]。
4. **验证与比较**：将新方法估算的 JRC 和剪切强度与文献数据以及 `Z2` 方法的结果进行比较 [Zhang 2014, pp. 6-8]。

## Key Findings
1. 提出的粗糙度指标 λ 能够精确地确定 JRC 值，其结果优于一些现有方法，有助于更准确地估计不连续面的剪切强度和导水开度 [Zhang 2014, pp. 1-1].
2. 研究建立了基于 λ 计算 JRC 上界、建议和下界值的三个公式 [Zhang 2014, pp. 1-1].
3. 发现 `Z2` 方法会高估 JRC 值，从而导致在法向应力较高时对岩石节理剪切强度的估算失败，而新提出的方法则能计算出更准确的剪切强度值 [Zhang 2014, pp. 6-8].
4. JRC、剪切强度和力学开度与导水开度之比 (E/e) 对 λ 的敏感性趋势相似 [Zhang 2014, pp. 1-1].

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| `Z2` 方法在较高法向应力下未能准确估算岩石节理剪切强度，因为它高估了 JRC 值。 | [Zhang 2014, pp. 6-8] | 与文献数据进行比较。 | 新提出的粗糙度指数能计算出更准确的剪切强度值。 |
| 提出的粗糙度指数公式 λ = (h/L) * (α * (Z2)^2 / (1 - α))，其中 α = 1/3。 | [Zhang 2014, pp. 5-6] | α 值来自曲线拟合。 | 此公式结合了未明确指出的 `Z2` 参数。 |
| 建立了 λ 与 JRC 之间的一般逻辑函数关系：`JRC_suggested = 40 / (1 + e^(-20λ)) - 20`。 | [Zhang 2014, pp. 5-6] | 基于 Bandis [37] 的 64 个数字化剖面数据拟合得到。 | JRC 的上下界计算公式也在 Eq. 15 中给出。 |
| 所提方法在验证中表现出高精度，例如对 Grasselli and Egger [38] 的 100mm 剖面（JRC=20, λ=0.148），估算的 `JRC_suggested` 为 18.0，`JRC_upper` 为 19.5，`JRC_lower` 为 16.1。 | [Zhang 2014, pp. 6-8] | 对比了多个文献来源的剖面数据。 | 表格中列出了部分比较结果。 |

## Limitations
未从索引片段中确认研究是否讨论了方法的局限性，例如在特定地质条件或缩放效应下的适用性。

## Assumptions / Conditions
未从索引片段中明确确认研究所依赖的假设或前提条件。

## Key Variables / Parameters
- **λ**: 提出的新粗糙度指数，结合了平均高度 (h)、剖面长度 (L) 和常数 α [Zhang 2014, pp. 5-6].
- **h**: 平均高度，定义为通过迭代过程找到的使平均垂直距离最小的均值线对应的高度 [Zhang 2014, pp. 3-5].
- **α**: 用于计算 λ 的常数，值为 1/3 [Zhang 2014, pp. 5-6].
- **JRC**: Joint Roughness Coefficient，用于计算岩石节理剪切强度的关键参数 [Zhang 2014, pp. 1-1].
- **τ**: 岩石节理的峰值剪切强度 [Zhang 2014, pp. 1-3].
- **σ_n**: 有效法向应力 [Zhang 2014, pp. 1-3].
- **φ_b**: 不连续面的基本摩擦角 [Zhang 2014, pp. 1-3].
- **E/e**: 力学开度与导水开度之比 [Zhang 2014, pp. 1-1].
- **logistic function**: 用于关联 λ 和 JRC 的数学函数 [Zhang 2014, pp. 5-6].

## Reusable Claims
1. **Claim**: 新提出的粗糙度指标 λ 比 `Z2` 方法能更准确地估算 JRC，尤其是在高法向应力条件下，因为 `Z2` 会高估 JRC。**Condition**: 准确估算岩石节理剪切强度。**Evidence**: [Zhang 2014, pp. 6-8].
2. **Claim**: JRC 与 λ 之间的关系可用特定的逻辑函数 `JRC = 40 / (1 + e^(-20λ)) - 20` 来描述，该函数并给出上下界误差带。**Condition**: 用于根据 λ 值估算 JRC。**Evidence**: [Zhang 2014, pp. 5-6].
3. **Claim**: 现有的节理粗糙度模型普遍忽略了剪切方向、节理面尺度、倾斜角和起伏幅度等因素的共同作用。**Condition**: 评估已有 JRC 模型的局限性。**Evidence**: [Zhang 2014, pp. 1-3].

## Candidate Concepts
- [[Joint Roughness Coefficient (JRC)]]
- [[shear strength of rock joints]]
- [[Root Mean Square]]
- [[fracture asperity]]
- [[hydraulic aperture]]
- [[2D discontinuity profiles]]
- [[logistic function]]

## Candidate Methods
- [[Root Mean Square (Z2) method for JRC estimation]]
- [[fractal approach (D) for roughness quantification]]
- [[Roughness profile index (Rp)]]
- [[logistic function fitting for JRC correlation]]

## Connections To Other Work
- 与 Barton [8] 的工作直接相关，使用了其提出的 JRC-JCS 剪切强度公式 [Zhang 2014, pp. 1-3; Zhang 2014, pp. 6-8].
- 与 Tse and Cruden [19] 和 Yang et al. [20] 的工作直接相关，比较或引用了他们基于 `Z2` 的 JRC 估算方法 [Zhang 2014, pp. 3-3; Zhang 2014, pp. 6-8].
- 与 Lee et al. [12] 和 Ge et al. [36] 的工作有关系，文中提到了基于分形维度 (fractal dimension) 的粗糙度量化方法 [Zhang 2014, pp. 3-3].
- 引用了 Bandis [37] 的数据来拟合 JRC 和 λ 的逻辑函数 [Zhang 2014, pp. 5-6].
- 使用了 Grasselli and Egger [38]， Odling [39]， Bakhtar and Barton [40]， Ozvan et al. [41] 等人的数据进行方法验证 [Zhang 2014, pp. 6-8].

## Open Questions
未从索引片段中确认作者提出的未来研究方向或开放性问题。

## Source Coverage
本页基于 8 个索引片段生成。这些片段涵盖了摘要、引言与文献综述的结尾部分、方法的核心步骤、关键公式、部分实验结果表格和完整结论。覆盖信息集中于所提方法及其验证结果，但可能缺失详细的实验设置、讨论部分以及对局限性的评述。部分公式（如 Eq. 10, 11）未在片段中给出，常数 α 的拟合细节也未在片段中完全展开。
