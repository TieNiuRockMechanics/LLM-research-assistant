---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-guo-impact-of-cooling-rate-on-mechanical-properties-and-failure-mechanism-of-sandstone-unde"
title: "Impact of Cooling Rate on Mechanical Properties and Failure Mechanism of Sandstone under Thermal–Mechanical Coupling Effect."
status: "draft"
source_pdf: "data/papers/2023 - Impact of cooling rate on mechanical properties and failure mechanism of sandstone under thermal–mechanical coupling effect.pdf"
collections:
  - "论文"
citation: "Guo, Pingye, et al. “Impact of Cooling Rate on Mechanical Properties and Failure Mechanism of Sandstone under Thermal–Mechanical Coupling Effect.” *International Journal of Coal Science & Technology*, vol. 10, 2023, p. 26, doi:10.1007/s40789-023-00584-7."
indexed_texts: "13"
indexed_chars: "61820"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T12:46:29"
---

# Impact of Cooling Rate on Mechanical Properties and Failure Mechanism of Sandstone under Thermal–Mechanical Coupling Effect.

## One-line Summary
利用单轴压缩实验与PFC颗粒流数值模型，揭示了冷却速率对高温砂岩力学性质（强度、变形模量）和破坏机制（微裂纹分布、主控断裂类型）的显著影响，指出高冷却速率加剧了外部区域的颗粒内损伤和径向键断裂，使宏观破坏趋于X型共轭破裂。

## Research Question
深部工程开挖后，高温岩石受低温气流（即机械通风或环境温差）的快速冷却作用，其力学性质和破坏模式如何随冷却速率变化？[Guo 2023, pp. 1-2]

## Study Area / Data
- **岩性**：高岩温隧道中广泛分布的砂岩 [Guo 2023, pp. 2-3]。  
- **样品**：均取自同一块岩石，加工成直径50 mm、高100 mm圆柱，满足ISRM标准；通过密度和纵波波速筛选，天然密度1.88±0.3 g/cm³ [Guo 2023, pp. 2-3]。  
- **矿物组成（XRD）**：石英28.3%，钠长石39.5%，粘土矿物（高岭石、绿泥石、伊利石）26.8%，方解石2.3%，微斜长石3.1% [Guo 2023, pp. 2-3]。  
- **实验数据**：室温与TM耦合（加热至200°C，以5、10°C/min冷却至−30°C）下的单轴压缩应力-应变曲线、AE事件空间分布及宏观破坏照片 [Guo 2023, pp. 3-6]。  
- **数值模拟数据**：相同砂岩的PFC2D-GBM模型，冷却速率扩展至5, 10, 20, 30, 40, 50, 80, 100, 150, 180°C/min下的力学响应、微裂纹数量及空间分布 [Guo 2023, pp. 7-15]。

## Methods
1. **热-力耦合实验系统**：集成AE监测（PCI-2系统）、2000 kN电液伺服三轴仪及高低温环境箱，实现从200°C（恒温2小时）以可控速率（5、10°C/min）实时冷却至−30°C，随即在−30°C下以0.1 mm/min速率进行单轴压缩至破坏，同步采集力-位移和AE事件 [Guo 2023, pp. 2-6]。  
2. **基于颗粒流的等效非均质数值模型（PFC2D-GBM）**：  
   - 依据XRD结果，利用rblock模块生成矿物颗粒边界；矿物内部采用线性平行键模型，矿物间采用光滑节理模型，以再现晶界滑移与颗粒破碎 [Guo 2023, pp. 6-7]。  
   - 热计算通过热管网络实现，对不同矿物的热导率、线膨胀系数、比热容分别赋值（通过Fish函数），并依据热阻公式 (4)、(5) 计算管段热阻，边界墙体温度由Fish回调函数连续控制 [Guo 2023, pp. 7-9]。  
   - 应力加载采用多梯度分级加载公式（式1），以降低扰动；每一步迭代至不平衡力比达0.0001 [Guo 2023, pp. 6-7]。  
   - 微裂纹空间分布以“微裂纹热点图”表征，通过Fish与Scalar模块搜索并可视化测量单元内的微裂纹密度 [Guo 2023, pp. 9-12]。  
3. **分析流程**：实验室结果与数值模型相互校准（室温、5°C/min、10°C/min），并利用后者推演更广冷却速率下的力学行为与内部损伤演化 [Guo 2023, pp. 7-9]。

## Key Findings
- **力学参数随冷却速率增大而劣化**：实验显示，室温至TM耦合（5°C/min）UCS降低约16%，5°C/min与10°C/min之间UCS下降约3%；模拟结果进一步表明，峰值应力、峰值应变和弹性模量均随冷却速率（5～180°C/min）增加而单调减小，破坏后的破碎程度逐渐上升 [Guo 2023, pp. 3-6, 9-12]。  
- **冷却阶段的损伤空间分布**：低冷却速率（5°C/min）下AE事件随机分布；10°C/min时外部区域AE密度增大，表明外部损伤加剧 [Guo 2023, pp. 3-6]。数值模拟定量显示，冷却速率≤20°C/min时微裂纹在各径向区域均匀分布；>20°C/min后呈外多内少特征，如50°C/min时最外区（I）微裂纹149条，最内区（III）仅65条 [Guo 2023, pp. 12-15]。  
- **破坏机制**：冷却阶段以颗粒内破坏为主，微裂纹数量与冷却速率呈指数关系；轴向加载时，拉应力主要沿径向分布，冷却期的损伤本质上是径向键的断裂 [Guo 2023, pp. 12-15]。  
- **宏观破坏模式转变**：室温下砂岩呈典型斜剪破坏，而TM耦合后（如50°C/min代表性情形）呈现X型共轭破坏，伴生明显次级裂纹，整体破碎度提高 [Guo 2023, pp. 9-12]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| UCS较室温降低约16%，5和10°C/min间仅差约3%；峰值应力和弹性模量随冷却速率增大而减小，破碎度增加 | [Guo 2023, pp. 3-6, 9-12] | 加热至200°C，实时冷却至−30°C后单轴压缩；数值模拟冷却速率5–180°C/min | 实验仅5和10°C/min，模拟将此趋势外推 |
| 10°C/min冷却时AE事件在外部区域聚集，数量较5°C/min增多 | [Guo 2023, pp. 3-6] | 实时冷却阶段中部20 mm高度AE定位 | 仅两组冷却速率对比，样本数有限 |
| 冷却阶段微裂纹数量与冷却速率呈指数关系；冷却速率>20°C/min后微裂纹外多内少，50°C/min时区域I 149条，III 65条 | [Guo 2023, pp. 12-15] | PFC2D-GBM模型，冷却至−30°C，径向等距划分为I–V区 | 模型为2D，热参数基于矿物组成 |
| 冷却阶段以颗粒内破坏为主，轴向加载时拉应力主要沿径向分布，径向键断裂主导 | [Guo 2023, pp. 12-15] | 数值模拟热固耦合分析 | 基于颗粒间键的断裂统计与应力分布 |
| TM耦合处理后单轴破坏由斜剪转变为X型共轭破坏，并出现二级裂纹 | [Guo 2023, pp. 3-6, 9-12] | 实验室观察（室温 vs. 50°C/min代表） | 室温试验明确为斜剪，高冷却速率模拟呈X型破坏 |

## Limitations
- 实验装置限制，仅测试了5°C/min和10°C/min两个冷却速率，更高速率的结论依赖数值模型外推，且模型校准仅基于上述两点 [Guo 2023, pp. 3-6]。  
- 数值模型为二维PFC2D，无法完全反映三维热传导、裂纹空间扩展和能量释放特征。  
- 研究对象仅为一种特定矿物组成的砂岩，结论向其他岩类（如花岗岩、石灰岩）的推广性有待验证。  
- 模拟中未考虑流体对流、孔隙水相变及湿度对热传导和力学性能的影响。  
- 未从索引片段中确认是否分析了循环冷却或长期强度退化效应。

## Assumptions / Conditions
- **实验**：试样均质取自同一岩块；加热至200°C并恒温2h以均匀热透；冷却过程为表面接触换热，环境温度−30°C；单轴压缩速率0.1 mm/min为静态加载 [Guo 2023, pp. 2-6]。  
- **数值模型**：矿物颗粒视为圆形（半径0.15–0.40 mm均匀分布）；颗粒间热传导仅通过热管，热阻计算基于平均孔隙率和热导率；矿物热参数（热导率、热膨胀系数、比热）为定值，见表1（具体数值未在该片段给出）；力学接触采用平行键和光滑节理模型，并经过室温与两种冷却速率下的宏观力学参数标定；地应力环境通过先施加围压（22 MPa）再卸除来模拟卸荷取心过程 [Guo 2023, pp. 6-9]。  
- **分析假设**：微裂纹热点图的搜索半径和单位网格尺寸足以反映损伤梯度；径向分区概括裂纹分布特征；温度梯度及矿物间热应力失配是冷却阶段损伤的主要诱因 [Guo 2023, pp. 2, 12-15]。

## Key Variables / Parameters
- **冷却速率**：实验5, 10°C/min；模拟5, 10, 20, 30, 40, 50, 80, 100, 150, 180°C/min  
- **热处理制度**：目标温度200°C，恒温2 h；冷却终点−30°C  
- **力学指标**：单轴抗压强度（UCS）、峰值应变、弹性模量  
- **声发射参数**：AE事件计数、事件空间分布密度  
- **微裂纹统计**：冷却阶段及加载后微裂纹总数、径向分区（I–V）计数、微裂纹热点图密度  
- **破坏模式**：宏观裂纹形态（斜剪、X型共轭、次级裂纹）  
- **热物理参数**：各矿物的热导率、线膨胀系数、比热容（具体数值未在本片段列出）  
- **数值模型控制参数**：颗粒半径范围、孔隙率、平行键/光滑节理微观参数、热管热阻、墙体温度回调函数、多梯度加载衰减系数β  
- **几何与工艺参数**：加载速率0.1 mm/min，数值轴向目标应力22 MPa，测量球半径等

## Reusable Claims
1. **冷却速率对砂岩强度的损伤规律**：对于200°C高温后的钠长石-石英-粘土质砂岩，当冷却速率从5°C/min增至180°C/min时，其UCS和弹性模量单调下降（5 vs 10°C/min UCS下降约3%），峰值应变同步减小。这一趋势在实验室和标定后的PFC2D-GBM模型中一致成立。 [Guo 2023, pp. 3-6, 9-12]  
   *条件*：岩石须经历不低于200°C的均热，冷源温度−30°C，且矿物组成与本试样类似。  
   *限制*：直接实验证据限于≤10°C/min；高冷却速率结论来自2D模拟。  
2. **高冷却速率下的外部集中损伤模式**：当冷却速率超过20°C/min时，热冲击诱发的微裂纹呈现显著的外部集中特征（如50°C/min时最外层微裂纹数约为最内层的2.3倍），而低冷却速率时裂纹分布均匀。这是因为外部温变速率快，热应力率先超过强度。 [Guo 2023, pp. 12-15]  
   *条件*：基于PFC2D-GBM模型，未考虑蠕变与流固耦合；岩样视为径向对称。  
   *限制*：实验结果仅间接由AE分布支持（10°C/min外部事件增多），未直接验证>20°C/min的物理试验。  
3. **热-力耦合破坏机理**：在急冷条件下，砂岩损伤初始于颗粒内部的热应力开裂，随后在轴向载荷下沿径向拉应力集中带扩展，最终形成X型共轭剪切破坏。这与室温下的单一斜剪破坏截然不同。 [Guo 2023, pp. 9-12]  
   *条件*：适用于非均质脆性砂岩，且冷却速率足以引发显著温度梯度。  
   *限制*：机制解释源于数值模型的键断裂分析，真实岩石的矿物解理等未完全体现。

## Candidate Concepts
- [[thermal-mechanical coupling]]  
- [[cooling rate]]  
- [[sandstone failure mechanism]]  
- [[acoustic emission]]  
- [[grain-based model (GBM)]]  
- [[particle flow code (PFC)]]  
- [[microcrack hotspot map]]  
- [[intragrain failure]]  
- [[radial bond fracture]]  
- [[temperature gradient]]  
- [[thermal stress mismatch]]  
- [[X-type conjugate failure]]  
- [[uniaxial compressive strength (UCS)]]  
- [[elastic modulus degradation]]  
- [[high-temperature tunnel]]  
- [[thermal shock]]

## Candidate Methods
- [[real-time cooling experiment]]  
- [[uniaxial compression test]]  
- [[PFC2D GBM]]  
- [[smooth joint model]]  
- [[linear parallel bond model]]  
- [[Fish function thermal coupling]]  
- [[thermal pipe model]]  
- [[multi-gradient graded loading]]  
- [[AE monitoring]]  
- [[X-ray diffraction (XRD) for mineral quantification]]  
- [[microcrack hotspot mapping]]  
- [[servo-controlled boundary]]  
- [[callback function for transient thermal boundary]]

## Connections To Other Work
- 本文直接引用了以往高温岩石物性研究：Zhao et al. (2018) 发现花岗岩热导率随温度非线性下降，Jiang et al. (2018) 给出波速线性下降与渗透率指数上升，为本模型区分矿物热导率、考虑热致损伤提供了参考 [Guo 2023, pp. 2]。  
- 与花岗岩热开裂数字图像研究 (Yu et al. 2014) 的思路相近，但本文进一步量化了冷却速率对微裂纹空间分布和数量的指数关系，并引入了光滑节理模型模拟晶界效应。  
- 与Zhang et al. (2019) 在花岗岩中揭示的温度与预制裂纹共同主导破坏模式的结论互补，本文侧重于单一冷却速率变量对完整砂岩破坏模式的转变。  
- 主题上可连接至 [[rock thermal damage]]、[[cooling shock on granite]]、[[microcrack quantification in PFC]]、[[deep mining thermal hazards]] 等方向。

## Open Questions
- 冷却速率大于180°C/min或极缓慢冷却（<1°C/min）时力学性质和破坏模式如何变化？  
- 其他高岩温岩石（如花岗岩、石灰岩）在类似冷却条件下的响应是否遵循相同的指数-外聚损伤规律？  
- 真实隧道环境中，低温气流速度和湿度对等效冷却速率及岩石孔隙压力的影响尚未纳入。  
- 数值模型为2D，三维应力状态下热-力耦合的破裂路径、能量释放及延性–脆性转变待探讨。  
- 本文仅考察单次急冷后的单轴压缩，循环热冲击或长期蠕变效应未从索引片段中确认。  
- 冷却造成的微裂纹网络对渗透性、流体流动的影响及与断裂带自愈合的关联未被覆盖。

## Source Coverage
本页基于论文索引的全部13个片段撰写，覆盖了从摘要、引言（文献回顾与研究契机）、实验装置/流程（2–3页，3–6页）、数值模型建立及热-力计算方法（6–9页）、数值模拟分析与实验室结果对比（9–15页）等主体内容。具体覆盖范围包括：研究背景与关键科学问题、样品制备与设备、实验步骤（仅两个冷却速率）、AE与宏观破坏观测、GBM建模与热管/热阻设定、微裂纹热点图生成流程、力学参数演化数据、裂纹空间分布定量分析。可能缺失的部分有：详细的微观参数标定表（表1仅引用，无具体数值）、结论章节的工程建议、更多不同冷却速率下的实验验证细节、讨论中对矿物热膨胀系数差异与强度之间关系的深入分析，以及完整的数值模型网格或接触参数列表。总体而言，片段覆盖偏重于实验设计、数值方法以及核心机理揭示，对研究结果的普适性讨论和未来工作的交代相对简略，读者需结合全文以获取完整数据。
