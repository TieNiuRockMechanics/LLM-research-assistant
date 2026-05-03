---
type: "paper"
paper_id: "1980-witherspoon-validity-of-cubic-law-for-fluid-flow-in-a-deformable-rock-fracture"
title: "Validity of Cubic Law for Fluid Flow in a Deformable Rock Fracture."
status: "draft"
source_pdf: "data/papers/1980 - Validity of Cubic Law for fluid flow in a deformable rock fracture.pdf"
citation: "Witherspoon, P. A., et al. \"Validity of Cubic Law for Fluid Flow in a Deformable Rock Fracture.\" *Water Resources Research*, vol. 16, no. 6, Dec. 1980, pp. 1016-1024."
indexed_texts: "8"
indexed_chars: "39334"
compiled_at: "2026-04-27T19:28:09"
---

# Validity of Cubic Law for Fluid Flow in a Deformable Rock Fracture.

## One-line Summary

该论文通过花岗岩、玄武岩和大理石的人工张裂缝实验，验证了立方定律在可变形岩石裂缝中的有效性，并引入修正因子 f 来量化非理想平行板条件造成的流动偏差 [Witherspoon 1980, pp. 1-1]。

## Research Question

验证立方定律（即层流条件下通过平行平面板开放裂缝的流量 Q 与孔径 2b 的立方成正比）在闭合裂缝（表面接触、孔径在法向应力下减小）中的有效性，并探究岩石类型、应力历史及非理想几何条件对立方定律适用的影响 [Witherspoon 1980, pp. 1-1]。

## Study Area / Data

- **岩石样品**：均质的花岗岩、玄武岩和大理石，取自加利福尼亚采石场，基质渗透率极低可忽略 [Witherspoon 1980, pp. 2-3]。
- **裂缝生成**：使用改进的“巴西”加载方法人工诱导水平张裂缝，裂缝面基本正交于圆柱轴线 [Witherspoon 1980, pp. 2-3]。
- **流动几何**：采用径向流（圆柱样品，直径0.15 m，长0.17-0.21 m，中心孔直径0.022 m）和直线流两种几何 [Witherspoon 1980, pp. 2-3]。
- **实验条件**：室温下使用过滤水，法向应力最大20 MPa，孔径范围从250 μm降至4 μm（最小可达孔径）[Witherspoon 1980, pp. 1-1]。使用Riehle试验机施加轴向载荷，三个LVDT（间隔120°）检测孔径变化，精度0.4 μm [Witherspoon 1980, pp. 2-3]。

## Methods

1. **实验流程**：在加载和卸载循环中测量流量 Q、水头差 Δh 和裂缝变形，记录孔径随应力的非线性变化 [Witherspoon 1980, pp. 3-5]。
2. **残余孔径确定**：通过最小二乘法拟合参数 n 和 2b_r（残余孔径），方程形式为 Q/Δh = C(2b_a + 2b_r)^n，其中 2b_a 为表观孔径，假设 f=1 [Witherspoon 1980, pp. 5-7]。
3. **修正因子拟合**：进一步拟合 f 和 2b_r，最小化目标函数 Σ[log(Q/Δh) - log(C(2b_a+2b_r)^3/f)]^2，得到 f 值在 1.04 至 1.65 之间 [Witherspoon 1980, pp. 7-8]。
4. **数据可视化**：将实验数据与立方定律预测线（f=1 及拟合 f）绘制在同一图中，评估吻合程度 [Witherspoon 1980, pp. 7-8]。

## Key Findings

- 立方定律在开放裂缝和闭合裂缝（表面接触）中均成立，且结果不依赖于岩石类型 [Witherspoon 1980, pp. 1-1]。
- 渗透率唯一由孔径决定，与应力历史无关 [Witherspoon 1980, pp. 1-1]。
- 实际裂缝与理想平行板模型的偏差仅表现为流量表观减小，可通过修正因子 f 纳入立方定律：Q/Δh = C(2b)^3 / f [Witherspoon 1980, pp. 1-1]。
- 实验中 f 值范围为 1.04 到 1.65，且随着循环加载次增加（裂缝更匹配），f 值趋于减小 [Witherspoon 1980, pp. 7-8]。
- 残余孔径（2b_r）的拟合值与通过立方定律直接计算的值接近，验证了模型一致性（见表2）[Witherspoon 1980, pp. 7-8]。
- 径向流数据比直线流数据偏离理想立方定律更大（f 最大值达1.49），可能反映粗糙度在径向流场中的复杂影响 [Witherspoon 1980, pp. 7-8]。
- 闭合裂缝中的流动路径可能由交织的变截面管组成，但整体几何效应仍可由孔径 2b 表征，孔径的微小变化支配流动变化 [Witherspoon 1980, pp. 8-9]。

## Limitations

- **应力条件**：仅研究了法向应力下的裂缝闭合，未涉及剪切变形，而现场通常同时存在法向和剪切变形 [Witherspoon 1980, pp. 8-9]。
- **尺寸效应**：存在潜在尺寸效应，已在不同尺寸岩石样品的渗透率测试中被观察到，需要进一步研究接触面积行为 [Witherspoon 1980, pp. 8-9]。
- **模型简化**：裂缝闭合的物理过程（如接触面积的弹性变形）被理想化，实际流动路径更复杂，需要更多机理性理解 [Witherspoon 1980, pp. 8-9]。
- **未从索引片段中确认其他限制**（如温度、化学效应、多相流等）。

## Reusable Claims

- 在孔径低至 4 μm、法向应力高达 20 MPa 的条件下，立方定律依然有效 [Witherspoon 1980, pp. 1-1]。
- 对于非理想平行板裂缝，使用修正因子 f（1.04–1.65）可将立方定律推广应用 [Witherspoon 1980, pp. 1-1]。
- 裂缝渗透率仅由孔径立方关系决定，应力历史不影响该关系 [Witherspoon 1980, pp. 1-1]。
- 径向流几何下的粗糙度效应比直线流更显著，导致更大的 f 值 [Witherspoon 1980, pp. 7-8]。
- 循环加载可使裂缝面逐渐匹配，降低 f 值 [Witherspoon 1980, pp. 7-8]。

## Candidate Concepts

- [[cubic law]]
- [[fracture aperture]]
- [[residual aperture]]
- [[asperity]]
- [[factor f]]
- [[rock fracture permeability]]
- [[parallel plate model]]
- [[deformable rock fracture]]
- [[contact area in fractures]]

## Candidate Methods

- [[radial flow experiments]]
- [[straight flow experiments]]
- [[Brazilian loading method for tension fracture]]
- [[LVDT aperture measurement]]
- [[least squares fitting for fracture parameters]]
- [[cyclic loading test on fractures]]

## Open Questions

- 法向和剪切变形同时作用下的力学与水力行为如何？ [Witherspoon 1980, pp. 8-9]
- 如何理解裂缝表面变形过程中的实际物理过程及其对流体流动的影响？ [Witherspoon 1980, pp. 8-9]
- 尺寸效应如何影响裂缝水力性质的确定？ [Witherspoon 1980, pp. 8-9]
- 裂缝中接触面积的行为及其对流动路径的几何控制机制是什么？ [Witherspoon 1980, pp. 8-9]

## Source Coverage

- 论文首页及等效定律历史背景：[Witherspoon 1980, pp. 1-1]
- 实验程序与样品制备：[Witherspoon 1980, pp. 2-3]
- 循环加载与变形测量：[Witherspoon 1980, pp. 3-5]
- 残余孔径与参数拟合方法：[Witherspoon 1980, pp. 5-7]
- 修正因子 f 拟合与结果表：[Witherspoon 1980, pp. 7-8]
- 讨论、不足与开放问题：[Witherspoon 1980, pp. 8-9]
- 符号表与参考文献：[Witherspoon 1980, pp. 9-9]
