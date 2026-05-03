---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2023-guo-impact-of-cooling-rate-on-mechanical-properties-and-failure-mechanism-of-sandstone-unde"
title: "Impact of Cooling Rate on Mechanical Properties and Failure Mechanism of Sandstone under Thermal–Mechanical Coupling Effect."
status: "draft"
source_pdf: "data/papers/2023 - Impact of cooling rate on mechanical properties and failure mechanism of sandstone under thermal–mechanical coupling effect.pdf"
collections:
  - "论文"
citation: "Guo, Pingye, et al. “Impact of Cooling Rate on Mechanical Properties and Failure Mechanism of Sandstone under Thermal–Mechanical Coupling Effect.” *International Journal of Coal Science & Technology*, vol. 10, 2023, p. 26, doi:10.1007/s40789-023-00584-7."
indexed_texts: "13"
indexed_chars: "61820"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "61192"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.989841"
coverage_status: "full-index"
source_signature: "fe6bd0ce41088a600be2a0ccc43c404e24abd2f5"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T06:42:58"
---

# Impact of Cooling Rate on Mechanical Properties and Failure Mechanism of Sandstone under Thermal–Mechanical Coupling Effect.

## One-line Summary
通过室内试验与PFC2D颗粒流数值模拟，研究冷却速率（5 °C/min至180 °C/min）对高低温差（150 °C至 −30 °C）及恒定轴压（22 MPa）共同作用下砂岩力学特性与破坏机制的影响，揭示冷却速率增大导致强度、变形参数下降、破坏向外部区域集中及降温阶段以晶内张拉破坏为主、裂纹数与冷却速率呈指数关系的规律[Guo 2023, pp. 1-20]。

## Research Question
在高地温隧道施工等深部工程中，围岩经受高温与低温气流交替作用后受轴向荷载，不同降温速率（模拟不同强度的高低温差作用）如何影响砂岩的力学性能、裂纹扩展路径及细观损伤机制？[Guo 2023, pp. 1-3]

## Study Area / Data
- 砂岩样品取自高地温隧道（如川藏铁路桑珠岭、拉月隧道）广泛分布的地层，取自同一岩块，通过密度和纵波波速筛选，加工为直径50 mm、高度100 mm的圆柱试样，符合ISRM要求。
- 矿物组成（XRD）：石英28.3%、钠长石39.5%、黏土矿物（高岭石、绿泥石、伊利石）26.8%，另含少量方解石（2.3%）和微斜长石（3.1%）。天然密度1.88 ± 0.3 g/cm³[Guo 2023, pp. 2-3]。

## Methods
### 室内试验
- 系统组合：AE监测系统（PCI-2，40 dB前置放大增益，50 dB阈值）、2000 kN电液伺服三轴试验机、GD8/10高低温试验箱（−80 °C~150 °C，有效容积0.01 m³）。
- 试验流程：（1）以2 MPa/min加载轴压至22 MPa（约UCS的60%），稳压5~10 min；（2）以5 °C/min升温至150 °C，恒温2 h；（3）分别以5 °C/min和10 °C/min降温至−30 °C，恒温2 h，同时进行AE定位；（4）在−30 °C下以0.1 mm/min进行单轴压缩至破坏，记录力‑位移数据（每500 ms一次）。每组重复两样[Guo 2023, pp. 3-4]。
### 数值模拟
- 基于PFC2D的晶粒模型（GBM）建立非均质等效砂岩模型，高100 mm、宽50 mm，含17 393个刚性颗粒（半径0.15~0.40 mm均匀分布）。矿物晶内采用线性平行黏结模型（PB），晶界采用光滑节理模型（SJ）。
- 根据XRD结果确定矿物含量并标定微观参数（表1）。热力耦合模拟中，通过Fish函数分别赋予不同矿物导热系数，实现热阻非均质分布；壁面温度按回调函数连续变化，加热速率5 °C/min，至150 °C后恒温至温度场均匀，再以5、10、20、50、100、180 °C/min降温至−30 °C。轴向伺服多梯度分级加载实现恒轴压22 MPa。计算中不平衡力比达到0.0001后进入下一步。
- 单轴压缩模拟（加载速率0.1 mm/min）监测微裂纹及声发射，并利用Fish函数与Scalar模块生成微裂纹热点图以表征裂纹密度[Guo 2023, pp. 6-10]。

## Key Findings
1. **宏观力学性能**：随冷却速率增大，峰值应力、峰值应变和弹性模量均呈下降趋势。与未处理室温砂岩相比，冷却速率5~180 °C/min下峰值应力分别下降15%、23%、25%、37%、41%和54%；峰值应变下降20%~44%；弹性模量下降5%~21%。弹性模量变化幅度相对较小（室温9.7 GPa，180 °C/min时7.95 GPa）[Guo 2023, pp. 8-9]。
2. **单轴破坏特征**：冷却速率增大使裂纹扩展路径由内而外均匀连通转为从外部区域优先破坏，宏观上多呈X型共轭破坏且次级裂纹增多，破碎度提高[Guo 2023, pp. 9-10]。但冷却速率对微裂纹类型比例（晶内/晶界）无显著影响[Guo 2023, pp. 10-11]。
3. **降温阶段细观损伤**：降温阶段以晶内破坏为主，晶界破坏占比小；当冷却速率<20 °C/min时微裂纹空间分布较均匀，>20 °C/min时裂纹显著集中于试件外部区域。微裂纹总数随冷却速率呈指数增长（相邻速率增量13%~71%），50 °C/min为累积损伤加速的拐点[Guo 2023, pp. 11-13]。
4. **应力分布与损伤机制**：恒轴压作用下，降温过程中轴向为压应力集中，张应力主要沿径向分布；微裂纹倾角多集中在70°~110°（径向张拉键断裂为主）。外部区域过高的温度梯度是损伤集中的主因，降温损伤由轴向荷载、温度梯度及相邻矿物热失配共同诱发[Guo 2023, pp. 17-19]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| UCS较未处理样下降幅度：5 °C/min降15%，10 °C/min降23%，20 °C/min降25%，50 °C/min降37%，100 °C/min降41%，180 °C/min降54% | [Guo 2023, pp. 8-9] | 轴压22 MPa维持；150 °C→−30 °C降温；数值模拟结果 | 弹性模量降5%~21%；峰值应变降20%~44% |
| 降温阶段微裂纹数与冷却速率呈指数关系，50 °C/min以上损伤增速显著加快 | [Guo 2023, pp. 13,15] | GBM模型，全部冷却速率 | 裂纹总数增量：13%、29%、60%、71%、47% |
| 冷却速率>20 °C/min时外部区域（区I、V）微裂纹数明显多于内部，如50 °C/min时区I = 149，区III = 65；100 °C/min时区I = 324，区III = 113 | [Guo 2023, pp. 12-13] | 等距5分法统计径向裂纹数 | 轴向非对称，区I总最大 |
| 降温阶段晶内裂纹占比始终高于晶界，且钠长石与黏土矿物损伤最严重，高冷却速率下钠长石损伤超越黏土矿物 | [Guo 2023, pp. 15,17] | 数值模拟，各类矿物裂纹计数 | 损伤严重程度与矿物组分、冷却速率均相关 |
| 温度边界达−30 °C时，内部最大温度（探针3）随冷却速率升高：5 °C/min为−14.89 °C，180 °C/min为142.53 °C，内外温差达172.53 °C | [Guo 2023, pp. 15,表2] | 数值模拟 | 温度梯度增大导致外部热应力集中 |
| 降温阶段张裂纹倾角集中在70°~110°，以径向黏结断裂为主 | [Guo 2023, pp. 17-18] | 50 °C/min例 | 轴向压应力使张应力转向径向分布 |
| AE事件在5 °C/min降温时分布随机，10 °C/min降温时外部区域密度略增且总数增多 | [Guo 2023, pp. 4-5] | 室内试验，中段20 mm区域 | 与模拟裂纹集中结论一致 |

## Limitations
- 室内试验受设备限制，仅实现了5 °C/min和10 °C/min两种降温速率[Guo 2023, pp. 3-4]。
- 数值模型未模拟原始裂隙闭合行为，所得应力‑应变曲线缺少压密阶段[Guo 2023, pp. 6-7]。
- 模型假设矿物导热系数和热膨胀系数不随冷却速率变化，可能高估热传导均匀性[Guo 2023, pp. 15,17]。
- 研究仅针对一种砂岩，温度区间固定（150 °C→−30 °C）、轴压固定（22 MPa），结论外推需谨慎[Guo 2023, pp. 2-3]。
- 二维模型无法反映三维应力路径及真实矿物连通性对损伤的影响[Guo 2023, pp. 6]。
- 每种试验条件下仅重复两个样品，统计意义有限[Guo 2023, pp. 3]。

## Assumptions / Conditions
- 轴向压力始终维持22 MPa（约UCS的60%），降温速率在5~180 °C/min范围内变化。
- 加热速率固定为5 °C/min，热平衡后降温；恒温保持2 h以确保温度场均匀（数值模拟在加热后亦保持至均匀）。
- 数值模型认为导热系数、比热容、热膨胀系数为常数，不随温度与降温速率改变。
- GBM模型中晶内采用PB模型（可模拟热膨胀），晶界采用SJ模型；颗粒不可破坏，强度由黏结模型控制。
- 壁面温度作为热边界连续变化，样品与外界热交换通过热管实现；不考虑对流与辐射细节。
- 数值试样尺寸与实验室一致（50 mm×100 mm），矿物含量及粒径分布参照XRD与真实岩样。

## Key Variables / Parameters
- **自变量**：降温速率（5、10、20、50、100、180 °C/min）
- **响应变量**：单轴抗压强度（UCS）、峰值应变、弹性模量；微裂纹数量与类型（晶内抗拉/剪切、晶界抗拉/剪切）；微裂纹空间分布（径向分区密度、热点图）；AE计数及累积计数；宏观破坏模式与破碎度
- **控制变量**：轴压22 MPa；加热目标温度150 °C；冷却目标温度−30 °C；恒温时间2 h；加载速率0.1 mm/min（压缩）
- **数值模型参数**：颗粒半径0.15–0.40 mm；各矿物热导率、热膨胀系数、比热容（见表1）；PB及SJ黏结强度与刚度等

## Reusable Claims
1. 在恒轴压低温降温条件下，砂岩的峰值应力、峰值应变和弹性模量均随降温速率增大而单调递减，弹性模量下降幅度小于强度与峰值应变[Guo 2023, pp. 8-9]。
2. 当降温速率超过约20 °C/min时，降温阶段的微裂纹将明显集中于试件外部区域，外部先发生破坏，导致后续压缩裂纹由外向内扩展[Guo 2023, pp. 11-13]。
3. 降温过程中损伤以晶内张拉破坏为主导，晶界裂纹占比较小；微裂纹总数随降温速率呈指数增长，50 °C/min可作为损伤加速的分界点[Guo 2023, pp. 13,15]。
4. 在恒定轴压作用下，降温阶段的应力分布表现为轴向受压、径向受拉，使得张拉裂纹主要沿径向黏结断裂，而非自由热应力条件下的外拉内压模式[Guo 2023, pp. 17-18]。
5. 外部区域过高的温度梯度是降温损伤集中于该区域的主要原因；损伤由轴向荷载、温度梯度与矿物热膨胀失配共同驱动[Guo 2023, pp. 17,19]。
6. 当环境温度变化梯度超过0.3 °C/mm时，温度梯度引起的热应力对微裂纹形成的影响不可忽略（源自Fredrich & Wong, 1986等，本研究引用并印证）[Guo 2023, pp. 13,15]。

## Candidate Concepts
- [[热力耦合效应|thermal–mechanical coupling]]
- [[冷却速率|cooling rate]]
- [[砂岩|sandstone]]
- [[晶粒模型|grain-based model (GBM)]]
- [[微裂纹热点图|microcrack hotspot map]]
- [[温度梯度|temperature gradient]]
- [[晶内破坏|intragrain failure]]
- [[径向黏结断裂|radial bond fracture]]
- [[外部区域损伤集中|exterior damage concentration]]
- [[声发射事件分布|AE event distribution]]
- [[力链|force chain]]
- [[热失配|thermal stress mismatch]]

## Candidate Methods
- [[声发射监测|AE monitoring]]
- [[三轴试验系统|triaxial test system]]
- [[高低温试验箱|high & low temperature test chamber]]
- [[PFC2D|PFC2D]]
- [[晶粒模型建模|grain-based modeling (GBM)]]
- [[微裂纹热点图算法|microcrack hotspot map via Fish function]]
- [[热管热阻分布|thermal pipe resistance distribution]]
- [[伺服多梯度分级加载|multi-gradient graded axial loading via servo]]
- [[回调函数连续变温|wall temperature callback function]]

## Connections To Other Work
- 降温过程中的外部拉应力、内部压应力分布特征与Kim等(2014)对预加热岩石冷却的结论相符，但本研究表明恒轴压改变了应力场，使张应力转为径向分布[Guo 2023, pp. 17-18]。
- Wu与Liu(2003)的均匀加热与骤热分类，以及温度变化率5 °C/min时约0.27 °C/mm的温度梯度，呼应Fredrich & Wong(1986)提出的梯度>0.3 °C/mm时热应力致裂显著的结论，本研究在实验和模拟中验证了该阈值[Guo 2023, pp. 13,15]。
- 与Zuo等(2012)、Yin等(2016)的热‑力耦合花岗岩断裂研究思路相似，但本文关注较低温度区间（<200 °C）和极低温气流冲击，并引入实时降温与轴压的共同作用[Guo 2023, pp. 2-3]。
- 模型校准参考了Peng等(2018)的“试错法”颗粒流标定流程；热参数赋值借鉴了Fish函数非均质导热方法，区别于多数忽略矿物导热差异的研究[Guo 2023, pp. 6-8]。

## Open Questions
- 不同轴压水平（如低于或高于60%UCS）对降温阶段应力分布及微裂纹方向的影响尚待系统探究。
- 多次热循环或长期蠕变效应下，冷却速率造成的损伤累积规律是否变化，现有数据未覆盖。
- 三维应力状态和实际隧道围岩的约束条件对“外‑内”破坏模式的影响需通过三维模拟或现场监测验证。
- 矿物导热系数和热膨胀系数的温度/速率依赖性若被考虑，是否改变损伤集中区的范围和速率阈值？
- 如何将该实验室尺度的冷却速率损伤规律推广至隧道施工通风降温的工程尺度，还需尺度效应与等效准则研究。

## Source Coverage
所有13个非空索引片段均已处理并编入本页。片段总字符数61 820，实际编译字符数61 192，以块计覆盖率为100%，以字符计覆盖率为98.98%（coverage_ratio_by_blocks=1.0, coverage_ratio_by_chars=0.989841）[Source Coverage audit data provided].
