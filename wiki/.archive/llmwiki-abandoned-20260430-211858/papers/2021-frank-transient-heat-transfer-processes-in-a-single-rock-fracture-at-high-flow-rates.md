---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-frank-transient-heat-transfer-processes-in-a-single-rock-fracture-at-high-flow-rates"
title: "Transient Heat Transfer Processes in a Single Rock Fracture at High Flow Rates."
status: "draft"
source_pdf: "data/papers/2021 - Transient heat transfer processes in a single rock fracture at high flow rates.pdf"
collections:
citation: "Frank, Sascha, et al. \"Transient Heat Transfer Processes in a Single Rock Fracture at High Flow Rates.\" *Geothermics*, vol. 89, 2021, p. 101989. Accessed 2026."
indexed_texts: "20"
indexed_chars: "95356"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T03:31:50"
---

# Transient Heat Transfer Processes in a Single Rock Fracture at High Flow Rates.

## One-line Summary
在高流速（80–350 mm/s）条件下，通过实验室裂隙岩心实验，研究了单裂隙中的瞬态传热行为，发现高流速（>200 mm/s）导致出口水温显著下降，表面粗糙度（JRC=14）对整体传热系数有实质性影响，热突破曲线显示岩石可在相当长时间内维持最大出口温度 [Frank 2021, pp. 1-1, pp. 6-7]。

## Research Question
在瞬态温度阶跃条件下，高流速（最高 350 mm/s）如何影响单裂隙中的热量传递过程？裂隙表面形态（粗糙度）对传热系数和热突破曲线有何调节作用？稳态传热分析在高流速下是否存在上限？ [Frank 2021, pp. 1-1, pp. 2-3, pp. 6-7]。

## Study Area / Data
- 实验材料：取自德国弗莱赫廷格山脊（Flechtinger mountain ridge）采石场的弗莱赫廷格砂岩（Flechtinger sandstone），为二叠纪红棕色砂岩，相关物性参数已被广泛研究 [Frank 2021, pp. 2-3]。
- 样品规格：岩心长 150 mm、直径 100 mm，垂直层理钻取；沿中心劈裂形成单裂隙 [Frank 2021, pp. 2-3, pp. 3-5]。
- 实验组：8 次传热实验，覆盖 4 种泵流量（1.1 g/s、2 g/s、3 g/s、4.2 g/s，对应流速 92～352 mm/s）和两种冷却水平（最大冷却与降低冷却），系统加压 3 bar [Frank 2021, pp. 3-5, pp. 6-7]。

## Methods
1. **实验装置**：高压釜（奥氏体不锈钢 1.4571）内置劈裂岩心，连接 5 L 水储罐、活塞隔膜泵、双管换热器（HEX）及电伴热管路，实现循环水温阶跃 [Frank 2021, pp. 3-5]。通过切换阀门，可让流体经换热器冷却后再进入岩心，或直接循环。
2. **数据采集**：岩心前后各 5 mm 处安装铠装 K 型热电偶（精度 ±0.5 °C），记录瞬态温度曲线；配合压力传感器（量程 0–400 bar，精度 0.25% FS）和 LabVIEW 系统采集 [Frank 2021, pp. 3-5]。
3. **裂隙表征**：采用高精度表面扫描获取裂隙面形貌，计算节理粗糙度系数（JRC，流向 JRC=14）和孔径分布 [Frank 2021, pp. 6-7]。
4. **理论分析**：
   - 稳态阶段基于局部热非平衡（LTNE）模型推导整体传热系数 \(h\)，利用岩石最高温度 \(T_C\) 估算 \(h\) 的下界 [Frank 2021, pp. 5-6]。
   - 瞬态热突破曲线用对流-弥散方程（ADE）解析解拟合，提取热传输参数 [Frank 2021, pp. 2-3, pp. 5-5]。
   - 流动雷诺数在多数实验中低于 80–100，假设主要呈层流 [Frank 2021, pp. 5-5]。

## Key Findings
- **高流速下的出口降温**：稳态出口温度随流速升高而降低。在高冷却度条件下，流速 352 mm/s 时进出口温差为 7.5 °C（26.9→34.4 °C），而 92 mm/s 时温差为 11.6 °C（41.7→53.3 °C）；在低冷却度下，同样趋势的温差绝对值更低（6.3 °C vs 9.3 °C） [Frank 2021, pp. 6-7]。
- **粗糙度对传热的影响**：样品 JRC=14（属“粗糙、起伏”类），表面粗糙度对稳态传热系数有实质性影响，增加了有效换热面积 [Frank 2021, pp. 6-7]。
- **瞬态热容量效应**：热突破曲线表明岩石能在相当长时间内维持最大出口温度，显示裂隙-基质系统的蓄热能力 [Frank 2021, pp. 1-1]。
- **解析解的应用限制**：热弥散系数与质量弥散系数可比，但利用解析解描述热传输存在较强局限性 [Frank 2021, pp. 1-1]。
- **工程意义**：流速超过 200 mm/s 时出口温度明显偏低，可能引起储层不必要的冷却，延长热提取过程，降低地热系统效率 [Frank 2021, pp. 1-1]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 稳态进出口温差：92 mm/s 时为 11.6 °C，352 mm/s 时为 7.5 °C（高冷却度） | [Frank 2021, pp. 6-7] | 弗莱赫廷格砂岩，JRC≈14，系统加压 3 bar，高冷却度（HEX 冷却水>20 g/s） | 表 1 汇总了所有实验的稳态温度、传热量和传热系数，此处仅提取示例 |
| 低冷却度下温差绝对值减小，但趋势相同（92 mm/s 时 9.3 °C，352 mm/s 时 6.3 °C） | [Frank 2021, pp. 6-7] | 弗莱赫廷格砂岩，JRC≈14，系统加压 3 bar，低冷却度（HEX 冷却水 4.5 g/s） | 进口水温较高时（与围岩温差小），流速对温差的影响较小 |
| 裂隙表面粗糙度 JRC=14（流向），略高于垂直流向方向 | [Frank 2021, pp. 6-7] | 高精度表面扫描，劈裂后分析 | 轻微各向异性，个别颗粒脱落影响粗糙度计算 |
| 解析解只能有限度地适用于瞬态热传输分析 | [Frank 2021, pp. 1-1] | 阶跃温度边界，对流-弥散方程 | 未详细说明限制的具体类别 |
| 稳态传热系数可根据 ln((T2-Tc)/(T1-Tc)) 与流量关系计算，Tc 取系统最高岩温 | [Frank 2021, pp. 5-6] | 基于 LTNE，假设常物性、岩石不透水，传热项线性常数化 | 所得 h 为下限估计 |

## Limitations
- 实验结果仅来自弗莱赫廷格砂岩一种岩性，裂隙粗糙度范围有限（JRC≈14），结论向其他岩类和粗糙度推广需谨慎 [Frank 2021, pp. 6-7]。
- 解析解适用范围受严格限制，瞬态过程的全物理模拟有难度 [Frank 2021, pp. 1-1]。
- 高压釜内温度测点间存在微小偏差（因底部加热和顶盖散热），可能引入系统偏差 [Frank 2021, pp. 3-5]。
- 劈裂过程造成局部颗粒脱落，影响粗糙度分析和孔径分布精度 [Frank 2021, pp. 6-7]。
- 流量范围最高 4.2 g/s，更高流速的影响未探索。
- 瞬态分析结果、传热系数具体数值和拟合参数未在提供的片段中详细给出，限制了对核心瞬态机制的进一步评估。

## Assumptions / Conditions
- 采用局部热非平衡（LTNE）模型，分别描述水相和固相的能量方程，固相仅考虑导热，水相考虑对流和热弥散/导热 [Frank 2021, pp. 5-5]。
- 推导稳态传热系数时，将岩 - 水热交换项视为线性常数源，并假设岩石最高温度 \(T_C\) 作为裂隙终端岩石表面温度（由此得到 \(h\) 的下界） [Frank 2021, pp. 5-6]。
- 多数实验假设流动为层流（参考 Re<100 的临界值），忽略湍流效应 [Frank 2021, pp. 5-5]。
- 解析解建立在阶跃函数入口边界条件、常弥散系数和平均流速下，且将热交换项简化为恒定来源 [Frank 2021, pp. 5-5, pp. 5-6]。
- 实验过程维持系统压力 3 bar，视为对流动和传热参数无显著非等温效应。

## Key Variables / Parameters
- **流量 / 流速**：质量流量 \(q_v\) (g/s)，等效流速 \(v\) (mm/s)，裂隙截面积依赖隙宽 \(b\) 和宽度 \(L_W\) [Frank 2021, pp. 5-6]。
- **温度**：入口水温 \(T_1\)，出口水温 \(T_2\)，岩石最高温度 \(T_C\) [Frank 2021, pp. 5-6]。
- **传热系数**：整体传热系数 \(h\) (W/(m² °C))，利用稳态数据计算 [Frank 2021, pp. 5-6]。
- **热 - 水力裂隙参数**：节理粗糙度系数 JRC（流向 14）、隙宽分布（由表面扫描获得）、渗透率（基质渗透率约 10⁻¹⁷ m²）、孔隙度（6–11%） [Frank 2021, pp. 2-3, pp. 6-7]。
- **热物性参数**：水密度 \(\rho_w\)，比热容 \(C_w\)，岩石导热系数 \(K_r\)，热弥散系数 \(D_w\) [Frank 2021, pp. 5-5, pp. 5-6]。
- **无量纲数**：雷诺数 Re [Frank 2021, pp. 5-5]。
- **传热量**：稳态单位时间传热量 \(Q = C_w \rho_w q_v (T_2 - T_1)\) [Frank 2021, pp. 5-6]。

## Reusable Claims
1. 在粗糙单裂隙（JRC=14）中，流速从 ~90 mm/s 升至 ~350 mm/s 时，稳态进出口温差下降约 30%–35%（高冷却度下从 11.6 °C 降至 7.5 °C；低冷却度下从 9.3 °C 降至 6.3 °C），显示高流速显著削弱单位流量下的热提取能力 [Frank 2021, pp. 6-7]。**条件**：弗莱赫廷格砂岩，单裂隙，系统加压 3 bar，冷却水温度稳定；**限制**：仅针对此粗糙度范围，且为稳态结果。
2. 瞬态阶段岩石可长时间保持接近最高的出口水温，表明裂隙岩体具有可观的热缓冲能力，该效应由热突破曲线表征 [Frank 2021, pp. 1-1]。**条件**：流量阶跃引发的瞬态冷却/加热过程；**限制**：未给出具体维持时间和对应流速、温度的定量关系。
3. 表面粗糙度通过改变有效换热面积，实质性地影响整体传热系数，JRC=14 的粗糙裂隙与光滑裂隙的传热差异需通过粗糙度形态因子修正 [Frank 2021, pp. 1-2, pp. 6-7]。**条件**：稳态 LTNE 模型；**限制**：仅基于 JRC 表述，未提供与光滑面的直接对比数据。
4. 现有解析解（如基于阶跃入口的 ADE 解）尽管可拟合热突破曲线，但应用时存在强局限性，不可直接用于精确预测高流量下的瞬态传热 [Frank 2021, pp. 1-1, pp. 2-3]。**条件**：高流速、单裂隙、LTNE 非平衡；**限制**：片段中未列出限制的具体来源（如非达西效应、参数非恒定等）。

## Candidate Concepts
- [[local thermal non-equilibrium (LTNE)]]
- [[heat transfer coefficient]]
- [[thermal breakthrough curve]]
- [[joint roughness coefficient (JRC)]]
- [[advection-dispersion equation (ADE)]]
- [[thermal dispersivity]]
- [[fracture surface roughness]]
- [[enhanced geothermal system (EGS)]]

## Candidate Methods
- [[transient heat transfer experiment with temperature step]]
- [[high-precision fracture surface scanning]]
- [[analytical solution fitting to thermal breakthrough curves]]
- [[steady-state heat transfer calculation with LTNE]]
- [[LabVIEW-based data acquisition]]
- [[Reynolds number calculation for fractured flow]]

## Connections To Other Work
- 本文整体传热系数方法沿用 Zhao (2014) 的常系数假设，并参考 Heinze et al. (2017) 的局部/动态传热系数拓展 [Frank 2021, pp. 1-2]。
- Bai et al. (2016) 和 Bai et al. (2017) 提出了改进的传热系数模型，考虑岩石径向线性温度分布和圆柱形几何形状，本研究在公式推导中借鉴其形式 [Frank 2021, pp. 1-2, pp. 5-6]。
- He et al. (2016) 指出局部传热系数主要受裂隙表面粗糙度、隙宽和流量控制；He et al. (2019) 进一步引入经验形态条件因子，与本研究的粗糙度影响发现一致 [Frank 2021, pp. 1-2]。
- Luo et al. (2019) 比较光滑与粗糙裂隙，发现差异较小，本研究的 JRC=14 粗糙度影响是否显著尚未直接对比。
- 多数前期实验关注稳态传热（Zhao & Tso, 1993; Huang et al., 2016; Luo et al., 2017 等），本文补充了高流速下的瞬态行为 [Frank 2021, pp. 1-2, pp. 2-3]。

## Open Questions
- 瞬态热突破曲线的解析解限制具体是什么？如何在更高流速或复杂裂隙几何中改进传热输运模型？ [Frank 2021, pp. 1-1, pp. 2-3]
- JRC 以外的粗糙度参数（如分形维度、隙宽标准差）对瞬态传热的影响如何？ [未从索引片段中确认]
- 流速超过 350 mm/s 时，传热上限是否继续下降，是否存在临界流速？ [未从索引片段中确认]
- 瞬态过程中的三维效应和局部热非平衡程度如何量化？ [未从索引片段中确认]
- 在何种条件下，热弥散系数与质量弥散系数的可比性会失效？ [Frank 2021, pp. 1-1]
- 高流速下实际储层尺度的有效传热如何从实验室尺度外推？ [未从索引片段中确认]

## Source Coverage
本页基于论文索引的 20 个片段生成，覆盖范围涉及摘要、引言重要引用、样品与实验方法、部分理论推导、粗糙度分析及稳态结果初期描述。片段内容偏向方法与早期结果，缺失以下重要信息：
- 完整的瞬态热突破曲线分析结果（如拟合参数、热弥散度、热传导系数等）。
- 表 1 中的全部传热系数和传热量定量数据，以及高冷却与低冷却的所有组别对比。
- 讨论部分对瞬态行为的深入解释和与前期研究的详细对比。
- 结论部分的主要总结和工程建议。
因此，关于瞬态传热机理的定量证据和综合讨论在本页中未能充分体现，部分声明仅基于片段间接推断。
