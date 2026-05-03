---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-fan-a-real-time-visual-investigation-on-microscopic-progressive-fatigue-deterioration-of-gr"
title: "A Real-Time Visual Investigation on Microscopic Progressive Fatigue Deterioration of Granite Under Cyclic Loading."
status: "draft"
source_pdf: "data/papers/2023 - A Real-Time Visual Investigation on Microscopic Progressive Fatigue Deterioration of Granite Under Cyclic Loading.pdf"
collections:
  - "part2"
citation: "Fan, L. F., et al. \"A Real-Time Visual Investigation on Microscopic Progressive Fatigue Deterioration of Granite Under Cyclic Loading.\" *Rock Mechanics and Rock Engineering*, vol. 56, 2023, pp. 5133-5147. doi:10.1007/s00603-023-03326-y."
indexed_texts: "11"
indexed_chars: "53311"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T11:42:27"
---

# A Real-Time Visual Investigation on Microscopic Progressive Fatigue Deterioration of Granite Under Cyclic Loading.

## One-line Summary
本研究利用实时CT扫描对花岗岩在循环加载下的微观疲劳劣化进行了可视化研究，发现当最大循环应力超过46.04% UCS时，面孔隙率和体孔隙率迅速增加，且损伤主要集中在前20个循环内 [Fan 2023, pp. 1-2, pp. 10-11]。

## Research Question
花岗岩在多级和单级循环加载下微观结构（孔隙和裂纹）的渐进性疲劳劣化过程是怎样的？循环应力和循环次数如何影响岩石微观损伤的演化？ [Fan 2023, pp. 1-2]

## Study Area / Data
- **材料**：花岗岩，采自中国湖南省，主要矿物成分为石英(28.2%)、钾长石(27.4%)、高岭石(4.9%)、斜长石(17.3%)和云母(22.2%) [Fan 2023, pp. 3-4]。
- **样本尺寸**：圆柱形样本，直径6.0 mm，高12.0 mm，高径比2.0，两端磨平并在105°C下干燥48小时 [Fan 2023, pp. 3-4]。
- **单轴抗压强度**：干燥花岗岩样本的UCS约为108.6 MPa [Fan 2023, pp. 3-4]。

## Methods
- **实验设备**：Nano Voxel-2200系列高分辨率CT扫描系统，配备Deben Micro-test CT 5000加载装置，由北京工业大学岩石力学实验室提供 [Fan 2023, pp. 4-5]。
- **加载方案**：
  - **多级循环加载**：最小循环应力恒定20.0 MPa，最大循环应力从30.0 MPa开始，每100次循环后增加10.0 MPa直至破坏。在加载前、每100次循环后及破坏后进行实时CT扫描 [Fan 2023, pp. 4-5]。
  - **单级循环加载**：根据多级加载实验结果确定裂纹起始应力（46.04% UCS），并将其作为最大循环应力进行单级循环加载。加载/卸载速率恒为0.02 mm/min。在循环次数达到0、20、40、60、80、100、200、250和300次时进行CT扫描 [Fan 2023, pp. 4-5, pp. 10-11]。
- **图像分析方法**：
  - **2D分析**：在分析区域选取三个不同角度（0°、120°、240°）的垂直截面，测量面孔隙率以定量研究平面上的渐进疲劳行为 [Fan 2023, pp. 5-7]。
  - **3D分析**：通过统计微缺陷体素数量并乘以体素体积计算微缺陷体积，得到体孔隙率以定量研究空间损伤 [Fan 2023, pp. 5-7]。3D重建中对每个孔隙或裂纹用特定颜色单独标记 [Fan 2023, pp. 11-13]。

## Key Findings
1. **多级循环加载下的面孔隙率变化**：
   - 第1阶段和第2阶段（最大循环应力≤40.0 MPa）：面孔隙率从1.43%降至0.97%，主要由于原始裂纹压缩闭合 [Fan 2023, pp. 7-9]。
   - 第3阶段（最大循环应力50.0 MPa）：面孔隙率从0.97%急剧上升至5.92%，增长311.11%，主要由平行于加载方向的裂纹生成和扩展引起 [Fan 2023, pp. 7-9]。
   - 第4阶段（最大循环应力60.0 MPa）：28次循环后花岗岩突然破坏，面孔隙率从5.92%增至41.45%，形成多条宏观破坏面 [Fan 2023, pp. 7-9]。
   - 总体趋势：当最大循环应力小于46.04% UCS时，面孔隙率和体孔隙率基本不变；当达到或超过该阈值时，两者迅速增加 [Fan 2023, pp. 1-2]。
2. **多级循环加载下的空间损伤**：第1、2阶段后内部结构相对稳定；第3阶段产生平行加载方向的穿透性大裂纹；第4阶段裂纹演化为宏观破坏面 [Fan 2023, pp. 7-9]。
3. **单级循环加载下的损伤演化**：
   - 在裂纹起始应力下，面孔隙率和体孔隙率随循环次数单调递增 [Fan 2023, pp. 1-2]。
   - 增加主要集中在前20次循环内，内部结构显著开裂，如产生穿透性大裂纹，同时部分原始裂纹压缩闭合 [Fan 2023, pp. 9-11, pp. 11-13]。
   - 20至100次循环阶段，穿透性大裂纹变化较小，损伤轻微 [Fan 2023, pp. 11-13]。
   - 100至200次循环阶段，小裂纹扩展并与穿透性大裂纹连接 [Fan 2023, pp. 11-13]。
   - 200至300次循环阶段，内部结构由相对稳定转变为不稳定状态，形成更大的穿透裂纹 [Fan 2023, pp. 11-13]。
   - 裂纹起始应力在本研究中被确定为46.04% UCS [Fan 2023, pp. 10-11]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 面孔隙率从1.43%降至0.97%（初始状态至第2阶段） | [Fan 2023, pp. 7-9] | 多级加载，最大循环应力30-40 MPa | 由原始裂纹压缩闭合引起 |
| 面孔隙率从0.97%急增至5.92%（第3阶段） | [Fan 2023, pp. 7-9] | 最大循环应力50.0 MPa | 增长311.11%，因平行加载方向裂纹生成和扩展 |
| 花岗岩在28次循环后破坏，面孔隙率从5.92%升至41.45%（第4阶段） | [Fan 2023, pp. 7-9] | 最大循环应力60.0 MPa | 形成多条宏观破坏面 |
| 面孔隙率和体孔隙率在最大应力<46.04%UCS时基本不变，在≥46.04%UCS时迅速增加（多级加载） | [Fan 2023, pp. 1-2] | 多级循环加载 | 总体趋势总结 |
| 前20次循环中，第2分析截面产生平行加载方向的大裂纹，且随循环次数增加孔隙率和体孔隙率单调递增，增加集中在前20次循环 | [Fan 2023, pp. 1-2, pp. 9-11, pp. 11-13] | 单级循环加载，应力=裂纹起始应力(46.04%UCS) | 损伤早期剧烈，后减缓 |
| 20至100次循环阶段，穿透性大裂纹变化较小，损伤轻微 | [Fan 2023, pp. 11-13] | 单级循环加载，应力=裂纹起始应力 | 内部结构相对稳定 |
| 100至300次循环阶段，小裂纹扩展并与主裂纹连接，结构由稳定变为不稳定 | [Fan 2023, pp. 11-13] | 单级循环加载，应力=裂纹起始应力 | 后期损伤加剧 |

## Limitations
- 未从索引片段中确认样本数量及实验的重复性信息。
- 实时CT扫描的成像参数（如分辨率、扫描时间）未在索引片段中明确给出。
- 裂纹起始应力的具体确定方法未详细说明 [Fan 2023, pp. 10-11]。
- 研究针对干燥样本，未考虑水分对疲劳劣化的影响 [Fan 2023, pp. 3-4]。

## Assumptions / Conditions
- 实验采用径向尺寸极小的圆柱样本（直径6mm），可能为了适应CT扫描系统的空间限制并提高成像精度 [Fan 2023, pp. 3-4]。
- 样本两端磨平以保证均匀加载，减少应力集中 [Fan 2023, pp. 3-4]。
- 干燥处理（105°C，48小时）假设排除了孔隙水对疲劳过程的影响 [Fan 2023, pp. 3-4]。
- 加载速率（0.02 mm/min）为静态或准静态条件，未涉及加载频率对疲劳的影响 [Fan 2023, pp. 4-5]。

## Key Variables / Parameters
- **面孔隙率**：用于定量评价平面微观损伤的指标 [Fan 2023, pp. 7-9]。
- **体孔隙率**：用于定量评价空间整体微观损伤的指标 [Fan 2023, pp. 7-9, pp. 9-11]。
- **最大循环应力**：在多级加载中从30 MPa递增至破坏，在单级加载中为裂纹起始应力（50.0 MPa，即46.04% UCS） [Fan 2023, pp. 4-5, pp. 10-11]。
- **最小循环应力**：恒定20.0 MPa [Fan 2023, pp. 4-5]。
- **循环次数**：多级加载每级100次；单级加载共300次，关键节点为0、20、100、200、300次 [Fan 2023, pp. 4-5, pp. 9-11]。
- **单轴抗压强度 (UCS)**：108.6 MPa [Fan 2023, pp. 3-4]。
- **裂纹起始应力**：46.04% UCS [Fan 2023, pp. 10-11]。

## Reusable Claims
- **Claim 1**：对于类似湖南花岗岩的脆性岩石，在循环加载下，面孔隙率和体孔隙率在最大循环应力低于裂纹起始应力阈值（46.04% UCS）时保持恒定，主要表现为裂纹闭合；超过此阈值后，两者急剧上升，裂纹生成和扩展成为主导。证据来自多级循环加载实验 [Fan 2023, pp. 1-2, pp. 7-9]。**限制**：此阈值依赖于岩性、样本尺寸及加载路径。
- **Claim 2**：在裂纹起始应力水平下的单级循环加载中，岩石微观损伤（通过孔隙率衡量）随循环次数单调递增，但绝大多数损伤累积发生在前20个循环内。证据来自单级循环加载实验 [Fan 2023, pp. 1-2, pp. 9-11]。**限制**：结论基于200-300次循环的观测，长期（如数千次循环）行为未从索引片段中确认。
- **Claim 3**：实时CT技术能够捕捉岩石在循环加载下孔隙、裂纹闭合、生成、扩展和连接的动态演化过程，为建立宏观力学响应与微观结构变化的关联提供了直接可视化手段。证据基于整个实验流程与分析 [Fan 2023, pp. 1-2]。**条件**：需要高分辨率CT系统与同步加载装置集成。
- **Claim 4**：在微观裂纹演化的不同阶段，岩石的损伤行为呈现阶段性特征：初始阶段（<20次循环）由于裂纹生成而损伤迅速增加；中间阶段结构趋于稳定；在后期（>100-200次循环）由于小裂纹连接主裂纹，结构再次变得不稳定。证据基于单级循环加载的3D重构分析 [Fan 2023, pp. 11-13]。**限制**：行为可能随加载应力水平而变化。

## Candidate Concepts
- [[microscopic fatigue deterioration]] / 微观疲劳劣化
- [[crack initiation stress]] / 裂纹起始应力
- [[areal porosity]] / 面孔隙率
- [[volumetric porosity]] / 体孔隙率
- [[real-time CT scanning]] / 实时CT扫描
- [[multi-level cyclic loading]] / 多级循环加载
- [[single-level cyclic loading]] / 单级循环加载
- [[fracture evolution]] / 裂纹演化
- [[crack closure]] / 裂纹闭合
- [[crack propagation]] / 裂纹扩展
- [[progressive fatigue deterioration]] / 渐进疲劳劣化
- [[brittle rock failure]] / 脆性岩石破坏

## Candidate Methods
- [[X-ray computed tomography]] (CT)
- [[cyclic loading test]] with real-time monitoring
- [[areal porosity calculation]] via 2D image analysis
- [[volumetric porosity calculation]] via 3D reconstruction
- [[crack initiation stress determination]] from CT measurements
- [[cyclic loading path design]] (multi-level vs. single-level)
- microdefect voxel counting and volumetric analysis [Fan 2023, pp. 5-7]

## Connections To Other Work
- 研究引述了前期工作关于加载频率对岩石宏观疲劳响应（不可逆应变、疲劳变形模量、能量耗散）及加载波形对疲劳强度和疲劳能量影响的研究 [Fan 2023, pp. 2-3]。
- 指出前期研究多集中于宏观力学特性，而本研究旨在将宏观强度衰减与微观结构劣化联系起来 [Fan 2023, pp. 2-3]。
- 提及扫描电镜（SEM）、核磁共振（NMR）和X射线CT是岩石力学中常用的微观观测技术，并特别强调了CT技术的非破坏性和可视化优势 [Fan 2023, pp. 2-3]。
- 在孔隙率分析中引用了其他学者关于岩体中微缺陷体积计算的类似方法 [Fan 2023, pp. 5-7]。
- 从主题上，本研究的结果可与以下概念和方法的研究建立联系：[[fracture damage evolution in rocks]]、[[microcrack nucleation and growth under fatigue]]、[[fracture criterion for frictional materials]]、[[porous media]]。

## Open Questions
- 实验所用的花岗岩样本（直径6 mm）是否存在尺寸效应，其结论能否推广至工程尺度的岩体？ [索引片段未确认]
- 加载频率、波形、湿度等其他因素如何影响观察到的微观损伤演化规律？ [Fan 2023, pp. 2-3]表明这些因素影响宏观疲劳响应，但其对微观损伤的影响未在本研究中探讨。
- 未从索引片段中确认疲劳破坏的微观判据（如临界孔隙率或裂纹密度）及其与宏观疲劳寿命的定量关系。
- 文中提到在单级加载下，内部结构从相对稳定变为不稳定状态，此过程是否与AE声发射等其他损伤监测信号存在关联？ [索引片段未确认]

## Source Coverage
本页面基于索引提供的**11个片段**编写，涵盖了论文的多个核心部分，包括摘要、引言方法总结、实验材料与设备、加载方案、图像分析方法、多级和单级循环加载下的平面及空间损伤结果以及关键结论。覆盖范围较好，但可能存在以下缺失：
- **详细数据统计**：如不同截面、不同阶段孔隙率的完整变化数据及误差范围未全部提供。
- **实验重复性**：多次实验结果的一致性和可重复性信息未在片段中明确。
- **扩展讨论**：对实验结果背后物理机制的深入讨论（如矿物颗粒尺度上的断裂力学解释）未在片段中体现。
- **研究局限性**：论文本身可能讨论的局限性未在索引片段中明确。
- 部分段落被截断，导致相关信息可能不完整（如pp. 11-13结尾处与体孔隙率相关的分析结果被截断）。
