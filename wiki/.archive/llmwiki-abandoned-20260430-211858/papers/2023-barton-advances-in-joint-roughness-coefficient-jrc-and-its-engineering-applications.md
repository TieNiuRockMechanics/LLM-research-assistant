---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-barton-advances-in-joint-roughness-coefficient-jrc-and-its-engineering-applications"
title: "Advances in Joint Roughness Coefficient (JRC) and Its Engineering Applications."
status: "draft"
source_pdf: "data/papers/2023 - Advances in joint roughness coefficient (JRC) and its engineering applications.pdf"
collections:
  - "zotero new"
citation: "Barton, Nick, et al. \"Advances in Joint Roughness Coefficient (JRC) and Its Engineering Applications.\" *Journal of Rock Mechanics and Geotechnical Engineering*, vol. 15, 2023, pp. 3352-79, doi:10.1016/j.jrmge.2023.02.002. Accessed 2026."
indexed_texts: "32"
indexed_chars: "157612"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T11:50:11"
---

# Advances in Joint Roughness Coefficient (JRC) and Its Engineering Applications.

## One-line Summary
本综述系统回顾了节理粗糙度系数（JRC）的起源、内涵、测量方法、估计技术、粗糙特性研究及其在岩石工程中的广泛应用，并讨论了试样代表性与采样间距问题 [Barton 2023, pp. 1-1]。

## Research Question
如何全面梳理 JRC 的概念、测量与估计方法、基于 JRC 的节理性质描述、对岩体性质的影响及其工程应用，并展望发展趋势？[Barton 2023, pp. 1-1]

## Study Area / Data
不涉及特定地理研究区。本文为综述，数据来源于文献中大量岩石节理测试结果，包括 Barton 和 Choubey (1977) 测试的 136 条天然节理（每条 3 个剖面，共 390 个剖面）、Barton 早期模型材料试验、Bandis (1980) 等的大尺度节理测试，以及众多 JRC 估计方法研究 [Barton 2023, pp. 1-2, 5-7, 8-9]。

## Methods
综述整合了以下 JRC 估计与粗糙度测量方法：
- **视觉比较法**：将实测剖面与 Barton 和 Choubey (1977) 的 10 条典型剖面比对，给出大致 JRC 范围，被 ISRM 推荐用于小尺度粗糙度表征，但被认为具有主观性 [Barton 2023, pp. 5-7]。
- **试验反算法**：通过直接剪切试验获得峰值强度包线，代入 JRC-JCS 准则（式 10）反算 JRC，反算时建议最大允许总摩擦角不超过 70° [Barton 2023, pp. 7-8]。
- **倾斜试验**：利用自重滑动时的倾斜角 α，结合 φr 估算 JRC；试验方向可反映粗糙度的方向性 [Barton 2023, pp. 1-2, 7-8]。
- **振幅/长度（a/L）法**：针对野外大尺度节理，基于剖面最大振幅 a 与长度 L 的比例估算尺寸校正后的 JRC，公式为 `JRC = k·a/L`（k 分别为 400、450、500 对应 L=0.1m、1m、10m）[Barton 2023, pp. 8-9]。
- **粗糙度测量仪器**：包括剖面梳（分辨率 0.25 mm）、滚轮/触针式轮廓仪、手持机械轮廓仪（Du, 1992），以及摄影测量、结构光扫描等非接触方法 [Barton 2023, pp. 5-5, 5-7]。

## Key Findings
- JRC 并非仅反映二维粗糙度的主观参数；倾斜试验能体现真实的三维粗糙度及剪切方向性 [Barton 2023, pp. 1-2]。
- JRC 对给定节理大致为常数，可在五个数量级的应力范围内保持稳定，甚至可外推至八个数量级的脆性行为范围 [Barton 2023, pp. 8-9]。
- 视觉比较法因主观性易产生偏差，但仍被 ISRM 采纳；存在大量基于拓扑描述或三维激光扫描的复杂 JRC 评价方程，但对工程应用而言成本与实用性受限 [Barton 2023, pp. 1-2, 5-7]。
- 振幅/长度法提供了考虑尺度效应的 JRC 估计途径，且应使用野外实际块体尺寸进行推拉试验以覆盖更高粗糙度的节理 [Barton 2023, pp. 8-9]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 倾斜试验测得的 JRC 反映节理的真实三维粗糙度和方向性 | [Barton 2023, pp. 1-2] | 节理未风化或风化程度已知；滑动方向与试验一致 | 许多研究者误认为 JRC 只反映二维粗糙度 |
| JRC 可通过直接剪切试验反算获得，反算时建议 arctan(τ/σn) 不超过 70° | [Barton 2023, pp. 7-8] | 需要获取足够的代表性试样；避免同一样本多次剪切 | 多次剪切会引入虚假“黏聚力”并使强度包络线顺时针旋转 |
| 振幅/长度比公式 JRC = 400a/L (L=0.1m)，450a/L (L=1m)，500a/L (L=10m) | [Barton 2023, pp. 8-9] | a 为最大振幅，L 为试样长度；基于约 200 条不同长度剖面及模型节理试验 | 强调了“岩石块体尺寸”对尺度效应的重要性 |
| 剖面梳实际分辨率为 0.25 mm，可满足节理粗糙度测量需求 | [Barton 2023, pp. 5-5] | 梳齿间距约 4 个/mm；测量范围一般不超过 400 mm | 较大采样间距会使表面变平滑，丢失细部起伏信息 |
| 基本摩擦角 φb 需在光滑、无任何可见尺度的粗糙组分的未风化岩石表面测量 | [Barton 2023, pp. 4-5] | 表面如锯切面或岩心，无脊状起伏；可获得残余剪切试验值或文献推荐值 | φb 反映平面表面的矿物学性质 |

## Limitations
- 视觉比较法具有主观性，可能引起 JRC 估计偏差，尤其在不同评估者之间 [Barton 2023, pp. 5-7]。
- 剖面梳等接触式量测仪器量程有限（通常不超过 400 mm），对大尺度节理粗糙度的测量能力受限 [Barton 2023, pp. 5-5]。
- 多次重复剪切同一样本会累积损伤，导致有效摩擦角下降并引入虚假黏聚力，需严格避免 [Barton 2023, pp. 7-8]。
- 未从索引片段中确认本文对摄影测量、结构光扫描等非接触方法的具体精度与适用限制的深入讨论 [Barton 2023, pp. 5-5]。

## Assumptions / Conditions
- JRC 估计所用节理试样需具有代表性，且不应使用重复剪切的同一样本 [Barton 2023, pp. 7-8]。
- 振幅/长度比法基于大量模型试验和特定长度（0.1 m, 1 m, 10 m）的推导，外推到中间尺度时需谨慎 [Barton 2023, pp. 8-9]。
- JCS（节理壁单轴抗压强度）和 φb（或 φr）可较准确获得后，JRC 成为剪切强度估算中的主要未知量 [Barton 2023, pp. 4-5]。
- JRC 有效性建立在节理未风化或风化程度可定量评估的前提下（通过 JCS 与回弹值 r 等表述）[Barton 2023, pp. 2-4, 4-5]。

## Key Variables / Parameters
- **JRC**（Joint Roughness Coefficient）：节理粗糙度系数，值域通常 0–20 [Barton 2023, pp. 2-4, 5-7]。
- **JCS**（Joint wall Compressive Strength）：节理壁单轴抗压强度，未风化时节理等同于完整岩石的 sc [Barton 2023, pp. 2-4]。
- **φb**：基本摩擦角，未风化光滑平面摩擦角 [Barton 2023, pp. 4-5]。
- **φr**：残余摩擦角，可由 φb 与 Schmidt 回弹值 r 和 R 计算，φr = φb − 20° + 20(r/R) [Barton 2023, pp. 4-5]。
- **a**：剖面最大振幅，用于 a/L 法 [Barton 2023, pp. 8-9]。
- **L**：节理试样长度，用于 a/L 方法和尺寸校正 [Barton 2023, pp. 8-9]。
- **α**：倾斜试验中的临界滑动角 [Barton 2023, pp. 7-8]。
- **τ / σn**：剪应力与正应力比，用于反算 JRC 的约束条件 [Barton 2023, pp. 7-8]。

## Reusable Claims
1. JRC 通过倾斜试验获得时能反映节理的三维方向性粗糙度，而非仅二维剖面信息 [Barton 2023, pp. 1-2]。适用条件：试验方向与剪切方向一致，节理未风化或风化程度已知。
2. 同一样本重复进行直剪试验会使强度包线顺时针旋转，产生虚假的“黏聚力”，因此必须用多个代表性试样进行单次试验 [Barton 2023, pp. 7-8]。限制：多组试样须属于同一节理组。
3. 对于大尺度（1 m 或 10 m 长）节理，可采用振幅/长度比公式估计尺寸校正后的 JRC：JRC = 450a/L (L=1m) 或 JRC = 500a/L (L=10m) [Barton 2023, pp. 8-9]。前提：a 和 L 在现场真实块体或暴露面上测得。
4. JRC 在宽应力范围内基本为常数（实测可达五个数量级，外推达八个数量级），可用于从倾斜试验到推拉试验的适用范围外推 [Barton 2023, pp. 8-9]。注意：外推适用于脆性行为范围。
5. 剖面梳的有效分辨率约为 0.25 mm（对应于 1 mm 间距的四个可调薄片），能满足节理粗糙度测量需求，但较多研究者错误地假设其分辨率为 1 mm [Barton 2023, pp. 5-5]。适用条件：梳齿密排且操作正确。

## Candidate Concepts
- [[joint roughness coefficient (JRC)]]
- [[rock joint shear strength]]
- [[joint wall compressive strength (JCS)]]
- [[scale effect in rock joints]]
- [[basic friction angle]]
- [[residual friction angle]]
- [[roughness directionality]]

## Candidate Methods
- [[visual comparison method for JRC]]
- [[direct shear test back-calculation]]
- [[tilt test]]
- [[amplitude/length method]]
- [[profile comb measurement]]
- [[stylus profilometry]]
- [[photogrammetry for rock joints]]
- [[structured-light scanning]]
- [[push/pull test]]

## Connections To Other Work
- 本文提到 Tse and Cruden (1979)、Yu and Vayssade (1991)、Tatone and Grasselli (2010)、Kulatilake et al. (2006) 等学者提出了多种基于拓扑或激光扫描的复杂 JRC 估计方程，但片段中未具体比较或关联其适用性 [Barton 2023, pp. 1-2]。
- 视觉比较法源自 Barton and Choubey (1977)，而后被 ISRM 采纳为建议方法 [Barton 2023, pp. 5-7]。
- 剖面梳数字化的方法由 Özvan et al. (2014) 推动；Hencher and Richards (2015) 认为常规设备对整体节理刻画已足够；Du (1992) 开发了现场手持轮廓仪 [Barton 2023, pp. 5-5, 5-7]。
- 非接触测量领域可连接到 [[Buzzi and Casagrande (2018)]] 等摄影测量工作 [Barton 2023, pp. 5-5]。
- 大尺度试验方面连接到 Bandis (1980) 和 Bandis et al. (1981) 的模型节理复刻试验 [Barton 2023, pp. 8-9]。

## Open Questions
- 如何进一步提升 JRC 估计的客观性并降低工程应用成本仍未完全解决。
- 大尺度（>10 m）节理粗糙度的准确原位估计方法尚未成熟。
- 非接触扫描手段的大量数据如何与 JRC 准则有效对接仍需探索。
- 未来 JRC 相关方法在岩石工程中将如何进一步扩展和完善，仍属开放方向 [Barton 2023, pp. 1-1]。

## Source Coverage
本 Markdown 页依据所提供的 32 条索引片段中的 8 条直接内容撰写，片段主要涵盖引言、JRC 起源、测量仪器、估计方法（视觉比较法、直接剪切法、倾斜法、振幅/长度法）以及部分假设与条件。可能缺失部分包括：基于 JRC 的节理粗糙特性深入调查（第 5 节）、节理性质描述、对岩体特性的影响（第 6–7 节）、具体工程应用案例，以及关于采样间隔和试样代表性更详细的讨论。因此，本页对方法学与基本参数有较好覆盖，但对应用成果和统计数据覆盖不足。
