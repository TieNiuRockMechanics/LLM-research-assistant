---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2009-zhao-investigation-of-fractal-distribution-law-for-the-trace-number-of-random-and-grouped-f"
title: "Investigation of Fractal Distribution Law for the Trace Number of Random and Grouped Fractures in a Geological Mass."
status: "draft"
source_pdf: "data/papers/2009 - Investigation of fractal distribution law for the trace number of random and grouped fractures in a geological mass.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Zhao, Yangsheng, et al. \"Investigation of Fractal Distribution Law for the Trace Number of Random and Grouped Fractures in a Geological Mass.\" *International Journal of Rock Mechanics and Mining Sciences*, vol. 46, no. 8, 2009, pp. 1347-1355."
indexed_texts: "7"
indexed_chars: "32362"
nonempty_source_blocks: "7"
compiled_source_blocks: "7"
compiled_source_chars: "32506"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.00445"
coverage_status: "full-index"
source_signature: "a53e876c239d4ec41b5c4aab1fe142df9bd3e0c0"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T18:00:48"
---

# Investigation of Fractal Distribution Law for the Trace Number of Random and Grouped Fractures in a Geological Mass.

## One-line Summary
地质体裂隙（迹线）数目在不同尺度上遵循分形分布规律，且分组后的裂隙以及不同岩层间的裂隙分维数与岩石强度-弹性模量积存在幂函数关系。[Zhao 2009, pp. 1-1, 5-6]

## Research Question
1. 地质体裂隙数目是否随观测尺度呈现某种普适分布律？该律在不同规模地质体中是否一致？[Zhao 2009, pp. 1-1]
2. 按走向分组后，裂隙数目的分布是否仍保持分形特征？分组后的分维数有何变化？[Zhao 2009, pp. 1-1]
3. 同一构造区内不同岩层的裂隙数目分布与其力学参数（强度、弹性模量）之间存在怎样的相关关系？[Zhao 2009, pp. 1-1, 4-5]

## Study Area / Data
- 现场原位观测：中国13个煤矿区（轩岗、汾西、东山、阳泉、大同等）的工作面、巷道等。[Zhao 2009, pp. 1-1, 2-3]
- 室内煤样：采集自20余个煤矿区的煤块，实验室统计了边长100 mm的煤样裂隙。[Zhao 2009, pp. 1-1, 2-3]
- 微观观测：煤样磨片在显微镜下统计微裂隙，原尺度L₀=1 mm，子尺度0.5 mm、0.25 mm，共观测25,250个方格、100,000条裂隙。[Zhao 2009, pp. 2-3]
- 岩心：汾西、介休的3个地质钻孔（1002、1006、试验6-1），深度范围60 m ~ 609 m。[Zhao 2009, pp. 4-5, 5-6]
- 地质图件：东山、汾西、轩岗矿区的一般地质图、煤层断层图，研究断层迹线分形。[Zhao 2009, pp. 3-4]
- 尺度范围：最大边长2400 m，最小0.25 mm，跨度7个数量级。[Zhao 2009, pp. 2-3]

## Methods
- **二维盒计数法**：对实测地质体选定初始尺度 L₀，统计长度≥L₀ 的裂隙数；逐次将网格边长减半（L₀/2ⁿ⁻¹），重复计数，建立裂隙迹线数 N 与网格尺度 L 的关系 N = N₀ (L₀/L)⁻ᴰ [Zhao 2009, pp. 1-2]。该方法直接采用裂隙条数而非百分数 [Zhao 2009, pp. 2-3]。
- **重随机/弱随机分布定义**：若裂隙位置和方向均随机，称**重随机裂隙分布**；若走向可分组而位置随机，称**弱随机裂隙分布** [Zhao 2009, pp. 1-2]。
- **分组统计**：按地质观测将裂隙（或断层）依走向分组，分别计算各组的裂隙数目分维数 [Zhao 2009, pp. 3-4]。
- **岩心测试**：对岩心制备平行/垂直于层理的平面，统计两方向上裂隙数目的分维，同时测定单轴抗压强度（UCS）和弹性模量，拟合分维数与强度–模量积的幂律关系 [Zhao 2009, pp. 4-5]。
- 分维数计算采用线性回归，并给出标准差和相关系数（如相关系数80.9%–93.18%）[Zhao 2009, pp. 5-6]。

## Key Findings
1. **重随机分布的分形律**：无论是现场煤壁、实验室煤样还是显微镜下微裂隙，裂隙数目均良好服从分形律；尺度从2400 m至0.25 mm跨越7个数量级均一致 [Zhao 2009, pp. 2-3]。例如，工作面和煤样的分维数多在1.3–1.8之间 [Zhao 2009, pp. 1-1, 2-3]。
2. **按走向分组的分形律**：裂隙（包括断层）按走向分组后仍然遵循分形分布，但各走向组的分维数不同。例如，东山矿灰岩中，主裂隙100°组分维1.7095，次裂隙170°组1.3732，25°组1.4532 [Zhao 2009, pp. 3-4]。断层分组后，主次断层分维数的大小关系在不同矿区不同：汾西、轩岗主断层分维大于次断层，而东山相反 [Zhao 2009, pp. 3-4, 6-6]。
3. **岩层分维数与力学参数的关系**：同一钻孔内不同岩层的裂隙数目分维 D 与岩石的单轴抗压强度 σ 和弹性模量 E 的乘积 Q = σ·E 呈幂函数关系 Q = a Dᵇ，相关性较高（如水平方向拟合 R²≈86% – 93%）[Zhao 2009, pp. 5-6]。**Q 越大，D 越大，反之亦然** [Zhao 2009, pp. 5-6, 6-6]。这一结果可用岩层在相同构造应力下不同变形阶段（弹性→弹塑性→应变软化）解释 [Zhao 2009, pp. 5-6]。
4. **断层预测意义**：分组断层的分形律为断层预测和岩体工程稳定性评价提供了定量基础 [Zhao 2009, pp. 3-4, 6-6]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 现场煤壁裂隙分维 D=1.48–1.70 | [Zhao 2009, pp. 1-1] Table 1 | 工作面巷道，L₀=0.5 m或1.0 m | 5个矿区的数据 |
| 室内煤块裂隙分维 D=1.33–1.76 | [Zhao 2009, pp. 1-1] Table 2 | L₀=100 mm | 17个煤样，分维平均约1.55 |
| 显微镜微裂隙分维 D=1.28–1.84 | [Zhao 2009, pp. 2-3] Table 3 | L₀=1 mm | 10个煤样，最短尺度0.25 mm |
| 地质图断层分维 D=1.20–1.66 | [Zhao 2009, pp. 3-4] Table 4 | 原图尺度2400 m–270 m | 8幅地质图，包含断层与一般地质图 |
| 岩样裂隙分维 D=1.38–1.92 | [Zhao 2009, pp. 3-4] Table 5 | 钻孔岩样，L₀=60–150 mm | 石灰岩、泥岩、凝灰岩等 |
| 分组裂隙分维对比：东山灰岩主100°组1.71，次170°组1.37 | [Zhao 2009, pp. 3-4] Table 7 | 井下实测，按走向分组 | 多组数据均显示走向分组后分维差异 |
| 分组断层分维：汾西Cuijiagou 2#煤主20–30°组1.48，次60–65°组1.31 | [Zhao 2009, pp. 4-5] Table 8 | 煤层断层图，按走向分组 | 主次断层分维差0.16 |
| 岩层裂隙分维与强度–模量积幂律：D与Q的幂指数2.2–4.3，R²≥0.81 | [Zhao 2009, pp. 5-6] Table 12, Fig. 4 | 3个钻孔，水平/垂直方向分别拟合 | 幂律系数随钻孔变化 |

## Limitations
- 裂隙迹线数目分形仅描述数量与尺度的关系，**不包含裂隙的确定位置和方向信息**（文中定义为“弱随机”和“重随机”），无法直接重建裂隙网络几何 [Zhao 2009, pp. 1-2]。
- 岩层分维–强度–模量关系的研究仅基于汾西、介休等地的三个钻孔，**样本量有限**，幂律系数的普适性需要更多地区验证 [Zhao 2009, pp. 5-6]。
- 分维数对走向分组的窗口选择（主、次走向范围）和初始尺度敏感，但文中未评估这种不确定性 [Zhao 2009, pp. 3-4]。
- 未讨论分形无标度区的上下界限；文中最大尺度2400 m、最小0.25 mm，但不同地质体可能具有不同的无标度区间 [Zhao 2009, pp. 2-3]。
- 不同煤区主次断层分维大小关系不一致（东山与汾西、轩岗相反），**原因尚未解释** [Zhao 2009, pp. 3-4, 6-6]。

## Assumptions / Conditions
- 采用二维盒计数法，且统计时要求“裂隙长度≥网格边长”时才计入 [Zhao 2009, pp. 1-2]。
- 初始尺度 L₀ 和初始裂隙数 N₀ 在“标准情况”下均取1，便于比较 [Zhao 2009, pp. 1-2]。
- 重随机分布假设：裂隙位置和方向均为随机；弱随机分布假设：方向可据构造分组，位置随机 [Zhao 2009, pp. 1-2]。
- 岩层分维–力学参数分析假定：同一构造区内各岩层经历了**近乎相同的构造运动**，且本次构造期决定了当前裂隙分布 [Zhao 2009, pp. 1-1, 5-6]。

## Key Variables / Parameters
- 裂隙迹线数 N
- 网格尺度 L（边长，mm、m 等）
- 初始尺度 L₀（如 0.5 m、100 mm、1 mm）
- 分维数 D（拟合直线斜率）
- 裂隙数目分布的“初始值” N₀（L=L₀ 时的裂隙数）
- 裂隙走向分组（如主100°组、次25°组等）
- 单轴抗压强度 UCS (MPa)
- 弹性模量 E (GPa)
- 强度–弹性模量积 Q = UCS × E (GPa²)
- 幂律拟合公式 Q = a·Dᵇ 中的系数 a 和指数 b

## Reusable Claims
- 裂隙数目分布的幂律形式：N = N₀ (L₀/L)⁻ᴰ 适用于从米级到微米级的裂隙统计，分维数 D 通常在 1.2–1.9 之间。[Zhao 2009, pp. 1-2, 2-3]
- 在经历相似构造运动的沉积岩层中，**裂隙数目分维 D 与岩石的强度–弹性模量积 Q 呈正幂律相关**，即 Q ∝ Dᵇ（b>0），且这一关系在垂直和平行层理方向均可观测。[Zhao 2009, pp. 5-6, 6-6] (注: 原文为 power function, 等式形式为 Q = a Dᵇ)
- 按构造走向分组后，各组的裂隙数目仍各自服从分形分布，但**不同走向组的 D 值不同**，使得断层或裂隙网络的主次方向分维存在差异。[Zhao 2009, pp. 3-4, 6-6]
- 在同一构造单元内，主要断层（或裂隙）的走向在不同地层和尺度之间存在一定偏转，但**分维数相近**，平均偏差异<0.081。[Zhao 2009, pp. 4-5, 6-6]

## Candidate Concepts
- [[分形裂隙分布]] – Fractal fracture distribution
- [[二维盒维数]] – 2D box-counting dimension
- [[重随机裂隙分布]] – Heavy random fracture distribution
- [[弱随机裂隙分布]] – Weak random fracture distribution
- [[裂隙迹线数–尺度幂律]] – Fracture trace number-scale power law
- [[强度–模量积分形律]] – Product of strength and modulus vs. fractal dimension power law
- [[分组断层分维]] – Grouped fault fractal dimension
- [[无标度区间]] – Scale-invariant range
- [[构造裂隙走向分组]] – Tectonic fracture strike grouping

## Candidate Methods
- [[二维盒计数法直接计数裂隙条数]] – 2D box counting with direct fracture count (not percentage)
- [[多尺度裂隙统计（宏观–细观–微观）]] – Multi-scale fracture observation (in situ → lab → microscope)
- [[钻孔岩心平行/垂直层理面制备与裂隙统计]] – Core specimen preparation parallel and perpendicular to bedding
- [[裂隙走向分组分形分析]] – Fractal analysis after tectonic strike grouping
- [[单轴抗压强度与弹性模量测定]] – Uniaxial compressive strength and elastic modulus testing
- [[幂律回归拟合Q=a·Dᵇ]] – Power-law regression between D and Q

## Connections To Other Work
- La Pointe (1988) 的二维盒计数法用于裂隙密度，但仅计百分比，本文则直接使用裂隙条数 [Zhao 2009, pp. 1-2]。
- Barton & Larsen (1985)、Aviles et al. (1987)、Hirata (1989) 等研究过断裂网络的分形特征，但未涉及数量与尺度的分维 [Zhao 2009, pp. 1-2]。
- 本文所用的“分形裂隙分布律”在前人（如 Turcotte 1989, Xie 1993）等岩石力学分形研究基础上，进一步扩展到分组和力学参数关联 [Zhao 2009, pp. 1-1]。
- 与赵阳升等（2002, 2005）关于岩层裂隙分形分布及三维分形模拟的工作一脉相承 [Zhao 2009, pp. 1-1, 6-6]。

## Open Questions
- 在岩层分维–强度–模量幂律中，系数 a 和指数 b 是否由构造应力大小、期次等决定？能否建立更一般的预测模型？[Zhao 2009, pp. 5-6]
- 为什么不同矿区主、次断层分维大小关系相反（东山 vs. 汾西、轩岗）？是否与区域应力场的差异有关？[Zhao 2009, pp. 4-5, 6-6]
- 本方法是否能直接用于三维裂隙网络的分维推断？文中提及了“3D fractal distribution emulation”（赵等 2005），但未在本研究中深入 [Zhao 2009, pp. 1-1]。
- 裂隙分维数是否与渗透率、岩体损伤等工程特性有定量联系？本文仅提供了数量分布规律，未涉及渗透-力学耦合 [Zhao 2009, pp. 6-6]。
- 分维数的上下截止尺度受哪些因素控制？文中未探索无标度区边界 [Zhao 2009, pp. 2-3]。

## Source Coverage
本次利用全部已索引碎片（共7个非空片段，32,506字符），所有片段均被处理。覆盖比率按片段为100%，按字符为100.44% (coverage_ratio_by_chars: 1.00445)。无遗漏内容。所有声称均来自所提供片段，未添加外部信息。
