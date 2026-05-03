---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2018-hartig-porous-media-of-the-red-river-formation-williston-basin-north-dakota-a-possible-sedi"
title: "Porous Media of the Red River Formation, Williston Basin, North Dakota: A Possible Sedimentary Enhanced Geothermal System."
status: "draft"
source_pdf: "data/papers/2018 - Porous media of the Red River Formation, Williston Basin, North Dakota a possible Sedimentary Enhanced Geothermal System.pdf"
collections:
  - "part4-1"
citation: "Hartig, Caitlin M. \"Porous Media of the Red River Formation, Williston Basin, North Dakota: A Possible Sedimentary Enhanced Geothermal System.\" *International Journal of Earth Sciences*, vol. 107, 2018, pp. 103-112. DOI 10.1007/s00531-016-1398-9."
indexed_texts: "8"
indexed_chars: "36737"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T22:16:34"
---

# Porous Media of the Red River Formation, Williston Basin, North Dakota: A Possible Sedimentary Enhanced Geothermal System.

## One-line Summary
评估美国北达科他州威利斯顿盆地红河组作为沉积增强型地热系统（SEGS）的潜力，发现150–156°C的高温区与高裂隙密度区在威廉姆斯县东南部重合，构成有利的地热开发靶区。

## Research Question
红河组在威利斯顿盆地Nesson背斜下是否具备作为沉积增强型地热系统（SEGS）所需的热、渗透性和裂缝网络条件？如何通过现有井数据量化其热潜力并识别最佳开发位置？

## Study Area / Data
研究区位于美国北达科他州西部威利斯顿盆地，Nesson背斜下方。数据来源包括：
- 81口井的红河组顶面深度，36口井的底面深度（源自北达科他州石油和天然气部门）[Hartig 2018, pp. 4-5]。
- 66个来自声波测井的孔隙度估算点 [Hartig 2018, pp. 5-6]。
- 50个经过校正的井底温度（BHT）数据，用于计算地温梯度和温度插值 [Hartig 2018, pp. 6-7]。
- 参考NDGS Well 5086、6840、2894的层序厚度、热导率等物理性质 [Hartig 2018, pp. 4-5, 8-9]。

## Methods
- **GIS与地质统计**：利用ArcGIS进行线理分析，创建代表地下离散裂缝网络（DFN）的shapefile，用于储层模拟代理 [Hartig 2018, pp. 3-4]。
- **空间插值**：对地层顶面、底面深度和孔隙度采用普通克里金法（Ordinary Kriging），以最小均方根误差（RMSE）选择最佳模型 [Hartig 2018, pp. 4-6]。
- **厚度校正**：利用NDGS Well 5086的最大地层厚度求和与深度的偏差计算校正因子（Eq.1），推算红河组平均厚度（154 m），并用于缺失底面深度的井 [Hartig 2018, pp. 4-5]。
- **孔隙度计算**：应用Wyllie时间平均方程（Eq.2, ϕsonic = (Δt log − Δtma) / (Δtf − Δtma)），其中泥浆时差Δtf=185 μs/ft（盐水），基质时差Δtma=43.5 μs/ft（石灰岩/白云岩），并假定孔隙度为正态分布且包含天然裂缝与岩石孔隙 [Hartig 2018, pp. 5-6]。
- **温度校正与热参数计算**：采用Harrison等（1983）的方法校正BHT；利用地表温度6°C计算地温梯度；通过各层厚度和热导率计算热阻（Eq.4: TRi = zi/λi）和盆地的加权调和平均热导率（Eq.5: λbasin = Σz / ΣTR），继而用热流值预测温度-深度剖面（Eq.6）[Hartig 2018, pp. 6-9]。
- **温度插值**：分别用普通克里金和协克里金（以热流为协变量）对计算得到的地下温度进行空间插值 [Hartig 2018, pp. 9-10]。

## Key Findings
- 红河组校正后的井底温度超过140°C，最高可达156°C，满足低温-中温（~150°C）二元发电系统的要求 [Hartig 2018, pp. 5-6, 9-10]。
- 威利斯顿盆地估算总热能为3.4 × 10¹⁹ kJ [Hartig 2018, pp. 4]。
- 天然裂缝主要走向为320°（西北）和043°（东北），东北走向裂缝构成注入流体的主要通道 [Hartig 2018, pp. 3-4]。
- 温度插值图显示最热区域（150–156°C）在威廉姆斯县，普通克里金指出该区域在东南部延伸至Mountrail县西部（东西9.8 km，南北8.0 km），协克里金则显示在西南-中南部（东西13.6 km，南北9.9 km）；两者共同确认威廉姆斯县东南部为高温区 [Hartig 2018, pp. 9-10]。
- 该高温区与Hartig (2015) 识别的高线理密度区（22条线理）重叠，表明高裂缝密度与高热流位置一致，使威廉姆斯县东南部成为最优SEGS开发远景点 [Hartig 2018, pp. 10]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 红河组BHT可达156°C，适合二元地热 | [Hartig 2018, pp. 5-6, 9-10] | 使用Harrison等方法校正BHT，假设地表温度6°C | 两种插值均显示150-156°C的高温区 |
| 孔隙度源于声波测井，66个点，正态分布 | [Hartig 2018, pp. 5-6] | 采用Wyllie方程，泥浆时差185 μs/ft（盐水），基质时差43.5 μs/ft | 包含天然裂缝与基质孔隙，插值见Fig.7 |
| 裂缝主导方向320°和043°，NE向为流体主通道 | [Hartig 2018, pp. 3-4] | 基于Hartig (2015)线理分析DFN | 无直接渗透率测试数据 |
| 威廉姆斯县东南部22-lineament区与最高温重合 | [Hartig 2018, pp. 10] | 叠加Hartig (2015)线理密度图与本研究温度图 | 认为是最佳SEGS位置 |
| 盆地热储量3.4×10¹⁹ kJ | [Hartig 2018, pp. 4] | 引自Porro and Augustine (2014) | 本研究未重新计算该储量 |

## Limitations
- 渗透率数据仅在附录提及，未在索引片段中显示具体数值或插值分布，无法评估其与温度、裂缝的耦合关系。
- 井底温度校正依赖的Harrison等法细节未详述，其适用性和误差未讨论。
- 地层厚度校正仅基于一口参考井（NDGS Well 5086），可能引入局部偏差。
- 温度预测模型（Eq.6）的有效性高度依赖热导率数据的连续性和覆盖地表的要求，虽声称满足，但未提供验证证据。
- 研究局限于Nesson背斜区，结论外推到全盆地需谨慎。
- 未从片段中见到SEGS经济性、可持续性及刺激方案（如水力压裂）的定量分析，仅定性提及SEGS优势。

## Assumptions / Conditions
- SEGS概念假设沉积地层具有较高的自然渗透性，只需少量刺激连接井与储层 [Hartig 2018, pp. 1-2]。
- ~150°C的温度可在常规油气作业深度内提取，无需特殊高温钻测设备 [Hartig 2018, pp. 1-2]。
- 孔隙度估算假设储层孔隙度符合正态分布，且声波孔隙度综合反映了裂缝和基质孔隙 [Hartig 2018, pp. 5-6]。
- Wyllie方程中泥浆时差取185 μs/ft（盐水），因红河组含页岩；基质时差取43.5 μs/ft（石灰岩/白云岩典型值）[Hartig 2018, pp. 5-6]。
- 井底温度校正假设能抵消钻井液冷却效应，恢复原始岩温 [Hartig 2018, pp. 6]。
- 热参数计算和温度建模（Eq.6）要求热导率从地表开始连续无间断，否则计算结果错误 [Hartig 2018, pp. 8]。
- 热流值采纳Gosnold et al. (2012)的测定结果，但该研究指出页岩热导率测量不精确可能导致热流差异 [Hartig 2018, pp. 8]。

## Key Variables / Parameters
- **孔隙度 (ϕsonic)**：由Δt log通过Wyllie方程求取，Δtf=185 μs/ft，Δtma=43.5 μs/ft。
- **井底温度 (BHT)**：原始测量→ Harrison等法校正→ 地温梯度 = (BHT - 6°C)/深度。
- **热阻**：TRi = zi / λi。
- **调和平均热导率**：λbasin = Σ所有层厚度 / Σ所有层热阻。
- **温度-深度预测**：T(z) 基于热流和各层热阻计算（Eq.6，具体形式未完全列出），要求连续热导率。
- **红河组厚度**：最大厚度213 m，校正后平均厚度154 m。
- **热储量**：3.4×10¹⁹ kJ（引用）。
- **裂缝方向**：320° (NW) 和043° (NE)，NE向为注入流体主要通道。
- **插值方法**：普通克里金、协克里金；评价指标RMSE。

## Reusable Claims
- SEGS比结晶岩EGS更具经济性，因为天然渗透率较高、目标温度适中（~150°C）且可持续 [Hartig 2018, pp. 1-2]。
- 在红河组这样的碳酸盐岩储层中，裂缝方向控制流体流动，NE向裂缝是注采流体的主要优势通道 [Hartig 2018, pp. 3-4]。
- 高裂缝密度区（以线理密度为代理）与150°C以上高温区重叠时，可作为SEGS开发的优先靶区，这一空间耦合是选址关键 [Hartig 2018, pp. 10]。
- 使用调和平均热导率和连续热导率剖面可预测沉积盆地的温度分布，该方法依赖于高质量的岩石热物性数据 [Hartig 2018, pp. 8-9]。
- 在含页岩的石灰岩/白云岩地层中，Wyllie时间平均方程结合盐水泥浆时差仍可用于孔隙度估算，但需检验其适用性 [Hartig 2018, pp. 5-6]。

## Candidate Concepts
- [[Sedimentary Enhanced Geothermal System (SEGS)]]
- [[Discrete Fracture Network (DFN)]]
- [[Porosity from Sonic Logs]]
- [[Bottom-Hole Temperature Correction]]
- [[Geothermal Gradient]]
- [[Harmonic Mean Thermal Conductivity]]
- [[Ordinary Kriging and Co-Kriging]]
- [[Thermal Resistance of Layers]]

## Candidate Methods
- [[Wyllie Time-Average Equation for Porosity]]
- [[Harrison et al. BHT Correction Method]]
- [[Temperature-depth modeling using thermal resistance summation]]
- [[GIS lineament analysis for fracture mapping]]
- [[Geostatistical interpolation (Kriging) for subsurface properties]]

## Connections To Other Work
- 直接基于Hartig (2015) 的DFN模拟，将裂缝网络与热场结合，扩展了该区域地热评估 [Hartig 2018, pp. 3-4, 10]。
- 借鉴了德国已运行的SEGS项目（Unterhaching、Landau）的刺激经验（酸化、水力压裂），但未直接对比结果 [Hartig 2018, pp. 1-2]。
- 使用了Gosnold et al. (2012) 的威利斯顿盆地热地层学数据及热流值，以及McDonald et al. (2015) 的热流成果 [Hartig 2018, pp. 7-8]。
- 温度校正方法参考Harrison et al. (1983)，热导率背景参考Blackwell and Richards (2004a) 和Crowell et al. (2011) [Hartig 2018, pp. 6-7]。
- 可由主题关联至 [[Fracture reservoir characterization]]、[[Low-enthalpy geothermal systems]] 和 [[Geostatistical reservoir modeling]]。

## Open Questions
- 未从索引片段中确认红河组的实测渗透率值或分布，无法验证流动能力。
- 开发经济性（如钻井成本、平准化电力成本）和具体的储层刺激方案未讨论。
- 储层流体地球化学特征及潜在结垢问题未知。
- 未进行长期生产条件下的热-流-力耦合模拟，可持续提取能力未验证。

## Source Coverage
本页面依据8个索引片段覆盖了论文的主体部分：引言与研究背景（pp.1-2）、研究区与数据概述（pp.2-4）、详细方法（pp.4-9，涵盖深度校正、孔隙度、温度校正、热参数和插值）、核心发现与结论（pp.9-10）以及致谢/参考文献。片段似涉及全文的绝大多数章节，但可能缺失部分图和表格（如渗透率分布、附录数据表），对结果的讨论、与其他盆地的对比等细节未在片段中呈现，因此本页对热参数和温度分布有较完整记录，而对渗透率、经济性和流体特性存在明显的信息缺口。
