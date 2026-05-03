---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2023-g-mez-a-non-parametric-discrete-fracture-network-model"
title: "A Non-parametric Discrete Fracture Network Model."
status: "draft"
source_pdf: "data/papers/2023 - A Non-parametric Discrete Fracture Network Model.pdf"
collections:
  - "1文章:2D-3D分形关系"
citation: "Gómez, Santiago, et al. \"A Non-parametric Discrete Fracture Network Model.\" *Rock Mechanics and Rock Engineering*, vol. 56, no. 5, 2023, pp. 3255-3278. doi:10.1007/s00603-022-03194-y."
indexed_texts: "17"
indexed_chars: "84828"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T11:40:28"
---

# A Non-parametric Discrete Fracture Network Model.

## One-line Summary
提出一种基于非参数核密度估计与方向-线性统计的离散裂隙网络模型，用于联合表征裂隙产状与尺寸分布，并在采石场高墙非平面迹线图上取得突出验证结果 [Santiago 2023, pp. 1-2]。

## Research Question
如何在不依赖特定参数分布（如 Fisher 或普通高斯）的情况下，从露头迹线测量中联合、无偏地估计裂隙产状和尺寸（迹长/圆盘直径）的概率密度函数，并生成可重现的三维离散裂隙网络？[Santiago 2023, pp. 3-4]

## Study Area / Data
数据采集自 **12 个采石场台阶高墙面** 的摄影测量模型，这些面均为非平面。研究将 12 个高墙面分为两个数据组 DS1（TM1–TM6）和 DS2（TM7–TM12），DS2 因受到一条断层的影响，其迹线密度和平均 P21 更高（DS1 平均 P21 ≈ 0.72 m⁻¹，DS2 ≈ 1.23 m⁻¹）。每个面记录了迹线类型（完整、半截断、两端截断）及长度特征（总迹线数 50–267 条不等，平均长度 1.19–3.19 m）[Santiago 2023, pp. 4-6]。

## Methods
1. **方向-线性联合核密度估计 (directional-linear KDE)**  
   将 Garcia-Portugues 等人 (2013) 的定向核密度理论推广到球面与实数线的笛卡尔积上，联合估计产状-迹长的非参数 PDF。定向带宽使用根据数据似然最大点及其 45° 锥域内点计算的 ROT 带宽规则（以避免多峰高估带宽）[Santiago 2023, pp. 6-7]。  
2. **迹长到尺寸的反演**  
   采用基于贝特朗悖论的解，从伪迹长 L 反推圆盘直径 D。通过引入径向距离的均匀性假设（`Λ = R·U(0,1)`），建立 L 与 D 的关系：`L = D√(1-U²(0,1))`，并证明其与 Warburton 的迹长方差关系及贝特朗悖论第三解的一致性 [Santiago 2023, pp. 7-10]。对截断偏倚，用含截断概率 P 的混合随机变量 `Ξ = D·Ψ` 修正不完整迹线 [Santiago 2023, pp. 10-11]。  
3. **采样偏差校正**  
   在核密度采样中采用权重函数修正产状与尺寸偏差；采用随机优化算法解决阈值截断（小于截断长度的迹线未记录）带来的系统误差 [Santiago 2023, pp. 1-2, 10-11]。  
4. **DFN 生成**  
   基元为平坦圆形（用正三十边形近似）；空间位置服从均匀泊松-布尔点过程，强度 P30 通过与实测面密度 P21（单位面积迹长总和）拟合确定；蒙特卡洛采样自定向-线 KDE [Santiago 2023, pp. 4-5, 11]。

## Key Findings
1. 非参数定向-线性 KDE 联合模型能够成功表征多峰产状和尺寸分布，对 12 个采石场面的验证结果 "outstanding" [Santiago 2023, pp. 1-2]。  
2. 通过贝特朗悖论导出的公式 (15) `L = D√(1-U²(0,1))` 与经典瓦伯顿迹长-尺寸关系等价，且自然避免贝特朗悖论在选择上的模糊性 [Santiago 2023, pp. 7-10]。  
3. 半截断迹线在总体迹线中的比例 (P) 对估计影响显著，引入混合变量 `Ξ` 可使尺寸 CDF 相对伪迹长偏大，从而合理补偿截断偏倚 [Santiago 2023, pp. 10-11]。  
4. 定向 ROT 带宽仅在最大似然点周围 45° 锥区内计算，可避免因多峰性使得整体带宽过宽而导致细节丢失，所得边缘定向 KDE 主峰明确 [Santiago 2023, pp. 6-7]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 非参数定向-线性 KDE 联合模型对 12 个非平面高墙面迹线图效果优秀 | [Santiago 2023, pp. 1-2] | 迹线图从摄影测量模型获得；尺寸分布假定为按分片线性累积函数反演 | 模型成功捕捉了多峰产状与迹长联合分布 |
| 公式 `L = D √(1-U²(0,1))` 等价于 Warburton 的迹长-直径理论关系 | [Santiago 2023, pp. 7-10] | 圆盘假设；弦与圆盘中心距的分布为均布 | 该公式同时对 Bertrand 悖论保持一致 |
| 对 TM12 (P=0.18) 的尺寸分布反演显示，圆盘尺寸的累积分布整体大于伪迹长累积分布 | [Santiago 2023, pp. 10-11] | 迹线截断比例为 18%；数值计算基于试验迹长 KDE | 验证截断校正的有效性 |
| 定向 ROT 带宽选取法基于最大似然点 45° 锥域，克服多峰问题 | [Santiago 2023, pp. 6-7] | 仅用于产状数据；带宽以内核规模参数控制 | 确保了定向密度的主峰分辨率 |

## Limitations
- 模型假设裂隙均为平坦圆形（正三十边形近似），且产状与尺寸独立；形状和依附关系未从索引片段中确认是否可推广至其他几何假设 [Santiago 2023, pp. 4, 6]。  
- 定向带宽的计算局限于最大似然点附近 45°，可能导致次要产状集中区的带宽非最优；对高度弥散产状的样本适用性未从索引片段中确认 [Santiago 2023, pp. 6-7]。  
- 非参数方法的计算负担虽被称为“优于传统参数模型”，但具体时间或可扩展性数字未从索引片段中确认 [Santiago 2023, pp. 1-2]。

## Assumptions / Conditions
1. 裂隙个体相互独立，形状为平坦圆形，且可以独立泊松-布尔过程分布 [Santiago 2023, pp. 4-5]。  
2. 产状（球面）和尺寸（迹长/直径）的联合密度估计假设样本独立同分布 [Santiago 2023, pp. 6]。  
3. 迹线截断比 (P) 为已知或可估计常数，且足够描述半截断迹线的混合分布 [Santiago 2023, pp. 10-11]。  
4. 定向核密度中，似然最大值附近单峰足够表征该主峰带宽，以确保 ROT 规则对多峰数据的稳健性 [Santiago 2023, pp. 6-7]。  
5. P30 的点估计通过与实验 P21 拟合间接确定 [Santiago 2023, pp. 4-5]。

## Key Variables / Parameters
- **P30**：单位体积内的裂隙中心数 (m⁻³)  
- **P21**：单位面积上的迹长总和 (m⁻¹)，用作 P30 的拟合目标  
- **P32**：单位体积内的裂隙总面积 (m⁻¹)  
- **h**：定向带宽（标量）  
- **h₋ROT₋**：基于最大似然点 45° 锥域的规则化定向带宽 [Santiago 2023, pp. 6-7]  
- **g**：线性带宽（迹长域）  
- **L (完整迹长随机变量)**，**↕ (不完整迹长随机变量)**，**D (圆盘直径随机变量)**  
- **Ξ = D·Ψ**：纠正截断的混合随机变量，其中 Ψ 的密度从 KDE 和已知截断比例 P 求出 [Santiago 2023, pp. 10-11]  
- **Y = L / D**，分布函数 f_Y(y) = y/√(1-y²), y∈[0,1] [Santiago 2023, pp. 9-10]  
- **定向平滑器 K_L** 和 **线性平滑器 K_Z**  
- **截断概率 P**（半截断迹线占总迹线比例）

## Reusable Claims
1. **Claim：定向-线性 KDE 可以无分布假设地联合表征裂隙产状-迹长的 PDF。**  
   条件：有从高墙面或露头提取的迹线长度和产状样本；迹线索采样随机且可加权重修正偏差；截断和尺寸-产状独立性得到处理。证据：在 12 个非平面采石场面上验证成功 [Santiago 2023, pp. 1-2]。限制：需确定合适的定向带宽（如本文主峰 45° 法则）和线性带宽。

2. **Claim：公式 `L = D √(1-U²(0,1))` 给出在圆形裂隙假设下完整伪迹长与圆盘直径的随机关系，并与经典的 Warburton 形式等价，同时避开贝特朗悖论。**  
   条件：裂隙为平面各向同性取向的扁平圆盘；弦距圆心的径向距离服从均匀分布（即贝特朗 3 型）。证据：本文给出了解析证明 [Santiago 2023, pp. 7-10]。限制：若圆盘假设不成立（如真实裂隙形状为非圆形），此关系需修正。

3. **Claim：半截断迹线可用混合随机变量 Ξ = D·Ψ 校正，Ψ 的密度由迹线 KDE、截断比值 P 和理论尺寸-迹长关系联立数值解出，从而使 CDF 合理向大尺寸偏移。**  
   条件：迹线至少有一端为可见截断；P 已知或可被准确估计；采用的迹线长度分布仍是 KDE。证据：对 TM12（P=0.18）计算的尺寸 CDF 始终大于迹线 CDF（图6） [Santiago 2023, pp. 10-11]。限制：P 必须独立准确测量。

## Candidate Concepts
- [[fracture reservoir]]  
- [[discrete fracture network (DFN)]]  
- [[non-parametric KDE]]  
- [[directional-linear statistics]]  
- [[Bertrand paradox]]  
- [[trace length bias correction]]  
- [[Poisson-Boolean point process]]  
- [[censored data in discontinuity survey]]  
- [[photogrammetric fracture mapping]]

## Candidate Methods
- [[directional-linear kernel density estimation]]  
- [[ROT bandwidth selection on sphere]]  
- [[trace-to-size inversion using Bertrand solutions]]  
- [[mixed random variable for censored data correction]]  
- [[Monte Carlo sampling from non-parametric joint distributions]]  
- [[P30 fitting by P21 matching]]  
- [[triangulated surface-disk intersection (Moller 1998)]]

## Connections To Other Work
- 关于离散裂隙网络建模中的产状-尺寸联合估计：作者指出非参数联合估计几近空白。已有面向非参数产状分析的工作（如 Xu 和 Dowd 2010）[Santiago 2023, pp. 3-4]。未从索引片段中确认与具体论文有系统性对比验证。  
- 迹长—尺寸关系的经典基础：本工作建立在 Warburton (1980b) 以及 Tonon 和 Chen (2007) 的综述框架上，提供了非参数对应版本 [Santiago 2023, pp. 3-4, 7-10]。  
- 空间点过程：沿用 Baecher 等人的泊松-布尔模型，未对比其他更复杂点过程（如 Cox、Levy-Lee、Gibbs 过程）的实施效果 [Santiago 2023, pp. 4-5]。候选连接概念：[[stochastic point process models for fractures]]。

## Open Questions
- 非参数带宽选择在多峰且弥散较大的产状数据中，能否在不损失次要模式的情况下制定更普适的策略？[Santiago 2023, pp. 6-7]  
- 方向-线性联合 KDE 对非圆形、非平面裂隙形态的推广是否可能，其理论推导需如何修正？未从索引片段中确认。  
- 该方法在三维高分辨率大范围裂隙网络（如几公里级岩体）的扩展性和计算成本仍不明确 [Santiago 2023, pp. 1-2]。

## Source Coverage
本页依据该论文的 17 条索引片段，覆盖了摘要、引言、方法描述、变量列表、研究区数据、部分结果（图 6 和产状 KDE 结果）和主要结论。证据多偏向模型构造、关键公式和基本验证；未获得的完整内容可能包括：详细的优化算法伪代码、全面敏感性分析、所有 12 面尺寸反演的汇总统计、与传统参数模型的对比结果及其讨论。
