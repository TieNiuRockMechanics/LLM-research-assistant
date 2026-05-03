---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2021-rong-effect-of-thermal-damage-on-mechanical-and-permeability-properties-of-sandstone"
title: "Effect of Thermal Damage on Mechanical and Permeability Properties of Sandstone."
status: "draft"
source_pdf: "data/papers/2021 - Effect of thermal damage on mechanical and permeability properties of sandstone.pdf"
collections:
  - "论文"
citation: "Rong, Guan, et al. \"Effect of Thermal Damage on Mechanical and Permeability Properties of Sandstone.\" *Arabian Journal of Geosciences*, vol. 14, 1772, 2021, doi:10.1007/s12517-021-08098-9."
indexed_texts: "11"
indexed_chars: "53297"
nonempty_source_blocks: "11"
compiled_source_blocks: "11"
compiled_source_chars: "53428"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.002458"
coverage_status: "full-index"
source_signature: "1f238dfeb132fbe79456b1e1dfffe9761f4a8917"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-02T04:08:59"
---

# Effect of Thermal Damage on Mechanical and Permeability Properties of Sandstone.

## One-line Summary
热处理温度存在一个阈值（200 °C）：低于此温度时，随着温度升高，砂岩的P波波速、弹性模量、峰值强度等物理力学参数提高，渗透率下降；超过阈值后，物理力学性质急剧劣化，微裂缝大量形成并扩展，导致渗透率急剧增加；整个变形过程中渗透率均呈现缓慢下降、稳定上升、急剧增加三个阶段。

## Research Question
研究不同温度（25 °C、200 °C、400 °C、600 °C）处理后砂岩的力学特性与渗透率演化规律，为地下岩石工程（如高放射性废物深层处置、地热开发、深埋隧道）提供参考。[Rong 2021, pp. 1-2]

## Study Area / Data
- 岩样：取自湖北省秭归县的完整石英砂岩块，尺寸约700×500×150 mm³，纹理相对均匀，无明显裂隙。[Rong 2021, pp. 3-4]
- 岩性：细至中粒沉积岩，粒径0.1~0.5 mm，主要矿物为石英（75%）、长石（20%）、云母（1%）、方解石（2%）和粘土矿物（2%）。[Rong 2021, pp. 3-4]
- 试样制备：标准圆柱样φ50 mm×100 mm；自然干燥5天以上，筛选波速差异较小的岩样；共8组，其中单轴声发射试验4组（每组2个），渗透试验4组（每组1个）。[Rong 2021, pp. 3-4]
- 基本物理参数（未加热，均值）：密度2.31 g/cm³，P波波速3012 m/s，单轴抗压强度51.2 MPa，弹性模量13.1 GPa，泊松比0.17。[Rong 2021, pp. 3-4， Table 1]
- 温度分组：25 °C、200 °C、400 °C、600 °C，每组3个试样。[Rong 2021, pp. 3-4]

## Methods
- **热处理**：SX2-10-12中温箱式电阻炉，加热速率10 °C/min，升至目标温度后恒温6 h，再随炉缓慢冷却至室温。[Rong 2021, pp. 3-4]
- **P波波速测试**：RSM-SY5(T)非金属声波测试仪，端面中心置探头，涂抹凡士林，纵波测量。[Rong 2021, pp. 3-4]
- **单轴压缩声发射试验**：TAW-3000岩石三轴伺服耦合试验机，轴向与径向LVDT（精度1×10⁻⁴ mm），声发射实时监测；先以3 kN固定，初始载荷控制（50 N/s），轴向变形达50 μm后转为变形控制（0.02 mm/min），接近峰值时降为0.005 mm/min至应力-应变曲线下降。[Rong 2021, pp. 4-5]
- **三轴压缩渗透试验**：稳态法，试样进口端施加恒定渗透压2.0 MPa，出口端自由出流，形成稳定压差2.0 MPa；围压4.0 MPa、孔压2.0 MPa；每100 μm轴向变形保持4 h使渗流稳定，随后继续4 h测试流速，重复至试样破坏，单样耗时7~10天。渗透系数按达西定律计算。[Rong 2021, pp. 4-5]
- **特征应力确定**：
  - 损伤强度σcd：体积应变法（Martin 1997）
  - 裂隙闭合应力σcc：新的轴向应变响应法（NASR，Peng et al. 2015）
  - 裂隙起裂应力σci：侧向应变响应法（LSR，Nicksiar & Martin 2012）[Rong 2021, pp. 5-6]

## Key Findings
- 阈值温度：200 °C是砂岩波速、力学性质和渗透特性转变的临界点。[Rong 2021, pp. 1-2, 5-6, 10-11]
- **力学参数**（与25 °C相比）：200 °C时峰值强度提高至165.23%，弹性模量11.47 GPa；400 °C时峰值强度159.74%，弹性模量12.40 GPa；600 °C时峰值强度125.17%，弹性模量6.72 GPa。[Rong 2021, pp. 5-6, Table 3] P波波速同样先升后降：200 °C为3124.73 m/s（102.18%），600 °C降至2874.23 m/s（93.99%）。[Rong 2021, pp. 4-5, Table 2]
- **渗透率**：初始值（轴向应变0）从25 °C的2.13×10⁻¹⁶ m²降至200 °C的1.93，再升至400 °C的3.94和600 °C的7.58；变形过程呈现下降段、缓慢上升段和急剧上升段三个阶段，且随温度升高下降段与稳定上升段延长，水平段缩短。[Rong 2021, pp. 7-8, Table 4, Fig. 10]
- **特征应力**：200 °C以下各特征应力（σcc、σci、σcd）随温度上升而增加；超过400 °C后，σcd、σci下降，σcc略有升高；归一化特征应力也有类似趋势。[Rong 2021, pp. 6-7, Fig. 7]
- **声发射**：各温度下峰后声发射活动强烈；200 °C以下声发射活动较少，400~600 °C稳定裂纹扩展阶段声发射更活跃。[Rong 2021, pp. 6-7, Fig. 8]
- **渗透率与裂纹体积应变关联**：渗透率在裂纹体积收缩阶段下降，在裂纹体积开始膨胀后维持低位，裂纹体积快速膨胀时渗透率急剧增大；断裂损伤应力σcd是渗透率变化的重要转折点。[Rong 2021, pp. 8-10, Figs. 11-13]
- **细观机制**：25~200 °C主要为吸附水蒸发、粘土矿物熔融填充孔隙，致密化；200~400 °C因矿物不均匀膨胀萌生微裂纹；400~600 °C石英、长石晶体软化、晶面滑移，热应力急剧增加，微裂纹大量扩展贯通。[Rong 2021, pp. 10-11]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 热处理后P波波速平均值：25 °C: 3012 m/s；200 °C: 3124.73 m/s；400 °C: 3087.25 m/s；600 °C: 2874.23 m/s | [Rong 2021, pp. 4-5, Table 2] | RSM-SY5(T)波速仪，端面中心测试，每温度3个样 | 200 °C为波速变化阈值 |
| 热处理后峰值强度：25 °C: 52.08 MPa；200 °C: 86.05 MPa (165.23%)；400 °C: 83.19 MPa (159.74%)；600 °C: 65.19 MPa (125.17%) | [Rong 2021, pp. 5-6, Table 3] | 单轴压缩，代表样结果，加载控制由力转位移 | 所有热损伤试样的峰值强度均高于室温样 |
| 弹性模量：25 °C: 9.65 GPa；200 °C: 11.47 GPa；400 °C: 12.40 GPa；600 °C: 6.72 GPa | [Rong 2021, pp. 5-6, Table 3] | 切线模量，取50%峰值应力水平 | 200 °C最优，600 °C显著劣化 |
| 渗透率初始值（轴向应变0）：25 °C: 2.13e-16 m²；200 °C: 1.93e-16 m²；400 °C: 3.94e-16 m²；600 °C: 7.58e-16 m² | [Rong 2021, pp. 8, Table 4] | 围压4 MPa，渗透压差2 MPa，稳态法 | 200 °C渗透率最低，600 °C最高 |
| 特征应力（以200 °C附近为例）：σcd随温度先升后降，σci类似，σcc在400 °C后有所增加 | [Rong 2021, pp. 6-7, Fig. 7a] | 由体积应变法、NASR、LSR确定 | 归一化特征应力200 °C以下增高，400 °C以上σcd/σc、σci/σc下降 |
| 渗透率与裂纹体积应变关系：渗透率下降段对应裂纹体积收缩，膨胀初期维持低位，急剧膨胀段渗透率陡增；σcd是转折点 | [Rong 2021, pp. 8-10, Figs. 11-13] | 三轴压缩条件下测试 | 裂纹体积应变由$ε_{vc} = ε_v - (1-2ν)(σ_1+2σ_3)/E$计算 |

## Limitations
- 前人研究中对热损伤岩石渗透率及其在加载过程中的变化的研究仍然不多。[Rong 2021, pp. 2-3]
- 从细观角度对热开裂及破坏过程中裂纹扩展机制的研究尚不充分、不成熟。[Rong 2021, pp. 2-3]
- 本试验仅针对单一石英砂岩，结论是否适用于其他岩性未知。[未明确陈述，但隐含]
- 仅使用了固定的加热速率（10 °C/min）、恒温时间（6 h）和冷却方式（随炉冷却），不同热处理制度的影响未探讨。

## Assumptions / Conditions
- 加热过程中，温度分布均匀，忽略试样内部温度梯度。
- 单轴压缩试验中，加载后期采用位移控制可获得峰后曲线。
- 三轴渗透试验中，渗流服从一维达西定律，且当出口流量恒定时视为稳定渗流状态。[Rong 2021, pp. 4-5]
- 采用体积应变法、NASR和LSR确定特征应力时，假定这些方法适用于本次试验的石英砂岩，且误差已被合理控制。
- 弹性模量以50%峰值强度处的切线模量近似。

## Key Variables / Parameters
- 处理温度（25 °C, 200 °C, 400 °C, 600 °C）
- P波波速 (m/s)
- 峰值强度 UCS (MPa)、峰值应变 (%)
- 弹性模量 (GPa)、泊松比
- 渗透率 (10⁻¹⁶ m²)
- 特征应力：裂隙闭合应力σcc、起裂应力σci、损伤应力σcd、峰值应力σP
- 归一化特征应力（特征应力/峰值强度）
- 裂缝体积应变εvc、总体积应变εv
- 声发射参数（振铃计数、撞击率）
- 围压 (4 MPa)、孔压 (2 MPa)
- 加热速率 (10 °C/min)、恒温时间 (6 h)

## Reusable Claims
- **在本文特定石英砂岩及热处理条件下（加热速率10 °C/min，恒温6 h，炉内冷却）**：当处理温度低于200 °C时，随着温度升高，砂岩的P波波速、弹性模量、峰值强度等物理力学参数增大，渗透率降低；当处理温度超过200 °C后，波速、弹性模量和强度快速衰减，渗透率显著上升。阈值温度为200 °C。[Rong 2021, pp. 1-2, 5-6, 10-11]
- **石英砂岩在单轴压缩下**：200 °C及以下试样呈脆性破坏，应力-应变曲线无明显初始凹段；600 °C试样呈S形，初始塑性变形明显增大。[Rong 2021, pp. 5-6]
- **三轴压缩渗流试验（围压4 MPa，孔压差2 MPa）**：砂岩渗透率随轴向应变的变化可分为三个阶段：缓慢下降段（裂隙闭合）、稳定上升段（新生裂隙）、急剧上升段（裂隙贯通形成宏观破裂）。断裂损伤应力σcd是渗透率由下降转为上升的关键转折点，与体积应变由压缩转向膨胀的拐点一致。[Rong 2021, pp. 7-10, Fig. 13]
- **热损伤机制**：25~200 °C由粘土矿物熔融、充填孔隙导致致密化；200~400 °C因矿物不均匀膨胀萌生微裂纹；400~600 °C因石英、长石晶体软化、晶面滑移及热应力剧增，微裂纹大量扩展，岩石体积和渗透率急剧增大。[Rong 2021, pp. 10-11]
- **渗透率与裂纹体积应变的相关性**：裂纹体积收缩阶段渗透率下降，裂纹体积开始膨胀后渗透率维持低位，仅在裂纹体积快速膨胀并形成贯通通道时渗透率才急剧上升。[Rong 2021, pp. 8-10]

## Candidate Concepts
- [[thermal damage]]
- [[permeability evolution]]
- [[threshold temperature]]
- [[crack volumetric strain]]
- [[acoustic emission]]
- [[fracture initiation stress]]
- [[damage stress]]
- [[P-wave velocity]]
- [[quartz α-β phase transition]]
- [[crystal softening]]
- [[crystalline surface slippage]]
- [[brittle-ductile transition]]
- [[volumetric strain method]]
- [[NASR method]]
- [[LSR method]]
- [[uniaxial compression test]]
- [[triaxial permeability test]]
- [[steady-state method]]
- [[Darcy’s law]]
- [[fracture closure]]
- [[fracture propagation]]
- [[fracture coalescence]]

## Candidate Methods
- [[uniaxial compression test with acoustic emission monitoring]]
- [[triaxial compression permeability test (steady-state)]]
- [[P-wave velocity measurement using non-metallic acoustic wave tester]]
- [[method for determining characteristic stresses: volumetric strain method (Martin 1997)]]
- [[new axial strain response method (NASR, Peng et al. 2015)]]
- [[lateral strain response method (LSR, Nicksiar & Martin 2012)]]
- [[high-temperature box-type resistance furnace heating (10°C/min, 6 h holding, furnace cooling)]]
- [[crack volumetric strain calculation from total volumetric strain and elastic constants]]

## Connections To Other Work
- 地热开发与深部工程：高温下岩石力学-渗透特性研究对放射性废物处置（Ringwood 1985; Gibb et al. 2008）、地热资源开发（Gelet et al. 2012）、深埋隧道（Li 2020）至关重要。[Rong 2021, pp. 1-2]
- 砂岩力学性质与温度：先前工作表明温度升高使岩石强度、弹性模量下降，峰后时间延长（Yin 2008）；Wu et al. (2007) 认为矿物吸附水脱出、晶型转变、重结晶等是砂岩性能恶化的根本原因；Zuo et al. (2007) 发现高温下砂岩由局部脆性断裂向脆-塑性耦合断裂转变。[Rong 2021, pp. 1-2]
- 渗透性研究：高温可使砂岩渗透率增加50%（Somerton et al. 1965）；围压对力学性质的影响比温度更敏感，脆-韧转变临界温度约400 °C（Liu et al. 2011）；Zhang et al. (2011) 将渗透率变化划分为五个阶段；Wang & Park (2002) 发现渗透系数在全应力-应变过程中不断变化。[Rong 2021, pp. 2-3]
- 大理岩等其它岩石：高温处理后力学性质与裂隙扩展规律已由Yao et al. (2016) 等研究。[Rong 2021, pp. 1-2]
- 本工作结合单轴声发射与三轴渗透试验，从细观微裂纹角度解释宏观力学与渗透特性演化，填补了热损伤岩石渗透率全过程研究的不足。

## Open Questions
- 热损伤岩石渗透率在加载破坏过程中的变化规律仍需更多实验数据积累。[Rong 2021, pp. 2-3]
- 岩石热开裂和损伤过程中裂纹扩展的细观机制研究尚不充分、不成熟，需发展更精细的测试与表征手段。[Rong 2021, pp. 2-3]
- 不同矿物组成的砂岩（或其它岩类）是否具有不同的阈值温度及渗透率演化模式？[未直接研究，但问题可推]
- 加热速率、恒温时间、冷却制度等因素对热损伤程度及后续力学-渗透行为的影响尚未系统探讨。[未在本文涉及]
- 真实工程中复杂应力路径与水力耦合条件下热损伤岩石的长期渗透性演化规律有待研究。

## Source Coverage
本文档基于全部11个非空索引片段编译而成，片段覆盖率为100%（按片段数），字符覆盖率约为100.2%（按原始索引字符数，因索引中包含少量空白或元数据导致微小超出）。所有非空片段均已纳入，未添加片段外的信息。覆盖率状态：full-index。[来源：coverage audit]
