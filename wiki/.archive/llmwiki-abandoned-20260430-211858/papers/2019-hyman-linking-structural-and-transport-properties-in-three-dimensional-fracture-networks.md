---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2019-hyman-linking-structural-and-transport-properties-in-three-dimensional-fracture-networks"
title: "Linking Structural and Transport Properties in Three-Dimensional Fracture Networks."
status: "draft"
source_pdf: "data/papers/2019 - Linking Structural and Transport Properties in Three-Dimensional Fracture Networks.pdf"
collections:
citation: "Hyman, J. D., et al. \"Linking Structural and Transport Properties in Three-Dimensional Fracture Networks.\" *Journal of Geophysical Research: Solid Earth*, vol. 124, 2019, pp. 1185–1204. doi:10.1029/2018JB016553."
indexed_texts: "18"
indexed_chars: "87894"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-29T23:23:32"
---

# Linking Structural and Transport Properties in Three-Dimensional Fracture Networks.

## One-line Summary
通过直接数值模拟，该研究揭示了具有相同裂隙强度但不同幂律长度分布的三维裂隙网络在拓扑结构、流动特性和溶质穿透行为上的差异，并评估了两种平均输运模型（流管模型和伯努利连续时间随机游走模型）的预测能力 [Hyman 2019, pp. 1-2]。

## Research Question
如何将稀疏三维离散裂隙网络的结构特性（特别是幂律长度分布指数所控制的拓扑结构）与输运特性（如溶质穿透曲线）联系起来？哪些平均输运模型能够捕捉这种联系，并直接利用网络结构信息进行合理预测？ [Hyman 2019, pp. 1-2]。

## Study Area / Data
研究基于三个合成、非周期的三维离散裂隙网络（DFN）。域为边长为 \(100 r_0\) 的立方体（\(r_0\) 为最小裂隙半径），裂隙为圆盘形，中心位置和取向均为均匀随机分布。裂隙半径 \(r\) 服从截断幂律分布，其概率密度函数为：
\[
p_r(r) = \frac{\alpha}{r_0} \frac{(r/r_0)^{-1-\alpha}}{1 - (r_u/r_0)^{-\alpha}}
\]
其中 \(\alpha\) 为幂律指数，\(r_0\) 和 \(r_u\) 分别为半径的下限和上限 [Hyman 2019, pp. 2-4]。三个网络分别采用 \(\alpha = 1.6\)（网络 1）、\(\alpha = 2.2\)（网络 2）和 \(\alpha = 2.6\)（网络 3）。所有网络具有相同的裂隙强度 \(P_{32}\)（单位体积内的裂隙表面积），但因指数不同而具有截然不同的逾渗密度 \(p^*\) 和拓扑结构 [Hyman 2019, pp. 2-4, 4-5]。各网络的 \(p^*\) 均远大于逾渗阈值，确保存在从流入到流出边界的贯通路径 [Hyman 2019, pp. 4-5]。

## Methods
- **裂隙网络生成与网格化**：使用 `fram` 生成 DFN，`LaGriT` 生成并行计算网格 [Hyman 2019, pp. 2-4]。
- **流动模拟**：假设稳态、等温、单相流动，裂隙内满足立方律且孔径均匀。忽略基质扩散，施加沿 \(x\) 轴方向的 1 MPa 压差，侧向为无流边界，并不计重力。使用 `pflotran` 数值求解压力场，并由通量重建欧拉速度场 [Hyman 2019, pp. 6-7]。
- **溶质输运模拟**：采用无反应粒子的拉格朗日追踪方法，使用 `walkabout` 确定粒子路径。通过 1,000,000 个粒子生成穿透曲线（BTC），并利用 100,000 个粒子详细记录拉格朗日速度等统计量 [Hyman 2019, pp. 7-8]。
- **拓扑表征**：将网络表示为图（顶点对应裂隙，边对应相交），计算度分布、同配系数，并用 Dijkstra 算法确定流入-流出边界间的最短拓扑路径 [Hyman 2019, pp. 4-6]。
- **平均输运模型**：应用两种模型预测 BTC：随机对流流管模型（streamtube model）和以初始速度分布为条件的伯努利连续时间随机游走（CTRW）模型 [Hyman 2019, pp. 1-2, 7-8]。

## Key Findings
- 尽管三个网络具有相同的 \(P_{32}\)，但幂律指数 \(\alpha\) 越小，长裂隙出现的概率越高，导致更少的裂隙总数、更高的逾渗密度 \(p^*\) 以及更低的平均迂曲度（网络 1：\(\chi_\infty = 1.36\)，网络 2：1.47，网络 3：2.71）[Hyman 2019, pp. 4-5, 8-10]。
- 所有网络的裂隙度分布均呈偏态，表现出无标度网络特性；且同配系数为负值，表明高度裂隙主要连接低度裂隙（大裂隙连接大量小裂隙），网络可视为由枢纽（大裂隙）经小裂隙路径相互连通的系统 [Hyman 2019, pp. 5-6]。
- 最短拓扑路径中的裂隙数从网络 1 的 2 个（存在直接连接流入和流出边界的裂隙）增加到网络 3 的 11 个，反映了随着 \(\alpha\) 增大，粒子必须经历更多次裂隙间过渡 [Hyman 2019, pp. 5-6, 8-10]。
- 流管模型在短距离对网络 1 和 2 提供可接受的预测，但在出口平面均无法准确预测穿透时间，表明粒子运动不能简化为恒定速度 [Hyman 2019, pp. 1-2]。
- 以初始速度分布为条件的伯努利 CTRW 模型，尽管面临较宽的速度分布和较少的独立速度跃迁次数，仍能为不同距离的穿透曲线提供合理的预测，从而将网络结构信息与输运行为更有效地联系起来 [Hyman 2019, pp. 1-2]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|---|---|---|---|
| 网络 1 (\(\alpha=1.6\)) 逾渗密度 \(p^*\) 最高，裂隙数最少；网络 3 (\(\alpha=2.6\)) \(p^*\) 最低，裂隙数最多 | [Hyman 2019, pp. 4-5] | 相同 \(P_{32}\)、固定域尺寸和裂隙半径截断范围 | \(p^*\) 相对于逾渗阈值的恒定度量 |
| 网络 1 渐近迂曲度 \(\chi_\infty = 1.36\)，网络 2 为 1.47，网络 3 为 2.71 | [Hyman 2019, pp. 8-10] | 稳态流动，圆盘形裂隙，立方律 | 高迂曲度与较多短裂隙及更长最短路径相关 |
| 所有网络的度分布呈偏态，同配系数 \(r < 0\)（异配混合） | [Hyman 2019, pp. 5-6] | 图表示方法：顶点=裂隙，边=相交 | 异配意味着大裂隙主要与小裂隙相连 |
| 流管模型在出口平面预测失败，不能以恒定颗粒速度描述输运 | [Hyman 2019, pp. 1-2] | 三维稀疏 DFN，幂律裂隙长度，单相稳态流 | 频繁的速度跃迁是网络结构带来的必然结果 |
| 伯努利 CTRW 模型以初始速度分布为条件能合理预测不同距离的 BTC | [Hyman 2019, pp. 1-2] | 同上，使用 1,000,000 粒子生成 BTC | 该模型提供了结构与输运之间的直接联系 |

## Limitations
- 裂隙网络为合成、均质孔径且无粗糙度的简化模型，未考虑天然裂隙中常见的孔径变异性、充填物及基质扩散作用 [Hyman 2019, pp. 6-7]。
- 流动模拟仅考虑稳态、单相等温条件，忽略重力效应和瞬态效应 [Hyman 2019, pp. 6-7]。
- 网络数量有限（仅三个），且参数选择范围有限，可能不足以全面反映幂律指数变化的影响 [Hyman 2019, pp. 2-4]。
- 未从索引片段中确认对 CTRW 模型参数化细节的敏感性分析或模型在更复杂流动情景（如多相流、反应输运）下的适用性评估。

## Assumptions / Conditions
- 三维离散裂隙网络由圆盘形裂隙组成，裂隙中心位置和取向均为均匀随机分布 [Hyman 2019, pp. 2-4]。
- 裂隙半径服从具有上下限的截断幂律分布，且所有网络具有相同的裂隙强度 \(P_{32}\) [Hyman 2019, pp. 2-4]。
- 流动为稳态、单相、等温，裂隙内满足立方律，孔径在单个裂隙内均匀但裂隙间允许不同 [Hyman 2019, pp. 6-7]。
- 忽略基质扩散、重力以及裂隙壁面粗糙度对流动的影响 [Hyman 2019, pp. 6-7]。
- 溶质为无反应、非吸附的保守示踪剂，输运仅由平流主导 [Hyman 2019, pp. 7-8]。
- 所有网络均满足 \(p^*\) 远大于逾渗阈值，保证存在贯通流动路径 [Hyman 2019, pp. 4-5]。

## Key Variables / Parameters
- 裂隙半径分布幂律指数 \(\alpha\)：取 1.6、2.2、2.6 [Hyman 2019, pp. 2-4]
- 裂隙强度 \(P_{32}\)：三个网络相同，具体值未从索引片段中确认 [Hyman 2019, pp. 1-2]
- 逾渗密度 \(p^*\)：相对于逾渗阈值的无尺度密度 [Hyman 2019, pp. 4-5]
- 度分布及其幂律拟合指数：反映网络无标度特性 [Hyman 2019, pp. 5-6]
- 同配系数 \(r\)：量化度-度相关性的 Pearson 系数 [Hyman 2019, pp. 5-6]
- 最短拓扑路径中的裂隙数：网络 1 为 2，网络 3 为 11 [Hyman 2019, pp. 5-6]
- 迂曲度 \(\chi\)：平均路径长度与直线距离之比，渐近值网络 1 为 1.36，网络 2 为 1.47，网络 3 为 2.71 [Hyman 2019, pp. 8-10]
- 欧拉速度分布和拉格朗日速度分布：用于表征流动非均匀性 [Hyman 2019, pp. 7-8]
- 突破曲线及其尾部标度：非高斯行为指示异常输运 [Hyman 2019, pp. 2-2, 7-8]

## Reusable Claims
1. 在具有相同裂隙强度的三维离散裂隙网络中，幂律长度分布指数越小，网络越倾向于由少量长裂隙主导连通性，其逾渗密度 \(p^*\) 越高、裂隙总数越少、迂曲度越低，且最短路径所含的裂隙过渡次数越少 [Hyman 2019, pp. 4-6, 8-10]。  
   *条件*：网络裂隙为圆盘形，位置和方向均匀随机，裂隙半径服从截断幂律分布，且 \(P_{32}\) 固定，域尺寸与截断半径不变。  
   *证据*：三个网络的对比分析。  
   *限制*：只验证了 \(\alpha = 1.6, 2.2, 2.6\) 三种情况，未推广到其他指数范围。

2. 在幂律长度分布的裂隙网络中，大裂隙（枢纽）通常具有高连接度，且倾向与众多小裂隙相连，形成异配混合的枢纽-路径结构 [Hyman 2019, pp. 5-6]。  
   *条件*：基于图表示法（裂隙为节点，相交为边），且网络内裂隙孔径对连通性无影响。  
   *证据*：度分布偏态与负同配系数。  
   *限制*：结论限于所生成的无标度式网络拓扑，实际野外网络的度分布可能受其他因素影响。

3. 对于此类裂隙网络，基于恒定速度假设的随机流管模型无法准确预测长距离穿透行为，因为颗粒在运移过程中必须经历频繁且不可忽略的速度跃迁 [Hyman 2019, pp. 1-2]。  
   *条件*：稳态流动，无基质扩散，裂隙孔径均匀，幂律长度分布。  
   *证据*：流管模型在出口平面预测失败，而颗粒路径分析表明存在多次裂隙间过渡。  
   *限制*：仅对比了流管模型与伯努利 CTRW，未与其他非恒定速度模型（如分数阶方程）进行直接比较。

4. 伯努利连续时间随机游走模型，仅以颗粒在入口处的初始速度分布作为条件，即可对稀疏三维幂律裂隙网络中的穿透曲线给出合理预测，从而建立了网络结构（控制初始速度分布）与输运行为的直接联系 [Hyman 2019, pp. 1-2]。  
   *条件*：网络满足幂律长度分布且 \(p^*\) 远高于逾渗阈值；流动为稳态立方律流动；颗粒以恒定质量通量注入。  
   *证据*：BTC 预测与直接数值模拟结果吻合（具体定量对比如 \(R^2\) 未在片段中出现）。  
   *限制*：仅基于三个合成网络验证，能否推广到更复杂的孔径分布或存在基质扩散的情况未从索引片段中确认。

## Candidate Concepts
- [[fracture network]]
- [[power-law fracture length distribution]]
- [[breakthrough curve]]
- [[percolation threshold]]
- [[continuous time random walk]]
- [[tortuosity]]
- [[fracture degree distribution]]
- [[assortativity coefficient]]
- [[scale-free network]]
- [[Eulerian velocity field]]
- [[Lagrangian particle tracking]]
- [[streamtube model]]
- [[anomalous transport]]
- [[cubic law fracture flow]]

## Candidate Methods
- [[discrete fracture network generation]]
- [[graph representation of fracture networks]]
- [[Dijkstra’s algorithm for shortest path]]
- [[Bernoulli CTRW model]]
- [[particle tracking simulation]]
- [[finite volume flow solver]]
- [[stochastic convective streamtube model]]
- [[steady-state pressure equation]]

## Connections To Other Work
- 野外试验中常观测到裂隙介质穿透曲线具有幂律尾部，这一非高斯输运行为是本研究的动机之一 [Hyman 2019, pp. 2-2]（引用了 Becker & Shapiro, 2003 等）。本研究结果通过合成网络揭示了这些宏观行为与微观结构的联系。
- 所使用的图表示与拓扑分析方法基于 Hyman et al. (2017) 的框架，其中顶点对应裂隙、边对应相交关系，该图谱可由 Huseby et al. (1997) 的早期工作溯源 [Hyman 2019, pp. 4-5]。
- 逾渗密度 \(p^*\) 的定义和其作为通用网络密度度量的优势在 de Dreuzy et al. (2012) 的工作中有所论证 [Hyman 2019, pp. 4-5]。
- 无标度网络的概念（Albert & Barabási, 2002）被用于解释度分布的偏态特征 [Hyman 2019, pp. 5-6]。
- 迂曲度的渐进关系式引用了 Koponen et al. (1996) 的理论推导 [Hyman 2019, pp. 8-10]。
- 从主题上，该工作可连接到 [[fracture reservoir characterization]]、[[upscaled transport models in fractured media]]、[[network topology and flow]] 等方向，但未从索引片段中确认与其他具体论文的进一步定量比对。

## Open Questions
- 伯努利 CTRW 模型对孔径非均质性、基质扩散或瞬态流动条件的稳健性如何？未从索引片段中确认。
- 除幂律指数外，其他结构参数（如裂隙方向分布的各向异性）如何影响 CTRW 模型的通用性？未从索引片段中确认。
- 所提方法在真实野外裂隙网络（非合成、多尺度）中的应用与验证效果如何？未从索引片段中确认。

## Source Coverage
本页基于该论文的 18 个索引片段编写。片段覆盖了摘要、引言的部分内容、方法概要（DFN 生成、流动模拟、粒子追踪）、基本结果（拓扑性质、迂曲度、模型比较结论），但未包含完整的计算结果、穿透曲线的详细图形、CTRW 模型的具体参数化过程以及讨论部分中关于模型局限性的深入分析。因此，对于 BTC 拟合的定量指标、敏感性分析或与野外数据的对比等关键细节，本页无法提供，标记为“未从索引片段中确认”。
