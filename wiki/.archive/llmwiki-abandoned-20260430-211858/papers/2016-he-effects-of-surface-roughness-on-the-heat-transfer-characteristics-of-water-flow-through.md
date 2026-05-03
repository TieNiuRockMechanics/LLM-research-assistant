---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2016-he-effects-of-surface-roughness-on-the-heat-transfer-characteristics-of-water-flow-through"
title: "Effects of Surface Roughness on the Heat Transfer Characteristics of Water Flow through a Single Granite Fracture."
status: "draft"
source_pdf: "data/papers/2016 - Effects of surface roughness on the heat transfer characteristics of water flow through a single granite fracture.pdf"
collections:
  - "part2"
  - "雷恩学派分形研究"
citation: "He, Yuanyuan, et al. \"Effects of Surface Roughness on the Heat Transfer Characteristics of Water Flow through a Single Granite Fracture.\" *Computers and Geotechnics*, vol. 80, 2016, pp. 312-321. doi:10.1016/j.compgeo.2016.09.002. Accessed 2026."
indexed_texts: "8"
indexed_chars: "36267"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T19:49:39"
---

# Effects of Surface Roughness on the Heat Transfer Characteristics of Water Flow through a Single Granite Fracture.

## One-line Summary
通过实验与数值模拟，揭示花岗岩单裂缝中水流换热特性主要由表面粗糙度（以分形维数D与轮廓波度Ra表征）控制，局部换热系数分布与波度负相关，而水温和内表面温度沿流向呈近似对数分布 [He 2016, pp. 1-2, pp. 8-8]。

## Research Question
粗糙裂缝中的流动与换热机理尚不清楚，主要困难在于裂缝几何形态的量化及实验数据的缺乏。本文旨在研究表面粗糙度对水流通过单条花岗岩裂缝时换热特性的影响 [He 2016, pp. 1-2]。

## Study Area / Data
- **试样**：取自花岗岩岩块，钻取直径 50 mm、长度 100 mm 的圆柱试样，通过巴西劈裂法产生单裂缝 [He 2016, pp. 2-4]。
- **表面形貌数据**：使用激光扫描显微镜对裂缝表面进行非接触式三维扫描，获取上表面 19,900 个点的坐标（x, y, z）[He 2016, pp. 2-4]。
- **实验数据**：在不同围压（0 MPa、3 MPa、6 MPa）与流量（5、15、30 ml/min）组合下进行水-岩换热实验，记录了进出口水温、实际隙宽等参数。详细的工况条件见原文 Table 2 及附录 A [He 2016, pp. 4-6, pp. 8-10]。

## Methods
- **表面粗糙度表征**：分别提取五个典型纵向剖面 (Y=30, 40, 50, 60, 70 mm)，采用 Xie 和 Pariseau 提出的 h-L 方法计算各剖面的**分形维数 D** 表征整体粗糙度，同时使用**轮廓波度 Ra** 描述局部起伏 [He 2016, pp. 2-2, pp. 2-4]。
- **实验设备与流程**：试验系统示意图见 Fig. 5，测量并记录不同工况下的进出口水温、流量和围压 [He 2016, pp. 4-6]。
- **数值模拟**：将五个剖面导入 COMSOL Multiphysics 构建二维裂缝模型，基于 Navier-Stokes 方程和质量、能量守恒方程进行流-固耦合数值解算，从中提取裂缝中间水流的温度及各点流速，以及裂缝内壁各点的温度分布 [He 2016, pp. 4-6, pp. 6-8]。
- **换热系数计算**：通过数值模拟导出流体和壁面分布温度，代入局部换热系数公式 (4) 计算**局部换热系数 h'**；同时比较文献中三种平均换热系数公式 (10)–(12) 的差异 [He 2016, pp. 6-8]。

## Key Findings
- **局部换热系数分布的主控因素**：局部换热系数分布首先取决于**裂缝表面粗糙度**，其次是隙宽与流量 [He 2016, pp. 1-2, pp. 8-8]。
- **局部换热系数与波度的关系**：局部换热系数 h' 在轮廓波度 Ra 最大处达到最小值，在 Ra 最小处达到最大值。其机制是波峰处流速低，波谷处流速高 [He 2016, pp. 8-8]。
- **温度分布的普遍规律**：对于不同分形维数的裂缝表面，当流量与隙宽恒定时，水温与内表面温度沿流向的分布始终近似为**对数（非线性）**曲线，表面粗糙度对水温及内表面温度分布的影响很小 [He 2016, pp. 6-8, pp. 8-8]。
- **平均换热系数与局部换热系数的本质区别**：常见经验公式给出的平均换热系数为一常数，而局部换热系数沿流向是与轮廓波度相关的分布函数，二者截然不同 [He 2016, pp. 8-8]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
| :--- | :--- | :--- | :--- |
| 局部换热系数分布主要由裂缝表面粗糙度决定，其次为隙宽和流量。 | [He 2016, pp. 1-2, pp. 8-8] | 单相水流，花岗岩劈裂裂缝，隙宽95–125.5 μm，流量5–30 ml/min。 | 此结论源自摘要与结果比较。 |
| 局部换热系数 h' 在轮廓波度 Ra 最大处最小，在 Ra 最小处最大。 | [He 2016, pp. 8-8, Fig. 15] | 五组不同分形维数的剖面，恒定隙宽与流量。 | 解释了波度对局部流速及换热的具体影响。 |
| 水温和内表面温度沿流向呈近似对数分布，且表面粗糙度对其影响很小。 | [He 2016, pp. 6-8, Figs. 9-12] | 不同分形维数剖面，恒定隙宽与流量下的出口温度。 | 此规律与 Zhao 的观点一致 [He 2016, pp. 6-8]。 |
| 恒定工况下，传统公式得出的平均换热系数为常数，而局部换热系数是一个分布值。 | [He 2016, pp. 8-8, Fig. 14, Fig. 15] | 实验工况 30 ml/min, 125.5 μm (Case 9)。 | 对比了三个不同文献的平均换热系数公式与该文的局部换热系数分布。 |
| 水温增长在裂缝入口处较快，后转为缓慢稳定增长。 | [He 2016, pp. 6-8, Fig. 9, Fig. 11] | 恒定隙宽 (125.5 μm) 和多种流量工况。 | 此对数增长规律在非恒定隙宽下也成立。 |

## Limitations
- **数值模型简化**：二维模型中假设裂缝表面无接触凸起体，未考虑真实裂缝的三维复杂结构 [He 2016, pp. 4-6]。
- **温度测量限制**：由于高压下隙宽仅微米级，难以用实验直接测量流体与内壁各点温度，导致局部换热系数的验证高度依赖数值模拟 [He 2016, pp. 2-4]。
- **表面粗糙度表征**：仅沿五个纵向剖面提取分形维数和轮廓波度，其对三维表面粗糙度的整体代表性未从索引片段中确认。

## Assumptions / Conditions
- **模型假设**：水为单相、不可压缩牛顿流体，密度为常数 (1000 kg/m³) [He 2016, pp. 2-4, pp. 4-6]。
- **能量方程简化**：因水密度视为常数，热量方程 (7) 简化为式 (8) [He 2016, pp. 4-6]。
- **模拟设计**：构建二维几何模型时，将二维剖面沿垂直流动方向拉伸一段等于隙宽的距离形成裂缝，不考虑接触凸起体（asperities）的影响 [He 2016, pp. 4-6]。
- **实验边界**：流体通过圆柱形花岗岩试样中的单裂缝，进水端施加不同组合的流量和围压，岩石外壁边界条件未从索引片段中确认。

## Key Variables / Parameters
- **表面粗糙度指标**：分形维数 D，轮廓波度 Ra [He 2016, pp. 1-2, pp. 8-8]。
- **局部换热系数**：h' (W/(m²·K))，由式 (4) 定义 [He 2016, pp. 2-4, pp. 8-8]。
- **平均换热系数**：h (W/(m²·K))，比较了 Chapman [28]， Zhao [3] 和 Zhang et al. [27] 的三组经典公式 [He 2016, pp. 6-8, pp. 8-8]。
- **几何与控制参数**：隙宽 d (μm)，水流速率 u (m/s)，围压 (MPa)，进出口水温 T1, T2 (K) [He 2016, pp. 4-6]。
- **岩石与水物性参数**：水定压比热容 cp,w (4200 J/(kg·K))，岩石和水的导热系数 Kr, Kw [He 2016, pp. 2-4, pp. 6-8]。

## Reusable Claims
- **Claim 1**：对于单相水流经粗糙花岗岩裂缝，壁面对流换热系数（局部换热系数）是随裂缝壁面波度剧烈变化的分布，而非一个固定常数；传统宏观换热关联式在此条件下不再适用。**条件**：微尺度（95–125.5 μm 隙宽）、单相层流、低雷诺数。**证据**：实验和数值结果均表明局部换热系数分布与平均换热系数的恒定值截然不同 [He 2016, pp. 8-8]。
- **Claim 2**：沿流向，当隙宽恒定时，水温与裂缝内壁温度的上升曲线均呈近似对数型，其增长速率在入口处最快，随后减缓。这一规律不受裂缝面分形维数差异的显著影响。**条件**：恒定隙宽、恒定流量。**证据**：五组不同分形维数剖面的模拟结果均显示一致的对数分布 [He 2016, pp. 6-8]。
- **Claim 3**：裂缝轮廓波度的波峰对应局部换热系数的极小值，波谷对应极大值。这一关系由流道形状变化导致的局部流速差异决定。**条件**：裂缝几何由剖面波度Ra和隙宽 d 定义，未考虑三维湍流和接触凸起体。**证据**：局部换热系数与波度 Ra 呈一一对应的镜像关系 [He 2016, pp. 8-8]。

## Candidate Concepts
- [[fracture reservoir]]
- [[Enhanced Geothermal System (EGS)]]
- [[hot dry rock (HDR)]]
- [[joint roughness coefficient (JRC)]]
- [[fracture surface roughness]]
- [[fractal dimension]]
- [[profile waviness]]
- [[local heat transfer coefficient]]
- [[fluid-solid coupling]]
- [[Navier-Stokes equations in fractures]]

## Candidate Methods
- [[Brazilian splitting method]]
- [[laser scanning microscopy for fracture morphology]]
- [[h-L method for fractal dimension]]
- [[COMSOL Multiphysics numerical modeling]]
- [[2D fracture profile modeling from experiment]]
- [[variogram analysis for surface fractals]]

## Connections To Other Work
- **裂隙粗糙度表征**：本文舍弃依赖主观对比的 JRC 方法，转而采用分形维数 D 和轮廓波度 Ra 定量表征，与 Xie 和 Pariseau [18] 提出的 D 与 JRC 正相关的观点衔接 [He 2016, pp. 2-2]。
- **裂隙换热经验公式**：对 Zhao [3]， Chapman [28] 和张国等 [27] 提出的三种平均换热系数公式进行了对比，指出这些公式无法描述局部换热系数的非均匀性 [He 2016, pp. 6-8, pp. 8-10]。
- **EGS研究**：工作在宏观上承接了地热提取中裂隙网络内流体-岩石换热理论，与 Zhao 和 Tso [6] 关于水流在岩体裂隙中对数型温度分布的结论一致 [He 2016, pp. 1-2, pp. 6-8]。
- **流-固耦合方法**：数值模拟方法引用并拓展了 Bai 等人 [26] 关于局部换热特性研究的策略，利用数值模型获取难以通过实验测量的界面温度和温度场 [He 2016, pp. 2-4]。

## Open Questions
- 本文二维模型得出的粗糙度-局部换热系数关系在考虑三维真实裂隙、接触凸起体以及剪切膨胀作用时会发生何种变化？未从索引片段中确认。
- 分形维数 D 和轮廓波度 Ra 是否可作为独立参数，用于预测不同种类岩石裂缝中的换热性能？其普适性未从索引片段中确认。
- 所发现的局部换热系数分布规律在更高流速（如湍流）或气-液两相流条件下的适用性未被探讨。

## Source Coverage
该 Markdown 页面基于提供的 8 个索引片段编译而成。片段主要覆盖了论文的摘要、引言（表面粗糙度量化的背景）、实验方法（试样制备、表面形貌扫描）、数值模拟（控制方程及建模过程）以及关键结果与讨论部分。重要图表（如 Fig. 15, Fig. 16）及其解释在片段中有较详细描述。附录 A 的实验验证数据集提供了精确的实验工况参考。尚缺失的信息包括：结论部分完整总结、参考文献的完整讨论、模型验证的具体误差量化过程，以及对现场尺度和工程应用的延伸讨论。
