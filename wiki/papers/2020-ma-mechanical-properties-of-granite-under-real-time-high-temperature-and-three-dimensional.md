---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2020-ma-mechanical-properties-of-granite-under-real-time-high-temperature-and-three-dimensional"
title: "Mechanical Properties of Granite under Real-Time High Temperature and Three-Dimensional Stress."
status: "draft"
source_pdf: "data/papers/2020 - Mechanical properties of granite under real-time high temperature and three-dimensional stress.pdf"
collections:
  - "zotero new"
citation: "Ma, Xiao, et al. \"Mechanical Properties of Granite under Real-Time High Temperature and Three-Dimensional Stress.\" *International Journal of Rock Mechanics & Mining Sciences*, vol. 136, 2020, article 104521. Accessed 2026."
indexed_texts: "6"
indexed_chars: "29660"
nonempty_source_blocks: "6"
compiled_source_blocks: "6"
compiled_source_chars: "27718"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.934525"
coverage_status: "full-index"
source_signature: "1b501b6587f742a37d3954f013bc07a6d15fb77c"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T03:13:49"
---

# Mechanical Properties of Granite under Real-Time High Temperature and Three-Dimensional Stress.

## One-line Summary
实时高温和三向应力条件下，花岗岩的峰值强度随温度先增后减，脆性随应力和温度增加而减弱，黑云母颗粒的韧性增强是力学性质变化的主要原因。

## Research Question
在干热岩（HDR）增强型地热系统（EGS）的真实工况下，实时高温与三向应力如何共同影响花岗岩的力学性质（峰值强度、变形参数、破坏模式）及其细观机理？

## Study Area / Data
- **岩石类型**：花岗岩，采自中国湖南省。
- **样品尺寸**：长方体 50 × 50 × 100 mm，符合ISRM建议方法[Ma 2020, pp. 1-4]。
- **矿物组成**（XRD测定）：石英 19.87%，黑云母 12.32%，长石 66.52%，斜绿泥石 1.29%。[Ma 2020, pp. 1-4] Table 1
- **基本物性**：平均密度 2.768 g/cm³，导热系数 2.78 W/mK，P波波速 4179 m/s。[Ma 2020, pp. 1-4]
- **试验条件**：水平应力σ₂ = σ₃取四个水平（0, 20, 40, 60 MPa）；实时高温取五级（室温RT, 100, 200, 300, 400 °C）。[Ma 2020, pp. 1-4]

## Methods
- **试验系统**：自主研发的实时高温真三轴试验系统，可同时施加三向应力（σ₁ < 1000 MPa，σ₂,₃ < 200 MPa）和高温（ < 460 °C），配备闭环伺服控制和温度伺服[Ma 2020, pp. 1-4]。
- **加载程序**：先加热至目标温度，恒温2h；随后以恒定位移速率（0.001 mm/min）分别加载σ₂和σ₃至目标值；再以0.01 mm/min速率加载σ₁直至破坏。[Ma 2020, pp. 4-5]
- **参数获取**：
  - 峰值强度：直接从应力-应变曲线读取；
  - 弹性模量：取50%峰值强度处应力-应变曲线的斜率；
  - 泊松比：取50%峰值强度处两个水平方向泊松比的平均值（μ₁₂、μ₁₃）；
  - 内摩擦角φ与黏聚力c：基于破坏准则反算[Ma 2020, pp. 1-4, 4-5]。
- **细观分析**：采用扫描电子显微镜（SEM）对断面进行形貌观察。[Ma 2020, pp. 5-7]
- **对比分析**：将实时高温下的黏聚力、内摩擦角与高温预处理文献数据进行对比[Ma 2020, pp. 7-7]。

## Key Findings
1. **峰值强度随温度先增后减**：存在与水平应力相关的温度阈值——水平应力0 MPa时阈值为200 °C，20和40 MPa时均为300 °C；阈值处强度较室温分别提高51.9%、71.6%、50.58%和23.1%（对应水平应力0~60 MPa）。超过阈值后强度下降，归因于矿物不均匀热膨胀引发的晶间裂纹。[Ma 2020, pp. 1-4]
2. **脆性破坏特征随应力和温度增加而减弱**：所有试样均表现为脆性破坏，但低水平应力、室温下明显的脆性特征在最高应力（60 MPa）和最高温度（400 °C）时有所减弱；宏观裂纹与应力-应变曲线吻合。[Ma 2020, pp. 1-4, 4-5]
3. **内摩擦角基本不变，黏聚力受温度显著影响**：φ波动于46°左右，温度不敏感；c先增后减，趋势与峰值强度一致。[Ma 2020, pp. 4-5]
4. **弹性模量和泊松比**：100 °C前呈上升趋势，之后波动下降。[Ma 2020, pp. 1-4]
5. **黑云母韧性增强是力学性质改善的主因**：SEM观察显示，石英断面以河流花样和阶步花样为主，阶步花样随温度增多；长石为共轭穿晶剪切断裂；低温下黑云母断口边缘可见脆性透明薄片，而高温下黑云母颗粒呈现韧性增强，降低了岩石脆性并增强了力学性能。[Ma 2020, pp. 5-7]
6. **实时高温黏聚力降幅大于高温预处理**：由于水平应力与实时高温的耦合作用，实时高温条件下黏聚力的劣化程度更明显。[Ma 2020, pp. 7-7]
7. **力学性质的转变机制**：温度引起的强化效应（热膨胀致晶间接触压实、黑云母韧性增强）与劣化效应（过量热裂纹）的竞争结果。[Ma 2020, pp. 5-7]

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 峰值强度随温度先增后减；阈值与水平应力有关（σ₂=σ₃=0 MPa时为200°C，20 MPa和40 MPa时为300°C） | [Ma 2020, pp. 1-4] | 实时高温三轴压缩，σ₂=σ₃=0,20,40,60 MPa，RT~400°C | Fig.4 |
| 内摩擦角约46°，几乎不随温度变化；黏聚力先增后减 | [Ma 2020, pp. 4-5] | 同上 | Fig.5；Wang (2019)模型结论与此一致 |
| 弹性模量和泊松比在100 °C前上升，之后波动下降 | [Ma 2020, pp. 1-4] | 取50%峰值强度处斜率与泊松比平均值 | Figs.6,7 |
| 石英断口以河流花样和阶步花样为主；阶步花样比例随温度升高而增加 | [Ma 2020, pp. 5-7] | SEM, 室温~400°C | Fig.8；阶步属高能脆性断裂 |
| 黑云母颗粒在高温下出现韧性增强，是脆性减弱的主要机制 | [Ma 2020, pp. 5-7] | SEM, 高温耦合应力 | Fig.10；黑云母为云母类矿物，工业上已利用其升温增韧特性 |
| 实时高温条件下的黏聚力劣化程度大于高温预处理条件 | [Ma 2020, pp. 7-7] | 与文献[10,16,32]对比 | Fig.11 |
| 温度阈值之后的强度下降由矿物不均匀热膨胀产生的晶间裂纹造成 | [Ma 2020, pp. 1-4] | 高于温度阈值时 | Chen et al. (2017)[26]支持该解释 |

## Limitations
- 试验仅考虑σ₂ = σ₃的简单应力路径，未涵盖真实HDR中σ₁ > σ₂ > σ₃的真三轴条件[Ma 2020, pp. 7-7]。
- 未考虑孔隙压力和热-流-固耦合效应[Ma 2020, pp. 4-5]。
- 最高温度限于400 °C，花岗岩种类单一，结论外推需谨慎。
- 破坏准则的黏聚力与内摩擦角推导依赖于特定的破坏准则假设。
- 试验加载速率为准静态，未涉及长期蠕变或循环效应。

## Assumptions / Conditions
- 采用岩石力学符号约定（压为正）和固定坐标系[Ma 2020, pp. 1-4]。
- 所有试验遵循相同的加热速率和恒温时间（2 h），认为试样温度均匀。
- 弹性常数取自应力-应变曲线线性段（50%峰值强度处）。
- 峰后行为与破裂形貌的分析基于单批次试验，未考虑岩样非均质性引起的离散。
- 温度强化机制（热膨胀压实+黑云母增韧）与劣化机制（热开裂）的竞争模型基于文献推断。

## Key Variables / Parameters
- 控制变量：水平应力（σ₂ = σ₃），温度（RT~400°C）
- 响应变量：峰值强度、弹性模量、泊松比、黏聚力c、内摩擦角φ
- 矿物学参数：石英、黑云母、长石含量（XRD）
- 断裂形貌特征：河流花样、阶步花样、共轭穿晶断裂、云母韧性增强

## Reusable Claims
1. **存在应力相关的温度阈值，使花岗岩峰值强度从强化转向劣化**——提高水平应力可使温度阈值向更高温移动[Ma 2020, pp. 1-4]。条件：实时高温，σ₂=σ₃约束，花岗岩。
2. **实时高温对岩石黏聚力的劣化程度高于经历同样温度预处理后的劣化**，原因是应力与高温的耦合作用[Ma 2020, pp. 7-7]。
3. **花岗岩的内摩擦角在实时高温条件下可视为常数**（≈46°），其软化律不依赖于温度[Ma 2020, pp. 4-5]。
4. **黑云母颗粒在高温下发生韧性增强，是花岗岩脆性降低和力学性质强化的主要细观机制**[Ma 2020, pp. 5-7]。
5. **弹性模量和泊松比在100 °C附近出现峰值**，之后波动下降，表明初始压实和后续损伤的竞争[Ma 2020, pp. 1-4]。
6. **高温下石英的阶步花样增多，反映能量释放型脆性断裂比例上升**，可辅助判断高温下力学性质的转变[Ma 2020, pp. 5-7]。

## Candidate Concepts
[[Hot Dry Rock (HDR)]], [[Enhanced Geothermal System (EGS)]], [[real-time high temperature]], [[three-dimensional stress]], [[true triaxial test]], [[triaxial compression]], [[temperature threshold]], [[biotite toughness enhancement]], [[fracture morphology]], [[river pattern cleavage]], [[step pattern cleavage]], [[inter-crystalline cracks]], [[thermo-mechanical coupling]], [[cohesion degradation]], [[internal friction angle constancy]], [[granite mechanical properties]]

## Candidate Methods
[[real-time high temperature true triaxial test system]], [[Scanning Electron Microscope (SEM) fracture analysis]], [[X-ray diffraction (XRD) mineral quantification]], [[determination of cohesion and internal friction angle from triaxial tests]], [[elastic modulus extraction at 50% peak strength]], [[Poisson's ratio averaging from two horizontal strains]], [[comparative analysis with pre-treated high temperature data]]

## Connections To Other Work
- **高温预处理数据对比**：本文与Wu et al. (2019)[10]、Zhang et al. (2018)[16]、Griffiths et al. (2017)[32]等的黏聚力、内摩擦角归一化曲线进行比较，发现φ一致而c差异显著，揭示了实时条件下耦合效应的额外贡献[Ma 2020, pp. 7-7]。
- **热-力耦合模型**：验证了Wang & Konietzky (2019)[28]所建模型中“内摩擦角不依赖温度”的结论[Ma 2020, pp. 4-5]。
- **热开裂机理**：引用Chen et al. (2017)[26]关于不均匀热膨胀导致晶间裂纹的解释，与本文阈值后的弱化现象一致[Ma 2020, pp. 1-4]。
- **云母增韧机理**：黑云母增韧与其工业应用（Yu & Dai, 2011[30]）相符，为富黑云母储层EGS设计提供依据[Ma 2020, pp. 5-7]。
- 本研究强调了在EGS热-流-固耦合分析中必须考虑目标储层岩石的温度与应力联合效应，尤其是对于黑云母含量较高的花岗岩[Ma 2020, pp. 5-7]。

## Open Questions
- 中间主应力（σ₂ ≠ σ₃）对实时高温力学行为的影响尚未探索（论文指明将在后续工作中研究）[Ma 2020, pp. 7-7]。
- 孔隙压力参与下的热-水-力全耦合效应需进一步试验验证。
- 花岗岩中黑云母含量与韧性增强程度的定量关系尚未建立。
- 400 °C以上温度、蠕变及循环温度载荷下的行为尚不清楚。
- 实时高温下的黏聚力劣化机制能否通过细观参数（如热开裂密度）定量预测仍有待研究。

## Source Coverage
All six non-empty indexed fragments from the paper were processed.  
- Source blocks: 6  
- Compiled characters: 27,718  
- Total indexed characters: 29,660  
- Coverage ratio by blocks: 1.0  
- Coverage ratio by characters: 0.9345  
All factual statements are derived from the indexed fragments and marked with in-text source labels.
