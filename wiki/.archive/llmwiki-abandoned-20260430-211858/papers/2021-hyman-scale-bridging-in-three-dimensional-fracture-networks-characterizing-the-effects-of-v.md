---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2021-hyman-scale-bridging-in-three-dimensional-fracture-networks-characterizing-the-effects-of-v"
title: "Scale-Bridging in Three-Dimensional Fracture Networks: Characterizing the Effects of Variable Fracture Apertures on Network-Scale Flow Channelization."
status: "draft"
source_pdf: "data/papers/2021 - Scale-Bridging in Three-Dimensional Fracture Networks Characterizing the Effects of Variable Fracture Apertures on Network-Scale Flow Channelization.pdf"
collections:
citation: "Hyman, Jeffrey D., et al. \"Scale-Bridging in Three-Dimensional Fracture Networks: Characterizing the Effects of Variable Fracture Apertures on Network-Scale Flow Channelization.\" *Geophysical Research Letters*, vol. 48, no. 14, 2021."
indexed_texts: "15"
indexed_chars: "71807"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T03:12:25"
---

# Scale-Bridging in Three-Dimensional Fracture Networks: Characterizing the Effects of Variable Fracture Apertures on Network-Scale Flow Channelization.

## One-line Summary

通过将实验室测量的真实裂缝孔径变异性纳入三维离散裂缝网络模拟，量化了微观尺度的孔径变化如何显著重塑网络尺度的流动沟槽化程度、溶质运移时间及活跃表面积 [Hyman 2021, pp. 1-1, 2-3]。

## Research Question

微观尺度的裂缝内部孔径变异性如何影响宏观网络尺度的流动与溶质运移行为，特别是其是否及如何改变流动场组织和流动沟槽化程度 [Hyman 2021, pp. 1-2]。

## Study Area / Data

- **实验样品**：Marcellus页岩，取自美国宾夕法尼亚州 Bedford 的“原样”露头 [Hyman 2021, pp. 2-3]。
- **实验方法**：利用三轴直剪系统在真实地应力条件下制造剪切裂缝，并耦合实时X射线成像技术测量裂缝孔径 [Hyman 2021, pp. 1-1, 2-3]。
- **模拟基础**：离散裂缝网络的参数宽松地基于在 Marcellus 页岩中观测到的天然裂缝带，但网络本身不代表某个特定场地 [Hyman 2021, pp. 3-5]。

## Methods

1.  **实验室数据获取**：在 Marcellus 页岩样品中制造剪切裂缝，使用三轴直剪设备在真实地应力条件下，并通过实时X射线显微断层成像测量裂缝的机械孔径分布，获得具有非均质性的孔径场 [Hyman 2021, pp. 1-1, 2-3, 3-5]。
2.  **离散裂缝网络生成**：使用 `dfnWorks` 模拟套件生成10个独立的微尺度三维离散裂缝网络，每个网络的尺寸在厘米级立方体内。网络由三个裂缝族组成，其方向与笛卡尔坐标轴对齐（基于Fisher分布，参数为100）。所有裂缝为边长均匀且位置随机分布的方形，以隔离孔径变异性影响 [Hyman 2021, pp. 3-5, 5-6]。
3.  **孔径场映射**：将实验获得的非均质孔径场随机旋转、反射后，投影到网络中的每一个裂缝面上，使得每个裂缝都有独特且基于真实观测的可变孔径分布。裂缝间或交叉处的孔径独立不相关 [Hyman 2021, pp. 2-3, 5-6]。
4.  **流动与运移模拟**：
    - 计算不可压缩、等温流体的稳态压力场和体积流率，通过施加Dirichlet边界条件（压差）实现 [Hyman 2021, pp. 5-6]。
    - 使用粒子追踪方法模拟纯平流（无分子扩散）条件下的溶质运移。粒子初始位置按通量加权分配，在裂缝交叉点采用完全混合规则 [Hyman 2021, pp. 6-7]。
5.  **对比组设置**：生成一个具有恒定孔径的网络（孔径值为 \(2.2 \times 10^{-4}\) m，介于孔径场的几何平均和算术平均之间）作为参考案例 [Hyman 2021, pp. 5-6]。

## Key Findings

- **网络尺度流场重组**：局部裂缝内的孔径变异性能产生尺度桥梁效应，改变网络尺度的流场组织。流动拓扑图显示，优先流路径在可变孔径网络中发生根本性改变，小孔径区域会阻塞某些主要通道 [Hyman 2021, pp. 7-8]。
- **溶质运移行为改变**：
  - 与恒定孔径网络相比，可变孔径网络中粒子首次到达时间更早，突破曲线峰值更低，且幂律拖尾的衰减速率更慢（衰减指数由约2.6变为约2.3），表明溶质运移的离散度显著增大 [Hyman 2021, pp. 7-8]。
  - 粒子路径线的平均曲折度增加，在某些网络中增长超过50%，这主要由网络尺度流场重组导致，而非单一的平面内效应 [Hyman 2021, pp. 8-9]。
- **流动沟槽化加剧与活跃表面积减小**：
  - 可变孔径网络的流动沟槽化程度（相对于恒定孔径网络）显著增加 [Hyman 2021, pp. 2-3]。
  - 活跃表面积（存在显著流动的区域比例）在大多数情况下减少超过50%，且其分布比恒定孔径网络更集中且数值更低 [Hyman 2021, pp. 8-9]。

## Core Evidence Table

| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 局部裂缝孔径变异性改变了网络尺度的流场组织，一个小孔径区域即可阻塞主要通道 | [Hyman 2021, pp. 7-8] | 基于流动拓扑图（FTG）可视化 | 代表110个样本的观察结果 |
| 可变孔径网络突破曲线拖尾衰减指数为 \( \psi(\tau) \propto \tau^{-2.3} \)，慢于恒定网络的 \( \psi(\tau) \propto \tau^{-2.6} \) | [Hyman 2021, pp. 7-8] | 时间由恒定网络首次到达时间归一化 | 95%置信区间不重叠，差异显著 |
| 可变孔径网络的活跃表面积大多数情况下减少超过50% | [Hyman 2021, pp. 8-9] | 与恒定孔径网络对比，基于额外生成的90个恒定孔径网络样本 | 可变孔径网络活跃表面积分布更集中且更低 |
| 部分网络中粒子平均路径线长度增加50%以上 | [Hyman 2021, pp. 8-9] | 曲折度增加主要由网络尺度流场重组引起 | - |

## Limitations

未从索引片段中确认。

## Assumptions / Conditions

- **量化流动沟槽化程度**：使用恒定孔径的参考案例作为比较基线 [Hyman 2021, pp. 2-3, 5-6]。
- **粒子运移**：模拟中溶质粒子为纯平流，不考虑分子扩散 [Hyman 2021, pp. 6-7]。
- **流体**：流体视为不可压缩、等温流体 [Hyman 2021, pp. 5-6]。
- **孔径与渗透率关系**：直接使用机械孔径（mechanical aperture）作为水力孔径（hydraulic aperture） [Hyman 2021, pp. 5-6]。
- **裂缝网络构造**：为隔离孔径影响，所有裂缝尺寸统一，方向接近正交 [Hyman 2021, pp. 3-5]。
- **边界条件**：通过施加压差（Dirichlet边界条件）驱动流动 [Hyman 2021, pp. 5-6]。

## Key Variables / Parameters

- **微观裂缝特征**：孔径场，变异系数（0.59），相关长度（≈ \(3 \times 10^{-4}\) m） [Hyman 2021, pp. 3-5]。
- **网络特征**：裂缝边长（\(2 \times 10^{-3}\) m），恒定参考孔径值（\(2.2 \times 10^{-4}\) m） [Hyman 2021, pp. 3-5, 5-6]。
- **流动运移指标**：流动拓扑图（FTG），突破曲线（BTC）及其幂律衰减指数，粒子曲折度（tortuosity），活跃表面积（active surface area）比例，流动沟槽化（flow channelization）程度 [Hyman 2021, pp. 6-7]。

## Reusable Claims

- 将单个裂缝中观察到的真实孔径变异性（如通过X射线成像获得）投影至网络模拟中，可导致网络尺度流动结构的重组，而不仅仅是局部效应的叠加 [Hyman 2021, pp. 2-3, 7-8]。**条件**：裂缝网络中存在显著的微观孔径变异；**证据**：流动拓扑图显示优先路径改变，粒子曲折度增加超50%。
- 在具有微观非均质孔径的裂缝网络中，以平流为主的溶质运移会呈现出比平滑平行板模型假设下更早的首次到达时间和更慢的拖尾衰减 [Hyman 2021, pp. 7-8]。**条件**：微观孔径变异性显著；**证据**：突破曲线拖尾指数由约2.6减至约2.3，且置信区间不重叠。
- 考虑内部孔径变异会显著减少裂缝网络的活跃流动表面积（可减少超50%），并加剧流动的沟槽化 [Hyman 2021, pp. 2-3, 8-9]。**条件**：与使用等效平滑裂缝的网络模型对比；**证据**：可变孔径网络的活跃表面积分布整体低于常孔径网络。

## Candidate Concepts

- [[flow channelization]]
- [[discrete fracture network]]
- [[fracture aperture variability]]
- [[scale-bridging effect]]
- [[breakthrough curve tailing]]
- [[active surface area]]
- [[particle tortuosity]]
- [[flow topology graph]]

## Candidate Methods

- [[triaxial direct-shear with real-time X-ray imaging]]
- [[DFN simulation with dfnWorks]]
- [[aperture field projection]]
- [[steady-state flow simulation]]
- [[advective particle tracking]]
- [[flux-weighted injection]]
- [[complete mixing rule at fracture intersections]]

## Connections To Other Work

- **流动沟槽化与活跃表面积**：与 [[Maillot et al., 2016]] 和 [[Hyman et al., 2020]] 关于活跃表面积定义与作用的研究直接关联 [Hyman 2021, pp. 1-2, 8-9]。
- **粒子追踪与通用DFN方法**：采用了 [[Frampton & Cvetkovic, 2009]] 的通量加权法、[[Berkowitz et al., 1994]], [[Kang et al., 2015]], [[Stockman et al., 1997]] 等研究的完全混合规则，以及 [[Hyman, Rajaram, et al., 2019]] 和 [[Makedonska et al., 2015]] 的粒子追踪方法 [Hyman 2021, pp. 6-7]。
- **先前孔径-运移关系研究背景**：将具有统计代表性的孔径场纳入DFN的先前工作，如 [[de Dreuzy et al., 2012]], [[Frampton et al., 2019]], [[Huang et al., 2019]], [[Karra et al., 2015]], [[Zou & Cvetkovic, 2020]] [Hyman 2021, pp. 1-2]。
- **页岩水力行为背景**：研究动机涉及页岩层中的水力传导特性及其对 [[unconventional hydrocarbon production]] 和断层损伤带渗透率变化的影响 [Hyman 2021, pp. 3-5]。

## Open Questions

- 未从索引片段中确认。

## Source Coverage

本页内容基于15个索引片段，覆盖了论文摘要、引言、方法（实验与模拟）、部分结果和讨论。覆盖相对均衡，侧重于证据和核心发现。部分结果中的非主要指标（如流动拓扑图的更多细节）和补充信息（Supporting Information）中提供的方法细节缺失。讨论与结论部分的具体推断未完整覆盖。
