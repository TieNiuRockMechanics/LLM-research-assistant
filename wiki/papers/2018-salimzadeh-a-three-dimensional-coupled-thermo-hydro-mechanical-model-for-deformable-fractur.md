---
type: "paper"
schema_version: "paper-v4-2026-04-30"
paper_id: "2018-salimzadeh-a-three-dimensional-coupled-thermo-hydro-mechanical-model-for-deformable-fractur"
title: "A Three-Dimensional Coupled Thermo-Hydro-Mechanical Model for Deformable Fractured Geothermal Systems."
status: "draft"
source_pdf: "data/papers/2018 - A three-dimensional coupled thermo-hydro-mechanical model for deformable fractured geothermal systems.pdf"
collections:
  - "part3-3"
citation: "Salimzadeh, Saeed, et al. “A Three-Dimensional Coupled Thermo-Hydro-Mechanical Model for Deformable Fractured Geothermal Systems.” *Geothermics*, vol. 71, 2018, pp. 212-24. doi:10.1016/j.geothermics.2017.09.012."
indexed_texts: "13"
indexed_chars: "64271"
nonempty_source_blocks: "13"
compiled_source_blocks: "13"
compiled_source_chars: "64601"
compiled_stage_count: "1"
single_pass_char_budget: "320000"
compile_strategy: "single-pass-markdown"
coverage_ratio_by_blocks: "1.0"
coverage_ratio_by_chars: "1.005135"
coverage_status: "full-index"
source_signature: "3f4199cbadb80851d66aaee284d5a850a48198da"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-05-01T20:08:20"
---

# A Three-Dimensional Coupled Thermo-Hydro-Mechanical Model for Deformable Fractured Geothermal Systems.

## One-line Summary
本文提出一个三维全耦合热-水-力（THM）有限元模型，将裂缝视为三维基岩内的二维面间断，通过增广拉格朗日接触模型求解裂缝面接触应力，并应用于冷流体注入引起的流动通道化效应的研究。

## Research Question
冷流体注入可变形裂缝地热储层时，热-水-力多场耦合如何影响流体流动、热交换以及裂缝开度的演化？尤其是热体积收缩导致的流动通道化和应力重分布如何发生？

## Study Area / Data
- **算例1（刚性裂缝，渗透基岩）**：裂缝长度100 m，注入井与生产井，平面应变；恒定注入速率Q=0.0001 m³/s，冷水温度20 °C，初始岩石温度100 °C；基岩渗透率从0增至1×10⁻¹² m²。材料参数见表1（示例1）。对比Bodvarsson(1969)和Ghassemi et al.(2008)的解。
- **算例2（可变形裂缝，不渗透基岩）**：水平圆盘状裂缝，直径200 m，注入井和生产井距中心50 m；注入速率Q=0.001 m³/s，水温20 °C，初始岩石温度80 °C；法向地应力σ=60 MPa，初始流体压力p_i=20 MPa；裂缝刚度10¹¹ Pa/m，零接触应力时裂缝开度0.6 mm；基岩E=37.5 GPa，ν=0.25；水黏度按温度变化。
- **算例3（可变形裂缝，渗透基岩）**：圆形裂缝直径400 m，倾角30°；垂直注入井与生产井间距300 m，仅下部20 m射孔，井与裂缝不直接连接；注入/生产速率均为0.005 m³/s，水温20 °C；基岩渗透率k_m=10⁻¹⁴ m²，E=20 GPa，ν=0.20，Biot系数α=0.8；裂缝刚度10¹¹ Pa/m，零接触开度0.6 mm。三组条件对比：情况1（T_ini=80 °C，σ_ini=60 MPa），情况2（T_ini=250 °C，σ_ini=60 MPa），情况3（T_ini=250 °C，σ_ini=75 MPa）；初始流体压力均为20 MPa，初始时间步1天，最大步长0.2年。

## Methods
- **全耦合THM有限元模型**：包含热弹性力学模型、基质流动模型、裂缝流动模型、基质传热模型和裂缝传热模型五个子模型；位移u、基质压力p_m、裂缝压力p_f、基质温度T_m和裂缝温度T_f作为主变量。
- **力学**：基于Biot有效应力（α系数）和热弹性本构；裂缝面承受流体压力与接触应力，通过增广拉格朗日接触模型求解。
- **流动**：裂缝流动服从立方定律，开度与接触开度相关；基质与裂缝间存在漏失（达西定律），实现质量与能量交换。
- **传热**：基质内固液局部热平衡；裂缝与基质间通过壁面导热和漏失对流进行热交换；考虑对流-扩散。
- **数值**：Galerkin有限元空间离散，有限差分时间离散；四面体（二次）和三角形（二次）单元；裂缝两侧节点重复，裂缝方程单侧求解，耦合矩阵两侧累加；Picard迭代更新系数（加权系数θ=2/3，容差0.01）；代数多重网格求解器（SAMG）。
- **接触迭代**：每一时间步内THM与接触模型顺序迭代，直至压力和温度与接触应力收敛。
- **实现平台**：Imperial College Geomechanics toolkit 和 CSMP++。

## Key Findings
- 冷流体注入使基岩冷却收缩，降低裂缝接触应力，增大开度，形成从注入井指向生产井的流动通道（flow channelling），其余区域热提取显著减少。
- 应力重分布使接触应力先下降后回升：开度增量在约7年达峰值后减小，这一效应降低了纯张性裂缝扩展的可能性，但扩大低接触应力区可能增加剪切破坏风险。
- 渗透基岩情况下，裂缝初始开度控制早期流动；随基岩降温，开度增加，裂缝逐渐成为优势通道；漏失量随时间动态变化，与固定漏失率假设的结果明显不同。
- 算例3对比表明：高温差（250 °C）和较高初始开度（接触应力60 MPa）的情况最早形成强优势通道，生产井温度下降最快（案例2）；低初始开度（75 MPa）案例开度增量绝对值最大，但通道面积较小；低初始温度（80 °C）案例热收缩和开度变化均最小。
- 验证结果：不渗透刚性裂缝与Bodvarsson(1969)解吻合良好；渗透情况与Ghassemi et al.(2008)解相比，动态漏失造成更长的热提取期。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 全耦合THM有限元模型同时求解位移、基质压力和温度、裂缝压力和温度 | Salimzadeh 2018, pp. 3-7 | 单相流，弹性变形，基质内局部热平衡 | Picard迭代，容差0.01 |
| 裂缝开度受接触应力影响，接触应力由增广拉格朗日接触模型迭代获得 | Salimzadeh 2018, pp. 7-9 | 裂缝刚度K_n=10¹¹ Pa/m | 线性或非线性开度-应力关系可用 |
| 冷流体注入导致基岩收缩，接触应力降低，开度增大，形成流动通道 | Salimzadeh 2018, pp. 12-13, Figs.5,8-10 | 圆盘裂缝算例，温差明显 | 通道化降低其他区域热提取 |
| 应力重分布使最小接触应力在约7年后上升，开度增量随后减小 | Salimzadeh 2018, pp. 12-13, Fig.12 | 三种不同初始温度和接触应力情况 | 案例3中显著 |
| 动态漏失导致的生产温度下降比固定漏失率假设缓慢 | Salimzadeh 2018, pp. 9-10 | 基岩渗透率1×10⁻¹³ m²，2D漏失 | 对比Ghassemi et al.(2008)解 |
| 高温差和高初始开度条件下温度突破最早 | Salimzadeh 2018, pp. 12-13, Fig.12 | T_ini=250 °C, σ_ini=60 MPa (案例2) | 开度增量非最大，但通道效率最高 |
| 验证算例与Bodvarsson(1969)不渗透解吻合 | Salimzadeh 2018, pp. 9-10 | 刚性裂缝，1D扩散 | 验证热传递模块 |

## Limitations
- 模型假设单相流动，未包含多相流或相变。
- 基岩变形为线弹性，未考虑塑性、损伤或断裂扩展过程。
- 接触模型采用线性关系，未使用非线性裂缝刚度模型。
- 裂缝表面忽略流体剪切牵引力。
- 仅通过简单几何算例验证和展示，未处理复杂多裂缝网络。
- 三维大规模裂缝系统需并行计算（作为未来工作方向）。

## Assumptions / Conditions
- 线弹性变形，小变形假设，有效应力原理（Biot理论）。
- 基质各向同性，热物理性质均匀。
- 裂缝为平行光滑表面，满足立方定律。
- 漏失项垂直于裂缝方向由达西定律控制。
- 流体为牛顿型，密度随压力和温度变化（barotropic）。
- 传热为对流-扩散，忽略热辐射和机械耗散。
- 忽略重力（示例中流动以水平为主）。
- 接触模型与THM模型在单个时间步内顺序迭代，更新接触应力。
- Picard迭代采用加权因子θ=2/3，收敛容差0.01。

## Key Variables / Parameters
- 主变量：u（位移），p_m（基质压力），p_f（裂缝压力），T_m（基质温度），T_f（裂缝温度）
- 裂缝开度a_f，接触开度a_fc，接触应力σ_c，法向接触应力σ_n，裂缝刚度K_n
- 基岩渗透率k_m，法向渗透率k_n，基质孔隙度ϕ
- Biot系数α，固体颗粒体积模量K_s，基岩排水体积模量K
- 弹性模量E，泊松比ν
- 基岩热膨胀系数β_s，流体热膨胀系数β_f
- 基岩导热系数λ_s，流体导热系数λ_f，平均导热系数λ_m
- 流体比热容C_f，基岩比热容C_s，等效体积热容ρ_m C_m
- 流体黏度μ_f（温度函数，如式(64)）
- 注入速率Q，注入温度，初始储层温度T_ini，初始地应力σ_ini，初始流体压力p_i

## Reusable Claims
- [Reusable] 冷流体注入地热储层时，基岩热收缩降低裂缝接触应力、增大开度，形成流动通道化；温差和初始开度越大，该效应越显著[Salimzadeh 2018, pp. 12-13, Figs.8-12]。
- [Reusable] 接触应力先因冷却减小，后因受影响区域扩大而发生应力重分布而回升，最大开度增量的非单调演化降低了纯张性裂缝扩展的可能，但可能增加剪切破坏风险[Salimzadeh 2018, pp. 13, Fig.12]。
- [Reusable] 在渗透基岩中，裂缝漏失不应假定为固定比率，而须动态耦合计算；固定漏失率假设会高估后期温度下降[Salimzadeh 2018, pp. 9-10]。
- [Reusable] 全耦合THM框架可分别建立基质和裂缝的压力/温度方程，并通过接触模型更新裂缝面牵引力，适用于可变形裂缝地热系统[Salimzadeh 2018, pp. 3-7,14]。
- [Reusable] 数值实现中采用二次四面体和三角形单元、Picard迭代（θ=2/3）和代数多重网格求解器可有效求解非线性THM方程组[Salimzadeh 2018, pp. 5-7]。
- [Reusable] Biot系数α仅出现在基质方程中，用于耦合基质流动与变形；裂缝流动不直接含α[Salimzadeh 2018, pp. 5]。

## Candidate Concepts
- [[全耦合THM模型]] (fully coupled thermal-hydraulic-mechanical model)
- [[裂缝-基质耦合流动]] (fracture-matrix coupled flow)
- [[立方定律]] (cubic law)
- [[增广拉格朗日接触模型]] (augmented Lagrangian contact model)
- [[流动通道化]] (flow channelling)
- [[热收缩致裂缝开度变化]] (thermally-induced aperture change)
- [[动态漏失]] (dynamic leak-off)
- [[应力重分布]] (stress redistribution)
- [[地热双井系统]] (geothermal doublet)
- [[增强型地热系统]] (enhanced geothermal system, EGS)
- [[局部热非平衡]] (local thermal non-equilibrium)
- [[Picard迭代耦合]] (Picard iteration coupling)

## Candidate Methods
- [[有限元法]](Galerkin离散)  
- [[增广拉格朗日接触算法]](augmented Lagrangian contact)  
- [[THM-接触顺序迭代耦合]] (iteratively coupled THM-contact)  
- [[代数多重网格求解器]](SAMG)  
- [[CSMP++与八叉树网格]] (octree mesher and CSMP++ API)  
- [[二次四面体/三角形单元]] (quadratic tetrahedral/triangular elements)  
- [[加权Picard迭代]](weighted Picard iteration, θ=2/3)

## Connections To Other Work
- 与Bodvarsson (1969)的单裂缝热传递解析解对比验证了不渗透情况。
- 对比Ghassemi et al. (2008)的半解析解，指出其恒定漏失率假设的局限；本研究通过动态漏失计算改进了预测。
- 模型采用Zimmerman and Bodvarsson (1996)的立方定律、Biot (1941)有效应力、Khalili and Selvadurai (2003)的热弹性方程及Nejati et al. (2016)的裂缝增广拉格朗日接触方法。
- 数值工具继承自Paluszny and Zimmerman (2011)的地质力学工具包及Matthäi et al. (2001)的CSMP++平台。
- 本研究与Pandey et al. (2017)、Guo et al. (2016)、Ghassemi and Zhou (2011)等关于裂缝开度演化和热-力耦合的工作相关，但提供了更完整的全耦合三维接触求解。

## Open Questions
- 多裂缝网络、非均质孔径分布对通道化和热提取的影响。
- 非线性裂缝刚度模型（Bandis et al., 1983; Barton et al., 1986）的使用会如何改变结果？
- 大规模并行计算实现含大量离散裂缝的复杂储层模拟。
- 热致破裂（thermally-induced fracturing）的萌生与扩展未直接模拟。
- 裂缝剪切滑移及其对渗透率的动态影响未在本模型中体现。
- 流体相变和多组分效应尚未耦合。

## Source Coverage
已处理全部13个非空索引片段，覆盖文章第1–14页。索引字符数：64,271；汇编源字符数：64,601；字符覆盖率约1.005，表明全文已被完整索引并处理，无遗漏片段。
