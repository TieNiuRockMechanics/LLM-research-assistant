---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2020-mahanta-an-insight-into-pore-network-models-of-high-temperature-heat-treated-sandstones-usi"
title: "An Insight into Pore-Network Models of High-Temperature Heat-Treated Sandstones Using Computed Tomography."
status: "draft"
source_pdf: "data/papers/2020 - An insight into pore-network models of high-temperature heat-treated sandstones using computed tomography.pdf"
collections:
  - "zotero new"
  - "论文"
citation: "Mahanta, Bankim, et al. \"An Insight into Pore-Network Models of High-Temperature Heat-Treated Sandstones Using Computed Tomography.\" *Journal of Natural Gas Science and Engineering*, vol. 77, 2020, p. 103227. doi:10.1016/j.jngse.2020.103227. Accessed 2026."
indexed_texts: "14"
indexed_chars: "65795"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T00:08:36"
---

# An Insight into Pore-Network Models of High-Temperature Heat-Treated Sandstones Using Computed Tomography.

## One-line Summary
该研究利用高分辨率micro-CT对三种印度砂岩在25–800°C热处理后的孔隙网络模型进行了表征，揭示了矿物学（尤其粘土矿物）控制下的孔隙空间演化和孔隙网络属性变化 [Mahanta 2020, pp. 1-2]。

## Research Question
高温热处理如何影响不同矿物学组成的砂岩的微观结构及孔隙网络特征？孔隙空间演化与粘土矿物依赖性如何？[Mahanta 2020, pp. 1-2, 5-7]

## Study Area / Data
研究选用印度三种砂岩：Dholpur砂岩 (DS)、Jodhpur砂岩 (JS) 和 Gondwana砂岩 (GS) [Mahanta 2020, pp. 1-2]。样品直径约2–3 mm，取自不同地点（图1地质图），矿物组成通过XRD分析确定 [Mahanta 2020, pp. 2-5]。矿物相总结于表1：DS富含石英 (94.3%)，JS含较高粘土矿物（迪开石5.7%、高岭石5.5%），GS含铁白云石、伊利石等 (石英50.8%，菱铁矿18.2%，白云母18.7%，伊利石9.1%，高岭石2.5%）[Mahanta 2020, pp. 2-5]。

## Methods
- **热处理**：样品以5 °C/min升温至目标温度（200、400、600、800 °C），保温3小时后空冷至室温 [Mahanta 2020, pp. 7-9]。
- **Micro-CT扫描与图像处理**：使用高分辨率micro-CT获取三维图像，在Avizo 9.0软件中处理，包括平滑与去噪（各向异性扩散滤波器）、锐化（unsharp masking filter）以及基于阈值的分割 [Mahanta 2020, pp. 9-11]。
- **代表性单元体积 (REV) 确定**：以孔隙度为参数，当立方体边长超过550 μm时孔隙体积近乎稳定且标准偏差极小，故选取边长600 μm的立方体作为REV [Mahanta 2020, pp. 11-13]。
- **孔隙网络模型 (PNM)**：采用separate-objects模块（结合分水岭、距离变换和数值重建算法）提取孔隙和喉道，并生成PNM [Mahanta 2020, pp. 13-14]。提取算法基于骨架化/中轴法和最大球法（参见Al-Kharusi and Blunt 2007; Dong and Blunt 2009; Silin and Patzek 2006等）[Mahanta 2020, pp. 13-14]。
- **孔隙网络属性计算**：包括孔隙体积、孔隙半径、喉道半径、喉道长度和配位数 [Mahanta 2020, pp. 2-5]。

## Key Findings
1. **孔隙度随温度的非单调响应**：DS从室温20.02%下降至200°C的18.25%（-8.8%），之后上升至800°C的24.79%（+23.84%）；JS在600°C达到峰值20.03%（+39.44%），800°C降至16.89%；GS持续增加至600°C的23.94%（+71.09%），800°C稍降至23.47%（+67.79%）[Mahanta 2020, pp. 13-14]。
2. **矿物学控制孔隙演化**：DS和GS总体孔隙度随温度增加，而JS在600°C后下降，归因于粘土矿物热反应差异 [Mahanta 2020, pp. 1-2, 14-15]。加热过程中，<200°C失去自由水、吸附水及结合水，矿物膨胀导致孔隙度降低；200–400°C失去结晶水与结构水，孔隙度轻微上升；400–600°C因热应力致矿物微破裂和结构损伤，孔隙度显著增加；600°C以上微裂纹网络扩张 [Mahanta 2020, pp. 14-15]。
3. **微裂纹分布的温度依赖性**：DS和GS中，800°C观察到更多、更宽的微裂纹，而JS中微裂纹密度最高出现在600°C [Mahanta 2020, pp. 14-15]。
4. **孔隙网络属性提取**：通过PNM获得了孔隙半径、喉道半径、配位数、喉道通道长度等参数，可用于评价流体流动行为 [Mahanta 2020, pp. 2-5, 13-14]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| DS孔隙度：25°C 20.02%；200°C 18.25%（-8.8%）；400°C 21.33%（+6.58%）；600°C 22.22%（+11.02%）；800°C 24.79%（+23.84%）| [Mahanta 2020, pp. 13-14] | 热处理25–800°C，升温速率5°C/min，恒温3h，空冷 | 整体增加，200°C出现初始降低 |
| JS孔隙度：25°C 14.37%；200°C 14.88%（+3.61%）；400°C 16.61%（+15.59%）；600°C 20.03%（+39.44%）；800°C 16.89%（+17.58%）| [Mahanta 2020, pp. 13-14] | 同上 | 600°C最大孔隙度，800°C下降 |
| GS孔隙度：25°C 13.99%；200°C 13.82%（-1.19%）；400°C 18.35%（+31.16%）；600°C 23.94%（+71.09%）；800°C 23.47%（+67.79%）| [Mahanta 2020, pp. 13-14] | 同上 | 400°C后大幅增加，富含粘土矿物 |
| 矿物相：DS: 石英94.3%，正长石5.4%，单斜辉石0.3%；JS: 石英83.9%，迪开石5.7%，高岭石5.5%，方解石3.5%，长石0.8%，尖晶石0.5%；GS: 石英50.8%，菱铁矿18.2%，白云母18.7%，伊利石9.1%，高岭石2.5%，白云石0.8% | [Mahanta 2020, pp. 2-5] | XRD分析 | GS粘土矿物含量最高 |
| JS在600°C时微裂纹密度最高，而DS和GS在800°C最高 | [Mahanta 2020, pp. 14-15] | 显微观察 | 裂纹演化与矿物热分解差异有关 |
| REV边长超过550 μm时孔隙体积几乎相等且标准偏差极小，选择600 μm立方体 | [Mahanta 2020, pp. 11-13] | 基于孔隙度参数的REV分析 | 保证孔隙网络尺度代表性 |
| 图像处理采用各向异性扩散滤波器去噪，unsharp masking锐化，阈值分割 | [Mahanta 2020, pp. 9-11] | Avizo 9.0 | 保留边缘并增强对比 |

## Limitations
- 研究未提供孔隙网络属性（如配位数、喉道半径等）的定量值或对比表格，片段中仅提到进行了PNM提取 [Mahanta 2020, pp. 2-5, 13-14]。
- 未确认是否考虑了加热-冷却循环导致的热滞后效应或冷却速率的影响，仅提及空冷 [Mahanta 2020, pp. 7-9]。
- 文中未涉及流体流动模拟或渗透率计算，仅关注孔隙结构演化 [Mahanta 2020, pp. 1-2]。
- 样本量及统计分析未明确，可能影响观测的代表性 [未从索引片段中确认]。
- 粘土矿物转化（如高岭石→伊利石）及化学反应的细节未在片段中体现，仅泛泛提及水损失和矿物分解 [Mahanta 2020, pp. 14-15]。

## Assumptions / Conditions
- 热处理在常压空气气氛中进行，无围压，与实际深部地层条件（高温高压、流体存在）存在差异 [Mahanta 2020, pp. 7-9]。
- 孔隙网络建模基于球-管（球代表孔隙体，圆柱代表喉道）的理想化简化，可能忽略不规则几何的影响 [Mahanta 2020, pp. 2-5]。
- 孔隙度和孔隙结构演化主要归因于热应力与矿物脱水/分解，未考虑水岩反应或胶结物溶解 [Mahanta 2020, pp. 14-15]。
- REV基于干燥样品图像分析，未考虑饱和介质、有效孔隙度或非连通孔隙的流体可及性评估 [Mahanta 2020, pp. 11-13]。
- PNM提取依赖骨架化与最大球算法，其精度受图像分辨率和分割阈值影响 [Mahanta 2020, pp. 13-14]。

## Key Variables / Parameters
- **温度（°C）**：25, 200, 400, 600, 800
- **总孔隙度（%）**：DS, JS, GS 在各温度点的孔隙度值
- **孔隙度增量百分比（%）**：相对于25°C的变化
- **矿物组成（%）**：石英、粘土矿物、碳酸盐等关键相
- **孔隙网络属性**：孔隙半径、喉道半径、喉道通道长度、配位数 [Mahanta 2020, pp. 2-5]
- **微裂纹密度与形态** [Mahanta 2020, pp. 14-15]
- **REV尺寸**：600 μm 立方体 [Mahanta 2020, pp. 11-13]

## Reusable Claims
1. **粘土矿物含量控制热处理砂岩孔隙度演化路径**：在25–800°C热作用下，富含粘土矿物（伊利石、高岭石）的砂岩（如GS）在400°C以上孔隙度急剧增加，而富石英砂岩（DS）变化相对平缓，含混合粘土矿物的JS在600°C后孔隙度下降。此规律适用于干燥、无围压热处理条件，且依赖于初始矿物组成和微裂纹发育模式 [Mahanta 2020, pp. 1-2, 13-14]。
2. **升温早期（<200°C）因水损失和矿物膨胀可能导致砂岩孔隙度短暂降低**：DS和GS在200°C均表现为孔隙度下降，而JS因粘土矿物性质不同表现出轻微增加。该现象取决于岩石的含水类型和矿物热膨胀性质 [Mahanta 2020, pp. 13-15]。
3. **最大球法和骨架化法结合的PNM可以从micro-CT图像中提取喉道-孔隙网络参数**：可采用Avizo软件中的separate-objects模块进行孔隙分割和网络构建，前提是图像经过去噪、锐化和适当阈值分割，且REV确保代表性 [Mahanta 2020, pp. 9-14]。

## Candidate Concepts
- [[Pore-network model]]
- [[Micro-CT imaging]]
- [[Thermal treatment of reservoir rocks]]
- [[Clay mineral dehydration]]
- [[Pore connectivity and coordination number]]
- [[Representative Elementary Volume (REV)]]
- [[Anisotropic diffusion filter for image processing]]
- [[Maximal ball algorithm]]
- [[Skeletonization-based pore extraction]]

## Candidate Methods
- [[X-ray computed tomography (XCT)]]
- [[Avizo 9.0 software for 3D image analysis]]
- [[Unsharp masking filter]]
- [[Thermal gravimetric analysis (TGA)]]
- [[X-ray diffraction (XRD)]]
- [[Watershed segmentation]]
- [[Separate-objects module in PNM extraction]]

## Connections To Other Work
- 文中引用了孔隙网络模型相关基础研究，如 Blunt (2001) 对多孔介质PNM的综述，以及 Xiong et al. (2016) 的发展 [Mahanta 2020, pp. 13-14]。算法方面，最大球法参考了 Al-Kharusi and Blunt (2007) 和 Dong and Blunt (2009)，骨架化方法参考了 Lindquist et al. (1996) 和 Silin and Patzek (2006) [Mahanta 2020, pp. 13-14]。
- 热作用引起孔隙变化机制与 Sun et al. (2016) 和 Tian et al. (2012) 关于砂岩热损伤的论述一致 [Mahanta 2020, pp. 14-15]。
- 未从片段中发现与其它具体实验研究的直接比较，但可从主题上连接到 [[High-temperature rock mechanics]]、[[Underground coal gasification]]、[[Enhanced geothermal systems]] 及 [[Thermal cracking in sandstone]] 等相关文献。

## Open Questions
- 热处理后砂岩的渗透率如何变化？PNM能否预测渗透率？[未从索引片段中确认]
- 添加围压和流体条件后，孔隙网络演化规律是否改变？
- 粘土矿物的具体相变反应（如高岭石→偏高岭石）及其对孔隙度的定量贡献是多少？
- JS在800°C孔隙度下降的具体机理（是否由于粘土烧结或塌陷）是什么？
- 不同冷却方式（水冷、快速冷却）会产生怎样的孔隙结构差异？

## Source Coverage
本页依据14个索引片段撰写，覆盖了摘要、引言、方法（图像处理、REV、PNM）、主要结果（孔隙度数据、微裂纹观察）。但关键限制是缺少PNM属性的定量报告（如配位数、喉道半径数值），且讨论和结论部分未完整呈现，使得无法具体评述流体传输能力预测。部分图表描述仅通过文字说明，可能遗漏图形中的细节。因此，基于这些片段的综合信息应被视为不完整，尤其是孔隙网络模型的输出参数和模拟结果未被收录。
