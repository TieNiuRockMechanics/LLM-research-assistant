---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-salimzadeh-thermoporoelastic-effects-during-heat-extraction-from-low-permeability-reservoir"
title: "Thermoporoelastic Effects during Heat Extraction from Low-Permeability Reservoirs."
status: "draft"
source_pdf: "data/papers/2018 - Thermoporoelastic effects during heat extraction from low-permeability reservoirs.pdf"
collections:
  - "part3-3"
citation: "Salimzadeh, Saeed, et al. \"Thermoporoelastic Effects during Heat Extraction from Low-Permeability Reservoirs.\" *Energy*, vol. 142, 2018, pp. 546-558. doi:10.1016/j.energy.2017.10.059."
indexed_texts: "12"
indexed_chars: "57552"
nonempty_source_blocks: "12"
compiled_source_blocks: "12"
compiled_source_chars: "56505"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "0.981808"
coverage_status: "full-index"
source_signature: "5cfcaf70142ed362c834f11fd577806c21abe180"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T21:24:00"
---

# Thermoporoelastic Effects during Heat Extraction from Low-Permeability Reservoirs.

## One-line Summary
本文提出一种耦合热‑水力（TH）模型，并与力学接触模型（M）顺序耦合，研究低渗透裂缝型地热储层采热过程中的热孔弹性效应，重点探讨基质流体“不排水热膨胀系数”假设的适用性，并提出部分排水条件下的有效热膨胀系数估算方法。[Salimzadeh 2018, pp. 1-3]

## Research Question
在增强型地热系统（EGS）中，低渗透岩石基质的流体在采热冷却过程中，何时能视为不排水状态？若不排水假设不成立，如何确定部分排水条件下的等效热膨胀系数以准确预测热‑孔弹性变形？ [Salimzadeh 2018, pp. 2, 15‑16]

## Study Area / Data
算例基于一个水平圆盘形裂缝（半径500 m）位于3×3×3 km立方体中的理想化EGS储层，大致参考澳大利亚Cooper Basin的Habanero项目。注水井与生产井相距500 m，以恒定流量0.0125 m³/s注入50°C冷水，生产井保持34 MPa，初始温度200°C，基质孔隙度0.01，基质渗透率1×10⁻²⁰ m²。岩石及流体物性见表1，如杨氏模量50 GPa、泊松比0.25、固相热膨胀系数2.4×10⁻⁵/°C、流体热膨胀系数7.66×10⁻⁴/°C。[Salimzadeh 2018, pp. 8-9, 22]

## Methods
采用一种隐式考虑孔隙弹性基质体应变的TH模型，其推导基于总应力不变的假设，将体应变表示为孔隙压力和温度的函数。TH模型求解基质压力、裂缝压力、基质温度和裂缝温度；裂缝流动遵循立方定律，裂缝开度采用Barton‑Bandis模型，由力学接触模型（M）提供的接触应力更新。TH与M顺序迭代：每个时间步先用上一时间步的裂缝开度运行TH，获得压力和温度场，然后运行M计算接触应力与开度。M使用基于间隙的增广拉格朗日（AL）法处理裂缝面接触，且摩擦滑动被限制（stick模式）。基质与裂缝之间的漏失量和热量交换被考虑，局部热非平衡假设成立。空间离散采用二次四面体和三角形，时间离散用有限差分，整体代数方程组由SAMG代数多重网格求解器求解。[Salimzadeh 2018, pp. 4-8]

## Key Findings
- 在基质渗透率 km = 1×10⁻²⁰ m² 的EGS算例中，基质流体实为部分排水状态，并非不排水。采用不排水热膨胀系数高估了基质收缩和裂缝开度增长，而排水系数则低估；前者的热突破（生产水温降至130°C）不足21年，后者延长至27.6年。[Salimzadeh 2018, pp. 10, 12]
- 要实现不排水条件，水力扩散系数必须远小于热扩散系数（α_Dh ≤ 0.01 α_DT），对应的临界基质渗透率当α=1时为 km ≤ 8.43×10⁻²³ m²，远低于一般EGS储层渗透率。因此，多数EGS项目不能假定为不排水。[Salimzadeh 2018, pp. 13]
- 降低Biot系数α（从1.0到0.2）使系统行为更接近排水状态，不排水所需临界渗透率进一步降至 km ≤ 2.6×10⁻²³ m²。α减小减弱了压力变化引起的体积收缩，延缓了热突破。[Salimzadeh 2018, pp. 13-14]
- 提高孔隙度（从0.01到0.10）增大了不排水与排水结果的差距：φ=0.1时，不排水热膨胀系数β_u=3.21×10⁻⁵/°C，排水热突破时间由28.6年提前至20.6年。部分排水情况（km=10⁻²⁰ m²）位于两者之间。[Salimzadeh 2018, pp. 14]
- 定义了基于注入点裂缝开度的无量纲排水比δ_D，发现δ_D与无量纲扩散比ξ_D = 1 - log(α_Dh/α_DT) 呈线性关系。利用该关系可计算有效热膨胀系数 β_eq = β_s + δ_D φ B (β_f ‑ β_s)，用于等效模拟部分排水效应。测试案例显示，该有效系数比单纯使用排水或不排水系数能更好地逼近全热孔弹性模型结果，但δ_D随时间变化会导致一定偏差。[Salimzadeh 2018, pp. 15-16]

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 不排水热膨胀系数得到的生产水温降至130°C的时间 < 21年，排水情况为27.6年；不排水假设显著提前热突破。 | [Salimzadeh 2018, pp. 10] | 均匀初始开度，注入量0.0125 m³/s，α=1，φ=0.01 | 与Guo et al. (2016)结果吻合，验证模型 |
| 基质渗透率 km=1×10⁻²⁰ m² 时，生产水温与裂缝开度结果处于排水与不排水之间，且更接近排水情况。 | [Salimzadeh 2018, pp. 12] | 排水热膨胀系数β_s=2.4×10⁻⁵/°C，不排水β_u=3.0×10⁻⁵/°C | 说明常用EGS渗透率下实际为部分排水 |
| 要使不排水条件成立（α_Dh ≤ 0.01 α_DT），当α=1时 km ≤ 8.43×10⁻²³ m²；α=0.2时 km ≤ 2.6×10⁻²³ m²。给定 km=10⁻²⁰ m² 时，t_Dp = 1.2 t_Dh，不排水假设不可接受。 | [Salimzadeh 2018, pp. 13] | 基于一维扩散无量纲时间，t_D=0.001对应过程完成3% | 热扩散慢是即使超低渗透仍无法保持不排水的主因 |
| δ_D与ξ_D的线性回归可用于预测部分排水下的等效热膨胀系数。测试案例（φ=0.05,α=0.40,km=2×10⁻²¹ m²）预测δ_D=0.509，全模型计算δ_D=0.507，有效系数β_eq=3.02×10⁻⁵/°C的结果优于纯排水/不排水。 | [Salimzadeh 2018, pp. 15-16] | 基于注入点30年末裂缝开度定义δ_D | δ_D随时间下降，故单时间点估算会引入偏差，但仍大幅改善预测 |

## Limitations
- 推导TH隐式耦合方程时，假设基质内总应力在整个生产周期保持不变，这可能不适用于有明显应力拱效应的储层。[Salimzadeh 2018, pp. 5]
- 力学接触模型仅允许法向接触，未考虑裂缝面滑动（stick模式），无法模拟剪切扩容效应。[Salimzadeh 2018, pp. 8]
- 模型针对单一水平圆盘状裂缝，未考虑多裂缝相互作用及裂缝网络非均质性。[Salimzadeh 2018, pp. 8-9]
- 排水比相关关系来自有限算例，且排水比随时间变化，故用恒定等效系数存在误差，且普适性有待验证。[Salimzadeh 2018, pp. 15-16]

## Assumptions / Conditions
- 基质总应力不变，有效应力变化仅与孔隙压力变化成正比，以此解耦力学变形。[Salimzadeh 2018, pp. 5]
- 裂缝为面状不连续体，两表面间服从Barton‑Bandis经验开度模型，参考点定义为 σ_n=30 MPa时 a_f=0.24 mm，σ_n=5 MPa时 a_f=0.72 mm。[Salimzadeh 2018, pp. 5-6, 8‑9]
- 流体密度随压力和温度变化，遵循式(22)。[Salimzadeh 2018, pp. 8]
- 基质与裂缝流体之间采用局部热非平衡，热交换包括传导和漏失对流。[Salimzadeh 2018, pp. 4]
- 储层均质且初始开度均匀（验证算例）；除 km=10⁻¹⁷、10⁻¹⁸ m² 外，漏失量可忽略。[Salimzadeh 2018, pp. 10]
- 裂缝剪切滑动被抑制，仅考虑法向压缩变形。[Salimzadeh 2018, pp. 8]

## Key Variables / Parameters
- 基质渗透率 km (10⁻¹⁷ ~ 10⁻²² m²)
- Biot系数 α (0.2, 1.0)
- 孔隙度 φ (0.01, 0.10)
- 注入流量 (0.0125 m³/s)，注入温度50°C，初始温度200°C
- 固体热膨胀系数 β_s = 2.4×10⁻⁵/°C，流体热膨胀系数 β_f = 7.66×10⁻⁴/°C
- 裂缝开度模型参数 a, b
- 不排水热膨胀系数 β_u，排水系数 β_s，等效系数 β_eq
- 水力扩散系数 α_Dh，热扩散系数 α_DT
- 无量纲排水比 δ_D = (a_f - a_fD)/(a_fU - a_fD)，扩散比 ξ_D = 1 - log(α_Dh/α_DT)

## Reusable Claims
- 在低渗EGS储层中，即使基质渗透率低至10⁻²⁰ m²量级，亦不能简单假定孔隙流体为不排水状态；只有当水力扩散系数至少比热扩散系数低两个数量级时，不排水假设才近似成立，对应的渗透率通常需低于10⁻²² m²。[Salimzadeh 2018, pp. 13]
- 采用排水热膨胀系数会低估基质的热致体积应变，而不排水系数会高估；对于部分排水系统，可利用无量纲排水比线性关系构造有效热膨胀系数，显著改善无全耦合模拟时的预测精度，但该系数并非恒定，使用时需注意时间依赖性。[Salimzadeh 2018, pp. 15-16]
- Biot系数越小，基质体积变形对孔隙压力变化的敏感度越低，热突破延迟，且实现不排水所需临界渗透率更低。[Salimzadeh 2018, pp. 13-14]
- 提高孔隙度会增大不排水热膨胀系数（因流体的热膨胀远大于固体），同时增加基质的等效热容，拉大不排水与排水预测差距，使部分排水状态更需精细处理。[Salimzadeh 2018, pp. 14]

## Candidate Concepts
- [[partially drained thermal expansion]]
- [[undrained thermal expansion coefficient]]
- [[effective thermal expansion coefficient]]
- [[dimensionless drainage ratio]]
- [[Barton-Bandis fracture model]]
- [[thermoporoelasticity]]
- [[hydraulic vs thermal diffusivity]]
- [[Biot coefficient]]
- [[Augmented Lagrangian contact mechanics]]
- [[local thermal non-equilibrium]]

## Candidate Methods
- [[implicitly coupled thermo-hydraulic model]]
- [[sequential TH-M coupling]]
- [[finite element method with quadratic tetrahedral and triangular elements]]
- [[gap-based augmented Lagrangian contact algorithm for fractures]]
- [[Galerkin finite difference temporal discretisation]]
- [[algebraic multigrid solver SAMG]]
- [[hydro-mechanical decoupling by constant total stress assumption]]
- [[cubic law for fracture flow]]
- [[leakoff heat and mass exchange model]]

## Connections To Other Work
本文构建的隐式TH模型是基于Salimzadeh et al. (2017a,b,c)的完全耦合热‑水‑力模型解耦而来，以降低超低渗透率储层模拟的计算成本。裂缝开度计算使用经典的Barton‑Bandis模型（Bandis et al., 1983; Barton et al., 1986），不排水热膨胀系数参考了McTigue (1986)的理论。验证算例采用Guo et al. (2016)的EGS几何和结果，证明模型正确性。热‑孔弹性参数关系与Zimmerman (2000)和Biot (1941)的经典理论一致。文中关于热扩散与水力扩散的比较方法借鉴了Carslaw and Jaeger (1959)的扩散时间尺度概念。[Salimzadeh 2018, pp. 2-4, 8, 10, 13]

## Open Questions
- 本研究提出的排水比‑扩散比线性关系能否推广到多裂缝网络和非均质储层？
- 若允许裂缝滑动（包括剪切扩容），部分排水条件下的有效热膨胀修正是否需要调整？
- 有效热膨胀系数随时间变化，是否可建立随时间演化的函数形式以进一步提高预测精度？
- 注入流量和裂缝几何尺寸对临界排水条件的影响规律如何？
- 在不同地应力路径（如总应力并不是完全恒定）下，隐式耦合的适用性边界是什么？

## Source Coverage
本次编写基于论文《Thermoporoelastic Effects during Heat Extraction from Low-Permeability Reservoirs》的全部索引片段。总计12个非空索引块（compiled source blocks 12），覆盖原文第1–32页。索引字符数57,552，编译后源字符数56,505，按块覆盖率为1.0，按字符覆盖率为0.9818。所有非空片段均被处理，未添加任何非原文证据。
