---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2016-liu-critical-hydraulic-gradient-for-nonlinear-flow-through-rock-fracture-networks-the-roles"
title: "Critical Hydraulic Gradient for Nonlinear Flow through Rock Fracture Networks: The Roles of Aperture, Surface Roughness, and Number of Intersections."
status: "draft"
source_pdf: "data/papers/2016 - Critical hydraulic gradient for nonlinear flow through rock fracture networks The roles of aperture, surface roughness, and number of intersections.pdf"
collections:
  - "雷恩学派分形研究"
citation: "Liu, Richeng, et al. \"Critical Hydraulic Gradient for Nonlinear Flow through Rock Fracture Networks: The Roles of Aperture, Surface Roughness, and Number of Intersections.\" *Advances in Water Resources*, vol. 88, 2016, pp. 53–65. doi:10.1016/j.advwatres.2015.12.002."
indexed_texts: "15"
indexed_chars: "71675"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T19:45:39"
---

# Critical Hydraulic Gradient for Nonlinear Flow through Rock Fracture Networks: The Roles of Aperture, Surface Roughness, and Number of Intersections.

## One-line Summary
通过物理实验和数值模拟，系统研究了孔径、表面粗糙度和交叉点数量对离散裂隙网络(DFN)中非线性流启动的临界水力梯度(J_c)的影响，并建立了基于Forchheimer定律的J_c及其系数的多变量回归预测公式。[Liu 2016, pp. 1-2]

## Research Question
在离散裂隙网络(DFN)中，流体流动从线性（符合立方定律）向非线性（符合Forchheimer定律）转变的临界水力梯度(J_c)如何受裂隙孔径、表面粗糙度和裂隙交叉点数量的影响？如何确立DFN中非线性流动启动的准则？[Liu 2016, pp. 1-2]

## Study Area / Data
- **物理模型**: 两个交叉裂隙模型，一个表面光滑(S模型)，一个表面粗糙(R模型)。每个模型有四个节段和一个交叉点。S模型的节段平均机械孔径(h_M)为1.23 mm，R模型为1.17 mm。R模型裂隙的表面粗糙度用Z_2（0.14-0.43）和JRC（4.47-20.30）量化。[Liu 2016, pp. 2-4]
- **数值模型**: 基于物理模型建立和验证后，生成了具有不同孔径(h_M = 0.5–10 mm)、交叉点数量(N_i = 1–12)、表面粗糙度(JRC = 0–20)和水力梯度(J = 10⁻⁸–10⁰)的DFN系列模型。[Liu 2016, pp. 6-7]

## Methods
1.  **物理实验**: 对光滑(S)和粗糙(R)两个交叉裂隙模型进行了水流测试，使用高精度CCD相机结合图像处理获取裂隙几何形状，采用不同进出口组合（形成60°, 120°, 180°交叉角）进行测试。[Liu 2016, pp. 2-4]
2.  **数值模拟**: 使用基于有限体积法(FVM)的ANSYS FLUENT软件直接求解Navier-Stokes(NS)方程，模拟物理模型及大量具有不同几何特征的DFN模型。[Liu 2016, pp. 4-5]
3.  **非线性量化**: 使用Forchheimer定律（J = AQ + BQ²）拟合水力梯度(J)和流量(Q)的关系。引入因子E = BQ²/(AQ+BQ²)来量化非线性贡献，并以E = 0.01作为临界值J_c的判定标准。[Liu 2016, pp. 5-6]
4.  **回归分析**: 基于模拟结果，采用多变量回归算法建立了系数A、B和临界水力梯度J_c与孔径(h_M)、粗糙度(JRC)和交叉点数量(N_i)之间的数学表达式(8)-(10)。[Liu 2016, pp. 7-8]

## Key Findings
- **非线性判定**: 当E = 0.01时，R模型和S模型的临界雷诺数(Re)存在显著差异（例如，在outlet_2&3情况下，R模型Re = 13.81，S模型Re = 100.01），表明粗糙表面显著降低了非线性流动启动的Re阈值。[Liu 2016, pp. 5-6]
- **孔径(h_M)的主导作用**: 影响J_c最关键的因素是孔径。当h_M从0.5 mm增加到5 mm时，系数A和B的值下降三到四个数量级。孔径越大，J_c越低，非线性流越容易出现。[Liu 2016, pp. 7-8]
- **粗糙度(JRC)的作用**: 粗糙度较大的裂隙表面会导致在更低的J_c下启动非线性流动。但其影响比孔径小几个数量级。[Liu 2016, pp. 6-7]
- **交叉点数量(N_i)的作用**: DFN中交叉点数量越多，会导致在更低的J_c下启动非线性流动。但其影响也比孔径小几个数量级。[Liu 2016, pp. 6-7]
- **交叉角的影响**: 在单交叉点模型中，不同的交叉角（60°, 120°, 180°）对J-Q关系的影响远小于表面粗糙度和孔径的影响。[Liu 2016, pp. 5-5]
- **预测公式**: 建立了基于孔径、粗糙度和交叉点数量的指数型多变量回归方程((8)-(10))，用于预测Forchheimer定律系数A、B和临界水力梯度J_c，预测值与模拟结果的相关性很高。[Liu 2016, pp. 7-8]
- **适用性说明**: 提出的公式可能仅适用于工程活动最为活跃的浅层岩体。对于孔径极小的深层岩石（< 0.1 mm），达到J_c所需的极大水力梯度在自然界中几乎不存在，因此公式的适用范围受限。[Liu 2016, pp. 7-8]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 对于outlet_2&3组合，粗糙模型(R)的临界雷诺数Re=13.81，光滑模型(S)的Re=100.01。 | [Liu 2016, pp. 6-6] | 单交叉点物理模型，E=0.01。 | 粗粗糙度显著降低了流态转变阈值。 |
| 当水力梯度J低于J_c时，Forchheimer定律简化为广泛使用的立方定律。 | [Liu 2016, pp. 1-2] | 非线性项被消除。 | 这是整个研究的理论基础。 |
| 当h_M从0.5 mm增加至5 mm（一个数量级），A和B的值下降三到四个数量级。 | [Liu 2016, pp. 7-8] | DFN数值模型。 | 证明孔径是影响A, B, J_c的主要因素。 |
| N_i和JRC的类似变化导致A和B的变化小于一个数量级。 | [Liu 2016, pp. 7-8] | DFN数值模型。 | 证明N_i和JRC的影响远小于h_M。 |
| 当E=0.01时，非线性项仅占总压降的1%。 | [Liu 2016, pp. 5-6] | 物理模型和数值模拟。 | 文中采用的J_c判定标准，比前人研究(E=0.1)更严格。 |
| 拟合公式(8)-(10)见表2，与模拟结果的相关系数很高。 | [Liu 2016, pp. 7-8] | 多变量回归。 | 系数的具体数值和表2未在片段中显示。 |
| 当孔径低于0.1 mm时，达到J_c需要自然界几乎不存在的水力梯度。 | [Liu 2016, pp. 7-8] | 基于公式(10)的预测。 | 公式对深层岩石的适用性有限。 |

## Limitations
- 数值模型的网格层数(10层)是基于计算时间和精度的折中选择，可能不足以完全再现大雷诺数下交叉口等几何突变位置的涡流结构。[Liu 2016, pp. 5-5]
- 用于建立预测公式的DFN模型几何形状较为简单，其有效性有待于在更真实、几何特征更复杂的DFN模型中进行进一步验证。[Liu 2016, pp. 7-8]
- 玻璃制造的物理模型表面可能缺乏天然岩石裂隙的微观粗糙度，仅代表了一级粗糙度。[Liu 2016, pp. 3-4]
- 当孔径较小时(<0.1mm，如深层岩石)，非线性效应不显著，建立的表达式可能不适用。[Liu 2016, pp. 7-8]
- 未从索引片段中确认该方法对三维裂隙网络、多相流或应力耦合条件下的适用性。

## Assumptions / Conditions
- **流动控制方程**: 数值模拟直接求解Navier-Stokes(NS)方程，其中对流加速项是几何变化引起非线性的唯一来源。对于天然裂隙中的层流，该假设成立。[Liu 2016, pp. 4-5]
- **边界条件**: 数值模型在裂隙壁面上采用无滑移边界条件。[Liu 2016, pp. 4-5]
- **临界非线性判据**: 定义E = 0.01为临界值，即非线性压降占总压降的1%时，流动进入非线性区域。这是基于本研究高精度实验系统系统误差的估计。[Liu 2016, pp. 5-6]
- **粗糙度表征**: 利用高斯分布的节点位移生成裂隙粗糙度，并使用JRC（0-20）作为代表性的粗糙度参数。JRC=0代表光滑，JRC=20代表极粗糙。[Liu 2016, pp. 6-7]
- **模型维度**: 所有模型均为二维离散裂隙网络（DFN）模型。[Liu 2016, pp. 6-7]
- **孔径分布**: 回归公式(8)-(10)中引入系数 λ 来量化DFN内裂隙孔径变化导致的h_M折减。若所有裂隙h_M相同，λ = 1 mm⁻¹。[Liu 2016, pp. 7-8]

## Key Variables / Parameters
- `J`: Hydraulic Gradient (水力梯度)
- `J_c`: Critical Hydraulic Gradient (临界水力梯度)
- `Q`: Flow Rate (流量)
- `Re`: Reynolds Number (雷诺数)
- `h_M`: Mechanical Aperture (机械孔径)
- `JRC`: Joint Roughness Coefficient (节理粗糙度系数)
- `Z_2`: 表面粗糙度无量纲参数
- `N_i`: Number of Intersections (交叉点数量)
- `A`: Forchheimer定律线性项系数
- `B`: Forchheimer定律非线性项系数
- `E`: 非线性项对总压降的贡献比率
- `λ`: 孔径变异折减系数

## Reusable Claims
- **Claim 1**: 在单个交叉裂隙模型中，对于相同的平均机械孔径，表面粗糙度是使流动在更低Re下进入非线性区域的主要因素。例如，当E=0.01时，粗糙模型(Re≈13-32)的临界雷诺数远低于光滑模型(Re≈50-100)。[Liu 2016, pp. 5-6] [条件：单交叉点，水流，J由并联路径平均计算，E=0.01作为非线性判据]。
- **Claim 2**: 在离散裂隙网络(DFN)中，裂隙的机械孔径是控制非线性流启动的最主要参数。其影响幅度（导致系数A和B变化3-4个数量级）远超交叉点数量和粗糙度（导致A和B变化小于1个数量级）。[Liu 2016, pp. 7-8] [条件：范围h_M=0.5-5mm, JRC=0-20, N_i=1-12，基于NS方程模拟]。
- **Claim 3**: Forchheimer定律（J = AQ + BQ²）可以很好地量化DFN中从线性到非线性的流动关系；当J < J_c（本研究定义为E=0.01）时，非线性项(BQ²)的贡献可以忽略，流动回归为立方定律。[Liu 2016, pp. 1-2, 5-6] [条件：层流假设，无滑移边界，单相牛顿流体]。

## Candidate Concepts
- [[Discrete Fracture Network, DFN 离散裂隙网络]]
- [[Nonlinear Flow 非线性流]]
- [[Critical Hydraulic Gradient 临界水力梯度]]
- [[Forchheimer's Law Forchheimer定律]]
- [[Cubic Law 立方定律]]
- [[Joint Roughness Coefficient, JRC 节理粗糙度系数]]
- [[Mechanical Aperture 机械孔径]]
- [[Navier-Stokes Equations N-S方程]]
- [[Finite Volume Method, FVM 有限体积法]]
- [[Reynolds Number 雷诺数]]

## Candidate Methods
- [[Image Processing For Fracture Geometry 图像处理获取裂隙几何]]
- [[Computational Fluid Dynamics, CFD 计算流体力学]]
- [[Direct Numerical Simulation of NS Equations NS方程直接数值模拟]]
- [[Multi-variable Regression Analysis 多变量回归分析]]
- [[ANSYS Fluent Simulation ANSYS Fluent模拟]]
- [[Critical Nonlinearity Factor E Method 临界非线性因子E法]]

## Connections To Other Work
- **与非线性流动机理研究的关系**: 以前的研究广泛探讨了粗糙表面和裂隙交叉口处涡旋形成等驱动非线性流的微观机制（文献[12,34,35,76]），但本文指出这些微观现象对DFN宏观水力特性的影响尚未被定量评估。[Liu 2016, pp. 2-2]。
- **与立方定律应用的关系**: 以前大多数研究假设立方定律总是适用，而不考虑J的大小（文献[2,3,15,31,37,40,41,43,52,59,70,71,72,73,74,75]）。本研究旨在解决此问题，确定立方定律适用的J_c阈值。[Liu 2016, pp. 2-2]。
- **与临界E值选择的关系**: 本研究中使用了E=0.01作为临界值，比文献[25,69]中使用的E=0.1更严格，这是因为本实验系统精度更高。[Liu 2016, pp. 5-6]。
- **与粗糙度表征参数的关系**: 本研究利用Z_2与JRC的经验关系（公式(1)(2)，引用自[46,62]和[5,50]），将岩体力学中的粗糙度表征与水力行为联系起来。[Liu 2016, pp. 3-4, 6-7]。
- **候选联系**: 主题上，本研究可与 [[fracture reservoir]]，[[groundwater hydrology]] 和 [[geothermal systems]] 等领域的裂隙渗流研究相关联。

## Open Questions
- 需要验证本研究中基于简单几何DFN提出的预测公式在具有更真实几何特征（如二维剖面切割三维网络、更复杂的孔径分布）的DFN模型中的有效性。[Liu 2016, pp. 7-8]
- 未从索引片段中确认J_c与裂隙网络连通性、裂隙长度分布等其他拓扑特性的关系。
- 未从索引片段中确认该方法在应力-渗流耦合或非饱和流动条件下的适用性。

## Source Coverage
本页基于提供的15个索引片段撰写。片段覆盖了论文的标题、摘要、引言、方法（物理实验与数值模拟设置）、部分结果分析和讨论（单交叉口模型和DFN模型的关键发现）、以及结论（回归公式及其局限性）。片段密集覆盖了研究动机、核心方法、关键变量和主要结论，但缺乏对DFN生成算法、回归分析具体统计量（如R²数值）、验证过程以及讨论部分的完整数据表（如Table 2的全部内容）。
