---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2020-thomas-permeability-of-three-dimensional-numerically-grown-geomechanical-discrete-fracture"
title: "Permeability of Three-Dimensional Numerically Grown Geomechanical Discrete Fracture Networks With Evolving Geometry and Mechanical Apertures."
status: "draft"
source_pdf: "data/papers/2020 - Permeability of Three-Dimensional Numerically Grown Geomechanical Discrete Fracture Networks With Evolving Geometry and Mechanical Apertures.pdf"
collections:
citation: "Thomas, Robin N., et al. \"Permeability of Three-Dimensional Numerically Grown Geomechanical Discrete Fracture Networks With Evolving Geometry and Mechanical Apertures.\" *Journal of Geophysical Research: Solid Earth*, vol. 125, no. 7, 2020, e2019JB018899. doi:10.1029/2019JB018899."
indexed_texts: "22"
indexed_chars: "106579"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T01:21:11"
---

# Permeability of Three-Dimensional Numerically Grown Geomechanical Discrete Fracture Networks With Evolving Geometry and Mechanical Apertures.

## One-line Summary
该研究提出了一种三维数值生长的地质力学离散裂缝网络（GDFN）生成方法，并量化了裂缝几何演化与力学开度对等效渗透率张量的影响，发现相比随机DFN，GDFN具有更强的各向异性和沟道化流动特征 [Thomas 2020, pp. 1-1]。

## Research Question
如何将裂缝扩展的力学过程（包括裂缝相互作用、非平面生长）直接纳入三维离散裂缝网络建模，并评估由此产生的几何形态和力学开度对网络等效渗透率的影响？[Thomas 2020, pp. 1-1, 3-5]。

## Study Area / Data
本研究不依赖于特定实地数据；模拟域为一边长 20 m 的立方体，内部预置初始缺陷（微小裂缝），在远程单轴拉伸应力作用下准静态扩展 [Thomas 2020, pp. 3-5, 5-6]。材料属性取低渗透脆性岩石的典型值 [Thomas 2020, pp. 6-7]。无实测裂缝网络或现场渗透率数据被使用。

## Methods
1. **裂缝网络生成**：采用 Imperial College Geomechanics Toolkit（ICGT）的有限元方法，基于线弹性断裂力学模拟多裂缝并发扩展。裂缝尖端应力强度因子（SIFs）由位移相关法（DC）计算，结合三类 SIF（KI、KII、KIII）的等效 SIF（Kv）判断扩展 [Thomas 2020, pp. 6-7]。扩展长度遵循修正的两步 Paris-type 律，扩展方向由混合模式经验公式（式 4）确定，扭曲角被忽略以简化离散化 [Thomas 2020, pp. 6-7]。裂缝相交时，尖端被去激活（停止扩展），至于是 T 型或 X 型相交不做区分 [Thomas 2020, pp. 7-8]。
2. **渗透性计算**：在每个生长步，求解三个独立的稳态、单相达西流问题，边界条件为对向等压源汇（100 Pa 和 10 Pa），其余边界为无流边界。基质渗透率固定为 10⁻¹⁵ m²，裂缝渗透率由局部开度 h 通过立方定律 kf = h²/12 计算 [Thomas 2020, pp. 8-9]。通过单元体积加权平均压力梯度和流速，根据达西定律求取等效渗透率张量 k（3×3 矩阵）[Thomas 2020, pp. 8-9]。
3. **对比方案**：生成两组随机 DFN 作为基准，比较 GDFN 的等效渗透率 [Thomas 2020, pp. 1-1]。

## Key Findings
- 裂缝间的力学相互作用导致网络中裂缝非均匀、非平面生长，并可使初始不活跃的裂缝重新激活 [Thomas 2020, pp. 1-1]。
- 均匀开度假设下，GDFN 的等效渗透率张量呈强各向异性，在裂缝强度较高时渗透率值高于随机 DFN [Thomas 2020, pp. 1-1]。
- 当裂缝开度按力学原理分配时，流动强烈聚拢为离散的沟道化路径，裂缝方位和相互作用会显著改变开度分布，进而影响网络水力性质 [Thomas 2020, pp. 1-1]。

## Core Evidence Table

| Evidence                                                                                                                                                                                                 | Source                              | Conditions                                                                                                           | Notes                                                                                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| GDFN 在均匀裂缝开度条件下表现出强各向异性等效渗透率张量，且高裂缝强度时渗透率高于对比随机 DFN。                                                                                                              | [Thomas 2020, pp. 1-1]              | 远程单轴拉伸应力，线弹性均质各向同性岩石，准静态生长，均匀开度假设。                                                  | 强各向异性被认为是力学驱动的裂缝优势取向所致。                                                                                  |
| 采用力学开度（由裂缝局部变形决定）后，GDFN 内流体流动出现显著的沟道化，裂缝方位和相互作用直接影响开度并改变渗透性。                                                                                     | [Thomas 2020, pp. 1-1]              | 开度由力学计算获得，非预设均匀值；基质渗透率固定为 10⁻¹⁵ m²，裂缝渗透率遵循 kf = h²/12。                                   | 沟道化现象意味着流动主要集中在少量高开度路径上。                                                                                |
| 裂缝力学相互作用改变尖端应力分布，导致网络中裂缝呈非平面、非均匀扩展，并使某些初始不活跃裂缝再次扩展。                                                                                                 | [Thomas 2020, pp. 1-1]              | 多裂缝在有限域内并发扩展，考虑了尖端应力强度因子的三种模式。                                                            | 该行为无法被常规随机 DFN 复现。                                                                                                  |
| 采用修正的 Paris-type 扩展律可以在三维条件下实现多裂缝尖端的并发生长，扩展长度由应变能释放率 G 决定（式 5）。                                                                                              | [Thomas 2020, pp. 6-7]              | 准静态拉伸加载，线弹性，KIC = 1.8×10⁶ Pa·m¹ᐟ²，韧性比 α₁ = 1/1.3268，α₂ = 1/0.6297。                                    | 该方法避免了固定步长假设，可体现不同尖端能量差异性。                                                                             |
| 裂缝相交处理采用简化策略：尖端一遇到边界或其他裂缝即被冻结，暂不区分 T 型或 X 型相交。                                                                                                                   | [Thomas 2020, pp. 7-8]              | 拉伸边界条件，裂缝面不传力；未使用 Renshaw & Pollard 或 Cheng 等复杂相交准则。                                          | 文中明确此为简化，并指出未来工作需要研究不同相交类型的影响。                                                                     |

## Limitations
- 裂缝相交处理简单，所有相交均停止尖端扩展，未区分 T 型与 X 型相交，且未采用基于局部应力场的穿越/终止准则 [Thomas 2020, pp. 7-8]。
- 模拟仅针对远程单轴拉伸应力，未考虑压缩、剪切、摩擦接触或多相流体 [Thomas 2020, pp. 3-5, 7-8]。
- 岩石基质为线弹性、均质、各向同性，未纳入非均质性、塑性变形或孔隙弹性效应 [Thomas 2020, pp. 5-6]。
- 扭曲角（mode III 分解）被忽略，实际三维裂缝尖端可能出现更复杂的几何形态，增加了离散化难度 [Thomas 2020, pp. 6-7]。
- 渗透率计算基于单相不可压缩达西流，且裂缝透射率使用抛物线律（立方定律），未考虑裂缝粗糙度或非达西效应 [Thomas 2020, pp. 8-9]。
- 片段未包含详细的网格敏感性分析和计算性能讨论，可能缺失数值收敛性验证的结果。

## Assumptions / Conditions
- 岩石基质：线弹性、均质、各向同性，服从静态弹性方程 [Thomas 2020, pp. 5-6]。
- 荷载：远程单轴拉伸应力作用于正方体域顶部，底部固定，侧边界无面力，不计重力 [Thomas 2020, pp. 5-6]。
- 裂缝扩展：准静态，基于线性弹性断裂力学；使用等效 SIF（Kv）和修正 Paris 律确定扩展量；忽略模式 III 导致的扭曲角 [Thomas 2020, pp. 6-7]。
- 裂缝相交：尖端一接触任何边界或裂缝即停止扩展 [Thomas 2020, pp. 7-8]。
- 流动：单相不可压缩流体，服从达西定律；裂缝渗透率 kf = h²/12，其中 h 为局部力学开度 [Thomas 2020, pp. 8-9]。
- 韧性参数针对低渗脆性岩石：KIC = 1.8×10⁶ Pa·m¹ᐟ²，KIC/KIIC = 1/1.3268，KIC/KIIIC = 1/0.6297 [Thomas 2020, pp. 6-7]。

## Key Variables / Parameters
- **Kv**：等效应力强度因子，综合 KI、KII、KIII [Thomas 2020, pp. 6-7]
- **G** (G_n)：应变能释放率，用于 Paris 律扩展长度 [Thomas 2020, pp. 6-7]
- **h**：裂缝局部力学开度 [Thomas 2020, pp. 8-9]
- **kf = h²/12**：裂缝渗透率（立方定律） [Thomas 2020, pp. 8-9]
- **k**：等效渗透率张量 (3×3) [Thomas 2020, pp. 8-9]
- **KIC, KIIC, KIIIC**：断裂韧性及比值 α₁, α₂ [Thomas 2020, pp. 6-7]
- **φ**：扩展角，由混合模式公式决定 [Thomas 2020, pp. 6-7]
- **域尺寸**：20 m 立方体 [Thomas 2020, pp. 3-5]
- **基质渗透率**：10⁻¹⁵ m² [Thomas 2020, pp. 8-9]
- **源汇压差**：100 Pa → 10 Pa [Thomas 2020, pp. 8-9]

## Reusable Claims
1. 在远程单轴拉伸条件下，**基于断裂力学并发生长的 GDFN 具有比随机 DFN 更强的渗透率各向异性**，这源于裂缝取向受应力控制而非随机分配。当裂缝强度（单位体积裂缝面积）较高时，GDFN 的均匀开度等效渗透率值也高于随机网络 [Thomas 2020, pp. 1-1]。**条件**：线弹性均质各向同性岩石，准静态生长。**限制**：未验证压缩、剪切或非均质条件下的表现。
2. **当 GDFN 的裂缝开度由局部力学变形计算（而非均匀赋值）时，网络流动会自然产生沟道化**，即大部分流量仅通过少数高开度裂缝；裂缝之间的相互作用会进一步放大开度差异 [Thomas 2020, pp. 1-1]。**条件**：开度是线性弹性变形结果，不包含粗糙度或接触摩擦。**限制**：沟道化程度可能受基质渗透率、边界应力方向影响，片段未提供定量沟道化指标。
3. **利用等效 SIF（Kv）和修正 Paris 律可实现多裂缝并发、非均匀扩展的三维模拟**，扩展长度与局部应变能释放率成正比，能重现裂缝屏蔽、应力集中导致再激活等现象 [Thomas 2020, pp. 1-1, 6-7]。**条件**：KIC 确定，韧性比固定，忽略扭曲角以保持尖端平滑。**限制**：Paris 律参数需根据材料校准，适用范围限于亚临界裂缝生长。
4. **简化裂缝相交处理（全部停止扩展）在纯拉伸加载下是合理的**，因为裂缝面不传递应力，但可能导致渗透率估计偏差，未来应比较 T 型终止与 X 型穿越的影响 [Thomas 2020, pp. 7-8]。**条件**：拉伸应力，裂缝面未接触。**限制**：实际岩体中常见 X 型相交，此简化可能高估连通性在某些阈值下的衰减。

## Candidate Concepts
- [[geomechanical discrete fracture network]]
- [[stress intensity factor]]
- [[mixed mode fracture propagation]]
- [[equivalent permeability tensor]]
- [[channeling flow in fractures]]
- [[linear elastic fracture mechanics]]
- [[Paris law for fracture growth]]
- [[displacement correlation method for SIF]]
- [[fracture interaction]]
- [[Darcy flow in fractured media]]

## Candidate Methods
- [[finite element method for elasticity and flow]]
- [[displacement correlation SIF computation]]
- [[modified Paris law for concurrent growth]]
- [[equivalent permeability upscaling via Darcy experiments]]
- [[octree meshing for fracture simulations]]
- [[stochastic discrete fracture network generation]]

## Connections To Other Work
- **随机 DFN 建模**：与众多使用泊松点过程或分形理论生成的随机 DFN 直接对比，包括 Ebigbo et al. (2016)、Leung & Zimmerman (2012)、Mourzenko et al. (2011)、Sævik et al. (2013) 等研究 [Thomas 2020, pp. 1-2]。
- **伪地质力学 DFN**：区别于使用启发式规则（如幂律长度分布、伪力学中止/成核规则）的 DFN 生成方法（Bonneau et al., 2016; Davy et al., 2013; Maillot et al., 2016 等），本研究严格模拟了变形与断裂过程的物理本质 [Thomas 2020, pp. 2-3]。
- **ICGT 的扩展应用**：文中所用数值框架此前已用于研究压缩应力下的裂缝扩展（Thomas et al., 2020b）、摩擦接触（Nejati et al., 2016）以及热‑水‑力耦合过程（Salimzadeh et al., 2018），表明该方法具有向多物理场拓展的潜力 [Thomas 2020, pp. 3-5]。
- **裂缝相交准则**：现有的线性弹性介质摩擦表面穿越/终止准则（如 Renshaw & Pollard, 1995；Cheng et al., 2014）因计算成本高、非平面三维相交难以定义单一角度而未采用，留待后续研究 [Thomas 2020, pp. 7-8]。

## Open Questions
- 当考虑 T 型终止与 X 型穿越的精确相交准则时，GDFN 的连通性和渗透率将如何变化？[Thomas 2020, pp. 7-8]
- 在压缩、剪切应力条件下，GDFN 的渗透率演变是否仍表现出强各向异性和沟道化？[Thomas 2020, pp. 3-5] 未从片段确认。
- 裂缝粗糙度、多相流与基质‑裂缝耦合传输对等效渗透率计算结果有何影响？未从片段确认。
- 该方法能否通过实际野外裂缝网络几何与渗透率数据进行标定和验证？未从片段确认。

## Source Coverage
本页依据 22 个索引片段编写，覆盖了论文的摘要、引言、方法（几何与离散化、弹性变形、SIF 计算、扩展准则、裂缝相交、流动模拟）等核心内容，涉及页码约 1-9 页（共 24 页）。缺失部分主要位于**结果与讨论**章节（约第 10–24 页），因此无法详细展示 GDFN 与随机 DFN 的渗透率随裂缝强度变化的定量对比曲线、开度分布统计、各向异性参数演化等具体数据。此外，文中提及的网格敏感性分析、计算性能对比及最终结论的数值支撑也未被片段覆盖。本页的定量声明主要来源于摘要和方法描述，有待补充完整文章以提升证据密度。
