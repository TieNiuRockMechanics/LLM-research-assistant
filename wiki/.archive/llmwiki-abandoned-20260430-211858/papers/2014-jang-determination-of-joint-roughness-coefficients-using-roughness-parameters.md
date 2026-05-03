---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2014-jang-determination-of-joint-roughness-coefficients-using-roughness-parameters"
title: "Determination of Joint Roughness Coefficients Using Roughness Parameters."
status: "draft"
source_pdf: "data/papers/2014 - Determination of Joint Roughness Coefficients Using Roughness Parameters.pdf"
collections:
  - "粗糙裂隙渗流"
citation: "Jang, Hyun-Sic, et al. \"Determination of Joint Roughness Coefficients Using Roughness Parameters.\" *Rock Mechanics and Rock Engineering*, vol. 47, no. 6, 2014, pp. 2061-2073. doi:10.1007/s00603-013-0535-z."
indexed_texts: "9"
indexed_chars: "42558"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T18:56:12"
---

# Determination of Joint Roughness Coefficients Using Roughness Parameters.

## One-line Summary
本研究通过高精度数字化10条标准粗糙度剖面，建立了基于幂律方程的节理粗糙度系数（JRC）与多种粗糙度参数（统计参数、2D参数、分形维数）之间的高相关性（R² > 0.96）经验关系，并系统评估了采样间隔对这些参数和JRC估计值的影响。 [Jang 2014, pp. 1-2]

## Research Question
如何利用统计粗糙度参数、二维不连续面粗糙度参数及分形维数，精确、客观地确定岩石节理的节理粗糙度系数（JRC），并量化采样间隔对这些参数与JRC关系的影响？ [Jang 2014, pp. 1-3]

## Study Area / Data
本研究基于Barton和Choubey（1977）提出的10条标准粗糙度剖面。这些剖面源自对136个岩石节理试样的剪切试验，并为每条剖面分配了一个JRC范围。剖面岩性包括板岩、细晶岩、片麻岩（含白云母）、花岗岩、角岩（球粒状）和皂石等。 [Jang 2014, pp. 2-3]

## Methods
- **剖面数字化**：对10条标准粗糙度剖面以四种不同的采样间隔（0.1 mm， 0.5 mm， 1.0 mm， and 2.0 mm）进行精确数字化。 [Jang 2014, pp. 2-3]
- **参数计算**：
    - **统计参数**：计算了均方根一阶导数值 (Z₂)、结构函数 (SF) 和粗糙度剖面指数 (Rp, Rp-1)。 [Jang 2014, pp. 3-5]
    - **二维不连续面粗糙度参数**：采用了Tatone和Grasselli（2010）提出的方法，计算最大视倾角（θ*max）和无量纲参数（C）构成的参数 θ*max / (C+1)₂D。 [Jang 2014, pp. 7-8]
    - **分形维数 (D)**：使用分规法（divider method）测量分形维数，并对比了在分规“全范围”与“适宜范围”内回归计算D值的效果。同时分析了归一化截距 (a_n) 与JRC的关系。 [Jang 2014, pp. 8-10]
- **关系建立**：利用幂律方程（power law equation）形式 `JRC = a × (参数)^b + c`，对计算出的各粗糙度参数与JRC标准值进行回归分析，建立经验预测公式。 [Jang 2014, pp. 1-2]
- **对比验证**：将本研究建立的关系式与前人提出的经验公式（如Tse和Cruden 1979， Yu和Vayssade 1991， Maerz et al. 1990, Tatone和Grasselli 2010等）进行对比，评估预测准确性。 [Jang 2014, pp. 3-7]

## Key Findings
- **高相关性**：统计粗糙度参数（Z₂, SF, Rp-1）、二维不连续面粗糙度参数（θ*max / (C+1)₂D）和分形维数（D）均与JRC值存在良好的幂律相关性，相关系数（R²）超过0.96。 [Jang 2014, pp. 1-2]
- **异常剖面**：在所有关系中，第4条剖面（JRC 6–8）的估算值与标准JRC值的偏差均超过±5%，表明该剖面在统计上与其他剖面存在差异。 [Jang 2014, pp. 1-2]
- **分形参数计算方法论**：基于全部分规范围计算的分形维数（D）与JRC的相关性（R² = 0.990）优于仅在“适宜范围”内计算的D值（R² = 0.852），这与Kulatilake等人（1997）的论点相悖。归一化截距 (a_n) 同样与JRC值高度相关。 [Jang 2014, pp. 8-10]
- **采样间隔依赖性**：
    - Z₂, Rp-1, θ*max / (C+1)₂D 和 D 值均随采样间隔增大而减小。 [Jang 2014, pp. 1-2]
    - 结构函数 (SF) 值随采样间隔增大而急剧增加。 [Jang 2014, pp. 1-2]
    - 粗糙度参数并非独立于采样间隔，其与JRC值的具体关系取决于采样间隔。 [Jang 2014, pp. 10-12]
    - 建立的幂律方程在不同采样间隔下系数（a, b, c）和相关性（R²）均不同，使用错误采样间隔对应的关系式会导致JRC估算严重失准。 [Jang 2014, pp. 11-12]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| JRC与Z₂的幂律关系： `JRC = 55.58(Z₂)^0.573 - 10.38` (R² = 0.972, 采样间隔 0.5 mm) | [Jang 2014, pp. 4-5] | 对10条标准剖面以0.5 mm间隔数字化后计算。 | 第4条剖面偏差超过±5%。 |
| JRC与SF的幂律关系： `JRC = 73.95(SF)^0.266 - 11.38` (R² = 0.972, 采样间隔 0.5 mm) | [Jang 2014, pp. 5-7] | 对10条标准剖面以0.5 mm间隔数字化后计算。 | 第4条剖面偏差超过±5%；SF值随采样间隔增大剧增。 |
| JRC与Rp-1的幂律关系： `JRC = 65.9(Rp-1)^0.302 - 9.65` (R² = 0.973, 采样间隔 0.5 mm) | [Jang 2014, pp. 6-7] | 对10条标准剖面以0.5 mm间隔数字化后计算。 | 第4条剖面偏差超过±5%。 |
| JRC与θ*max/(C+1)₂D的幂律关系： `JRC = 5.30[θ*max/(C+1)₂D]^0.605 - 9.49` (R² = 0.978, 采样间隔 0.5 mm) | [Jang 2014, pp. 7-8] | 对10条标准剖面以0.5 mm间隔数字化后计算。从正反方向测量取平均值。 | 第4条剖面偏差超过±5%。 |
| JRC与分形维数D（全范围）的幂律关系： `JRC = 103.37(D-1)^0.300 - 8.54` (R² = 0.990) | [Jang 2014, pp. 9-10] | 使用分规法的全部范围进行回归计算D值。 | 相关性优于仅在“适宜范围”内计算D值的方法（R² = 0.852）。 |
| 各参数与JRC关系在不同采样间隔（0.1, 0.5, 1.0, 2.0 mm）下的幂律方程系数及R² | [Jang 2014, Table 2, pp. 11] | 统计参数、2D参数和分形维数均在四个采样间隔下单独拟合。 | R²普遍随采样间隔增加而提高，但D值的最高R²出现在0.5 mm间隔。 |

## Limitations
- **第4条剖面异常**：所有提出的关系对第4条标准剖面（JRC 6–8）的预测误差均超过±5%，原因未完全明确，可能源于其统计特征的固有差异。 [Jang 2014, pp. 1-2]
- **二维方法局限性**：所有分析均基于二维剖面，未扩展到三维表面形貌。虽然使用了二维不连续面参数，但三维特征（如Grasselli和Egger 2003提出的方法）在本研究中未进行数字化和评价。 [Jang 2014, pp. 2-3]
- **采样间隔依赖性未完全解决**：研究揭示了JRC估算严重依赖采样间隔，并给出了不同间隔下的关系式，但这意味着在应用时必须明确测量采样间隔，且未提供一个能统一不同间隔的通用公式。 [Jang 2014, pp. 10-12]
- **分形参数方法论争议**：研究发现使用全分规范围计算分形维数效果更好，但这与部分前人研究（Kulatilake et al. 1997）结论相悖，其普适性需更多验证。 [Jang 2014, pp. 8-10]

## Assumptions / Conditions
- **标准剖面代表性**：假设Barton和Choubey（1977）的10条标准剖面能够充分代表自然界中岩石节理的粗糙度范围。 [Jang 2014, pp. 2-3]
- **目视估计基准**：标准剖面本用于视觉对比，本研究假设其背后通过反分析获得的JRC精确值（表1中括号内数值）是该研究的真实值基准。 [Jang 2014, pp. 3]
- **数学关系形式**：假定JRC与各粗糙度参数之间遵循幂律方程 (`JRC = a × P^b + c`) 形式。 [Jang 2014, pp. 1-2]
- **数字化精度**：研究基于高精度数字化剖面，其结果和结论的前提是数字化过程足够精确。 [Jang 2014, pp. 2-3]
- **二维剖面适用性**：整个方法学建立在二维剖面分析有效的基础上，认为从二维剖面提取的参数足以表征节理对剪切强度的主要贡献。 [Jang 2014, pp. 2-3]

## Key Variables / Parameters
- **JRC (Joint Roughness Coefficient)**：节理粗糙度系数，被预测量。 [Jang 2014, pp. 1]
- **Z₂**：均方根一阶导数, 反映粗糙度坡度。 [Jang 2014, pp. 3]
- **SF (Structure Function)**：结构函数, 反映粗糙度高度变化的程度。 [Jang 2014, pp. 3]
- **Rp (Roughness Profile Index)**：粗糙度剖面指数, 反映剖面实际长度。 [Jang 2014, pp. 3]
- **θ*max / (C+1)₂D**：二维不连续面粗糙度参数，由最大视倾角（θ*max）和无量纲拟合参数（C）构成。 [Jang 2014, pp. 7]
- **D (Fractal Dimension)**：分形维数，通过分规法在双对数图上由非平坦部分斜率求得。 [Jang 2014, pp. 8]
- **a_n (Normalized Intercept)**：归一化截距，由分规法分析中截距（log a）除以剖面名义长度得到。 [Jang 2014, pp. 8]
- **Sampling Interval (SI)**：采样间隔，数字化剖面时相邻数据点的水平距离（0.1， 0.5, 1.0, 2.0 mm）。 [Jang 2014, pp. 3]
- **公式中的回归系数 (a, b, c)**：幂律方程（`JRC = a × P^b + c`）中的系数，随粗糙度参数类型和采样间隔变化。 [Jang 2014, pp. 2]

## Reusable Claims
- **Claim 1**: 对于通过视觉对比法估计JRC时所使用的10条标准剖面，可以使用幂律方程 `JRC = a × P^b + c` 将统计或二维粗糙度参数（P）转换为JRC值，该类方程的决定系数（R²）普遍高于0.96。证据：基于0.5 mm采样间隔数据，Z₂, SF, Rp-1, θ*(max)/(C+1)₂D参数均达到此精度。 [Jang 2014, pp. 1-2, 4-8] 限制：此关系在第4条标准剖面上误差超过±5%。
- **Claim 2**: 使用分规法计算分形维数D与JRC的关系时，对分规跨距对数-长度对数图中所有数据点（全范围）进行回归获得的D值与JRC的相关性，优于仅在“非平坦段”（适宜范围）回归获得的D值。证据：全范围回归R² = 0.990，适宜范围回归R² = 0.852。 [Jang 2014, pp. 8-10] 限制：此发现与Kulatilake等人（1997）的结论相悖，其普适性未从索引片段中确认。
- **Claim 3**: JRC与粗糙度参数（Z₂, SF, Rp-1, θ*max/(C+1)₂D, D）的定量关系严重依赖于数字化剖面时所采用的采样间隔。使用与测量采样间隔不匹配的关系式会导致显著的JRC估算误差。证据：以Z₂为例，采用0.1 mm间隔测得的Z₂值代入0.5 mm间隔的公式，估算的JRC值与精确值及真值偏差巨大。 [Jang 2014, pp. 10-12]

## Candidate Concepts
- [[Joint Roughness Coefficient (JRC)]]
- [[Rock Joint Roughness]]
- [[Standard Roughness Profiles (Barton & Choubey 1977)]]
- [[Roughness Parameters]]
- [[Fractal Dimension]]
- [[Sampling Interval Effect]]
- [[Discontinuity Roughness]]
- [[Self-affine Fractal]]

## Candidate Methods
- [[Profile Digitization]]
- [[Statistical Roughness Parameter Calculation (Z2, SF, Rp)]]
- [[2D Discontinuity Roughness Parameter (Tatone & Grasselli 2010)]]
- [[Divider Method for Fractal Analysis]]
- [[Power Law Regression]]

## Connections To Other Work
- **Tse & Cruden (1979)， Yu & Vayssade (1991)， Tatone & Grasselli (2010)**：这些研究提出了JRC与Z₂、SF、Rp等参数的不同形式（线性、平方根、幂律）关系式。本研究引入的幂律关系基于0.5 mm采样间隔，预测效果优于Tse和Cruden的公式，与Yu和Vayssade及Tatone和Grasselli的公式精度相当，但在第4条剖面均出现偏差。 [Jang 2014, pp. 3-7]
- **Maerz et al. (1990)**：其提出的JRC与Rp-1线性关系在本研究的对比中，产生较大误差。 [Jang 2014, pp. 5-7]
- **Kulatilake et al. (1997)**：本研究关于分形维数应在分规全范围而非“适宜范围”内计算的发现，直接与Kulatilake等人的方法学建议相悖。 [Jang 2014, pp. 8-10]
- **概念关联 Candidate Concepts/Methods**：本研究的主题和方法可连接到[[scale effect]]（尺度效应）、[[fracture surface topography]] 表征、[[shear strength of rock joints]] 经验估算（如Barton-Bandis模型），以及[[signal processing]]和[[geostatistics]]在岩石力学中的应用。

## Open Questions
- 第4条标准剖面为何与所有拟合关系存在系统性、超过±5%的偏差？其独特的统计或分形特性根源是什么？ [Jang 2014, pp. 1-2]
- 在自然节理上，使用全部范围还是适宜范围计算分形维数才能得到与JRC最相关的结果，这一方法论争议是否具有普遍性？ [Jang 2014, pp. 8-10]
- 如何建立一个统一、独立于采样间隔的JRC估计框架，以避免对测量规范的严格依赖？ [Jang 2014, pp. 11-12]
- 本研究的结论和方法在多大程度上可以通过三维表面粗糙度参数分析得到改进或确认？未从索引片段中确认。

## Source Coverage
本页内容完全基于提供的9个索引片段，这些片段覆盖了论文的摘要、引言、方法、结果与讨论部分。覆盖范围相对全面，能够支撑对研究问题、方法、核心发现和主要局限性的描述。

但由于缺少全文，以下重要信息可能缺失或不够详尽：
- **引言部分**：对该领域更完整的历史回顾和理论背景。
- **实验细节**：高精度数字化的具体操作流程、设备和误差控制手段（仅从片段中得知使用了不同采样间隔）。
- **讨论部分**：可能包含对第4剖面异常更深入的机理分析，以及对与其他工作（如3D参数化）联系的更广泛讨论。
- **结论部分**：作者最终凝练的、更具概括性的研究发现陈述。
- **图表**：所有图表（Fig. 1-12）仅通过文字描述推断，具体数据和趋势的可视化信息缺失。
