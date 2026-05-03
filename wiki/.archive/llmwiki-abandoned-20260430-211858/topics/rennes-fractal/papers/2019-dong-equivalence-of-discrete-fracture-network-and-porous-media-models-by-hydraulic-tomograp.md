---
type: "paper"
paper_id: "2019-dong-equivalence-of-discrete-fracture-network-and-porous-media-models-by-hydraulic-tomograp"
title: "Equivalence of Discrete Fracture Network and Porous Media Models by Hydraulic Tomography."
status: "draft"
source_pdf: "data/papers/2019 - Equivalence of Discrete Fracture Network and Porous Media Models by Hydraulic Tomography.pdf"
citation: "Dong, Yanhui, et al. \"Equivalence of Discrete Fracture Network and Porous Media Models by Hydraulic Tomography.\" *Water Resources Research*, 2019, doi:10.1029/2018WR024290."
indexed_texts: "14"
indexed_chars: "65786"
compiled_at: "2026-04-27T19:39:32"
---

# Equivalence of Discrete Fracture Network and Porous Media Models by Hydraulic Tomography.

## One-line Summary

该研究通过水力层析成像（HT）结合等效多孔介质（EPM）模型反演离散裂缝网络（DFN）模型生成的合成水力测试数据，发现当DFN存在空间代表性单元体积（REV）时，HT-EPM方法可以满意地预测全场水头；反之，在稀疏DFN中只能捕捉大尺度主导裂缝 [Dong, 2019, pp. 1-1, 1-2]。

## Research Question

水力层析成像（HT）在使用等效多孔介质（EPM）模型时，能否有效表征裂缝岩石中的离散裂缝网络（DFN）？其预测能力与裂缝网络的空间代表性单元体积（REV）有何关系？（研究动机来自：现有HT研究多采用EPM模型，可能未能充分捕捉裂缝的离散本质，因而HT性能可能被高估 [Dong, 2019, p. 1-1]）

## Study Area / Data

未从索引片段中确认实际野外场地。研究采用合成的二维DFN模型，域大小为1000 m × 1000 m × 1 m（厚度可忽略，视为二维模型）[Dong, 2019, pp. 3-4]。共建立三个随机DFN模型（A、B、C），裂缝密度依次递增：模型A、B、C中Set1和Set2的总裂缝数分别为200、500、1000 [Dong, 2019, p. 4]。所有模型包含两组小裂缝（Set1和Set2）和两个断层（F1、F2），几何与水力参数固定（见表1，p. 5）[Dong, 2019, pp. 4-5]。裂缝中心位置采用Enhanced Baecher模型依据泊松过程生成 [Dong, 2019, p. 4]。模型边界为无通量边界，初始水头均匀为100 m，未包含基质 [Dong, 2019, p. 5]。

## Methods

1. **DFN正向模拟**：使用FracMan软件生成裂缝，MAFIC程序计算裂隙中水头分布，流动假设为层流，方程使用裂隙储水性和传导性 [Dong, 2019, pp. 4-5]。
2. **HT反演（EPM模型）**：采用同时连续线性估计器（SimSLE）算法，同时利用所有注水/抽水测试数据进行水力传导系数（K）和储水率（Ss）的估计，并给出不确定性 [Dong, 2019, p. 5]；反演模型假设连续地质介质（EPM-异质模型）[Dong, 2019, p. 7]。
3. **验证实验**：使用HT估计的K和Ss场预测独立（未用于反演）的DFN模型注射测试的水头响应，评估预测能力 [Dong, 2019, p. 1-1, p. 8-10]。
4. **空间REV定义**：定义了整个DFN主导区域的裂缝连通概率的空间REV，以此判断DFN与EPM是否等效 [Dong, 2019, p. 1-1]。

## Key Findings

- 对于高强度裂缝网络（模型C，总裂缝数1000），HT-EPM方法能够较好地估计K和Ss，验证中大部分水头对接近1:1线，预测满意；此时DFN接近多孔介质，信息采样更充分 [Dong, 2019, pp. 7-8]。
- 对于低强度裂缝网络（模型A，200条裂缝），HT-EPM捕捉了不同裂缝簇的水头响应差异，但估计的Ss场出现反常高值（高K区域对应高Ss），反映了EPM假设与DFN离散本质的差异 [Dong, 2019, pp. 5-7]。
- 对于中等强度（模型B），HT-EPM未能产生足够低渗透率区域以隔离未连通井 [Dong, 2019, p. 7]。
- 若DFN具有空间REV（如模型C），则EPM模型可预测全场水头；若为稀疏DFN无此REV，HT-EPM只能捕捉大尺度主导裂缝 [Dong, 2019, pp. 1-1, 1-2]。
- 估计的K和Ss场是条件有效参数场，而非DFN的真实参数，但其能再现所有注水试验期间的水头过程线 [Dong, 2019, p. 8-10]。

## Limitations

- 研究仅考虑二维DFN模型，未涉及三维情况 [Dong, 2019, p. 4]。
- DFN模型中未包含基质，而真实岩石中基质与裂缝共存 [Dong, 2019, p. 5]。
- 反演模型（EPM）假设连续介质，对于稀疏DFN预测能力有限 [Dong, 2019, p. 7]。
- 估计的Ss值出现反常（高K区域对应高Ss），源于EPM模型对离散裂缝的平滑等效 [Dong, 2019, pp. 5-7, 8-10]。
- 几何参数（如裂缝方位、尺寸）的影响未被研究，仅关注裂缝密度 [Dong, 2019, p. 4]。

## Reusable Claims

- “如果 DFN 存在空间 REV，则 DFN 与 EPM 等效，HT-EPM 方法能对整个 DFN 域内的水头场进行满意预测；反之，对于无空间 REV 的稀疏 DFN，HT-EPM 只能识别大尺度主导裂缝。” [Dong, 2019, pp. 1-1, 1-2]
- “HT 估计的 K 和 Ss 是条件有效参数场，它们能再现所有注水试验期间的水头观测值，但并非 DFN 的真实参数值。” [Dong, 2019, pp. 8-10]
- “EPM 模型估计的 Ss 场在高渗透率区域出现异常高值，这源自连续介质假设与裂缝离散存储行为的矛盾。” [Dong, 2019, pp. 5-7]

## Candidate Concepts

- [[discrete fracture network (DFN)]]
- [[equivalent porous media (EPM)]]
- [[hydraulic tomography (HT)]]
- [[representative elementary volume (REV)]]
- [[Simultaneous Successive Linear Estimator (SimSLE)]]
- [[conditional effective parameter fields]]
- [[dual porosity model]]
- [[dual permeability model]]

## Candidate Methods

- [[FracMan]]
- [[MAFIC]]
- [[Enhanced Baecher Model]]
- [[Simultaneous Successive Linear Estimator]]
- [[VSAFT2]]（SimSLE的代码载体，未在片段中明确命名，但推断为用于EPM反演的程序）

## Open Questions

- 如何在实际应用中可靠地判断DFN是否具有空间REV？是否有定量准则？（未从索引片段中确认）
- 当DFN中存在基质时，HT-EPM方法是否仍有效？如何扩展？（未从索引片段中确认）
- 三维DFN模型的HT-EPM等效性是否与二维结论一致？（未从索引片段中确认）

## Source Coverage

本页内容基于以下索引片段编写（均为 Dong 等 2019）：pp. 1-1, 1-2, 2-3, 3-4, 4-5, 5-7, 7-8, 8-10。
