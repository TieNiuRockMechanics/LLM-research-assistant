---
type: "paper"
schema_version: "paper-v2-2026-04-28"
paper_id: "2020-sherman-characterizing-the-influence-of-fracture-density-on-network-scale-transport"
title: "Characterizing the Influence of Fracture Density on Network Scale Transport."
status: "draft"
source_pdf: "data/papers/2020 - Characterizing the Influence of Fracture Density on Network Scale Transport.pdf"
collections:
citation: "Sherman, Thomas, et al. \"Characterizing the Influence of Fracture Density on Network Scale Transport.\" *Journal of Geophysical Research: Solid Earth*, vol. 125, 2020, e2019JB018547, doi:10.1029/2019JB018547."
indexed_texts: "19"
indexed_chars: "91800"
compiled_model: "deepseek/deepseek-v4-pro"
compiled_at: "2026-04-30T00:17:59"
---

# Characterizing the Influence of Fracture Density on Network Scale Transport.

## One-line Summary
通过生成不同密度的三维离散裂缝网络并模拟流动与保守溶质传输，该研究发现裂缝密度降低会增强溶质在大裂缝中的通道化、增加网络尺度平均迂曲度，并使局部逆压梯度速度区对穿透曲线尾部延迟作用更明显；基于这些观察，提出从迂曲度‑速度联合分布采样的升尺度伯努利空间马尔可夫模型，比使用固定迂曲度值显著提升了传输预测能力 [Sherman 2020, pp. 1-2, pp. 9-10]。

## Research Question
裂缝网络密度如何影响从单裂缝到网络尺度上的流动结构、速度分布、溶质通道化程度以及有效迂曲度？局部拓扑特征（如逆主流方向的速度区）的作用如何随密度变化？如何将局部拓扑影响纳入升尺度随机游走模型，使其更好地预测宏观传输行为 [Sherman 2020, pp. 1-2, pp. 2-2]？

## Study Area / Data
本研究基于合成裂缝网络，无特定野外研究区。网络由随机放置的平面圆盘构成，裂缝半径服从上下限分别为 1 m 和 10 m、幂律指数 α\=1.8 的截断幂律分布 [Sherman 2020, pp. 4-4]。模拟域为边长 50 m 的立方体，通过施加 1 MPa 的 x 方向压差驱动流动，侧向边界为无流动条件 [Sherman 2020, pp. 5-6]。所使用的离散裂缝网络模型 `dfnWorks` 完全解析网络拓扑，并基于拉格朗日粒子跟踪法模拟保守溶质羽流的纯平流传输 [Sherman 2020, pp. 4-4, pp. 5-5]。

## Methods
- **网络生成与表征**：使用 `dfnWorks` 中的 `FRAM` 生成不同密度的裂缝网络（P3、P5、P10，对应无量纲密度）；移除不连接入流‑出流边界的裂缝后保留有效网络 [Sherman 2020, pp. 4-4]。采用图论方法构建裂缝网络拓扑图，以裂缝度为 d（每个裂缝的交点数）量化局部连通性 [Sherman 2020, pp. 4-5]。
- **流动模拟**：假设裂缝内为斯托克斯流，无基质交换，利用达西定律和质量守恒得到的椭圆方程 ∇·(b³∇P)=0 求解稳态压力场，其中 b 为裂缝孔径（随裂缝变化）；使用 `pflotran` 的有限体积法数值积分，并重建速度场 [Sherman 2020, pp. 5-6]。
- **传输模拟**：通过通量加权注入条件释放纯平流保守溶质粒子，采用 `walkabout` 粒子追踪算法模拟粒子轨迹 [Sherman 2020, pp. 5-6]。
- **迂曲度定义**：定义流依赖的有效迂曲度 χ\=λ/Δl，其中 λ 为粒子在两控制面间的总旅行距离，Δl 为沿流动方向的直线距离；并引入总迂曲度 χ50,0 和渐近欧拉迂曲度 χ∞ [Sherman 2020, pp. 6-6, pp. 7-9]。
- **升尺度模型**：构建伯努利空间马尔可夫随机游走模型，其跃迁速度从局部迂曲度与速度的联合分布采样，并与使用固定迂曲度值的传统方法对比 [Sherman 2020, pp. 1-2, pp. 2-4]。

## Key Findings
1. **通道化随密度降低而增强**：在稀疏网络（P3）中，溶质被主要大裂缝构成的优先通道输运，羽流扩展减小；而在高密度网络（P10）中，流动更加均匀，通道化减弱，这由流动通道化密度指标 d<sub>Q</sub>/P<sub>32</sub> 随密度增大而减小所证实 [Sherman 2020, pp. 1-2, pp. 6-7]。
2. **平均旅行距离与迂曲度**：出口处平均有效迂曲度从 P3 网络的 2.21 降至 P5 的 1.98 和 P10 的 1.62，同时渐近欧拉迂曲度也从 2.7 降至 1.6，表明高密度网络中流动路径更直接；最大局部有效迂曲度分别为 140、150 和 51，而最大总迂曲度仅为 5.2、4.8、3.2，凸显局部拓扑的剧烈影响 [Sherman 2020, pp. 7-9, pp. 9-10]。
3. **负速度区的作用**：在低密度网络中，逆主压力梯度方向的速度区（“负速度区”）能捕获大量粒子（例如某 P3 实现中约 18% 的粒子在特定窗口内 χ>10），导致传输延迟和穿透曲线尾部的加重；随密度增加，粒子因更多交叉点而更易逃离这类区域，其影响减弱 [Sherman 2020, pp. 7-9, pp. 9-10]。
4. **升尺度建模的改进**：在伯努利空间马尔可夫模型中，从迂曲度分布采样代替固定迂曲度值能更好地再现高保真 DFN 模拟结果，说明必须细致考虑局部拓扑特征才能实现有效的升尺度 [Sherman 2020, pp. 1-2]。

## Core Evidence Table
| Evidence | Source | Conditions | Notes |
|----------|--------|------------|-------|
| 出口平均有效迂曲度：P3 为 2.21，P5 为 1.98，P10 为 1.62 | [Sherman 2020, pp. 7-9] | 50 m 域，Δl 取 2% 域长，三次密度各多实现平均 | 置信区间见图 3 |
| 渐近欧拉迂曲度 χ∞：P3 为 2.7，P5 为 2.1，P10 为 1.6 | [Sherman 2020, pp. 7-9] | 欧拉统计在远离入口处收敛 | 密度的增加使渐近值接近 Lagrangian 值 |
| 最大局部有效迂曲度：P3 为 140，P5 为 150，P10 为 51；最大总迂曲度 χ50,0 分别为 5.2、4.8、3.2 | [Sherman 2020, pp. 9-10] | 局部窗口 Δl 固定，总迂曲度为全程平均值 | 局部极值远大于总迂曲度，显示局部拓扑影响 |
| d<sub>Q</sub>/P<sub>32</sub> 随网络密度增加而增大 | [Sherman 2020, pp. 6-7] | α=1.8，半径 1‑10 m，域 50 m | 流动通道化程度降低，网络更均匀 |
| 平均裂缝度 d̄ 从 P3 的低值增至 P10 的接近 30 | [Sherman 2020, pp. 4-5, Table 1] | 无量纲密度 P′ 分别为 3、5、10 | 高密度网络连通性好，流动不受拓扑强约束 |
| 使用迂曲度分布采样的伯努利模型优于固定迂曲度模型 | [Sherman 2020, pp. 1-2] | 升尺度预测对比高保真 DFN 模拟 | 具体拟合优度指标未从片段中确认 |

## Limitations
- 研究仅考虑了三种无量纲密度（P3、P5、P10）和单一的幂律半径指数（α=1.8），对其他裂缝几何分布和水力属性（如孔径‑半径关系）的敏感性未从索引片段中确认。
- 流动被简化为斯托克斯流且忽略基质‑裂缝物质交换，可能不完全适用于强惯性效应或基质渗透性不可忽略的系统。
- 传输仅模拟纯平流保守溶质，未包括扩散、吸附或反应过程，这些在实际地下环境中可能显著影响宏观行为。
- 升尺度伯努利模型的验证仅以高保真 DFN 为基准，其在实际现场数据上的表现尚未在片段中提及。

## Assumptions / Conditions
- 裂缝为平面圆盘，半径 r 服从式 (1) 的截断幂律分布，指数 α=1.8，下限 r0=1 m，上限 ru=10 m [Sherman 2020, pp. 4-4]。
- 裂缝孔径 b 通过未在片段中给出的关系 (2) 与半径相关（通常假定 b ∝ r^γ），且单裂缝内孔径均匀 [Sherman 2020, pp. 5-5]。
- 裂缝网络已移除不连接入流‑出流边界的孤立裂缝，仅保留对流动有贡献的部分 [Sherman 2020, pp. 4-4]。
- 流体为水，雷诺数 Re < O(1)，流动处于斯托克斯区，可采用达西方程 [Sherman 2020, pp. 5-6]。
- 基质不可渗透，裂缝与基质间无流体或溶质交换 [Sherman 2020, pp. 5-6]。
- 传输为纯平流，溶质保守，粒子初位置按通量加权注入 [Sherman 2020, pp. 5-6]。
- 模拟域为 50 m 立方体，进出口施加 1 MPa 压差，其余边界无流 [Sherman 2020, pp. 5-6]。

## Key Variables / Parameters
- 无量纲网络密度 P′（3, 5, 10）或每体积裂缝数
- 裂缝度 d 及平均裂缝度 d̄
- 比表面积密度 P<sub>32</sub>*
- 流动通道化密度指标 d<sub>Q</sub> 及比值 d<sub>Q</sub>/P<sub>32</sub>
- 有效迂曲度 χ、总迂曲度 χ50,0、渐近欧拉迂曲度 χ∞
- 局部速度 v 及其 Eulerian PDF ψe(v)、通量加权 Lagrangian PDF ψl(v) 和 ̂ψ𝓁(v)
- 幂律半径指数 α（固定为 1.8）、半径上下限 r0、ru
- 孔径 b（与裂缝尺寸相关，具体形式未确认）
- 域尺寸 L = 50 m，压差 ΔP = 1 MPa
- 粒子轨迹和旅行时间统计（未给出具体泛函形式）

## Reusable Claims
1. 在幂律半径指数 α=1.8、半径 1–10 m 的合成裂缝网络中，当无量纲密度从 P3 增至 P10 时，出口平面上的平均有效迂曲度从 2.21 降至 1.62，表明增加裂缝密度使流动路径更直接；该结论基于 50 m 域内多网络实现的拉格朗日统计 [Sherman 2020, pp. 7-9]。**限制**：结果依赖于特定幂律分布和孔径‑半径关系（此处未具体说明），不保证在其他分布下成立。
2. 稀疏网络（如 P3）中的局部有效迂曲度可达 140 以上，且约 18% 的粒子在某些窗口经历 >10 的迂曲度，从而导致穿透曲线尾部加重；在高密度网络（P10）中此类极端迂曲度显著减少，表明局部逆流区的影响随密度增加而减弱 [Sherman 2020, pp. 9-10]。**限制**：定量比例来自单次实现的观察，代表性需要更多实现验证。
3. 采用从局部迂曲度‑速度联合分布采样的伯努利空间马尔可夫模型比使用固定迂曲度值更能准确重现高保真 DFN 的传输结果，这为在升尺度模型中纳入拓扑异质性提供了参数化路线 [Sherman 2020, pp. 1-2]。**限制**：模型适用范围（如是否对不同边界条件、幂律指数通用）未从片段中确认。

## Candidate Concepts
- [[fracture density]]
- [[tortuosity]] (有效迂曲度、总迂曲度)
- [[discrete fracture network]] (DFN)
- [[channeling]]
- [[negative velocity zones]]
- [[velocity distribution]]
- [[graph-based connectivity]]
- [[Lagrangian particle tracking]]
- [[spatial Markov process]]
- [[Bernoulli model]]
- [[upscaled transport model]]

## Candidate Methods
- [[dfnWorks]]（包含 FRAM、LaGriT、pflotran、walkabout）
- [[flux-weighted particle injection]]
- [[graph-theoretic network characterization]]
- [[continuous time random walk (CTRW)]]
- [[time domain random walk]]
- [[Bernoulli spatial Markov model with tortuosity-velocity joint distribution]]
- [[effective tortuosity measurement]]

## Connections To Other Work
- 本文的升尺度建模思路显式建立在连续时间随机游走（CTRW）和时域随机游走的框架之上 [Sherman 2020, pp. 2-2]，因此与 [[CTRW]]、[[spatial Markov model]] 及相关参数化方法直接关联。
- 裂缝网络拓扑的图论表征方法引用自 [[Hyman et al., 2018]] 等，该方法可应用于其他离散裂缝网络研究。
- 对通道化和速度相关性的讨论与 [[Kang, Le Borgne et al., 2015]]、[[Sherman et al., 2019]] 等关于裂缝网络中拉格朗日加速和速度持续性的工作相呼应，可形成关于 [[flow channeling in fracture networks]] 的研究联系。
- 流动通道化指标 d<sub>Q</sub> 出自 [[Maillot et al., 2016]]，可用于比较不同 DFN 研究中的 flow channeling degree。

## Open Questions
- 当幂律半径指数 α 变化、或孔径‑半径关系不同时，密度对迂曲度和通道化的影响是否保持相似趋势？未从索引片段中确认。
- 本文的升尺度伯努利模型依赖于从完整 DFN 模拟中提取的迂曲度‑速度联合分布，如何从更易获取的网络几何统计（如裂缝度分布）先验地估计该分布仍是一个开放问题。
- 局部负速度区的形成、大小与网络密度、裂缝交叉角等几何属性的定量关系未在片段中深入讨论。
- 若考虑溶质扩散或吸附作用，密度对传输行为的影响是否会改变，特别是低密度网络中滞留效应是否会进一步加强？未在片段中涉及。

## Source Coverage
本知识页依据索引片段 19 段中的部分内容撰写，主要覆盖了摘要、数值方法概述（网络生成、流动与传输模拟、迂曲度定义）、以及部分结果（网络连通性、速度分布、迂曲度统计和空间演变）。所引用的具体量化证据均来自第 1‑2、4‑7、9‑10 页。**未包括的信息**：完整的网络属性表（Table 1、Table 2 的具体数值）、孔径‑半径关系 (2)、连续性方程的具体形式、粒子追踪的完整统计定义、伯努利模型的详细实现和验证指标、讨论与结论部分的分析，以及可能出现的敏感性研究。因此，本页对参数化的细节和模型性能的定量比较可能缺失，建议在获取全文后补充。
