---
type: "paper"
paper_id: "2021-hyman-scale-bridging-in-three-dimensional-fracture-networks-characterizing-the-effects-of-v"
title: "Scale-Bridging in Three-Dimensional Fracture Networks: Characterizing the Effects of Variable Fracture Apertures on Network-Scale Flow Channelization."
status: "draft"
source_pdf: "data/papers/2021 - Scale-Bridging in Three-Dimensional Fracture Networks Characterizing the Effects of Variable Fracture Apertures on Network-Scale Flow Channelization.pdf"
citation: "Hyman, Jeffrey D., et al. \"Scale-Bridging in Three-Dimensional Fracture Networks: Characterizing the Effects of Variable Fracture Apertures on Network-Scale Flow Channelization.\" *Geophysical Research Letters*, vol. 48, no. 12, 2021."
indexed_texts: "15"
indexed_chars: "71807"
compiled_at: "2026-04-27T19:43:41"
---

# Scale-Bridging in Three-Dimensional Fracture Networks: Characterizing the Effects of Variable Fracture Apertures on Network-Scale Flow Channelization.

## One-line Summary

通过将实验室测量的真实裂缝开度变异性投影到三维离散裂缝网络（DFN）模拟中，发现微尺度开度变化不仅影响单裂缝内流场，而且能够重新组织网络尺度的流场结构，显著增强流动通道化、降低活跃表面积并改变溶质传输时间分布 [Hyman 2021, pp. 1-2, pp. 2-3]。

## Research Question

微尺度裂缝开度变异性（即裂缝内部开度非均匀性）如何影响网络宏观尺度的流动与传输行为？此前该问题尚未得到明确回答，已有研究多使用统计模型描述开度场，而缺乏基于真实观测的系统模拟 [Hyman 2021, pp. 1-2]。

## Study Area / Data

实验数据来自对马塞勒斯页岩（Marcellus shale）露头样品的直接剪切测试，使用三轴直剪系统结合实时X射线成像在原位应力条件下测量剪切裂缝的开度场 [Hyman 2021, pp. 2-3]。DFN模拟参数松散基于马塞勒斯页岩中的天然裂缝观测数据（如Gale等 2014；Kavousi等 2017等），但网络不代表任何特定场地 [Hyman 2021, pp. 3-5]。

## Methods

1. **实验室实验**：在圆柱形马塞勒斯页岩样品上制造剪切裂缝，采集三维X射线显微断层扫描图像，通过图像处理获得开度场（平均值33.0 μm，标准差19.7 μm，变异系数0.59，相关长度≈3.4×10⁻⁵ m）[Hyman 2021, pp. 3-5]。
2. **DFN 模拟**：使用 dfnWorks 建模套件生成10个独立的三维微观DFN，每个位于厘米立方体内。每个网络由3个裂缝组组成，平均取向与笛卡尔轴对齐（Fisher分布参数κ=100），裂缝均为方形，边长3.2×10⁻³ m，位置均匀分布 [Hyman 2021, pp. 3-5]。
3. **开度投影**：每条裂缝采用符合Delaunay三角剖分网格（边长为50 μm，与实验层析分辨率一致）。将实验集成开度场的不同区域随机旋转、反射后投影到每条裂缝上，每条裂缝具有唯一且可变的开度分布；开度在裂缝间独立，不跨交叉面相关 [Hyman 2021, pp. 5-6]。共生成10个变开度版本 × 10个网络 = 100个变开度模拟，另建立10个常开度（2.2×10⁻⁴ m）网络作为对照 [Hyman 2021, pp. 5-6]。
4. **流动与传输模拟**：应用Dirichlet压力边界条件求解稳态不可压缩等温流体压力场与体积流量 [Hyman 2021, pp. 5-6]。使用纯对流示踪粒子（无分子扩散）进行粒子追踪，每个网络注入100,000个粒子，初始位置采用通量加权，裂缝交叉口采用完全混合规则 [Hyman 2021, pp. 6-7]。
5. **观测指标**：包括流拓扑图（FTG）、首次穿透时间分布（突破曲线）、粒子曲折度、活跃表面积及相对于常开度情况的流动通道化程度 [Hyman 2021, pp. 6-7]。

## Key Findings

1. **局部开度变异具有尺度关联效应**：单个裂缝内的开度变化可重新组织整个网络尺度的流场结构，表现为流拓扑图中节点与边的重新分布 [Hyman 2021, pp. 7-8]。
2. **突破曲线差异显著**：变开度网络中粒子首次到达时间更早，突破曲线峰值更低，拖尾衰减幂律指数更慢（ψ(τ) ∝ τ⁻²·³ vs 常开度ψ(τ) ∝ τ⁻²·⁶），两集合置信区间不重叠，说明差异不能由网络间变异性解释 [Hyman 2021, pp. 7-8]。
3. **粒子路径长度增加**：变开度网络中路径长度均值在某些样本中增加50%以上，这些增加主要源于网络流场重组而非裂缝内的局部弯曲 [Hyman 2021, pp. 8-9]。
4. **活跃表面积显著减少**：变开度网络的活跃表面积（有显著流动的区域占总表面积比例）分布更集中且值更低，在多数情形下活跃表面积减少超过50% [Hyman 2021, pp. 8-9]。
5. **流动通道化程度增加**：与常开度参考网络相比，变开度网络的流动通道化程度明显升高 [Hyman 2021, pp. 2-3]。

## Limitations

- 模拟仅在小尺度（厘米立方）上进行，但作者预期观察到的模式在更大尺度也会出现，只是开度变化比例相应增大 [Hyman 2021, pp. 2-3]。
- 研究中直接使用机械开度作为水力开度，未区别两者差异 [Hyman 2021, pp. 5-6]。
- 裂缝开度独立分配，不跨交叉面相关 [Hyman 2021, pp. 5-6]；此假设是否影响真实网络行为未从索引片段中确认。
- 其他潜在的局限性（如忽略分子扩散、所用裂缝几何简化等）未从索引片段中确认。

## Reusable Claims

- [Hyman 2021, pp. 7-8] “local aperture variability within individual fractures can have a scale-bridging effect and modify the network-scale flow field organization.” ——单裂缝内的开度变异性可产生尺度关联效应，改变网络尺度流场组织。
- [Hyman 2021, pp. 8-9] “In most cases the active surface area decreased by over 50%” ——引入可变开度使网络活跃表面积减少超过50%。
- [Hyman 2021, pp. 7-8] 变开度网络的突破曲线幂律衰减指数约为-2.3，显著慢于常开度网络的-2.6，且置信区间不重叠，表明差异具有统计显著性。
- [Hyman 2021, pp. 2-3] 研究者预计这些厘米尺度模式可迁移至现场尺度，只是比例上开度变化更大。

## Candidate Concepts

- [[fracture aperture variability]]
- [[flow channelization]]
- [[discrete fracture network (DFN)]]
- [[Marcellus shale]]
- [[dfnWorks]]
- [[flow topology graph (FTG)]]
- [[particle tracking]]
- [[breakthrough curve]]
- [[power-law tailing]]
- [[active surface area]]
- [[scale bridging]]

## Candidate Methods

- [[triaxial direct-shear system]]
- [[X-ray microtomography aperture mapping]]
- [[DFN construction with Fisher distribution]]
- [[Delaunay triangulation meshing]]
- [[flux-weighted particle insertion]]
- [[complete mixing at fracture intersections]]
- [[flow topology graph (FTG) analysis]]

## Open Questions

- 实验观察到的尺度关联模式在更大现场尺度（如千米级裂缝网络）中是否依然成立？需要哪些调整？[未从索引片段中确认]
- 裂缝开度场在交叉面处的相关性如何影响网络尺度结果？[未从索引片段中确认]
- 不同岩石类型（如碳酸盐岩、花岗岩）中类似机制是否产生相同效应？[未从索引片段中确认]

## Source Coverage

- [Hyman 2021, pp. 1-2] 研究背景、问题提出、主要结论概述。
- [Hyman 2021, pp. 2-3] 实验与模拟的总体发现、尺度外推预期。
- [Hyman 2021, pp. 3-5] 实验方法、DFN参数设置。
- [Hyman 2021, pp. 5-6] 开度投影、网格划分、流动控制方程。
- [Hyman 2021, pp. 6-7] 流拓扑图定义、粒子追踪方法、观测指标。
- [Hyman 2021, pp. 7-8] 突破曲线对比、置信区间、幂律指数。
- [Hyman 2021, pp. 8-9] 粒子路径长度、活跃表面积、通道化程度。
