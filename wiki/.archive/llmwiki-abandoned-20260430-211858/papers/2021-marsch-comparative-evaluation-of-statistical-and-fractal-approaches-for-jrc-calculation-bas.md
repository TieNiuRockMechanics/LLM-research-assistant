---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-marsch-comparative-evaluation-of-statistical-and-fractal-approaches-for-jrc-calculation-bas"
title: "Comparative Evaluation of Statistical and Fractal Approaches for JRC Calculation Based on a Large Dataset of Natural Rock Traces."
status: "draft"
source_pdf: "data/papers/2021 - Comparative Evaluation of Statistical and Fractal Approaches for JRC Calculation Based on a Large Dataset of Natural Rock Traces.pdf"
collections:
  - "zotero new"
citation: "Marsch, Kristofer, and Tomas M. Fernandez-Steeger. \"Comparative Evaluation of Statistical and Fractal Approaches for JRC Calculation Based on a Large Dataset of Natural Rock Traces.\" *Rock Mechanics and Rock Engineering*, vol. 54, 2021, pp. 1897-1917. doi:10.1007/s00603-020-02348-0. Accessed 2026."
indexed_texts: "18"
indexed_chars: "87843"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T02:14:37"
---

# Comparative Evaluation of Statistical and Fractal Approaches for JRC Calculation Based on a Large Dataset of Natural Rock Traces.

## One-line Summary
基于六个不同岩石表面的超40,000条节理轮廓线，对比了统计参数（以$Z_2$为代表）和分形方法计算节理粗糙度系数（JRC）的可靠性，发现简单的$Z_2$参数足以确定JRC类别，而分形方法过于依赖特定计算程序且未提供更可靠的估计 [Marsch 2021, pp. 1-2]。

## Research Question
鉴于所有JRC数学相关性均参考Barton和Choubey的10条标准轮廓线，理论上同一任意轮廓应得出相同的JRC值，本研究旨在探究在评估大量非标准自然岩石轮廓线时，不同统计与分形计算方法的JRC结果是否一致 [Marsch 2021, pp. 1-2]。

## Study Area / Data
未从索引片段中确认具体研究区域。数据为六个不同岩石表面的超过40,000条节理轮廓线，覆盖广泛粗糙度类别 [Marsch 2021, pp. 1-2]。此外，使用了三种不同数字化方式生成的Barton和Choubey的10条标准轮廓线数据集进行方法敏感性评估 [Marsch 2021, pp. 2-3]。

## Methods
研究评估了统计方法和分形方法两大类JRC计算方法：
*   **统计方法**：采用$Z_2$参数（均方根一阶导数）作为代表，因其使用广泛且可比性强。计算式如下 [Marsch 2021, pp. 5-5]：
    $$Z_2 = \sqrt{\frac{1}{(N-1)(dx)^2} \sum_{i=1}^{N-1} (y_{i+1} - y_i)^2}$$
    JRC通过Tatone和Grasselli (2010) 提出的相关性计算 [Marsch 2021, pp. 5-5]。
*   **分形方法**：使用了三种定义不同的分形方法 [Marsch 2021, pp. 1-2]：
    1.  **RMS相关法 (RMS-COR method)**：计算不同顶点间隔（$dv$）下高度差（$dh$）的标准差（$\sigma(dh)$），在双对数坐标下拟合直线求取Hurst指数（$H$）作为斜率。采用Stigsson和Mas Ivars (2019)的$H$、$\sigma\delta h(dx)$与JRC的相关性，并补充了$H_{RMS} > 0.5$时的系统低估校正方程 [Marsch 2021, pp. 5-6]。
    2.  **功率谱分析法 (Power spectrum analysis)**：应用快速傅里叶变换(FFT)计算分形参数，并对计算得到的$H_{FFT,cal} > 0.7$进行线性校正 [Marsch 2021, pp. 6-8]。
    3.  **罗盘行走法 (Compass walking method)**：基于分形维数$D$计算JRC，使用了Turk et al. (1987)的线性相关性 [Marsch 2021, pp. 6-8]。

## Key Findings
*   **统计方法的一致性**：对于$Z_2$等统计参数，如果严格遵循1 mm采样间隔和去除趋势项等预处理步骤，即便来自不同的数字化数据集，分析结果也具有很好的可比性，$Z_2$对输入信号不敏感，是计算JRC的稳健方法 [Marsch 2021, pp. 8-9]。
*   **分形方法的分歧**：分形方法所得JRC严重依赖于特定的计算程序，不同的计算程序会导致不同的分形维数$D$或Hurst指数$H$，因此这些值不可互换 [Marsch 2021, pp. 5-5, 6-6]。
*   **方法有效性总结**：在评估大量非标准轮廓线时，即使参考同一标准轮廓线，不同方法（尤其是分形方法之间）得到的结果差异巨大，通常无法获得同等或令人满意的相似结果 [Marsch 2021, pp. 1-2]。分形理论对于稀疏、低分辨率的标准轮廓线而言过于复杂。分形方法并未比使用简单统计参数$Z_2$产生更安全、更可靠的粗糙度估计 [Marsch 2021, pp. 1-2]。
*   **统计参数的可互换性**：参数$\sigma_i$（高度均方根）、$SF$（结构函数）、$R_p$（粗糙度轮廓指数）与$Z_2$之间存在精确的传递函数（$R^2 \approx 1$），可以互换，因此$Z_2$可作为这四个参数的共同代表 [Marsch 2021, pp. 6-8]。
*   **预处理的重要性**：未进行预处理（去除趋势）的轮廓线数据计算出超出合理范围的JRC值（大于20），违背了标准轮廓线的JRC范围 [Marsch 2021, pp. 8-9]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 对于40,000+条自然岩石轮廓线，不同统计和分形方法计算出的JRC差异巨大。 | [Marsch 2021, pp. 1-2] | 数据来自六个覆盖广泛粗糙度类别的岩石表面。 | 证实了即使共同参考10条标准轮廓线，不同方法也得不到一致的JRC。 |
| $Z_2$、$\sigma_i$、$SF$、$R_p$之间存在决定系数$R^2 \approx 1$的精确传递函数，可以互换。 | [Marsch 2021, pp. 6-8] | 10条标准轮廓线。 | 使得$Z_2$可以作为多个统计参数的代理进行分析。 |
| 严格遵循1 mm采样和去趋势预处理后，$Z_2$值在不同数字化数据集间差异仅4%，对应JRC差异仅0.5。 | [Marsch 2021, pp. 8-9] | 对标准轮廓线的不同数字化数据集。 | 验证了统计方法在标准化预处理后的稳健性。 |
| 不同分形算法（如罗盘行走、盒计数等）计算出的标准轮廓线分形维数D不同，不可互换。 | [Marsch 2021, pp. 5-6] | 引用前人研究（Lee et al. 1990；Odling 1994）。 | 分形方法结果依赖于所选算法，是造成JRC结果不一致的根本原因之一。 |

## Limitations
*   **标准轮廓线的固有缺陷**：所有JRC相关性均基于Barton和Choubey(1977)的10条标准轮廓线，这些轮廓线仅以图形方式呈现，经打印缩小后损失信息，且原始数据由触针式轮廓仪采集，存在探针变形导致的间距变化，原始测量质量难以评估 [Marsch 2021, pp. 2-3]。
*   **标准轮廓线数字化差异**：不同研究者采用不同的数字化方法、采样间隔（0.05 mm至2.4 mm不等）和预处理步骤生成标准轮廓线数据集，导致输入变量不统一，影响了各相关性的可追溯性与可比性 [Marsch 2021, pp. 2-2]。
*   **分形方法的不适用性**：分形理论应用于低分辨率、稀疏的标准轮廓线时过于复杂，且方法本身存在系统偏差（如RMS相关法对Hurst指数的高估或低估） [Marsch 2021, pp. 1-2, 5-6]。
*   **研究范围**：未从索引片段中确认该方法在其他结构面或工程尺度的适用性。

## Assumptions / Conditions
*   **自仿射性前提**：所有基于分形理论的方法均基于一个根本假设，即岩石不连续面轮廓线具有自仿射（self-affine）而非自相似（self-similar）性质 [Marsch 2021, pp. 5-5]。
*   **采样间隔标准化**：JRC计算应以1 mm的采样间隔为默认标准，这与原始类型剖面数据的采集分辨率一致 [Marsch 2021, pp. 3-5, 5-6]。
*   **趋势去除**：为获得可比的结果，轮廓线数据在计算前必须去除整体趋势 [Marsch 2021, pp. 5-5, 6-6]。
*   **顶点间隔限制**：RMS相关法中，为减少轮廓线有限长度引起的非线性影响，用于拟合直线的顶点间隔$dv$应不超过轮廓总长度$L$的20% [Marsch 2021, pp. 8-9]。

## Key Variables / Parameters
*   **$JRC$**：节理粗糙度系数（Joint Roughness Coefficient），目标变量。
*   **$Z_2$**：均方根一阶导数，核心统计参数。
*   **$\sigma_i$**：高度均方根。
*   **$SF$**：结构函数。
*   **$R_p$**：粗糙度轮廓指数。
*   **$D$**：分形维数（Fractal dimension）。
*   **$H$**：Hurst指数。
*   **$\sigma\delta h(dx)$**：RMS相关法中的幅度参数，用于区分具有相同$H$的轮廓线。
*   **$dv$**：RMS相关法中的顶点间隔长度。
*   **$dx$**：采样间隔。

## Reusable Claims
*   **Claim 1**: 只要对轮廓线数据进行严格的去趋势和1 mm标准化采样预处理，统计参数$Z_2$就是一个对输入数据源不敏感的稳健JRC计算指标，可在不同数据集中得到可比的JRC结果。证据：对10条标准轮廓线不同数字化版本的分析结果显示，预处理后$Z_2$值的差异降至4%，对应JRC差异仅为0.5 [Marsch 2021, pp. 8-9]。限制：结论仅在被分析的标准轮廓线上验证，推广至其他非标准轮廓线时，稳健性的前提是严格遵守相同的预处理和采样标准。
*   **Claim 2**: 分形方法（如RMS相关法、罗盘行走法、谱分析法）在计算JRC时结果不具互操作性，因为不同算法得到的$D$或$H$值物理含义不同，不可直接比较或代入同一JRC相关公式。证据：不同作者对同一标准轮廓线计算得到的分形维数$D$值各异，导致JRC结果出现巨大分歧 [Marsch 2021, pp. 5-6]。条件：此结论适用于基于标准轮廓线建立的分形相关性。限制：未评估对三维表面或高分辨率扫描数据的分形分析。

## Candidate Concepts
*   [[Joint Roughness Coefficient (JRC)]]
*   [[Fractal Dimension (D)]]
*   [[Hurst Exponent]]
*   [[Self-Affinity]]
*   [[Shear Strength of Rock Joints]]

## Candidate Methods
*   [[Z2 Statistical Parameter]]
*   [[RMS-Correlation Method (RMS-COR)]]
*   [[Power Spectrum Analysis (FFT)]]
*   [[Compass Walking Method]]
*   [[Trend Removal Preprocessing for Profiles]]

## Connections To Other Work
*   本研究复现并引用了Tatone和Grasselli (2010)提出的 $Z_2$ 与 JRC 的相关性方程，并推荐其数字化数据集作为未来研究的参考 [Marsch 2021, pp. 3-5, 5-5]。
*   研究评估并修正了Stigsson和Mas Ivars (2019)基于RMS相关法的JRC相关性，并补充了Hurst指数校正公式 [Marsch 2021, pp. 5-6]。
*   讨论了分形方法时引用了Turk et al. (1987)的罗盘行走法研究及JRC线性相关性 [Marsch 2021, pp. 2-2, 6-8]，并提及Lee et al. (1990)和Odling (1994)等人计算了不同的分形维数$D$ [Marsch 2021, pp. 5-6]。
*   在文献回顾中提到了多种其他JRC确定方法，如[[支持向量回归]](Wang et al., 2017)、[[向量相似性度量]](Yong et al., 2018)、[[随机场理论]](Gravanis and Pantelidis, 2019)，但这些均未在本研究中作为主要评估对象 [Marsch 2021, pp. 2-2]。

## Open Questions
*   未从索引片段中确认所述结论是否适用于三维表面粗糙度评估。
*   未从索引片段中确认是否存在能适用于所有类型轮廓线的、算法无关的统一分形JRC评估框架。
*   尽管$Z_2$显示出稳健性，但在极端粗糙或极为平滑的岩石表面上其区分度和适用性未从索引片段中确认。

## Source Coverage
本页基于18个索引片段生成，其中12个片段提供了实质性信息（引文、主体章节文字、图表说明）。覆盖了论文的摘要、引言（数据基础问题）、方法（统计和三种分形方法）、部分结果（标准轮廓线再评估）。缺少关于6个岩石样本大规模应用部分的详细结果片段，以及讨论和最终结论的完整归纳。因此，在自然轮廓线上大规模应用的具体统计分析、图表结果和全面讨论方面的细节可能缺失。
