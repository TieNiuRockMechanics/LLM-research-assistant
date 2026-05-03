---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2025-meng-evaluation-of-the-diametrical-core-deformation-analysis-dcda-and-fracture-surface-morp"
title: "Evaluation of the Diametrical Core Deformation Analysis (DCDA) and Fracture Surface Morphology for In-Situ Stress Estimation."
status: "draft"
source_pdf: "data/papers/2025 - Evaluation of the Diametrical Core Deformation Analysis (DCDA) and Fracture Surface Morphology for In-Situ Stress Estimation.pdf"
collections:
  - "zotero new"
citation: "Meng, Qingsen, et al. “Evaluation of the Diametrical Core Deformation Analysis (DCDA) and Fracture Surface Morphology for In-Situ Stress Estimation.” *Rock Mechanics and Rock Engineering*, vol. 58, 2025, pp. 7363-76. doi:10.1007/s00603-025-04512-w. Accessed 2026."
indexed_texts: "12"
indexed_chars: "55641"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "55185"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.991805"
coverage_status: "full-index"
source_signature: "2f3dd5dfb20de8ea509bc001788ac53d3db50532"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T08:05:15"
---

# Evaluation of the Diametrical Core Deformation Analysis (DCDA) and Fracture Surface Morphology for In-Situ Stress Estimation.

## One-line Summary
在新疆北天山中段500 m深度的二长花岗岩中，利用岩芯直径变形分析（DCDA）和岩饼破裂面三维形貌定量化方法估算原位应力，所得应力值与水压致裂结果一致，且最小主应力方向可由破裂面形貌各向异性指示。 [Meng 2025, pp. 1-2; Meng 2025, pp. 12-13]

## Research Question
如何基于岩芯直径变形分析（DCDA）和岩芯破裂面形貌（core discing fracture surface morphology），在深部高地应力环境下高效、准确地估算原位应力的大小和方向，并与现场水压致裂测量结果进行对比验证。 [Meng 2025, pp. 1-2; Meng 2025, pp. 2-3]

## Study Area / Data
研究区位于中国新疆北天山、埋深约500 m的隧道水平钻孔DYL‑1，岩性为二长花岗岩（monzonitic granite）。 [Meng 2025, pp. 1-2; Meng 2025, pp. 5-7] 岩石基本力学参数见表1（密度2.62–2.69 g/cm³、平均弹模31.2 GPa、泊松比0.25、UCS平均72.0 MPa、抗拉强度平均3.75 MPa等）。 [Meng 2025, pp. 5-7] 现场水压致裂试验在三向正交钻孔（DYL‑1、DYL‑2、DYL‑3）中进行，给出主应力大小和方向：σ₁=26.05 MPa (358.56°/12.41°)；σ₂=21.34 MPa (91.45°/12.89°)；σ₃=15.01 MPa (226.07°/71.96°)。 [Meng 2025, pp. 5-7; Meng 2025, pp. 6-7, Table 2] 分析所用20块岩芯样品取自DYL‑1钻孔，多数发生岩饼化（core discing），厚度2–4 cm，未连续取样，无定向标志。 [Meng 2025, pp. 5-7]

## Methods
- **DCDA理论**：基于广义虎克定律和体积应变，考虑岩芯应力解除后的不等量膨胀，建立最大/最小岩芯直径（d_max、d_min）与差分应力、主应力方向的关系式；当钻孔轴向与一个主应力一致且Sz≈0时，可利用直径测量解算S_max与S_min。 [Meng 2025, pp. 3-5]
- **直径测量**：使用蔡司Spectrum 7106型坐标测量机（CMM）量测岩芯直径，最大分辨率1.2 μm，恒温（23℃）条件下，以5 mm/s扫描速度、0.5 N恒力沿圆周每隔5°采集数据，每条样品至少72个测点。通过最小二乘拟合得到d_max、d_min及其相对于参考线的方向。 [Meng 2025, pp. 5-7; Meng 2025, pp. 7-8]
- **破裂面形貌提取**：使用SIMSCAN 30三维激光扫描仪（最高分辨率0.02 mm，扫描分辨率0.4 mm），利用Rhino软件生成三角形网格，导入ArcGIS生成栅格表面并裁剪为直径48 mm的圆形区域，提取边缘高度分布和坡向（aspect）分布，并用周期180°的正弦曲线拟合。 [Meng 2025, pp. 7-8; Meng 2025, pp. 8-11]
- **应力计算与对比**：以E=30 GPa、ν=0.26代入公式计算对比；含参数敏感性分析。 [Meng 2025, pp. 8-11; Meng 2025, pp. 11-12]

## Key Findings
1. DCDA方法能有效获取平面内主应力差值与方向，应力大小总体与水压致裂结果相符（S_max均值29.03 MPa vs 26.05 MPa，S_min均值8.94 MPa vs 15.01 MPa）。 [Meng 2025, pp. 8-11; Meng 2025, pp. 11-12]
2. 剔除4个Δd>100 μm的异常样品后，剩余16个样品的Δd平均为48.9 μm，d_max与d_min分布稳定；用d_min代替d_0是合理的（用E=30 GPa、ν=0.26测算的d_0与d_min分布高度相似）。 [Meng 2025, pp. 8-11; Table 3; Fig. 6]
3. 岩芯破裂面的边缘高度分布与坡向分布均呈现周期180°的正弦特征（平均R²高度0.67，坡向0.76），其各向异性可指示应力方向；d_min方向与边缘高点方向偏差<12°，与坡向峰值方向偏差<15°，三者所指示的最小主应力方向一致。 [Meng 2025, pp. 11-12; Fig. 11, 12]
4. 岩石力学参数的变异性对应力估算影响显著：高估弹性模量E会高估应力，高估泊松比ν会低估应力；需准确评估局部岩石力学参数和各向异性才能获得可靠估算。 [Meng 2025, pp. 11-12; Fig. 7]
5. CMM（1.2 μm分辨率）能连续、准确地捕捉微米级直径变形，优于传统光学测微计和摄影测量方法，为DCDA提供可靠基础。 [Meng 2025, pp. 11-12]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 16个有效样品的Δd (d_max−d_min) 范围27.2–73.9 μm，均值48.9 μm | Table 3 [Meng 2025, pp. 8-11] | 排除Δd>100 μm的4个异常点；测量条件恒温23℃，CMM分辨率1.2 μm | 直径拟合R²>0.95，相邻可对齐样品d_max/d_min一致性好 |
| 依据E=30 GPa、ν=0.26估算的S_max均值29.03 MPa、S_min均值8.94 MPa | Table 3; Fig. 8 [Meng 2025, pp. 8-11] | 假设Sz≈0，用d_min代替d_0 | 与水压致裂实测S_max=26.05、S_min=15.01 MPa存在偏差 |
| d_min方向与破裂面边缘高点方向角差<12°，与坡向峰值方向角差<15° | Fig. 12 [Meng 2025, pp. 11-12] | 无定向岩芯，仅比较相对方向 | 正弦拟合R²高度0.67，坡向0.76 |
| 参数敏感性分析：E增高10% → 应力值正偏差；ν增高10% → 应力值负偏差 | Fig. 7 [Meng 2025, pp. 8-11] | 使用表1中E和ν范围进行模拟 | 强调各向异性导致估算不确定性 |
| 破裂面高度分布与坡向分布均呈180°周期正弦变化 | Fig. 11 [Meng 2025, pp. 11-12] | 扫描分辨率0.4 mm（因0.4–0.5 mm以下各向异性消失） | 可作为应力方向指示器 |

## Limitations
- 岩芯无定向工具，故不能直接与地理坐标下的水压致裂方向比较，仅能在相对方向上验证一致性。 [Meng 2025, pp. 12-13; Meng 2025, pp. 5-7]
- DCDA仅能解算垂直钻孔轴线平面内的差分应力，如需完整三维应力，需三个互垂钻孔采样（本研究已假设Sz≈0）。 [Meng 2025, pp. 3-5]
- 假设岩石为各向同性线弹性小变形材料，未考虑微裂隙张开与扩展引起的非弹性变形和塑性行为。 [Meng 2025, pp. 11-12]
- 岩石力学参数（E, ν）的局部显著各向异性（如P波速度差异>20%）可能导致应力估算严重偏差，此时DCDA不适用。 [Meng 2025, pp. 11-12; Funato and Ito 2017]
- 破裂面边缘磨损使高度正弦拟合R²仅约0.67，影响方向判别的精度。 [Meng 2025, pp. 11-12]
- 未对样品进行连续取心和对齐，仅有3组可对齐样品（表3中粗体），一定程度上限制了方向验证的强度和统计可靠性。 [Meng 2025, pp. 8-11]

## Assumptions / Conditions
- 岩石为各向同性、线弹性材料，且变形微小。 [Meng 2025, pp. 3-5]
- 钻孔轴线平行于一个主应力，且隧道掌子面附近Sz≈0（应力释放后轴向应变可忽略）。 [Meng 2025, pp. 4-5]
- 原始岩芯直径d_0未知，但因变形量比d_0小约三个数量级，用d_min近似替代d_0。 [Meng 2025, pp. 3-4]
- 直径测量时环境恒温（23℃），保持稳定接触力和扫描速度，以减小测量误差。 [Meng 2025, pp. 5-7]
- 破裂面扫描分辨率0.4 mm，以避免低于0.4–0.5 mm尺度上各向异性消失影响分析。 [Meng 2025, pp. 7-8; Candela and Brodsky 2016]
- 高分辨率测量（CMM 1.2 μm）是DCDA有效性的前提。 [Meng 2025, pp. 11-12]

## Key Variables / Parameters
- **测量变量**：岩芯最大直径 d_max，最小直径 d_min，直径差 Δd，d_max相对参考线的方向角，破裂面边缘高度分布，坡向（aspect）分布。
- **岩石力学参数**：杨氏模量 E，泊松比 ν，单轴抗压强度 UCS，抗拉强度（巴西劈裂），密度（表1）。
- **中间导出量**：线应变 ε_max、ε_min、ε_z，体积应变 ε_v，变形前直径 d_0，变形后截面积 A₁，岩芯长度 L₀、L₁。
- **估算应力**：垂直钻孔面内主应力 S_max、S_min（当Sz≈0时即为σ_max、σ_min）。
- **拟合参数**：直径分布、高度和坡向正弦拟合的R²，正弦曲线相位（对应方向）。 [Meng 2025, pp. 3-5; Meng 2025, pp. 5-8; Meng 2025, pp. 8-11]

## Reusable Claims
- 在保证高分辨率（微米级）直径测量且具备较准确局部岩石弹性参数（E, ν）条件下，DCDA可用于估算垂直钻孔轴线平面内的差分应力和主应力方向，但其可靠性对E和ν的各向异性敏感，当P波速度各向异性超过20%时不宜使用。 [Meng 2025, pp. 11-12; Meng 2025, pp. 3-5]
- 岩芯破裂面的边缘高度分布和坡向分布均表现出约180°周期的正弦各向异性，其高点方向或坡向峰值方向可指示最小主应力方向，偏差一般小于15°。 [Meng 2025, pp. 11-12; Fig. 12]
- 使用三坐标测量机（CMM）可实现优于数微米的岩芯直径测量，配合最小二乘正弦拟合（R²>0.95）能可靠获取d_max和d_min，优于摄影测量和光学测微计。 [Meng 2025, pp. 11-12]
- 应力解除引起的岩芯膨胀量级仅为直径的千分之几，故可用d_min近似代替变形前直径d_0进行应力估算。 [Meng 2025, pp. 8-11; Meng 2025, pp. 3-4]
- 弹性模量E的高估会导致应力高估，泊松比ν的高估会导致应力低估；因此，准确评估岩石的局部力学参数是提高DCDA精度的关键。 [Meng 2025, pp. 8-11; Fig. 7]
- 当钻孔轴线与一个主应力方向一致时，岩饼呈鞍形（saddle shape），其两个对称面的交线方向分别对应S_max和S_min。 [Meng 2025, pp. 4-5; Fig. 1b]

## Candidate Concepts
- [[岩芯饼化 Core discing]]
- [[直径变形分析 DCDA]]
- [[破裂面形貌各向异性]]
- [[原位应力估算]]
- [[二长花岗岩]]
- [[水力压裂法]]
- [[坐标测量机 CMM]]
- [[岩芯应力解除]]
- [[弹性各向异性]]
- [[拉伸破坏机制]]
- [[差分应力]]
- [[体积应变法]]

## Candidate Methods
- [[Diametrical Core Deformation Analysis DCDA]]
- [[三维激光扫描与ArcGIS形貌表征]]
- [[坐标测量机高精度直径测量]]
- [[正弦曲线最小二乘拟合]]
- [[参数敏感性分析]]
- [[水压致裂应力测量]]
- [[体积应变平面应力解算]]
- [[P波速度各向异性筛选]]
- [[岩饼厚度-应力关系经验估算]]

## Connections To Other Work
- DCDA理论最初由Ito et al. (2013)提出，本研究沿用并采用Li and Mitri (2023)的体积应变修改方法，在Sz≈0假设下获得平面主应力。 [Meng 2025, pp. 3-5]
- Ziegler and Valley (2021)曾用摄影测量法获取岩芯变形，本研究使用分辨率更高的CMM（1.2 μm）并实现了自动化的圆柱面测量，提高了精度和可操作性。同时，Ziegler and Valley (2021)引入了各向异性指数，提示材料各向异性是误差主因，本文的敏感性分析与之一致。 [Meng 2025, pp. 11-12]
- Matsuki et al. (2004)基于破裂面形态的对称性确定主应力方向，但主要靠鞍形高/低点定性判断。本研究通过ArcGIS定量提取高度和坡向分布，并发现其正弦规律，将方向判别提升至15°以内的精度。 [Meng 2025, pp. 4-5; Meng 2025, pp. 11-12]
- Lim and Martin (2010)建立了岩饼厚度与最大主应力的关系（Lac du Bonnet花岗岩），本研究发现应力大小与厚度无直接分析，但建议未来可结合DCDA与厚度测量以提高估计精度。 [Meng 2025, pp. 12-13]
- Funato and Ito (2017)提出利用P波速度圆周变化判断各向异性严重性，若最大与最小波速差>20%则不宜使用DCDA，本文引用了该判据作为适用前提。 [Meng 2025, pp. 11-12]

## Open Questions
- 如何在无定向岩芯条件下直接获得地理坐标系下的主应力方向，需引入随钻定向装置或井壁印模等方法进行校准。 [Meng 2025, pp. 12-13]
- 考虑岩石塑性行为和微裂隙影响的修正DCDA模型尚未建立，目前仍以弹性假定为基础，可能导致应力估算的系统偏差。 [Meng 2025, pp. 11-12]
- 岩饼厚度与应力大小在二长花岗岩中的定量关系尚不明确，可否将厚度与DCDA联立以提高应力估计的准确性，有待进一步验证。 [Meng 2025, pp. 12-13]
- 破裂面形态分析仅在本研究500 m深度、鞍形为主的条件下得到验证，对于不同深度、不同形态（如平型、碗型）的普遍适用性尚待更多案例检验。 [Meng 2025, pp. 12-13]
- 当Sz不可忽略时（即钻孔轴线不平行于主应力），如何利用DCDA和形貌特征联合反演三维应力场的理论框架需要发展。 [Meng 2025, pp. 4-5; Meng 2025, pp. 12-13; Fig. 13]

## Source Coverage
All non-empty indexed fragments (12 text blocks) were processed. The compiled source consists of 12 source blocks with a total of 55,185 characters. Coverage by blocks is 1.0, coverage by characters is 0.991805. All fragments have been utilized to construct this page; no information outside the indexed texts was added.
