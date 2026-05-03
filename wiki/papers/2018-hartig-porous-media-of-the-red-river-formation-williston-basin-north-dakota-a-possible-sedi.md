---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-hartig-porous-media-of-the-red-river-formation-williston-basin-north-dakota-a-possible-sedi"
title: "Porous Media of the Red River Formation, Williston Basin, North Dakota: A Possible Sedimentary Enhanced Geothermal System."
status: "draft"
source_pdf: "data/papers/2018 - Porous media of the Red River Formation, Williston Basin, North Dakota a possible Sedimentary Enhanced Geothermal System.pdf"
collections:
  - "part4-1"
citation: "Hartig, Caitlin M. \"Porous Media of the Red River Formation, Williston Basin, North Dakota: A Possible Sedimentary Enhanced Geothermal System.\" *International Journal of Earth Sciences*, vol. 107, 2018, pp. 103-112. DOI 10.1007/s00531-016-1398-9."
indexed_texts: "8"
indexed_chars: "36737"
nonempty_source_blocks: "8"
compiled_source_blocks: "8"
compiled_source_chars: "36478"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.99295"
coverage_status: "full-index"
source_signature: "6d81440dc3513cbb4661df89a443c6977eca6803"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T21:04:48"
---

# Porous Media of the Red River Formation, Williston Basin, North Dakota: A Possible Sedimentary Enhanced Geothermal System.

## One-line Summary
运用GIS克里格插值与井温校正方法，评估北达科他州威利斯顿盆地红河组（Ordovician）作为沉积增强型地热系统（SEGS）的潜力，识别出渗透率为0.1–38 mD、温度达150–156°C并与离散裂缝网络重合的有利靶区。

## Research Question
红河组的多孔介质属性和温度场是否能支撑一个可行的沉积增强型地热系统（SEGS）？其地下温度、渗透率、孔隙度等关键参数的空间分布如何指导SEGS靶区优选？

## Study Area / Data
- **研究区**：美国北达科他州西部威利斯顿盆地内的Nesson背斜区域（图1、图2），具体涉及Burke、Divide、Williams、Mountrail四县交界（图4）[Hartig 2018, pp. 2-3]。
- **目标层位**：奥陶系红河组，岩性以灰岩和白云岩为主，整体渗透率<1–62.8 mD，孔隙度10–24%，地层温度（BHT）超过140°C [Hartig 2018, pp. 2-3]。
- **数据来源**：
  - 北达科他州油气部门（North Dakota Oil and Gas Division）网站的井数据，包括81口井的顶部深度、36口井的底部深度、BHT数据（50口井有记录）、渗透率数据（仅3口井有全组数据，8口井有Unit C数据）及测井曲线（CND、BCS）[Hartig 2018, pp. 3-5]。
  - 北达科他州地质调查局（NDGS）的地层柱状图与最大厚度数据（Murphy and Helms 2009）[Hartig 2018, pp. 3-4]。
  - NDGS Well 5086 用于盆地深度校正，NDGS Well 6840 用于热导率与热阻计算，NDGS Well 2894 用于地层厚度模型与温度计算 [Hartig 2018, pp. 4-8]。
  - 前人离散裂缝网络（DFN）分析结果（Hartig 2015），裂缝主方向为320°(NW)和043°(NE) [Hartig 2018, pp. 2-3]。

## Methods
1. **GIS空间插值**：采用ArcGIS中的Ordinary Kriging（普通克里格）和Co-Kriging（协同克里格）方法，对红河组的顶部深度、底部深度、孔隙度（仅Unit C）、地温梯度、热流和温度进行插值；选择均方根误差（RMSE）最小的模型 [Hartig 2018, pp. 3-4, 8]。
2. **地层厚度推算**：对于缺乏底部深度数据的45口井，利用NDGS地层柱的总最大厚度与NDGS Well 5086实测盆地底深计算校正因子（0.72），将校正后的红河组最大厚度（154 m）作为平均单位厚度加至顶部深度 [Hartig 2018, pp. 4-5]。
3. **孔隙度估算**：优先使用补偿中子-密度（CND）测井；无CND测井时，利用井眼补偿声波（BCS）测井获得Δt<sub>log</sub>，并基于Wyllie公式计算孔隙度，泥浆声波时差选用盐水值（185 μs/ft）[Hartig 2018, pp. 5-6]。
4. **井底温度（BHT）校正**：先用Harrison校正处理50口井的BHT；但因校正后温度仍低估（尤其在>2.5 km深度），进一步采用基于傅里叶定律的传导热流方法估算温度 [Hartig 2018, pp. 5-6]。
5. **热参数计算**：
   - 使用表面温度6°C，计算每口井的视地温梯度 [Hartig 2018, pp. 6-7]。
   - 基于NDGS Well 6840的各层厚度与热导率计算热阻，并得到盆地加权调和平均热导率 λ<sub>basin</sub> = 1.667 W/(m·K) [Hartig 2018, pp. 7]。
   - 由地温梯度与λ<sub>basin</sub>按傅里叶定律 q = (dT/dz) · λ 计算热流 [Hartig 2018, pp. 7]。
   - 对无BHT的31口井，从热流插值图（Fig. 10）预测其热流值 [Hartig 2018, pp. 7-8]。
6. **温度场重建**：利用NDGS Well 2894的更新地层厚度与热导率模型，以公式 T(z) = T₀ + Σ (q·zᵢ / λᵢ) 计算各井深度z处的温度，要求热导率连续至地表 [Hartig 2018, pp. 7-8]。
7. **温度插值**：分别用Ordinary Kriging（仅温度）和Co-Kriging（以热流为协变量）生成温度分布图，并以RMSE评判模型优劣 [Hartig 2018, pp. 8-9]。

## Key Findings
- 红河组渗透率在Unit C中为0.1–38 mD，属于低-中渗透率，适合通过压裂增产形成SEGS [Hartig 2018, pp. 4-5]。
- 校正后BHT提示地层温度普遍超过140°C，满足中低温双工质地热发电要求 [Hartig 2018, pp. 2-3]。
- 温度插值中，Co-Kriging图（RMSE=1.926）优于Ordinary Kriging图（RMSE=4.987），前者为推荐储层模拟输入 [Hartig 2018, pp. 8-9]。
- 根据Co-Kriging结果，最热区域（150–156°C）位于研究区中南部Williams县境内，东西延伸13.6 km，南北延伸9.9 km [Hartig 2018, pp. 9]。
- 在Williams县东南角，该高温区与Hartig (2015)识别的高线密度区（22条线理，暗示强DFN）重合，被认为是SEGS开发的优选靶区 [Hartig 2018, pp. 9]。
- 红河组地温梯度、热流、孔隙度等属性图（Fig. 5–7, Fig. 9–10）可为后续储层模拟提供输入 [Hartig 2018, pp. 9]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 红河组渗透率0.1–38 mD（Unit C灰岩）；全组渗透率<1–62.8 mD | [Hartig 2018, pp. 2-5] | 数据来自北达科他州油气部门岩心分析；Unit C样品覆盖有限 | 低-中渗透率适合压裂增产SEGS |
| 红河组BHT超过140°C，校正后部分区域达150–156°C | [Hartig 2018, pp. 2-3, 8-9] | 基于50口井的Harrison校正和传导热流模型；温度估算依赖热导率连续性与地层模型 | 满足双工质机组热源要求 |
| Co-Kriging温度插值RMSE=1.926，Ordinary Kriging RMSE=4.987 | [Hartig 2018, pp. 8-9] | 协同变量为热流，自变量为温度；研究区东南和东北角存在轻微畸变 | Co-Kriging模型更可靠 |
| 盆地调和平均热导率 λ<sub>basin</sub> = 1.667 W/(m·K) | [Hartig 2018, pp. 7] | 基于NDGS Well 6840的各层厚度和热导率；假设各向同性导热 | 用于计算热流和温度 |
| 红河组平均单位厚度154 m（由校正因子0.72修正最大厚度213 m得出） | [Hartig 2018, pp. 4-5] | 依据NDGS地层柱最大厚度和Well 5086盆地底深；仅用于缺失底部深度的井 | 校正因子计算式为：4740 m / 6545 m |
| 孔隙度估算66个数据点，使用CND或BCS测井，Unit C | [Hartig 2018, pp. 5-6] | 假设孔隙度正态分布，且含天然裂缝与基质孔；泥浆声波时差采用盐水值 | 插值图RMSE=0.057 (Fig. 7) |
| 离散裂缝网络主方向为320°和043°，NE向裂缝为导流主通道 | [Hartig 2018, pp. 2-3] | 基于Hartig (2015)的DFN模拟 | 裂缝密度与高温区重叠利于开发 |

## Limitations
- BHT校正方法固有的不准确性：即使使用Harrison校正，校正后BHT仍会低估深部温度，尤其在>2.5 km深度 [Hartig 2018, pp. 5-6]。
- 渗透率数据严重不足，仅3口井有全组数据，8口井有Unit C数据，无法开展空间插值 [Hartig 2018, pp. 4-5]。
- 孔隙度估算仅限于Unit C，不能代表整个红河组 [Hartig 2018, pp. 4-5]。
- 温度计算所用的地层厚度模型来自距离研究区中心约120 km的NDGS Well 2894，虽经深度校正，但仍可能因横向相变产生偏差 [Hartig 2018, pp. 7-8]。
- Co-Kriging温度图在东南和东北角存在畸变（锯齿状边缘），可能影响局部解释 [Hartig 2018, pp. 9]。
- 热导率和热阻计算依赖于NDGS Well 6840和Well 2894的数据，未考虑研究区内可能的非均质性 [Hartig 2018, pp. 7-8]。
- 温度估算要求热导率数据连续至地表，虽然本研究满足此条件，但实际工程中可能较难保证 [Hartig 2018, pp. 8]。

## Assumptions / Conditions
- 热流为传导型且恒定，地温梯度与热导率服从傅里叶定律（q = dT/dz · λ）[Hartig 2018, pp. 6]。
- 表面温度固定为6°C [Hartig 2018, pp. 6-7]。
- 红河组平均单位厚度为154 m，通过盆地总厚度与最大深度的校正因子（0.72）获得 [Hartig 2018, pp. 4-5]。
- 用于热导率和热阻计算的NDGS Well 6840和Well 2894的岩性和厚度与研究区具有可比性 [Hartig 2018, pp. 7-8]。
- 孔隙度数据服从正态分布，且CND/BCS测井估算的孔隙度包含基质孔与天然裂缝的贡献 [Hartig 2018, pp. 5-6]。
- 渗透率属性在Unit C的变化可部分代表整个红河组储层特性 [Hartig 2018, pp. 4-5]。
- 使用Harrison校正时假设该校正适用于北达科他地区（原为俄克拉荷马州推导）[Hartig 2018, pp. 5]。

## Key Variables / Parameters
- 顶部深度、底部深度（红河组） [Hartig 2018, pp. 3-4]
- 孔隙度（Unit C） [Hartig 2018, pp. 5-6]
- 地温梯度（°C/km） [Hartig 2018, pp. 6-7]
- 热流（mW/m²） [Hartig 2018, pp. 7-8]
- 温度（°C） [Hartig 2018, pp. 7-8]
- 渗透率（mD） [Hartig 2018, pp. 4-5]
- 热导率（W/(m·K)）[Hartig 2018, pp. 7-8]
- 热阻（(m²·K)/W） [Hartig 2018, pp. 7]
- 调和平均热导率 1.667 W/(m·K) [Hartig 2018, pp. 7]
- 校正因子 0.72 [Hartig 2018, pp. 4]
- 红河组最大厚度 213 m，平均厚度 154 m [Hartig 2018, pp. 4-5]
- 泥浆声波时差（Δt_f）185 μs/ft，基质声波时差（Δt_ma）43.5 μs/ft [Hartig 2018, pp. 5-6]
- 表面温度 T₀ = 6°C [Hartig 2018, pp. 6]
- 线理密度（条数/84.9 km²） [Hartig 2018, pp. 9]

## Reusable Claims
1. **Claim**: 在威利斯顿盆地红河组，若利用NDGS Well 2894的地层厚度-热导率模型和傅里叶定律进行温度推算，可在缺乏高精度平衡温度测井的情况下获得较BHT校正更可靠的深部温度分布，前提是热导率数据连续至地表且研究区地层结构与模型井相似。 [Hartig 2018, pp. 5-8]
2. **Claim**: 红河组Unit C灰岩的渗透率范围为0.1–38 mD，在此渗透率区间实施水力压裂，可有效增强井筒与天然裂缝网络的连通性，从而提升SEGS的换热能力，但该结论基于有限样本量，适用于类似碳酸盐岩储层。 [Hartig 2018, pp. 4-5]
3. **Claim**: 使用Co-Kriging方法以热流作为协变量对推算温度进行插值，能显著降低RMSE（较Ordinary Kriging降低约2.6倍），为沉积盆地地热温度场建模提供了一种优于单变量克里格的空间估计手段，要求热流与温度存在空间相关性。 [Hartig 2018, pp. 8-9]
4. **Claim**: 研究区Williams县东南角同时具备150–156°C的高温、高线理密度（22条/84.9 km²）以及适合压裂的低-中渗透率，可作为SEGS先导试验靶区，但需注意Co-Kriging图在该边缘存在锯齿状畸变，开发前需补充局部物探资料。 [Hartig 2018, pp. 9]
5. **Claim**: 沉积盆地SEGS的商业可行性已被德国Unterhaching、Landau和美国Desert Peak等案例初步证明，其关键技术包括酸化增产和/或水力压裂以连接天然渗透性通道，这一经验可推广至温度>140°C、基质渗透率0.1–38 mD且存在天然裂缝的碳酸盐岩地层。 [Hartig 2018, pp. 1-2]

## Candidate Concepts
- [[Sedimentary Enhanced Geothermal System (SEGS)]]
- [[Discrete Fracture Network (DFN)]]
- [[Ordovician Red River Formation]]
- [[Williston Basin]]
- [[Nesson Anticline]]
- [[Kriging interpolation]]
- [[Ordinary Kriging]]
- [[Co-Kriging]]
- [[Bottom-hole temperature (BHT) correction]]
- [[Harrison correction]]
- [[Fourier’s law in geothermics]]
- [[Harmonic mean thermal conductivity]]
- [[Thermostratigraphy]]
- [[Binary geothermal power plant]]
- [[Compensated neutron-density (CND) log]]
- [[Borehole compensated sonic (BCS) log]]
- [[Lineament density and geothermal targeting]]

## Candidate Methods
- [[GIS-based spatial interpolation for geothermal parameters]]
- [[Co-Kriging with heat flow as covariate for temperature mapping]]
- [[Correction of BHT using stratigraphic heat flow model]]
- [[Calculation of harmonic mean conductivity for a sedimentary basin]]
- [[Porosity estimation from well logs (CND and BCS)]]
- [[Unit thickness correction using basin depth and stratigraphic maximum thickness]]
- [[Stratigraphic thickness model for temperature reconstruction (T(z) summation)]]
- [[Semivariogram analysis for kriging]]
- [[DFN-based site selection combined with temperature maps]]

## Connections To Other Work
- **Gosnold et al. (2012)** 的威利斯顿盆地热地层学（Thermostratigraphy）研究为本项目提供了井温校正思路、调和平均热导率计算方法和NDGS Well 6840、Well 2894的物性数据，同时指出了BHT校正不一致性的根源是页岩热导率不准 [Hartig 2018, pp. 6-8]。
- **Hartig (2015)** 的离散裂缝网络模拟揭示了研究区的裂缝主导方向和线理密度，被用来交叉验证高温区的SEGS开发前景 [Hartig 2018, pp. 2-3, 9]。
- **Blackwell and Richards (2004b)** 的北美地热图和**Blackwell et al. (2006)** 对沉积盆地地热资源的评估，将威利斯顿盆地列为候选SEGS盆地 [Hartig 2018, pp. 1-2]。
- **Porro and Augustine (2014)** 估算了威利斯顿盆地的总地热能（3.4×10¹⁹ kJ）并评估了美国主要沉积盆地的EGS潜力 [Hartig 2018, pp. 2-3]。
- **SEGS工程案例**：墨西哥Maguarichic的中低温双工质机组、德国Unterhaching与Landau的酸化/压裂灰岩SEGS，以及美国Desert Peak的压裂增产（175倍注入率提升），提供了实际的工程参照 [Hartig 2018, pp. 1-2]。
- **McDonald et al. (2015)** 和 **Crowell & Gosnold (2011)** 等研究也为盆地BHT校正和热流分析提供了方法基础 [Hartig 2018, pp. 5-6]。

## Open Questions
- 渗透率的全空间分布特征尚未解决，仅有零星数据，是否能通过地质统计方法（如序贯高斯模拟）生成合理的渗透率场供储层模拟使用？ [Hartig 2018, pp. 4-5]
- 文中提到的储层模拟模型尚未建立，该模型的建立能否验证裂缝网络对热开采的长期影响？ [Hartig 2018, pp. 9]
- 红河组Unit C的孔隙度估算结果是否可外推至整个红河组？不同岩性段的储集空间差异有多大？ [Hartig 2018, pp. 5-6]
- 在Co-Kriging温度图的畸变区域（东南、东北角），是否可通过增加控制井或使用更先进的插值方法（如局部变差函数）来改善？ [Hartig 2018, pp. 9]
- 该SEGS靶区若实施水力压裂，地层天然裂缝与压裂裂缝的相互作用如何影响换热性能和诱发地震风险？ [Hartig 2018, pp. 1-2, 9]
- 威利斯顿盆地其他层位（如Deadwood组）是否具备同等的SEGS潜力？ [Hartig 2018, pp. 2-3]

## Source Coverage
所有8个非空索引片段均已被处理并编译入本页面。基于提供的覆盖率审计数据，片段编译的覆盖率按源码块计为100%（8/8块），按字符数计约为99.3%（36,478/36,737字符）。未发现未处理的索引片段。

---
**Note:** 本页面仅基于提供的索引片段生成，未引入外部信息。所有数据、条件与局限性均已附上原始出处标签。
