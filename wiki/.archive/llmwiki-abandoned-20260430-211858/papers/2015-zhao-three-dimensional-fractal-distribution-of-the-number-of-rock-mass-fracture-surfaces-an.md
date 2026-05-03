---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2015-zhao-three-dimensional-fractal-distribution-of-the-number-of-rock-mass-fracture-surfaces-an"
title: "Three-Dimensional Fractal Distribution of the Number of Rock-Mass Fracture Surfaces and Its Simulation Technology."
status: "draft"
source_pdf: "data/papers/2015 - Three-dimensional fractal distribution of the number of rock-mass fracture surfaces and its simulation technology.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Zhao, Yangsheng, et al. \"Three-Dimensional Fractal Distribution of the Number of Rock-Mass Fracture Surfaces and Its Simulation Technology.\" *Computers and Geotechnics*, vol. 65, 2015, pp. 136–146, doi:10.1016/j.compgeo.2014.12.006."
indexed_texts: "10"
indexed_chars: "47939"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T19:30:17"
---

# Three-Dimensional Fractal Distribution of the Number of Rock-Mass Fracture Surfaces and Its Simulation Technology.

## One-line Summary
通过数值模拟与理论推导，证实了岩体裂隙面数量服从三维分形分布，并建立了二维剖面裂隙迹线分形参数与三维裂隙面分形参数之间的定量关系及模拟技术 [Zhao 2015, pp. 1-2]。

## Research Question
二维分形分析难以全面揭示岩体内部裂隙面的三维分布规律，甚至可能导致错误认知。因此，核心研究问题是：如何在理论上验证裂隙面分布的三维分形模式，并严格描述三维分形几何特征及其与二维分形参数的关系 [Zhao 2015, pp. 2-2]。

## Study Area / Data
此为数值模拟与理论研究，不涉及特定地理区域的现场数据。模拟输入的裂隙数据可通过露头测量和岩芯钻探获得 [Zhao 2015, pp. 2-4]。模拟算例中使用的参数包括：初始尺度 $L_0=1$，三维分形维数 $D_S$ 在 2.0 至 2.9 之间，初始裂隙面数量 $N_S$ 等 [Zhao 2015, pp. 5-7]。

## Methods
1.  **三维分形描述与模拟方法**：
    *   **描述方法**：采用类似计盒维数的方法。将初始立方体（边长 $L_0$）不断二等分，计算每个小立方体（边长 $d_k = L_0/2^k$）内面积等于或大于 $d_k^2$ 的裂隙面数量 $N(L_0/2^k)$，从而定义裂隙面数量的三维分形 [Zhao 2015, pp. 2-2]。
    *   **模拟技术**：基于已知裂隙面的几何参数（中心点坐标 $x_c, y_c, z_c$，法向量 $n$，直径 $r$，倾向 ST，走向 SP）和分形参数（三维分形维数 $D_S$，初始裂隙面数量 $N_S$），利用 Visual C++6.0 MFC 开发了模拟系统，能够生成三维裂隙面网络，并模拟任意剖面和子块中的裂隙分布 [Zhao 2015, pp. 2-5]。

2.  **二维三维关系推导方法**：
    *   提出裂隙面随机分布（RDFS）的三种类型：完全随机、弱随机和分组分布 [Zhao 2015, pp. 1-2]。
    *   通过大量的数值计算和理论推导，分析在不同三维分形维数 ($D_S$)、初始数量 ($N_S$)、倾向 ($ST$) 和走向 ($SP$) 条件下，二维剖面裂隙迹线的分形维数 ($D_L$) 和初始分布值 ($N_L$) 的变化规律 [Zhao 2015, pp. 5-2]。

## Key Findings
1.  **分布规律传递性**：如果三维裂隙面分布服从分形规律，那么其任意剖面上的二维裂隙迹线也服从分形规律，且反之亦然。三种随机分布类型（完全随机、弱随机、分组分布）均满足此规律 [Zhao 2015, pp. 5-2]。
2.  **分形维数关系**：推导出二维剖面裂隙迹线的分形维数 $D_L$ 与三维裂隙面的分形维数 $D_S$ 之间存在关系 $D_L = D_S / C_0 - 1$，其中 $C_0$ 为常数 [Zhao 2015, pp. 1-2]。$D_L$ 与裂隙面的倾向 $ST$ 和走向 $SP$ 无关 [Zhao 2015, pp. 6-2]。
3.  **初始值关系**：二维分形分布的初始值 $N_L$ 与三维分形分布的初始值 $N_S$ 呈线性关系 $N_L = k N_S$，其中 $k$ 由岩体剖面与三维裂隙面的投影关系决定 [Zhao 2015, pp. 1-9]。
4.  **三维分维 $D_S$ 的独立性**：在完全随机分布条件下，二维分形分布的初始值 $N_L$ 与三维分形维数 $D_S$ 的变化无关 [Zhao 2015, pp. 8-2]。
5.  **特例验证**：对于两种特殊情况进行了验证：(1) 当岩体中仅含一个 $L_0 * L_0$ 裂隙面时，$D_S = 2, D_L = 1$；(2) 当任何尺度的子块中均存在一个平行裂隙面时，$D_S = 3, D_L = 2$。这两个特例均符合推导出的 $D_L = D_S - 1$ 的关系 [Zhao 2015, pp. 9-2]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 在分组分布条件下，各剖面裂隙迹线的分形维数基本一致，相关系数 >0.9，最大误差 8.6%。 | [Zhao 2015, pp. 5-6] | 三组模拟参数：Group1: $D_{S1}=2.3,N_{S1}=1,ST_1=30°,SP_1=75°$; Group2: $D_{S2}=2.6,N_{S2}=1,ST_2=60°,SP_2=15°$。初始尺度 $L_0=1$。 | 参阅表4数据。 |
| 二维分形维数 $D_L$ 不随裂隙面的走向 $SP$ 和倾向 $ST$ 变化。 | [Zhao 2015, pp. 6-2, 7-2] | 固定 $D_S=2.405$, 改变 ST (45°, 85°) 和 SP (0°-90°)。 | 参阅图11。 |
| 三维分形维数 $D_S$ 与二维分形维数 $D_L$ 满足关系 $D_L=D_S/C_0-1$。 | [Zhao 2015, pp. 1-2, 9-2] | 通过大量数值计算和理论推导得出，且在 $D_S=2$ 和 $D_S=3$ 的特例中得到验证。 | $C_0$ 的来源未从索引片段中确认。 |
| 二维分形分布初始值 $N_L$ 与三维分形分布初始值 $N_S$ 成线性正比关系 $N_L = k N_S$。 | [Zhao 2015, pp. 1-2, 7-2] | 固定 $D_S$, $ST$, $SP$，$N_S$ 作为变量。 | 参阅图13。比例系数 k 由投影关系决定 [Zhao 2015, pp. 9-2]。 |
| 在完全随机分布下，二维初始值 $N_L$ 不随三维分形维数 $D_S$ 变化。 | [Zhao 2015, pp. 9-2] | 固定初始值 $N_S=1$，$D_S$ 作为变量。 | 参阅图14。 |

## Limitations
1.  对二维和三维分形参数关系的推导主要基于数值模拟实验和理论分析，未从索引片段中确认是否经过了现场大规模实验数据的直接验证。
2.  模拟软件的开发环境（Visual C++6.0 MFC, Windows 环境）表明了其当时的技术平台，可能不反映当前最新的计算架构或跨平台兼容性 [Zhao 2015, pp. 2-4]。
3.  未从索引片段中确认裂隙面的形状假设（如是否为圆盘形）及其曲面对模拟结果影响的分析。

## Assumptions / Conditions
1.  **裂隙面形状假设**：模拟方法中将裂隙面视为圆盘，具有直径 $r$ 和法向量 $n$ 等参数 [Zhao 2015, pp. 2-4]。
2.  **分布类型划分**：研究基于将裂隙面随机分布（RDFS）划分为完全随机、弱随机和分组分布三种类型进行 [Zhao 2015, pp. 1-2]。
3.  **参数范围**：三维分形维数 $D_S$ 被定义为一个介于 2 和 3 之间的有理数，初始裂隙面数量 $N_S$ 是一个大于零的有理数 [Zhao 2015, pp. 4-2]。
4.  **各向异性排布**：模拟算例中裂隙面的倾向 $ST$ 和走向 $SP$ 是给定的固定值或特定分布，反映了特定构造条件下的裂隙分布特征 [Zhao 2015, pp. 5-4]。

## Key Variables / Parameters
*   $D_S$：裂隙面数量的三维分形维数 [Zhao 2015, pp. 1-2]
*   $D_L$：二维剖面裂隙迹线的分形维数 [Zhao 2015, pp. 1-2]
*   $N_S$：三维分形分布的初始值（初始裂隙面数量）[Zhao 2015, pp. 1-2]
*   $N_L$：二维分形分布的初始值 [Zhao 2015, pp. 1-2]
*   $L_0$：初始观测尺度（立方体边长）[Zhao 2015, pp. 2-2]
*   $ST$：裂隙面倾向 [Zhao 2015, pp. 2-4]
*   $SP$：裂隙面走向 [Zhao 2015, pp. 2-4]
*   $r$：裂隙面直径 [Zhao 2015, pp. 2-4]
*   $x_c, y_c, z_c$：裂隙面中心点坐标 [Zhao 2015, pp. 2-4]
*   $k$：$N_L$ 与 $N_S$ 线性关系的比例系数，由投影关系决定 [Zhao 2015, pp. 1-2]
*   $C_0$：$D_L$ 与 $D_S$ 关系式中的常数 [Zhao 2015, pp. 1-2]

## Reusable Claims
*   **Claim 1**：对于服从三维分形分布的岩体裂隙面，其在任意二维剖面上生成的裂隙迹线也必然服从分形分布，且这种对应关系适用于裂隙面的完全随机、弱随机和分组分布三种模式 [Zhao 2015, pp. 5-2]。适用条件：岩体裂隙面数量的三维分布已被证明或假设为分形分布。
*   **Claim 2**：在固定倾向和走向的条件下，裂隙面数量的二维分形参数初始值 $N_L$ 与其三维分形参数初始值 $N_S$ 呈线性正比关系（$N_L = k N_S$）[Zhao 2015, pp. 1-9]。适用条件：已知三维分形维数 $D_S$、倾向 $ST$ 和走向 $SP$。比例系数 $k$ 需通过投影关系确定。
*   **Claim 3**：在裂隙面完全随机分布情况下，二维分形分布的初始值 $N_L$ 与三维分形维数 $D_S$ 的变化无关 [Zhao 2015, pp. 8-2]。适用条件：裂隙面呈完全随机分布，且不分组。
*   **Claim 4**：二维剖面裂隙迹线的分形维数 $D_L$ 与裂隙面的几何产状（倾向 $ST$ 和走向 $SP$）无关，而仅与三维分形维数 $D_S$ 相关 [Zhao 2015, pp. 6-2]。适用条件：裂隙面系统具备整体的分形特征。

## Candidate Concepts
*   [[fracture networks]]
*   [[fracture reservoir]]
*   [[fractal geometry]]
*   [[discrete fracture network (DFN)]]
*   [[scale invariance]]
*   [[geostatistics]]
*   [[rock mass characterization]]

## Candidate Methods
*   [[box-counting method]]
*   [[numerical simulation]]
*   [[outcrop measurement]]
*   [[core drilling analysis]]
*   [[stereology]]
*   [[projection method]]

## Connections To Other Work
本文可视为对裂隙岩体[[fractal geometry]]描述从二维到三维的深化工作，在概念上连接了早期的二维裂隙迹线分形研究 [Zhao 2015, pp. 2-2]。其开发的模拟技术可与[[discrete fracture network (DFN)]]建模方法相联系，为生成符合分形规律的复杂三维[[fracture networks]]提供理论依据。其中关于 $D_S$ 与散系数关系的特例讨论，可能关联到多孔介质中渗透与分形维数的理论模型，但未从索引片段中确认。

## Open Questions
*   常数 $C_0$ 的具体物理意义或确定方法是什么？[Zhao 2015, pp. 1-2]
*   该模拟技术对于非圆盘形（例如多边形）裂隙面的适用性如何？[Zhao 2015, pp. 2-4]
*   如何将二维露头测量数据更准确地反演为三维分形参数 $D_S$ 和 $N_S$ 以驱动模型？

## Source Coverage
本页面基于提供的 10 个索引片段编撰。这些片段主要覆盖了论文的摘要、引言、方法论中的 3D 分形描述与模拟实现、以及结果中的二维-三维分形参数关系推导和核心证据图表。覆盖了论文的核心创新点（$D_S$-$D_L$ 关系，$N_S$-$N_L$ 关系，模拟技术），但可能缺少对文献综述、模拟软件具体功能模块的完整描述、讨论部分的全部细节以及结论部分的内容。
