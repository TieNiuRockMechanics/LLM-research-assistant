---
type: "paper"
schema_version: "paper-v4-2026-04-30"
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
nonempty_source_blocks: "14"
compiled_source_blocks: "14"
compiled_source_chars: "60501"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.919538"
coverage_status: "full-index"
source_signature: "c929be74fc9cc7c44a920c161b3527e9e993406a"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T01:59:56"
---

# An Insight into Pore-Network Models of High-Temperature Heat-Treated Sandstones Using Computed Tomography.

## One-line Summary
利用高分辨率微CT技术，探究了三种印度砂岩（Dholpur、Jodhpur、Gondwana）在25°C至800°C热处理条件下的微观结构变化、孔隙空间演化与孔隙网络属性（配位数、孔喉半径等），发现富含黏土矿物的Gondwana砂岩对高温最为敏感，且370°C–680°C为岩石结构损伤的主要温度窗口。[Mahanta 2020, pp. 1-2; Mahanta 2020, pp. 14-15; Mahanta 2020, pp. 19-20]

## Research Question
高温热处理如何引起不同矿物组成（尤其是黏土含量不同）的砂岩在孔隙尺度上发生微观结构改变？具体的孔隙空间演化规律、孔隙网络配置（配位数、孔喉尺寸等）如何随温度而变化？[Mahanta 2020, pp. 1-2; Mahanta 2020, pp. 6-7]

## Study Area / Data
- **三种印度砂岩样品**：[Mahanta 2020, pp. 7-8]
  - **Dholpur sandstone (DS)**：采自印度拉贾斯坦邦；矿物组成为石英(94.3%)、正长石(5.4%)、斜辉石(0.3%)。[Mahanta 2020, pp. 2-3]
  - **Jodhpur sandstone (JS)**：采自印度拉贾斯坦邦；矿物组成为石英(83.9%)、迪开石(5.7%)、高岭石(5.5%)、方解石(3.5%)、长石(0.8%)、尖晶石(0.5%)。[Mahanta 2020, pp. 2-3]
  - **Gondwana sandstone (GS)**：采自印度贾坎德邦；矿物组成为石英(50.8%)、菱铁矿(18.2%)、白云母(18.7%)、伊利石(9.1%)、高岭石(2.5%)、白云石(0.8%)。[Mahanta 2020, pp. 2-3]
- **热处理温度**：25°C（室温）、200°C、400°C、600°C、800°C；加热速率5°C/min，达到目标温度后恒温3小时，随后空气冷却至室温。[Mahanta 2020, pp. 7-8]
- **样本尺寸**：用于CT扫描的小样品平均直径2–3 mm；分析选取的代表性体积元(REV)为600×600×600 μm³的立方体。[Mahanta 2020, pp. 8-9; Mahanta 2020, pp. 12-13]

## Methods
1. **图像采集**：使用Xradia Versa 520微CT仪器，有效体素尺寸0.7 μm，源距样品约10 mm，探测器距样品9 mm，20倍光学放大，源参数100.102 kV / 89.7 μA。[Mahanta 2020, pp. 4-5; Mahanta 2020, pp. 8-9]
2. **图像处理与分割**：通过Avizo 9.0软件，依次进行各向异性扩散滤波去噪、反锐化掩膜锐化，以及基于分水岭膨胀的三阶段分割流程（先识别边界，再分别阈值化孔隙/基质，最后用分水岭算法分配边界体素）。[Mahanta 2020, pp. 9-11]
3. **REV确定**：以孔隙体积随立方体边长的变化为标准，当边长超过550 μm后孔隙体积趋于稳定且标准差极小，故选择600 μm边长的立方体作为REV。[Mahanta 2020, pp. 11-13]
4. **孔隙数据提取**：通过交互式阈值与轴连通性模块，分别计算总孔隙体积、连通孔隙体积和非连通孔隙体积。[Mahanta 2020, pp. 12-14]
5. **孔隙网络模型生成**：基于连通孔隙，使用最大球（maximal ball）等算法提取等效孔隙和喉道，获得等效孔隙半径、配位数、等效喉道半径和喉道通道长度等属性。[Mahanta 2020, pp. 13-15; Mahanta 2020, pp. 18-19]
6. **热重分析**：在惰性气氛中，从室温以5°C/min升温，测量约16 mg样品的重量变化。[Mahanta 2020, pp. 13-14]

## Key Findings
1. **主要结构损伤温度窗口**：三种砂岩在370°C–680°C范围内均经历显著的结构损伤，可归因于矿物热分解、脱羟基、挥发、氧化，以及α-石英在573°C（JS）和579°C（GS）的相变。[Mahanta 2020, pp. 14-15; Mahanta 2020, pp. 19-20]
2. **黏土含量的关键影响**：GS黏土矿物含量最高（约30%），受高温影响最大，600°C时孔隙率较常温增幅达71.09%。[Mahanta 2020, pp. 2-3; Mahanta 2020, pp. 12-13; Mahanta 2020, pp. 15-16]
3. **孔隙率演化差异**：
   - DS：总孔隙率由25°C的20.02%升至800°C的24.79%（增加23.84%），整体呈上升趋势。[Mahanta 2020, pp. 12-13]
   - JS：总孔隙率从25°C的14.37%升至600°C的20.03%，随后在800°C下降至16.89%。[Mahanta 2020, pp. 12-13]
   - GS：总孔隙率从25°C的13.99%升至600°C的23.94%，800°C时略降至23.47%。[Mahanta 2020, pp. 12-13]
4. **孔隙网络属性变化**：
   - DS：平均配位数在600°C达到最大（7.097），平均喉道通道长度在800°C达到最大（55.832 μm）。[Mahanta 2020, pp. 18-20]
   - JS：平均配位数在800°C达到最大（6.953），但平均孔隙半径和喉道半径在600°C后下降，可能与Ca(OH)₂（portlandite）的形成有关。[Mahanta 2020, pp. 18-20; Mahanta 2020, pp. 15-16]
   - GS：由于非连通孔隙比例高（常温下约占40%），仅基于连通孔隙的PNM未能观察到明确趋势。[Mahanta 2020, pp. 15-16; Mahanta 2020, pp. 18-19]
5. **热重分析验证**：在370°C–680°C区间，DS、JS和GS分别失重0.734%、1.585%和8.112%，证实GS因黏土矿物分解而更易受热损伤。[Mahanta 2020, pp. 15-16]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| DS在800°C时总孔隙率为24.79%（较常温增23.84%） | [Mahanta 2020, pp. 12-13] | 600×600×600 μm³ REV，基于微CT分割 | DS常温孔隙率为20.02% |
| GS在600°C时总孔隙率增幅达71.09% | [Mahanta 2020, pp. 12-13] | 600×600×600 μm³ REV，基于微CT分割 | GS常温孔隙率为13.99%，黏土矿物约30% |
| JS的孔隙率在600°C（20.03%）后于800°C降至16.89% | [Mahanta 2020, pp. 12-13] | 600×600×600 μm³ REV，基于微CT分割 | 可能因portlandite形成，TG曲线在680°C后有增重段 |
| DS平均配位数最大值出现在600°C（7.097） | [Mahanta 2020, pp. 18-20] | 仅使用连通孔隙生成PNM | 800°C时略降至6.457 |
| JS平均配位数最大值出现在800°C（6.953） | [Mahanta 2020, pp. 18-20] | 仅使用连通孔隙生成PNM | 喉道等效半径在600°C后下降 |
| 370°C–680°C为三种砂岩共同的主要结构变化窗口 | [Mahanta 2020, pp. 19-20] | 综合显微观察、TG与PNM结果 | 与α-β石英相变（573°C）及黏土矿物分解重合 |
| TGA中GS失重8.112%（室温–680°C） | [Mahanta 2020, pp. 15-16] | 升温速率5°C/min，惰性气氛 | 远高于DS（0.734%）和JS（1.585%） |
| DS常温孔隙率为20.02%，JS为14.37%，GS为13.99% | [Mahanta 2020, pp. 12-13] | 室温25°C，微CT分割 | GS含近40%非连通孔隙 |
| α-石英相变在JS约573°C，GS约579°C可观察到 | [Mahanta 2020, pp. 14-16] | 由TG曲线和文献交叉推断 | 相变伴随2%体积膨胀 |
| 微CT有效体素尺寸0.7 μm | [Mahanta 2020, pp. 8-9; Mahanta 2020, pp. 4-5] | 20倍光学放大 | 物理分辨率可能低于亚微米 |

## Limitations
- 研究中未对不同矿物相进行分类和单独标记，所有亮像素统一视为“基质”。[Mahanta 2020, pp. 10-11]
- 孔隙网络模型仅基于连通孔隙体积生成，GS因非连通孔隙比例高，其PNM结论的普适性受限。[Mahanta 2020, pp. 15-16; Mahanta 2020, pp. 18-19]
- 最大球算法对分辨率敏感，精细的喉道尺寸可能被低估，影响PNM精度。[Mahanta 2020, pp. 13-14]
- 所分析样本尺寸（2–3 mm直径）较小，用于REV的600 μm立方体可能仍不足以完全代表高度非均质的岩石。[Mahanta 2020, pp. 7-8; Mahanta 2020, pp. 11-13]
- 热处理采用空气冷却，可能引入额外的热应力损伤，但未与慢速炉冷对比。[Mahanta 2020, pp. 7-8]

## Assumptions / Conditions
- **热平衡假定**：3小时恒温处理足以使小样本达到均匀热平衡，忽略内部温度梯度。[Mahanta 2020, pp. 7-8]
- **冷却路径一致性**：所有样品均为空气冷却，未考虑冷却速率差异对微裂纹的潜在影响。[Mahanta 2020, pp. 7-8]
- **REV充分性假定**：以孔隙体积随边长变化趋稳为标准，边长>550 μm视为REV，并选取600 μm立方体进行分析。[Mahanta 2020, pp. 11-13]
- **图像分割准确性**：所用的三阶段分水岭分割流程能够可靠地区分孔隙与基质，未进一步验证边界体素分配的不确定性。[Mahanta 2020, pp. 10-11]
- **连通性定义**：通过轴连通性模块定义连通孔隙，连通性依赖于所选取的方向和阈值设定。[Mahanta 2020, pp. 12-14]
- **矿物反应窗口**：引用文献中不同矿物的分解/脱羟基温度区间（如高岭石455–642°C，伊利石400–625°C等）适用于本研究的砂岩。[Mahanta 2020, pp. 13-14]

## Key Variables / Parameters
- **温度条件**：25, 200, 400, 600, 800°C [Mahanta 2020, pp. 7-8]
- **砂岩类型**：DS, JS, GS（按矿物组成与黏土含量区分）[Mahanta 2020, pp. 2-3]
- **总孔隙率**（%）[Mahanta 2020, pp. 12-13]
- **连通/非连通孔隙率**（%及比值）[Mahanta 2020, pp. 12-15]
- **平均孔隙等效半径** (μm) [Mahanta 2020, pp. 18-20]
- **平均配位数** [Mahanta 2020, pp. 18-20]
- **平均喉道等效半径** (μm) [Mahanta 2020, pp. 18-20]
- **平均喉道通道长度** (μm) [Mahanta 2020, pp. 18-20]
- **代表性体积元边长** (μm)，微CT有效体素尺寸 (μm) [Mahanta 2020, pp. 4-5; Mahanta 2020, pp. 12-13]
- **热处理加热速率** (°C/min) [Mahanta 2020, pp. 7-8]

## Reusable Claims
1. 对于富含黏土矿物（如高岭石、伊利石、迪开石）的砂岩，高温热处理（尤其400°C以上）会导致更为显著的孔隙率增加和结构损伤，其敏感性显著高于贫黏土的石英砂岩。[Mahanta 2020, pp. 1-2; Mahanta 2020, pp. 15-16]
   - **条件**：升温速率5°C/min，无固压，空气冷却。
2. 在25°C至800°C范围内，DS（石英砂岩）的孔隙率随温度整体单调递增，而JS和GS因黏土矿物分解及可能的次生矿物沉淀（如portlandite），在高温段可能出现孔隙率下降。[Mahanta 2020, pp. 14-16]
   - **条件**：依赖于矿物组成，portlandite形成需钙质来源（如JS中的方解石）。
3. 370°C–680°C是多种砂岩共同经历的“主要结构变化窗口”，该窗口涵盖了α-β石英相变（~573°C）以及多种黏土矿物、碳酸盐矿物的热分解反应。[Mahanta 2020, pp. 14-15; Mahanta 2020, pp. 19-20]
   - **条件**：该窗口基于TG分析和孔隙率变化推断，适用于升温速率5°C/min。
4. 对于砂岩孔隙网络模型，平均配位数和喉道通道长度不一定随温度单调增加；矿物相变与次生胶结物的形成可导致喉道半径和配位数在600°C后降低。[Mahanta 2020, pp. 18-20]
   - **条件**：仅基于连通孔隙，如JS的配位数在800°C虽高，但喉道半径下降。
5. 当岩石中非连通孔隙占比很高（如GS常温下约40%）时，仅使用连通孔隙建立的孔隙网络模型可能无法正确反映真实的孔喉演化趋势。[Mahanta 2020, pp. 15-16; Mahanta 2020, pp. 18-19]
   - **条件**：分割算法将黏土矿物粒内孔隙标记为非连通。
6. TGA曲线可作为辅助验证工具，失重比例与岩石的热损伤敏感性密切相关；GS失重8.112% (RT–680°C) 是其强损伤的化学基础。[Mahanta 2020, pp. 15-16]

## Candidate Concepts
- [[pore network modelling]]
- [[micro-CT]]
- [[digital rock physics]]
- [[thermal treatment of sandstone]]
- [[representative elementary volume]]
- [[pore coordination number]]
- [[clay mineral dehydroxylation]]
- [[quartz alpha-beta inversion]]
- [[thermogravimetric analysis]]
- [[connected and non-connected porosity]]

## Candidate Methods
- [[X-ray micro computed tomography (micro-CT)]]
- [[Avizo image processing segmentation]]
- [[anisotropic diffusion filter]]
- [[unsharp masking filter]]
- [[watershed segmentation]]
- [[maximal ball algorithm for pore network extraction]]
- [[porosity profile and REV analysis]]
- [[thermogravimetric (TG) analysis]]
- [[axis-connectivity module for connected porosity]]

## Connections To Other Work
- 引用了Andrä等人（2013）关于数字岩石物理基准的成像与分割研究，作为方法论基础。[Mahanta 2020, pp. 1-2; Mahanta 2020, pp. 9-11; Mahanta 2020, pp. 20-21]
- 孔隙网络提取方法参照了Al-Kharusi和Blunt（2007）、Dong和Blunt（2009）以及Silin和Patzek（2006）的最大球与中轴算法。[Mahanta 2020, pp. 13-14; Mahanta 2020, pp. 18-20]
- 温度效应的解释借鉴了Sun等人（2016）关于砂岩热处理后物理性质变化的工作，以及Somerton（1992）对岩石/流体系统热行为的综述。[Mahanta 2020, pp. 14-15; Mahanta 2020, pp. 20-21]
- 矿物分解温度参考了Barshad（1972）、Somerton（1992）、Luo等人（2016）及Stoch和Wacławska（1981）的文献。[Mahanta 2020, pp. 13-14]
- REV分析引用了Al-Raoush和Papadopoulos（2010）以及Razavi等人（2007）的方法。[Mahanta 2020, pp. 11-13]
- 与其他岩石类型的微CT研究（如Goral等人(2015)的页岩、Rabbani等人(2017)的碳酸盐岩）进行了比较，说明本工作聚焦于砂岩。[Mahanta 2020, pp. 1-2]

## Open Questions
- 非连通孔隙（尤其GS中黏土矿物粒内孔）在高温下如何向连通孔隙转化？其转化机制及对渗透率的实际影响有待量化。[Mahanta 2020, pp. 15-16; Mahanta 2020, pp. 18-19]
- JS在600°C后孔隙率下降是否确实由portlandite (Ca(OH)₂)的生成导致？需要进一步的矿物学分析（如XRD或SEM）直接证实。[Mahanta 2020, pp. 15-16]
- 现有的PNM仅基于静力学配置，未讨论渗透率、毛管压力或多相流行为的模拟结果，这些动态特性尚未与孔隙网络数据关联。[Mahanta 2020, pp. 18-19]
- 在高于800°C的温度下，尤其是接近UCG腔壁温度（>1000°C），砂岩的孔隙结构将如何进一步演化？是否有局部熔融或玻璃化现象？[Mahanta 2020, pp. 7-8]
- 本文所用小尺寸无约束样品与地下原位围压条件下的热响应差异有多大？围压对微裂纹开闭和孔隙连通性的影响未涉及。

## Source Coverage
**所有14个非空索引片段均已处理。** 全文索引字符覆盖率约91.95%（60501/65795字符），基于源签名`c929be74fc9cc7c44a920c161b3527e9e993406a`的完全索引。本页面综合了来自涵盖引言、方法、结果、讨论及结论的14个片段证据，未依赖未提供的参考文献外部信息。[Coverage audit; Mahanta 2020, fragments 1–14]
