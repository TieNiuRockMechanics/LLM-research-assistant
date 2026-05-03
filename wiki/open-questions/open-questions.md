---
type: "open-question"
schema_version: "aggregate-v4-2026-04-30"
status: "draft"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T16:02:46"
title: "Open Questions"
---

# Open Questions

## 在三维分形裂缝网络中，a=D+1 的自相似条件是否同样严格成立？其连通性和渗透特性的标度律如何？

几乎所有理论验证都在二维进行，而真实渗流是三维的。三维标度关系的成立直接影响储层建模的准确性。

### Current Evidence

Darcel et al. (2003) 推测三维中也满足类似区制过渡；Kim (2009) 的 FDFN 生成显示 2D 和 3D 的孔隙度分形维数相同，但未验证连通标度。

### Needed Evidence

大规模三维裂缝网络逾渗和流动模拟；天然三维露头或地震属性导出的裂缝体积数据验证。

### Source Papers

- [2003-darcel-connectivity-properties-of-two-dimensional-fracture-networks-with-stochastic-fractal](../papers/2003-darcel-connectivity-properties-of-two-dimensional-fracture-networks-with-stochastic-fractal.md)
- [2009-kim-estimation-of-fracture-porosity-of-naturally-fractured-reservoirs-with-no-matrix-porosi](../papers/2009-kim-estimation-of-fracture-porosity-of-naturally-fractured-reservoirs-with-no-matrix-porosi.md)

## 裂隙岩体表征单元体 (REV) 的存在条件是什么？隙宽方差、长度-隙宽相关性以及空间聚簇如何影响 REV 尺度？

REV 是采用等效连续介质模型的前提；若不存在，则必须使用离散模型。

### Current Evidence

Baghbanan & Jing (2007) 指出，隙宽对数正态分布的二阶矩 b=3 时，20 m 尺度仍无 REV；隙宽与长度相关时 REV 尺寸增大。

### Needed Evidence

三维模拟，真实隙宽分布数据，考虑应力耦合的演化对 REV 的影响。

### Source Papers

- [2007-baghbanan-hydraulic-properties-of-fractured-rock-masses-with-correlated-fracture-length-and](../papers/2007-baghbanan-hydraulic-properties-of-fractured-rock-masses-with-correlated-fracture-length-and.md)

## 如何从地震波形的细微特征定量区分诱发地震中的剪切滑移、张裂和混合破裂机制？

理解储层改造的力学过程，区分水力压裂与剪切激活，对优化刺激策略至关重要。

### Current Evidence

Basel 事件初动极性矛盾提示存在非双力偶分量，但未进行矩张量反演。

### Needed Evidence

高精度矩张量反演，结合井下宽频带数据，与注水压力曲线联合分析。

### Source Papers

- [2009-deichmann-earthquakes-induced-by-the-stimulation-of-an-enhanced-geothermal-system-below-bas](../papers/2009-deichmann-earthquakes-induced-by-the-stimulation-of-an-enhanced-geothermal-system-below-bas.md)

## 在长期（>10年）热‑水‑力‑化学（THMC）多场耦合作用下，热损伤岩石及裂隙网络的渗透率、力学性质、诱发地震活动及换热效率将如何演化？矿物溶解/沉淀、应力腐蚀等化学过程如何反馈？

EGS的商业可行性依赖于长期稳定的产能和可预测的地震风险；化学封闭或增渗效应将决定储层寿命。

### Current Evidence

Soultz项目已运行多年，但详细的THMC演变模型仍在开发中，仅见裂隙带导水特征描述。现有实验和模拟多集中于短期THM耦合，化学效应量化不足。Junique (2021)发现淬火水中K、Na、Ca浓度随循环而累积，证实物理损伤加剧化学溶出；循环冷却实验显示参数趋稳，但力-化耦合（如压力溶解）未被纳入。

### Needed Evidence

需要长期现场监测数据、反应性溶质运移模拟和示踪试验；开展含反应性流体的长期循环实验并结合矿物反应动力学模型；开发THMC全耦合数值模拟工具并用现场数据（如Soultz、Pohang）校准；进行大型物理模型试验及微观CT观察。

### Source Papers

- [2010-dezayes-overview-of-the-fracture-network-at-different-scales-within-the-granite-reservoir-o](../papers/2010-dezayes-overview-of-the-fracture-network-at-different-scales-within-the-granite-reservoir-o.md)
- [2018-salimzadeh-thermoporoelastic-effects-during-heat-extraction-from-low-permeability-reservoir](../papers/2018-salimzadeh-thermoporoelastic-effects-during-heat-extraction-from-low-permeability-reservoir.md)
- [2017-lu-a-global-review-of-enhanced-geothermal-system-egs](../papers/2017-lu-a-global-review-of-enhanced-geothermal-system-egs.md)
- [2021-junique-experimental-investigation-of-the-effect-of-quenching-cycles-on-the-physico-chemica](../papers/2021-junique-experimental-investigation-of-the-effect-of-quenching-cycles-on-the-physico-chemica.md)
- [2020-sha-experimental-evaluation-of-physical-and-mechanical-properties-of-geothermal-reservoir-r](../papers/2020-sha-experimental-evaluation-of-physical-and-mechanical-properties-of-geothermal-reservoir-r.md)
- [2025-wu-thermal-property-of-reservoir-rocks-at-thermal-mechanical-coupled-conditions-and-resulta](../papers/2025-wu-thermal-property-of-reservoir-rocks-at-thermal-mechanical-coupled-conditions-and-resulta.md)
- [2023-ren-a-comprehensive-review-of-tracer-tests-in-enhanced-geothermal-systems](../papers/2023-ren-a-comprehensive-review-of-tracer-tests-in-enhanced-geothermal-systems.md)
- [2025-解经宇-我国干热花岗岩在不同冷却条件下的力学响应研究进展](../papers/2025-解经宇-我国干热花岗岩在不同冷却条件下的力学响应研究进展.md)
- [2025-zhu-physico-mechanical-properties-of-granite-after-thermal-treatments-using-different-cooli](../papers/2025-zhu-physico-mechanical-properties-of-granite-after-thermal-treatments-using-different-cooli.md)
- [2026-lei-a-review-of-reservoir-stimulation-technologies-for-enhanced-geothermal-systems](../papers/2026-lei-a-review-of-reservoir-stimulation-technologies-for-enhanced-geothermal-systems.md)

## 如何建立一个既遵循物理成核-生长-停止规则、又能在现有场地大数据（如钻孔成像、测井）下实现自动化参数标定的三维离散裂隙网络（DFN）生成模型？

经典泊松 DFN 已被证明系统性地高估连通性和渗透率。KFM 等成因模型能产生更现实的 T 形交叉和空间聚类，但其控制参数（成核率、a 指数、停止模式）过于复杂，工程师难以标定，阻碍了其在工业界的应用。

### Current Evidence

Maillot 等人(2016) 对比了 KFM 和泊松模型的逾渗行为，理论上定义了其参数但对标定保持开放性。Bonneau(2016) 可通过调节播种比例和影区强度来匹配一些统计矩，但仍无法实现单井确定性约束的反演。

### Needed Evidence

需要一个能够将 KFM 参数空间与可观察量（如 P32、线密度、产状和关联维数 Dc）关联起来的简化代理模型。可使用马尔可夫链蒙特卡洛等方法，利用来自多个场地的均匀测绘数据进行对抗性测试。

### Source Papers

- [2016-maillot-connectivity-permeability-and-channeling-in-randomly-distributed-and-kinematically](../papers/2016-maillot-connectivity-permeability-and-channeling-in-randomly-distributed-and-kinematically.md)
- [2016-bonneau-impact-of-a-stochastic-sequential-initiation-of-fractures-on-the-spatial-correlatio](../papers/2016-bonneau-impact-of-a-stochastic-sequential-initiation-of-fractures-on-the-spatial-correlatio.md)

## 什么是控制裂隙尺寸-导水性（T或b）相关性的具体物理机制？在经历多期次应力转动和胶结的天然储层中，这种相关性还会保留吗？

Hyman(2016) 证明尺寸-T 相关性对渗透率和早期溶质突破有绝对主导作用。然而该指标通常是基于新鲜岩石断裂力学的理论（假设有 b ∝ l^0.5）或者统计推断，并不一定在古应力场和成岩胶结的天然裂缝中仍保持该正比性。

### Current Evidence

Hyman 等人的合成 DFN 模型展示了相关/不相关模型之间的巨大敏感性。在碳酸盐岩中，Wennberg(2016) 发现大部分裂缝都已充填或只局部张开，这与基于粗糙力学模型的强正相关性相悖。

### Needed Evidence

需要结合井下的生产测井、成像测井的裂隙开度、和在围压下的渗透率测试，与岩心中古胶结裂隙的微观统计，来系统标定。需要一个具体场地的多尺度近井带井间压力恢复试验进行校正。

### Source Papers

- [2016-hyman-fracture-size-and-transmissivity-correlations-implications-for-transport-simulations](../papers/2016-hyman-fracture-size-and-transmissivity-correlations-implications-for-transport-simulations.md)
- [2016-wennberg-the-characteristics-of-open-fractures-in-carbonate-reservoirs-and-their-impact-on](../papers/2016-wennberg-the-characteristics-of-open-fractures-in-carbonate-reservoirs-and-their-impact-on.md)

## 能通过地表破裂迹线或深大断裂的露头粗糙度测量，来定量约束断层的摩擦强度（静摩擦系数 μ）和伴生的裂隙损伤带渗透率吗？

断层粗糙度（自仿射、各向异性、多尺度）被认为是控制摩擦滑动稳定性和破裂能的关键。若可从形貌估算剪切强度 μ 和渗透率，将直接为地应力评价和诱发地震评估提供基础。

### Current Evidence

Candela(2012) 发现了九个量级的粗糙度在垂向和走向上的自仿射规律。Faulkner(2010) 综述了μ与弱化机制，但仅将粗糙度作为磨损的来源而不是直接预测其 μ 值。当沟槽化成为主导时，损伤带的渗透率呈现几个数量级的各向异性。

### Needed Evidence

在实验室直接剪切具有精确三维形貌的天然断层岩样本，将测得的 μ 值、剪切产生的渗透率各向异性与沿滑移方向的 Hk 和垂直于滑移的 H⊥ 进行回归。

### Source Papers

- [2012-candela-roughness-of-fault-surfaces-over-nine-decades-of-length-scales](../papers/2012-candela-roughness-of-fault-surfaces-over-nine-decades-of-length-scales.md)
- [2010-faulkner-a-review-of-recent-developments-concerning-the-structure-mechanics-and-fluid-flow](../papers/2010-faulkner-a-review-of-recent-developments-concerning-the-structure-mechanics-and-fluid-flow.md)
- [2016-wennberg-the-characteristics-of-open-fractures-in-carbonate-reservoirs-and-their-impact-on](../papers/2016-wennberg-the-characteristics-of-open-fractures-in-carbonate-reservoirs-and-their-impact-on.md)

## 在全球尺度的结晶岩中，什么过程控制了渗透率的深度衰减斜率和它的巨大剩余方差（在给定深度下仍可跨越 5 个数量级）？

Achtziger-Zupan(2017) 的全球大数据回归显示深度仅能解释渗透率方差的 20%，其余全部是由地质构造和地震活动等因素控制的“散点”。识别这些影响深远地质过程的构成是建立可靠的深层水动力和地热模型的前提。

### Current Evidence

该数据库指出了 PGA 和地质构造省是主控因素，但其他研究表明，达西测试抽样性的不均一、不同尺度测试到的不同构造域（隧道掘进松弛带对比深部油井测试）、以及动态地震周期导致的渗透率损伤与愈合作用，都可能是巨大变异性的来源。

### Needed Evidence

进行高密度的、利用示踪微震成像和长期信号的大型跨孔地下水试验。将渗透率与更细化的地质度量（如裂隙密度 P32、特定脆性矿物含量）和地下水年龄指标关联起来。

### Source Papers

- [2017-achtziger-zupan-a-new-global-database-to-improve-predictions-of-permeability-distribution-i](../papers/2017-achtziger-zupan-a-new-global-database-to-improve-predictions-of-permeability-distribution-i.md)

## 在水力增产及长期注采地热过程中，长时间尺度和强化学场（如卤水）下，裂隙表面粗糙度随应力-化学共同演化，会如何影响渗透率和换热效率？

现有的 JRC 或分形维数-渗透率经验模型多假设裂隙表面是刚性且化学上不变的。但压溶、矿物沉淀/溶解等过程会持续改变裂隙接触面的粗糙度和开度，对沟槽化在 EGS 的寿命有决定性影响。

### Current Evidence

Faulkner(2010) 指出压力溶蚀蠕变是长期断层弱化的候选机制。Siratovich(2015) 指出在 EGS 高温水中可能存在矿物沉淀。He(2016) 的模拟发现在粗糙度变化时，换热系数（OHTC）的空间分布会完全改变，说明这是一个一级效应。

### Needed Evidence

长期（数月到年）的热-水-力-化耦合实验，结合 CT 和表面形貌仪的定期扫描。测试项目应包括：具有不同初始粗糙度和矿物含量的花岗岩/碳酸盐岩，与原始地热盐水流体进行循环。

### Source Papers

- [2016-he-effects-of-surface-roughness-on-the-heat-transfer-characteristics-of-water-flow-through](../papers/2016-he-effects-of-surface-roughness-on-the-heat-transfer-characteristics-of-water-flow-through.md)
- [2010-faulkner-a-review-of-recent-developments-concerning-the-structure-mechanics-and-fluid-flow](../papers/2010-faulkner-a-review-of-recent-developments-concerning-the-structure-mechanics-and-fluid-flow.md)
- [2015-siratovich-saturated-heating-and-quenching-of-three-crustal-rocks-and-implications-for-ther](../papers/2015-siratovich-saturated-heating-and-quenching-of-three-crustal-rocks-and-implications-for-ther.md)

## 能否将地热力学-地震危险性的混合评估模型（如 FISHA）与考虑裂隙与断层多相流和THM耦合的油藏数值模拟器（如 TOUGH2、PFLOTRAN）完全耦合，以实现兼具高精度的诱发地震时空预测和产能预测的平台？

目前这类模型要么聚焦于地震统计（基于迁移率和统计指数），要么专注于产能评估（单井或双井的热弹性产能预测），且极少包含矿物的真实化学沉降演变。这种分裂使得生产操作者无法在同一环境中权衡防震和提产量。

### Current Evidence

Zang(2014) 报道了 GEISER 项目成果提供了基于统计的地震危险性评估进阶模型。Cao(2016) 证明了自然对流和变物性的工质对产能的模拟异常敏感，Yin(2016) 的热损伤仅仅部分体现在这些力学公式中。

### Needed Evidence

需要开发一个开源的、模块化的模拟集成环境，能将离散裂隙网络（DFN）的生成（包含粗糙度和孔径相关性的可能数据归纳）、H-M 耦合模拟（如 PFLOTRAN）、再与周期性震源统计更新和力学模块交互。在巴塞尔或 Soultz 这样有完整长期历史和微震记录的 EGS 场地做对比验证。

### Source Papers

- [2014-zang-analysis-of-induced-seismicity-in-geothermal-reservoirs-an-overview](../papers/2014-zang-analysis-of-induced-seismicity-in-geothermal-reservoirs-an-overview.md)
- [2016-cao-numerical-study-on-variable-thermophysical-properties-of-heat-transfer-fluid-affecting](../papers/2016-cao-numerical-study-on-variable-thermophysical-properties-of-heat-transfer-fluid-affecting.md)
- [2016-yin-comparison-of-mechanical-properties-in-high-temperature-and-thermal-treatment-granite](../papers/2016-yin-comparison-of-mechanical-properties-in-high-temperature-and-thermal-treatment-granite.md)

## 如何科学地定义和测量复杂节理粗糙度系数的三维 JRC 值？这对于提升边坡稳定性和TBM掘进预测的准确性有何意义？

几乎所有的 JRC 实验关联和很多岩体分级都建立在二维剖面粗糙度上。Tatone 和 Grasselli(2010) 的三维粗糙度参数奠定了非接触测量的基础，而扫描圆和 λ 等新方法则进一步推动了对各向异性的考虑，但这些分数尚未被标准化并写入工程实践指南中。

### Current Evidence

Tatone(2010) 证实二维均值能接近三维粗糙度真值。Bae(2011) 用 BHTV 扫描圆证明了快速评估 JRC 各向异性的可能性。Zhang(2014) 的 λ 指数集成了幅值上去改进剪切强度估计。

### Needed Evidence

系统的天然多尺寸（10 cm 到 > 5 m）节理三维表面粗糙度和定向原位剪切试验获取的 JRC − 峰值摩擦角数据库。并将新的 3D 参数评估与现行的 ISRM 建议方法和强度准则进行对比验证。

### Source Papers

- [2010-tatone-a-new-2d-discontinuity-roughness-parameter-and-its-correlation-with-jrc](../papers/2010-tatone-a-new-2d-discontinuity-roughness-parameter-and-its-correlation-with-jrc.md)
- [2011-bae-characterization-of-joint-roughness-in-granite-by-applying-the-scan-circle-technique-to](../papers/2011-bae-characterization-of-joint-roughness-in-granite-by-applying-the-scan-circle-technique-to.md)
- [2014-zhang-a-new-method-estimating-the-2d-joint-roughness-coefficient-for-discontinuity-surfaces](../papers/2014-zhang-a-new-method-estimating-the-2d-joint-roughness-coefficient-for-discontinuity-surfaces.md)

## 在以冷却为主的低温液氮压裂刺激中，压裂液携带何种支撑剂以及如何支撑？热冲击产生的微裂缝在长期回温或循环开采过程中，会在多大程度上闭合进而丧失增产效果？

Wang(2016) 证明在低温液氮处理后渗透率提升了十几倍，但大部分增益会在岩石恢复到室温后损失掉（闭合）。若无小粒径支撑剂的支撑，这种效果在储层的长期高温高压环境下将无法维持。

### Current Evidence

Wang 的实验发现沙岩在回温后渗透率为低温时的 5 倍，但仍比未做处理提高了数倍，这被归因于颗粒间胶结的损伤和自支撑。然而，这种支撑的力学强度尚属未知。

### Needed Evidence

在模拟储层地应力和围压温度下，进行带闭合应力回温的长期渗透率监测实验。同时试验不同类型的微纳米支撑剂（如超轻支撑剂）或化学黏连剂，评估其在与液氮同时注入后的运移、嵌入和裂缝导流能力。

### Source Papers

- [2016-wang-waterless-fracturing-technologies-for-unconventional-reservoirs-opportunities-for-liqu](../papers/2016-wang-waterless-fracturing-technologies-for-unconventional-reservoirs-opportunities-for-liqu.md)

## 有围压和原位高应力条件下，热冲击损伤和渗透率增强规律与常压实验有何本质差异？如何修正实验室结果以应用于深部储层？

深层地热（>3 km）围压高，可能极大地抑制热裂纹萌生，导致现场效果远低于常压实验。

### Current Evidence

少量高围压热-渗实验（如2017-zhao, 2018-kumari, 2023-xue）显示临界温度和渗透率增幅显著变化，但系统参数研究缺失。

### Needed Evidence

高围压（>50 MPa）、高流体压力下的三轴热-渗-力耦合实验；不同岩性的对比；不同围压-温度组合下同步监测渗透率和声发射。

### Source Papers

- [2017-zhao-experimental-investigation-on-thermal-cracking-permeability-under-hthp-and-application](../papers/2017-zhao-experimental-investigation-on-thermal-cracking-permeability-under-hthp-and-application.md)
- [2018-kumari-experimental-investigation-of-quenching-effect-on-mechanical-microstructural-and-flo](../papers/2018-kumari-experimental-investigation-of-quenching-effect-on-mechanical-microstructural-and-flo.md)
- [2023-xue-effect-of-water-cooling-shock-on-fracture-initiation-and-morphology-of-high-temperature](../papers/2023-xue-effect-of-water-cooling-shock-on-fracture-initiation-and-morphology-of-high-temperature.md)
- [2024-suo-experimental-and-numerical-simulation-research-on-hot-dry-rock-wellbore-stability-under](../papers/2024-suo-experimental-and-numerical-simulation-research-on-hot-dry-rock-wellbore-stability-under.md)

## 水力刺激中无震滑移与地震滑移的转换条件是什么？无震滑移对渗透率增长的贡献比例如何量化？如何控制刺激方案以最大限度增渗同时避免破坏性地震？

是EGS项目社会许可的关键；Basel和Pohang事件表明控制不当可引发灾难；微震监测只捕获脆性破裂，若无震滑移主导渗透率提高，则现有储层评估严重低估了有效改造体积。

### Current Evidence

2018-amann综述显示无震滑移主导早期增渗，但缺乏现场速率-状态摩擦参数约束；2017-kim指出现有震级-体积模型不足；Lei 2026指出SRV不等于有效渗透体积，无震滑移直接证据和定量模型稀缺。

### Needed Evidence

在真实EGS深层储层中开展高分辨率无震/地震滑移联合测量（如分布式光纤应变、微震、井下压力），结合速率-状态摩擦模型，反演无震滑移分布并建立与渗透率变化的关系；建立实时预报模型。

### Source Papers

- [2018-amann-the-seismo-hydromechanical-behavior-during-deep-geothermal-reservoir-stimulations-ope](../papers/2018-amann-the-seismo-hydromechanical-behavior-during-deep-geothermal-reservoir-stimulations-ope.md)
- [2017-kim-induced-seismicity-assessing-whether-the-2017-mw-5-4-pohang-earthquake-in-south-korea-w](../papers/2017-kim-induced-seismicity-assessing-whether-the-2017-mw-5-4-pohang-earthquake-in-south-korea-w.md)
- [2026-lei-a-review-of-reservoir-stimulation-technologies-for-enhanced-geothermal-systems](../papers/2026-lei-a-review-of-reservoir-stimulation-technologies-for-enhanced-geothermal-systems.md)

## 液氮多次冷热循环在现场围压和流体循环条件下的增效机理及经济性如何？

现场成功实施液氮压裂将大幅改变干热岩开发模式，减少水资源消耗并提升增产效果。

### Current Evidence

实验室已证实液氮冷却可大幅增强花岗岩渗透率，但主要依靠小试样、无围压浸泡实验。目前缺管道输送、Leidenfrost 效应控制和支撑剂携带的工程验证。

### Needed Evidence

进行中等尺度真三轴液氮注入试验，结合数值仿真，考察围压、注入速率、循环次数的影响；开展示踪试验或测井评价现场裂缝连通性。

### Source Papers

- [2021-rong-experimental-investigation-on-physical-and-mechanical-properties-of-granite-subjected](../papers/2021-rong-experimental-investigation-on-physical-and-mechanical-properties-of-granite-subjected.md)
- [2021-kang-experimental-study-on-the-physical-and-mechanical-variations-of-hot-granite-under-diff](../papers/2021-kang-experimental-study-on-the-physical-and-mechanical-variations-of-hot-granite-under-diff.md)

## 如何利用地球物理数据（如微震、电阻率）和示踪剂反演，精确重构深部储层的三维离散裂隙网络及其动态演化？

准确的裂隙网络模型是地热产能预测和压裂方案设计的核心，目前依赖昂贵的钻井和稀疏数据。

### Current Evidence

贝叶斯随机反演方法（Ringel 2021）已展示了从水力层析中恢复主要流动路径的可行性；EGS Collab 的密集监测也支持多尺度数据融合。

### Needed Evidence

发展更高效、可融合多种地球物理和示踪数据的反演算法；研究裂隙几何和开度的唯一性约束问题；在多个地热场地进行验证。

### Source Papers

- [2021-ringel-stochastic-inversion-of-three-dimensional-discrete-fracture-network-structure-with-h](../papers/2021-ringel-stochastic-inversion-of-three-dimensional-discrete-fracture-network-structure-with-h.md)
- [2021-wu-characterization-of-flow-and-transport-in-a-fracture-network-at-the-egs-collab-field-exp](../papers/2021-wu-characterization-of-flow-and-transport-in-a-fracture-network-at-the-egs-collab-field-exp.md)

## 在经历多期构造运动的花岗岩基底中，冷却冲击产生的热裂纹与天然裂缝的交互机制是什么？如何利用先存裂缝优化储层建造？

深部干热岩必然存在被热液或岩浆充填的先存裂缝，其胶结界面是潜在的弱面，合理利用可减少压裂能耗。

### Current Evidence

Yin 等 (2020) 实验发现充填体胶结界面纵向贯穿时可形成高效渗透通道，但缺乏天然裂缝网络中热裂与原有裂缝的耦联观测。

### Needed Evidence

开展含预制胶结界面或天然裂缝网络的花岗岩热冲击试验与数值模拟，定量描述界面开裂条件、裂缝偏转规律和网络连通性。

### Source Papers

- [2019-yin-experimental-research-on-the-rupture-characteristics-of-fractures-subsequently-filled-b](../papers/2019-yin-experimental-research-on-the-rupture-characteristics-of-fractures-subsequently-filled-b.md)
- [2020-yin-experimental-research-on-the-permeability-of-fractured-subsequently-filled-granite-unde](../papers/2020-yin-experimental-research-on-the-permeability-of-fractured-subsequently-filled-granite-unde.md)

## 能否建立基于物理过程的普适岩石热损伤本构模型或标度律，以预测不同岩性、冷却速率和循环条件下的损伤阈值、脆-延转变及力学响应？

目前热损伤模型多依赖于拟合实验数据，缺乏普适性；不同论文报道的热损伤加速温度在300–600°C间变化，与矿物组成和实验条件有关，推广至EGS多样化储层时误差较大。

### Current Evidence

众多实验揭示了阈值温度、石英相变、循环硬化和疲劳饱和等复杂现象，但各种岩性规律不尽相同；Tomás (2025) 综述了众多岩石的TTT但均为观测值；解经宇2025汇总了多产地花岗岩，但未建立统一公式。

### Needed Evidence

整合微观裂纹密度、矿物反应、声发射等多源数据，构建基于热动力学和断裂力学的损伤演化方程；收集全球岩石热物性和强度数据库，利用机器学习分析主控因素，建立普适标度律。

### Source Papers

- [2020-qin-physical-and-mechanical-properties-of-granite-after-high-temperature-treatment](../papers/2020-qin-physical-and-mechanical-properties-of-granite-after-high-temperature-treatment.md)
- [2020-zhao-exploratory-experimental-study-on-the-mechanical-properties-of-granite-subjected-to-cy](../papers/2020-zhao-exploratory-experimental-study-on-the-mechanical-properties-of-granite-subjected-to-cy.md)
- [2021-wang-the-effects-of-thermal-treatments-on-the-fatigue-crack-growth-of-beishan-granite-an-in](../papers/2021-wang-the-effects-of-thermal-treatments-on-the-fatigue-crack-growth-of-beishan-granite-an-in.md)
- [2025-tom-s-how-do-high-temperatures-affect-rock-properties-a-comprehensive-review-of-experimenta](../papers/2025-tom-s-how-do-high-temperatures-affect-rock-properties-a-comprehensive-review-of-experimenta.md)
- [2025-解经宇-我国干热花岗岩在不同冷却条件下的力学响应研究进展](../papers/2025-解经宇-我国干热花岗岩在不同冷却条件下的力学响应研究进展.md)
- [2025-zhai-pfc-fdem-multi-scale-cross-platform-numerical-simulation-of-thermal-crack-network-evol](../papers/2025-zhai-pfc-fdem-multi-scale-cross-platform-numerical-simulation-of-thermal-crack-network-evol.md)

## 裂隙粗糙度（包括各向异性）及非均质开度如何影响网络尺度的流体流动、热传递和溶质运移？是否存在尺度桥接效应？

大多数DFN热-流模拟采用均匀开度或简化粗糙度，若尺度桥接效应显著，预测的换热面积和热突破时间将严重失准；粗糙度各向异性可能改变压降和弥散。

### Current Evidence

Hyman (2021) 在厘米级网络中发现真实孔径分布可重组流场、增加流道化；Yao (2020) 表明逾渗粗糙度仅影响逾渗后阶段；Diaz (2026) 提取了JRC各向异性，但未与渗流数值耦合。

### Needed Evidence

开展含热效应的孔径变异性DFN模拟，对比均匀开度结果；进行双向渗流实验或直接数值模拟，将粗糙度方向张量与渗透率张量关联，建立宏观各向异性渗透率模型；热示踪试验验证。

### Source Papers

- [2021-hyman-scale-bridging-in-three-dimensional-fracture-networks-characterizing-the-effects-of-v](../papers/2021-hyman-scale-bridging-in-three-dimensional-fracture-networks-characterizing-the-effects-of-v.md)
- [2020-yao-effects-of-fracture-density-roughness-and-percolation-of-fracture-network-on-heat-flow](../papers/2020-yao-effects-of-fracture-density-roughness-and-percolation-of-fracture-network-on-heat-flow.md)
- [2026-diaz-surface-roughness-characterization-of-open-and-closed-rock-joints-in-deep-cores-using](../papers/2026-diaz-surface-roughness-characterization-of-open-and-closed-rock-joints-in-deep-cores-using.md)

## 如何将实验室尺度获得的热-冷循环损伤规律（如第一次损伤或饱和效应）外推至工程尺度（空间和时间）的储层响应？

理解储层在长期生产采放热和循环注冷过程中的渗透率和力学性质演变，直接关系到EGS和冻土地带工程的安全性和经济寿命。

### Current Evidence

实验室证据（2023-cui-experimental-investigation, 2022-ge-thermal-damage）表明损伤累积具有饱和或阶段性特征，但都是基于数小时或数天的小尺寸试验，没有真实长达数十年、数百米尺度且包含原位应力、流体化学耦合的证据。

### Needed Evidence

需要发展中尺度物理模型实验，结合多场（THMC）耦合的数值模拟，将微观损伤机制（如裂纹闭合、扩展、矿物溶解/沉淀）参数化，来模拟从实验室到现场的尺度升级。

### Source Papers

- [2023-cui-experimental-investigation-on-the-influence-on-mechanical-properties-and-acoustic-emiss](../papers/2023-cui-experimental-investigation-on-the-influence-on-mechanical-properties-and-acoustic-emiss.md)
- [2022-ge-thermal-damage-and-mechanical-properties-of-high-temperature-sandstone-with-cyclic-heati](../papers/2022-ge-thermal-damage-and-mechanical-properties-of-high-temperature-sandstone-with-cyclic-heati.md)
- [2022-viswanathan-from-fluid-flow-to-coupled-processes-in-fractured-rock-recent-advances-and-new](../papers/2022-viswanathan-from-fluid-flow-to-coupled-processes-in-fractured-rock-recent-advances-and-new.md)

## 基于图的代理模拟器（Graph-based emulators）能否可靠地扩展到包含完整热-水-力-化学（THMC）耦合效应的全耦合过程？

解决THMC全耦合模拟的计算成本瓶颈是实现场尺度长期预测和不确定性量化的关键。若代理模型能够处理耦合，将极大推动地热开发、核废料处置等领域的预测能力。

### Current Evidence

2022-viswanathan-from-fluid-flow的综述中提到，基于图的模拟器在单相稳态流中实现了4个数量级的加速，但在引入热、力学和化学效应时，挑战剧增，可能引入与‘记忆效应’、过程路径依赖相关的误差。

### Needed Evidence

需要开发并验证能够动态更新节点和边属性（如对流通量、温度、裂面开度）的图结构框架，并系统对比其与高保真全耦合离散模型（如DFM）在长期模拟中的误差演变。

### Source Papers

- [2022-viswanathan-from-fluid-flow-to-coupled-processes-in-fractured-rock-recent-advances-and-new](../papers/2022-viswanathan-from-fluid-flow-to-coupled-processes-in-fractured-rock-recent-advances-and-new.md)

## 在各种裂缝性地热储层热提取模拟中，孔径变异性（非均质性）和裂缝网络几何结构，哪个是更重要的控制因素？

决定了研究的资源投入方向是放在精细化测量裂缝粗糙度/开度上，还是放在大尺度网络连通性的刻画上。

### Current Evidence

2022-he-numerical-evaluation和2023-gao-heat-extraction强调了孔径变异性导致的流动通道化，会使有效流动面积不足40%。然而，2022-viswanathan-from-fluid-flow的另一类研究认为网络结构（拓扑、连通性）在多数情况下比单一裂缝内的开度变化更重要。这可能是由“长程连通性控大局，局部开度控细节”共同作用的。

### Needed Evidence

需要设计一套包含不同网络密度、连接路径、同时控制孔径场相关长度的数值实验，系统分离并量化这两种因素对总产热和热突破时间的相对贡献度。

### Source Papers

- [2022-he-numerical-evaluation-of-heat-extraction-performance-in-enhanced-geothermal-system-consid](../papers/2022-he-numerical-evaluation-of-heat-extraction-performance-in-enhanced-geothermal-system-consid.md)
- [2023-gao-heat-extraction-performance-of-fractured-geothermal-reservoirs-considering-aperture-var](../papers/2023-gao-heat-extraction-performance-of-fractured-geothermal-reservoirs-considering-aperture-var.md)
- [2022-viswanathan-from-fluid-flow-to-coupled-processes-in-fractured-rock-recent-advances-and-new](../papers/2022-viswanathan-from-fluid-flow-to-coupled-processes-in-fractured-rock-recent-advances-and-new.md)

## 如何发展高效的三维热‑力耦合颗粒基模型（GBM）以准确模拟矿物尺度裂纹演化？

现有模型多为二维，忽略了裂纹的三维交互和应力路径效应，限制了对脆‑延转变和渗透率各向异性的预测。

### Current Evidence

二维 TM‑GBM 已能模拟加热和冷却过程的晶间/晶内裂纹，但计算资源限制了三维推广。

### Needed Evidence

开发高效并行三维 DEM 算法，结合 X 射线 CT 重构矿物边界，验证不同应力路径下的损伤。

### Source Papers

- [2024-yang-multiscale-damage-and-thermal-stress-evolution-characteristics-of-rocks-with-thermal-s](../papers/2024-yang-multiscale-damage-and-thermal-stress-evolution-characteristics-of-rocks-with-thermal-s.md)

## 冷却过程中矿物水解和粘土膨胀等化学效应对热损伤有无显著独立贡献？

水冷实验中常观察到碳酸盐溶解和粘土矿物膨胀，但这些化学作用对强度劣化的定量贡献尚不明确。

### Current Evidence

Xi (2024) 指出方解石水解和粘土膨胀可加剧裂纹，但未与纯热应力效应分离。

### Needed Evidence

使用惰性流体（如油、液氮）和不同 pH 水进行对照实验，结合微观元素分析。

### Source Papers

- [2024-xi-experimental-study-on-pore-characteristics-evolution-and-rock-damage-mechanism-of-therma](../papers/2024-xi-experimental-study-on-pore-characteristics-evolution-and-rock-damage-mechanism-of-therma.md)

## 如何从低维数据（一维钻孔或二维露头迹线）可靠地推断三维裂缝网络的几何尺寸、导通性和渗透率？

深部储层几乎完全依赖钻孔成像和岩心，缺失三维露头信息，导致DFN建模充满不确定性；裂缝尺寸分布反演存在非唯一性问题。

### Current Evidence

2019-moein证明仅一维分形维数无法唯一确定三维幂律参数；2017-huang等方法需要二维迹线图；Liu (2025) 提出的MPD方法在迹线推断上取得了MAE~1 m的精度，但推广有限。

### Needed Evidence

结合地质先验（如构造应力）或物探（如MT、地震）的联合反演框架；三维爆炸或矿井三维暴露验证；收集大量不同露头的三维真实裂缝网络进行验证。

### Source Papers

- [2019-moein-scaling-of-fracture-patterns-in-three-deep-boreholes-and-implications-for-constrainin](../papers/2019-moein-scaling-of-fracture-patterns-in-three-deep-boreholes-and-implications-for-constrainin.md)
- [2017-huang-estimation-of-permeability-of-3-d-discrete-fracture-networks-an-alternative-possibili](../papers/2017-huang-estimation-of-permeability-of-3-d-discrete-fracture-networks-an-alternative-possibili.md)
- [2025-liu-revisiting-each-fracture-size-and-spatial-pattern-inference-from-rock-mass-surface-to-i](../papers/2025-liu-revisiting-each-fracture-size-and-spatial-pattern-inference-from-rock-mass-surface-to-i.md)

## 裂缝网络模拟中的尺度效应如何从实验室推广到千米级储层？

实验室 DFN 多为厘米至米级，而地热储层尺度达公里级，渗透率和弥散性质的尺度升级律尚未解决。

### Current Evidence

Yin (2024) 提出了有限尺寸标度律，但仅适用于相对均匀的 DFN。

### Needed Evidence

建立多尺度嵌套露头数据集，开展跨尺度数值模拟，验证标度律参数的普适性。

### Source Papers

- [2024-yin-p-clet-number-dependent-longitudinal-dispersion-in-discrete-fracture-networks](../papers/2024-yin-p-clet-number-dependent-longitudinal-dispersion-in-discrete-fracture-networks.md)

## 如何将二维裂缝网络建模（分形、GAN）有效扩展到三维，并保持连通性、开度变异性及计算可行性？

真实裂缝岩体为三维，二维模型无法捕捉交切和流动迂曲，限制了渗流和力学模拟的准确性。

### Current Evidence

FracGen、Upscaling-GAN已实现二维升尺度，FT-DFN提供了二维表征框架。三维CT扫描（Zhu 2025）和深孔成像（Zhang 2025）提供数据，但三维建模仍处于概念或结构统计阶段。

### Needed Evidence

开发三维生成式模型（如3D GAN）并利用少量岩心CT或钻孔数据融合训练；验证生成网络的拓扑和渗流一致性。

### Source Papers

- [2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers](../papers/2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers.md)
- [2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai](../papers/2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai.md)
- [2025-zhao-characterizing-the-intrinsic-complexity-of-natural-fracture-networks-a-novel-fractal-b](../papers/2025-zhao-characterizing-the-intrinsic-complexity-of-natural-fracture-networks-a-novel-fractal-b.md)

## 在EGS现场，如何利用实时监测数据自适应调整液压、化学、热刺激组合策略？

固定刺激方案难以应对异构储层响应，自适应控制有望在实现增产的同时降低地震社会风险。

### Current Evidence

循环软刺激和交通灯系统为实时控制提供基础；数字孪生概念提出但缺乏集成算法。

### Needed Evidence

构建储层数据同化框架，集成分布式光纤、微震、井口参数，训练强化学习智能体，在小型现场试验中验证闭环自适应调整。

### Source Papers

- [2026-lei-a-review-of-reservoir-stimulation-technologies-for-enhanced-geothermal-systems](../papers/2026-lei-a-review-of-reservoir-stimulation-technologies-for-enhanced-geothermal-systems.md)

## GAN或其它生成式AI模型在不同地质背景裂缝网络的泛化能力如何？

若AI模型严重依赖单张训练图像，其应用将局限于特定露头，无法推广。

### Current Evidence

FracGen和Upscaling-GAN均基于单图训练，泛化未验证。

### Needed Evidence

利用多露头、不同构造域的裂缝图像进行迁移学习或few-shot learning测试，评估生成网络的域外推能力。

### Source Papers

- [2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers](../papers/2025-zhou-fracgen-natural-fracture-networks-reconstruction-and-upscaling-using-generative-advers.md)
- [2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai](../papers/2026-nie-constructing-large-scale-high-fidelity-fracture-networks-based-on-generative-ai.md)

## 如何将毫米级及以下微裂缝纳入采动增强渗透率评价？

气体渗流很大程度上受微米至亚毫米级裂隙控制，现有钻孔监控缺失这些小尺度信息。

### Current Evidence

Zhu 2025钻孔成像只捕捉>1 mm裂缝，模型忽略了微观贡献。

### Needed Evidence

结合显微CT、核磁共振等对煤/岩石微观孔隙裂隙表征，建立多尺度裂缝孔隙耦合渗透率模型，并引入PER框架。

### Source Papers

- [2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi](../papers/2025-zhu-mining-induced-fracture-network-reconstruction-and-anisotropic-mining-enhanced-permeabi.md)

## 多级水力刺激的应力阴影在EGS大温差环境下如何演变？

温度变化引入的热弹性应力可能改变应力阴影区的大小和方向，影响裂缝网络的连通性。

### Current Evidence

目前压裂应力阴影模型多基于等温或小温差，EGS研究未系统考虑热效应。

### Needed Evidence

开展热-流-固耦合数值分析，分析不同温度梯度和注入方案下多裂缝应力干扰演化，并通过现场光纤测量验证。

### Source Papers

- [2026-lei-a-review-of-reservoir-stimulation-technologies-for-enhanced-geothermal-systems](../papers/2026-lei-a-review-of-reservoir-stimulation-technologies-for-enhanced-geothermal-systems.md)
