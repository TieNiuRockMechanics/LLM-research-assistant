---
type: "paper"
paper_id: "2020-thomas-permeability-of-three-dimensional-numerically-grown-geomechanical-discrete-fracture"
title: "Permeability of Three-Dimensional Numerically Grown Geomechanical Discrete Fracture Networks With Evolving Geometry and Mechanical Apertures."
status: "draft"
source_pdf: "data/papers/2020 - Permeability of Three-Dimensional Numerically Grown Geomechanical Discrete Fracture Networks With Evolving Geometry and Mechanical Apertures.pdf"
citation: "Thomas, Robin N., et al. \"Permeability of Three-Dimensional Numerically Grown Geomechanical Discrete Fracture Networks With Evolving Geometry and Mechanical Apertures.\" *Journal of Geophysical Research: Solid Earth*, 2020, doi:10.1029/2019JB018899."
indexed_texts: "22"
indexed_chars: "106579"
compiled_at: "2026-04-27T19:43:02"
---

# Permeability of Three-Dimensional Numerically Grown Geomechanical Discrete Fracture Networks With Evolving Geometry and Mechanical Apertures.

## One-line Summary
应用有限元、线性弹性断裂力学方法生成三维[[geomechanical discrete fracture network (GDFN)]]，对比随机DFN，GDFN具有强各向异性和更高渗透率，且基于力学原理的孔径导致流体流动强烈通道化 [Thomas 2020, pp. 1-1]。

## Research Question
如何将力学过程（裂缝扩展与相互作用）纳入离散裂缝网络模型，以及力学机制如何影响裂缝网络几何、孔径演变和渗透率特性？[Thomas 2020, pp. 1-1] 未从索引片段中确认更精确的问题陈述。

## Study Area / Data
- 数值模拟区域：20 m × 20 m × 20 m 立方体域 [Thomas 2020, pp. 5-6]。
- 初始裂缝形状：圆盘状，从初始缺陷开始生长 [Thomas 2020, pp. 3-5]。
- 岩石材料：线性弹性、均质、各向同性，低渗透性脆性岩石，KIC = 1.8×10⁶ Pa·m^(1/2)，KIC/KIIC = 1/1.3268，KIC/KIIIC = 1/0.6297 [Thomas 2020, pp. 6-7]。
- 边界条件：远程单轴拉伸应力作用于顶面（+Z），底面固定，其他边界无牵引 [Thomas 2020, pp. 5-6]。未施加重力体力 [Thomas 2020, pp. 5-6]。
- 未从索引片段中确认具体的地质或现场数据。

## Methods
- **裂缝生长方法**：基于[[stress intensity factor (SIF)]]的准静态有限元方法，采用位移相关法计算尖端三个模式的SIF（K_I, K_II, K_III）[Thomas 2020, pp. 5-6]。
- **生长准则**：使用比较SIF Kv（包含所有模式）评估是否生长；扩展角度φ基于Richard公式（A=140°, B=-70°）计算；扩展长度基于应变能释放率，采用改进两步Paris型律处理多裂缝同步生长 [Thomas 2020, pp. 6-7]。
- **裂缝相交处理**：尖端与边界或其他裂缝相交时停活，不对T型或X型相交做区分 [Thomas 2020, pp. 7-8]。
- **渗透率计算**：每个生长步骤后，通过有限元法求解三个方向的单相达西流（源100 Pa，汇10 Pa），计算等效渗透率张量 [Thomas 2020, pp. 8-9]。
- **孔径与渗透率**：裂缝渗透率 k_f = h²/12，h为机械孔径；基质渗透率固定为10⁻¹⁵ m² [Thomas 2020, pp. 8-9]。

## Key Findings
- GDFN中裂缝非均匀、非平面生长，密集网络中应力集中可重新激活初始不活动裂缝 [Thomas 2020, pp. 1-1]。
- 与两组随机DFN相比，均匀孔径GDFN强各向异性，且在较高裂缝强度下具有更高渗透率 [Thomas 2020, pp. 1-1]。
- 在基于力学原理的机械孔径模型中，流体流动强烈通道化，沿特定路径集中 [Thomas 2020, pp. 1-1]。
- 裂缝取向和相互作用显著改变机械孔径，进而控制网络水力特性 [Thomas 2020, pp. 1-1]。

## Limitations
- 未从索引片段中确认明确的局限性陈述。根据方法推断：
- 裂缝相交处理过于简单（仅停活），未考虑T型与X型相交对渗透率的不同影响 [Thomas 2020, pp. 7-8]。
- 模拟仅限拉伸应力条件，未考虑压缩、摩擦或接触 [Thomas 2020, pp. 3-5]。
- 未纳入模式III撕裂导致的复杂尖端几何 [Thomas 2020, pp. 6-7]。
- 未考虑重力体力对裂缝生长的影响 [Thomas 2020, pp. 5-6]。

## Reusable Claims
- 对于低渗透性脆性岩石，可采用KIC = 1.8×10⁶ Pa·m^(1/2)，KIC/KIIC = 1/1.3268，KIC/KIIIC = 1/0.6297作为典型材料参数 [Thomas 2020, pp. 6-7]。
- 三维混合模式裂缝扩展角φ可由Richard公式计算：φ = ∓[140°·(|KII|/(KI+|KII|+|KIII|)) + (-70°)·(|KII|/(KI+|KII|+|KIII|))²] [Thomas 2020, pp. 6-7]。
- 在达西流模拟中，岩石基质渗透率可取10⁻¹⁵ m²，流体粘度取1×10⁻³ Pa·s [Thomas 2020, pp. 8-9]。
- 裂缝渗透率与机械孔径的平方成正比（k_f = h²/12）[Thomas 2020, pp. 8-9]。

## Candidate Concepts
- [[geomechanical discrete fracture network (GDFN)]]
- [[stress intensity factor (SIF)]]
- [[mechanical aperture]]
- [[equivalent permeability tensor]]
- [[fracture intersection]]
- [[channelized flow]]

## Candidate Methods
- [[displacement correlation method for SIF computation]]
- [[quasi-static fracture growth algorithm]]
- [[modified two-step Paris law for concurrent fracture growth]]
- [[finite element method for Darcy flow and permeability upscaling]]

## Open Questions
未从索引片段中确认。可能方向包括：如何更精确处理三维裂缝相交（如T型/X型对渗透率的影响）；压缩应力下GDFN渗透率行为；模式III撕裂对渗透率的作用；接触与摩擦的耦合效应。

## Source Coverage
索引片段主要覆盖摘要、引言、方法（几何离散化、线性弹性变形、SIF计算、生长准则、相交处理、渗透率计算）。讨论与结论部分的具体分析、图表示例、对比结果细节未从索引片段中获取。
